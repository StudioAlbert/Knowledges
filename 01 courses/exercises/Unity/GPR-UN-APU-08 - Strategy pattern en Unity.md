# Exercices — GPR-UN-APU-08 — Strategy pattern en Unity

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-08 - Strategy pattern en Unity|GPR-UN-APU-08 - Strategy pattern en Unity]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, la scène de
> départ et les corrigés viendront après validation de ces pistes.

Terrain de jeu : le **Dungeon Crawler** du bloc, dont le script de tir contient un `switch` sur trois armes.

## Courts — valider la compréhension

### 1 — Le `switch` à supprimer
Sortir les trois branches du `switch` de tir vers trois classes derrière une même interface. Le script du joueur ne doit plus citer aucun nom d'arme.

### 2 — L'arme en asset
Transformer une stratégie en `ScriptableObject`, régler ses cadence et dégâts dans l'inspecteur, et créer deux variantes du même comportement sans écrire une ligne de code.

### 3 — Échanger à chaud
Ramasser une arme au sol remplace la stratégie courante. Vérifier que rien d'autre ne change dans la scène, et que le joueur tire immédiatement autrement.

### 4 — La même idée pour l'IA
Trois stratégies de décision — agressive, peureuse, soutien — derrière une interface, assignées à trois ennemis identiques. Constater que le prefab est le même pour les trois.

## Complet — reprendre toute la séance

### 5 — L'arsenal
Quatre armes en assets (pistolet, fusil à pompe, laser continu, grenade), une roue de sélection dans l'interface, et un tireur qui ignore tout de ce qu'il tire. Ajouter une cinquième arme en fin d'exercice : la contrainte est de n'ouvrir aucun fichier existant, seulement d'en créer. Le rendu est la scène jouable plus la liste des fichiers touchés.

## Difficile — se projeter

### 6 — Les modificateurs d'arme
On veut pouvoir empiler des effets sur une arme : perforant, explosif, ralentissant, et n'importe quelle combinaison, y compris deux fois le même. Le tireur et les armes existantes ne doivent pas changer. Construire l'empilement, dire quel pattern vient d'apparaître en plus de Strategy, et mesurer ce que coûte une pile de cinq modificateurs sur une cadence de tir élevée.
