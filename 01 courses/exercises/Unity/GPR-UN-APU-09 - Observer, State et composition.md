# Exercices — GPR-UN-APU-09 — Observer, State et composition

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-09 - Observer, State et composition|GPR-UN-APU-09 - Observer, State et composition]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, la scène de
> départ et les corrigés viendront après validation de ces pistes.

Terrain de jeu commun : le **Dungeon Crawler** du bloc, déjà utilisé en `GPR-UN-APU-01`.

## Courts — valider la compréhension

### 1 — Le HUD qui n'appelle personne
`PlayerHealth` expose un `event Action<int, int>` et ne connaît plus le HUD. Brancher la barre de vie dessus, vérifier qu'aucun des deux scripts ne cite l'autre, et que retirer le HUD de la scène ne casse rien.

### 2 — L'abonné fantôme
Un script s'abonne dans `OnEnable` mais ne se désabonne jamais. Reproduire l'erreur, lire l'exception au rechargement de scène, puis la corriger. Expliquer en une phrase ce que Unity gardait en mémoire.

### 3 — Deux états valent mieux qu'un `if`
Le garde a un `Update` avec quatre `if` imbriqués. Le découper en `PatrolState` et `ChaseState` sans changer le comportement observable.

### 4 — Une capacité qui s'ajoute
Rendre l'ennemi volant en ajoutant un composant `Hover`, sans créer de classe `FlyingEnemy` ni toucher à `Enemy`.

## Complet — reprendre toute la séance

### 5 — Le garde du donjon
Un garde complet : machine à états à quatre états (patrouille, alerte, poursuite, retour), des capacités en composants (vue, ouïe, sprint), et toutes ses annonces passant par des événements — le HUD, le son et le journal de quête réagissent sans que le garde les connaisse. Le rendu est la scène jouable plus un schéma d'une page de la machine à états.

## Difficile — se projeter

### 6 — Le boss qui change de phase
Un boss à trois phases, chacune étant elle-même une machine à états, avec des transitions déclenchées par des événements du jeu (seuil de PV, minuterie, mort d'un sbire). Contrainte : ajouter une quatrième phase ne doit demander aucune modification des trois autres ni du code qui les pilote, et deux boss différents doivent pouvoir partager des phases.
