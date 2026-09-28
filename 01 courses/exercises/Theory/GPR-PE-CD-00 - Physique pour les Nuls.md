# Exercices — GPR-PE-CD-00 — Physique pour les Nuls

> Cours associé : [[01 courses/slides/Theory/GPR-PE-CD-00 - Physique pour les Nuls|GPR-PE-CD-00 - Physique pour les Nuls]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les valeurs
> numériques et les corrigés viendront après validation de ces pistes.

Exercices 1 et 2 sur papier, le reste en C++ avec un pas de temps fixe de 16 millisecondes.

## Courts — valider la compréhension

### 1 — Remplir le tableau
Une accélération constante donnée : calculer à la main la vitesse et la position aux six premiers pas, puis comparer avec la formule exacte.

### 2 — Lire trois courbes
Trois graphes de position dans le temps : dire pour chacun ce que valent la vitesse et l'accélération, et à quel mouvement de jeu il correspond.

### 3 — Force et masse
La même impulsion appliquée à une caisse légère et à une caisse lourde : calculer les deux vitesses obtenues, puis vérifier par simulation.

### 4 — Rien ne s'arrête
Simuler un glissement sans frottement, constater que la caisse ne s'arrête jamais, puis ajouter un amortissement et trouver la valeur qui donne un arrêt en une seconde.

## Complet — reprendre toute la séance

### 5 — La balle qui rebondit
Une balle lâchée d'une hauteur donnée : gravité, rebond avec perte d'énergie, amortissement de l'air, et arrêt quand le mouvement devient négligeable. Afficher la hauteur de chaque rebond et le temps total, comparer les trois premiers rebonds à la théorie, et expliquer les écarts.

## Difficile — se projeter

### 6 — Le pas de temps qui mentait
Simuler la même chute avec trois pas de temps, en ajoutant la vitesse avant ou après la position selon deux variantes d'intégration. Comparer les trajectoires obtenues à la solution exacte, montrer laquelle des deux variantes reste stable quand le pas grandit, et conclure sur ce que les moteurs physiques font réellement. C'est la justification du pas fixe de `GPR-CF-SBD-04`.
