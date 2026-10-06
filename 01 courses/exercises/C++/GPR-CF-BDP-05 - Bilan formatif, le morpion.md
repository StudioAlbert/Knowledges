---
seances: [GPR-CF-BDP-05]
---
# Exercices — GPR-CF-BDP-05 — Bilan formatif : le morpion

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05 - Énumérations et tableaux]]
> Autres feuilles de la séance : [[01 courses/exercises/C++/GPR-CF-BDP-05 - Énumérations|Énumérations]] · [[01 courses/exercises/C++/GPR-CF-BDP-05 - Tableaux|Tableaux]]

Un seul fichier `main.cpp` par exercice, sortie avec `std::println`. Accolades obligatoires, comme en `GPR-CF-BDP-04`. Pas de `std::vector` : il arrive plus tard.

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
