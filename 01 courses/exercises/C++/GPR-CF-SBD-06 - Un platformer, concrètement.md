# Exercices — GPR-CF-SBD-06 — Un platformer, concrètement

> Cours associé : [[01 courses/slides/C++/GPR-CF-SBD-06 - Un platformer, concrètement|GPR-CF-SBD-06 - Un platformer, concrètement]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le niveau de test
> et les corrigés viendront après validation de ces pistes.

Le niveau de test est fourni : sol, trois plateformes, un mur, un trou. On part du personnage de `GPR-CF-SBD-05`.

## Courts — valider la compréhension

### 1 — Le capteur de sol
Ajouter le capteur sous les pieds et afficher son état à l'écran. Montrer qu'il est faux quand le personnage touche un mur par le côté, puis le corriger.

### 2 — Pas de saut en l'air
Interdire le second saut, sauter contre un mur pour tenter de tricher, et prouver par la normale du contact que la triche ne passe plus.

### 3 — L'indulgence
Mesurer combien de sauts sur vingt tentatives partent au bord d'une plateforme, ajouter coyote time et mémoire d'appui, refaire la mesure, et donner les deux valeurs retenues en millisecondes.

### 4 — La plateforme à sens unique
Traverser une plateforme par le bas, se poser dessus par le haut, et décrire la condition exacte qui décide.

## Complet — reprendre toute la séance

### 5 — Le contrôleur complet
Un contrôleur jouable de bout en bout : déplacement précis, saut à hauteur variable selon la durée d'appui, gravité asymétrique montée-descente, coyote time, mémoire d'appui, glissement le long des murs sans accrochage, plateformes à sens unique, animation et sons cohérents. Le rendu inclut un tableau de tous les réglages avec leur valeur et ce qu'elle change pour le joueur.

## Difficile — se projeter

### 6 — Wall jump, dash et tests à l'aveugle
Ajouter le wall jump et un dash avec temps de recharge, puis faire tester le contrôleur par trois personnes qui ne l'ont pas réglé, en notant chaque moment où elles ont échoué sans comprendre pourquoi. Corriger les réglages en conséquence et documenter les décisions. Prolongement : redécouper le contrôleur en machine à états et dire ce que cela facilite pour la suite.
