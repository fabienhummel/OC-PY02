# OC-PY02 — Analyse de marché avec Python

Projet 2 de la formation OpenClassrooms **Développeur d'application Python** :
**Utilisez les bases de Python pour l'analyse de marché**.

Ce projet consiste à développer un programme Python capable d'extraire les informations de livres depuis le site [Books to Scrape](https://books.toscrape.com/), puis de sauvegarder les données dans un fichier CSV et de télécharger les images associées.

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

Les données sont ensuite exportées dans un fichier CSV. Les images des livres sont téléchargées localement dans un dossier dédié à chaque extraction.

## Fonctionnalités

Le programme permet de :

- récupérer automatiquement les catégories du site ;
- sélectionner les catégories à extraire en mode interactif ;
- lancer une extraction complète en ligne de commande ;
- lister les catégories disponibles ;
- lister les titres des livres d'une ou plusieurs catégories ;
- afficher le détail d'un ou plusieurs livres ;
- générer un fichier CSV daté ;
- télécharger les images des livres ;
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

Les dossiers `outputs/`, `images/` et `logs/` contiennent des fichiers générés localement pendant l'exécution. Ces fichiers ne sont pas destinés à être versionnés dans Git.

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

- écriture du fichier CSV ;
- génération d'un nom de fichier daté ;
- création du dossier images associé à l'extraction ;
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

Cette syntaxe permet de passer plusieurs titres sans répéter l'option `--detail`. Les titres contenant des virgules restent correctement gérés s'ils sont placés entre guillemets.

Si un titre contient un guillemet double, il est possible d'utiliser des apostrophes autour du titre :

```bash
python src/main.py --detail 'Titre avec " dans le nom du livre' "Second livre"
```

## Fichiers générés

Lors d'une extraction, le programme génère :

- un fichier CSV dans `outputs/` ;
- un dossier d'images dans `images/` ;
- un fichier log dans `logs/`.

Exemple :

```text
outputs/books_extraction_20260620_183000.csv
images/books_extraction_20260620_183000/
logs/extraction_20260620_183000.log
```

Le fichier CSV et le dossier images partagent le même nom de base afin de relier facilement les données et les images d'une même extraction.

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

- extrait les livres des catégories `Classics` et `Philosophy` ;
- génère un fichier CSV dans `exports/` ;
- crée un dossier `exports/images/` pour les images ;
- écrit un fichier log dans `logs/`.

## Statut

Projet en cours de développement dans le cadre de la formation OpenClassrooms.
