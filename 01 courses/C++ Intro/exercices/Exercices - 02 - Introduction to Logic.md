# Exercices — 02 — Introduction to Logic

> Source : [Google Docs](https://docs.google.com/document/d/1AdyLhRPLkF83w6Oh0DzUrVPcXM5GmTqPe_4lK3TvIaw/edit)
> Cours associé : [[02 - Introduction to logic - non decimal arithmetic]] · Voir aussi [[Truth table]]

## Exercise 1.1 — Classroom

Write the truth table for the boolean expression : `(a∧b)∨(!a∨b)`

| a | b | a ∧ b | !a | !a ∨ b | (a∧b)∨(!a∨b) |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 | 1 |

## Exercise 1.2 — Formative

Write the truth table for the boolean expression : `!(a∧!b)∨(!a∨b)`

## Exercise 1.3 — Formative

Write the truth table for the boolean expression : `(a∧c)∨(!a∨b)∧!(c∨!b)`

## Exercise 2.1 — Classroom

Find the boolean expression that produces the following table (only using `!`, `∧`, `∨`) — multiple solutions exist.

| a | b | Boolean expression |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## Exercise 2.2 — corrigé

Find the boolean expression that produces the following table (only using `!`, `∧`, `∨`).

| a | b | terme | Boolean expression |
|:-:|:-:|:-:|:-:|
| 0 | 0 | `!a && !b = 1` | 1 |
| 0 | 1 |  | 0 |
| 1 | 0 | `a && !b = 1` | 1 |
| 1 | 1 | `a && b = 1` | 1 |

Simplification étape par étape :

```
(!a && !b) || (a && !b) || (a && b) = 1
!(a || b)  || (a && !b) || (a && b) = 1
!(a || b)  || a || (!b && b)        = 1
!(a || b)  || a || 0                = 1
!(a || b)  || a                     = 1
a || !b
```

Vérification :

| a | b | !b | a ∨ !b |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |

Étape 4 — pourquoi `(!b && b)` disparaît :

| b | !b | (!b && b) |
|:-:|:-:|:-:|
| 0 | 1 | 0 |
| 1 | 0 | 0 |

## Formative — conversions de base

Compléter le tableau :

| Valeur décimale | Valeur hexadécimale | Valeur binaire |
|:-:|:-:|:-:|
|  | AF = 10 × 16 + 15 = 175 |  |
|  | ACD |  |
|  | AB2 |  |
|  | FF |  |
| 25 | 19 | 11001 |
| 147 |  |  |
| 39554 |  | 1001 1010 1000 0010 |
| 15637 |  |  |
| 2856 |  |  |

Décomposition de 39554, à titre d'exemple de méthode :

```
39554 = 32768 + 6786
39554 = 32768 + 4096 + 2690
39554 = 32768 + 4096 + 2048 + 642
39554 = 32768 + 4096 + 2048 + 512 + 130
39554 = 32768 + 4096 + 2048 + 512 + 128 + 2
39554 = 2^15 + 2^12 + 2^11 + 2^9 + 2^7 + 2^1
```
