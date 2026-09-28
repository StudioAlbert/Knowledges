# Exercices — GPR-CF-SBD-03 — Son

> Cours associé : [[01 courses/slides/C++/GPR-CF-SBD-03 - Son|GPR-CF-SBD-03 - Son]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les fichiers
> audio et les corrigés viendront après validation de ces pistes.

On repart du personnage animé de `GPR-CF-SBD-02`. Les sons sont fournis, libres de droits.

## Courts — valider la compréhension

### 1 — Le tir silencieux
Jouer un son dont le tampon est déclaré dans une portée locale, constater le silence ou le crash, puis corriger la durée de vie du tampon.

### 2 — La musique qui boucle
Lancer une musique en boucle, la mettre en pause et la reprendre au même endroit, et afficher sa position de lecture à l'écran.

### 3 — Le tir qui ne lasse pas
Jouer le même son de tir vingt fois de suite, puis y ajouter une variation aléatoire de hauteur et de volume. Décrire la différence en une phrase.

### 4 — Trente sons d'un coup
Déclencher trente sons dans la même image, compter ceux réellement audibles, et proposer une règle pour n'en jouer que ce qui est utile.

## Complet — reprendre toute la séance

### 5 — Le paysage sonore du niveau
Un niveau avec musique de fond en boucle, sons de pas synchronisés sur l'animation de marche, saut et atterrissage, ambiance de vent en boucle, et trois réglages de volume indépendants — musique, effets, ambiance — pilotés au clavier. Le rendu est une capture vidéo de trente secondes et un tableau des sons avec leur poids en mémoire.

## Difficile — se projeter

### 6 — Le petit gestionnaire audio
Écrire de quoi demander « joue ce son, dans cette catégorie, à cette position » sans que le code de gameplay connaisse ni les fichiers ni les canaux : réserve de sons réutilisables, catégories avec leur volume, limite du nombre d'instances simultanées d'un même son, et atténuation de la musique quand une voix parle. Mesurer la mémoire audio totale et dire ce qui devrait passer en flux.
