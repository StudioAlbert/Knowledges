# Exercices — GPR-UN-APU-05 — ScriptableObjects, architecture data-driven

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|GPR-UN-APU-05 - ScriptableObjects — architecture data-driven]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les scènes de
> départ et les corrigés viendront après validation de ces pistes.

Projet fourni : une scène de jeu et une scène d'interface, chargées ensemble, qui ne peuvent pas se référencer.

## Courts — valider la compréhension

### 1 — La vie en asset
Mettre les points de vie du joueur dans une variable partagée en asset, l'afficher depuis la scène d'interface, et vérifier qu'aucun des deux scripts ne cite l'autre.

### 2 — Le canal d'événement
Créer un canal en asset pour l'événement « ennemi vaincu », l'émettre depuis le gameplay, et y abonner un compteur de score dans l'autre scène.

### 3 — La valeur qui traîne
Terminer une partie, en relancer une, et constater que la variable partagée a gardé l'état précédent. Décider qui la réinitialise et l'implémenter.

### 4 — Couper un abonné
Désactiver le récepteur d'interface pendant le jeu, montrer que le gameplay continue sans erreur, puis le réactiver et vérifier qu'il se resynchronise.

## Complet — reprendre toute la séance

### 5 — Deux scènes vraiment indépendantes
Le jeu complet en deux scènes qui ne se connaissent pas : gameplay et interface communiquent uniquement par des canaux et des variables en assets. Chaque scène doit pouvoir être lancée seule sans erreur, l'interface affichant alors des valeurs par défaut. Le rendu montre les deux scènes séparément, puis ensemble, et la liste des assets de liaison.

## Difficile — se projeter

### 6 — Traçable et réinitialisable
Ajouter à l'architecture un journal qui indique, pour chaque canal, qui a émis et qui a reçu, avec l'horodatage, activable sans recompiler. Ajouter une remise à zéro fiable de tout l'état partagé au démarrage d'une partie. Provoquer ensuite deux pannes typiques — abonné détruit qui écoute encore, valeur écrite par deux sources — et montrer que le journal permet de les trouver en moins d'une minute. Conclure sur la limite : à partir de combien de canaux cette architecture devient-elle plus obscure que le couplage direct ?
