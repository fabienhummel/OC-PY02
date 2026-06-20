"""
Fonctions de chargement pour le projet Books to Scrape.

Ce module contient les fonctions qui permettent de sauvegarder
les données extraites dans des fichiers locaux.

Dans le découpage ETL :
- Extract : récupération des données depuis le HTML ;
- Transform : nettoyage et conversion des données ;
- Load : écriture des données dans un fichier CSV.
"""

import csv  # Permet d'écrire les données dans un fichier CSV.
from datetime import datetime  # Permet de générer une date et une heure.
from pathlib import Path  # Permet de gérer les chemins de fichiers proprement.


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


def ask_csv_output_path():
    """
    Propose un chemin de sauvegarde CSV à l'utilisateur.

    L'utilisateur peut :
    - appuyer sur Entrée pour accepter le chemin proposé ;
    - saisir un autre chemin s'il souhaite un emplacement différent.

    Returns:
        Path: Chemin du fichier CSV à créer.
    """
    default_path = get_default_csv_path()

    print()
    print("Chemin de sauvegarde CSV proposé :")
    print(default_path)

    user_path = input(
        "Appuie sur Entrée pour accepter, "
        "ou saisis un autre chemin de fichier CSV : "
    ).strip()

    if user_path:
        return Path(user_path)

    return default_path


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