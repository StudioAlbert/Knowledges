# Exercices — GPR-UN-VRG-14 — Shaders, matériaux, textures, UV

> Cours associé : [[01 courses/slides/Unity/GPR-UN-VRG-14 - Shaders, matériaux, textures, UV|GPR-UN-VRG-14 - Shaders, matériaux, textures, UV]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les assets et les
> corrigés viendront après validation de ces pistes.

Projet URP fourni, avec un cube, un quad, un personnage et un jeu de textures dont un atlas.

## Courts — valider la compréhension

### 1 — Un shader, dix matériaux
Créer dix matériaux à partir du même shader standard, tous visiblement différents, sans toucher au shader. Dire ce qui a changé et ce qui n'a pas pu changer.

### 2 — Les quatre canaux
Ouvrir une texture de masque et afficher successivement ses quatre canaux, en disant ce que chacun encode dans le matériau qui l'utilise.

### 3 — Poser l'atlas
Régler répétition et décalage pour n'afficher qu'une tuile de l'atlas sur un quad, puis une autre, sans découper l'image.

### 4 — Hors des bornes
Comparer répétition, bornage et miroir sur la même texture avec des UV allant de zéro à trois, et dire lequel convient à un mur, à une barre de progression et à un ciel.

## Complet — reprendre toute la séance

### 5 — Habiller une pièce
Habiller entièrement une petite pièce avec trois textures seulement : sol, murs, et un atlas pour les détails. Les UV doivent éviter les répétitions visibles et les étirements, les formats de texture sont choisis et justifiés, et le poids total en mémoire est mesuré et annoncé. Rendu : captures, tableau des textures, et le budget mémoire atteint.

## Difficile — se projeter

### 6 — Le budget par pixel
Sur une même scène, produire deux versions du même aspect visuel : l'une avec quatre échantillonnages de texture par pixel, l'autre avec deux, en compensant par les canaux et par le pré-calcul. Mesurer les deux au profileur GPU, vérifier qu'un joueur ne voit pas la différence, et conclure sur ce qui coûte vraiment dans un programme de pixel. C'est la préparation de `GPR-UN-VRG-17`.
