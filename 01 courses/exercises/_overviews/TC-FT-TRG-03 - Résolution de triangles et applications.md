# Exercices — TC-FT-TRG-03 — Résolution de triangles et applications

> Cours associé : [[01 courses/slides/Theory/TC-FT-TRG-03 - Résolution de triangles et applications|TC-FT-TRG-03 - Résolution de triangles et applications]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les valeurs
> numériques et les corrigés viendront après validation de ces pistes. Le deck, lui, est
> écrit et relu.

Exercices 1 à 4 sur papier, 5 et 6 au clavier. Les angles sont en radians dès qu'on programme.

## Courts — valider la compréhension

### 1 — Le bon outil
Six triangles donnés par leurs mesures connues (CAC, ACA, CCC, CCA…). Pour chacun, dire s'il se résout par la loi des sinus, par la loi des cosinus, ou pas du tout — sans le résoudre.

### 2 — La portée du pont de corde
Un triangle CAC entre deux plateformes : calculer la distance manquante à la loi des cosinus, puis l'angle de visée à la loi des sinus. Vérifier la cohérence des deux résultats.

### 3 — Pourquoi `atan2` et pas `atan`
Quatre directions, une par quadrant. Calculer l'angle avec `atan` puis avec `atan2` et expliquer les deux cas où `atan` se trompe de 180 degrés.

### 4 — L'angle entre deux gardes
Le joueur voit deux gardes ; à partir des deux vecteurs, donner l'angle entre eux par le produit scalaire, puis retrouver le même résultat par `atan2` des deux directions.

## Complet — reprendre toute la séance

### 5 — Le champ de vision du garde
Écrire la fonction qui répond « le joueur est-il vu ? » : direction du regard, demi-angle du cône, portée. Traiter le joueur pile derrière, pile sur le bord du cône, et à la limite de portée. Le rendu est la fonction plus un petit programme qui balaie une grille de positions et dessine le cône en caractères.

## Difficile — se projeter

### 6 — Le tir en cloche
Étant donné une cible, une vitesse initiale et la gravité, calculer les deux angles de tir qui atteignent la cible, choisir le tendu ou le bombé selon un obstacle, et dire à quelle condition aucune solution n'existe. Prolongement : cible mobile, donc résolution à chaque frame avec une prédiction de position.
