"""
Fonctions de transformation pour le projet Books to Scrape.

Ce module contient les fonctions qui nettoient ou convertissent
les données extraites depuis le HTML.

Dans le découpage ETL :
- Extract : récupération des données depuis le HTML ;
- Transform : nettoyage et conversion des données ;
- Load : écriture des données dans un fichier CSV.
"""

import re  # Permet d'extraire un nombre depuis une chaîne de caractères.


def clean_text(text):
    """
    Nettoie un texte en supprimant les espaces inutiles.

    Args:
        text (str): Texte à nettoyer.

    Returns:
        str: Texte nettoyé.
    """
    return " ".join(text.split())


def extract_number_available(availability):
    """
    Extrait le nombre de livres disponibles.

    Exemple :
    "In stock (22 available)" devient 22.

    Args:
        availability (str): Texte de disponibilité extrait du site.

    Returns:
        int: Nombre d'exemplaires disponibles.
    """
    match = re.search(r"\d+", availability)

    if match:
        return int(match.group())

    return 0


def convert_rating_to_number(rating):
    """
    Convertit une note textuelle en nombre.

    Exemple :
    "Three" devient 3.

    Args:
        rating (str): Note brute extraite du HTML.

    Returns:
        int | str: Note convertie, ou chaîne vide si inconnue.
    """
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    return rating_map.get(rating, "")


def transform_book(book):
    """
    Transforme les données brutes d'un livre.

    La fonction prépare les champs finaux attendus pour le CSV.

    Args:
        book (dict): Dictionnaire contenant les données brutes d'un livre.

    Returns:
        dict: Dictionnaire transformé avec les champs attendus.
    """
    transformed_book = {
        "product_page_url": book.get("product_page_url", ""),
        "universal_product_code": book.get("universal_product_code", ""),
        "title": clean_text(book.get("title", "")),
        "price_including_tax": book.get("price_including_tax", ""),
        "price_excluding_tax": book.get("price_excluding_tax", ""),
        "number_available": extract_number_available(
            book.get("availability", "")
        ),
        "product_description": clean_text(
            book.get("product_description", "")
        ),
        "category": clean_text(book.get("category", "")),
        "review_rating": convert_rating_to_number(
            book.get("review_rating", "")
        ),
        "image_url": book.get("image_url", ""),
    }

    return transformed_book


def transform_books(books):
    """
    Transforme une liste de livres.

    Args:
        books (list): Liste de dictionnaires de livres bruts.

    Returns:
        list: Liste de dictionnaires transformés.
    """
    transformed_books = []

    for book in books:
        transformed_books.append(transform_book(book))

    return transformed_books