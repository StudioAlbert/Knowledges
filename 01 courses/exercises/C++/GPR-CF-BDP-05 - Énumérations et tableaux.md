# Exercices — GPR-CF-BDP-05 — Énumérations et tableaux

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05 - Énumérations et tableaux]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

Un seul fichier par exercice, sortie avec `std::println`. Accolades obligatoires, comme en `GPR-CF-BDP-04`.

## Courts — valider la compréhension

### 1 — Les états du garde
Déclarer les quatre états d'un garde, écrire la fonction qui renvoie le libellé à afficher, et la faire tourner sur les quatre cas avec un `switch` sans `default`. Ajouter un cinquième état et constater l'avertissement du compilateur.

### 2 — Le tableau des scores
Dix scores : afficher le meilleur, la moyenne, puis la liste triée à la main par échanges successifs. Aucun index écrit en dur à part 0.

### 3 — Dégâts par type d'arme
Un tableau indexé par une énumération d'armes donne les dégâts de base. Écrire la fonction qui calcule les dégâts d'une attaque en croisant l'arme et un multiplicateur de critique.

### 4 — Hors des bornes
Lire volontairement l'index 12 d'un tableau de 10, afficher ce qu'on obtient, refaire avec `at()`, et comparer les deux comportements en trois lignes.

## Complet — reprendre toute la séance

### 5 — La vague d'ennemis
Douze ennemis dans un `std::array`, chacun avec son type énuméré et ses points de vie. Écrire : afficher la vague, appliquer une attaque de zone qui ne touche qu'un type, compter les survivants, et faire avancer chacun selon une vitesse lue dans un tableau indexé par le type. Le programme tourne cinq tours et affiche l'état après chacun.

## Difficile — se projeter

### 6 — La carte de tuiles
Une grille 2D de tuiles énumérées, chargée depuis un tableau de chaînes et affichée en caractères. Écrire : compter les tuiles de chaque type, dire si deux cases sont voisines, lister les voisins franchissables d'une case, et vérifier qu'une ligne droite entre deux points ne traverse aucun mur. C'est le socle des séances de pathfinding.
