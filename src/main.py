"""
Point d'entrée du programme Books to Scrape.

Ce fichier orchestre l'extraction :
- récupération des catégories ;
- choix entre toutes les catégories ou une sélection manuelle ;
- extraction détaillée des livres pour chaque catégorie choisie.

Navigation dans les menus :
- flèches haut / bas pour naviguer ;
- espace pour cocher dans le second menu ;
- entrée pour valider.
"""

import questionary  # Permet de créer des menus interactifs dans le terminal.

from books_scraper.extract import extract_books_from_category, extract_categories


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


def main():
    """
    Point d'entrée principal du programme.

    Cette fonction :
    - récupère les catégories depuis Books to Scrape ;
    - demande à l'utilisateur quelles catégories traiter ;
    - extrait les livres détaillés des catégories choisies.
    """
    categories = extract_categories(HOME_URL)
    selected_categories = get_categories_to_process(categories)

    print()
    print(f"Nombre de catégories sélectionnées : {len(selected_categories)}")
    print()

    if not selected_categories:
        print("Aucune catégorie sélectionnée. Fin du programme.")
        return

    all_books = []

    for category_name, category_url in selected_categories.items():
        print(f"Extraction de la catégorie : {category_name}")

        books = extract_books_from_category(category_name, category_url)
        all_books.extend(books)

        print(f"{len(books)} livres extraits pour {category_name}")
        print("-" * 80)

    print()
    print(f"Nombre total de livres extraits : {len(all_books)}")
    print()

    for book in all_books:
        print(f"Titre : {book['title']}")
        print(f"Catégorie : {book['category']}")
        print(f"UPC : {book['universal_product_code']}")
        print(f"Prix TTC : {book['price_including_tax']}")
        print(f"Prix HT : {book['price_excluding_tax']}")
        print(f"Disponibilité : {book['availability']}")
        print(f"Note : {book['review_rating']}")
        print(f"Image : {book['image_url']}")
        print("-" * 80)


if __name__ == "__main__":
    main()