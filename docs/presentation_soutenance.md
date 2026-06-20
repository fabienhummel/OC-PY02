# Soutenance — Projet 2 OC-PY02

**Projet :** Utilisez les bases de Python pour l'analyse de marché  
**Formation :** OpenClassrooms — Développeur d'application Python  
**Auteur :** Fabien Hummel

---

## 1. Contexte du projet

Books Online souhaite automatiser le suivi des prix de livres d'occasion chez un concurrent fictif : **Books to Scrape**.

Le travail manuel étant trop long, l'objectif est de développer une première version bêta d'un scraper Python capable de récupérer les informations produits au moment de son exécution.

**Objectif principal :** produire automatiquement des données exploitables sous forme de fichier CSV, avec les images associées.

---

## 2. Objectif de l'application

L'application permet de :

- récupérer les catégories disponibles sur Books to Scrape ;
- extraire les informations détaillées des livres ;
- transformer certaines données pour les rendre exploitables ;
- générer un fichier CSV ;
- télécharger les images des livres ;
- tracer les actions et erreurs dans un fichier log.

---

## 3. Données extraites

Pour chaque livre, le programme extrait les champs demandés :

| Champ | Description |
|---|---|
| `product_page_url` | URL de la page produit |
| `universal_product_code` | Code UPC du livre |
| `title` | Titre du livre |
| `price_including_tax` | Prix TTC |
| `price_excluding_tax` | Prix HT |
| `number_available` | Nombre d'exemplaires disponibles |
| `product_description` | Description du produit |
| `category` | Catégorie du livre |
| `review_rating` | Note du livre |
| `image_url` | URL de l'image |

---

## 4. Livrables attendus

Les livrables du projet sont :

1. un repository GitHub public contenant le code, le `README.md` et le `requirements.txt` ;
2. un fichier ZIP contenant les données générées et les images associées ;
3. un mail PDF décrivant comment l'application permet d'établir un pipeline ETL.

Le repository ne contient pas :

- l'environnement virtuel ;
- les fichiers CSV générés ;
- les images extraites ;
- les fichiers logs.

---

## 5. Organisation du projet

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

**Principe :** le dépôt contient le code source et la documentation, mais pas les fichiers générés.

---

## 6. Architecture générale

Le programme est organisé autour de quatre rôles principaux :

| Fichier | Rôle |
|---|---|
| `main.py` | Point d'entrée et orchestration |
| `extract.py` | Extraction des données depuis le HTML |
| `transform.py` | Nettoyage et conversion des données |
| `load.py` | Sauvegarde CSV et téléchargement des images |
| `logger_config.py` | Configuration des logs |

Cette organisation permet de séparer clairement les responsabilités du code.

---

## 7. Pipeline ETL

Le projet suit une logique ETL :

| Étape | Rôle dans le projet |
|---|---|
| Extract | Récupérer les pages HTML et les données brutes |
| Transform | Nettoyer et convertir les données utiles |
| Load | Sauvegarder les données et les images localement |

**Message clé :** le programme ne se limite pas à scraper une page ; il structure le processus de collecte sous forme de pipeline.

---

## 8. Extract — Extraction

La partie extraction permet de :

- récupérer les catégories ;
- parcourir les pages de catégories ;
- récupérer les liens des livres ;
- ouvrir chaque page produit ;
- extraire les données du tableau `Product Information` ;
- extraire la description, la catégorie, la note et l'image.

Le module concerné est :

```text
src/books_scraper/extract.py
```

---

## 9. Transform — Transformation

La partie transformation prépare les données avant l'export CSV.

Exemples :

```text
Three -> 3
In stock (22 available) -> 22
```

Les textes sont également nettoyés pour éviter les espaces ou retours à la ligne inutiles.

Le module concerné est :

```text
src/books_scraper/transform.py
```

---

## 10. Load — Chargement / restitution

La partie chargement permet de :

- générer un fichier CSV daté ;
- créer un dossier images associé à l'extraction ;
- télécharger les images avec un nom explicite ;
- produire un fichier log pour tracer l'exécution.

Exemple de sortie :

```text
outputs/books_extraction_20260620_183000.csv
images/books_extraction_20260620_183000/
logs/extraction_20260620_183000.log
```

---

## 11. Modes d'utilisation

L'application peut être utilisée en mode interactif ou en ligne de commande.

### Mode interactif

```bash
python src/main.py --interactive
```

Ce mode permet de choisir les catégories avec un menu dans le terminal.

### Mode ligne de commande

```bash
python src/main.py --extract --categories all
```

ou :

```bash
python src/main.py --extract --categories "Fantasy,Travel"
```

---

## 12. Commandes utiles pour la démonstration

Afficher l'aide :

```bash
python src/main.py
```

Lister les catégories :

```bash
python src/main.py --list categories
```

Lister les titres des livres :

```bash
python src/main.py --list books --categories "Fantasy"
```

Afficher le détail d'un livre :

```bash
python src/main.py --detail "A Light in the Attic"
```

Lancer une extraction :

```bash
python src/main.py --extract --categories "Classics,Philosophy"
```

---

## 13. Gestion des erreurs

Le programme intègre plusieurs mécanismes de sécurité :

- gestion des erreurs réseau ;
- plusieurs tentatives en cas d'échec temporaire ;
- logs détaillés ;
- poursuite de l'extraction si un livre ou une catégorie échoue ;
- mode silencieux `--quiet` pour une utilisation automatisée.

Le fichier log permet de retrouver les erreurs sans surcharger l'affichage terminal.

---

## 14. GitHub et reproductibilité

Le repository contient :

- le code source ;
- le `README.md` ;
- le `requirements.txt` ;
- la documentation du projet.

Le repository ne contient pas :

- `.venv/` ;
- les fichiers CSV générés ;
- les images téléchargées ;
- les logs.

L'installation se fait avec :

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

---

## 15. Démonstration prévue

Plan de démonstration :

1. afficher l'aide du programme ;
2. lister les catégories ;
3. afficher les livres d'une catégorie ;
4. afficher le détail d'un livre ;
5. lancer une extraction sur une ou deux catégories ;
6. montrer le CSV généré ;
7. montrer le dossier images ;
8. montrer le fichier log.

---

## 16. Améliorations futures

Idées d'améliorations possibles :

- ajout de tests automatisés ;
- export d'un fichier CSV par catégorie ;
- planification automatique de l'extraction ;
- stockage des données dans une base de données ;
- comparaison des prix dans le temps ;
- ajout d'un rapport d'exécution plus détaillé ;
- meilleure gestion des reprises après interruption.

---

## 17. Questions possibles de l'évaluateur

### Comment les champs ont-ils été identifiés ?

En analysant la structure HTML des pages : balises, classes CSS, tableau `Product Information`, fil d'Ariane et attributs HTML.

### Pourquoi utiliser un environnement virtuel ?

Pour isoler les dépendances du projet et rendre l'installation reproductible avec `requirements.txt`.

### Pourquoi les données ne sont-elles pas dans GitHub ?

Les fichiers CSV, les images et les logs sont des fichiers générés. Ils ne doivent pas faire partie du repository, mais du ZIP livré séparément.

### Comment le programme illustre-t-il un pipeline ETL ?

Il extrait les données du site, les transforme pour les rendre exploitables, puis les charge dans un fichier CSV avec les images associées.

---

## 18. Conclusion

Ce projet met en pratique les bases de Python dans un cas concret d'automatisation et de traitement de données.

Il démontre :

- l'utilisation de Python ;
- la manipulation de pages HTML ;
- l'organisation d'un code en modules ;
- l'usage de Git et GitHub ;
- la génération de livrables exploitables ;
- la compréhension du processus ETL.

**Phrase de conclusion :**  
L'application constitue une première version fonctionnelle d'un outil de collecte automatisée, qui pourrait être enrichi ensuite pour suivre les prix dans le temps.
