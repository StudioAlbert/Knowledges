---
seances:
  - GPR-CF-BDP-04
---

# Exercices — GPR-CF-BDP-04 — Branches et boucles

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-04 - Branches et boucles|GPR-CF-BDP-04 - Branches et boucles]]

Un seul fichier `main.cpp` par exercice. On utilise `std::println` :

```cpp
#include <print>

int main()
{
    int pv = 42;
    std::println("PV : {}", pv);
}
```

Pas de tableaux, pas de `std::vector` : ils arrivent en [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05]]. Les fonctions de [[01 courses/slides/C++/GPR-CF-BDP-03 - Fonctions|GPR-CF-BDP-03]], elles, sont les bienvenues.

**Une règle pour toute la fiche : accolades obligatoires**, même pour une seule instruction.

## Exercice 1 — L'échauffement

Neuf micro-programmes. Chacun tient en une dizaine de lignes et cible **une** structure de contrôle.

### 1.1 — `if`

Déclarer `int pv = 0;`. Afficher `Game over` si les points de vie sont épuisés.

Refaire tourner le programme avec `pv = 42` : il ne doit plus rien afficher.

### 1.2 — `if / else`

Déclarer `int munitions = 7;`. Afficher `Impair` ou `Pair` selon la parité, avec l'opérateur `%`.

```
Impair
```

### 1.3 — `else if`

Afficher l'état d'un personnage selon ses points de vie :

| Points de vie | Affichage   |
| ------------- | ----------- |
| > 75          | `Intact`    |
| 41 … 75       | `Egratigne` |
| 1 … 40        | `Critique`  |
| ≤ 0           | `Mort`      |

Tester les quatre valeurs `90`, `60`, `12`, `0` en modifiant la variable à la main.

> **Piège :** les conditions sont testées **dans l'ordre**. Écrire `if (pv > 0)` en premier rend toutes les autres branches inatteignables.

### 1.4 — `switch`

Déclarer `char touche = 'z';`. Afficher la direction correspondante :

| Touche      | Affichage           |
| ----------- | ------------------- |
| `z`         | `Avancer`           |
| `s`         | `Reculer`           |
| `q`         | `Gauche`            |
| `d`         | `Droite`            |
| autre chose | `Touche inconnue`   |

Puis : supprimer un seul `break` et observer ce qui s'affiche. Le remettre.

### 1.5 — `while`

Compte à rebours de `10` à `0`, un nombre par ligne, suivi de `Decollage`.

```
10
9
…
0
Decollage
```

### 1.6 — `do … while`

Demander à l'utilisateur un nombre entre 1 et 3 avec `std::cin`, et **redemander** tant que la saisie est hors de cet intervalle.

```cpp
#include <iostream>

int choix = 0;
std::cin >> choix;
```

```
Choisissez entre 1 et 3 : 7
Choisissez entre 1 et 3 : 0
Choisissez entre 1 et 3 : 2
Merci
```

> **Question :** pourquoi un `do … while` plutôt qu'un `while` ? Que faudrait-il écrire en plus avec un `while` ?

### 1.7 — `for`

Afficher la table de multiplication de 7, de 1 à 10, puis la même à l'envers.

```
7 x 1 = 7
7 x 2 = 14
…
7 x 10 = 70
--
7 x 10 = 70
…
7 x 1 = 7
```

### 1.8 — `break` et `continue`

1. Afficher les nombres de 1 à 100, mais **s'arrêter** dès qu'on en trouve un divisible par 17.
2. Afficher les nombres de 1 à 30 en **sautant** les multiples de 3.

### 1.9 — Synthèse

Pour les nombres de 1 à 30 :

- multiple de 3 **et** de 5 → `FizzBuzz`
- multiple de 3 → `Fizz`
- multiple de 5 → `Buzz`
- sinon → le nombre

### Critères de réussite

- chaque programme compile sans warning avec `-Wall` (ou `/W4`)
- toutes les instructions conditionnelles ont leurs accolades
- en 1.3, l'ordre des branches est le bon et aucune n'est morte
- en 1.5 et 1.7, la variable de boucle est déclarée **dans** le `for` quand c'est possible
- aucune boucle ne tourne à l'infini

### Bonus — boucles imbriquées

Afficher un triangle de hauteur 5 avec deux `for` :

```
*
**
***
****
*****
```

`std::print("*");` écrit sans passer à la ligne ; `std::println("");` passe à la ligne.

## Exercice 2 — Le mini-combat

On reprend l'orc et le troll de [[01 courses/exercises/C++/GPR-CF-BDP-03 - Fonctions|GPR-CF-BDP-03]]. Là-bas, les trois tours étaient écrits à la main. Ici, le combat dure **le temps qu'il faut**, et le hasard s'en mêle.

### Boîte à outils — le hasard

```cpp
#include <cstdlib>
#include <ctime>

std::srand(static_cast<unsigned int>(std::time(nullptr)));

int jet = std::rand() % 6 + 1;
```

- `std::srand(...)` s'appelle **une seule fois**, au tout début de `main`
- `std::rand() % 6` donne un nombre de 0 à 5 ; `+ 1` le ramène sur 1 à 6
- `std::rand()` est un mauvais générateur, mais il suffit ici. Le vrai outil, `<random>`, viendra plus tard.

### Étape 1 — Le dé

Écrire `int lancer_de(int faces)`, qui renvoie un entier entre `1` et `faces`.

Vérifier avec un `for` qui affiche dix jets de `lancer_de(6)` : aucune valeur ne doit sortir de l'intervalle, et deux exécutions successives ne doivent pas donner la même suite.

### Étape 2 — Un coup

Écrire `int calculer_degats(int attaque, int defense)` :

- les dégâts valent `attaque + lancer_de(6) - defense`
- ils ne sont **jamais négatifs** : un coup qui ne passe pas l'armure fait `0`

### Étape 3 — La boucle de combat

Deux combattants :

| Personnage | PV | Attaque | Défense |
| ---------- | -- | ------- | ------- |
| Orc        | 60 | 14      | 4       |
| Troll      | 80 | 11      | 6       |

Écrire la boucle principale : **tant que** les deux sont vivants, jouer un tour. Un tour = l'orc frappe, puis le troll frappe. Afficher le numéro du tour, les dégâts et les PV restants.

```
=== Tour 1 ===
L'orc frappe le troll : 11 degats -> Troll : 69 PV
Le troll frappe l'orc : 10 degats -> Orc : 50 PV
```

### Étape 4 — Le type de coup

Avant chaque attaque, lancer un dé à 10 faces et traiter le résultat avec un `switch` :

| Jet      | Effet                                      |
| -------- | ------------------------------------------ |
| `1`      | coup manqué : aucun dégât, on passe au tour suivant |
| `2` … `9`| coup normal                                |
| `10`     | coup critique : dégâts **doublés**         |

Le cas « manqué » est l'occasion d'utiliser `continue`.

### Étape 5 — La fin du combat

Dès qu'un combattant tombe à `0` PV ou moins :

- sortir immédiatement de la boucle avec `break` — le combattant mort ne doit pas riposter
- afficher le vainqueur et le nombre de tours

```
Le troll s'effondre.
L'orc gagne en 7 tours.
```

### Étape 6 — Le garde-fou

Ajouter un compteur de tours. Au-delà de `100` tours, arrêter le combat et afficher `Match nul`.

> **Pourquoi :** si un jour la défense dépasse l'attaque, les dégâts valent toujours `0` et la boucle ne se termine jamais. Une boucle de gameplay a toujours une porte de sortie.

### Critères de réussite

- la formule des dégâts n'apparaît qu'**une seule fois** dans tout le fichier
- la boucle se termine **quelle que soit** la suite de nombres tirée
- le combattant mort ne frappe jamais après sa mort
- les PV affichés ne sont jamais négatifs
- la boucle principale ne dépasse pas deux niveaux d'imbrication : au-delà, extraire une fonction
- accolades partout, y compris pour les `if` d'une seule ligne

### Bonus

- **Rejouer la même partie.** Remplacer `std::srand(std::time(nullptr))` par `std::srand(42)`. Le combat devient identique à chaque exécution — c'est comme ça qu'on débogue un jeu qui utilise du hasard.
- **Le joueur décide.** Au début de chaque tour, demander une action avec `std::cin` et la traiter avec un `switch` : `1` attaquer, `2` boire une potion (`+15` PV, deux fois maximum), `3` fuir (termine le combat). Une saisie invalide redemande, avec un `do … while`.
- **Les statistiques.** Compter les coups critiques, les coups manqués et retenir les dégâts maximum. Les afficher à la fin.
- **La revanche.** Entourer tout le combat d'un `do … while` qui propose de rejouer.
