# Documentation développeur — OC-PY02

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel  
**Objectif :** expliquer le fonctionnement interne du programme et le rôle de chaque fichier.

---

## 1. Objectif du programme

Le programme extrait les informations de livres depuis le site Books to Scrape.

Il permet de :

- récupérer les catégories du site ;
- parcourir les livres d'une ou plusieurs catégories ;
- ouvrir chaque page produit ;
- extraire les champs demandés ;
- transformer les données brutes ;
- télécharger les images ;
- générer un fichier CSV par catégorie ;
- organiser les résultats dans un dossier d'extraction daté.

Le programme suit une logique **ETL** :

| Étape | Rôle |
|---|---|
| Extract | Récupérer les données depuis les pages HTML. |
| Transform | Nettoyer et convertir les données extraites. |
| Load | Sauvegarder les CSV et les images. |

---

## 2. Organisation des fichiers

```text
src/
├── main.py
└── books_scraper/
    ├── __init__.py
    ├── extract.py
    ├── transform.py
    ├── load.py
    └── logger_config.py
```

| Fichier | Rôle |
|---|---|
| `main.py` | Point d'entrée du programme et orchestration générale. |
| `extract.py` | Fonctions d'extraction depuis le HTML. |
| `transform.py` | Fonctions de nettoyage et conversion des données. |
| `load.py` | Fonctions de sauvegarde CSV, images et chemins de sortie. |
| `logger_config.py` | Configuration du fichier log. |
| `__init__.py` | Indique que `books_scraper` est un package Python. |

---

## 3. Parcours complet d'une extraction

Commande exemple :

```bash
python src/main.py --extract --categories "Classics,Philosophy"
```

Déroulement simplifié :

```text
main()
→ parse_arguments()
→ validate_arguments()
→ setup_logger()
→ extract_categories()
→ run_cli_mode()
→ resolve_categories()
→ run_extraction()
→ build_export_dir()
→ extract_books()
→ extract_book_links_from_category()
→ extract_book_details()
→ transform_book()
→ download_image()
→ save_category_csv_files()
→ save_books_to_csv()
→ print_summary()
```

---

## 4. Structure des données principales

### Catégories

Les catégories sont stockées dans un dictionnaire :

```python
{
    "Classics": "https://books.toscrape.com/.../classics_6/index.html",
    "Philosophy": "https://books.toscrape.com/.../philosophy_7/index.html"
}
```

### Livre trouvé dans une catégorie

```python
{
    "category": "Fantasy",
    "title": "Unicorn Tracks",
    "product_page_url": "https://books.toscrape.com/catalogue/unicorn-tracks_951/index.html"
}
```

### Livre transformé pour le CSV

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

### Regroupement par catégorie

```python
{
    "Classics": [book1, book2, book3],
    "Philosophy": [book1, book2]
}
```

---

## 5. `main.py` — Orchestration du programme

`main.py` est le point d'entrée du programme. Il ne contient pas directement le détail du scraping HTML : il coordonne les autres modules.

| Fonction | Rôle | Entrée principale | Sortie principale |
|---|---|---|---|
| `parse_arguments()` | Définit les options disponibles en ligne de commande. | Aucune | `parser` |
| `validate_arguments(parser, args)` | Vérifie que les options saisies sont cohérentes. | `parser`, `args` | Aucune, ou erreur contrôlée |
| `choose_interactive_categories(categories)` | Permet de choisir les catégories via un menu interactif. | `categories` | `selected_categories` |
| `resolve_categories(...)` | Transforme `--categories` en dictionnaire exploitable. | `categories`, `categories_argument` | `selected_categories` |
| `build_export_dir(output_dir=None)` | Crée le dossier racine daté de l'extraction. | `output_dir` | `export_dir` |
| `print_if_not_quiet(message, quiet)` | Affiche un message seulement si `quiet` est désactivé. | `message`, `quiet` | Affichage terminal |
| `list_categories(categories)` | Affiche les catégories disponibles. | `categories` | Affichage terminal |
| `list_books(categories, categories_argument, logger)` | Affiche les titres des livres. | Catégories choisies | Affichage terminal |
| `print_book_details(book)` | Affiche les détails d'un livre transformé. | `book` | Affichage terminal |
| `show_details(categories, titles, categories_argument, logger)` | Recherche et affiche les détails d'un ou plusieurs livres. | `titles` | Affichage terminal |
| `extract_books(selected_categories, export_dir, logger, quiet=False)` | Extrait les livres, transforme les données et télécharge les images. | Catégories choisies | `books_by_category`, `summary`, `image_summary` |
| `print_summary(summary, total)` | Affiche le résumé de l'extraction. | `summary`, `total` | Affichage terminal |
| `save_category_csv_files(books_by_category, export_dir, logger)` | Écrit un CSV par catégorie. | `books_by_category` | `csv_paths` |
| `run_extraction(...)` | Lance l'extraction complète et la sauvegarde. | Catégories choisies | Fichiers générés |
| `run_cli_mode(args, categories, logger, log_file)` | Gère le mode ligne de commande. | `args` | Action demandée |
| `run_interactive_mode(categories, logger, log_file)` | Gère le mode interactif. | `categories` | Extraction |
| `main()` | Fonction principale du programme. | Arguments CLI | Exécution du programme |

### Points importants à expliquer

- `main.py` sépare les modes : liste, détail, interaction, extraction.
- `--detail` accepte plusieurs titres grâce à `nargs="+"`.
- `extract_books()` regroupe les livres par catégorie.
- `save_category_csv_files()` crée un CSV par catégorie.
- Le programme continue autant que possible même si un livre ou une catégorie échoue.

---

## 6. `extract.py` — Extraction des données

`extract.py` correspond à la partie **Extract** du pipeline ETL.

| Fonction | Rôle | Entrée principale | Sortie principale |
|---|---|---|---|
| `get_soup(page_url, retries=3, timeout=20)` | Récupère une page web et la transforme en objet BeautifulSoup. | URL | `soup` |
| `extract_categories(home_url)` | Extrait les catégories depuis la page d'accueil. | `HOME_URL` | `categories` |
| `extract_number_of_pages(category_url)` | Récupère le nombre de pages d'une catégorie. | URL catégorie | `int` |
| `build_category_page_url(category_url, page_number)` | Construit l'URL d'une page de catégorie. | URL catégorie, numéro page | URL page |
| `extract_book_links_from_category(category_name, category_url)` | Récupère les livres d'une catégorie. | Catégorie | Liste de livres |
| `extract_product_information_table(soup)` | Extrait le tableau `Product Information`. | `soup` | Dictionnaire |
| `extract_product_description(soup)` | Extrait la description du livre. | `soup` | Texte |
| `extract_product_category(soup, default_category='')` | Extrait la catégorie depuis le fil d'Ariane. | `soup` | Texte |
| `extract_product_rating(soup)` | Extrait la note brute du livre. | `soup` | Texte, par exemple `Three` |
| `extract_product_image_url(soup, product_page_url)` | Extrait l'URL complète de l'image. | `soup`, URL produit | URL image |
| `extract_book_details(book)` | Regroupe toutes les informations détaillées d'un livre. | `book` | Dictionnaire brut |

### Points importants à expliquer

- `requests` récupère le HTML.
- `BeautifulSoup` analyse le HTML.
- `urljoin` transforme les URL relatives en URL complètes.
- `get_soup()` centralise la récupération des pages et la gestion des erreurs réseau.
- `extract_book_details()` assemble les données d'un livre avant transformation.

---

## 7. `transform.py` — Transformation des données

`transform.py` correspond à la partie **Transform** du pipeline ETL.

| Fonction | Rôle | Entrée principale | Sortie principale |
|---|---|---|---|
| `clean_text(text)` | Nettoie un texte extrait du HTML. | Texte brut | Texte nettoyé |
| `extract_number_available(availability)` | Extrait le stock disponible. | Texte de disponibilité | Nombre entier |
| `convert_rating_to_number(rating)` | Convertit une note textuelle en nombre. | `One`, `Two`, etc. | `1`, `2`, etc. |
| `transform_book(book)` | Prépare un livre pour le CSV. | Livre brut | Livre transformé |
| `transform_books(books)` | Transforme une liste de livres. | Liste brute | Liste transformée |

### Exemples

```text
In stock (22 available) → 22
Three → 3
```

### Points importants à expliquer

- Les données extraites du HTML sont souvent textuelles.
- La transformation rend les données plus faciles à exploiter.
- Les prix sont conservés avec la devise d'origine.
- Seuls les champs attendus dans le CSV final sont conservés dans `transform_book()`.

---

## 8. `load.py` — Sauvegarde et organisation des fichiers

`load.py` correspond à la partie **Load** du pipeline ETL.

| Fonction | Rôle | Entrée principale | Sortie principale |
|---|---|---|---|
| `get_default_export_dir(output_dir=None)` | Crée le chemin du dossier d'extraction daté. | `output_dir` | `export_dir` |
| `get_category_slug(category_name)` | Convertit un nom de catégorie en nom de dossier/fichier propre. | Nom catégorie | Slug |
| `get_category_dir(export_dir, category_name)` | Crée le chemin du dossier catégorie. | Export, catégorie | `category_dir` |
| `get_category_csv_path(category_dir, category_name)` | Crée le chemin du CSV de la catégorie. | Dossier catégorie | `csv_path` |
| `get_category_images_dir(category_dir)` | Crée le chemin du dossier images de la catégorie. | Dossier catégorie | `images_dir` |
| `save_books_to_csv(books, csv_file_path)` | Écrit les données dans un CSV. | Livres, chemin CSV | `csv_path` |
| `build_image_file_name(book)` | Crée un nom d'image explicite. | Livre transformé | Nom fichier image |
| `download_image(image_url, image_path)` | Télécharge une image localement. | URL image, chemin local | `True` ou `False` |

### Fonctions conservées temporairement

| Fonction | Rôle actuel |
|---|---|
| `get_default_csv_path()` | Ancienne logique avec un CSV global. Peut être supprimée plus tard si elle n'est plus utilisée. |
| `get_images_dir_from_csv_path()` | Ancienne logique avec un dossier images global. Peut être supprimée plus tard si elle n'est plus utilisée. |

### Points importants à expliquer

- `save_books_to_csv()` utilise `csv.DictWriter`.
- `utf-8-sig` facilite l'ouverture du CSV dans Excel.
- `python-slugify` évite les noms de fichiers problématiques.
- Chaque catégorie possède son propre CSV et son dossier `images/`.

---

## 9. `logger_config.py` — Logs

`logger_config.py` configure la journalisation du programme.

| Fonction | Rôle | Entrée principale | Sortie principale |
|---|---|---|---|
| `setup_logger()` | Crée le dossier `logs/`, configure le logger et prépare un fichier log daté. | Aucune | `logger`, `log_file` |

### Points importants à expliquer

- Les logs permettent de conserver une trace des actions et erreurs.
- Le mode `--quiet` peut limiter l'affichage terminal, mais les logs restent utiles.
- Les erreurs réseau ou erreurs de traitement sont tracées avec `logger.exception()`.

---

## 10. Techniques Python utilisées

| Technique | Utilisation dans le projet |
|---|---|
| Fonctions | Découper le programme en blocs réutilisables. |
| Modules | Séparer `main`, extraction, transformation, sauvegarde et logs. |
| Listes | Stocker les livres d'une catégorie. |
| Dictionnaires | Représenter les catégories, les livres et les résumés. |
| Boucles `for` | Parcourir les catégories, pages et livres. |
| Conditions `if` | Gérer les modes, options et cas particuliers. |
| `try / except` | Gérer les erreurs réseau ou les erreurs sur un livre. |
| Compréhensions | Calculer le total des livres ou aplatir `args.detail`. |
| `argparse` | Créer une interface en ligne de commande. |
| `pathlib.Path` | Manipuler les chemins de fichiers proprement. |
| `csv.DictWriter` | Écrire les dictionnaires de livres dans des CSV. |
| `logging` | Tracer l'exécution et les erreurs. |
| Expressions régulières | Extraire le nombre disponible depuis le texte de disponibilité. |

---

## 11. Points à retenir pour la soutenance

- Le projet est organisé selon une logique ETL.
- `main.py` orchestre, mais ne fait pas tout.
- `extract.py` récupère les données brutes depuis le HTML.
- `transform.py` nettoie et convertit les données.
- `load.py` sauvegarde les CSV et les images.
- Un CSV est généré pour chaque catégorie.
- Les fichiers générés ne sont pas versionnés dans GitHub.
- Le ZIP final doit contenir les données générées et les images, organisées par catégorie.

---

## 12. Chemin de sortie attendu

Exemple :

```text
outputs/books_extraction_YYYYMMDD_HHMMSS/
├── classics/
│   ├── classics.csv
│   └── images/
└── philosophy/
    ├── philosophy.csv
    └── images/
```

Cette structure est simple à expliquer :

```text
1 extraction = 1 dossier daté
1 catégorie = 1 sous-dossier
1 catégorie = 1 CSV
1 catégorie = 1 dossier images
```
