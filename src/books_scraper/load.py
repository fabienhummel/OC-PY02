"""
Fonctions de chargement pour le projet Books to Scrape.

Ce module contient les fonctions qui permettent de sauvegarder
les données extraites dans des fichiers locaux.

Dans le découpage ETL :
- Extract : récupération des données depuis le HTML ;
- Transform : nettoyage et conversion des données ;
- Load : écriture des données dans un fichier CSV et sauvegarde des images.
"""

import csv  # Permet d'écrire les données dans un fichier CSV.
from datetime import datetime  # Permet de générer une date et une heure.
from pathlib import Path  # Permet de gérer les chemins de fichiers proprement.

import requests  # Permet de télécharger les images depuis leur URL.
from slugify import slugify  # Permet de créer des noms de fichiers propres.


CSV_HEADERS = [
    "product_page_url",
    "universal_product_code",
    "title",
    "price_including_tax",
    "price_excluding_tax",
    "number_available",
    "product_description",
    "category",
    "review_rating",
    "image_url",
]


def get_default_csv_path():
    """
    Génère un chemin CSV par défaut à partir du dossier courant.

    Le fichier est placé dans le dossier outputs avec un nom contenant
    la date et l'heure de l'extraction.

    Exemple :
    outputs/books_extraction_20260620_153045.csv

    Returns:
        Path: Chemin complet du fichier CSV proposé.
    """
    current_path = Path.cwd()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"books_extraction_{timestamp}.csv"

    return current_path / "outputs" / file_name


def save_books_to_csv(books, csv_file_path):
    """
    Sauvegarde une liste de livres dans un fichier CSV.

    Args:
        books (list): Liste de dictionnaires contenant les données des livres.
        csv_file_path (Path): Chemin du fichier CSV à créer.

    Returns:
        Path: Chemin du fichier CSV créé.
    """
    csv_path = Path(csv_file_path)

    # Crée le dossier parent si nécessaire.
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    with csv_path.open(
        mode="w",
        encoding="utf-8-sig",
        newline="",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=CSV_HEADERS,
            extrasaction="ignore",
        )

        writer.writeheader()

        for book in books:
            writer.writerow(book)

    return csv_path


def get_images_dir_from_csv_path(csv_file_path):
    """
    Génère un dossier images à partir du nom du fichier CSV.

    Exemple :
    outputs/books_extraction_20260620_183000.csv

    devient :
    images/books_extraction_20260620_183000/

    Args:
        csv_file_path (Path): Chemin du fichier CSV généré.

    Returns:
        Path: Dossier de sauvegarde des images pour l'extraction courante.
    """
    csv_path = Path(csv_file_path)
    extraction_name = csv_path.stem

    return Path.cwd() / "images" / extraction_name


def build_image_file_name(book):
    """
    Construit un nom de fichier explicite pour l'image d'un livre.

    Le nom utilise :
    - la catégorie ;
    - le titre ;
    - l'UPC.

    Exemple :
    fantasy_a-light-in-the-attic_a897fe39b1053632.jpg

    Args:
        book (dict): Dictionnaire contenant les données d'un livre.

    Returns:
        str: Nom de fichier image propre.
    """
    category = slugify(book.get("category", "unknown")) or "unknown"
    title = slugify(book.get("title", "unknown-title")) or "unknown-title"
    upc = slugify(book.get("universal_product_code", "unknown-upc"))
    upc = upc or "unknown-upc"

    return f"{category}_{title}_{upc}.jpg"


def download_image(image_url, image_path):
    """
    Télécharge une image et l'enregistre localement.

    Args:
        image_url (str): URL de l'image à télécharger.
        image_path (Path): Chemin local de sauvegarde.

    Returns:
        bool: True si l'image a été téléchargée, False sinon.
    """
    if not image_url:
        return False

    response = requests.get(image_url, timeout=20)
    response.raise_for_status()

    image_path.parent.mkdir(parents=True, exist_ok=True)

    with image_path.open("wb") as image_file:
        image_file.write(response.content)

    return True
