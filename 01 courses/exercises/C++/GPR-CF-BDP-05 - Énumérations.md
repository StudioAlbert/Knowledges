---
seances: [GPR-CF-BDP-05]
---
# Exercices — GPR-CF-BDP-05 — Énumérations

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05 - Énumérations et tableaux]]
> Autres feuilles de la séance : [[01 courses/exercises/C++/GPR-CF-BDP-05 - Tableaux|Tableaux]] · [[01 courses/exercises/C++/GPR-CF-BDP-05 - Bilan formatif, le morpion|Bilan formatif — le morpion]]

Un seul fichier `main.cpp` par exercice, sortie avec `std::println`. Accolades obligatoires, comme en `GPR-CF-BDP-04`. Pas de `std::vector` : il arrive plus tard.

### 1 — Les états du garde

> [!abstract] Objectifs
> `enum class`, `switch` sans `default`, avertissement du compilateur

1. Déclarer une `enum class EtatGarde` à quatre valeurs : `PATROUILLE`, `ALERTE`, `POURSUITE`, `RETOUR`.
2. Écrire `std::string libelle(EtatGarde etat)`, qui renvoie la phrase à afficher pour chaque état, avec un `switch` **sans** `default`.
3. Dans `main`, afficher le libellé des quatre états.
4. Ajouter un cinquième état, `ENDORMI`, recompiler sans toucher au `switch`, et recopier l'avertissement du compilateur. Que dit-il, et pourquoi est-ce utile ?

### 2 — Au restaurant

> [!abstract] Objectifs
> l'énumération `Aliment` du cours, `switch`, boucle de menu, `static_cast`

Reprendre l'énumération des slides :

```cpp
enum class Aliment { BURGER, SUSHI, SALADE, PIZZA };
```

1. Écrire `std::string nom(Aliment a)` et `int prix(Aliment a)` : Burger 12, Sushi 18, Salade 9, Pizza 15 CHF.
2. Afficher le menu, lire un numéro, le convertir en `Aliment` en utilisant `static_cast<Aliment>(choix - 1)` (voir tip ci-dessous)
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

> [!tip] Mais c'est quoi static_cast o_O ?
> 
>```c++
> // C++-Style cast : nouvelle ecriture
> int un_entier = static_cast<int> a_convertir;
> // C-Style cast : ancienne ecriture
> int un_entier = (int)a_convertir;
> // Les 2 ecritures donnent le meme resultat
> ```
> 

> [!tip] Pourquoi vérifier avant le `static_cast` ?
> `static_cast<Aliment>(6)` compile, et produit un `Aliment` qui ne correspond à aucun plat : aucun `case` ne le reconnaît.
