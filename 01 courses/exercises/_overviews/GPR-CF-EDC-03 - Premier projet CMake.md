# Exercices — GPR-CF-EDC-03 — Premier projet CMake

> Cours associé : [[01 courses/slides/C++/GPR-CF-EDC-03  - Premier projet CMake|GPR-CF-EDC-03 - Premier projet CMake]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. La séance étant déjà publiée, cette
> fiche attend dans `_overviews/` et ne partira en ligne qu'une fois les énoncés écrits.

Tout se rend sous forme de `CMakeLists.txt` commentés et de sorties de configuration.

## Courts — valider la compréhension

### 1 — Le projet minimal
Écrire le plus petit `CMakeLists.txt` qui compile un `main.cpp`, configurer, générer, compiler, exécuter. Rendre les six lignes du fichier et la sortie de configuration.

### 2 — Ce que CMake fabrique
Lister ce qui apparaît dans le dossier de build après la configuration, et dire lesquels de ces fichiers doivent être ignorés par Git et pourquoi.

### 3 — Deux fichiers, une cible
Ajouter un second couple de fichiers au projet, l'intégrer à la cible, et montrer ce qui se passe quand on oublie de déclarer le nouveau source.

### 4 — Lier une bibliothèque
Lier une bibliothèque déjà installée, provoquer l'erreur du lien manquant, lire le message de l'éditeur de liens, puis corriger.

## Complet — reprendre toute la séance

### 5 — Le squelette de projet de l'année
Un projet propre et réutilisable : arborescence source et include séparées, standard C++ imposé, avertissements activés, une dépendance externe trouvée et liée, un dossier de build hors du dépôt, et une cible exécutable qui se lance depuis l'IDE. Le fichier est commenté ligne par ligne pour être relu dans six mois, et le dépôt contient le `.gitignore` correspondant.

## Difficile — se projeter

### 6 — Une bibliothèque, deux exécutables
Découper le projet en une bibliothèque de gameplay et deux exécutables — le jeu et un petit banc de test — qui la partagent sans la recompiler deux fois. Ajouter une option de configuration qui active ou non le banc de test, vérifier que la configuration et la compilation restent correctes dans les deux cas, et mesurer le temps gagné à la recompilation. Prolongement : dire comment cette découpe prépare l'arrivée des tests automatisés.
