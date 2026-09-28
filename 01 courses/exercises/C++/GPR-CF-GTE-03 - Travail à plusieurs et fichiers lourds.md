# Exercices — GPR-CF-GTE-03 — Travail à plusieurs et fichiers lourds

> Cours associé : [[01 courses/slides/C++/GPR-CF-GTE-03 - Travail à plusieurs et fichiers lourds|GPR-CF-GTE-03 - Travail à plusieurs et fichiers lourds]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les dépôts de
> départ et les corrigés viendront après validation de ces pistes.

Terrain de jeu : un dépôt de projet Unity fourni, avec des textures, des sons, et un dossier de build oublié dedans.

## Courts — valider la compréhension

### 1 — Regarder sans intégrer
Faire un `fetch`, montrer ce qui a changé sur le remote sans que la copie de travail bouge, puis intégrer. Dire ce que `pull` aurait fait des deux gestes à la fois.

### 2 — Un message par intention
Cinq commits mal nommés à réécrire, chacun avec une intention identifiable. Donner la règle d'équipe qui en découle, en trois lignes maximum.

### 3 — La version jouable
Taguer le commit de la première version jouable, la retrouver depuis le tag dans un dossier vierge, et vérifier qu'elle lance bien.

### 4 — Le sous-module qui ne suit pas
Un projet compagnon en sous-module a avancé, mais le parent pointe encore l'ancien commit. Diagnostiquer, mettre à jour, et expliquer ce que le parent enregistre exactement.

## Complet — reprendre toute la séance

### 5 — Préparer le dépôt du projet
Sur le dépôt fourni : écrire le `.gitignore` qui exclut ce qui se régénère, le `.gitattributes` qui déclare les binaires et protège les scènes, activer LFS sur les textures et les sons, taguer la version de départ, et documenter le tout dans un `CONTRIBUTING.md` d'une page. Le rendu compare la taille du clone avant et après.

## Difficile — se projeter

### 6 — Le build de 500 Mo dans l'historique
Un équipier a commité un build complet il y a vingt commits, puis l'a supprimé : le dépôt pèse toujours 500 Mo et le clone en salle prend un quart d'heure. Diagnostiquer avec les outils de comptage, réécrire l'historique pour l'en sortir, mesurer le gain — et écrire la procédure que toute l'équipe devra suivre après la réécriture, puisque tous les clones existants deviennent incompatibles. L'exercice est aussi un exercice de communication.
