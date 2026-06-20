# Annexe — Variables et structures de données

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Rôle de cette annexe

Cette annexe présente les principales variables et structures de données utilisées dans le projet.

## Variables générales

| Variable | Type | Description |
|---|---|---|
| `HOME_URL` | `str` | URL de départ du site Books to Scrape. |
| `CSV_HEADERS` | `list` | Liste des colonnes attendues dans chaque fichier CSV. |
| `LOGGER` | `logging.Logger` | Logger utilisé dans le module d'extraction. |

## Catégories

| Variable | Type | Description |
|---|---|---|
| `categories` | `dict` | Dictionnaire contenant les catégories disponibles. |
| `selected_categories` | `dict` | Dictionnaire contenant uniquement les catégories choisies. |
| `category_name` | `str` | Nom d'une catégorie. |
| `category_url` | `str` | URL complète d'une catégorie. |
| `category_slug` | `str` | Nom technique propre utilisé pour le dossier et le CSV d'une catégorie. |
| `categories_argument` | `str` ou `None` | Valeur reçue avec l'option `--categories`. |

Structure de `categories` :

```python
{
    "Fantasy": "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
    "Travel": "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
}
```

## Livres

| Variable | Type | Description |
|---|---|---|
| `book_links` | `list` | Liste des livres trouvés dans une catégorie, avec titre et URL. |
| `book` | `dict` | Dictionnaire représentant un livre. |
| `book_details` | `dict` | Données détaillées brutes extraites depuis la page produit. |
| `transformed_book` | `dict` | Données transformées prêtes pour le CSV. |
| `transformed_books` | `list` | Liste des livres transformés pour une catégorie. |
| `books_by_category` | `dict` | Dictionnaire regroupant les livres transformés par catégorie. |

Structure de base d'un livre trouvé dans une catégorie :

```python
{
    "category": "Fantasy",
    "title": "Unicorn Tracks",
    "product_page_url": "https://books.toscrape.com/catalogue/unicorn-tracks_951/index.html"
}
```

Structure d'un livre transformé :

```python
{
    "product_page_url": "...",
    "universal_product_code": "...",
    "title": "...",
    "price_including_tax": "£51.77",
    "price_excluding_tax": "£51.77",
    "number_available": 22,
    "product_description": "...",
    "category": "Poetry",
    "review_rating": 3,
    "image_url": "..."
}
```

Structure de `books_by_category` :

```python
{
    "Classics": [book1, book2, book3],
    "Philosophy": [book1, book2]
}
```

## Chemins de fichiers

| Variable | Type | Description |
|---|---|---|
| `export_dir` | `Path` | Dossier racine daté de l'extraction. |
| `category_dir` | `Path` | Dossier d'une catégorie dans le dossier d'extraction. |
| `csv_path` | `Path` | Chemin du fichier CSV d'une catégorie. |
| `csv_paths` | `list` | Liste des fichiers CSV générés. |
| `images_dir` | `Path` | Dossier `images/` d'une catégorie. |
| `image_path` | `Path` | Chemin local d'une image. |
| `log_file` | `Path` | Chemin du fichier log. |
| `output_dir` | `str` ou `None` | Dossier de sortie fourni avec `--output`. |

Structure de sortie :

```text
outputs/books_extraction_YYYYMMDD_HHMMSS/
└── fantasy/
    ├── fantasy.csv
    └── images/
```

## Résumés d'exécution

| Variable | Type | Description |
|---|---|---|
| `summary` | `dict` | Nombre de livres extraits par catégorie. |
| `image_summary` | `dict` | Nombre d'images réussies ou en erreur. |
| `count` | `int` | Nombre de livres traités pour une catégorie. |
| `total_books` | `int` | Nombre total de livres extraits pendant l'exécution. |

Structure de `summary` :

```python
{
    "Classics": 19,
    "Philosophy": 11
}
```

Structure de `image_summary` :

```python
{
    "downloaded": 30,
    "failed": 0
}
```

## Arguments de ligne de commande

| Variable | Type | Description |
|---|---|---|
| `args` | `argparse.Namespace` | Arguments saisis au lancement du programme. |
| `args.extract` | `bool` | Indique si le mode extraction est demandé. |
| `args.interactive` | `bool` | Indique si le mode interactif est demandé. |
| `args.list_mode` | `str` ou `None` | Mode de liste demandé : catégories ou livres. |
| `args.detail` | `list` ou `None` | Titres demandés avec `--detail`. Avec `nargs="+"` et `action="append"`, la valeur brute est une liste de listes. |
| `args.quiet` | `bool` | Indique si le mode silencieux est activé. |

Dans `run_cli_mode()`, `args.detail` est aplati dans une liste simple appelée `detail_titles` avant l'appel à `show_details()`.
