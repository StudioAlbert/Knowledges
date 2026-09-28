# Exercices — TC-FT-GVM-05 — Interpolation et courbes

> Cours associé : [[01 courses/slides/Theory/TC-FT-GVM-05 - Interpolation et courbes|TC-FT-GVM-05 - Interpolation et courbes]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les valeurs
> numériques et les corrigés viendront après validation de ces pistes.

Les exercices simulent le temps par pas fixes de 16 millisecondes et affichent l'évolution en caractères.

## Courts — valider la compréhension

### 1 — La barre de vie qui descend
Faire passer la barre de 100 à 35 en 0,4 seconde par interpolation linéaire, en affichant une ligne par image.

### 2 — Le paramètre qui déborde
Laisser le temps dépasser la durée et observer la valeur obtenue. Ajouter la borne, puis dire ce que produirait un paramètre négatif.

### 3 — Le piège de l'angle
Interpoler d'un cap de 350 degrés vers 10 degrés : montrer le tour complet parcouru par la version naïve, puis corriger en passant par le plus court chemin.

### 4 — Tourner un sprite
Faire tourner quatre points d'un carré autour de son centre, de 30 degrés, et vérifier que les longueurs des côtés n'ont pas changé.

## Complet — reprendre toute la séance

### 5 — L'ouverture du coffre
Une séquence complète : le couvercle pivote en smoother step, la lueur monte puis redescend en smooth arch, le butin sort avec un smooth stop, et le panneau de récompense arrive en dernier. Chaque animation a son délai, sa durée et sa courbe ; le programme affiche une frise texte du déroulé pour vérifier l'enchaînement.

## Difficile — se projeter

### 6 — Un petit moteur de tween
Écrire de quoi déclarer une animation — valeur de départ, d'arrivée, durée, courbe — puis les enchaîner, les jouer en aller-retour, les répéter, et savoir laquelle est terminée. Les courbes sont interchangeables sans toucher au moteur. Prolongement : dire ce qu'il faudrait ajouter pour animer une position, une couleur et un angle avec le même code, ce qui pose la question de la généricité.
