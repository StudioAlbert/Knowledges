# Exercices — TC-FT-GVM-01 — Vecteurs et repères

> Cours associé : [[01 courses/slides/Theory/TC-FT-GVM-01 - Vecteurs et repères|TC-FT-GVM-01 - Vecteurs et repères]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les valeurs
> numériques et les corrigés viendront après validation de ces pistes.

Exercices 1 à 3 sur papier puis vérifiés au clavier ; 4 à 6 en C++, avec une structure `Vector2`.

## Courts — valider la compréhension

### 1 — Du joueur à l'ennemi
Deux positions données : calculer le vecteur qui va de l'une à l'autre, sa norme, et dire lequel des deux sens il faut prendre pour fuir.

### 2 — Viser juste
À partir d'une direction non normalisée, obtenir la direction unitaire, puis la position atteinte après 3 secondes à 4 unités par seconde.

### 3 — Somme de déplacements
Un vaisseau subit sa poussée et un courant. Composer les deux vecteurs, donner la trajectoire résultante, et dire ce qui se passe quand ils s'annulent.

### 4 — Le piège du vecteur nul
Écrire `normalize` et lui passer un vecteur nul. Décrire ce que renvoie la version naïve, puis proposer les deux conventions possibles et choisir.

## Complet — reprendre toute la séance

### 5 — Le radar du vaisseau
Le joueur et douze contacts. Écrire les fonctions qui donnent la distance à chaque contact, trient les contacts par proximité, filtrent ceux à portée de tir, et renvoient la direction unitaire vers le plus proche. Afficher un radar en caractères où chaque contact apparaît à sa place relative.

## Difficile — se projeter

### 6 — Les trois comportements de base
Implémenter `seek`, `flee` et `arrive` : un agent qui se dirige vers une cible, qui la fuit, et qui ralentit à l'approche sans la dépasser. Tout se fait avec les opérations de la séance, plus une vitesse maximale. Comparer les trajectoires obtenues sur un même parcours et expliquer pourquoi `arrive` a besoin d'un rayon de freinage — c'est l'entrée en matière du steering behavior.
