# Exercices — TC-FT-GVM-02 — Produits scalaire et vectoriel

> Cours associé : [[01 courses/slides/Theory/TC-FT-GVM-02 - Produits scalaire et vectoriel|TC-FT-GVM-02 - Produits scalaire et vectoriel]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les valeurs
> numériques et les corrigés viendront après validation de ces pistes.

Papier puis clavier, avec la structure `Vector2` de la séance précédente.

## Courts — valider la compréhension

### 1 — Devant ou derrière
Le garde regarde dans une direction donnée, le joueur est quelque part. Décider par le seul signe du produit scalaire, sur cinq positions, sans calculer d'angle.

### 2 — Le cône de vision
Un cône de 60 degrés de demi-angle : dire pour chaque cible si elle est dedans, en comparant des cosinus et non des angles. Expliquer pourquoi c'est plus juste et moins cher.

### 3 — Le rebond de la balle
Une balle arrive sur un mur de normale donnée : calculer la direction sortante, vérifier que l'angle d'incidence égale l'angle de réflexion, et traiter le cas de l'arrivée perpendiculaire.

### 4 — À gauche du garde
Par le signe du produit vectoriel en 2D, dire de quel côté de sa ligne de regard se trouve la cible, et en déduire dans quel sens le garde doit tourner.

## Complet — reprendre toute la séance

### 5 — L'arène de billard
Une balle, quatre murs, et des obstacles rectangulaires. Calculer les rebonds successifs sur dix secondes : normale du mur touché, réflexion, projection pour savoir de combien la balle a dépassé le mur, et correction de position. Le rendu trace la trajectoire en caractères et affiche le nombre de rebonds.

## Difficile — se projeter

### 6 — La zone de déclenchement
Une zone de trigger convexe définie par ses sommets, dans l'ordre. Écrire le test « le joueur est-il à l'intérieur » par le signe du produit vectoriel sur chaque arête, puis la distance au bord la plus courte par projection, et enfin la normale de sortie pour repousser le joueur. Prolongement : dire ce qui casse si le polygone n'est pas convexe, et ce que font les moteurs à la place.
