# Truth table

> Source : [Google Sheets](https://docs.google.com/spreadsheets/d/1m8pm8AT__nPt7bC67bGFnnhdso4ZAk2DjFetnMSOhYA/edit)
> Cours associé : [[02 - Introduction to logic - non decimal arithmetic]] · [[Exercices - 02 - Introduction to Logic]]

Tables de vérité de référence des opérateurs booléens du cours.

## AND — `A && B`

| A | B | A && B |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## OR — `A || B`

| A | B | A \|\| B |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

## NOT — `!A`

| A | !A |
|:-:|:-:|
| 0 | 1 |
| 1 | 0 |

## XOR — `A ^ B`

| A | B | A ^ B |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Égalité — `A == B`

| A | B | A == B |
|:-:|:-:|:-:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## Différence — `A != B`

| A | B | A != B |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Expression composée — `A && (B || C)`

La colonne « # » donne la valeur décimale des trois bits `ABC`, pour montrer qu'une table de vérité à *n* variables énumère simplement les entiers de 0 à 2ⁿ−1.

| A | B | C | # | B \|\| C | A && (B \|\| C) |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 | 0 |
| 0 | 1 | 0 | 2 | 1 | 0 |
| 0 | 1 | 1 | 3 | 1 | 0 |
| 1 | 0 | 0 | 4 | 0 | 0 |
| 1 | 0 | 1 | 5 | 1 | 1 |
| 1 | 1 | 0 | 6 | 1 | 1 |
| 1 | 1 | 1 | 7 | 1 | 1 |
