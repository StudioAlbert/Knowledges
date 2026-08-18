---
title: Deeper dive into STD 1/2 — file I/O, stringstream
type: course
duration_h: 3
bloc: "[[Structures de Données et STL]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Deeper dive into STD
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### 1 / 2 — file I/O, stringstream, algorithms

<small>Module 4FSC0PF001 · Introduction to Games Programming</small>

Note:
Deux thèmes dans cette première partie : lire et écrire des fichiers —
donc la persistance, les sauvegardes, les settings — puis l'entrée dans
la bibliothèque `<algorithm>`, qui remplace la plupart des boucles que
vous écrivez à la main.

---

## Source
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine (contient les schémas non transposés) :

- 🔗 [Google Slides — 07 Deeper dive into STD 1/2](https://docs.google.com/presentation/d/1Xttry7t9F_i_Q4NBECm4Q3ewRQGu437fiCZBex5Ad2w/edit)

Suite : [[07 - Deeper dive into STD 2-2 - Algorithms]] · Exercices : [[Exercices - 07b - Deeper dive into STD - File IO]] · [[Exercices - 07a - Deeper dive into STD - algorithms]]

</div>

---

# File I/O
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Pourquoi écrire dans un fichier externe ?
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- système de sauvegarde
- settings
- ressources (modèles 3D, image, son, shader, material, etc.)

---

## Ouvrir un fichier
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <iostream>
#include <fstream>   // new include
#include <string>    // new include

int main()
{
    std::ifstream inFile;

    inFile.open("test.txt");
}
```

---

## Ouvrir un fichier ⇒ toujours fermer
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream inFile;
    inFile.open("test.txt");
    inFile.close();
}
```

---

## Lire en mode stream
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream inFile;
    std::string line;
    inFile.open("test.txt");
    while (inFile >> line) {
        std::cout << line << "\n";
    }
    inFile.close();
}
```

---

## Lire en mode string
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream inFile;
    inFile.open("test.txt");
    for (std::string line; getline(inFile, line); ) {
        std::cout << line << "\n";
    }
    inFile.close();
}
```

Note:
Différence avec la diapo précédente : `>>` découpe sur les espaces,
`getline` découpe sur les retours à la ligne. C'est presque toujours
`getline` que vous voudrez.

---

## Restart from file start
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
std::ifstream inFile;

inFile.open("test.txt");

for (std::string line; getline(inFile, line); )
{
    std::cout << line << "\n";
}

inFile.clear();
inFile.seekg(0);

// read file again

inFile.close();
```

Note:
`clear()` avant `seekg(0)` : arrivé en fin de fichier, le flux est en
état d'erreur (eof), et tant qu'on ne l'a pas remis à zéro, le
repositionnement ne sert à rien.

---

## Écrire en mode stream
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
int main()
{
    std::ofstream outFile;

    outFile.open("test.txt");

    outFile << "Salut c'est un test\nCoucou";

    outFile.close();
}
```

---

## Écrire — write()
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
int main()
{
    std::ofstream outFile;

    outFile.open("test.txt");

    char s[] = "Ceci est un test\n";

    outFile.write(s, 18);

    outFile.close();
}
```

---

## stringstream !
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::ostringstream out_string{};
    out_string << "hello ";
    std::string name;
    std::cin >> name;
    out_string << name;
    out_string << "!\n";
    std::cout << out_string.str();
    return 0;
}
```

You can have :

- `ostringstream` → output string stream
- `istringstream` → input string stream
- `stringstream` → input / output string stream

---

## XML vs JSON
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- **XML** (Extensible Markup Language) is a pretty big standard.
- **JSON** (JavaScript Object Notation) is pretty simple and easier to read.

---

## JSON — exemple
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 25,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    { "type": "home",   "number": "212 555-1234" },
    { "type": "office", "number": "646 555-4567" },
    { "type": "mobile", "number": "123 456-7890" }
  ],
  "children": [],
  "spouse": null
}
```

---

## Schema
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- les schémas sont un moyen de vérifier le contenu de votre XML / JSON
- ils **valident** votre XML / JSON
- ils vérifient les données que vous faites circuler
- vous pouvez utiliser JSON pour stocker des données
- vous pouvez utiliser JSON pour communiquer avec des serveurs (on parle de communication **REST**)

---

## Pause
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Question time !

Vous pouvez aussi jouer avec VS2019 — ou faire une pause, au cas où votre cerveau serait en train de fondre…

---

# Algorithm
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Algorithm — pourquoi
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

La bibliothèque `<algorithm>` permet d'éviter :

- les **border issues** (où s'arrête la boucle ?)
- les **empty loops** (que se passe-t-il s'il n'y a rien dedans ?)

Elle est utilisée par **énormément** de monde.

C'est bien plus que `for_each` : il y a **105 algorithmes** en C++17.

---

## Algorithm — la bibliothèque
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

> The algorithms library defines functions for a variety of purposes (searching, sorting, counting, manipulating) that operate on ranges of elements.

Depuis C++20, certaines fonctions ont été redéfinies pour utiliser les **ranges** et n'ont plus besoin qu'on leur passe `begin` et `end`.

```cpp
#include <vector>
#include <iostream>
#include <algorithm>

int main()
{
    std::vector<int> v = {12, 2, 32, 1};
    std::sort(v.begin(), v.end());
    std::for_each(
        v.begin(),
        v.end(),
        [](auto item)
        {
            std::cout << item << "\n";
        });
    return 0;
}
```

<small>[en.cppreference.com/w/cpp/algorithm](https://en.cppreference.com/w/cpp/algorithm)</small>

---

## Algorithm — les ranges (C++20)
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    std::vector<int> v = {12, 2, 32, 1};
    std::ranges::sort(v);
    std::ranges::for_each(v, [](auto item)
        {
            std::cout << item << "\n";
        });
    return 0;
}
```

Pour tester sur [godbolt.org](https://godbolt.org), ajoutez `-std=c++20` à la ligne de commande. Dans Visual Studio, ajoutez au `CMakeLists.txt` :

```cmake
if(WIN32)
    add_compile_options("/std:c++latest")
endif(WIN32)
```

---

## Algorithm — execution policy (C++17)
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

L'execution policy peut optimiser votre code pour le rendre multithread ou vectorisé. Très utile si vous voulez que ça aille plus vite — **mais attention aux valeurs partagées !**

```
std::execution::par
std::execution::seq
std::execution::parallel_unsequenced_policy
std::execution::unsequenced_policy
```

```cpp
#include <vector>
#include <iostream>
#include <algorithm>
#include <execution>

int main() {
    std::vector<int> v = { 12, 2, 32, 1 };
    std::ranges::sort(v);
    std::for_each(
        std::execution::par,
        v.begin(),
        v.end(),
        [](auto& item) { item++; });
    std::ranges::for_each(v, [](auto item) {
        std::cout << item << "\n";
    });
    return 0;
}
```

---

## Algorithm — les familles
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- the **queries**
- the **permutations**
- the algos on **sets**
- the **movers**
- the **value modifiers**
- the **structure changers**
- and the algos of **raw memory**

<small>[Wallpaper — the world of C++ STL algorithms](https://www.reddit.com/r/cpp/comments/8faq2p/wallpaper_the_world_of_c_stl_algorithms_1800_x/)</small>

---

# Itérateurs et intervalles
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Notion d'itérateur
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Un **itérateur** est un objet qui pointe l'élément d'un container.

Pour un `vector<int> myVector` :

| Expression | Désigne |
|---|---|
| `myVector.begin()` | le 1ᵉʳ élément |
| `myVector.end()` | l'élément « après » le dernier élément |
| `vector<int>::iterator it` | un pointeur sur un élément |

---

## Déplacer un itérateur
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Avec les opérateurs d'addition : `++` (incrémentation), `--` (décrémentation), `+ 3`.

```cpp
it++;                    // permet d'avancer d'un élément
it = begin() + 6;        // saut direct
```

---

## Notion d'intervalle
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Deux itérateurs définissent un intervalle **`[it1, it2)`** — borne de gauche incluse, borne de droite exclue.

- `[myVector.begin(), myVector.end())` — intervalle complet
- `[it1, it2)` — intervalle partiel

---

## Fonction unaire, prédicat
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- **Fonction unaire** : fonction à un seul paramètre
- **Prédicat** : fonction retournant un booléen

Plusieurs formes :

```cpp
// Fonction standard
bool isTrue(auto element);

// Expression lambda
[ageLimit](Person& p) -> bool { return p.getAge() <= ageLimit; }

// Objet fonction : classe avec surcharge de operator()
```

---

# Les algorithmes, un par un
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## copy
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
copy(InputIterator first, InputIterator last, OutputIterator result);
```

Copie l'intervalle `[first, last)` à partir de `result`.

---

## count, count_if
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
Typename count(InputIterator first, InputIterator last, const T& val);

Typename count_if(InputIterator first, InputIterator last, UnaryPredicate pred);
```

| Paramètre | Rôle |
|---|---|
| `[first, last)` | intervalle de comptage |
| `val` | valeur à vérifier |
| `pred` | condition à vérifier, sous forme de prédicat |

**Résultat** = nombre d'itérations satisfaisant la condition.

---

## find, find_if
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
InputIterator find(InputIterator first, InputIterator last, const T& val);

InputIterator find_if(InputIterator first, InputIterator last, UnaryPredicate pred);
```

| Paramètre | Rôle |
|---|---|
| `[first, last)` | intervalle de recherche |
| `val` | valeur à chercher |
| `pred` | condition à vérifier, sous forme de prédicat |

**Résultat** = itérateur sur le 1ᵉʳ élément trouvé.

---

## remove, remove_if
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
ForwardIterator remove(ForwardIterator first, ForwardIterator last, const T& val);

ForwardIterator remove_if(ForwardIterator first, ForwardIterator last, UnaryPredicate pred);
```

| Paramètre | Rôle |
|---|---|
| `[first, last)` | intervalle |
| `val` | valeur à chercher |
| `pred` | condition de suppression, sous forme de prédicat |

**Résultat** = itérateur à la fin du nouveau dataset.

---

## erase, erase_if
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**DON'T FORGET ERASE OPERATION**

```cpp
iterator erase(iterator first, iterator last);
```

L'algorithme `remove` ou `remove_if` **ne supprime pas** les éléments : il les déplace et les laisse dans un état indéfini.

Note:
C'est le fameux *erase–remove idiom*. `remove` seul laisse le conteneur
de la même taille, avec de la queue indéfinie ; c'est `erase` qui coupe.
L'oublier est l'erreur la plus fréquente sur cette bibliothèque.

---

## sort, shuffle
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
void sort(RandomAccessIterator first, RandomAccessIterator last, Compare comp);

void shuffle(RandomAccessIterator first, RandomAccessIterator last, URNG&& g);
```

| Paramètre | Rôle |
|---|---|
| `[first, last)` | intervalle |
| `comp` | fonction binaire permettant la comparaison entre 2 éléments |
| `g` | uniform random number generator |

---

## Les queries
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `std::count` → count the elements
- `std::find` → find an element in a collection
- `std::max_element` → return the max
- `std::min_element` → return the min
- `std::minmax_element` → do both
- `std::search` → search for a subset of elements (des items, dans l'ordre, dans un ensemble)
- `std::is_permutation` → is it a permutation ? (même contenu, ordre différent)

```cpp
#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    std::vector<int> v1 = { 12, 2, 32, 1 };
    std::vector<int> v2 = { 2, 32 };
    auto it = std::search(v1.begin(), v1.end(),
                          v2.begin(), v2.end());
    if (it == v1.end())
        std::cout << "not found.";
    else
        std::cout << "found!";
    return 0;
}
```

---

## Les permutations
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `std::sort` → sort a collection. Vous pouvez spécifier un comparateur ; par défaut c'est `<=`
- `std::shuffle` → shuffle a collection. Très utile pour mélanger
- `std::reverse` → reverse the order of a collection
- `std::rotate` → rotate a collection : met l'élément indiqué en premier et repousse à la fin tous ceux qui le précédaient

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main () {
    std::vector<int> v = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    std::rotate(v.begin(), v.begin() + 3, v.end());
    for (const auto& item : v)
        std::cout << ' ' << item;
    return 0;
}
// >> 3 4 5 6 7 8 9 0 1 2
```

---

## Les algos sur les sets
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `std::set_union` → make a merge between 2 sets
- `std::set_intersection` → return the intersection
- `std::set_difference` → return the difference

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v1{ 1, 2, 3, 4, 5, 6, 7, 8 };
    std::vector<int> v2{ 5, 7, 9, 10 };
    std::sort(v1.begin(), v1.end());
    std::sort(v2.begin(), v2.end());
    std::vector<int> v_intersection;
    std::set_intersection(
        v1.begin(), v1.end(),
        v2.begin(), v2.end(),
        std::back_inserter(v_intersection));
    for (int n : v_intersection)
        std::cout << n << ' ';
}
```

Note:
Les deux `sort` ne sont pas décoratifs : tous les algorithmes de la
famille `set_*` exigent des intervalles **déjà triés**.

---

## Les movers
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `std::copy` → copy from a collection to another. Remplace `memcpy` et les autres fonctions C, désormais inutiles
- `std::move` → this moves it. Retire le nom d'une variable et rend son contenu disponible pour la nouvelle. Façon **très** efficace de déplacer de la mémoire

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v1{ 1, 2, 3, 4, 5, 6, 7, 8 };
    std::vector<int> v2;
    std::copy(
        v1.begin(),
        v1.begin() + 3,
        std::back_inserter(v2));
    for (const auto& item : v2)
        std::cout << item << ' ';
    return 0;
}
```

---

## Les value modifiers — remplir
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `std::fill` → fill a collection with a value. Très utile par exemple pour remplir un vector qui est une texture, avec une couleur
- `std::iota` → fill with incrementing values. Prend le début, la fin, et la valeur de départ
- `std::generate` → same, but with a generator, rappelé pour chaque élément

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v{ 0, 1, 2, 3, 4, 5, 6 };
    std::generate(v.begin(), v.end(), []
        {
            static int i = 0;
            i += 3;
            return i;
        });
    for (const auto& item : v)
        std::cout << item << ' ';
    return 0;
}
```

---

## Les value modifiers — supprimer
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `std::unique` → remove all except the first. Équivalent d'une copie vers un `set`, mais en place. **Il faut trier d'abord !**
- `std::remove` → remove all matching elements. Prend l'élément à retirer

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> v{ 0, 1, 2, 1, 4, 2, 6 };
    std::sort(v.begin(), v.end());
    auto last = std::unique(v.begin(), v.end());
    v.erase(last, v.end());
    for (const auto& item : v)
        std::cout << item << ' ';
    return 0;
}
```

---

## Les algos sur la mémoire brute
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `std::uninitialized_fill` → s'utilise sur de la mémoire non initialisée, pour y assigner une valeur
- `std::uninitialized_copy` → idem, mais appelle le constructeur de copie
- `std::destroy` → idem, mais appelle le destructeur

---

## Et les autres
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `std::for_each` → apply a function to a collection
- `std::transform` → same, but outputs a collection

```cpp
#include <algorithm>
#include <iostream>
#include <string>

int main() {
    std::string s("hello world!");
    std::transform(
        s.begin(),
        s.end(),
        s.begin(),
        [](const auto c)
        {
            return std::toupper(c);
        });
    std::cout << s;
    return 0;
}
```

---

## Questions ?
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->
