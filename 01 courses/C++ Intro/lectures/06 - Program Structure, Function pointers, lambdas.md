---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Program Structure
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Compilation, function pointers, functors, lambdas

<small>Sébastien Albert · Module 4FSC0PF001</small>

Note:
Deux moitiés dans cette séance. D'abord ce qui se passe entre votre code
source et l'exécutable — préprocesseur, compilation, linkage. Ensuite,
comment passer une fonction en paramètre : pointeur de fonction, functor,
et finalement la lambda, qui remplace les deux.

---

## Source
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine (contient les schémas non transposés) :

- 🔗 [Google Slides — 06 Program Structure, Function pointers, lambdas](https://docs.google.com/presentation/d/19yelZ4RW_DA6tjML_gIsVDftDDvVToMGCR_ks7l2srU/edit)

Exercices : [[Exercices - 06 - Program Structure, Function pointers, lambdas]]

</div>

---

## Program structure — les questions
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- What is a program ?
- What is the entry point ?
- What is a function ?
- How do we add something from somewhere else ?
- What is this `#include` ?
- What is linking ?

---

# Entry point
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Entry point !
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

This is where the C stack starts.

```cpp
int main() { ... }

int main(int ac, char** av) { ... }

int WINAPI WinMain(
    HINSTANCE hInstance,
    HINSTANCE hPrevInstance,
    PWSTR pCmdLine,
    int nCmdShow) { ... }
```

- **hInstance** — a « handle to an instance » or « handle to a module ». The OS uses this value to identify the executable (EXE) when it is loaded in memory. Needed for certain Windows functions — for example, to load icons or bitmaps.
- **hPrevInstance** — has no meaning. It was used in 16-bit Windows, but is now always zero.
- **pCmdLine** — contains the command-line arguments as a Unicode string.
- **nCmdShow** — a flag saying whether the main application window will be minimized, maximized or shown normally.

---

## Entry point — une seule fois
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- les deux premières formes viennent de la bibliothèque externe C, liée par défaut à votre programme
- ça peut être désactivé — mais vous n'avez alors plus les bibliothèques C ou C++, tout en pouvant encore utiliser `WinMain` (sous Windows)
- il vous faut **un** point d'entrée dans **un** de vos fichiers `.cpp`
- **une seule fois par application !**

---

# Compilation
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Program and compilation — les étapes
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

1. on prend le fichier et on passe le **préprocesseur**
2. puis vient la compilation des **templates** (le même processus)
3. puis le **compilateur** fait l'étape de compilation et assemble le code
4. c'est ensuite assemblé dans le fichier **`.obj`** (*compilation unit*)
5. les différentes unités de compilation sont **liées** ensemble pour faire l'application

---

## Mise en pratique
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- create a new file `rectangle.h`
- create a new file `rectangle.cpp`
- add the 2 file references in the `CMakeLists.txt`
- rebuild with `cmake ..`, or ask Visual Studio to do it for you

---

## Le header
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#pragma once

struct Rectangle {
    int point_x;
    int point_y;
    int delta_x;
    int delta_y;
    bool is_inside(int x, int y);
};
```

`#pragma once` is a guard — this is the same as :

```cpp
#ifndef RECTANGLE_INCLUDE_H
#define RECTANGLE_INCLUDE_H

[...]

#endif // RECTANGLE_INCLUDE_H
```

Les pragmas sont des instructions spécifiques au compilateur, mais celle-ci est implémentée dans la plupart d'entre eux (clang, gcc, CL, etc.).

---

## Le source
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include "rectangle.h"

bool Rectangle::is_inside(int x, int y) {
    if (x < point_x ||
        x > point_x + delta_x)
        return false;
    [...]
    return true;
}
```

- l'include est entre `"` parce que c'est un fichier local (dans le même répertoire que `rectangle.cpp`)
- la fonction membre s'écrit `Rectangle::is_inside` pour préciser qu'on parle de la fonction membre du struct `Rectangle`

---

## L'utilisation
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <iostream>
#include "rectangle.h"

int main(int ac, char** av) {
    Rectangle rect{ 10, 10, 20, 30 };
    if (rect.is_inside(12, 14))
        std::cout << "it's inside!\n";
    else
        std::cout << "it's outside!\n";
    return 0;
}
```

Vous pouvez inclure `rectangle.h` et l'utiliser comme s'il était déclaré juste au-dessus du `main` — c'est très exactement ce que fait l'`#include` : il **copie** le fichier à cet endroit.

---

## Ce que l'on peut inclure
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- you can include stuff you wrote yourself
- you can include stuff from the internet (almost) — c'est encore un peu trop avancé, il faut mettre en place les bindings
- you can include stuff from Windows
- **watch out for circular dependencies !**

---

# Directives de précompilation
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## La liste
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

```
#include
#define
#ifdef / #ifndef
#endif
#else
#if
#typedef
#pragma
```

---

## `#include`
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- `#include <fichier>` — recherche le fichier parmi les **fichiers ressource** (chemins système)
- `#include "fichier"` — recherche le fichier **selon le chemin indiqué** (relatif au fichier courant)

---

## `#define`
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Permet de **substituer du texte** :

- définition d'un **symbole**
- définition d'une **macro**

---

## `#ifdef` `#ifndef` `#else` `#elseif` `#endif`
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Agit comme un **guard** pour les compilations circulaires — empêche les doubles déclarations.

---

## `#ifdef` — compilation conditionnelle
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Compilation conditionnelle à certaines déclarations (le système, notamment).

---

# Fonctions et lambdas
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Function
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

A function is a set of statements that are called when you call it ; it will return where you called it when finished.

```cpp
Return-type function-name(parameters);
auto function-name(parameters) -> return-type;
```

```cpp
int power(const int val, const int mul) {
    int v = val;
    for (int i = 1; i < mul; ++i)
        v *= val;
    return v;
}

int main(int ac, char** av) {
    power(ac, 4);
    return 0;
}
```

Ceci utilise l'instruction assembleur `[call]`.

---

## Function — valeurs par défaut
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

You can pre-declare a function (in a `.h`, as we'll see later). In the pre-declaration you can specify **default values** :

```cpp
int power(const int val, const int mul = 2);
```

Watch out for what is valid or not :

> Default arguments are only allowed in the parameter lists of function declarations and lambda-expressions (since C++14), and are not allowed in the declarations of pointers to functions, references to functions, or in typedef declarations.

<small>[en.cppreference.com/w/cpp/language/default_arguments](https://en.cppreference.com/w/cpp/language/default_arguments)</small>

---

## Function pointer
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Equivalent of a function, but in a C-style function.

```cpp
int (*func)(int, int);
```

And then you can call it in your code as :

```cpp
int result = func(2, 10);
```

C'est la raison pour laquelle on peut nommer une fonction sans spécifier les paramètres : cela retourne en fait un pointeur vers la fonction.

**This is a C way of doing things — you should never use it, but it's good to know it exists.**

---

## Functor
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Equivalent of a function, but in a class structure.

```cpp
struct functor {
    int operator() (int a, int b) {
        [...]
    }
};
```

You can call it as follows :

```cpp
functor power_functor;
int result = power_functor(2, 20);
```

- ainsi vous pouvez passer une fonction à une autre fonction
- la classe porte le nom du functor — ici `functor`
- `operator()` définit ce qui se passe quand on l'appelle

C'est l'ancienne façon de faire ; la suivante montre comment on procède aujourd'hui.

---

## Lambda
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

A lambda is a functor, packaged in a nice way.

```cpp
auto power_lambda = [](int val, int mul) {
    [...]
};

int result = power_lambda(2, 20);
```

- la lambda est la nouvelle façon de rendre un appel de fonction accessible depuis n'importe où : elle remplace le pointeur de fonction **et** le functor
- c'est une fonction **anonyme** qui peut servir de paramètre
- elle peut être assignée à une variable (le type est opaque, mais on peut le nommer avec `std::function`)
- elle est plus utilisable que `std::bind`, qu'il faut éviter dès C++11

---

## Lambda — appel immédiat
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

A lambda has no type — or rather, it has its own type.

```cpp
int result = [](int val, int mul) {
    [...]
}(2, 15);
```

You get the return value directly at call time by adding the call parameters at the end.

---

## Lambda — la capture
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
[capture_list](parameters) -> return_type {
    Implementation
}
```

La **capture list** est la liste des valeurs accessibles à l'intérieur de la lambda. Par défaut c'est une copie, mais ça peut être une référence.

| Forme | Effet |
|:-:|---|
| `[]` | no capture |
| `[a]` | capture by value |
| `[&a]` | reference capture |
| `[this]` | capture the `this` pointer, used for classes |
| `[=]` | copy all values |
| `[&]` | capture all by reference |
