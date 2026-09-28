# Exercices — TC-FT-TRG-02 — Cercle trigonométrique et unités

> Cours associé : [[01 courses/slides/Theory/TC-FT-TRG-02 - Cercle trigonométrique et unités|TC-FT-TRG-02 - Cercle trigonométrique et unités]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. La séance étant déjà publiée, cette
> fiche attend dans `_overviews/` et ne partira en ligne qu'une fois les énoncés écrits.
> Le widget `cercle_trigo_widget.html` existe déjà et sert d'appui aux exercices 1 à 3.

Papier d'abord, clavier ensuite. En programmation, les angles sont en radians — toujours.

## Courts — valider la compréhension

### 1 — Le triangle rectangle du niveau
Trois situations de jeu — pente d'un toit, portée d'une échelle, hauteur d'une tour — à résoudre par sinus, cosinus ou tangente, en disant chaque fois lequel et pourquoi.

### 2 — Trois unités pour un angle
Convertir une série d'angles entre degrés, radians et tours, puis dire dans quelle unité travaillent respectivement l'inspecteur d'Unity, la bibliothèque standard, et un artiste.

### 3 — Les valeurs remarquables
Retrouver sans calculatrice les sinus et cosinus des angles remarquables, les placer sur le cercle, et en déduire quatre symétries utiles pour éviter des calculs.

### 4 — Le déphasage
Montrer que le cosinus est un sinus décalé, puis s'en servir pour faire osciller une plateforme et une lumière avec un quart de cycle d'écart.

## Complet — reprendre toute la séance

### 5 — Le mouvement circulaire
Faire tourner un ennemi autour d'un point à vitesse constante : position à chaque image, direction du regard tangente à la trajectoire, et vitesse angulaire réglable. Ajouter une oscillation verticale déphasée, puis vérifier par l'identité pythagoricienne que la distance au centre ne dérive jamais. Le rendu affiche la trajectoire en caractères et le tableau des positions sur un tour.

## Difficile — se projeter

### 6 — La dérive numérique
Faire tourner le même point pendant cent mille images de deux façons : en recalculant sa position depuis l'angle cumulé, et en appliquant une petite rotation à la position précédente. Mesurer la distance au centre dans les deux cas, montrer laquelle dérive, et expliquer pourquoi. Puis corriger par renormalisation et dire ce que cela coûte. C'est le même problème que les moteurs rencontrent sur les quaternions.
