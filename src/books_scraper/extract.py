"""
Fonctions d'extraction pour le site Books to Scrape.

Ce module contient uniquement les fonctions qui récupèrent des informations
depuis les pages HTML du site.

Découpage ETL :
- Extract : récupération des données brutes depuis le HTML ;
- Transform : nettoyage et conversion des données dans un autre module ;
- Load : écriture CSV et sauvegarde des fichiers dans un autre module.
"""

import time  # Permet d'attendre entre deux tentatives en cas d'erreur réseau.
from urllib.parse import urljoin  # Transforme une URL relative en URL complète.

import requests  # Récupère le contenu HTML d'une page web.
from bs4 import BeautifulSoup  # Analyse le HTML pour en extraire des éléments.
from requests.exceptions import RequestException  # Capture les erreurs réseau.


def get_soup(page_url, retries=3, timeout=20):
    """
    Récupère une page web et la transforme en objet BeautifulSoup.

    La fonction tente plusieurs fois de récupérer la page en cas d'erreur
    réseau temporaire.

    Args:
        page_url (str): URL de la page à récupérer.
        retries (int): Nombre de tentatives avant abandon.
        timeout (int): Temps maximum d'attente en secondes.

    Returns:
        BeautifulSoup: Objet permettant de rechercher des éléments HTML.

    Raises:
        RequestException: Si la page reste inaccessible après les tentatives.
    """
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(page_url, timeout=timeout)

            # Arrête la tentative si la réponse HTTP est une erreur.
            response.raise_for_status()

            # Force l'encodage UTF-8 pour éviter les problèmes avec le symbole £.
            response.encoding = "utf-8"

            return BeautifulSoup(response.text, "html.parser")

        except RequestException as error:
            last_error = error
            print(
                f"Erreur réseau sur {page_url} "
                f"(tentative {attempt}/{retries})"
            )

            if attempt < retries:
                time.sleep(2)

    raise last_error


def extract_categories(home_url):
    """
    Extrait les catégories depuis la page d'accueil Books to Scrape.

    La catégorie globale "Books" est volontairement ignorée, car elle regroupe
    tous les livres et ne permet pas de produire un CSV par vraie catégorie.

    Args:
        home_url (str): URL de la page d'accueil du site.

    Returns:
        dict: Dictionnaire contenant le nom de la catégorie en clé
        et son URL complète en valeur.
    """
    soup = get_soup(home_url)
    categories = {}

    # Sélectionne les liens des catégories dans la colonne de gauche.
    category_links = soup.select("div.side_categories ul li a")

    for link in category_links:
        category_name = link.get_text(strip=True)
        relative_url = link.get("href")

        if category_name == "Books":
            continue

        if relative_url:
            category_url = urljoin(home_url, relative_url)
            categories[category_name] = category_url

    return categories


def extract_number_of_pages(category_url):
    """
    Extrait le nombre de pages d'une catégorie.

    Exemple de texte trouvé dans le HTML :
    "Page 1 of 3"

    Args:
        category_url (str): URL de la première page de catégorie.

    Returns:
        int: Nombre total de pages pour cette catégorie.
    """
    soup = get_soup(category_url)
    current_page = soup.select_one("li.current")

    if current_page:
        current_page_text = current_page.get_text(strip=True)
        return int(current_page_text.split()[-1])

    # Si aucun bloc de pagination n'existe, la catégorie contient une seule page.
    return 1


def build_category_page_url(category_url, page_number):
    """
    Construit l'URL d'une page de catégorie.

    La première page utilise index.html.
    Les pages suivantes utilisent le format page-2.html, page-3.html, etc.

    Args:
        category_url (str): URL de la première page de catégorie.
        page_number (int): Numéro de la page à construire.

    Returns:
        str: URL complète de la page de catégorie.
    """
    if page_number == 1:
        return category_url

    return category_url.replace(
        "index.html",
        f"page-{page_number}.html",
    )


def extract_book_links_from_category(category_name, category_url):
    """
    Extrait les liens des livres présents dans toutes les pages d'une catégorie.

    Cette fonction récupère seulement les informations nécessaires pour aller
    ensuite consulter chaque page détail :
    - la catégorie ;
    - l'URL de la page produit.

    Args:
        category_name (str): Nom de la catégorie.
        category_url (str): URL de la première page de catégorie.

    Returns:
        list: Liste de dictionnaires contenant category et product_page_url.
    """
    books = []
    nb_page_categories = extract_number_of_pages(category_url)

    for page_number in range(1, nb_page_categories + 1):
        page_url = build_category_page_url(category_url, page_number)
        soup = get_soup(page_url)

        # Chaque livre affiché sur une page de catégorie est dans un article.
        book_cards = soup.select("article.product_pod")

        for book_card in book_cards:
            product_link = book_card.select_one("h3 a")

            if product_link:
                product_relative_url = product_link.get("href", "")
                product_page_url = urljoin(page_url, product_relative_url)

                books.append(
                    {
                        "category": category_name,
                        "product_page_url": product_page_url,
                    }
                )

    return books


def extract_product_information_table(soup):
    """
    Extrait le tableau Product Information d'une page produit.

    Le tableau contient notamment :
    - UPC ;
    - Product Type ;
    - Price excl. tax ;
    - Price incl. tax ;
    - Tax ;
    - Availability ;
    - Number of reviews.

    Args:
        soup (BeautifulSoup): Page produit analysée avec BeautifulSoup.

    Returns:
        dict: Dictionnaire contenant les données du tableau.
    """
    product_information = {}
    rows = soup.select("table.table-striped tr")

    for row in rows:
        header = row.find("th")
        value = row.find("td")

        if header and value:
            key = header.get_text(strip=True)
            product_information[key] = value.get_text(strip=True)

    return product_information


def extract_product_description(soup):
    """
    Extrait la description d'un livre depuis une page produit.

    Sur Books to Scrape, la description se trouve dans le paragraphe
    qui suit le bloc dont l'id est product_description.

    Args:
        soup (BeautifulSoup): Page produit analysée avec BeautifulSoup.

    Returns:
        str: Description du produit, ou chaîne vide si absente.
    """
    description_block = soup.find("div", id="product_description")

    if not description_block:
        return ""

    description_paragraph = description_block.find_next_sibling("p")

    if description_paragraph:
        return description_paragraph.get_text(strip=True)

    return ""


def extract_product_category(soup, default_category=""):
    """
    Extrait la catégorie depuis le fil d'Ariane d'une page produit.

    Si la catégorie n'est pas trouvée dans la page détail, la fonction retourne
    la catégorie déjà connue depuis la page catégorie.

    Args:
        soup (BeautifulSoup): Page produit analysée avec BeautifulSoup.
        default_category (str): Catégorie connue depuis la page catégorie.

    Returns:
        str: Nom de la catégorie.
    """
    breadcrumb_links = soup.select("ul.breadcrumb li a")

    if breadcrumb_links:
        return breadcrumb_links[-1].get_text(strip=True)

    return default_category


def extract_product_rating(soup):
    """
    Extrait la note brute d'un livre depuis la page produit.

    Exemple HTML :
    <p class="star-rating Three">

    La fonction retourne "Three". La conversion en 3 sera faite dans
    le module transform.py.

    Args:
        soup (BeautifulSoup): Page produit analysée avec BeautifulSoup.

    Returns:
        str: Note brute sous forme de texte.
    """
    rating_tag = soup.select_one("p.star-rating")

    if rating_tag:
        rating_classes = rating_tag.get("class", [])

        if rating_classes:
            return rating_classes[-1]

    return ""


def extract_product_image_url(soup, product_page_url):
    """
    Extrait l'URL de l'image depuis une page produit.

    On utilise l'image de la page détail, car elle est plus pertinente que
    la miniature affichée sur les pages de catégorie.

    Args:
        soup (BeautifulSoup): Page produit analysée avec BeautifulSoup.
        product_page_url (str): URL de la page produit.

    Returns:
        str: URL complète de l'image.
    """
    image_tag = soup.select_one("div.item.active img")

    if image_tag:
        image_relative_url = image_tag.get("src", "")
        return urljoin(product_page_url, image_relative_url)

    return ""


def extract_book_details(book):
    """
    Extrait les informations détaillées d'un livre depuis sa page produit.

    Si une information existe à la fois sur la page catégorie et sur la page
    détail, la page détail est prioritaire.

    Args:
        book (dict): Dictionnaire contenant au minimum :
            - category ;
            - product_page_url.

    Returns:
        dict: Dictionnaire contenant les informations détaillées du livre.
    """
    product_page_url = book["product_page_url"]
    soup = get_soup(product_page_url)

    product_information = extract_product_information_table(soup)

    title_tag = soup.find("h1")

    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        title = ""

    product_details = {
        "product_page_url": product_page_url,
        "universal_product_code": product_information.get("UPC", ""),
        "title": title,
        "price_including_tax": product_information.get("Price (incl. tax)", ""),
        "price_excluding_tax": product_information.get("Price (excl. tax)", ""),
        "availability": product_information.get("Availability", ""),
        "product_description": extract_product_description(soup),
        "category": extract_product_category(
            soup,
            default_category=book.get("category", ""),
        ),
        "review_rating": extract_product_rating(soup),
        "image_url": extract_product_image_url(soup, product_page_url),
        "product_type": product_information.get("Product Type", ""),
        "tax": product_information.get("Tax", ""),
        "number_of_reviews": product_information.get("Number of reviews", ""),
    }

    return product_details