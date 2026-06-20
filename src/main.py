"""Point d'entrée du programme Books to Scrape.

Modes disponibles :
- sans option : affiche l'aide ;
- --interactive : lance le mode interactif ;
- --extract : lance une extraction non interactive ;
- --list categories : affiche les catégories ;
- --list books : affiche les titres des livres ;
- --detail : affiche les détails d'un ou plusieurs livres.
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

import questionary
from tqdm import tqdm

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


def parse_arguments():
    """Analyse les options passées au lancement du programme."""
    parser = argparse.ArgumentParser(
        description="Scraper Books to Scrape."
    )

    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Lance le mode interactif.",
    )

    parser.add_argument(
        "--extract",
        action="store_true",
        help="Lance une extraction non interactive.",
    )

    parser.add_argument(
        "--categories",
        help=(
            "Catégories séparées par des virgules, "
            "ou all pour toutes les catégories."
        ),
    )

    parser.add_argument(
        "--output",
        help="Dossier de sortie du CSV et du dossier images.",
    )

    parser.add_argument(
        "--list",
        choices=["categories", "books"],
        dest="list_mode",
        help="Liste les catégories ou les titres des livres.",
    )

    parser.add_argument(
        "--detail",
        action="append",
        nargs="+",
        metavar="TITLE",
        help=(
            "Titre exact d'un livre à détailler. "
            "Plusieurs titres peuvent être indiqués après --detail."
        ),
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="N'affiche aucune sortie terminal pendant une extraction.",
    )

    return parser


def validate_arguments(parser, args):
    """Valide les combinaisons d'options autorisées."""
    selected_modes = [
        args.interactive,
        args.extract,
        args.list_mode is not None,
        args.detail is not None,
    ]

    if sum(bool(mode) for mode in selected_modes) > 1:
        parser.error(
            "Choisis un seul mode : --interactive, --extract, --list ou --detail."
        )

    if args.quiet and not args.extract:
        parser.error("--quiet ne peut être utilisé qu'avec --extract.")

    if args.output and not args.extract:
        parser.error("--output ne peut être utilisé qu'avec --extract.")

    if args.extract and not args.categories:
        parser.error("--extract nécessite --categories.")

    if args.list_mode == "books" and not args.categories:
        parser.error("--list books nécessite --categories.")

    if args.list_mode == "categories" and args.categories:
        parser.error("--categories n'est pas utile avec --list categories.")

    if args.categories and not (
        args.extract or args.list_mode == "books" or args.detail
    ):
        parser.error(
            "--categories doit être utilisé avec --extract, --list books "
            "ou --detail."
        )


def choose_interactive_categories(categories):
    """Sélectionne les catégories en mode interactif."""
    mode = questionary.select(
        "Que veux-tu extraire ?",
        choices=[
            "Toutes les catégories",
            "Sélection de catégories",
        ],
    ).ask()

    if mode == "Toutes les catégories":
        return categories

    selected_names = questionary.checkbox(
        "Choisis les catégories à traiter :",
        choices=list(categories.keys()),
        instruction=(
            "flèches pour naviguer, espace pour cocher, "
            "entrée pour valider"
        ),
    ).ask()

    if not selected_names:
        return {}

    return {name: categories[name] for name in selected_names}


def resolve_categories(
    categories,
    categories_argument,
    default_all=False,
    logger=None,
    quiet=False,
):
    """Résout l'argument --categories en dictionnaire de catégories."""
    if not categories_argument:
        if default_all:
            return categories

        return {}

    if categories_argument.casefold() == "all":
        return categories

    selected_categories = {}

    for requested_name in categories_argument.split(","):
        requested_name = requested_name.strip()
        found = False

        for category_name, category_url in categories.items():
            if category_name.casefold() == requested_name.casefold():
                selected_categories[category_name] = category_url
                found = True
                break

        if not found:
            if not quiet:
                print(f"Catégorie inconnue : {requested_name}")

            if logger:
                logger.warning("Catégorie inconnue : %s", requested_name)

    return selected_categories


def build_output_paths(output_dir=None):
    """Construit le chemin du CSV et le dossier images."""
    if output_dir:
        output_path = Path(output_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_path = output_path / f"books_extraction_{timestamp}.csv"
        images_dir = output_path / "images" / csv_path.stem

        return csv_path, images_dir

    csv_path = get_default_csv_path()
    images_dir = get_images_dir_from_csv_path(csv_path)

    return csv_path, images_dir


def print_if_not_quiet(message="", quiet=False):
    """Affiche un message uniquement si le mode quiet est désactivé."""
    if not quiet:
        print(message)


def list_categories(categories):
    """Affiche les catégories disponibles, une par ligne."""
    for category_name in categories:
        print(category_name)


def list_books(categories, categories_argument, logger):
    """Affiche uniquement les titres des livres."""
    selected_categories = resolve_categories(
        categories,
        categories_argument,
        logger=logger,
    )

    if not selected_categories:
        print("Aucune catégorie sélectionnée.")
        print("Exemple : python src/main.py --list books --categories all")
        return

    for category_name, category_url in selected_categories.items():
        try:
            books = extract_book_links_from_category(
                category_name,
                category_url,
            )
        except Exception as error:
            print(f"Erreur de lecture pour la catégorie : {category_name}")
            logger.exception("Erreur catégorie %s : %s", category_name, error)
            continue

        for book in books:
            print(book.get("title", ""))


def print_book_details(book):
    """Affiche les détails d'un livre."""
    print()
    print(f"Titre : {book['title']}")
    print(f"Catégorie : {book['category']}")
    print(f"UPC : {book['universal_product_code']}")
    print(f"Prix TTC : {book['price_including_tax']}")
    print(f"Prix HT : {book['price_excluding_tax']}")
    print(f"Stock disponible : {book['number_available']}")
    print(f"Note : {book['review_rating']}")
    print(f"Image : {book['image_url']}")
    print(f"Description : {book['product_description']}")
    print("-" * 80)


def show_details(categories, titles, categories_argument, logger):
    """Affiche les détails des livres demandés."""
    selected_categories = resolve_categories(
        categories,
        categories_argument,
        default_all=True,
        logger=logger,
    )

    requested_titles = {title.casefold(): title for title in titles}
    found_titles = set()

    for category_name, category_url in selected_categories.items():
        try:
            books = extract_book_links_from_category(
                category_name,
                category_url,
            )
        except Exception as error:
            print(f"Erreur de lecture pour la catégorie : {category_name}")
            logger.exception("Erreur catégorie %s : %s", category_name, error)
            continue

        for book in books:
            title = book.get("title", "")
            title_key = title.casefold()

            if title_key not in requested_titles:
                continue

            try:
                details = extract_book_details(book)
                transformed_book = transform_book(details)
                print_book_details(transformed_book)
                found_titles.add(title_key)

            except Exception as error:
                print(f"Erreur sur le livre : {title}")
                logger.exception("Erreur livre %s : %s", title, error)

    for title_key, requested_title in requested_titles.items():
        if title_key not in found_titles:
            print(f"Livre non trouvé : {requested_title}")


def extract_books(selected_categories, images_dir, logger, quiet=False):
    """Extrait les données, transforme les livres et télécharge les images."""
    transformed_books = []
    summary = {}
    image_summary = {
        "downloaded": 0,
        "failed": 0,
    }

    for category_name, category_url in selected_categories.items():
        print_if_not_quiet(
            f"Préparation de la catégorie : {category_name}",
            quiet,
        )
        logger.info("Début catégorie : %s", category_name)

        try:
            book_links = extract_book_links_from_category(
                category_name,
                category_url,
            )
        except Exception as error:
            print_if_not_quiet(f"Catégorie ignorée : {category_name}", quiet)
            logger.exception("Erreur catégorie %s : %s", category_name, error)
            summary[category_name] = 0
            continue

        count = 0

        for book in tqdm(
            book_links,
            desc=f"Extraction {category_name}",
            unit="livre",
            disable=quiet,
        ):
            try:
                details = extract_book_details(book)
                transformed_book = transform_book(details)

                image_name = build_image_file_name(transformed_book)
                image_path = images_dir / image_name

                if download_image(
                    transformed_book.get("image_url", ""),
                    image_path,
                ):
                    image_summary["downloaded"] += 1
                else:
                    image_summary["failed"] += 1

                transformed_books.append(transformed_book)
                count += 1

            except Exception as error:
                image_summary["failed"] += 1
                logger.exception(
                    "Erreur livre %s : %s",
                    book.get("product_page_url", "URL inconnue"),
                    error,
                )

        summary[category_name] = count
        print_if_not_quiet(f"Terminé : {count} livres extraits", quiet)
        print_if_not_quiet("-" * 80, quiet)

    return transformed_books, summary, image_summary


def print_summary(summary, total):
    """Affiche le résumé de l'extraction."""
    print()
    print("Résumé de l'extraction :")
    print()

    for category_name, count in summary.items():
        print(f"- {category_name} : {count} livres")

    print()
    print(f"Total : {total} livres extraits")
    print()


def run_extraction(selected_categories, output_dir, logger, log_file, quiet=False):
    """Lance l'extraction et sauvegarde les résultats."""
    if not selected_categories:
        print_if_not_quiet(
            "Aucune catégorie sélectionnée. Fin du programme.",
            quiet,
        )
        logger.warning("Aucune catégorie sélectionnée")
        return

    csv_path, images_dir = build_output_paths(output_dir)

    books, summary, image_summary = extract_books(
        selected_categories,
        images_dir,
        logger,
        quiet=quiet,
    )

    if not quiet:
        print_summary(summary, len(books))

    if not books:
        print_if_not_quiet(
            "Aucun livre extrait. Aucun fichier CSV généré.",
            quiet,
        )
        logger.warning("Aucun livre extrait")
        return

    try:
        saved_csv_path = save_books_to_csv(books, csv_path)

        if not quiet:
            print()
            print("Sauvegarde terminée.")
            print(f"Fichier CSV généré : {saved_csv_path}")
            print(f"Dossier images généré : {images_dir}")
            print(
                "Images téléchargées : "
                f"{image_summary['downloaded']} réussies, "
                f"{image_summary['failed']} en erreur"
            )
            print(f"Fichier log généré : {log_file}")

        logger.info("Fichier CSV généré : %s", saved_csv_path)
        logger.info("Dossier images généré : %s", images_dir)
        logger.info(
            "Images téléchargées : %s réussies, %s en erreur",
            image_summary["downloaded"],
            image_summary["failed"],
        )

    except Exception as error:
        print_if_not_quiet("Erreur lors de la sauvegarde des données.", quiet)
        print_if_not_quiet("Voir le fichier log pour le détail.", quiet)
        logger.exception("Erreur sauvegarde : %s", error)


def run_cli_mode(args, categories, logger, log_file):
    """Lance le mode ligne de commande."""
    if args.list_mode == "categories":
        list_categories(categories)
        return

    if args.list_mode == "books":
        list_books(categories, args.categories, logger)
        return

    if args.detail:
        detail_titles = [title for group in args.detail for title in group]
        show_details(categories, detail_titles, args.categories, logger)
        return

    if args.extract:
        selected_categories = resolve_categories(
            categories,
            args.categories,
            logger=logger,
            quiet=args.quiet,
        )

        run_extraction(
            selected_categories,
            args.output,
            logger,
            log_file,
            quiet=args.quiet,
        )


def run_interactive_mode(categories, logger, log_file):
    """Lance le mode interactif."""
    selected_categories = choose_interactive_categories(categories)

    print()
    print(f"Nombre de catégories sélectionnées : {len(selected_categories)}")
    print()

    run_extraction(
        selected_categories,
        output_dir=None,
        logger=logger,
        log_file=log_file,
    )


def main():
    """Configure le programme puis lance le mode adapté."""
    parser = parse_arguments()
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        return

    validate_arguments(parser, args)

    logger, log_file = setup_logger()

    try:
        categories = extract_categories(HOME_URL)
        logger.info("%s catégories récupérées", len(categories))

    except Exception as error:
        if not args.quiet:
            print("Impossible de récupérer les catégories.")
            print("Fin du programme. Voir le fichier log pour le détail.")

        logger.exception("Erreur catégories : %s", error)
        return

    if args.interactive:
        run_interactive_mode(categories, logger, log_file)
    else:
        run_cli_mode(args, categories, logger, log_file)


if __name__ == "__main__":
    main()
