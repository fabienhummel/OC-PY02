# Annexe — Pipeline ETL

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Objectif

Cette annexe explique comment l'application s'organise autour d'un pipeline ETL.

ETL signifie :

- **Extract** : extraire les données ;
- **Transform** : transformer les données ;
- **Load** : charger ou sauvegarder les données.

## Vue globale

```text
Books to Scrape
      ↓
Extract : récupération HTML et extraction des données
      ↓
Transform : nettoyage et conversion
      ↓
Load : dossier d'export, CSV par catégorie, images et logs
```

## Correspondance avec les fichiers du projet

| Étape | Fichier | Rôle |
|---|---|---|
| Extract | `extract.py` | Récupère les catégories, les livres et les détails produits. |
| Transform | `transform.py` | Nettoie les textes et convertit certaines valeurs. |
| Load | `load.py` | Prépare les dossiers de sortie, écrit les CSV et télécharge les images. |
| Logs | `logger_config.py` | Configure le fichier log de l'exécution. |
| Orchestration | `main.py` | Enchaîne les étapes et gère les options de lancement. |

## Étape 1 — Extract

La première étape consiste à récupérer les données depuis le site web.

Le programme :

- récupère la page d'accueil ;
- extrait les catégories ;
- parcourt les pages d'une catégorie ;
- récupère les liens des livres ;
- ouvre chaque page produit ;
- extrait les données demandées.

Les données récupérées peuvent encore être brutes.

Exemples :

```text
review_rating = Three
availability = In stock (22 available)
```

## Étape 2 — Transform

La deuxième étape prépare les données pour les rendre plus exploitables.

Exemples :

```text
Three -> 3
In stock (22 available) -> 22
```

Cette étape permet aussi de nettoyer les textes extraits depuis le HTML.

## Étape 3 — Load

La troisième étape sauvegarde les résultats.

Le programme génère :

- un dossier d'extraction daté ;
- un sous-dossier par catégorie ;
- un fichier CSV par catégorie ;
- un dossier `images/` dans chaque catégorie ;
- un fichier log dans `logs/`.

Exemple de sortie :

```text
outputs/books_extraction_YYYYMMDD_HHMMSS/
├── classics/
│   ├── classics.csv
│   └── images/
└── philosophy/
    ├── philosophy.csv
    └── images/

logs/extraction_YYYYMMDD_HHMMSS.log
```

## Pourquoi cette organisation est utile

Cette organisation permet de :

- mieux comprendre le cheminement des données ;
- séparer les responsabilités du code ;
- obtenir un fichier CSV distinct pour chaque catégorie ;
- regrouper les images avec la catégorie correspondante ;
- faciliter la création du ZIP final ;
- faciliter la maintenance ;
- préparer une éventuelle évolution vers un traitement plus automatisé.

## Évolutions possibles

Le pipeline pourrait être enrichi avec :

- une exécution planifiée ;
- une base de données ;
- un historique des prix ;
- un tableau de bord ;
- des alertes en cas de variation importante.

## Résumé

L'application établit un pipeline ETL simple :

```text
Site web → extraction → transformation → sauvegarde par catégorie
```

Chaque catégorie produit son propre CSV et son propre dossier d'images, ce qui répond plus directement au besoin de livrable demandé.
