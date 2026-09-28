# Exercices — TC-FT-RDE-03 — Fonctions et repères

> Cours associé : [[01 courses/slides/Theory/TC-FT-RDE-03 - Fonctions et repères|TC-FT-RDE-03 - Fonctions et repères]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les valeurs
> numériques et les corrigés viendront après validation de ces pistes.

Les courbes se tracent d'abord à la main sur papier quadrillé, puis se vérifient au clavier.

## Courts — valider la compréhension

### 1 — Domaine et image
Six fonctions de réglage de jeu : donner pour chacune les entrées permises, les sorties possibles, et le réglage que la courbe rendrait absurde.

### 2 — La sensibilité de la souris
Une fonction affine relie le réglage au déplacement de la visée. Donner sa pente, l'effet d'un cran de réglage, et la valeur du réglage qui double la sensibilité par défaut.

### 3 — La hauteur du saut
Une parabole décrit la hauteur en fonction du temps. Donner le sommet, la durée totale du saut, et l'instant où le joueur repasse sous la plateforme.

### 4 — Borner et prendre l'écart
Écrire les fonctions de bornage et d'écart absolu, puis s'en servir pour qu'une barre de vie affichée ne sorte jamais de l'écran et qu'un recentrage de caméra ignore les micro-déplacements.

## Complet — reprendre toute la séance

### 5 — L'atténuation du fusil à pompe
Une fonction par morceaux : dégâts pleins jusqu'à une distance, décroissance ensuite, plancher au-delà. La tracer, l'implémenter, régler les seuils pour que l'arme soit décisive de près et inutile de loin, et afficher le tableau des dégâts de 0 à 40 mètres par pas de 2.

## Difficile — se projeter

### 6 — La fonction de réglage réutilisable
Écrire de quoi transformer n'importe quelle valeur d'entrée en n'importe quelle sortie utile : normaliser l'entrée depuis son intervalle, appliquer une courbe choisie, remettre à l'échelle de sortie, borner. La faire servir sur trois réglages sans rien changer d'autre que ses paramètres — sensibilité de visée, volume sonore, vitesse d'un ascenseur. Prolongement : expliquer en quoi c'est la composition de fonctions de la séance, et quel lien avec les courbes d'easing de `TC-FT-GVM-05`.
