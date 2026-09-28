# Exercices — GPR-CF-POO-01 — Structures

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-01 - Structures|GPR-CF-POO-01 - Structures]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

Un seul fichier `main.cpp` par exercice, sortie avec `std::println`.

## Courts — valider la compréhension

### 1 — La fiche du monstre
Déclarer une structure `Monstre` (nom, points de vie, dégâts, vitesse), en instancier un gobelin, et afficher sa fiche sur quatre lignes alignées.

### 2 — Deux instances, deux vies
Créer deux monstres depuis la même structure, en blesser un seul, et afficher les deux fiches pour montrer que l'autre n'a pas bougé.

### 3 — Emboîter
Ajouter une structure `Vector2` et l'utiliser deux fois dans un `Transform` (position, échelle), lui-même membre du monstre. Afficher la position en une seule ligne.

### 4 — Copie ou référence
Écrire `soigner(Monstre m)` puis `soigner(Monstre& m)`, appeler les deux, et expliquer en une phrase pourquoi la première ne soigne personne.

## Complet — reprendre toute la séance

### 5 — Le bestiaire
Un tableau de six monstres rempli à la déclaration. Écrire les fonctions qui affichent le bestiaire complet, trouvent le plus dangereux, comptent ceux qui survivraient à un coup de 30 dégâts, et appliquent une vague de dégâts à tous. Chaque fonction prend le tableau par référence quand elle le modifie et par référence constante quand elle le lit seulement.

## Difficile — se projeter

### 6 — L'inventaire du héros
Un `Heros` contient un `Transform`, un tableau de huit emplacements d'`Objet` (nom, type énuméré, quantité, poids) et un poids maximum. Écrire ramasser, jeter, empiler les objets identiques, et calculer la charge — en refusant proprement ce qui dépasse. L'énoncé demandera ensuite d'expliquer quelles fonctions gagneraient à devenir des méthodes de la structure, ce qui ouvre la séance suivante.
