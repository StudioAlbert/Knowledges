---
title: Entiers signés et dépassements
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Représentation des Nombres et Logique Binaire
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: true
---

# Entiers signés et dépassements
<!-- .slide: class="title" -->

### Ce qui se passe quand un `int` ne suffit plus

<small>TC-FT-RNLB-02 · Représentation des Nombres et Logique Binaire</small>

Note:
On sait écrire un nombre en binaire. Restent deux questions : comment on
range un nombre négatif, et ce qui arrive quand un résultat ne tient plus
dans les bits disponibles.

---

## Objectifs

À la fin de la séance, vous savez :

- donner la plage d'un type entier à partir de son nombre de bits
- coder et décoder un entier négatif en **complément à deux**
- prévoir le résultat d'un dépassement, signé ou non signé
- choisir un type de taille fixe quand la taille compte

**Prérequis :** lire un nombre binaire — [[01 courses/slides/Theory/TC-FT-RNLB-01 - Bases et changements de base|TC-FT-RNLB-01]].

---

## Pac-Man, niveau 256

- le numéro de niveau tient sur **un octet** : de 0 à 255
- au niveau 256, le calcul du nombre de fruits à afficher **déborde**
- la routine d'affichage écrase la moitié droite du labyrinthe : le niveau ne peut plus être fini

**Un entier a une taille. Quand on la dépasse, le nombre ne grandit pas : il déborde.**

Note:
Le « kill screen » de Pac-Man (1980). On garde l'exemple en tête : à la fin
de la séance, on saura dire exactement ce qui s'est passé dans cet octet.

---

# Entiers non signés
<!-- .slide: class="title" -->

---

## *n* bits, 2ⁿ valeurs

- un entier non signé sur *n* bits va de **0** à **2ⁿ − 1**
- le plus grand, c'est tous les bits à 1 : `1111 1111` = 255 = 2⁸ − 1

| Bits | Nombre de valeurs | Plage non signée |
|:-:|:-:|---|
| 8 | 256 | 0 … 255 |
| 16 | 65 536 | 0 … 65 535 |
| 32 | 4 294 967 296 | 0 … 4 294 967 295 |

---

# Les nombres négatifs
<!-- .slide: class="title" -->

---

## Première idée : un bit de signe

On réserve le bit de gauche au signe :

```
+5 = 0000 0101
-5 = 1000 0101
```

Deux problèmes :

- deux zéros : `0000 0000` et `1000 0000`
- l'addition bit à bit est fausse : `0000 0101 + 1000 0101 = 1000 1010`, soit −10

Note:
Cette représentation, signe et valeur absolue, a existé. Elle survit dans
les flottants : IEEE 754 a un bit de signe, donc un +0 et un −0. On le
verra à la séance suivante.

---

## Le complément à deux

Le bit de poids fort ne pèse plus +2⁷ mais **−2⁷** :

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Poids** | **−128** | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

```
0111 1111 =        64 + 32 + 16 + 8 + 4 + 2 + 1  =  127
1000 0000 = -128                                 = -128
1111 1011 = -128 + 64 + 32 + 16 + 8     + 2 + 1  =   -5
1111 1111 = -128 + 64 + 32 + 16 + 8 + 4 + 2 + 1  =   -1
```

---

## Obtenir −x : inverser, puis ajouter 1

```
  5         = 0000 0101
  inverser  = 1111 1010
  + 1       = 1111 1011   = -5
```

- ça marche dans les deux sens : inverser `1111 1011` puis ajouter 1 redonne `0000 0101`
- l'addition redevient juste : `0000 0101 + 1111 1011 = 1 0000 0000` ; la retenue sort des 8 bits, il reste **0**

Note:
C'est pour ça que tous les processeurs l'utilisent : le même circuit
additionne signés et non signés. Depuis C++20, la norme impose le
complément à deux pour les entiers signés.

---

## Plages représentables

| Type | Minimum | Maximum |
|---|--:|--:|
| `int8_t` | −128 | 127 |
| `uint8_t` | 0 | 255 |
| `int16_t` | −32 768 | 32 767 |
| `uint16_t` | 0 | 65 535 |
| `int32_t` | −2 147 483 648 | 2 147 483 647 |
| `uint32_t` | 0 | 4 294 967 295 |
| `int64_t` | ≈ −9,2 × 10¹⁸ | ≈ 9,2 × 10¹⁸ |
| `uint64_t` | 0 | ≈ 1,8 × 10¹⁹ |

Signé sur *n* bits : de **−2ⁿ⁻¹** à **2ⁿ⁻¹ − 1** — un négatif de plus que de positifs.

<small>`std::numeric_limits<T>::min()` et `max()`, dans `<limits>`</small>

---

## À vous

Sur 8 bits, en complément à deux :

```
 42        = ???? ????
-42        = ???? ????
1001 0110  = ??
1100 1000  = ??
```

Note:
Corrigé : 42 = 0010 1010 ; −42 = 1101 0110 ; 1001 0110 = −106 ;
1100 1000 = −56.

---

# Dépassements
<!-- .slide: class="title" -->

---

## Opérateurs arithmétiques

| Opérateur | Nom | Description | Exemple |
|:-:|---|---|:-:|
| `+` | Addition | additionne deux valeurs | `x + y` |
| `-` | Soustraction | soustrait une valeur d'une autre | `x - y` |
| `*` | Multiplication | multiplie deux valeurs | `x * y` |
| `/` | Division | divise une valeur par une autre | `x / y` |
| `%` | Modulo | reste de la division | `x % y` |

Note:
Chacun peut produire un résultat qui ne tient pas dans le type. `+`, `-`
et `*` évidemment, mais aussi `/` : `INT_MIN / -1` donnerait 2 147 483 648,
qui n'existe pas en `int`.

---

## Dépassement non signé : ça tourne

Un entier non signé calcule **modulo 2ⁿ**. C'est défini par la norme.

```cpp
std::uint8_t vie = 255;
++vie;                   // 0

unsigned int stock = 0;
--stock;                 // 4 294 967 295
```

Comme un compteur kilométrique : après 999 999, on repasse à 000 000.

---

## Le piège classique du non signé

```cpp
std::vector<int> scores;                                 // vide
for (std::size_t i = 0; i < scores.size() - 1; ++i)      // 0 - 1 = 18 446 744 073 709 551 615
{
    std::cout << scores[i];                              // lecture hors du tableau
}

for (unsigned int i = 10; i >= 0; --i)                   // toujours vrai : boucle infinie
{
}
```

Note:
`size()` renvoie un `std::size_t`, non signé. Sur un vecteur vide,
`size() - 1` ne vaut pas −1 : il fait le tour. Même mécanisme pour la
seconde boucle : après 0, `i` passe à 4 294 967 295.

---

## Dépassement signé : comportement indéfini

```cpp
int score = 2'147'483'647;   // INT_MAX
score = score + 1;           // comportement indéfini (UB)
```

- sur la plupart des machines, on obtient −2 147 483 648… **mais rien ne le garantit**
- le compilateur a le droit de supposer que ça **n'arrive jamais**, et d'optimiser en conséquence
- c'est un bug : on l'évite, on ne s'en sert pas

Note:
Différence essentielle avec le non signé. Exemple d'optimisation :
`x + 1 > x` peut être remplacé par `true` pour un `int`, puisque le
débordement « n'existe pas ». Avec GCC ou Clang, `-fsanitize=undefined` le
détecte à l'exécution.

---

## Mélanger signé et non signé

```cpp
int a = -1;
unsigned int b = 1;
if (a < b) { /* jamais exécuté */ }   // -1 est converti en 4 294 967 295
```

- dans une opération mixte, le signé est **converti** en non signé
- le compilateur prévient : `signed/unsigned mismatch` sous MSVC, `-Wsign-compare` sous GCC et Clang
- lisez les avertissements

---

## Les petits types grandissent

```cpp
std::uint8_t a = 200, b = 100;
auto c = a + b;           // int, vaut 300
std::uint8_t d = a + b;   // vaut 44, soit 300 - 256
```

Avant un calcul, tout type plus petit qu'`int` est **promu** en `int`. Le dépassement arrive au moment où l'on range le résultat.

---

## Détecter avant de déborder

```cpp
#include <limits>

bool addition_sure(int a, int b)
{
    if (b > 0 && a > std::numeric_limits<int>::max() - b) return false;
    if (b < 0 && a < std::numeric_limits<int>::min() - b) return false;
    return true;
}
```

- on teste **avant** l'opération : après, il est trop tard
- ou on calcule dans un type plus large, par exemple `std::int64_t`

---

# Taille des types
<!-- .slide: class="title" -->

---

## Taille en mémoire ⚠ sous Windows ⚠

| Type | Octets | Plage | Équivalent |
|---|:-:|---|---|
| `int` | 4 (?) | −2³¹ … 2³¹−1 | `long` |
| `unsigned int` | 4 (?) | 0 … 2³²−1 | `unsigned long` |
| `char` | 1 | −128 … 127 | `int8_t` |
| `short` | 2 | −2¹⁵ … 2¹⁵−1 | `int16_t`, `wchar_t` |
| `long` | 4 | −2³¹ … 2³¹−1 | `int32_t` |
| `long long` | 8 | −2⁶³ … 2⁶³−1 | `int64_t` |

<small>[en.cppreference.com/w/cpp/language/types](https://en.cppreference.com/w/cpp/language/types)</small>

Note:
Les « (?) » ne sont pas une coquille : la norme ne fixe pas ces tailles,
elle fixe des minimums. Les valeurs du tableau sont celles de Windows.
D'où l'existence des types `intNN_t`, qui, eux, sont garantis.

---

## Selon la plateforme

| Type | Windows 64 bits | Linux et macOS 64 bits | Minimum de la norme |
|---|:-:|:-:|:-:|
| `short` | 2 | 2 | 16 bits |
| `int` | 4 | 4 | 16 bits |
| `long` | **4** | **8** | 32 bits |
| `long long` | 8 | 8 | 64 bits |
| pointeur | 8 | 8 | — |
| `wchar_t` | **2** | **4** | — |

Tailles en octets, données par `sizeof`. Le même code n'a pas les mêmes plages d'une machine à l'autre.

Note:
Windows suit le modèle LLP64, Linux et macOS le modèle LP64. Le `char`
lui-même est signé ou non selon la plateforme : signé sur x86, non signé
sur ARM Linux et Android. D'où `int8_t` et `uint8_t` quand on veut un
octet.

---

## Les types de taille fixe

`#include <cstdint>`

| Signés | Non signés | Taille |
|---|---|:-:|
| `std::int8_t` | `std::uint8_t` | 1 octet |
| `std::int16_t` | `std::uint16_t` | 2 octets |
| `std::int32_t` | `std::uint32_t` | 4 octets |
| `std::int64_t` | `std::uint64_t` | 8 octets |

- dès que la taille compte : fichiers, réseau, couleurs, sauvegardes
- `std::size_t` : le type non signé des tailles et des indices (`sizeof`, `.size()`)
- vérifier une hypothèse à la compilation : `static_assert(sizeof(int) == 4);`

Note:
Piège d'affichage : `std::int8_t` est un `signed char`, et `std::cout`
l'affiche comme un caractère. Écrire `+x` ou `static_cast<int>(x)` pour
voir le nombre.

---

# Clôture
<!-- .slide: class="title" -->

---

## Dans la vraie vie

- **Pac-Man** (1980) : niveau 256, un compteur sur 8 bits
- **YouTube** (2014) : les vues de *Gangnam Style* approchent 2 147 483 647, le compteur passe en 64 bits
- **Boeing 787** (2015) : un compteur interne déborde après 248 jours sans redémarrage et coupe les générateurs ; consigne : redémarrer régulièrement

Note:
Pour le 787, l'explication généralement retenue est un compteur en
centièmes de seconde sur un entier signé de 32 bits : 2³¹ centièmes font
un peu plus de 248 jours.

---

## À retenir

- *n* bits : 2ⁿ valeurs ; en signé, de −2ⁿ⁻¹ à 2ⁿ⁻¹ − 1
- complément à deux : le bit de poids fort pèse −2ⁿ⁻¹ ; pour obtenir −x, inverser puis ajouter 1
- non signé qui déborde : **modulo 2ⁿ**, défini ; signé qui déborde : **comportement indéfini**
- `long` et `wchar_t` changent de taille selon la plateforme ; `<cstdint>` quand la taille compte

---

## Exercices

- coder et décoder en complément à deux
- prévoir des dépassements, trouver un bug de boucle
- additionner sans déborder

Énoncés : [[01 courses/exercises/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements]]

---

## Pour aller plus loin

- Séance suivante : [[01 courses/slides/Theory/TC-FT-RNLB-03 - Flottants IEEE 754|TC-FT-RNLB-03 - Flottants IEEE 754]]
- [Complément à deux — Wikipédia](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)
- [Fixed width integer types — cppreference](https://en.cppreference.com/w/cpp/types/integer)
- [Arithmetic operators — cppreference](https://en.cppreference.com/w/cpp/language/operator_arithmetic) : section *Overflows*
