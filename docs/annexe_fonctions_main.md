# Annexe — Fonctions de `main.py`

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Rôle du fichier

`main.py` est le point d'entrée du programme. Il orchestre l'exécution : lecture des options, choix du mode, extraction, transformation, sauvegarde CSV, téléchargement des images et affichage des résultats.

## Fonctions

| Fonction | Utilité |
|---|---|
| `parse_arguments()` | Définit les options disponibles en ligne de commande. |
| `validate_arguments(parser, args)` | Vérifie que les combinaisons d'options sont cohérentes. |
| `choose_interactive_categories(categories)` | Affiche le menu interactif de sélection des catégories. |
| `resolve_categories(categories, categories_argument, default_all=False, logger=None, quiet=False)` | Transforme l'argument `--categories` en dictionnaire de catégories à traiter. |
| `build_output_paths(output_dir=None)` | Prépare le chemin du CSV et le dossier images associé. |
| `print_if_not_quiet(message='', quiet=False)` | Affiche un message uniquement si le mode silencieux est désactivé. |
| `list_categories(categories)` | Affiche les catégories disponibles. |
| `list_books(categories, categories_argument, logger)` | Affiche uniquement les titres des livres des catégories choisies. |
| `print_book_details(book)` | Affiche les détails d'un livre. |
| `show_details(categories, titles, categories_argument, logger)` | Recherche et affiche les détails d'un ou plusieurs livres. |
| `extract_books(selected_categories, images_dir, logger, quiet=False)` | Extrait les livres, transforme les données et télécharge les images. |
| `print_summary(summary, total)` | Affiche le résumé de l'extraction. |
| `run_extraction(selected_categories, output_dir, logger, log_file, quiet=False)` | Lance une extraction complète et sauvegarde les fichiers. |
| `run_cli_mode(args, categories, logger, log_file)` | Lance le mode ligne de commande. |
| `run_interactive_mode(categories, logger, log_file)` | Lance le mode interactif. |
| `main()` | Configure le programme et lance le mode adapté. |

## Points importants

- `main.py` ne contient pas directement la logique d'extraction HTML.
- Il coordonne les modules `extract`, `transform`, `load` et `logger_config`.
- Il gère les modes interactif et non interactif.
- Il applique le mode `--quiet` pour limiter les sorties terminal pendant l'extraction.
