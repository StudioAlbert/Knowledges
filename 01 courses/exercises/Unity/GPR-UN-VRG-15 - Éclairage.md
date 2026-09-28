# Exercices — GPR-UN-VRG-15 — Éclairage

> Cours associé : [[01 courses/slides/Unity/GPR-UN-VRG-15 - Éclairage|GPR-UN-VRG-15 - Éclairage]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, la scène de
> départ et les corrigés viendront après validation de ces pistes.

Scène de départ fournie : une salle de donjon grise, sans aucune lumière, avec un personnage qui la traverse.

## Courts — valider la compréhension

### 1 — Les quatre lumières
Éclairer la même salle avec chacun des quatre types de lumière, une capture par type, et une phrase sur ce que chacun raconte de l'endroit.

### 2 — Cuire la lumière
Marquer le décor comme statique, lancer la cuisson, et comparer trois résolutions de lightmap sur la qualité, le poids sur le disque et le temps de cuisson.

### 3 — L'objet qui bouge
Constater que le personnage reste plat dans une scène entièrement cuite, poser des sondes, et montrer la différence sur une capture avant-après.

### 4 — Compter les lumières
Ajouter des lumières temps réel jusqu'à faire tomber le framerate, relever le nombre atteint, puis montrer que le coût dépend de leur chevauchement et non de leur nombre.

## Complet — reprendre toute la séance

### 5 — L'ambiance de la salle du trésor
Éclairer une salle complète avec une intention : une source principale cuite, deux torches animées en temps réel, des sondes pour les objets mobiles, une sonde de réflexion sur le sol mouillé, et une exposition réglée pour que le coffre soit le point le plus lumineux. Le rendu est une capture, le budget d'éclairage par image, et trois lignes sur l'intention.

## Difficile — se projeter

### 6 — Éclairer sous contrainte
Le même niveau doit tourner à 60 images par seconde sur une machine d'entrée de gamme, avec un budget d'éclairage fixé. Mesurer le coût de chaque décision, arbitrer entre cuit et temps réel, réduire les chevauchements, et documenter les compromis. Conclure sur ce que le choix du pipeline de rendu change à cet arbitrage.
