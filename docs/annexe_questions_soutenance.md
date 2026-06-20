# Annexe — Questions de soutenance

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Objectif

Cette annexe regroupe des questions susceptibles d'être posées pendant la soutenance, avec des réponses courtes et professionnelles.

## Questions sur le projet

| Question | Réponse possible |
|---|---|
| Quel est l'objectif du projet ? | Automatiser l'extraction de données de livres depuis Books to Scrape, produire des CSV par catégorie et récupérer les images associées. |
| Quels sont les livrables attendus ? | Un repository GitHub, un fichier ZIP contenant les données générées et les images, et un mail PDF expliquant le pipeline ETL. |
| Pourquoi utiliser Books to Scrape ? | C'est un site fictif conçu pour s'entraîner au scraping web. |
| Pourquoi les données ne sont-elles pas dans GitHub ? | Les CSV, images et logs sont des fichiers générés. Ils doivent être fournis séparément dans le ZIP. |

## Questions sur le pipeline ETL

| Question | Réponse possible |
|---|---|
| Qu'est-ce qu'un pipeline ETL ? | ETL signifie Extract, Transform, Load : extraire les données, les transformer, puis les charger ou les sauvegarder. |
| Où se trouve la partie Extract ? | Dans `extract.py`, qui récupère les pages HTML et les informations des livres. |
| Où se trouve la partie Transform ? | Dans `transform.py`, qui nettoie et convertit certaines données. |
| Où se trouve la partie Load ? | Dans `load.py`, qui prépare les dossiers de sortie, les CSV par catégorie et les dossiers d'images. |
| Pourquoi séparer ces étapes ? | Pour rendre le code plus lisible, plus maintenable et plus facile à expliquer. |

## Questions sur l'extraction

| Question | Réponse possible |
|---|---|
| Comment récupères-tu les pages HTML ? | Avec `requests`, puis le HTML est analysé avec Beautiful Soup. |
| À quoi sert Beautiful Soup ? | À parcourir le HTML et récupérer les balises contenant les données utiles. |
| Comment récupères-tu les catégories ? | Depuis la page d'accueil, en analysant le menu des catégories. |
| Pourquoi ignorer la catégorie globale `Books` ? | Elle regroupe tous les livres et ne correspond pas à une catégorie précise. |
| Comment gères-tu la pagination ? | Le programme identifie le nombre de pages d'une catégorie et construit les URL page par page. |
| Comment récupères-tu les détails d'un livre ? | Le programme ouvre chaque page produit et extrait le tableau d'information, la description, la note, la catégorie et l'image. |

## Questions sur les transformations

| Question | Réponse possible |
|---|---|
| Pourquoi transformer les données ? | Pour obtenir des données plus propres et plus exploitables dans le CSV. |
| Comment transformes-tu la disponibilité ? | Le texte de disponibilité est converti en nombre d'exemplaires disponibles. |
| Comment transformes-tu la note ? | Une note textuelle comme `Three` est convertie en nombre, par exemple `3`. |
| Pourquoi nettoyer les textes ? | Pour supprimer les espaces, tabulations ou retours à la ligne inutiles. |
| Pourquoi conserver le symbole de devise dans les prix ? | Pour garder l'information d'origine. Une conversion numérique peut être ajoutée plus tard si nécessaire. |

## Questions sur les fichiers générés

| Question | Réponse possible |
|---|---|
| Comment le CSV est-il généré ? | Avec le module standard `csv`, un dictionnaire de champs fixes et une sauvegarde par catégorie. |
| Pourquoi un CSV par catégorie ? | C'est demandé dans le cahier des charges et cela rend les données plus simples à exploiter. |
| Où sont stockées les images ? | Dans le dossier `images/` de chaque catégorie, dans le dossier d'extraction daté. |
| À quoi servent les logs ? | À tracer l'exécution et les erreurs sans surcharger le terminal. |
| Que contient le fichier ZIP final ? | Le dossier d'extraction généré, avec un sous-dossier par catégorie contenant le CSV et les images. |

## Questions sur l'environnement Python

| Question | Réponse possible |
|---|---|
| À quoi sert l'environnement virtuel ? | À isoler les dépendances du projet. |
| À quoi sert `requirements.txt` ? | À installer les dépendances nécessaires sur un autre poste. |
| Pourquoi ne pas versionner `.venv` ? | C'est un dossier local, volumineux et propre à chaque environnement. |
| Pourquoi utiliser `.gitignore` ? | Pour exclure les fichiers générés ou locaux du dépôt Git. |

## Questions sur les choix techniques

| Question | Réponse possible |
|---|---|
| Pourquoi utiliser `requests` ? | Pour récupérer simplement les pages web. |
| Pourquoi utiliser `BeautifulSoup` ? | Pour extraire les données depuis le HTML. |
| Pourquoi utiliser `argparse` ? | Pour proposer une interface en ligne de commande. |
| Pourquoi utiliser `pathlib` ? | Pour manipuler les chemins de fichiers de manière propre. |
| Pourquoi ne pas tout mettre dans `main.py` ? | Pour éviter un fichier trop long et séparer les responsabilités. |

## Questions sur les améliorations possibles

| Question | Réponse possible |
|---|---|
| Que pourrais-tu améliorer ? | Ajouter des tests automatisés, une base de données, une planification automatique et un suivi des prix dans le temps. |
| Comment faire un vrai suivi de prix ? | Exécuter le script régulièrement et stocker les résultats avec une date d'extraction. |
| Comment industrialiser le pipeline ? | Ajouter une planification, une base de données, des logs centralisés et éventuellement des alertes. |

## Questions les plus probables

1. Peux-tu expliquer ton pipeline ETL ?
2. Où sont les parties Extract, Transform et Load dans ton code ?
3. Comment récupères-tu les données depuis le HTML ?
4. Comment gères-tu les catégories et la pagination ?
5. Comment transformes-tu la note et la disponibilité ?
6. Comment génères-tu un CSV par catégorie ?
7. Pourquoi les données et images ne sont-elles pas dans GitHub ?
8. Comment installer et lancer ton projet depuis zéro ?
9. À quoi sert `requirements.txt` ?
10. Que ferais-tu pour améliorer le projet ?
