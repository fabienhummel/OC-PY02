# Annexe — Fonctions de `main.py`

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Rôle du fichier

`main.py` est le point d'entrée du programme. Il orchestre l'exécution : lecture des options, choix du mode, extraction, transformation, sauvegarde des CSV par catégorie, téléchargement des images et affichage des résultats.

## Fonctions

| Fonction | Utilité |
|---|---|
| `parse_arguments()` | Définit les options disponibles en ligne de commande, dont `--detail` qui accepte un ou plusieurs titres. |
| `validate_arguments(parser, args)` | Vérifie que les combinaisons d'options sont cohérentes. |
| `choose_interactive_categories(categories)` | Affiche le menu interactif de sélection des catégories. |
| `resolve_categories(categories, categories_argument, default_all=False, logger=None, quiet=False)` | Transforme l'argument `--categories` en dictionnaire de catégories à traiter. |
| `build_export_dir(output_dir=None)` | Prépare le dossier racine daté de l'extraction. |
| `print_if_not_quiet(message='', quiet=False)` | Affiche un message uniquement si le mode silencieux est désactivé. |
| `list_categories(categories)` | Affiche les catégories disponibles. |
| `list_books(categories, categories_argument, logger)` | Affiche uniquement les titres des livres des catégories choisies. |
| `print_book_details(book)` | Affiche les détails d'un livre. |
| `show_details(categories, titles, categories_argument, logger)` | Recherche et affiche les détails d'un ou plusieurs livres. |
| `extract_books(selected_categories, export_dir, logger, quiet=False)` | Extrait les livres catégorie par catégorie, transforme les données et télécharge les images dans chaque dossier de catégorie. |
| `print_summary(summary, total)` | Affiche le résumé de l'extraction. |
| `save_category_csv_files(books_by_category, export_dir, logger)` | Sauvegarde un fichier CSV par catégorie. |
| `run_extraction(selected_categories, output_dir, logger, log_file, quiet=False)` | Lance une extraction complète et sauvegarde les fichiers générés. |
| `run_cli_mode(args, categories, logger, log_file)` | Lance le mode ligne de commande et prépare la liste des titres demandés avec `--detail`. |
| `run_interactive_mode(categories, logger, log_file)` | Lance le mode interactif. |
| `main()` | Configure le programme et lance le mode adapté. |

## Points importants

- `main.py` ne contient pas directement la logique d'extraction HTML.
- Il coordonne les modules `extract`, `transform`, `load` et `logger_config`.
- Il gère les modes interactif et non interactif.
- Il applique le mode `--quiet` pour limiter les sorties terminal pendant l'extraction.
- L'option `--detail` accepte plusieurs titres après une seule option, par exemple `--detail "Titre 1" "Titre 2"`.
- L'extraction génère désormais un dossier daté, puis un sous-dossier par catégorie.
- Chaque catégorie contient son propre fichier CSV et son propre dossier `images/`.
