# Exercices — GPR-CF-BDP-05 — Énumérations et tableaux

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05 - Énumérations et tableaux]]

Un seul fichier `main.cpp` par exercice, sortie avec `std::println`. Accolades obligatoires, comme en `GPR-CF-BDP-04`. Pas de `std::vector` : il arrive plus tard.

## Énumérations

### 1 — Les états du garde

> [!abstract] Objectifs
> `enum class`, `switch` sans `default`, avertissement du compilateur

1. Déclarer une `enum class EtatGarde` à quatre valeurs : `PATROUILLE`, `ALERTE`, `POURSUITE`, `RETOUR`.
2. Écrire `std::string libelle(EtatGarde etat)`, qui renvoie la phrase à afficher pour chaque état, avec un `switch` **sans** `default`.
3. Dans `main`, afficher le libellé des quatre états.
4. Ajouter un cinquième état, `ENDORMI`, recompiler sans toucher au `switch`, et recopier l'avertissement du compilateur. Que dit-il, et pourquoi est-ce utile ?

### 2 — Cris d'animaux

> [!abstract] Objectifs
> `enum class`, fonction qui prend une énumération, conversion d'un choix en énumération

1. Déclarer une `enum class Animal` d'au moins quatre animaux.
2. Écrire `std::string cri(Animal animal)`, qui renvoie le cri de l'animal.
3. Afficher la liste numérotée des animaux, demander un numéro, et afficher le cri correspondant.
4. Refuser un numéro hors de la liste avec un message.

```text
1. Chat  2. Chien  3. Vache  4. Hibou
Votre animal : 3
La vache fait : Meuh !
```

### 3 — Au restaurant

> [!abstract] Objectifs
> l'énumération `Aliment` du cours, `switch`, boucle de menu, `static_cast`

Reprendre l'énumération des slides :

```cpp
enum class Aliment { BURGER, SUSHI, SALADE, PIZZA };
```

1. Écrire `std::string nom(Aliment a)` et `int prix(Aliment a)` : Burger 12, Sushi 18, Salade 9, Pizza 15 CHF.
2. Afficher le menu, lire un numéro, le convertir en `Aliment` avec `static_cast<Aliment>(choix - 1)`.
3. Ajouter le prix du plat à l'addition, et recommencer jusqu'au choix `0`.
4. Refuser un numéro hors du menu, puis afficher le total.

```text
1. Burger  2. Sushi  3. Salade  4. Pizza  0. L'addition
Votre choix : 1
Burger ajouté : 12 CHF
1. Burger  2. Sushi  3. Salade  4. Pizza  0. L'addition
Votre choix : 7
Ce plat n'est pas au menu.
1. Burger  2. Sushi  3. Salade  4. Pizza  0. L'addition
Votre choix : 4
Pizza ajouté : 15 CHF
1. Burger  2. Sushi  3. Salade  4. Pizza  0. L'addition
Votre choix : 0
Total : 27 CHF
```

> [!tip] Pourquoi vérifier avant le `static_cast` ?
> `static_cast<Aliment>(6)` compile, et produit un `Aliment` qui ne correspond à aucun plat : aucun `case` ne le reconnaît.

## Tableaux

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

### 6 — La table de multiplication

> [!abstract] Objectifs
> tableau à deux dimensions, deux boucles imbriquées, alignement

1. Déclarer `int table[10][10]` et le **remplir** avec deux boucles : la case `[i][j]` contient `(i + 1) × (j + 1)`.
2. Dans une deuxième passe, l'**afficher** en colonnes alignées : `std::print("{:4}", table[i][j])`.
3. Afficher ensuite la seule ligne du 7, en ne lisant que `table`.

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

## Bilan formatif — le morpion

### 8 — Morpion

> [!abstract] Objectifs
> tout le contenu de la séance : `enum class`, `switch`, tableau 2D, fonctions qui reçoivent un tableau, boucles imbriquées

Bilan de séance, à terminer à la maison. Deux joueurs humains, `X` puis `O`, sur une grille de 3 × 3.

```cpp
enum class Case { VIDE, X, O };

Case grille[3][3]{};    // {} : toutes les cases à VIDE
```

**Étapes**

1. `char symbole(Case c)` : `.` pour une case vide, `X`, `O`.
2. `void afficher(const Case grille[3][3])` : la grille avec les numéros de lignes et de colonnes.
3. La boucle de jeu : afficher, demander `ligne colonne` au joueur courant, poser son symbole, passer à l'autre joueur.
4. Refuser un coup hors de la grille, ou sur une case déjà prise, **sans** changer de joueur.
5. `bool aGagne(const Case grille[3][3], Case joueur)` : 3 lignes, 3 colonnes, 2 diagonales.
6. Arrêter la partie sur une victoire, ou sur un match nul après 9 coups.

```text
  0 1 2
0 O . .
1 . X .
2 . . .
Joueur X, ligne et colonne : 1 1
Case déjà prise.
  0 1 2
0 O . .
1 . X .
2 . . .
Joueur X, ligne et colonne : 3 0
Hors de la grille.
…
  0 1 2
0 O . X
1 O X .
2 X . .
Victoire de X !
```

**Bonus**

- ranger la grille dans `Case grille[9]` et accéder aux cases par `ligne * 3 + colonne` (slide *Le morpion en une dimension*) ;
- tester la victoire avec des boucles plutôt que huit conditions écrites à la main.

> [!check] Grille d'auto-évaluation
> Cocher ce qui marche avant de rendre — chaque ligne correspond à une notion de la séance.
>
> | Je sais… | Vérification |
> |---|---|
> | déclarer et utiliser une `enum class` | `Case` a trois valeurs, aucun `0` / `1` / `2` dans le code pour désigner une case |
> | aiguiller une énumération avec `switch` | `symbole` traite les trois cas, sans `default`, sans avertissement |
> | déclarer et initialiser un tableau 2D | `grille` est vide au départ, sans boucle d'initialisation |
> | parcourir un tableau 2D | `afficher` utilise deux boucles imbriquées, lignes à l'extérieur |
> | passer un tableau à une fonction | `afficher` et `aGagne` reçoivent la grille en `const` |
> | protéger l'index | un coup en `3 0` ou `-1 2` est refusé, le programme ne lit jamais hors de la grille |
> | arrêter une boucle sur une condition | victoire et match nul arrêtent la partie, et seulement eux |
