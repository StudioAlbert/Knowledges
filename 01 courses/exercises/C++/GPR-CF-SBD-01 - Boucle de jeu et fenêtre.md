# Exercices — GPR-CF-SBD-01 — Boucle de jeu et fenêtre

> Cours associé : [[01 courses/slides/C++/GPR-CF-SBD-01 - Boucle de jeu et fenêtre|GPR-CF-SBD-01 - Boucle de jeu et fenêtre]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le projet CMake
> de départ et les corrigés viendront après validation de ces pistes.

Un projet CMake avec SFML est fourni ; chaque exercice part du précédent.

## Courts — valider la compréhension

### 1 — La fenêtre qui ne se ferme pas
Ouvrir une fenêtre sans traiter les événements, constater qu'elle ne répond plus, puis ajouter la boucle d'événements. Expliquer en une phrase qui ferme la fenêtre.

### 2 — Effacer, dessiner, afficher
Faire varier la couleur de fond avec le temps, puis retirer volontairement l'effacement et décrire ce qu'on voit à l'écran.

### 3 — Le carré qui va trop vite
Déplacer un carré au clavier en ajoutant une valeur par image, puis mesurer sa vitesse à 30 et à 144 images par seconde. Corriger en passant par le temps écoulé et vérifier que les deux vitesses se rejoignent.

### 4 — Plafonner
Limiter le framerate, puis se synchroniser à l'écran. Afficher le framerate réel dans le titre de la fenêtre et comparer les deux réglages.

## Complet — reprendre toute la séance

### 5 — Le squelette de jeu
Un programme avec trois états — menu, jeu, pause — une boucle unique et propre, le temps écoulé calculé une seule fois par image, les entrées traitées au même endroit, et un carré pilotable qui ne bouge que dans l'état jeu. Le rendu inclut un schéma d'une demi-page de la boucle et des transitions d'état.

## Difficile — se projeter

### 6 — Le pas fixe
Séparer la mise à jour du rendu : la simulation avance par pas fixes de 16 millisecondes quelle que soit la machine, le rendu tourne aussi vite qu'il peut, et la position affichée est interpolée entre deux pas. Faire la démonstration sur une machine bridée à 20 images par seconde, puis expliquer le problème que cela résout pour la physique de `GPR-CF-SBD-04`.
