---
title: GPR-CF-BDP-05 - Énumérations et tableaux
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Bases de la Programmation
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: online
---

# Énumérations et tableaux
<!-- .slide: class="title" -->
## GPR-CF-BDP-05

<small>Nommer les cas, ranger les séries</small>

Note:
Deux outils : l'énumération pour nommer un ensemble fini de cas, le tableau pour ranger
une série de valeurs du même type. Source : `01.02 - Programming Basics 2-2`, parties
*Enumerations* et *Arrays*.

---

## Objectifs

- nommer un ensemble fini de cas avec une `enum class`, et l'aiguiller avec un `switch`
- déclarer, remplir et parcourir un tableau
- éviter le dépassement d'index
- ranger une grille en deux dimensions

**Prérequis :** conditions et boucles — [[01 courses/slides/C++/GPR-CF-BDP-04 - Branches et boucles|GPR-CF-BDP-04]].

---

# Énumérations
<!-- .slide: class="title" -->

---

## Le problème : des nombres magiques

Le sens de chaque valeur vit dans un commentaire, et rien n'empêche d'écrire `gameMode = 7`.

```cpp
// 0 pour « solo », 1 pour « deathmatch », 2 pour « capture du drapeau »
int gameMode = 0;

if (gameMode == 0)
{
    std::println("Lancement d'une partie solo.");
}
else if (gameMode == 2)
{
    std::println("Lancement d'une capture du drapeau.");
}
// … et que veut dire gameMode == 7 ?
```

Note:
C'est exactement le trou que l'`enum` vient boucher : le sens passe du commentaire au code,
et le compilateur refuse les valeurs inventées.

---

## Déclarer une énumération

On crée un nouveau type, dont on liste toutes les valeurs possibles.

```cpp
enum class Aliment
{
    BURGER,
    SUSHI,
    SALADE,
    PIZZA
};

Aliment commande = Aliment::SUSHI;   // le nom du type, puis ::, puis la valeur
```

---

## Ce qu'est une énumération

- un groupe de valeurs **entières**, chacune avec un **nom**
- un **type** à part entière : `Aliment` comme `int` ou `bool`
- utile pour décrire un « type de quelque chose » : un type d'aliment, de monstre, d'arme
- par défaut, la première valeur vaut 0, la suivante 1, et ainsi de suite

---

## Un exemple de jeu

Les types de monstres d'un donjon, et une variable qui en retient un.

```cpp
enum class MonsterType
{
    SKELETON,
    ZOMBIE,
    BAT
};

MonsterType monstre = MonsterType::ZOMBIE;
```

---

## `switch` sur une énumération

Un `case` par valeur : le code se lit comme la liste des cas.

```cpp
switch (monstre)
{
    case MonsterType::SKELETON:
        std::println("Des os qui claquent.");
        break;
    case MonsterType::ZOMBIE:
        std::println("Un grognement sourd.");
        break;
    case MonsterType::BAT:
        std::println("Un battement d'ailes.");
        break;
}
```

Note:
Sans `default`, GCC et Clang avertissent (`-Wswitch`, activé par `-Wall`) si une valeur de
l'énumération n'a pas son `case` : ajouter `DRAGON` à l'enum signale tous les `switch` à
compléter. C'est l'exercice 1.

---

## À quoi ça sert

- états, animations, types d'objets, couleurs : un ensemble **fini** de cas
- plus lisible : `MonsterType::ZOMBIE` plutôt que `1`
- le compilateur **refuse** les valeurs inventées
- plus riche qu'un `int`, plus simple qu'une classe

---

## `enum` simple : ce qui se passe mal

```cpp
enum Couleur { ROUGE, VERT };
enum Feu     { ROUGE, ORANGE, VERT };  // erreur : ROUGE redéfini

enum Arme { EPEE, ARC };
enum Etat { MORT, VIVANT };

int degats = EPEE;           // compile sans rien dire : EPEE vaut 0
bool trop  = (EPEE < 10);    // compile aussi, et ne veut rien dire
bool bug   = (EPEE == MORT); // compile : les deux valent 0
```

Les valeurs sortent dans le code autour, et se comparent entre n'importe quoi.

Note:
Vérifié au compilateur. La collision est une vraie erreur (MSVC C2365,
« redéfinition ; la précédente définition était énumérateur »). Les trois lignes
suivantes, elles, **compilent** : seule la dernière déclenche un avertissement
(C5054, « opérateur == déconseillé entre les énumérations de types différents »).
Les deux premières passent en silence — c'est ça, le vrai danger.

---

## `enum class` : le compilateur reprend la main

```cpp
enum class Couleur { ROUGE, VERT };
enum class Feu     { ROUGE, ORANGE, VERT };  // aucune collision

Couleur c = Couleur::ROUGE;

// int degats = c;          // refusé : pas de conversion implicite
// if (c == Feu::ROUGE) {}  // refusé : types différents

const int index = static_cast<int>(c);  // explicite, et voulu
```

- chaque valeur reste **dans** son type : `Couleur::ROUGE`
- pas de conversion automatique vers `int`
- le passage en nombre existe, mais il se **demande**

Note:
Le revers : indexer un tableau par une énumération demande un `static_cast<int>`,
toujours. C'est le prix de la sûreté, et c'est pour ça qu'on l'utilise
systématiquement dans ce cours.

---

# Tableaux
<!-- .slide: class="title" -->

---

## Un tableau, cent ennemis

Un tableau range des valeurs du même type, côte à côte en mémoire, atteintes par leur index.

```cpp
int x[6] = { 19, 10, 8, 17, 9, 15 };

int premier = x[0];   // 19 : l'index commence à 0
x[5] = 42;            // [] lit et écrit
```

---

## L'index commence à zéro
<!-- .slide: class="schema" -->

Le dernier élément est à l'index `taille − 1` ; un index de trop ne provoque aucune erreur.

![[bdp05_index.svg]]

---

## Plusieurs façons de déclarer

La taille est donnée, ou déduite des valeurs ; les cases sans valeur valent zéro, sauf sans accolades.

```cpp
const int TAILLE = 5;

int a[TAILLE];                          // 5 cases, valeurs indéterminées
int b[TAILLE] = { 4, 8, 15, 16, 23 };   // taille et valeurs
int c[]{ 4, 8, 15, 16, 23 };            // taille déduite : 5
int d[TAILLE]{};                        // 0 0 0 0 0
int e[TAILLE]{ 4, 8 };                  // 4 8 0 0 0
```

Note:
`a` est le piège : ses cases contiennent ce qui traînait en mémoire. Écrire `{}` dès qu'on
ne remplit pas tout de suite. La taille d'un tableau C doit être connue à la compilation :
un littéral ou une constante, pas une variable lue au clavier.

---

## Plusieurs façons de parcourir

Avec un index quand on en a besoin, sans index quand on lit seulement.

```cpp
const int TAILLE = 5;
int scores[TAILLE]{ 84, 92, 76, 81, 56 };

for (int i = 0; i < TAILLE; ++i)        // avec l'index
{
    std::println("score {} : {}", i, scores[i]);
}

for (int score : scores)                // chaque valeur, sans index
{
    std::println("{}", score);
}
```

Note:
À l'envers : `for (int i = TAILLE - 1; i >= 0; --i)` — l'index part de la dernière case,
`TAILLE - 1`, et descend jusqu'à 0 compris.
La boucle « for each » (`for (int score : scores)`) ne marche que là où le tableau est
déclaré : passé à une fonction, il perd sa taille (slide « Passer un tableau à une
fonction »).

---

## Attention au dépassement

Un `<=` à la place de `<`, et la boucle lit une case qui n'existe pas — sans aucune erreur.

```cpp
int vies[3]{ 3, 3, 3 };

for (int i = 0; i <= 3; ++i)            // <= : une case de trop
{
    std::println("vies[{}] = {}", i, vies[i]);
}

// vies[0] = 3
// vies[1] = 3
// vies[2] = 3
// vies[3] = 344280576                  ← la mémoire voisine
```

Note:
Sortie réelle (GCC 14, sans optimisation) ; la dernière valeur change d'une exécution à
l'autre. En écriture, c'est pire : on écrase la variable voisine. Le compilateur ne dit
rien ; `-fsanitize=address` le détecte à l'exécution (« stack-buffer-overflow »). Parades :
`<` et une constante pour la taille, ou `std::array` et `at()` (fin de séance).

---

## Taille fixe : pas d'ajout, pas de suppression

- la taille d'un tableau est fixée **à la déclaration**, pour toujours
- pas d'« ajouter à la fin », pas de « retirer une case »
- « supprimer », c'est décaler les suivants ou marquer la case vide (une valeur spéciale)
- besoin d'une taille qui change : `std::vector`, en SDS-01

Note:
Conséquence en jeu : on dimensionne pour le pire cas (`MAX_ENNEMIS = 50`) et on garde à
côté un compteur des cases réellement utilisées.

---

## Indexer par une énumération

Une valeur `COUNT` en fin d'énumération donne la taille du tableau, et suit les ajouts.

```cpp
enum class Arme { EPEE, ARC, HACHE, COUNT };

int degats[static_cast<int>(Arme::COUNT)]{ 12, 8, 15 };

int coup = degats[static_cast<int>(Arme::EPEE)];   // 12
```

Note:
Ajouter `LANCE` avant `COUNT` agrandit le tableau automatiquement. Avec une `enum class`,
le `static_cast<int>` est obligatoire : c'est le prix de la sécurité de type.

---

## Passer un tableau à une fonction

Un tableau C n'est pas copié : la fonction reçoit l'original, et doit recevoir sa taille à côté.

```cpp
void doubler(int scores[], int taille)    // pas de copie : on modifie l'original
{
    for (int i = 0; i < taille; ++i)
    {
        scores[i] *= 2;
    }
}

int scores[]{ 84, 92, 76, 81, 56 };
doubler(scores, 5);                       // la taille voyage à côté
// scores vaut maintenant 168 184 152 162 112
```

Note:
Une fonction qui lit seulement prend le tableau en `const` :
`void afficher(const int scores[], int taille)`.
La fonction reçoit en réalité l'adresse de la première case : elle ne sait plus combien il
y en a. D'où le deuxième paramètre, et l'intérêt de `std::array`.

---

## `std::array`, celui qui se souvient

Il connaît sa taille, se copie comme une valeur, et son `at()` vérifie l'index.

```cpp
#include <array>

std::array<int, 5> scores{ 84, 92, 76, 81, 56 };

scores.size();     // 5
scores[1];         // 92, sans vérification
scores.at(1);      // 92
scores.at(5);      // erreur à l'exécution : std::out_of_range
```

Note:
`at()` et `[]` lisent la même case ; seul `at()` vérifie l'index et arrête le programme
au lieu de lire la mémoire voisine. `std::array` se passe à une fonction avec sa taille :
`void afficher(const std::array<int, 5>& scores)`.

---

# Plusieurs dimensions
<!-- .slide: class="title" -->

---

## Deux dimensions : déclarer

Une grille est un tableau de lignes : on donne le nombre de lignes, puis de colonnes.

```cpp
const int LIGNES   = 3;
const int COLONNES = 5;

char niveau[LIGNES][COLONNES]{
    { '#', '#', '#', '#', '#' },
    { '#', '.', '$', '.', '#' },
    { '#', '#', '#', '#', '#' },
};

niveau[1][2] = '.';     // ligne 1, colonne 2 : le trésor est ramassé
```

---

## Deux dimensions : parcourir

Une boucle par dimension : les lignes à l'extérieur, les colonnes à l'intérieur.

```cpp
for (int ligne = 0; ligne < LIGNES; ++ligne)
{
    for (int colonne = 0; colonne < COLONNES; ++colonne)
    {
        std::print("{}", niveau[ligne][colonne]);
    }
    std::println("");                   // fin de ligne
}

// #####
// #.$.#
// #####
```

Note:
Inverser les deux boucles affiche la grille couchée. Lire `niveau[ligne][colonne]` à voix
haute : ligne d'abord, colonne ensuite — comme `y` puis `x`.

---

## Anecdote : une grille dans une seule ligne
<!-- .slide: class="schema" -->

En mémoire, la grille est déjà une ligne : un calcul d'index suffit pour la ranger en 1D.

![[bdp05_grille_1d.svg]]

Note:
Les lignes d'une grille sont rangées les unes après les autres en mémoire : `grille[3][3]`
et `grille[9]` occupent la même place. Beaucoup de moteurs stockent ainsi leurs cartes de
tuiles, leurs images (pixels) et leurs grilles de pathfinding : un seul bloc, plus simple à
allouer et à parcourir. Le calcul inverse : `ligne = index / 3`, `colonne = index % 3`.

---

## Le morpion en une dimension

Même grille, un seul index : `ligne × 3 + colonne`.

```cpp
const int COTE = 3;
char morpion[COTE * COTE]{ 'X', 'O', ' ',  ' ', 'X', ' ',  'O', ' ', 'X' };

char c = morpion[2 * COTE + 0];                    // ligne 2, colonne 0 : index 6, 'O'
for (int i = 0; i < COTE * COTE; ++i)              // une seule boucle pour toute la grille
{
    std::print("{}", morpion[i]);
    if (i % COTE == COTE - 1)                      // fin de ligne tous les 3
    {
        std::println("");
    }
}
```

---

## Atelier — 20 min

Énumérations d'abord (le garde, le restaurant), puis tableaux (meilleur score, valeur cherchée) — le morpion en bilan, à finir à la maison.

Note:
Énoncés, en trois feuilles : [[01 courses/exercises/C++/GPR-CF-BDP-05 - Énumérations|Énumérations]] · [[01 courses/exercises/C++/GPR-CF-BDP-05 - Tableaux|Tableaux]] · [[01 courses/exercises/C++/GPR-CF-BDP-05 - Bilan formatif, le morpion|Bilan formatif]]

---

## À retenir

- une `enum class` pour les cas **nommés**, un `switch` pour les aiguiller
- un tableau pour les **séries** : taille fixe, index de 0 à `taille − 1`
- un index de trop ne prévient pas : `<`, une constante, ou `at()`
- une grille 2D est une ligne en mémoire : `ligne × colonnes + colonne`

---

## Questions ?
