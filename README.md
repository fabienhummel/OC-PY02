# OC-PY02 — Analyse de marché avec Python

Projet 2 de la formation OpenClassrooms **Développeur d'application Python** :
**Utilisez les bases de Python pour l'analyse de marché**.

Ce projet consiste à développer un programme Python capable d'extraire les informations de livres depuis le site [Books to Scrape](https://books.toscrape.com/), puis de sauvegarder les données dans des fichiers CSV et de télécharger les images associées.

## Objectif du projet

Le programme permet d'automatiser la collecte d'informations produits sur une librairie en ligne fictive.

Pour chaque livre extrait, les informations suivantes sont récupérées :

- `product_page_url`
- `universal_product_code`
- `title`
- `price_including_tax`
- `price_excluding_tax`
- `number_available`
- `product_description`
- `category`
- `review_rating`
- `image_url`

Les données sont exportées dans un dossier d'extraction daté. Chaque catégorie possède son propre dossier, son propre fichier CSV et son dossier d'images.

## Fonctionnalités

Le programme permet de :

- récupérer automatiquement les catégories du site ;
- sélectionner les catégories à extraire en mode interactif ;
- lancer une extraction complète en ligne de commande ;
- lister les catégories disponibles ;
- lister les titres des livres d'une ou plusieurs catégories ;
- afficher le détail d'un ou plusieurs livres ;
- générer un fichier CSV distinct par catégorie ;
- télécharger les images des livres dans le dossier de leur catégorie ;
- tracer les actions et erreurs dans un fichier log ;
- exécuter le programme en mode silencieux avec `--quiet`.

## Organisation du projet

```text
OC-PY02/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   └── books_scraper/
│       ├── __init__.py
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       └── logger_config.py
├── docs/
├── images/
├── logs/
├── outputs/
└── tests/
```

Les dossiers `outputs/`, `images` éventuels et `logs/` contiennent des fichiers générés localement pendant l'exécution. Ces fichiers ne sont pas destinés à être versionnés dans Git.

## Découpage ETL

Le programme suit une logique ETL :

### Extract

Le module `extract.py` récupère les informations depuis les pages HTML du site :

- catégories ;
- liens des livres ;
- pages détaillées des livres ;
- tableau `Product Information` ;
- description ;
- note ;
- image ;
- catégorie.

### Transform

Le module `transform.py` prépare les données avant l'export :

- nettoyage des textes ;
- conversion de la note en nombre ;
- extraction du nombre d'exemplaires disponibles.

Exemples :

```text
Three -> 3
In stock (22 available) -> 22
```

### Load

Le module `load.py` sauvegarde les résultats :

- création d'un dossier d'extraction daté ;
- création d'un sous-dossier par catégorie ;
- écriture d'un fichier CSV par catégorie ;
- création d'un dossier `images/` dans chaque catégorie ;
- téléchargement des images avec un nom de fichier explicite.

## Prérequis

- Python 3.14 ou version compatible ;
- accès Internet ;
- environnement virtuel Python activé.

## Installation

Depuis la racine du projet :

```bash
python -m venv .venv
```

Activation de l'environnement virtuel sous macOS / Linux :

```bash
source .venv/bin/activate
```

Activation de l'environnement virtuel sous Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Installation des dépendances :

```bash
python -m pip install -r requirements.txt
```

## Utilisation

Toutes les commandes se lancent depuis la racine du projet.

### Afficher l'aide

```bash
python src/main.py
```

### Mode interactif

Le mode interactif permet de choisir les catégories avec un menu dans le terminal.

```bash
python src/main.py --interactive
```

Navigation :

- flèches haut / bas pour naviguer ;
- espace pour cocher une catégorie ;
- entrée pour valider.

### Extraction de toutes les catégories

```bash
python src/main.py --extract --categories all
```

### Extraction de certaines catégories

```bash
python src/main.py --extract --categories "Fantasy,Travel"
```

### Choisir un dossier de sortie

```bash
python src/main.py --extract --categories "Fantasy,Travel" --output "./exports"
```

Avec cette option, le dossier d'extraction daté est créé dans `exports/` au lieu de `outputs/`.

### Mode silencieux

Le mode `--quiet` ne produit aucune sortie dans le terminal. Les logs restent écrits dans le fichier log.

```bash
python src/main.py --extract --categories all --quiet
```

L'option `--quiet` est réservée au mode `--extract`.

### Lister les catégories

```bash
python src/main.py --list categories
```

### Lister les titres des livres

Toutes les catégories :

```bash
python src/main.py --list books --categories all
```

Catégories précises :

```bash
python src/main.py --list books --categories "Fantasy,Travel"
```

### Afficher les détails d'un livre

```bash
python src/main.py --detail "A Light in the Attic"
```

Pour plusieurs livres :

```bash
python src/main.py --detail "A Light in the Attic" "Soulless"
```

Cette syntaxe permet de passer plusieurs titres après une seule option `--detail`. Les titres contenant des virgules restent correctement gérés s'ils sont placés entre guillemets.

Si un titre contient un guillemet double, il est possible d'utiliser des apostrophes autour du titre :

```bash
python src/main.py --detail 'Titre contenant "un guillemet"' "Second livre"
```

L'ancienne syntaxe reste compatible :

```bash
python src/main.py --detail "A Light in the Attic" --detail "Soulless"
```

## Fichiers générés

Lors d'une extraction, le programme génère :

- un dossier d'extraction daté dans `outputs/` ou dans le dossier fourni avec `--output` ;
- un sous-dossier par catégorie ;
- un fichier CSV par catégorie ;
- un dossier `images/` par catégorie ;
- un fichier log dans `logs/`.

Exemple :

```text
outputs/books_extraction_20260621_143000/
├── classics/
│   ├── classics.csv
│   └── images/
├── philosophy/
│   ├── philosophy.csv
│   └── images/
└── fantasy/
    ├── fantasy.csv
    └── images/

logs/extraction_20260621_143000.log
```

Cette organisation facilite la création du ZIP final demandé pour le livrable : chaque catégorie contient directement son fichier CSV et les images associées.

## Gestion des erreurs

Le programme intègre une gestion des erreurs :

- tentative de récupération réseau répétée en cas d'échec temporaire ;
- journalisation des erreurs dans un fichier log ;
- poursuite de l'extraction lorsqu'une catégorie ou un livre ne peut pas être traité ;
- mode silencieux pour les exécutions automatisées.

## Dépendances principales

Les principales dépendances utilisées sont :

- `requests` : récupération des pages HTML et téléchargement des images ;
- `beautifulsoup4` : analyse du HTML ;
- `questionary` : menus interactifs dans le terminal ;
- `tqdm` : barre de progression ;
- `python-slugify` : génération de noms de fichiers propres.

La liste complète est disponible dans `requirements.txt`.

## Données et images

Les données extraites, les images téléchargées et les logs ne sont pas inclus dans le dépôt GitHub.

Ils doivent être générés localement en exécutant le programme, puis fournis séparément dans le fichier ZIP demandé pour le livrable OpenClassrooms.

## Exemple de commande complète

```bash
python src/main.py --extract --categories "Classics,Philosophy" --output "./exports"
```

Cette commande :

- crée un dossier d'extraction daté dans `exports/` ;
- extrait les livres des catégories `Classics` et `Philosophy` ;
- génère un CSV dans chaque dossier de catégorie ;
- télécharge les images dans le dossier `images/` de chaque catégorie ;
- écrit un fichier log dans `logs/`.

## Statut

Projet en cours de développement dans le cadre de la formation OpenClassrooms.
