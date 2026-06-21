# Icônes, emojis et symboles — Cheat Sheet GitHub

> Référence pratique pour utiliser des emojis, icônes simples et symboles dans une documentation Markdown GitHub.
>
> Objectif : améliorer la lisibilité des README, documentations, issues, checklists, notes techniques et suivis de projet sans surcharger le contenu.

---

## Sommaire

- [1. Principes d'utilisation](#1-principes-dutilisation)
- [2. Statuts de validation](#2-statuts-de-validation)
- [3. Priorités et niveaux d'alerte](#3-priorités-et-niveaux-dalerte)
- [4. Progression et avancement](#4-progression-et-avancement)
- [5. Tests, qualité et bugs](#5-tests-qualité-et-bugs)
- [6. Documentation et apprentissage](#6-documentation-et-apprentissage)
- [7. Git, GitHub et versionnement](#7-git-github-et-versionnement)
- [8. Python et développement](#8-python-et-développement)
- [9. Fichiers, dossiers et données](#9-fichiers-dossiers-et-données)
- [10. Sécurité et confidentialité](#10-sécurité-et-confidentialité)
- [11. Réseau, API et web](#11-réseau-api-et-web)
- [12. Interface utilisateur et expérience utilisateur](#12-interface-utilisateur-et-expérience-utilisateur)
- [13. Performance, optimisation et monitoring](#13-performance-optimisation-et-monitoring)
- [14. Communication et collaboration](#14-communication-et-collaboration)
- [15. Symboles techniques utiles](#15-symboles-techniques-utiles)
- [16. Exemples prêts à copier](#16-exemples-prêts-à-copier)
- [17. GitHub shortcodes utiles](#17-github-shortcodes-utiles)
- [18. Bonnes pratiques](#18-bonnes-pratiques)
- [19. Mini-référence rapide](#19-mini-référence-rapide)

---

## 1. Principes d'utilisation

Les emojis et symboles peuvent rendre une documentation plus lisible, à condition de rester sobres.

Ils sont utiles pour :

- signaler un statut ;
- attirer l'attention sur un point important ;
- structurer visuellement une liste ;
- rendre un README plus agréable à parcourir ;
- distinguer rapidement les étapes terminées, en cours ou bloquées ;
- améliorer la lecture d'une documentation technique.

### Exemple simple

### Code Markdown

~~~md
## ✅ Fonctionnalités terminées

- ✅ Export CSV
- ✅ Téléchargement des images
- 🔄 Nettoyage du code en cours
- ⏳ Tests à compléter
~~~

### Résultat

## ✅ Fonctionnalités terminées

- ✅ Export CSV
- ✅ Téléchargement des images
- 🔄 Nettoyage du code en cours
- ⏳ Tests à compléter

### Règle simple

Utiliser les emojis comme des repères visuels, pas comme de la décoration excessive.

---

## 2. Statuts de validation

| Symbole | Signification possible | Exemple d'utilisation |
|---|---|---|
| ✅ | Fait / validé / réussi | `✅ Tests passés` |
| ❌ | Erreur / échec / refusé | `❌ Build échoué` |
| ⚠️ | Attention / risque | `⚠️ Configuration à vérifier` |
| ℹ️ | Information | `ℹ️ Compatible Python 3.12` |
| 🟢 | OK / opérationnel | `🟢 Service disponible` |
| 🟡 | À surveiller / partiel | `🟡 Couverture de tests incomplète` |
| 🔴 | Critique / bloqué | `🔴 API indisponible` |
| 🔵 | Information neutre | `🔵 Note technique` |
| 🟣 | Amélioration / optionnel | `🟣 Idée d'évolution` |
| ⚪ | Non démarré / neutre | `⚪ Tâche non commencée` |

### Exemple checklist projet

### Code Markdown

~~~md
## Suivi du projet

| Statut | Élément |
|---|---|
| ✅ | Environnement virtuel créé |
| ✅ | Dépendances installées |
| 🟡 | README à compléter |
| 🔴 | Tests non écrits |
| ⚪ | Documentation utilisateur à faire |
~~~

### Résultat

## Suivi du projet

| Statut | Élément |
|---|---|
| ✅ | Environnement virtuel créé |
| ✅ | Dépendances installées |
| 🟡 | README à compléter |
| 🔴 | Tests non écrits |
| ⚪ | Documentation utilisateur à faire |

---

## 3. Priorités et niveaux d'alerte

| Symbole | Niveau | Usage possible |
|---|---|---|
| 🔴 | Critique | Blocage, erreur majeure, sécurité |
| 🟠 | Élevé | À traiter rapidement |
| 🟡 | Moyen | À surveiller |
| 🟢 | Faible / OK | Fonctionnel ou non prioritaire |
| 🚨 | Urgent | Incident, panne, faille critique |
| ⚠️ | Attention | Risque ou point sensible |
| 🛑 | Stop | Ne pas continuer sans correction |
| ⛔ | Interdit / bloqué | Action non autorisée |
| ❗ | Important | Point à ne pas manquer |
| ❓ | Question | Point à clarifier |

### Exemple dans une issue GitHub

### Code Markdown

~~~md
## 🔴 Problème critique

Le script s'arrête lors de l'export CSV.

## ⚠️ Impact

- Aucun fichier n'est généré.
- Les images sont téléchargées mais non référencées.

## ✅ Résultat attendu

Le script doit créer un fichier CSV par catégorie.
~~~

---

## 4. Progression et avancement

| Symbole | Signification |
|---|---|
| ⏳ | En attente |
| 🔄 | En cours |
| 🚧 | En construction |
| 🧪 | En test |
| 📝 | À rédiger |
| 📌 | À faire / point important |
| ✅ | Terminé |
| 🏁 | Fin / objectif atteint |
| ⏭️ | Étape suivante |
| 🔜 | À venir |
| 📅 | Planifié |
| 🕒 | Temps / délai |

### Exemple roadmap

### Code Markdown

~~~md
## Roadmap

- ✅ Initialiser le dépôt
- ✅ Créer l'environnement Python
- 🔄 Développer le module d'extraction
- 🧪 Ajouter les tests
- 📝 Compléter la documentation
- 🏁 Préparer la soutenance
~~~

### Résultat

## Roadmap

- ✅ Initialiser le dépôt
- ✅ Créer l'environnement Python
- 🔄 Développer le module d'extraction
- 🧪 Ajouter les tests
- 📝 Compléter la documentation
- 🏁 Préparer la soutenance

---

## 5. Tests, qualité et bugs

| Symbole | Usage |
|---|---|
| 🧪 | Tests |
| ✅ | Test réussi |
| ❌ | Test échoué |
| 🐛 | Bug |
| 🐞 | Bug mineur |
| 🔍 | Analyse / inspection |
| 🧹 | Nettoyage du code |
| ♻️ | Refactoring |
| 🧰 | Outils de qualité |
| 📊 | Couverture / métriques |
| 🧯 | Correction urgente |
| 🩹 | Patch / correction rapide |

### Exemple rapport de test

### Code Markdown

~~~md
## 🧪 Résultat des tests

| Élément | Statut | Commentaire |
|---|---|---|
| Tests unitaires | ✅ | Tous les tests passent |
| Tests d'intégration | 🟡 | À compléter |
| Couverture | 📊 | Couverture partielle |
| Bugs connus | 🐛 | 1 bug mineur identifié |
~~~

### Résultat

## 🧪 Résultat des tests

| Élément | Statut | Commentaire |
|---|---|---|
| Tests unitaires | ✅ | Tous les tests passent |
| Tests d'intégration | 🟡 | À compléter |
| Couverture | 📊 | Couverture partielle |
| Bugs connus | 🐛 | 1 bug mineur identifié |

---

## 6. Documentation et apprentissage

| Symbole | Usage |
|---|---|
| 📚 | Documentation |
| 📖 | Guide / lecture |
| 📝 | Note / rédaction |
| ✏️ | Modification |
| 🧠 | Concept / compréhension |
| 💡 | Idée / astuce |
| 🗒️ | Notes |
| 📌 | Point à retenir |
| 🔗 | Lien utile |
| 🧭 | Orientation / guide |
| 🗂️ | Organisation |
| 🧾 | Procédure / compte rendu |

### Exemple section documentation

### Code Markdown

~~~md
## 📚 Documentation

- 📖 [Guide d'installation](docs/installation.md)
- 🧾 [Procédure de test](docs/protocole_tests.md)
- 🗂️ [Structure du projet](docs/architecture.md)
- 💡 [Bonnes pratiques](docs/bonnes_pratiques.md)
~~~

---

## 7. Git, GitHub et versionnement

| Symbole | Usage |
|---|---|
| 🌿 | Branche Git |
| 🔀 | Merge / fusion |
| 📦 | Release / paquet |
| 🏷️ | Tag / version |
| 🧩 | Pull request / composant |
| 👀 | Review / à relire |
| ✅ | Pull request validée |
| 🔒 | Branche protégée / sécurité |
| 📝 | Commit / message |
| ⬆️ | Push / montée |
| ⬇️ | Pull / récupération |
| 🔁 | Synchronisation |

### Exemple workflow Git

### Code Markdown

~~~md
## 🔁 Workflow Git

1. 🌿 Créer une branche de travail
2. 📝 Commiter les modifications
3. ⬆️ Pousser la branche sur GitHub
4. 🧩 Ouvrir une pull request
5. 👀 Faire relire le code
6. 🔀 Fusionner dans `main`
~~~

---

## 8. Python et développement

| Symbole | Usage |
|---|---|
| 🐍 | Python |
| ⚙️ | Configuration |
| 🧱 | Architecture / structure |
| 🧩 | Module / composant |
| 🧮 | Algorithme / calcul |
| 🔁 | Boucle / répétition |
| 🔀 | Condition / choix |
| 🧰 | Outil / utilitaire |
| 🖥️ | Programme / application |
| 🧵 | Processus / thread |
| 🧪 | Test |
| 🐛 | Bug |

### Exemple README Python

### Code Markdown

~~~md
# 🐍 Projet Python

## ⚙️ Installation

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

## 🖥️ Utilisation

```bash
python main.py
```

## 🧪 Tests

```bash
pytest
```
~~~

---

## 9. Fichiers, dossiers et données

| Symbole | Usage |
|---|---|
| 📁 | Dossier |
| 📂 | Dossier ouvert |
| 📄 | Fichier |
| 🧾 | Document / rapport |
| 📑 | Plusieurs documents |
| 🗃️ | Archive / stockage |
| 🗄️ | Base de données |
| 📊 | Données / statistiques |
| 📈 | Progression / graphique montant |
| 📉 | Baisse / graphique descendant |
| 🧮 | Calcul |
| 🖼️ | Image |
| 🗜️ | Compression / archive |

### Exemple structure documentaire

### Code Markdown

~~~md
## 📁 Structure documentaire

- 📄 `README.md` : documentation principale
- 📁 `docs/` : documentation détaillée
- 📁 `src/` : code source Python
- 📁 `tests/` : tests automatisés
- 📁 `outputs/` : fichiers générés
~~~

---

## 10. Sécurité et confidentialité

| Symbole | Usage |
|---|---|
| 🔒 | Sécurité / verrouillé |
| 🔓 | Déverrouillé |
| 🛡️ | Protection |
| 🔐 | Authentification |
| 🧑‍💻 | Utilisateur / compte |
| 🕵️ | Audit / investigation |
| 🚨 | Alerte sécurité |
| ⚠️ | Attention |
| ⛔ | Interdit |
| 🧯 | Incident à corriger |
| 🔑 | Clé / token |
| 🧬 | Donnée sensible |

### Exemple avertissement sécurité

### Code Markdown

~~~md
> [!CAUTION]
> 🔒 Ne jamais commiter de mot de passe, token, clé API ou fichier `.env`.
~~~

### Résultat

> [!CAUTION]
> 🔒 Ne jamais commiter de mot de passe, token, clé API ou fichier `.env`.

---

## 11. Réseau, API et web

| Symbole | Usage |
|---|---|
| 🌐 | Web / Internet |
| 🔗 | Lien / URL |
| 🔌 | API / connexion |
| 📡 | Réseau / communication |
| 🛰️ | Service distant |
| 🖧 | Infrastructure réseau |
| 🔐 | Authentification |
| 🧭 | Endpoint / route |
| 📥 | Entrée / téléchargement |
| 📤 | Sortie / envoi |
| 🔁 | Requête / synchronisation |
| 🧾 | Réponse / payload |

### Exemple documentation API

### Code Markdown

~~~md
## 🔌 API

| Méthode | Endpoint | Description |
|---|---|---|
| `GET` | `/api/books/` | 📥 Récupère la liste des livres |
| `POST` | `/api/books/` | 📤 Ajoute un livre |
| `DELETE` | `/api/books/{id}` | 🗑️ Supprime un livre |
~~~

---

## 12. Interface utilisateur et expérience utilisateur

| Symbole | Usage |
|---|---|
| 🖥️ | Interface / écran |
| 🎨 | Design / style |
| 🧭 | Navigation |
| 🖱️ | Clic / interaction |
| ⌨️ | Saisie clavier |
| 📱 | Mobile |
| 🧑‍💻 | Utilisateur |
| 👁️ | Visibilité |
| ♿ | Accessibilité |
| 🧪 | Test utilisateur |
| 💬 | Message utilisateur |
| 🪟 | Fenêtre / page |

### Exemple section UI

### Code Markdown

~~~md
## 🎨 Interface utilisateur

- 🧭 Navigation simple
- ♿ Interface accessible
- 🖱️ Boutons clairement identifiables
- 💬 Messages d'erreur compréhensibles
~~~

---

## 13. Performance, optimisation et monitoring

| Symbole | Usage |
|---|---|
| 🚀 | Performance / lancement |
| ⚡ | Rapidité |
| 🐢 | Lent / à optimiser |
| 📊 | Métriques |
| 📈 | Amélioration |
| 🔍 | Analyse |
| 🧠 | Optimisation logique |
| 🧮 | Complexité / calcul |
| 🕒 | Temps d'exécution |
| 🧵 | Concurrence / thread |
| 🧯 | Incident performance |
| 📡 | Monitoring |

### Exemple suivi de performance

### Code Markdown

~~~md
## 🚀 Performance

| Élément | Statut | Commentaire |
|---|---|---|
| Temps d'exécution | ⚡ | Correct |
| Mémoire | 🟡 | À surveiller |
| Requêtes HTTP | 🐢 | Optimisation possible |
| Logs | 📡 | Monitoring à ajouter |
~~~

---

## 14. Communication et collaboration

| Symbole | Usage |
|---|---|
| 💬 | Discussion |
| 🙋 | Question |
| 🤝 | Collaboration |
| 👀 | Relecture |
| 🧑‍🏫 | Mentor / accompagnement |
| 📣 | Annonce |
| 📌 | Point important |
| 📝 | Compte rendu |
| ✅ | Accord / validé |
| ❓ | Question ouverte |
| 💡 | Proposition |
| 🔄 | Retour / itération |

### Exemple compte rendu

### Code Markdown

~~~md
## 📝 Compte rendu

- ✅ Point validé : structure du projet
- ❓ Question : format final des exports CSV
- 💡 Proposition : ajouter un dossier par catégorie
- 🔄 Action suivante : mettre à jour `load.py`
~~~

---

## 15. Symboles techniques utiles

Ces symboles sont sobres et peuvent être utiles dans une documentation technique.

| Symbole | Usage possible |
|---|---|
| → | Étape suivante / transformation |
| ← | Retour / provenance |
| ↔ | Échange / relation bidirectionnelle |
| ⇒ | Conséquence |
| ⇐ | Dépendance inverse |
| ≠ | Différent |
| = | Égal |
| ≈ | Environ égal |
| ≤ | Inférieur ou égal |
| ≥ | Supérieur ou égal |
| ± | Plus ou moins |
| ∞ | Infini / illimité |
| ∅ | Vide / aucun résultat |
| # | Numéro / identifiant |
| @ | Mention / utilisateur |

### Exemple flux simple

### Code Markdown

~~~md
CSV brut → nettoyage → transformation → export CSV final
~~~

### Résultat

CSV brut → nettoyage → transformation → export CSV final

### Exemple comparaison

### Code Markdown

~~~md
- Version attendue ≥ Python 3.12
- Nombre d'erreurs = 0
- Résultat ≠ `None`
~~~

### Résultat

- Version attendue ≥ Python 3.12
- Nombre d'erreurs = 0
- Résultat ≠ `None`

---

## 16. Exemples prêts à copier

### Statuts de fonctionnalités

~~~md
## Fonctionnalités

| Statut | Fonctionnalité |
|---|---|
| ✅ | Extraction des données |
| ✅ | Transformation des données |
| 🔄 | Export CSV par catégorie |
| ⏳ | Téléchargement des images |
| 📝 | Documentation utilisateur |
~~~

### Suivi de bugs

~~~md
## 🐛 Bugs connus

| Priorité | Bug | Statut |
|---|---|---|
| 🔴 | Le script s'arrête si une image est manquante | 🔄 En cours |
| 🟡 | Certaines catégories créent des noms de dossiers trop longs | ⏳ À traiter |
| 🟢 | Message terminal peu clair | 📝 À améliorer |
~~~

### README avec titres visuels

~~~md
# 🐍 Nom du projet

## 📌 Présentation

## ⚙️ Installation

## 🖥️ Utilisation

## 📁 Structure du projet

## 🧪 Tests

## 📚 Documentation

## 🚀 Améliorations possibles
~~~

### Avertissements GitHub

~~~md
> [!NOTE]
> ℹ️ Cette commande doit être exécutée depuis la racine du projet.

> [!WARNING]
> ⚠️ Cette action supprime les fichiers générés dans `outputs/`.

> [!CAUTION]
> 🔒 Ne jamais publier de secret dans le dépôt.
~~~

### Checklist de soutenance

~~~md
## 🏁 Checklist avant soutenance

- [x] ✅ Code poussé sur GitHub
- [x] ✅ README à jour
- [x] ✅ Captures d'écran ajoutées
- [ ] 🧪 Tests vérifiés
- [ ] 📝 Notes de présentation préparées
- [ ] 💬 Questions possibles anticipées
~~~

### Journal de progression

~~~md
## 📅 Journal de progression

| Date | Avancement | Commentaire |
|---|---|---|
| 2026-06-21 | ✅ Initialisation | Dépôt créé et première documentation ajoutée |
| 2026-06-22 | 🔄 Développement | Mise en place de la structure du projet |
| 2026-06-23 | 🧪 Tests | Premiers tests unitaires |
~~~

---

## 17. GitHub shortcodes utiles

GitHub accepte aussi certains codes textuels d'emojis, appelés shortcodes.

Exemple :

~~~md
:rocket: Déploiement terminé
:white_check_mark: Tests validés
:warning: Point à vérifier
~~~

Selon la plateforme, ces codes peuvent être transformés en emojis.

| Shortcode | Rendu attendu | Usage |
|---|---|---|
| `:white_check_mark:` | ✅ | Validé |
| `:x:` | ❌ | Erreur |
| `:warning:` | ⚠️ | Attention |
| `:information_source:` | ℹ️ | Information |
| `:rocket:` | 🚀 | Lancement / performance |
| `:bug:` | 🐛 | Bug |
| `:memo:` | 📝 | Note |
| `:books:` | 📚 | Documentation |
| `:lock:` | 🔒 | Sécurité |
| `:key:` | 🔑 | Clé / accès |
| `:gear:` | ⚙️ | Configuration |
| `:package:` | 📦 | Package / release |
| `:mag:` | 🔍 | Recherche / analyse |
| `:construction:` | 🚧 | En construction |
| `:hourglass_flowing_sand:` | ⏳ | En attente |
| `:eyes:` | 👀 | Relecture |
| `:bulb:` | 💡 | Idée |
| `:link:` | 🔗 | Lien |
| `:file_folder:` | 📁 | Dossier |
| `:page_facing_up:` | 📄 | Fichier |

### Exemple avec shortcodes

### Code Markdown

~~~md
## :rocket: Déploiement

- :white_check_mark: Build terminé
- :warning: Variables d'environnement à vérifier
- :bug: Bug mineur connu
~~~

---

## 18. Bonnes pratiques

### À faire

- Utiliser les emojis pour faciliter la lecture.
- Garder une logique constante dans tout le document.
- Préférer les symboles simples et compréhensibles.
- Utiliser les mêmes couleurs pour les mêmes niveaux de priorité.
- Garder un README professionnel et lisible.
- Ajouter les emojis surtout dans les titres, tableaux, checklists et notes importantes.

### À éviter

- Mettre trop d'emojis dans un même paragraphe.
- Utiliser des emojis ambigus.
- Mélanger plusieurs symboles pour le même statut.
- Remplacer une explication claire par un emoji seul.
- Utiliser des emojis dans des noms de fichiers ou de dossiers.
- Utiliser trop de couleurs différentes dans une documentation technique.

### Convention simple recommandée

| Situation | Symbole conseillé |
|---|---|
| Terminé | ✅ |
| En cours | 🔄 |
| À faire | ⏳ |
| Problème | ❌ |
| Attention | ⚠️ |
| Critique | 🔴 |
| Information | ℹ️ |
| Documentation | 📚 |
| Test | 🧪 |
| Bug | 🐛 |
| Sécurité | 🔒 |
| Idée | 💡 |

---

## 19. Mini-référence rapide

| Besoin | Symbole conseillé |
|---|---|
| Validé | ✅ |
| Erreur | ❌ |
| Attention | ⚠️ |
| Information | ℹ️ |
| Critique | 🔴 |
| OK | 🟢 |
| En cours | 🔄 |
| En attente | ⏳ |
| En construction | 🚧 |
| À rédiger | 📝 |
| Documentation | 📚 |
| Fichier | 📄 |
| Dossier | 📁 |
| Python | 🐍 |
| Tests | 🧪 |
| Bug | 🐛 |
| Sécurité | 🔒 |
| API | 🔌 |
| Web | 🌐 |
| Performance | 🚀 |
| Analyse | 🔍 |
| Idée | 💡 |
| Relecture | 👀 |
| Collaboration | 🤝 |
| Release | 📦 |
| Version | 🏷️ |

---

## Exemple final de section README

~~~md
# 🐍 Projet Python — Analyse de marché

## 📌 Présentation

Ce projet extrait, transforme et exporte des données issues d'un site web.

## ✅ Fonctionnalités

- ✅ Extraction des données
- ✅ Export CSV
- 🔄 Téléchargement des images
- 🧪 Tests à compléter

## ⚙️ Installation

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

## 🧪 Tests

```bash
pytest
```

## ⚠️ Points d'attention

- Ne pas versionner `.venv/`.
- Ne pas publier de secrets.
- Vérifier les fichiers générés dans `outputs/`.
~~~

---

Document créé comme base de référence pour améliorer la lisibilité des documentations Markdown GitHub.
