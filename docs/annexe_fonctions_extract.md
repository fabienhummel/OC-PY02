# Annexe — Fonctions de `extract.py`

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Rôle du fichier

`extract.py` contient les fonctions chargées de récupérer les informations depuis les pages HTML de Books to Scrape.

Il correspond à la partie **Extract** du processus ETL.

## Fonctions

| Fonction | Utilité |
|---|---|
| `get_soup(page_url, retries=3, timeout=20)` | Récupère une page web, gère les tentatives réseau et retourne un objet BeautifulSoup. |
| `extract_categories(home_url)` | Extrait les catégories du site, en ignorant la catégorie globale `Books`. |
| `extract_number_of_pages(category_url)` | Récupère le nombre de pages d'une catégorie. |
| `build_category_page_url(category_url, page_number)` | Construit l'URL d'une page de catégorie à partir de son numéro. |
| `extract_book_links_from_category(category_name, category_url)` | Extrait les titres et URL des livres présents dans une catégorie. |
| `extract_product_information_table(soup)` | Extrait le tableau `Product Information` d'une page produit. |
| `extract_product_description(soup)` | Extrait la description d'un livre. |
| `extract_product_category(soup, default_category='')` | Extrait la catégorie depuis le fil d'Ariane, avec une valeur de secours. |
| `extract_product_rating(soup)` | Extrait la note brute du livre, par exemple `Three`. |
| `extract_product_image_url(soup, product_page_url)` | Extrait l'URL complète de l'image depuis la page produit. |
| `extract_book_details(book)` | Extrait toutes les informations détaillées d'un livre depuis sa page produit. |

## Données brutes extraites

Les données extraites peuvent encore être brutes, par exemple :

```text
review_rating = Three
availability = In stock (22 available)
price_including_tax = £51.77
```

Ces valeurs sont ensuite préparées dans `transform.py`.

## Points importants

- `requests` récupère les pages HTML.
- `BeautifulSoup` analyse le HTML.
- `urljoin` convertit les URL relatives en URL complètes.
- Les erreurs réseau sont journalisées dans le fichier log.
