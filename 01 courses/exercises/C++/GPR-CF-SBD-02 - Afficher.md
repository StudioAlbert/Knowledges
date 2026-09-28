# Exercices — GPR-CF-SBD-02 — Afficher

> Cours associé : [[01 courses/slides/C++/GPR-CF-SBD-02 - Afficher|GPR-CF-SBD-02 - Afficher]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les assets et les
> corrigés viendront après validation de ces pistes.

On repart du squelette de `GPR-CF-SBD-01`. Les images sont fournies.

## Courts — valider la compréhension

### 1 — Le sprite blanc
Charger une texture dans une portée locale, dessiner le sprite dehors, constater le rectangle blanc, puis corriger la durée de vie de la texture et expliquer ce qui s'était passé.

### 2 — L'origine au centre
Faire tourner un sprite autour de son coin, puis autour de son centre. Donner les deux lignes qui changent et l'effet visible.

### 3 — La caméra qui suit
Déplacer la vue pour garder le joueur au centre, puis la brider aux bords du niveau pour ne jamais montrer le vide.

### 4 — Redimensionner proprement
Implémenter les trois politiques de redimensionnement, les commuter avec une touche, et dire laquelle convient à un jeu de plateforme compétitif.

## Complet — reprendre toute la séance

### 5 — Le personnage animé
Un personnage sur une planche de sprites : quatre directions, animation de marche et d'arrêt, cadence réglée en images par seconde et non par image de jeu. Il se déplace dans un niveau plus grand que l'écran, la caméra le suit et reste dans les bornes, la fenêtre se redimensionne sans déformation. Le rendu est le programme plus une capture animée de trois secondes.

## Difficile — se projeter

### 6 — La parallaxe et ce qu'on ne dessine pas
Trois plans d'arrière-fond défilant à des vitesses différentes, et deux mille sprites de décor dont seuls ceux visibles sont dessinés. Mesurer le framerate avec et sans ce tri, afficher le nombre de sprites réellement dessinés, et expliquer pourquoi le test de visibilité coûte moins que le dessin. C'est la première rencontre avec le culling.
