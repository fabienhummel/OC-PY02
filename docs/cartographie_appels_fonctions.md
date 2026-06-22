# Cartographie des appels de fonctions — OC-PY02

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel  
**Objectif :** visualiser quelles fonctions appellent quelles autres fonctions.

---

## 1. Vue globale

```mermaid
flowchart TD
    main[main] --> parse[parse_arguments]
    main --> validate[validate_arguments]
    main --> logger[setup_logger]
    main --> cats[extract_categories]
    main --> mode{Mode choisi}

    mode --> cli[run_cli_mode]
    mode --> interactive[run_interactive_mode]

    interactive --> choose[choose_interactive_categories]
    interactive --> runex[run_extraction]

    cli --> listcat[list_categories]
    cli --> listbooks[list_books]
    cli --> details[show_details]
    cli --> resolve[resolve_categories]
    cli --> runex

    runex --> buildexport[build_export_dir]
    runex --> extractbooks[extract_books]
    runex --> summary[print_summary]
    runex --> savecats[save_category_csv_files]

    buildexport --> defaultdir[get_default_export_dir]

    extractbooks --> catdir[get_category_dir]
    extractbooks --> imgdir[get_category_images_dir]
    extractbooks --> links[extract_book_links_from_category]
    extractbooks --> bookdetails[extract_book_details]
    extractbooks --> transform[transform_book]
    extractbooks --> imagefile[build_image_file_name]
    extractbooks --> download[download_image]

    savecats --> catdir
    savecats --> csvpath[get_category_csv_path]
    savecats --> savecsv[save_books_to_csv]
```

---

## 2. Appels depuis `main.py`

```mermaid
flowchart TD
    main[main] --> parse_arguments
    main --> validate_arguments
    main --> setup_logger
    main --> extract_categories
    main --> run_interactive_mode
    main --> run_cli_mode

    run_cli_mode --> list_categories
    run_cli_mode --> list_books
    run_cli_mode --> show_details
    run_cli_mode --> resolve_categories
    run_cli_mode --> run_extraction

    run_interactive_mode --> choose_interactive_categories
    run_interactive_mode --> run_extraction

    run_extraction --> build_export_dir
    run_extraction --> extract_books
    run_extraction --> print_summary
    run_extraction --> save_category_csv_files
```

### Lecture du schéma

- `main()` initialise le programme.
- `run_cli_mode()` choisit l'action selon les options de ligne de commande.
- `run_extraction()` lance le vrai traitement d'extraction et de sauvegarde.

---

## 3. Appels dans la partie Extract

```mermaid
flowchart TD
    extract_categories --> get_soup

    extract_book_links_from_category --> extract_number_of_pages
    extract_book_links_from_category --> build_category_page_url
    extract_book_links_from_category --> get_soup

    extract_number_of_pages --> get_soup

    extract_book_details --> get_soup
    extract_book_details --> extract_product_information_table
    extract_book_details --> extract_product_description
    extract_book_details --> extract_product_category
    extract_book_details --> extract_product_rating
    extract_book_details --> extract_product_image_url
```

### Lecture du schéma

- `get_soup()` est la fonction de base pour récupérer et analyser une page HTML.
- `extract_book_links_from_category()` parcourt les pages d'une catégorie.
- `extract_book_details()` rassemble les informations détaillées d'un livre.

---

## 4. Appels dans la partie Transform

```mermaid
flowchart TD
    transform_book --> clean_text
    transform_book --> extract_number_available
    transform_book --> convert_rating_to_number

    transform_books --> transform_book
```

### Lecture du schéma

- `transform_book()` est la fonction principale du module `transform.py`.
- Elle s'appuie sur des fonctions spécialisées pour nettoyer et convertir les données.

---

## 5. Appels dans la partie Load

```mermaid
flowchart TD
    get_category_dir --> get_category_slug
    get_category_csv_path --> get_category_slug
    build_image_file_name --> slugify

    save_books_to_csv --> CSV_HEADERS
    save_books_to_csv --> csv_DictWriter[csv.DictWriter]

    download_image --> requests_get[requests.get]
```

### Lecture du schéma

- Les fonctions de chemin créent l'organisation des dossiers.
- `save_books_to_csv()` écrit les fichiers CSV.
- `download_image()` télécharge les images dans les dossiers de catégorie.

---

## 6. Chaîne complète d'une extraction

```mermaid
sequenceDiagram
    participant U as Utilisateur
    participant M as main.py
    participant E as extract.py
    participant T as transform.py
    participant L as load.py
    participant LOG as logger_config.py

    U->>M: python src/main.py --extract --categories "Classics,Philosophy"
    M->>M: parse_arguments()
    M->>M: validate_arguments()
    M->>LOG: setup_logger()
    M->>E: extract_categories(HOME_URL)
    M->>M: resolve_categories()
    M->>L: get_default_export_dir()
    M->>M: extract_books()
    loop Pour chaque catégorie
        M->>L: get_category_dir()
        M->>L: get_category_images_dir()
        M->>E: extract_book_links_from_category()
        loop Pour chaque livre
            M->>E: extract_book_details()
            M->>T: transform_book()
            M->>L: build_image_file_name()
            M->>L: download_image()
        end
    end
    M->>M: save_category_csv_files()
    M->>L: get_category_csv_path()
    M->>L: save_books_to_csv()
    M->>U: Résumé final
```

---

## 7. Points clés à retenir

- `main.py` orchestre les appels.
- `extract.py` récupère les données depuis le web.
- `transform.py` prépare les données pour le CSV.
- `load.py` écrit les CSV et télécharge les images.
- `logger_config.py` prépare les logs.
- La logique principale se lit de haut en bas : arguments, catégories, livres, détails, transformation, sauvegarde.
