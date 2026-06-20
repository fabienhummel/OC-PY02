# Annexe — Commandes CLI

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Objectif

Cette annexe regroupe les principales commandes utiles pour installer, exécuter et démontrer l'application.

Toutes les commandes sont à lancer depuis la racine du projet.

## Préparer l'environnement

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activer l'environnement virtuel sous macOS ou Linux :

```bash
source .venv/bin/activate
```

Activer l'environnement virtuel sous Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

## Afficher l'aide

```bash
python src/main.py
```

Cette commande affiche l'aide du programme et les options disponibles.

## Lancer le mode interactif

```bash
python src/main.py --interactive
```

Ce mode permet de sélectionner les catégories avec un menu dans le terminal.

## Lister les catégories

```bash
python src/main.py --list categories
```

Cette commande affiche les catégories disponibles sur le site.

## Lister les livres

Lister tous les livres :

```bash
python src/main.py --list books --categories all
```

Lister les livres d'une catégorie :

```bash
python src/main.py --list books --categories "Fantasy"
```

Lister les livres de plusieurs catégories :

```bash
python src/main.py --list books --categories "Fantasy,Travel"
```

## Afficher le détail d'un livre

Afficher un seul livre :

```bash
python src/main.py --detail "A Light in the Attic"
```

Afficher plusieurs livres :

```bash
python src/main.py --detail "A Light in the Attic" "Soulless"
```

Les titres contenant des virgules restent correctement gérés s'ils sont placés entre guillemets.

L'ancienne syntaxe reste compatible :

```bash
python src/main.py --detail "A Light in the Attic" --detail "Soulless"
```

## Lancer une extraction

Extraire toutes les catégories :

```bash
python src/main.py --extract --categories all
```

Extraire une seule catégorie :

```bash
python src/main.py --extract --categories "Fantasy"
```

Extraire plusieurs catégories :

```bash
python src/main.py --extract --categories "Classics,Philosophy"
```

## Choisir un dossier de sortie

```bash
python src/main.py --extract --categories "Classics,Philosophy" --output "./exports"
```

Cette commande génère le fichier CSV dans le dossier indiqué.

## Utiliser le mode silencieux

```bash
python src/main.py --extract --categories all --quiet
```

Le mode silencieux limite les sorties dans le terminal. Les informations restent disponibles dans le fichier log.

## Fichiers générés

Lors d'une extraction, le programme peut générer :

```text
outputs/books_extraction_YYYYMMDD_HHMMSS.csv
images/books_extraction_YYYYMMDD_HHMMSS/
logs/extraction_YYYYMMDD_HHMMSS.log
```

## Commande de démonstration recommandée

Pour la soutenance, une commande courte et lisible peut être utilisée :

```bash
python src/main.py --extract --categories "Classics,Philosophy"
```

Elle permet de montrer le fonctionnement complet sans extraire toutes les catégories.
