# Exercices — TC-FT-RNLB-04 — Algèbre de Boole et opérations bit à bit

> Cours associé : [[01 courses/slides/Theory/TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit]] · Voir aussi [[Truth table]]
> Source des exercices 1 et 2 : [Exercices 02 — Google Docs](https://docs.google.com/document/d/1AdyLhRPLkF83w6Oh0DzUrVPcXM5GmTqPe_4lK3TvIaw/edit)

## Exercice 1.1 — En classe

Écrire la table de vérité de l'expression booléenne : `(a∧b)∨(!a∨b)`

| a | b | a ∧ b | !a | !a ∨ b | (a∧b)∨(!a∨b) |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 | 1 |

## Exercice 1.2 — Formative

Écrire la table de vérité de l'expression booléenne : `!(a∧!b)∨(!a∨b)`

## Exercice 1.3 — Formative

Écrire la table de vérité de l'expression booléenne : `(a∧c)∨(!a∨b)∧!(c∨!b)`

## Exercice 2.1 — En classe

Trouver l'expression booléenne qui produit la table suivante, en n'utilisant que `!`, `∧` et `∨`. Plusieurs solutions existent.

| a | b | Expression booléenne |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## Exercice 2.2 — Corrigé

Trouver l'expression booléenne qui produit la table suivante, en n'utilisant que `!`, `∧` et `∨`.

| a | b | terme | Expression booléenne |
|:-:|:-:|:-:|:-:|
| 0 | 0 | `!a && !b = 1` | 1 |
| 0 | 1 |  | 0 |
| 1 | 0 | `a && !b = 1` | 1 |
| 1 | 1 | `a && b = 1` | 1 |

Simplification étape par étape :

```
(!a && !b) || (a && !b) || (a && b)
!(a || b)  || (a && !b) || (a && b)     De Morgan
!(a || b)  || (a && (!b || b))          distributivité
!(a || b)  || (a && 1)                  !b || b vaut toujours 1
!(a || b)  || a
(!a && !b) || a                         De Morgan
(!a || a)  && (!b || a)                 distributivité
a || !b                                 !a || a vaut toujours 1
```

Vérification :

| a | b | !b | a ∨ !b |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |

Pourquoi `(!b || b)` vaut toujours 1 :

| b | !b | (!b \|\| b) |
|:-:|:-:|:-:|
| 0 | 1 | 1 |
| 1 | 0 | 1 |

## Exercice 3 — De Morgan dans le code

Réécrire chaque condition sans négation devant une parenthèse :

1. `!(vie > 0 && munitions > 0)`
2. `!(touche_gauche || touche_droite)`
3. `!(x < 0 || x >= largeur || y < 0 || y >= hauteur)`

## Exercice 4 — Opérations bit à bit, à la main

Sur 8 bits non signés, avec `a = 0b1101'0110` et `b = 0b0101'1100`, calculer en binaire et en hexadécimal :

`a & b` · `a | b` · `a ^ b` · `~a` · `a << 2` (en gardant 8 bits) · `a >> 3`

## Exercice 5 — Masques

Soit `std::uint8_t x = 0b1010'0000;`. Écrire l'instruction qui, dans l'ordre :

1. allume le bit 0
2. éteint le bit 7
3. bascule les 4 bits de poids faible
4. teste si le bit 5 est allumé

Donner la valeur binaire de `x` après chaque étape.

## Exercice 6 — Couleurs

1. Écrire `std::uint8_t canal_vert(std::uint32_t argb)`, qui renvoie la composante verte d'une couleur `0xAARRGGBB`.
2. Écrire `std::uint32_t avec_alpha(std::uint32_t argb, std::uint8_t alpha)`, qui remplace la composante alpha.
3. Tester : `canal_vert(0xFF336699)` doit valoir `0x66`, et `avec_alpha(0xFF336699, 0x80)` doit valoir `0x80336699`.

## Exercice 7 — Les drapeaux d'une entité

1. Définir six drapeaux dans un `std::uint8_t` : `Visible`, `Solide`, `Ennemi`, `Invincible`, `EnFeu`, `Gele`.
2. Écrire `allumer`, `eteindre`, `basculer` et `est_allume`.
3. Écrire une fonction qui affiche l'état en binaire, puis la liste des drapeaux allumés.

### Bonus

Refaire l'exercice avec `std::bitset<8>`, et comparer la lisibilité des deux versions.

## Exercice 8 — Le piège de la priorité

Ce test n'affiche jamais « solide », alors que l'entité l'est. Pourquoi ? Le corriger.

```cpp
const unsigned SOLIDE = 1u << 1;
unsigned etat = 0b0010;
if (etat & SOLIDE != 0)
    std::cout << "solide\n";
```
