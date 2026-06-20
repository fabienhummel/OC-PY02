# Protocole de tests — OC-PY02

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel  
**Objet :** Vérifier le bon fonctionnement du script avant livraison et soutenance.

---

## 1. Objectif du document

Ce protocole sert à vérifier que l'application fonctionne correctement depuis un environnement propre.

Il permet de contrôler :

- l'installation de l'environnement Python ;
- l'installation des dépendances ;
- les commandes principales du programme ;
- le mode interactif ;
- l'extraction des données ;
- la génération du CSV ;
- le téléchargement des images ;
- la création des logs ;
- la nouvelle syntaxe de l'option `--detail`.

Ce document peut être complété avec des captures d'écran pendant les tests.

> 🔴 **Remarque :** les zones rouges ci-dessous indiquent les emplacements où coller les captures d'écran.  
> Si la couleur rouge n'est pas affichée dans GitHub, le texte reste identifiable grâce au symbole 🔴.

---

## 2. Préparation avant les tests

### Conditions de départ

Les tests doivent être réalisés depuis la racine du projet :

```bash
cd ~/Python/OC-PY02
```

L'environnement virtuel doit être activé :

```bash
source .venv/bin/activate
```

### Vérification de l'état Git

**Commande à lancer :**

```bash
git status
```

**Résultat attendu :**

- la branche doit être `main` ;
- le dépôt doit être à jour avec `origin/main` ;
- aucun fichier utile ne doit être en attente de commit avant le démarrage des tests.

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du résultat de git status avant les tests.
</div>

---

## 3. Test 01 — Affichage de l'aide

### Objectif

Vérifier que le programme affiche l'aide lorsqu'il est lancé sans option.

### Commande à lancer

```bash
python src/main.py
```

### Résultat attendu

Le terminal doit afficher l'aide du programme avec les options disponibles, notamment :

- `--interactive` ;
- `--extract` ;
- `--categories` ;
- `--output` ;
- `--list` ;
- `--detail` ;
- `--quiet`.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran de l'aide affichée par python src/main.py.
</div>

---

## 4. Test 02 — Liste des catégories

### Objectif

Vérifier que le programme récupère et affiche les catégories du site Books to Scrape.

### Commande à lancer

```bash
python src/main.py --list categories
```

### Résultat attendu

Le terminal doit afficher une liste de catégories, par exemple :

```text
Travel
Mystery
Historical Fiction
Sequential Art
Classics
Philosophy
```

La catégorie globale `Books` ne doit pas apparaître dans la liste.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran de la liste des catégories.
</div>

---

## 5. Test 03 — Liste des livres d'une catégorie

### Objectif

Vérifier que le programme affiche les titres des livres d'une catégorie précise.

### Commande à lancer

```bash
python src/main.py --list books --categories "Fantasy"
```

### Résultat attendu

Le terminal doit afficher uniquement les titres des livres de la catégorie `Fantasy`.

Aucun détail complet de livre ne doit être affiché : seulement les titres.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran de la liste des livres de la catégorie Fantasy.
</div>

---

## 6. Test 04 — Détail d'un livre

### Objectif

Vérifier que le programme affiche les informations détaillées d'un livre précis.

### Commande à lancer

```bash
python src/main.py --detail "A Light in the Attic"
```

### Résultat attendu

Le terminal doit afficher les informations du livre, notamment :

- titre ;
- catégorie ;
- UPC ;
- prix TTC ;
- prix HT ;
- stock disponible ;
- note ;
- URL de l'image ;
- description.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du détail du livre A Light in the Attic.
</div>

---

## 7. Test 05 — Détail de plusieurs livres avec la nouvelle syntaxe

### Objectif

Vérifier que la nouvelle syntaxe de `--detail` accepte plusieurs titres après une seule option.

### Commande à lancer

```bash
python src/main.py --detail "A Light in the Attic" "Soulless"
```

### Résultat attendu

Le terminal doit afficher successivement les détails des deux livres :

- `A Light in the Attic` ;
- `Soulless`.

Le programme ne doit pas retourner d'erreur liée aux arguments.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du détail des deux livres avec la nouvelle syntaxe --detail.
</div>

---

## 8. Test 06 — Compatibilité avec l'ancienne syntaxe de `--detail`

### Objectif

Vérifier que l'ancienne syntaxe reste fonctionnelle.

### Commande à lancer

```bash
python src/main.py --detail "A Light in the Attic" --detail "Soulless"
```

### Résultat attendu

Le terminal doit afficher les détails des deux livres.

Ce test confirme que la modification de `--detail` n'a pas cassé l'ancienne utilisation.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du détail des deux livres avec l'ancienne syntaxe --detail répétée.
</div>

---

## 9. Test 07 — Titre contenant une virgule

### Objectif

Vérifier que les titres contenant une virgule sont correctement traités lorsqu'ils sont placés entre guillemets.

### Commande à lancer

```bash
python src/main.py --detail "Scott Pilgrim, Volume 1: Scott Pilgrim's Precious Little Life"
```

### Résultat attendu

Le programme doit rechercher le titre complet, sans découper le titre au niveau de la virgule.

Si le titre existe sur le site, ses détails doivent être affichés. Sinon, le message `Livre non trouvé` doit reprendre le titre complet.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du test avec un titre contenant une virgule.
</div>

---

## 10. Test 08 — Catégorie inexistante

### Objectif

Vérifier le comportement du programme lorsqu'une catégorie incorrecte est fournie.

### Commande à lancer

```bash
python src/main.py --list books --categories "CategorieInexistante"
```

### Résultat attendu

Le terminal doit afficher un message indiquant que la catégorie est inconnue ou qu'aucune catégorie n'est sélectionnée.

Le programme ne doit pas se fermer avec une erreur Python non maîtrisée.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du test avec une catégorie inexistante.
</div>

---

## 11. Test 09 — Extraction d'une catégorie

### Objectif

Vérifier qu'une extraction complète fonctionne sur une catégorie limitée.

### Commande à lancer

```bash
python src/main.py --extract --categories "Fantasy"
```

### Résultat attendu

Le programme doit :

- afficher la progression de l'extraction ;
- générer un fichier CSV dans `outputs/` ;
- générer un dossier d'images dans `images/` ;
- générer un fichier log dans `logs/` ;
- afficher un résumé final.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran de l'extraction de la catégorie Fantasy et du résumé final.
</div>

---

## 12. Test 10 — Extraction de plusieurs catégories

### Objectif

Vérifier que plusieurs catégories peuvent être extraites dans une seule exécution.

### Commande à lancer

```bash
python src/main.py --extract --categories "Classics,Philosophy"
```

### Résultat attendu

Le programme doit extraire les livres des catégories `Classics` et `Philosophy`.

Le résumé final doit afficher le nombre de livres extraits par catégorie et le total.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran de l'extraction des catégories Classics et Philosophy.
</div>

---

## 13. Test 11 — Utilisation d'un dossier de sortie personnalisé

### Objectif

Vérifier que l'option `--output` permet de choisir un dossier de sortie.

### Commande à lancer

```bash
python src/main.py --extract --categories "Fantasy" --output "./exports_test"
```

### Résultat attendu

Le programme doit générer :

```text
exports_test/books_extraction_YYYYMMDD_HHMMSS.csv
exports_test/images/books_extraction_YYYYMMDD_HHMMSS/
```

Le fichier log doit rester dans le dossier `logs/`.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du dossier exports_test et du résumé d'extraction.
</div>

---

## 14. Test 12 — Mode silencieux

### Objectif

Vérifier que le mode `--quiet` limite les sorties terminal tout en générant les fichiers attendus.

### Commande à lancer

```bash
python src/main.py --extract --categories "Fantasy" --quiet
```

### Résultat attendu

Le terminal doit rester silencieux ou presque silencieux.

Les fichiers doivent tout de même être générés :

- CSV ;
- images ;
- log.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du terminal après exécution en mode quiet et des fichiers générés.
</div>

---

## 15. Test 13 — Vérification du fichier CSV

### Objectif

Vérifier que le CSV généré contient les colonnes attendues.

### Commande à lancer

Remplacer le nom du fichier par le dernier CSV généré :

```bash
python - <<'PY'
import csv
from pathlib import Path

csv_files = sorted(Path('outputs').glob('books_extraction_*.csv'))
latest_csv = csv_files[-1]

with latest_csv.open(encoding='utf-8-sig', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    print(latest_csv)
    print(reader.fieldnames)
PY
```

### Résultat attendu

Le terminal doit afficher les colonnes suivantes :

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

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran des colonnes affichées depuis le dernier CSV généré.
</div>

---

## 16. Test 14 — Vérification des images

### Objectif

Vérifier que les images sont bien téléchargées localement.

### Commande à lancer

```bash
find images -type f | head
```

### Résultat attendu

Le terminal doit afficher plusieurs fichiers images.

Les noms doivent être lisibles et contenir des éléments comme :

- la catégorie ;
- le titre du livre ;
- l'UPC.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran de la liste des images téléchargées.
</div>

---

## 17. Test 15 — Vérification des logs

### Objectif

Vérifier que le fichier log est bien généré.

### Commande à lancer

```bash
ls -lt logs | head
```

### Résultat attendu

Le terminal doit afficher au moins un fichier de log nommé selon ce format :

```text
extraction_YYYYMMDD_HHMMSS.log
```

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran de la liste des fichiers logs.
</div>

---

## 18. Test 16 — Vérification que les fichiers générés ne sont pas versionnés

### Objectif

Vérifier que les fichiers générés ne sont pas ajoutés au dépôt Git.

### Commande à lancer

```bash
git status
```

### Résultat attendu

Les fichiers générés dans `outputs/`, `images/`, `logs/` ou `exports_test/` ne doivent pas être proposés comme fichiers à committer.

Si certains fichiers apparaissent, il faut vérifier le fichier `.gitignore`.

### Statut

- [ ] Réussi
- [ ] Échec

<div style="color:red; font-weight:bold; border:1px dashed red; padding:10px;">
🔴 À COLLER ICI : capture d'écran du git status après génération des fichiers.
</div>

---

## 19. Nettoyage après les tests

### Objectif

Supprimer les fichiers générés uniquement pour les tests si nécessaire.

### Commandes possibles

```bash
rm -rf exports_test
```

Les dossiers `outputs/`, `images/` et `logs/` peuvent être conservés localement le temps de préparer le ZIP demandé dans les livrables.

---

## 20. Validation finale

| Point de contrôle | Statut |
|---|---|
| L'aide s'affiche correctement | [ ] OK |
| Les catégories sont listées | [ ] OK |
| Les livres d'une catégorie sont listés | [ ] OK |
| Le détail d'un livre fonctionne | [ ] OK |
| Le détail de plusieurs livres fonctionne | [ ] OK |
| L'extraction d'une catégorie fonctionne | [ ] OK |
| L'extraction de plusieurs catégories fonctionne | [ ] OK |
| Le CSV est généré | [ ] OK |
| Les images sont téléchargées | [ ] OK |
| Les logs sont générés | [ ] OK |
| Les fichiers générés ne sont pas versionnés | [ ] OK |

---

## 21. Conclusion du protocole

Lorsque tous les tests sont validés, le projet peut être considéré comme prêt pour :

- la démonstration de soutenance ;
- la génération du fichier ZIP des données ;
- la remise du lien GitHub ;
- la remise du mail PDF décrivant le pipeline ETL.
