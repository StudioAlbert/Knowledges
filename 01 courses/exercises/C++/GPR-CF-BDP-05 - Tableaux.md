---
seances: [GPR-CF-BDP-05]
---
# Exercices — GPR-CF-BDP-05 — Tableaux

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05 - Énumérations et tableaux]]
> Autres feuilles de la séance : [[01 courses/exercises/C++/GPR-CF-BDP-05 - Énumérations|Énumérations]] · [[01 courses/exercises/C++/GPR-CF-BDP-05 - Bilan formatif, le morpion|Bilan formatif — le morpion]]

Un seul fichier `main.cpp` par exercice, sortie avec `std::println`. Accolades obligatoires, comme en `GPR-CF-BDP-04`. Pas de `std::vector` : il arrive plus tard.

### 4 — Le meilleur score

> [!abstract] Objectifs
> parcours avec index, garder le meilleur au fil de la boucle

```cpp
int scores[]{ 84, 92, 76, 81, 56 };
```

Afficher le meilleur score **et sa position** dans le tableau : `Meilleur score : 92 (joueur 1)`. Le programme doit rester juste si l'on change les valeurs, ou si le meilleur score est le premier.

### 5 — La valeur est-elle là ?

> [!abstract] Objectifs
> remplir un tableau, recherche linéaire, `bool` posé avant la boucle

1. Demander un entier `V` entre 0 et 20 ; refuser une valeur hors de l'intervalle.
2. Remplir un tableau de 10 entiers tirés au hasard entre 0 et 20 (`std::rand() % 21`, après `std::srand(std::time(nullptr))`).
3. Afficher le tableau sur une ligne, puis `V est dans le tableau` ou `V n'est pas dans le tableau`.
4. Bonus : afficher aussi combien de fois `V` apparaît.

### ~~6 — La table de multiplication~~

> [!abstract] ~~Objectifs~~
> ~~tableau à deux dimensions, deux boucles imbriquées, alignement~~

1. ~~Déclarer `int table[10][10]` et le **remplir** avec deux boucles : la case `[i][j]` contient `(i + 1) × (j + 1)`.~~
2. ~~Dans une deuxième passe, l'**afficher** en colonnes alignées : `std::print("{:4}", table[i][j])`.~~
3. ~~Afficher ensuite la seule ligne du 7, en ne lisant que `table`.~~

## Complet — tableaux à deux dimensions

### 7 — La carte du donjon

> [!abstract] Objectifs
> grille 2D d'énumérations, parcours, coordonnées ligne / colonne, tout le vocabulaire de la séance

Une carte de 6 lignes sur 10 colonnes, rangée dans `Tuile carte[6][10]` :

```cpp
enum class Tuile { SOL, MUR, TRESOR, PIEGE };
```

```text
##########
#@..#..$.#
#.#.#.##.#
#.#$..^..#
#$..#...$#
##########
Trésors restants : 4   Vies : 3
z q s d (x pour quitter) :
```

1. Écrire `char symbole(Tuile t)` : `.` sol, `#` mur, `$` trésor, `^` piège. Remplir la carte à la déclaration.
2. Afficher la carte, avec `@` à la position du joueur (deux entiers `ligne`, `colonne`, départ en `[1][1]`).
3. Compter les trésors de la carte, une fois, avant de jouer.
4. Lire `z`, `q`, `s`, `d` et déplacer le joueur d'une case. Un mur bloque ; un trésor est ramassé (la case redevient du sol) ; un piège coûte une vie.
5. La partie s'arrête quand tous les trésors sont ramassés, quand il ne reste plus de vie, ou sur `x`.

> [!tip] Calculer avant de bouger
> Calculer la case visée dans deux variables, la tester, et seulement ensuite déplacer le joueur. La carte est entourée de murs : le joueur ne peut jamais sortir du tableau.
