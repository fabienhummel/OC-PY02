"""
Point d'entrée du programme Books to Scrape.

Ce fichier orchestre le processus ETL :
- Extract : récupération des catégories et extraction des livres ;
- Transform : nettoyage et conversion des données ;
- Load : sauvegarde des données dans un fichier CSV et téléchargement des images.

Navigation dans les menus :
- flèches haut / bas pour naviguer ;
- espace pour cocher dans le second menu ;
- entrée pour valider.
"""

import questionary  # Permet de créer des menus interactifs dans le terminal.
from tqdm import tqdm  # Permet d'afficher une barre de progression.

from books_scraper.extract import (
    extract_book_details,
    extract_book_links_from_category,
    extract_categories,
)
from books_scraper.load import (
    build_image_file_name,
    download_image,
    get_default_csv_path,
    get_images_dir_from_csv_path,
    save_books_to_csv,
)
from books_scraper.logger_config import setup_logger
from books_scraper.transform import transform_book


HOME_URL = "https://books.toscrape.com/index.html"


def choose_extraction_mode():
    """
    Affiche le premier menu de choix.

    L'utilisateur choisit entre :
    - traiter toutes les catégories ;
    - sélectionner manuellement certaines catégories.

    Returns:
        str: Mode choisi par l'utilisateur.
    """
    return questionary.select(
        "Que veux-tu extraire ?",
        choices=[
            "Toutes les catégories",
            "Sélection de catégories",
        ],
    ).ask()


def select_categories(categories):
    """
    Affiche un menu à cases à cocher pour sélectionner les catégories.

    Args:
        categories (dict): Dictionnaire des catégories disponibles.

    Returns:
        dict: Dictionnaire contenant uniquement les catégories sélectionnées.
    """
    selected_choices = questionary.checkbox(
        "Choisis les catégories à traiter :",
        choices=list(categories.keys()),
        instruction=(
            "Utilise les flèches pour naviguer, espace pour cocher, "
            "entrée pour valider"
        ),
    ).ask()

    if not selected_choices:
        return {}

    selected_categories = {}

    for category_name in selected_choices:
        selected_categories[category_name] = categories[category_name]

    return selected_categories


def get_categories_to_process(categories):
    """
    Détermine les catégories à traiter selon le choix utilisateur.

    Args:
        categories (dict): Dictionnaire de toutes les catégories disponibles.

    Returns:
        dict: Dictionnaire des catégories à traiter.
    """
    extraction_mode = choose_extraction_mode()

    if extraction_mode == "Toutes les catégories":
        return categories

    if extraction_mode == "Sélection de catégories":
        return select_categories(categories)

    return {}


def extract_selected_categories(selected_categories, images_dir, logger):
    """
    Extrait les livres détaillés des catégories sélectionnées.

    Les images sont téléchargées pendant l'extraction de chaque livre afin que
    la barre de progression reflète à la fois l'extraction des données et la
    sauvegarde de l'image associée.

    Les erreurs sont capturées catégorie par catégorie et livre par livre.
    Une erreur sur une catégorie ou un livre ne bloque pas forcément
    toute l'extraction.

    Args:
        selected_categories (dict): Catégories à traiter.
        images_dir (Path): Dossier de sauvegarde des images de l'extraction.
        logger (logging.Logger): Logger du programme.

    Returns:
        tuple: Liste de livres transformés, résumé par catégorie
        et résumé du téléchargement des images.
    """
    transformed_books = []
    extraction_summary = {}
    images_summary = {
        "downloaded": 0,
        "failed": 0,
    }

    for category_name, category_url in selected_categories.items():
        print(f"Préparation de la catégorie : {category_name}")
        logger.info("Début extraction catégorie : %s", category_name)

        try:
            book_links = extract_book_links_from_category(
                category_name,
                category_url,
            )
            logger.info(
                "%s livres trouvés dans la catégorie %s",
                len(book_links),
                category_name,
            )

        except Exception as error:
            print(
                "Erreur lors de la préparation de la catégorie : "
                f"{category_name}"
            )
            print("La catégorie est ignorée. Voir le fichier log.")
            logger.exception(
                "Erreur lors de la préparation de la catégorie %s : %s",
                category_name,
                error,
            )
            extraction_summary[category_name] = 0
            continue

        category_books_count = 0

        for book in tqdm(
            book_links,
            desc=f"Extraction {category_name}",
            unit="livre",
        ):
            try:
                book_details = extract_book_details(book)
                transformed_book = transform_book(book_details)

                image_file_name = build_image_file_name(transformed_book)
                image_file_path = images_dir / image_file_name

                if download_image(
                    transformed_book.get("image_url", ""),
                    image_file_path,
                ):
                    images_summary["downloaded"] += 1
                else:
                    images_summary["failed"] += 1

                transformed_books.append(transformed_book)
                category_books_count += 1

            except Exception as error:
                product_page_url = book.get("product_page_url", "URL inconnue")

                images_summary["failed"] += 1
                logger.exception(
                    "Erreur lors de l'extraction du livre %s : %s",
                    product_page_url,
                    error,
                )
                continue

        extraction_summary[category_name] = category_books_count

        logger.info(
            "Fin extraction catégorie %s : %s livres extraits",
            category_name,
            category_books_count,
        )

        print(f"Terminé : {category_books_count} livres extraits")
        print("-" * 80)

    return transformed_books, extraction_summary, images_summary


def display_extraction_summary(extraction_summary, total_books):
    """
    Affiche un résumé propre de l'extraction.

    Args:
        extraction_summary (dict): Nombre de livres extraits par catégorie.
        total_books (int): Nombre total de livres extraits.
    """
    print()
    print("Résumé de l'extraction :")
    print()

    for category_name, books_count in extraction_summary.items():
        print(f"- {category_name} : {books_count} livres")

    print()
    print(f"Total : {total_books} livres extraits")
    print()


def main():
    """
    Point d'entrée principal du programme.

    Cette fonction :
    - configure les logs ;
    - récupère les catégories depuis Books to Scrape ;
    - demande à l'utilisateur quelles catégories traiter ;
    - prépare les chemins de sortie ;
    - extrait les livres détaillés des catégories choisies ;
    - transforme les données extraites ;
    - télécharge les images pendant l'extraction ;
    - sauvegarde les résultats dans un fichier CSV ;
    - affiche un résumé de l'extraction.
    """
    logger, log_file = setup_logger()

    try:
        categories = extract_categories(HOME_URL)
        logger.info("%s catégories récupérées", len(categories))

    except Exception as error:
        print("Impossible de récupérer les catégories.")
        print("Fin du programme. Voir le fichier log pour le détail.")
        logger.exception("Erreur lors de la récupération des catégories : %s", error)
        return

    selected_categories = get_categories_to_process(categories)

    print()
    print(f"Nombre de catégories sélectionnées : {len(selected_categories)}")
    print()

    if not selected_categories:
        print("Aucune catégorie sélectionnée. Fin du programme.")
        logger.warning("Aucune catégorie sélectionnée")
        return

    csv_output_path = get_default_csv_path()
    images_dir = get_images_dir_from_csv_path(csv_output_path)

    transformed_books, extraction_summary, images_summary = extract_selected_categories(
        selected_categories,
        images_dir,
        logger,
    )

    display_extraction_summary(
        extraction_summary,
        total_books=len(transformed_books),
    )

    if not transformed_books:
        print("Aucun livre extrait. Aucun fichier CSV généré.")
        logger.warning("Aucun livre extrait")
        return

    try:
        saved_csv_path = save_books_to_csv(transformed_books, csv_output_path)

        print()
        print("Sauvegarde terminée.")
        print(f"Fichier CSV généré : {saved_csv_path}")
        print(f"Dossier images généré : {images_dir}")
        print(
            "Images téléchargées : "
            f"{images_summary['downloaded']} réussies, "
            f"{images_summary['failed']} en erreur"
        )
        print(f"Fichier log généré : {log_file}")

        logger.info("Fichier CSV généré : %s", saved_csv_path)
        logger.info("Dossier images généré : %s", images_dir)
        logger.info(
            "Images téléchargées : %s réussies, %s en erreur",
            images_summary["downloaded"],
            images_summary["failed"],
        )

    except Exception as error:
        print("Erreur lors de la sauvegarde des données.")
        print("Voir le fichier log pour le détail.")
        logger.exception("Erreur lors de la sauvegarde des données : %s", error)


if __name__ == "__main__":
    main()
