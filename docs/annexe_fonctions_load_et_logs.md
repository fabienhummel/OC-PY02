# Annexe — Fonctions de `load.py` et `logger_config.py`

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Rôle des fichiers

`load.py` contient les fonctions liées à la partie **Load** du pipeline ETL : création des chemins de sortie, écriture des CSV et téléchargement des images.

`logger_config.py` configure le fichier log de l'exécution.

## Fonctions de `load.py`

| Fonction | Utilité |
|---|---|
| `get_default_export_dir(output_dir=None)` | Génère le dossier racine daté d'une extraction. |
| `get_category_slug(category_name)` | Convertit le nom d'une catégorie en nom de dossier ou de fichier propre. |
| `get_category_dir(export_dir, category_name)` | Génère le dossier d'une catégorie dans le dossier d'extraction. |
| `get_category_csv_path(category_dir, category_name)` | Génère le chemin du fichier CSV d'une catégorie. |
| `get_category_images_dir(category_dir)` | Génère le dossier `images/` d'une catégorie. |
| `save_books_to_csv(books, csv_file_path)` | Écrit une liste de livres dans un fichier CSV. |
| `build_image_file_name(book)` | Crée un nom de fichier image lisible à partir de la catégorie, du titre et de l'UPC. |
| `download_image(image_url, image_path)` | Télécharge une image et l'enregistre localement. |

## Fonctions conservées temporairement

| Fonction | Statut |
|---|---|
| `get_default_csv_path()` | Ancienne logique avec un CSV global. Conservée temporairement pour compatibilité. |
| `get_images_dir_from_csv_path(csv_file_path)` | Ancienne logique avec un dossier images global. Conservée temporairement pour compatibilité. |

## Fonction de `logger_config.py`

| Fonction | Utilité |
|---|---|
| `setup_logger()` | Crée le fichier log daté et retourne le logger avec le chemin du log. |

## Organisation générée

Exemple de sortie :

```text
outputs/books_extraction_YYYYMMDD_HHMMSS/
└── fantasy/
    ├── fantasy.csv
    └── images/
```

Avec plusieurs catégories :

```text
outputs/books_extraction_YYYYMMDD_HHMMSS/
├── classics/
│   ├── classics.csv
│   └── images/
└── philosophy/
    ├── philosophy.csv
    └── images/
```

## Utilité dans le pipeline ETL

Ces fonctions correspondent à la phase **Load** : elles organisent les résultats de l'extraction dans des fichiers exploitables et faciles à remettre dans le ZIP final.
