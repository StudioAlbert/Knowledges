# Exercices — GPR-CF-SBD-05 — Relier physique et graphique

> Cours associé : [[01 courses/slides/C++/GPR-CF-SBD-05 - Relier physique et graphique|GPR-CF-SBD-05 - Relier physique et graphique]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le projet de
> départ et les corrigés viendront après validation de ces pistes.

On reprend la scène physique de `GPR-CF-SBD-04` et on lui donne enfin une image.

## Courts — valider la compréhension

### 1 — Le sprite qui suit
Afficher une caisse dynamique à l'écran en recopiant sa position après chaque pas. Puis déplacer le sprite à la main et décrire ce que la physique en pense.

### 2 — L'angle qui tourne à l'envers
Afficher une caisse qui tourne sans convertir les radians, constater, corriger. Donner la ligne de conversion et l'endroit où elle doit vivre.

### 3 — Trois façons de bouger
Piloter le même personnage par force, par impulsion, puis par vitesse imposée, et tracer sa vitesse. Dire lequel des trois convient à un jeu de plateforme et pourquoi.

### 4 — Le contact détecté
Afficher un message quand le personnage touche une caisse et quand il la quitte, en retrouvant les deux objets de jeu impliqués depuis le contact.

## Complet — reprendre toute la séance

### 5 — Le personnage physique
Un personnage avec corps dynamique, sprite synchronisé, animation liée à sa vitesse réelle, déplacement horizontal par vitesse imposée, saut par impulsion, son au contact du sol, et une caméra qui le suit. Les contacts sont collectés pendant le pas et traités après. Le rendu est le jeu plus le schéma de l'ordre des étapes dans une image.

## Difficile — se projeter

### 6 — Ramasser et détruire sans tout casser
Des pièces à ramasser et des ennemis à supprimer au contact. Implémenter la file d'événements de contact, la suppression différée des corps, et la réutilisation des corps plutôt que leur destruction. Provoquer volontairement le crash de la suppression pendant le pas, l'expliquer, puis montrer que la version différée tient sur mille collectes. Prolongement : dire ce que le pattern d'objets réutilisables apporte ici.
