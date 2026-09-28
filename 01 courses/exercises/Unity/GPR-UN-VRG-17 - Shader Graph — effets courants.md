# Exercices — GPR-UN-VRG-17 — Shader Graph, effets courants

> Cours associé : [[01 courses/slides/Unity/GPR-UN-VRG-17 - Shader Graph — effets courants|GPR-UN-VRG-17 - Shader Graph — effets courants]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les assets et les
> corrigés viendront après validation de ces pistes.

Projet URP fourni, avec un ennemi, une vitre, un cours d'eau et une scène de test éclairée.

## Courts — valider la compréhension

### 1 — Le défilement
Faire couler l'eau par défilement d'UV, dans deux directions superposées, avec la vitesse exposée. Montrer le cas où la répétition devient visible et le corriger.

### 2 — La dissolution
Faire disparaître l'ennemi par dissolution avec un bruit, seuil exposé et animé sur une seconde. Ajouter le liseré lumineux sur le front de dissolution.

### 3 — Le bord lumineux
Donner un contour fresnel à un bouclier, régler sa puissance, et dire pourquoi l'effet dépend de la position de la caméra.

### 4 — La distorsion
Déformer ce qui se voit à travers la vitre, régler l'amplitude, et traiter le cas où l'effet devient illisible.

## Complet — reprendre toute la séance

### 5 — La mort de l'ennemi
Un seul matériau pour toute la séquence de mort : flash blanc à l'impact, dissolution progressive avec liseré, contour fresnel qui s'intensifie, et disparition. Tout est piloté par deux propriétés exposées que le code anime. Le rendu est une capture animée et le graphe annoté.

## Difficile — se projeter

### 6 — Le même effet, la moitié du prix
Reprendre le matériau de mort et en produire une version deux fois moins chère par pixel, en remplaçant le bruit procédural par une texture, en fusionnant des échantillonnages et en supprimant une variante. Mesurer les deux versions au profileur GPU sur cinquante ennemis à l'écran, vérifier à l'aveugle que personne ne voit la différence, et conclure sur ce qui, dans un graphe, mérite d'être optimisé et ce qui ne le mérite pas.
