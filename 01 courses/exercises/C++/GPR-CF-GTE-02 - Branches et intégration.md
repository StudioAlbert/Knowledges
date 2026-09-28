# Exercices — GPR-CF-GTE-02 — Branches et intégration

> Cours associé : [[01 courses/slides/C++/GPR-CF-GTE-02 - Branches et intégration|GPR-CF-GTE-02 - Branches et intégration]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les dépôts de
> départ et les corrigés viendront après validation de ces pistes.

Terrain de jeu commun à toute la fiche : **Tank vs Towers**, un petit jeu 2D dont le dépôt contient `main.cpp`, `Tank.cpp` et un `GameConfig.h` que tout le monde veut modifier.

## Courts — valider la compréhension

### 1 — La branche du prototype
Le tank doit gagner un tir en cloche, mais la démo de vendredi doit rester jouable. Ouvrir une branche, y faire deux commits, revenir sur `main` et constater que le fichier modifié a disparu du disque.

### 2 — Fast-forward ou vrai merge
Fusionner une branche dont `main` n'a pas bougé, puis une branche dont `main` a bougé. Dire à chaque fois si Git a créé un commit de fusion, et pourquoi.

### 3 — Rebase avant de proposer
Une branche `tourelle-laser` a trois commits, `main` en a reçu deux entre-temps. Rebaser la branche sur `main` et comparer le graphe avant / après avec `git log --graph --oneline`.

### 4 — Le conflit de `GameConfig.h`
Deux branches changent la même ligne : `TANK_SPEED`. Provoquer le conflit, le lire, le résoudre en gardant la valeur de la branche, et expliquer ce que chaque marqueur désignait.

## Complet — reprendre toute la séance

### 5 — Intégrer une fonctionnalité de bout en bout
Sur le dépôt Tank vs Towers : ouvrir `feature/mines`, livrer la fonctionnalité en trois commits nommés, rebaser sur `main`, pousser, ouvrir une pull request, faire relire par le binôme, corriger une remarque, puis fusionner. Le rendu est le graphe final et le fil de la PR.

## Difficile — se projeter

### 6 — Sauver une branche partagée
Un équipier a rebasé puis force-pushé `develop` que trois personnes avaient déjà récupérée : chacun a un historique différent. Diagnostiquer ce qui s'est passé, remettre tout le monde d'accord avec `git reflog` et `git reset`, puis écrire la règle d'équipe qui aurait évité la soirée — et le fichier `CONTRIBUTING.md` qui la porte.
