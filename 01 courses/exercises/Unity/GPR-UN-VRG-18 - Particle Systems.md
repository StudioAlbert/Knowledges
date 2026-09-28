# Exercices — GPR-UN-VRG-18 — Particle Systems

> Cours associé : [[01 courses/slides/Unity/GPR-UN-VRG-18 - Particle Systems|GPR-UN-VRG-18 - Particle Systems]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les assets et les
> corrigés viendront après validation de ces pistes.

Projet URP fourni avec une scène de tir, un ennemi, et des textures de particules.

## Courts — valider la compréhension

### 1 — Débit ou rafale
Produire une fumée continue puis une gerbe d'étincelles instantanée, en ne changeant que le module d'émission. Deux captures animées.

### 2 — La forme compte
Le même effet émis depuis un point, un cône et le bord d'un maillage. Dire lequel convient à un impact, à un feu de camp et à une aura.

### 3 — Les courbes de vie
Régler taille, couleur et vitesse sur la durée de vie d'une étincelle pour qu'elle paraisse retomber et s'éteindre, sans toucher à la physique.

### 4 — Le tri visible
Créer deux nuages transparents qui se croisent, montrer l'artefact de tri, puis le corriger et dire ce que la correction coûte.

## Complet — reprendre toute la séance

### 5 — L'impact complet
L'effet d'un coup qui porte : rafale d'étincelles, nuage de poussière au sol, traînée de l'arme, et petit éclat lumineux. Tout est déclenché par le code au bon moment, coordonné avec le retour visuel de `GPR-UN-VRG-08`, et se termine proprement sans laisser de particules orphelines. Le rendu est une vidéo au ralenti et le tableau des réglages.

## Difficile — se projeter

### 6 — Cinquante impacts sous budget
Faire porter cinquante coups simultanés et tenir soixante images par seconde sur une machine modeste. Mesurer la surface d'écran recouverte, réduire le remplissage sans perdre l'effet, remplacer ce qui peut l'être par un shader, réutiliser les systèmes au lieu de les instancier, et documenter le budget final par effet. Conclure sur la règle d'équipe : combien de particules un effet a le droit de coûter, et qui arbitre.
