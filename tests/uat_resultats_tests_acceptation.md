# UAT — Résultats des tests d'acceptation utilisateur

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel  
**Document :** Résultats des tests UAT  
**Public cible :** Sam ou utilisateur testeur

---

## 1. Objectif du document

Ce document sert à consigner les résultats des **tests d'acceptation utilisateur** du projet OC-PY02.

Les tests UAT vérifient que le livrable répond bien au cahier des charges demandé par Sam :

- repository GitHub exploitable ;
- installation possible avec `requirements.txt` ;
- génération des données attendues ;
- présence des champs demandés dans les CSV ;
- génération d'un CSV distinct par catégorie ;
- téléchargement des images ;
- organisation simple des données générées ;
- présence du mail PDF décrivant le pipeline ETL.

Ce document ne remplace pas le protocole de tests technique. Il se concentre uniquement sur l'acceptation du livrable par l'utilisateur.

---

## 2. Informations de test

| Élément | Valeur |
|---|---|
| Testeur |  |
| Date du test |  |
| Version testée / commit GitHub |  |
| Système utilisé |  |
| Navigateur ou terminal utilisé |  |
| Décision finale | Accepté / Accepté avec réserve / Refusé |

---

## 3. Statuts possibles

| Statut | Signification |
|---|---|
| Réussi | Le résultat obtenu correspond au résultat attendu. |
| Échec | Le résultat obtenu ne respecte pas le critère d'acceptation. |
| Non testé | Le test n'a pas encore été exécuté. |
| Bloqué | Le test ne peut pas être réalisé à cause d'un prérequis manquant. |
| À corriger | Un écart est identifié et doit être traité avant validation complète. |

---

## 4. Synthèse des tests UAT

| ID | Exigence vérifiée | Statut |
|---|---|---|
| UAT-01 | Installation depuis le repository GitHub | Non testé |
| UAT-02 | Contenu attendu du repository | Non testé |
| UAT-03 | Extraction d'une catégorie complète | Non testé |
| UAT-04 | Présence des champs demandés dans le CSV | Non testé |
| UAT-05 | Cohérence des données extraites | Non testé |
| UAT-06 | Gestion de la pagination | Non testé |
| UAT-07 | Extraction de toutes les catégories | Non testé |
| UAT-08 | CSV distinct par catégorie | Non testé |
| UAT-09 | Téléchargement des images associées | Non testé |
| UAT-10 | Organisation du ZIP final | Non testé |
| UAT-11 | Mail PDF décrivant le pipeline ETL | Non testé |

---

## UAT-01 — Installation depuis le repository GitHub

### Exigence couverte

Le repository GitHub doit permettre à Sam ou à un utilisateur testeur de récupérer le code et de l'exécuter avec succès.

### Préconditions

- Avoir accès au repository GitHub public.
- Avoir Python installé.
- Avoir un terminal disponible.

### Actions à réaliser

```bash
git clone https://github.com/fabienhummel/OC-PY02.git
cd OC-PY02
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/main.py
```

### Résultat attendu

- Le repository est cloné correctement.
- L'environnement virtuel est créé.
- Les dépendances sont installées sans erreur bloquante.
- L'aide du programme s'affiche.

### Critère d'acceptation

Le test est réussi si un utilisateur peut installer le projet et afficher l'aide du programme en suivant les instructions fournies.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran de l'installation et de l'affichage de l'aide du programme.
</div>

---

## UAT-02 — Vérification du contenu du repository

### Exigence couverte

Le repository doit contenir le code, un `README.md` complété et un `requirements.txt`. Il ne doit pas contenir les données et images extraites.

### Préconditions

- Le repository est accessible sur GitHub.

### Actions à réaliser

Depuis GitHub ou depuis le dossier local, vérifier la présence des éléments suivants :

```text
README.md
requirements.txt
src/
docs/
tests/
```

Vérifier que les éléments suivants ne sont pas versionnés :

```text
.venv/
outputs/books_extraction_*/
logs/*.log
exports_test/
```

### Résultat attendu

- Le code source est présent.
- Le `README.md` est présent et documenté.
- Le `requirements.txt` est présent.
- Les données générées, images extraites et logs ne sont pas inclus dans le repository.

### Critère d'acceptation

Le test est réussi si le repository contient les fichiers nécessaires à l'exécution du projet, sans inclure les fichiers générés.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du contenu du repository GitHub.
</div>

---

## UAT-03 — Extraction d'une catégorie complète

### Exigence couverte

L'application doit pouvoir extraire les données d'une catégorie de livres.

### Préconditions

- Le projet est installé.
- L'environnement virtuel est activé.
- Les dépendances sont installées.

### Action à réaliser

```bash
python src/main.py --extract --categories "Fantasy"
```

### Résultat attendu

Le programme doit :

- parcourir la catégorie `Fantasy` ;
- extraire les livres de cette catégorie ;
- générer un dossier d'extraction daté ;
- générer `fantasy/fantasy.csv` ;
- télécharger les images dans `fantasy/images/` ;
- afficher un résumé final de l'extraction.

### Critère d'acceptation

Le test est réussi si l'extraction se termine sans erreur bloquante et si le CSV ainsi que le dossier d'images de la catégorie sont générés.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du résumé d'extraction de la catégorie Fantasy.
</div>

---

## UAT-04 — Vérification des champs demandés dans le CSV

### Exigence couverte

Le CSV généré doit contenir les champs demandés dans le cahier des charges.

### Préconditions

- Une extraction a déjà été réalisée.
- Au moins un fichier CSV est présent dans un dossier de catégorie.

### Action à réaliser

Commande possible :

```bash
python - <<'PY'
import csv
from pathlib import Path

csv_files = sorted(Path('outputs').glob('books_extraction_*/**/*.csv'))
latest_csv = csv_files[-1]

with latest_csv.open(encoding='utf-8-sig', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    print(latest_csv)
    print(reader.fieldnames)
PY
```

### Résultat attendu

Les colonnes suivantes doivent être présentes :

```text
product_page_url
universal_product_code
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url
```

### Critère d'acceptation

Le test est réussi si les dix champs demandés sont présents dans le CSV.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran des colonnes du CSV généré.
</div>

---

## UAT-05 — Vérification de la cohérence des données extraites

### Exigence couverte

Les données extraites doivent être exploitables par Sam pour l'analyse de marché.

### Préconditions

- Un fichier CSV de catégorie a été généré.

### Action à réaliser

Ouvrir le CSV et vérifier quelques lignes d'exemple.

Contrôler notamment que :

- les titres sont renseignés ;
- les UPC sont présents ;
- les prix TTC et HT sont présents ;
- le stock disponible est renseigné ;
- les descriptions sont présentes lorsque disponibles ;
- la catégorie est renseignée ;
- la note est lisible ;
- l'URL de l'image est présente.

### Résultat attendu

Les lignes du CSV doivent contenir des données cohérentes et exploitables.

### Critère d'acceptation

Le test est réussi si un échantillon de lignes permet de confirmer que les informations demandées sont bien présentes et lisibles.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran d'un extrait du CSV avec plusieurs lignes renseignées.
</div>

---

## UAT-06 — Gestion de la pagination

### Exigence couverte

L'application doit parcourir les pages d'une catégorie, y compris lorsqu'une catégorie contient plusieurs pages de résultats.

### Préconditions

- Le projet est installé.
- L'environnement virtuel est activé.

### Action à réaliser

```bash
python src/main.py --extract --categories "Default"
```

### Résultat attendu

Le programme doit parcourir toutes les pages de la catégorie concernée et extraire l'ensemble des livres disponibles pour cette catégorie.

### Critère d'acceptation

Le test est réussi si le nombre de livres extraits correspond à l'ensemble de la catégorie et ne se limite pas aux premiers résultats visibles sur la première page.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du résumé d'extraction montrant une catégorie avec pagination.
</div>

---

## UAT-07 — Extraction de toutes les catégories

### Exigence couverte

L'application doit permettre de traiter l'ensemble des catégories du site.

### Préconditions

- Le projet est installé.
- L'environnement virtuel est activé.
- La connexion Internet est disponible.

### Action à réaliser

```bash
python src/main.py --extract --categories all
```

### Résultat attendu

Le programme doit extraire les livres de toutes les catégories disponibles et générer un dossier par catégorie dans le dossier d'extraction.

### Critère d'acceptation

Le test est réussi si l'extraction complète se termine sans erreur bloquante et si les données sont générées par catégorie.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du résumé final de l'extraction de toutes les catégories.
</div>

---

## UAT-08 — CSV distinct par catégorie

### Exigence couverte

Le cahier des charges demande la génération d'un fichier CSV distinct pour chaque catégorie de livres.

### Préconditions

- Le projet est installé.
- L'environnement virtuel est activé.
- L'extraction de plusieurs catégories est possible.

### Action à réaliser

```bash
python src/main.py --extract --categories "Classics,Philosophy"
```

### Résultat attendu

Le programme doit générer un CSV distinct pour chaque catégorie extraite, par exemple :

```text
outputs/books_extraction_YYYYMMDD_HHMMSS/
├── classics/
│   └── classics.csv
└── philosophy/
    └── philosophy.csv
```

### Critère d'acceptation

Le test est réussi si chaque catégorie extraite produit son propre fichier CSV dans son propre dossier de catégorie.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran montrant les CSV générés par catégorie.
</div>

---

## UAT-09 — Téléchargement des images associées

### Exigence couverte

Les images des livres extraits doivent être téléchargées et fournies avec les données générées.

### Préconditions

- Une extraction a été réalisée.
- Un dossier d'images a été généré dans au moins une catégorie.

### Action à réaliser

```bash
find outputs -path "*/images/*" -type f | head
```

### Résultat attendu

Le dossier `images/` de chaque catégorie doit contenir des fichiers images correspondant aux livres extraits.

### Critère d'acceptation

Le test est réussi si les images sont présentes et organisées dans le dossier de leur catégorie.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du dossier contenant les images téléchargées.
</div>

---

## UAT-10 — Organisation du ZIP final

### Exigence couverte

Sam demande un fichier ZIP contenant les données générées et les images extraites, organisées simplement.

### Préconditions

- Les extractions nécessaires ont été réalisées.
- Les CSV et images sont disponibles localement.

### Action à réaliser

Créer ou vérifier le ZIP final contenant le dossier d'extraction généré.

Structure attendue recommandée :

```text
OC-PY02_donnees_generees.zip
└── books_extraction_YYYYMMDD_HHMMSS/
    ├── classics/
    │   ├── classics.csv
    │   └── images/
    └── philosophy/
        ├── philosophy.csv
        └── images/
```

### Résultat attendu

Le ZIP doit contenir les données générées et les images associées dans une structure claire.

### Critère d'acceptation

Le test est réussi si Sam peut ouvrir le ZIP et comprendre rapidement où se trouvent les CSV et les images.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du contenu du ZIP final.
</div>

---

## UAT-11 — Mail PDF décrivant le pipeline ETL

### Exigence couverte

Sam demande un mail au format PDF décrivant comment l'application permet d'établir un pipeline ETL.

### Préconditions

- Le PDF du mail ETL est disponible.

### Action à réaliser

Ouvrir le PDF et vérifier qu'il décrit clairement :

- la partie Extract ;
- la partie Transform ;
- la partie Load ;
- l'intérêt de cette organisation pour le suivi des données.

### Résultat attendu

Le PDF doit expliquer de manière sobre et compréhensible comment l'application s'inscrit dans une logique ETL.

### Critère d'acceptation

Le test est réussi si le PDF permet à Sam de présenter simplement le pipeline ETL à son responsable.

### Statut

- [ ] Réussi
- [ ] Échec
- [ ] Non testé
- [ ] Bloqué
- [ ] À corriger

### Commentaire du testeur



<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran ou aperçu du PDF décrivant le pipeline ETL.
</div>

---

## 5. Anomalies ou écarts constatés

| ID anomalie | Test concerné | Description | Impact | Décision |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

---

## 6. Décision finale

| Décision | Cocher |
|---|---|
| Livrable accepté | [ ] |
| Livrable accepté avec réserve | [ ] |
| Livrable refusé | [ ] |

### Commentaire final du testeur



### Signature ou validation

| Nom | Date | Validation |
|---|---|---|
|  |  |  |
