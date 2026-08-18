---
title: Introduction to logic
type: course
duration_h: 3
bloc: "[[Bases de la Programmation]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Introduction to logic
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Opérateurs, algèbre de Boole, arithmétique non décimale

<small>Module 4FSC0PF001 · Introduction to Games Programming</small>

Note:
Deux sujets liés dans une même séance : d'abord les opérateurs du langage
et l'algèbre booléenne qui les gouverne, ensuite les bases de numération.
Le lien entre les deux, c'est que la machine ne connaît que le binaire.

---

## Source
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine (contient les schémas non transposés) :

- 🔗 [Google Slides — 02 Introduction to logic](https://docs.google.com/presentation/d/1n-YUpykKSHexQ1hc6MRz3oKSkXam_iX5HYEDIY1dvSc/edit)

Exercices : [[Exercices - 02 - Introduction to Logic]] · Référence : [[Truth table]]

</div>

---

# Opérateurs C++
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## C++ operators — arithmétique
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

| Operator | Name | Description | Example |
|:-:|---|---|:-:|
| `+` | Addition | adds together values | `x + y` |
| `-` | Subtraction | subtracts one value from another | `x - y` |
| `*` | Multiplication | multiplies two values | `x * y` |
| `/` | Division | divides one value by another | `x / y` |
| `%` | Modulus | returns the division remainder | `x % y` |

---

## C++ operators — incrément et décalage
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

| Operator | Name | Description | Example |
|:-:|---|---|:-:|
| `++` | Increment (pre) | increases the value of a variable by 1 | `++x` |
| `--` | Decrement (pre) | decreases the value of a variable by 1 | `--x` |
| `++` | Increment (post) | same, but after assignment | `x++` |
| `--` | Decrement (post) | same, but after assignment | `x--` |
| `>>` | Roll right | shift a number to the right (carry sign ⚠) | `x >> 5` |
| `<<` | Roll left | shift a number to the left | `x << 5` |

---

## C++ assignment operators
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

| Operator | Example | Same as | | Operator | Example | Same as |
|:-:|:-:|:-:|---|:-:|:-:|:-:|
| `=` | `x = 5` | `x = 5` | | `%=` | `x %= 5` | `x = x % 5` |
| `+=` | `x += 5` | `x = x + 5` | | `&=` | `x &= 5` | `x = x & 5` |
| `-=` | `x -= 5` | `x = x - 5` | | `\|=` | `x \|= 5` | `x = x \| 5` |
| `*=` | `x *= 5` | `x = x * 5` | | `^=` | `x ^= 5` | `x = x ^ 5` |
| `/=` | `x /= 5` | `x = x / 5` | | `>>=` | `x >>= 5` | `x = x >> 5` |
| | | | | `<<=` | `x <<= 5` | `x = x << 5` |

---

## Boolean operations
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

`True` et `False`, combinés par : **and** (`&&`), **or** (`||`), **equal** (`==`), **not equal** (`!=`).

À vous :

```
True and False                            = ??
True or False                             = ??
True != False                             = ??
(True || False) && (True == False)        = ??
(False == False) || (True != True)        = ??
```

---

## Integer operations to boolean
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

| Opérateur | Signification |
|:-:|---|
| `>` | greater than |
| `<` | smaller than |
| `>=` | greater or equal than |
| `<=` | smaller or equal than |
| `==` | equal |
| `!=` | not equal |

```
3 > 2                     = ??
2 != 1                    = ??
4 < 1                     = ??
(4 > 1) && (2 < 1)        = ??
(4 == 3) || (2 > 1)       = ??
```

---

# Algèbre de Boole
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Operator AND
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

A and B (`A && B`) : **a ∧ b**

| a | b | AND |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

---

## Operator OR
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

A or B (`A || B`) : **a ∨ b**

| a | b | OR |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

---

## Operator NOT
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Not A (`!a`) : **¬a**

| a | NOT |
|:-:|:-:|
| 0 | 1 |
| 1 | 0 |

---

## Commutativité
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
a ∧ b  =  b ∧ a

a ∨ b  =  b ∨ a
```

---

## Distributivité mutuelle
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
a ∧ (b ∨ c)  =  (a ∧ b) ∨ (a ∧ c)

a ∨ (b ∧ c)  =  (a ∨ b) ∧ (a ∨ c)
```

---

## Lois de De Morgan
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
!(a ∧ b)  =  !a ∨ !b

!(a ∨ b)  =  !a ∧ !b
```

Note:
Ces deux lois sont celles que vous utiliserez le plus souvent en pratique,
pour simplifier une condition qui commence par une négation. C'est le
même outil que dans l'exercice 2.2.

---

## Priorité des opérateurs
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

1. **not** est évalué en premier
2. **and** est évalué en deuxième
3. **or** est évalué en dernier

---

# Arithmétique non décimale
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Non-decimal arithmetic
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

What is a decimal number ? It's a sum of *a* × 10ⁿ.

Exemple avec **368** :

| Chiffre | Poids | Valeur |
|:-:|:-:|:-:|
| 3 | 3 × 10² | 300 |
| 6 | 6 × 10¹ | 60 |
| 8 | 8 × 10⁰ | 8 |

---

## Changer de base
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Le même principe, mais en base 9 :

```
5 + 9 * 4 + 81 * 3
```

Note:
La base n'est qu'un choix de poids. Ici 81 = 9², 9 = 9¹, 1 = 9⁰ : rien
ne change dans la méthode, seule la valeur de la base change.

---

## Hexadecimal
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Préfixe `0x`. Digits are **0 to F** (= 15).

Exemple avec `0x182` :

| Chiffre | Poids | Valeur |
|:-:|:-:|:-:|
| 1 | 1 × 16² | 256 |
| 8 | 8 × 16¹ | 128 |
| 2 | 2 × 16⁰ | 2 |

---

## Hexadecimal — la table
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

| Hexa | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Décimal** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |

---

## Binary
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Digits are **0 or 1**.

Exemple avec `1100000010` :

| Bit posé | Poids | Valeur |
|:-:|:-:|:-:|
| 1 | 1 × 2⁹ | 512 |
| 1 | 1 × 2⁸ | 256 |
| 1 | 1 × 2¹ | 2 |

⇒ 512 + 256 + 2 = **770**
