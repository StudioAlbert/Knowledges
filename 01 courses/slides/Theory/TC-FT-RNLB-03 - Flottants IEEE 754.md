---
title: Flottants IEEE 754
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

# Flottants IEEE 754
<!-- .slide: class="title" -->

### Pourquoi `0.1 + 0.2 != 0.3`

<small>TC-FT-RNLB-03 · Représentation des Nombres et Logique Binaire</small>

Note:
On repart de la façon dont un nombre est rangé en mémoire, puis on
applique la notation scientifique au binaire : c'est exactement ce qu'est
un flottant. Précision, epsilon, valeurs spéciales et comparaisons en
découlent.

---

## Objectifs

À la fin de la séance, vous savez :

- décrire les trois champs d'un flottant : **signe, exposant, mantisse**
- lire un `float` donné en hexadécimal
- expliquer pourquoi la plupart des décimaux n'ont pas de valeur exacte
- reconnaître ±0, ±∞ et NaN
- comparer deux flottants **sans** `==`

**Prérequis :** binaire et hexadécimal — [[01 courses/slides/Theory/TC-FT-RNLB-01 - Bases et changements de base|TC-FT-RNLB-01]].

---

# Les nombres en machine
<!-- .slide: class="title" -->

---

## Notations numériques

Le système indo-arabe compte en **base 10** — probablement parce que nous avons 10 doigts.

```
196 = 1*10² + 9*10¹ + 6*10⁰
```

Cependant :

- les Chepang, au Népal, utilisent un système en **base 12** (plus facile à diviser par 2, 3, 4, 6)
- la numération **maya** est en base 20
- les Babyloniens utilisaient une numération en base 60

---

## Un nombre dans l'ordinateur

À cause de l'électronique, les ordinateurs stockent beaucoup de valeurs en 0 et 1.

`196`, en entier 32 bits :

```
Big-Endian    : 00000000 00000000 00000000 11000100
Little-Endian : 11000100 00000000 00000000 00000000
                (probablement votre ordinateur)
```

Note:
Big-endian : l'octet de poids fort est rangé en premier. Little-endian :
l'octet de poids faible d'abord — c'est le cas des processeurs x86 et de
la plupart des ARM. L'ordre des bits dans un octet, lui, ne change pas.

---

## Les nombres de 0 à 15 en binaire

| Déc | Bin | \| \| | Déc | Bin  |
| :-: | :-: | :---: | :-: | :--: |
|  0  |  0  | \| \| |  8  | 1000 |
|  1  |  1  | \| \| |  9  | 1001 |
|  2  | 10  | \| \| | 10  | 1010 |
|  3  | 11  | \| \| | 11  | 1011 |
|  4  | 100 | \| \| | 12  | 1100 |
|  5  | 101 | \| \| | 13  | 1101 |
|  6  | 110 | \| \| | 14  | 1110 |
|  7  | 111 | \| \| | 15  | 1111 |

---

## Hexadécimal

Le binaire est souvent encombrant, donc en informatique on aime bien l'**hexadécimal** :

```
196 = 0xC4 = 12*16¹ + 4*1
```

Le passage de l'hexadécimal au binaire est immédiat :

```
0xC4 :  C = 1100 , 4 = 0100  ->  1100'0100
```

**Un chiffre hexadécimal représente exactement 4 chiffres binaires !**

---

# La virgule flottante
<!-- .slide: class="title" -->

---

## La notation scientifique

```
196      = 1,96 × 10²
0,00042  = 4,2  × 10⁻⁴
```

Trois informations :

- un **signe**
- des chiffres significatifs : la **mantisse**
- une puissance de la base : l'**exposant**

La virgule se déplace — elle « flotte » — et l'exposant dit de combien : d'où **virgule flottante**.

---

## Après la virgule : des poids négatifs
<!-- .slide: class="schema" -->

Même lecture qu'en RNLB-01 : on additionne les poids des bits à 1 — ils continuent simplement après 2⁰.

![[rnlb03_poids_negatifs.svg]]

Note:
Chaque rang vers la droite divise le poids par 2 : 2⁻¹ = ½, 2⁻² = ¼, 2⁻³ = ⅛…
Dans l'autre sens, on retire les poids comme pour les entiers :
6,5 − 4 = 2,5 ; − 2 = 0,5 ; − 0,5 = 0 → bits à 1 sous 4, 2 et 0,5.
Question à la salle : que vaut 0000,1100₂ ? (0,75). Et 0,1 ? On ne tombe
jamais sur 0 en retirant ces poids — c'est la slide « 0,1 n'existe pas
en binaire ».

---

## La même idée en binaire

Avec ces poids, on écrit un nombre à virgule, puis on le normalise comme en décimal.

```
 6,5   = 110,1₂    = 1,101₂  × 2²
12,5   = 1100,1₂   = 1,1001₂ × 2³
 0,75  = 0,11₂     = 1,1₂    × 2⁻¹
```

En binaire, le premier chiffre significatif vaut **toujours 1** : inutile de le stocker.

---

## 0,1 n'existe pas en binaire

```
0,1 = 0,0001 1001 1001 1001 1001 1001 …₂
```

- comme ⅓ = 0,333… en décimal, **0,1 ne tombe jamais juste** en base 2
- la machine garde un nombre fini de bits : elle **arrondit**
- `0.1f` vaut en réalité **0,100000001490116119384765625**

Note:
Tout décimal dont le dénominateur n'est pas une puissance de 2 a une
écriture binaire infinie : 0,1, 0,2, 0,3… Seuls 0,5, 0,25, 0,75, 0,125…
tombent juste.

---

# La norme IEEE 754
<!-- .slide: class="title" -->

---

## Le `float` : 32 bits

| Signe | Exposant | Mantisse |
|:-:|:-:|:-:|
| 1 bit | 8 bits | 23 bits |

```
valeur = (-1)^signe × 1,mantisse₂ × 2^(exposant - 127)
```

- **signe** : 0 pour positif, 1 pour négatif
- **exposant** : stocké avec un **biais** de 127 ; `0111 1111` veut dire 2⁰
- **mantisse** : les bits qui suivent le « 1, » implicite

Note:
Le biais évite de coder un exposant négatif en complément à deux. Les
exposants stockés 0 et 255 sont réservés aux valeurs spéciales : les
exposants réels vont donc de −126 à 127.

---

## Le `double` : 64 bits

| | Signe | Exposant | Mantisse | Biais | Chiffres significatifs |
|---|:-:|:-:|:-:|:-:|:-:|
| `float` | 1 | 8 | 23 | 127 | environ 7 |
| `double` | 1 | 11 | 52 | 1023 | environ 16 |

Même principe, plus de bits partout : plus de précision, et des valeurs bien plus grandes.

---

## Écrire un flottant en C++

| Écriture | Type | Valeur |
|---|---|---|
| `1.5` | `double` | 1,5 |
| `1.5f` | `float` | 1,5 |
| `2.5e3` | `double` | 2 500 |
| `1e-3f` | `float` | 0,001 |

```cpp
float a = 0.1;    // un double, converti en float : avertissement C4305
float b = 0.1f;   // un float dès le départ
```

Note:
Sans suffixe, un littéral à virgule est un `double`. MSVC signale la
conversion par l'avertissement C4305 « troncation de double à float ».

---

## Lire un `float` en hexadécimal

`0xC0D00000` : on découpe les 32 bits en signe, exposant, mantisse.

```
hexa       C    0    D    0    0    0    0    0
binaire    1100 0000 1101 0000 0000 0000 0000 0000

signe      1                             → négatif
exposant   1000 0001 = 129               → 129 - 127 = 2
mantisse   101 0000 0000 0000 0000 0000  → 1,101₂ = 1,625
```

valeur = −1,625 × 2² = **−6,5**

Note:
Valeur unique pour les trois slides (lire, coder, vérifier) : −6,5. Elle
montre à la fois le **bit de signe** à 1 et un **exposant** différent du
biais : la virgule a été déplacée de 2 rangs, stockés 2 + 127 = 129.

---

## Dans l'autre sens : −6,5

On repart du nombre et on retrouve `0xC0D00000` : signe, puis virgule déplacée, puis mantisse.

```
6,5 = 110,1₂ = 1,101₂ × 2²      la virgule recule de 2 rangs

signe      1              (négatif)
exposant   2 + 127 = 129 = 1000 0001
mantisse   101, puis 20 zéros

1 10000001 10100000000000000000000
= 1100 0000 1101 0000 0000 0000 0000 0000 = 0xC0D00000
```

---

## −6,5 en mémoire
<!-- .slide: class="schema" -->

Le signe tient en un bit ; le déplacement de la virgule devient l'exposant.

![[rnlb03_moins_6_5.svg]]

Note:
Lire le schéma de haut en bas : on normalise (−110,1₂ → −1,101₂ × 2²), le
nombre de rangs dont la virgule a reculé devient l'exposant (2, stocké
129), les chiffres après la virgule deviennent la mantisse. Puis les 32
bits se regroupent par 4 : C0D00000.
Faire varier à l'oral : −13 = −1,101₂ × 2³ → même mantisse, exposant 130,
soit 0xC1500000. Seul l'exposant change quand on double le nombre.

---

## Le vérifier en C++

`std::bit_cast` relit les mêmes 32 bits dans l'autre type : −6,5 ↔ `0xC0D00000`.

```cpp
#include <bit>
#include <cstdint>
#include <format>
#include <iostream>

int main()
{
    auto bits = std::bit_cast<std::uint32_t>(-6.5f);
    std::cout << std::format("{:08X}\n", bits);                            // C0D00000
    std::cout << std::bit_cast<float>(std::uint32_t{0xC0D00000}) << '\n';  // -6.5
}
```

`std::bit_cast` : C++20, dans `<bit>`. Pour jouer avec les bits : [h-schmidt.net/FloatConverter](https://www.h-schmidt.net/FloatConverter/IEEE754.html)

---

## À vous

```
0x3F800000  = ??
0xC1200000  = ??
0.75f       = 0x????????
```

Note:
Corrigé : 0x3F800000 = 1,0 (exposant 127, mantisse nulle) ;
0xC1200000 = −10,0 (exposant 130, mantisse 01) ; 0,75 = 1,1₂ × 2⁻¹, soit
un exposant stocké de 126 : 0x3F400000.

---

# Précision
<!-- .slide: class="title" -->

---

## Epsilon

L'écart entre 1 et le flottant qui le suit.

| | `float` | `double` |
|---|:-:|:-:|
| epsilon | 2⁻²³ ≈ 1,19 × 10⁻⁷ | 2⁻⁵² ≈ 2,22 × 10⁻¹⁶ |
| plus grande valeur | ≈ 3,4 × 10³⁸ | ≈ 1,8 × 10³⁰⁸ |

`std::numeric_limits<float>::epsilon()`, dans `<limits>`.

---

## L'écart grandit avec le nombre

| Valeur | Écart avec le `float` suivant |
|--:|--:|
| 1 | 0,000 000 12 |
| 1 000 | 0,000 061 |
| 100 000 | 0,007 8 |
| 16 777 216 (2²⁴) | 2 |

```cpp
float f = 16777216.0f;
bool b = (f + 1.0f == f);   // true : 16 777 217 n'existe pas en float
```

Note:
La mantisse a toujours 23 bits : quand l'exposant augmente de 1, l'écart
entre deux flottants voisins double. Au-delà de 2²⁴, un `float` ne sait
même plus représenter tous les entiers.

---

## L'imprécision en action : le chrono de partie

Un chrono qui additionne la durée de chaque image perd presque 3 secondes en une heure.

```cpp
float temps = 0.0f;
for (int frame = 0; frame < 60 * 60 * 60; ++frame)   // 1 h de jeu à 60 images/s
{
    temps += 1.0f / 60.0f;                            // 0,016666… arrondi à chaque ajout
}
std::println("{}", temps);   // 3597.2068 au lieu de 3600
```

Note:
Sortie vérifiée (GCC 14, C++23) : 3597.2068. Deux causes cumulées :
1/60 n'est pas représentable exactement, et plus `temps` grandit, plus
l'écart entre flottants voisins grandit (slide précédente) : chaque
petit ajout est arrondi plus grossièrement. En `double`, on obtient
3600.0000000182 — l'erreur existe toujours, mais 10⁸ fois plus petite.
Parade en jeu : compter les images en entier, ou relire une horloge
absolue plutôt que d'accumuler.

---

## Dans un moteur de jeu

- les positions sont souvent des `float`
- à 100 000 unités de l'origine, deux positions voisines sont séparées de **7,8 mm** si 1 unité vaut 1 m
- au-delà : caméra qui tremble, physique qui saute, animations qui vibrent
- l'Inspector d'Unity avertit dès qu'une coordonnée dépasse 100 000
- parade : l'**origine flottante** — on recentre régulièrement le monde autour du joueur

---

## Les valeurs spéciales

| Exposant | Mantisse | Valeur | Exemple |
|:-:|:-:|---|---|
| tout à 0 | 0 | ±0 | `0x00000000`, `0x80000000` |
| tout à 0 | ≠ 0 | sous-normaux, très proches de 0 | `0x00000001` ≈ 1,4 × 10⁻⁴⁵ |
| tout à 1 | 0 | ±∞ | `0x7F800000`, `0xFF800000` |
| tout à 1 | ≠ 0 | NaN, *Not a Number* | `0x7FC00000` |

- ±∞ : un résultat trop grand, ou 1 ÷ 0 selon IEEE 754
- NaN : une opération sans résultat — racine de −1, 0 ÷ 0, ∞ − ∞
- `+0 == -0` est vrai

---

## NaN : ce que c'est, à quoi ça sert

- *Not a Number* : le résultat d'une opération **sans réponse** — 0 ÷ 0, √−1, ∞ − ∞
- il sert à **ne pas planter** : le calcul continue, l'erreur voyage jusqu'au résultat
- il sert aussi de valeur « **absente** » : `std::numeric_limits<float>::quiet_NaN()`
- il ne se teste qu'avec `std::isnan(x)`, jamais avec `==`

Note:
Choix de la norme IEEE 754 : plutôt que d'interrompre le programme au
milieu d'un calcul, on produit une valeur qui dit « ici, ça n'a pas de
sens » et on laisse le programme décider plus tard. En binaire :
exposant tout à 1, mantisse non nulle — il existe donc des millions de
NaN différents (la mantisse peut même transporter un code d'erreur).
Usage « valeur absente » : une mesure de capteur manquante, une case de
tableau de données non remplie (les bibliothèques d'analyse de données
s'en servent ainsi).
En jeu : une position NaN fait disparaître l'objet ; Unity le signale
souvent par des erreurs de bounding box invalide.

---

## NaN contamine tout

```cpp
float nan = std::sqrt(-1.0f);

bool a = (nan == nan);    // false !
bool b = (nan != nan);    // true
bool c = (nan < 1.0f);    // false
bool d = (nan > 1.0f);    // false
bool e = std::isnan(nan); // true : la seule façon fiable de tester
```

- toute opération arithmétique avec un NaN donne NaN
- une vitesse devient NaN, et l'objet disparaît de l'écran sans la moindre erreur

---

# Comparer des flottants
<!-- .slide: class="title" -->

---

## Pourquoi l'égalité ment

```cpp
if(0.1 + 0.2 == 0.3){
	std::println("Vrai ou faux ?"); 
}   // false : 0.1 + 0.2 = 0.30000000000000004

float t = 0.0f;
for (int i = 0; i < 10; ++i)
    t += 0.1f;
    
if(t == 1.0f){
	std::println("Vrai ou faux ?"); 
}          // false : t = 1.0000001
```

- chaque valeur a été **arrondie**, et les erreurs s'accumulent
- `0.1f + 0.2f == 0.3f` est vrai… par chance : les arrondis tombent au même endroit
- le résultat dépend des valeurs, du type, parfois des options du compilateur : `==` est **imprévisible**

Note:
Piège d'affichage : `std::cout << t` montre `1`, parce que le flux arrondit
à 6 chiffres significatifs. `std::format("{}", t)` affiche `1.0000001`.

---

## Le piège de la boucle

```cpp
for (float x = 0.0f; x != 1.0f; x += 0.1f)
{
    // ne s'arrête jamais : x passe de 0.9000001 à 1.0000001
}
```

Une condition avec **`<`**, ou mieux, un compteur **entier** :

```cpp
for (int i = 0; i <= 10; ++i)
{
    float x = i * 0.1f;
}
```

---

## Comparer avec une tolérance

```cpp
#include <algorithm>
#include <cmath>

bool presque_egaux(float a, float b)
{
    const float diff = std::abs(a - b);
    if (diff <= 1e-6f) return true;                                // près de zéro
    return diff <= 1e-5f * std::max(std::abs(a), std::abs(b));     // relatif
}
```

- une tolérance **relative** suit la taille des nombres ; près de zéro, il faut une tolérance **absolue**
- pas de valeur universelle : elle dépend de ce que les nombres représentent — mètres, degrés, pixels
- côté Unity : `Mathf.Approximately(a, b)`

---

## Du flottant vers l'entier

```cpp
int a = static_cast<int>(2.9f);    //  2 : troncature vers zéro
int b = static_cast<int>(-2.9f);   // -2
long c = std::lround(2.5f);        //  3 : arrondi au plus proche
long d = std::lround(-2.5f);       // -3
```

- un flottant hors de la plage de l'entier visé : **comportement indéfini**
- Ariane 5, vol 501 (1996) : une valeur liée à la vitesse horizontale, flottant sur 64 bits, est convertie en entier signé de 16 bits ; la conversion déborde et la fusée est détruite moins de 40 secondes après le décollage

---

# Clôture
<!-- .slide: class="title" -->

---

## À retenir

- un flottant = **signe × mantisse × 2^exposant**, sur 32 ou 64 bits
- `float` : 1 + 8 + 23 bits, biais 127 ; `double` : 1 + 11 + 52 bits, biais 1023
- la plupart des décimaux sont **arrondis**, et l'écart entre flottants grandit avec la valeur
- ±0, ±∞ et NaN existent ; `NaN != NaN`
- jamais `==` entre flottants calculés : une **tolérance**

---

## Exercices

- lire des flottants donnés en hexadécimal, en coder d'autres
- prévoir le résultat de comparaisons et de conversions
- écrire `presque_egaux`

Énoncés : [[01 courses/exercises/Theory/TC-FT-RNLB-03 - Flottants IEEE 754]]

---

## Pour aller plus loin

- Séance suivante : [[01 courses/slides/Theory/TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit|TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit]]
- [Float Converter — h-schmidt.net](https://www.h-schmidt.net/FloatConverter/IEEE754.html) : voir les bits d'un `float`
- [The Floating-Point Guide](https://floating-point-gui.de/) : l'essentiel, en court
- [Comparing Floating Point Numbers, 2012 Edition — Bruce Dawson](https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/)
- [IEEE 754 — Wikipédia](https://fr.wikipedia.org/wiki/IEEE_754)
