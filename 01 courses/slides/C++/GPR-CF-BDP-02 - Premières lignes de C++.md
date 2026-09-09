---
title: Premières lignes de C++
type: slides
status: Backlog
subject: C++
duration_h: 3
bloc_gsda: Bases de la Programmation
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
manual_order: 9
---
# Premières lignes de C++
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

---

## C++ : la base
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

C++ est en fait **3 langages** :

- le **pre-processor** (ne pas utiliser)
- les **templates** (pour les utilisateurs avancés)
- le **code** (langage C++)

Arrêtez de vous blâmer : c'est le langage le plus performant qui existe !

---

## C++ : l'historique
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

| Version   | Apport                                                                        |
| --------- | ----------------------------------------------------------------------------- |
| **C++98** | le standard ISO                                                               |
| **C++11** | supporté quasiment partout — lambdas, `auto`, variadic templates, `constexpr` |
| **C++14** | bugfix de C++11 (surtout)                                                     |
| **C++17** | beaucoup de support côté bibliothèque, `auto` en paramètre                    |
| **C++20** | modules, traits, …                                                            |
| **C++23** |                                                                               |
| C++26     |                                                                               |

---

# Écrire du code
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

---

## Comments
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

You can actually write whatever you want after `//`, or between `/*` and `*/`.

To be used when some code could be unclear or too complex.

---

## Hello World — cpp.sh
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```cpp
#include <iostream>

int main()
{
    // This is how you can output something on the console!
    std::cout << "Hello world!\n";
    return 0;
}
```

You can use :

- `std::cout << "output stuff";`
- `std::cin >> values;`

---

## Variables
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Numbers, characters, arrays, complex numbers, creatures, …

- All data are contained in **variables**
- Then you do **operations** on those data
- You can overload `*`, `/`, `+`, `-`, …

---

## Basic types
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

| Type | Contenu |
|---|---|
| `bool` | boolean (`true` or `false`) |
| `char` | character (`'a'`, `'b'`) |
| `int` | integer number |
| `float` | floating point |
| `double` | double floating point |
| `void` | valueless |

**Modifiers :** `signed` (+/−) / `unsigned` (+) · `short` / `long` · `const` · `auto`

---

## Size in memory ⚠ on Windows ⚠
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

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

## Operations on integers
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```cpp
int a = 3;  int b = 2;  int c = 0;

c = a + b;      // c = ??
c = a - b;      // c = ??
c = a * b;      // c = ??
c = a / b;      // c = ??
c = c + 1;      // using previous result, c = ??
c = a - c * b;  // using previous result, c = ??
```

---

## Priorité des opérateurs
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

1. `()`
2. `*`, `/` et `%`
3. `+` et `-`
4. de gauche à droite

```
  1 + 2 * 3   = ??
  1 + (2 * 3) = ??
  (1 + 2) * 3 = ??
```

<small>[en.cppreference.com/w/cpp/language/operator_precedence](https://en.cppreference.com/w/cpp/language/operator_precedence)</small>

---

## Text output
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```cpp
#include <iostream>

int main()
{
    std::cout << "value = " << value << "\n";
    return 0;
}
```

---

## Function — main
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```cpp
#include <iostream>

void main() { }   // ???

int main() { }

int main(int ac, char** av)
{
    std::cout << "Hello World!\n";
    return 0;
}
```

Forme générale :

```cpp
Return-type Function-name (Arguments)
{
    return Return-value;
}
```

---