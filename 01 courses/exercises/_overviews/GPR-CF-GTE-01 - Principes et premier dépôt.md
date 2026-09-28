# Exercices — GPR-CF-GTE-01 — Principes et premier dépôt

> Cours associé : [[01 courses/slides/C++/GPR-CF-GTE-01 - Principes et premier dépôt|GPR-CF-GTE-01 - Principes et premier dépôt]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. La séance étant déjà publiée, cette
> fiche attend dans `_overviews/` et ne partira en ligne qu'une fois les énoncés écrits.

Tout se rend en historique de dépôt et en captures de commandes.

## Courts — valider la compréhension

### 1 — Instantané ou différence
Faire trois commits successifs sur un fichier, puis expliquer, avec la sortie de `git log` et de `git show`, ce que Git a réellement enregistré à chaque fois.

### 2 — La zone d'index
Modifier trois fichiers, n'en indexer qu'un, committer, et montrer par `git status` l'état des deux autres. Dire à quoi sert cette étape intermédiaire.

### 3 — Récupérer un dépôt
Cloner un dépôt existant, y trouver la ligne de code demandée, et retrouver dans l'historique le commit qui l'a introduite.

### 4 — Le fichier qui ne doit pas entrer
Ajouter un dossier de build au dépôt par erreur, constater son poids, l'en retirer, puis écrire le `.gitignore` qui l'aurait évité.

## Complet — reprendre toute la séance

### 5 — Le dépôt du projet de l'année
Transformer un dossier de projet existant en dépôt propre : premier commit qui ne contient que ce qui doit y être, `.gitignore` adapté au C++ et à l'IDE, message de commit lisible, dépôt distant créé et poussé, et un fichier de présentation qui dit ce qu'est le projet et comment le compiler. Le rendu est l'URL du dépôt et la capture de son historique.

## Difficile — se projeter

### 6 — L'archéologie
Sur un dépôt fourni de quelques centaines de commits, répondre par des commandes à cinq questions : qui a introduit ce bug, quand cette ligne a-t-elle changé de sens, quel commit a fait grossir le dépôt, quel fichier change le plus souvent, et quelle version était en place à une date donnée. Rendre les commandes utilisées autant que les réponses — c'est l'outillage qui compte.
