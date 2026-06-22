# Glossaire Python utilisé — OC-PY02

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel  
**Objectif :** expliquer les notions Python utilisées dans le projet.

---

## 1. Fonction

Une fonction est un bloc de code réutilisable qui réalise une tâche précise.

Exemple dans le projet :

```python
def clean_text(text):
    return " ".join(text.split())
```

Utilité dans le projet :

- éviter de répéter le même code ;
- séparer les responsabilités ;
- rendre le programme plus lisible.

---

## 2. Paramètre

Un paramètre est une valeur reçue par une fonction.

Exemple :

```python
def get_soup(page_url, retries=3, timeout=20):
```

Ici :

- `page_url` est l'URL à récupérer ;
- `retries` est le nombre de tentatives ;
- `timeout` est le temps maximum d'attente.

---

## 3. Return

`return` permet à une fonction de renvoyer un résultat.

Exemple :

```python
return categories
```

Dans le projet, les fonctions renvoient souvent :

- une liste ;
- un dictionnaire ;
- un chemin de fichier ;
- un booléen ;
- un objet BeautifulSoup.

---

## 4. Liste

Une liste est une collection ordonnée d'éléments.

Exemple :

```python
book_links = []
```

Dans le projet, les listes servent notamment à stocker :

- les livres d'une catégorie ;
- les livres transformés ;
- les chemins des CSV générés.

---

## 5. Dictionnaire

Un dictionnaire stocke des données sous forme clé / valeur.

Exemple :

```python
{
    "title": "A Light in the Attic",
    "category": "Poetry"
}
```

Dans le projet, les dictionnaires servent à représenter :

- les catégories ;
- un livre ;
- les livres groupés par catégorie ;
- le résumé d'extraction.

---

## 6. Boucle `for`

Une boucle `for` permet de parcourir plusieurs éléments.

Exemple :

```python
for category_name, category_url in selected_categories.items():
```

Dans le projet, les boucles servent à parcourir :

- les catégories ;
- les pages d'une catégorie ;
- les livres ;
- les lignes à écrire dans un CSV.

---

## 7. Condition `if`

Une condition permet d'exécuter du code uniquement si une situation est vraie.

Exemple :

```python
if args.extract:
```

Dans le projet, les conditions servent à :

- choisir le mode d'exécution ;
- gérer les options CLI ;
- vérifier si une donnée HTML existe ;
- ignorer une catégorie inconnue ;
- afficher ou non les messages avec `--quiet`.

---

## 8. `try / except`

`try / except` permet de gérer une erreur sans arrêter tout le programme.

Exemple simplifié :

```python
try:
    details = extract_book_details(book)
except Exception as error:
    logger.exception(error)
```

Dans le projet, cette structure permet de :

- gérer les erreurs réseau ;
- continuer l'extraction si un livre échoue ;
- écrire les erreurs dans les logs.

---

## 9. Import

`import` permet d'utiliser du code situé dans un autre module.

Exemple :

```python
import csv
from pathlib import Path
```

Dans le projet, les imports permettent d'utiliser :

- des modules standards Python ;
- des packages installés avec `pip` ;
- les fonctions internes du package `books_scraper`.

---

## 10. Module

Un module est un fichier Python contenant du code.

Exemples :

```text
extract.py
transform.py
load.py
logger_config.py
```

Chaque module a un rôle spécifique :

- extraction ;
- transformation ;
- chargement ;
- logs.

---

## 11. Package Python

Un package est un dossier contenant des modules Python et un fichier `__init__.py`.

Dans le projet :

```text
books_scraper/
├── __init__.py
├── extract.py
├── transform.py
├── load.py
└── logger_config.py
```

Cela permet d'importer les fonctions avec :

```python
from books_scraper.extract import extract_categories
```

---

## 12. `argparse`

`argparse` est un module standard Python qui permet de créer une interface en ligne de commande.

Dans le projet, il permet d'utiliser :

```bash
python src/main.py --extract --categories "Fantasy"
```

Options gérées :

- `--interactive` ;
- `--extract` ;
- `--categories` ;
- `--output` ;
- `--list` ;
- `--detail` ;
- `--quiet`.

---

## 13. `pathlib.Path`

`Path` permet de manipuler les chemins de fichiers de manière propre.

Exemple :

```python
export_dir = Path.cwd() / "outputs" / extraction_name
```

Dans le projet, `Path` sert à :

- créer les dossiers d'export ;
- créer les dossiers de catégorie ;
- écrire les CSV ;
- enregistrer les images ;
- créer les logs.

---

## 14. `requests`

`requests` est un package qui permet d'effectuer des requêtes HTTP.

Dans le projet, il sert à :

- récupérer les pages HTML ;
- télécharger les images.

Exemple :

```python
response = requests.get(page_url, timeout=timeout)
```

---

## 15. Beautiful Soup

Beautiful Soup est utilisé pour analyser le HTML.

Exemple :

```python
soup.select("article.product_pod")
```

Dans le projet, Beautiful Soup permet de récupérer :

- les catégories ;
- les livres ;
- le tableau `Product Information` ;
- la description ;
- la note ;
- l'image.

---

## 16. Sélecteur CSS

Un sélecteur CSS permet de cibler un élément HTML.

Exemples :

```python
soup.select("article.product_pod")
soup.select_one("p.star-rating")
```

Dans le projet, les sélecteurs CSS permettent de trouver les blocs utiles dans les pages HTML.

---

## 17. `urljoin`

`urljoin` transforme une URL relative en URL complète.

Exemple :

```python
product_page_url = urljoin(page_url, product_relative_url)
```

Utilité :

Le site contient parfois des liens relatifs. Pour télécharger ou ouvrir une page, le programme a besoin d'une URL complète.

---

## 18. Expression régulière

Une expression régulière permet de rechercher un motif dans un texte.

Dans le projet :

```python
match = re.search(r"\d+", availability)
```

Cela permet d'extraire le stock depuis un texte comme :

```text
In stock (22 available)
```

Résultat :

```text
22
```

---

## 19. `csv.DictWriter`

`csv.DictWriter` permet d'écrire des dictionnaires dans un fichier CSV.

Dans le projet, chaque livre est un dictionnaire, donc `DictWriter` est adapté.

Exemple simplifié :

```python
writer = csv.DictWriter(csv_file, fieldnames=CSV_HEADERS)
writer.writeheader()
writer.writerow(book)
```

---

## 20. `logging`

`logging` permet d'écrire des informations dans un fichier log.

Dans le projet, les logs servent à :

- tracer le début d'une catégorie ;
- tracer les fichiers générés ;
- enregistrer les erreurs ;
- éviter d'afficher trop d'informations dans le terminal.

---

## 21. `tqdm`

`tqdm` affiche une barre de progression dans le terminal.

Dans le projet, elle est utilisée pendant la boucle sur les livres :

```python
for book in tqdm(book_links, desc=f"Extraction {category_name}"):
```

Cela permet de suivre l'avancement de l'extraction.

---

## 22. `python-slugify`

`python-slugify` transforme un texte en nom propre pour un fichier ou un dossier.

Exemple :

```text
Historical Fiction → historical-fiction
```

Dans le projet, il sert à créer :

- les noms de dossiers de catégories ;
- les noms de fichiers CSV ;
- les noms d'images.

---

## 23. Encodage `utf-8-sig`

`utf-8-sig` est utilisé lors de l'écriture du CSV.

Objectif :

- conserver les caractères spéciaux ;
- faciliter l'ouverture du fichier CSV dans Excel.

---

## 24. Mode silencieux `--quiet`

Le mode `--quiet` limite les sorties dans le terminal pendant l'extraction.

Il est utile pour :

- lancer une extraction automatisée ;
- éviter d'afficher trop de messages ;
- conserver les informations dans les logs.

---

## 25. Structure ETL

Le programme peut être résumé ainsi :

```text
Extract   → récupérer HTML, catégories, livres, détails
Transform → nettoyer textes, convertir stock et note
Load      → écrire CSV, sauvegarder images, créer logs
```

Cette séparation rend le programme plus lisible et plus facile à expliquer pendant la soutenance.
