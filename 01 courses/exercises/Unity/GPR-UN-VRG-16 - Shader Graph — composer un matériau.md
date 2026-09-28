# Exercices — GPR-UN-VRG-16 — Shader Graph, composer un matériau

> Cours associé : [[01 courses/slides/Unity/GPR-UN-VRG-16 - Shader Graph — composer un matériau|GPR-UN-VRG-16 - Shader Graph — composer un matériau]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les assets et les
> corrigés viendront après validation de ces pistes.

Projet URP fourni, avec une scène de test et un jeu de textures.

## Courts — valider la compréhension

### 1 — Le premier graphe
Une texture multipliée par une teinte, branchée sur la pile de sortie, appliquée à un cube. Deux captures : le graphe et le résultat.

### 2 — Deux propriétés exposées
Exposer la teinte et l'intensité, créer trois matériaux à partir du même shader, et montrer qu'aucune modification du graphe n'a été nécessaire.

### 3 — Mélanger deux textures
Faire passer un mur de la pierre sèche à la pierre mouillée par un curseur exposé, puis par une texture de masque.

### 4 — Lire l'aperçu
Un graphe fourni qui ne rend rien de correct. Le diagnostiquer uniquement en lisant les aperçus de chaque nœud, et dire quel nœud mentait.

## Complet — reprendre toute la séance

### 5 — Le matériau de l'eau
Une surface d'eau : deux textures de normales qui défilent à des vitesses opposées, teinte de profondeur, transparence, et bord d'écume près des berges. Tous les réglages utiles sont exposés et nommés pour un designer. Le rendu est une capture animée et la liste des propriétés avec leur plage de valeurs conseillée.

## Difficile — se projeter

### 6 — Un shader, cinq matériaux, un budget
Faire servir le même graphe à cinq matériaux très différents — glace, lave, eau, métal rouillé, cristal — uniquement par les propriétés exposées. Mesurer ensuite le coût par pixel de chacun, compter les échantillonnages de texture et les variantes compilées, puis réduire le coût de moitié sans perdre l'aspect. Conclure sur ce qui, dans le graphe, coûte vraiment — ce que prolonge `GPR-UN-VRG-17`.
