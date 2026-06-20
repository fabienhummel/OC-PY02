# Annexe — Packages Python

**Projet :** OC-PY02 — Analyse de marché avec Python  
**Auteur :** Fabien Hummel

## Packages principaux

| Package | Utilité |
|---|---|
| `requests` | Récupérer les pages HTML et télécharger les images. |
| `beautifulsoup4` | Analyser le HTML et extraire les données. |
| `questionary` | Afficher les menus interactifs dans le terminal. |
| `tqdm` | Afficher une barre de progression pendant l'extraction. |
| `python-slugify` | Créer des noms de fichiers propres pour les images. |

## Dépendances indirectes

| Package | Utilité |
|---|---|
| `certifi` | Gestion des certificats HTTPS. |
| `charset-normalizer` | Gestion de l'encodage texte. |
| `idna` | Gestion des noms de domaine. |
| `urllib3` | Couche réseau utilisée par `requests`. |
| `soupsieve` | Sélecteurs CSS utilisés par Beautiful Soup. |
| `prompt_toolkit` | Interface terminal utilisée par `questionary`. |
| `wcwidth` | Affichage des caractères dans le terminal. |
| `text-unidecode` | Conversion de caractères pour `python-slugify`. |
| `typing_extensions` | Fonctions de typage complémentaires. |

## Modules standards utilisés

| Module | Utilité |
|---|---|
| `argparse` | Options en ligne de commande. |
| `csv` | Écriture du fichier CSV. |
| `datetime` | Date et heure dans les noms de fichiers. |
| `logging` | Fichier log. |
| `pathlib` | Gestion des chemins. |
| `re` | Extraction du nombre disponible. |
| `sys` | Gestion des arguments du script. |
| `time` | Attente entre deux tentatives réseau. |
| `urllib.parse.urljoin` | Conversion des URL relatives en URL absolues. |
