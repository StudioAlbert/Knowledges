# Exercices — GPR-CF-POO-06 — Héritage et polymorphisme

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme|GPR-CF-POO-06 - Héritage et polymorphisme]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

## Courts — valider la compréhension

### 1 — Le tronc commun
Trois classes d'ennemis recopiées à l'identique sur 80 % de leur code. Extraire une base, ne laisser dans chaque enfant que ce qui lui est propre, et vérifier que le programme se comporte pareil.

### 2 — Avec ou sans `virtual`
Le même appel sur un pointeur de base, une fois sans `virtual`, une fois avec. Donner la sortie des deux versions et expliquer laquelle décide, le type écrit ou le type réel.

### 3 — La collection hétérogène
Un tableau de pointeurs vers la base contenant les trois types d'ennemis, parcouru par une seule boucle qui les fait tous attaquer.

### 4 — Le destructeur oublié
Détruire un enfant par un pointeur de base sans destructeur virtuel, avec des messages dans les destructeurs. Montrer ce qui n'est pas appelé, puis corriger.

## Complet — reprendre toute la séance

### 5 — Le bestiaire polymorphe
Une base abstraite `Ennemi` qui impose `attaquer`, `subirDegats` et `decrire`, et quatre enfants : gobelin, archer, golem, et un boss qui redéfinit tout. Une vague mélangée est stockée dans un seul conteneur, jouée sur cinq tours, et le journal de combat montre que chacun a fait ce qu'il sait faire. Aucun test de type dans la boucle de jeu.

## Difficile — se projeter

### 6 — L'ennemi qui vole et qui tire
On demande un ennemi volant, un tireur, puis un volant qui tire, puis un volant qui tire et se soigne. Construire la hiérarchie par héritage, constater l'explosion combinatoire, puis refaire le même jeu de capacités par composition. Comparer les deux versions sur trois critères — lignes de code, coût d'une nouvelle capacité, lisibilité — et conclure. C'est la démonstration que prolonge `TC-FT-PCL-04`.
