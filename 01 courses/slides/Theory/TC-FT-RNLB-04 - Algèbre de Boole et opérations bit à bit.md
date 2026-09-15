---
title: Algèbre de Boole et opérations bit à bit
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

# Algèbre de Boole et opérations bit à bit
<!-- .slide: class="title" -->

### Des tables de vérité aux masques

<small>TC-FT-RNLB-04 · Représentation des Nombres et Logique Binaire</small>

Note:
Deux sujets liés dans une même séance : d'abord l'algèbre booléenne qui
gouverne les conditions, ensuite les mêmes opérations appliquées à chaque
bit d'un entier. Le lien entre les deux, c'est que la machine ne connaît
que le binaire.

---

## Objectifs

À la fin de la séance, vous savez :

- écrire la table de vérité d'une expression booléenne
- simplifier une condition avec les lois de De Morgan
- distinguer `&&` de `&`, et `||` de `|`
- poser un masque et un décalage à partir d'une table de vérité
- ranger plusieurs booléens dans un seul entier

**Prérequis :** binaire et hexadécimal — [[01 courses/slides/Theory/TC-FT-RNLB-01 - Bases et changements de base|TC-FT-RNLB-01]].

---

# Booléens en C++
<!-- .slide: class="title" -->

---

## Opérations booléennes

`true` et `false`, combinés par : **et** (`&&`), **ou** (`||`), **égal** (`==`), **différent** (`!=`).

À vous :

```
true && false                             = ??
true || false                             = ??
true != false                             = ??
(true || false) && (true == false)        = ??
(false == false) || (true != true)        = ??
```

Note:
Corrigé : false, true, true, false, true.

---

## Des entiers aux booléens

| Opérateur | Signification |
|:-:|---|
| `>` | strictement supérieur |
| `<` | strictement inférieur |
| `>=` | supérieur ou égal |
| `<=` | inférieur ou égal |
| `==` | égal |
| `!=` | différent |

```
3 > 2                     = ??
2 != 1                    = ??
4 < 1                     = ??
(4 > 1) && (2 < 1)        = ??
(4 == 3) || (2 > 1)       = ??
```

Note:
Corrigé : true, true, false, false, true.

---

# Algèbre de Boole
<!-- .slide: class="title" -->

---

## Opérateur ET

a et b (`a && b`) : **a ∧ b**

| a | b | ET |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

---

## Opérateur OU

a ou b (`a || b`) : **a ∨ b**

| a | b | OU |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

---

## Opérateur NON

non a (`!a`) : **¬a**

| a | NON |
|:-:|:-:|
| 0 | 1 |
| 1 | 0 |

---

## Opérateur OU exclusif

a ou exclusif b (`a != b` sur des booléens, `a ^ b` sur des bits) : **a ⊕ b**

| a | b | OU exclusif |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Vrai quand **exactement un** des deux est vrai.

---

## Construire une table de vérité

Pour `a ∧ (b ∨ c)` : une ligne par combinaison, une colonne par sous-expression.

| a | b | c | b ∨ c | a ∧ (b ∨ c) |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 |

*n* variables donnent 2ⁿ lignes : on compte en binaire de 0 à 2ⁿ − 1.

---

## Commutativité

```
a ∧ b  =  b ∧ a

a ∨ b  =  b ∨ a
```

---

## Distributivité mutuelle

```
a ∧ (b ∨ c)  =  (a ∧ b) ∨ (a ∧ c)

a ∨ (b ∧ c)  =  (a ∨ b) ∧ (a ∨ c)
```

---

## Lois de De Morgan

```
!(a ∧ b)  =  !a ∨ !b

!(a ∨ b)  =  !a ∧ !b
```

Note:
Ces deux lois sont celles que vous utiliserez le plus souvent en pratique,
pour simplifier une condition qui commence par une négation. C'est le
même outil que dans l'exercice 2.2.

---

## De Morgan dans le code

```cpp
// ni mort, ni en pause
if (!(joueur_mort || jeu_en_pause)) { /* ... */ }

// la même condition, après De Morgan
if (!joueur_mort && !jeu_en_pause) { /* ... */ }
```

Une négation devant une parenthèse : on la **distribue** sur chaque terme, et on **échange** `&&` et `||`.

---

## Priorité des opérateurs

1. **non** est évalué en premier
2. **et** est évalué en deuxième
3. **ou** est évalué en dernier

`a || b && !c` se lit `a || (b && (!c))`.

---

# Opérations bit à bit
<!-- .slide: class="title" -->

---

## Le même calcul, sur chaque bit

| Sur des booléens | Sur chaque bit | Nom |
|:-:|:-:|---|
| `&&` | `&` | ET |
| `\|\|` | `\|` | OU |
| `!` | `~` | NON |
| `!=` | `^` | OU exclusif |

```
  1100        1100        1100        ~ 1100
& 1010      | 1010      ^ 1010
= 1000      = 1110      = 0110        = 0011
```

Le `~` est montré sur 4 bits. Rappel : `0b` pour le binaire, `0x` pour l'hexadécimal ; un chiffre hexadécimal vaut 4 bits.

Note:
`&&` et `||` travaillent sur des valeurs de vérité et s'arrêtent dès que
le résultat est connu : c'est l'évaluation en court-circuit. `&` et `|`
calculent toujours les deux côtés, bit par bit. Confondre `&&` et `&`
compile, et donne parfois le bon résultat : le pire des bugs.

---

## Incrément et décalage

| Opérateur | Nom | Description | Exemple |
|:-:|---|---|:-:|
| `++` | Incrément (pré) | augmente la variable de 1 | `++x` |
| `--` | Décrément (pré) | diminue la variable de 1 | `--x` |
| `++` | Incrément (post) | idem, mais renvoie l'ancienne valeur | `x++` |
| `--` | Décrément (post) | idem, mais renvoie l'ancienne valeur | `x--` |
| `>>` | Décalage à droite | décale les bits vers la droite (conserve le signe ⚠) | `x >> 5` |
| `<<` | Décalage à gauche | décale les bits vers la gauche | `x << 5` |

Note:
Le support d'origine appelait `>>` et `<<` « roll » : ce sont des
décalages (*shift*). La rotation, où les bits qui sortent rentrent de
l'autre côté, existe aussi : `std::rotl` et `std::rotr`, C++20.

---

## Décaler, c'est multiplier ou diviser par 2ⁿ

```cpp
1u << 3      //  8  : 0000 0001 → 0000 1000
5u << 4      // 80  : × 2⁴
40u >> 2     // 10  : ÷ 2²
0xF0u >> 4   // 15  : 1111 0000 → 0000 1111
```

- les bits qui sortent sont **perdus** ; côté vide, des 0 entrent
- un négatif décalé à droite garde son signe : `-8 >> 1` vaut `-4`
- décaler d'autant de bits que la taille du type, ou plus : **comportement indéfini**
- pour manipuler des bits, des types **non signés**

---

## Opérateurs d'affectation

| Opérateur | Exemple | Équivaut à | | Opérateur | Exemple | Équivaut à |
|:-:|:-:|:-:|---|:-:|:-:|:-:|
| `=` | `x = 5` | `x = 5` | | `%=` | `x %= 5` | `x = x % 5` |
| `+=` | `x += 5` | `x = x + 5` | | `&=` | `x &= 5` | `x = x & 5` |
| `-=` | `x -= 5` | `x = x - 5` | | `\|=` | `x \|= 5` | `x = x \| 5` |
| `*=` | `x *= 5` | `x = x * 5` | | `^=` | `x ^= 5` | `x = x ^ 5` |
| `/=` | `x /= 5` | `x = x / 5` | | `>>=` | `x >>= 5` | `x = x >> 5` |
| | | | | `<<=` | `x <<= 5` | `x = x << 5` |

---

## Un masque, lu dans la table de vérité

Pour chaque bit `x` de la valeur et chaque bit `m` du masque :

| Opération | là où `m` = 0 | là où `m` = 1 |
|:-:|:-:|:-:|
| `x & m` | 0 | x |
| `x \| m` | x | 1 |
| `x ^ m` | x | ¬x |

- `&` **garde** les bits sous les 1 du masque et **efface** les autres
- `|` **force à 1** les bits sous les 1 du masque
- `^` **inverse** les bits sous les 1 du masque

---

## Masques : les quatre gestes

| Geste | Code | Effet sur le bit visé |
|---|---|---|
| tester | `(x & masque) != 0` | vrai si le bit vaut 1 |
| allumer | `x \|= masque` | force à 1 |
| éteindre | `x &= ~masque` | force à 0 |
| basculer | `x ^= masque` | inverse |

Le masque du bit *n* se construit par décalage : `1u << n`.

---

## Extraire un champ : une couleur ARGB

Une couleur sur 32 bits : `0xAARRGGBB`

```cpp
std::uint32_t couleur = 0xFFA0522D;         // terre de Sienne, opaque

std::uint32_t r = (couleur >> 16) & 0xFF;   // 0xA0 = 160
std::uint32_t g = (couleur >> 8)  & 0xFF;   // 0x52 = 82
std::uint32_t b =  couleur        & 0xFF;   // 0x2D = 45

std::uint32_t recomposee = (0xFFu << 24) | (r << 16) | (g << 8) | b;
```

On **décale** pour amener le champ à droite, puis on **masque** pour ne garder que ses bits.

---

## Le piège de la priorité

```cpp
if (etat & VISIBLE == 0)     // lu : etat & (VISIBLE == 0)
if ((etat & VISIBLE) == 0)   // ce qu'on voulait dire
```

En C++, `==` et `!=` passent **avant** `&`, `^` et `|` :

`!` `~` → `*` `/` `%` → `+` `-` → `<<` `>>` → `<` `<=` `>` `>=` → `==` `!=` → `&` → `^` → `|` → `&&` → `||`

Le compilateur prévient — C4554 sous MSVC, `-Wparentheses` sous GCC : **parenthésez**.

<small>[en.cppreference.com/w/cpp/language/operator_precedence](https://en.cppreference.com/w/cpp/language/operator_precedence)</small>

---

# Drapeaux compactés
<!-- .slide: class="title" -->

---

## Un bit par drapeau

```cpp
#include <cstdint>

enum Etat : std::uint8_t
{
    Visible    = 1 << 0,   // 0000 0001
    Solide     = 1 << 1,   // 0000 0010
    Ennemi     = 1 << 2,   // 0000 0100
    Invincible = 1 << 3,   // 0000 1000
};
```

Chaque valeur n'a **qu'un seul bit à 1**, et jamais le même : on peut les combiner sans qu'elles se mélangent.

---

## Les quatre gestes, sur des drapeaux

```cpp
std::uint8_t etat = Visible | Solide;    // 0000 0011

etat |= Ennemi;                          // allumer   → 0000 0111
etat &= ~Solide;                         // éteindre  → 0000 0101
etat ^= Invincible;                      // basculer  → 0000 1101

bool visible = (etat & Visible) != 0;    // tester    → true
```

Tester plusieurs drapeaux d'un coup : `(etat & (Solide | Ennemi)) != 0`.

---

## Pourquoi compacter ?

- **mémoire** : 8 drapeaux dans 1 octet, au lieu de 8 `bool` — souvent 8 octets
- **fichiers, réseau** : on écrit un octet, pas une structure
- on les croise partout :
  - Unity, `LayerMask` : `1 << 8` vise la couche 8, `~(1 << 8)` toutes les autres
  - Unix, `chmod 755` : r = 4, w = 2, x = 1, un chiffre octal par groupe
  - OpenGL : `glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)`

---

## `std::bitset` : les bits sans les pièges

```cpp
#include <bitset>
#include <iostream>

std::bitset<8> etat{0b0000'0101};
etat.set(3);              // allumer le bit 3   → 0000 1101
etat.reset(0);            // éteindre le bit 0  → 0000 1100
etat.flip(1);             // basculer le bit 1  → 0000 1110
bool b = etat.test(2);    // tester le bit 2    → true

std::cout << etat << " : " << etat.count() << " bits à 1\n";   // 00001110 : 3 bits à 1
```

Note:
Les numéros de bits se comptent depuis la droite, à partir de 0. Pour
des drapeaux nommés, l'`enum` reste plus lisible ; `std::bitset` évite les
pièges de promotion et de priorité.

---

# Clôture
<!-- .slide: class="title" -->

---

## À retenir

- une table de vérité : 2ⁿ lignes, une colonne par sous-expression
- De Morgan : `!(a && b)` = `!a || !b` et `!(a || b)` = `!a && !b`
- `&&` `||` `!` sur des booléens ; `&` `|` `^` `~` sur chaque bit
- masque : `&` pour tester et éteindre, `|` pour allumer, `^` pour basculer ; `1u << n` vise le bit *n*
- `==` passe avant `&` : **parenthésez**

---

## Exercices

- tables de vérité, et l'expression qui produit une table donnée
- De Morgan dans des conditions de jeu
- masques, couleurs et drapeaux

Énoncés : [[01 courses/exercises/Theory/TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit]]

Référence : [[Truth table]]

---

## Pour aller plus loin

- [Algèbre de Boole — Wikipédia](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_de_Boole_(logique))
- [std::bitset — cppreference](https://en.cppreference.com/w/cpp/utility/bitset)
- [LayerMask — documentation Unity](https://docs.unity3d.com/ScriptReference/LayerMask.html)
- [Bit Twiddling Hacks — Sean Eron Anderson](https://graphics.stanford.edu/~seander/bithacks.html) : pour les curieux
