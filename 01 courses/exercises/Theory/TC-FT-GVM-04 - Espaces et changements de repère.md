# Exercices — TC-FT-GVM-04 — Espaces et changements de repère

> Cours associé : [[01 courses/slides/Theory/TC-FT-GVM-04 - Espaces et changements de repère|TC-FT-GVM-04 - Espaces et changements de repère]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les valeurs
> numériques et les corrigés viendront après validation de ces pistes.

Papier d'abord, puis vérification au clavier, puis comparaison avec les fonctions équivalentes d'Unity.

## Courts — valider la compréhension

### 1 — Le même point, quatre fois
Un point donné en coordonnées d'objet : le suivre jusqu'à l'écran en écrivant ses coordonnées dans les quatre espaces, avec la matrice utilisée à chaque étape.

### 2 — Remonter
À partir d'une position du monde et de la transformation d'un objet, retrouver la position locale correspondante. Traiter le cas d'une rotation pure en utilisant la transposée.

### 3 — La hiérarchie
Un coffre posé sur un radeau qui dérive et tourne : donner la position mondiale du coffre à trois instants, puis l'inverse — où était-il sur le radeau.

### 4 — L'échelle qui déforme
Appliquer une échelle non uniforme au parent d'un enfant tourné à 45 degrés, dessiner le résultat, et expliquer pourquoi l'angle droit de l'enfant a disparu.

## Complet — reprendre toute la séance

### 5 — Le clic dans le monde
Écrire la chaîne complète qui transforme un clic en pixels en une position du monde, puis en position locale d'un objet quelconque, et enfin le test « le clic est-il dans cet objet » fait en espace local. Vérifier sur un objet tourné, un objet à l'échelle, et un objet enfant d'un autre. Le rendu compare les résultats avec ceux des fonctions d'Unity sur la même scène.

## Difficile — se projeter

### 6 — Le viseur sur la tourelle
Sur le char de `TC-FT-GVM-03` : viser un point du monde avec le canon, ce qui demande de transformer la cible dans le repère de la tourelle, d'en tirer l'angle, puis de contraindre la rotation aux limites mécaniques de chaque niveau de la hiérarchie. Traiter le cas du char en pente et celui de la cible derrière. Prolongement : dire ce que les quaternions de la séance MJ apporteraient ici.
