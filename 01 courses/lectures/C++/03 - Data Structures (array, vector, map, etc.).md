---
title: Data Structures
type: course
status: Backlog
subject: C++
duration_h: 3
bloc_gsda: Bases de la Programmation
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
manual_order: 13
---

# Data Structures
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### array, vector, list, queue, stack, map, set

<small>Module 4FSC0PF001 · Introduction to Games Programming</small>

Note:
Le fil conducteur de la séance : chaque conteneur est un compromis entre
la vitesse d'accès, le coût d'insertion et la disposition en mémoire. On
regarde à chaque fois ce que ça donne « dans la RAM », parce que c'est ce
qui explique les avantages et les inconvénients.

---

## Source
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine (contient les schémas mémoire non transposés) :

- 🔗 [Google Slides — 03 Data Structures](https://docs.google.com/presentation/d/1NZKyWCq-HW2TdavXjxJedgGmXp1gWajZIe-coXFB-AI/edit)

Exercices : [[Exercices - 03 - Data Structures]] · [[Exercices - 03 - Data Structures - array]]

</div>

---

## Stocker des valeurs
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- Enemies
- Joueurs
- Bâtiments

---

# Séquences
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## std::array
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Avantages**

- même rapidité qu'un array C
- accès aux informations de taille
- iterator pour lire directement

**Désavantages**

- impossible de changer la taille (*fixed-size*)

---

## Mémoire de l'ordinateur (stack)
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
std::array<int, 6>

begin ┌───┬───┬───┬───┬───┬───┐ end
      │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │
      └───┴───┴───┴───┴───┴───┘
```

Un bloc contigu, de taille figée à la compilation, posé sur la **stack**.

---

## std::vector
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <vector>   // nouvelle include

std::vector<int> numbers;

numbers.push_back(1);
numbers.push_back(2);
numbers.push_back(3);
numbers.push_back(4);
numbers.push_back(5);
numbers.push_back(6);

for (int n : numbers) {
    std::cout << "value = " << n << "\n";
}
```

---

## Mémoire de l'ordinateur — vector
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
std::vector<int>(10);
for (int i = 0; i < 6; i++) { numbers[i] = i + 1; }
```

```
begin ┌───┬───┬───┬───┬───┬───┬┈┈┈┈┈┈┈┈┈┈┈┈┐
      │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │            │
      └───┴───┴───┴───┴───┴───┴┈┈┈┈┈┈┈┈┈┈┈┈┘
                              end      capacity
```

Note:
La distinction `end` / `capacity` est le point important : le vector
réserve plus de place qu'il n'en utilise. C'est ce qui rend `push_back`
amorti rapide — jusqu'à la réallocation.

---

## std::vector — opérations
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Affectation**

- `push_back()`, `insert(place, content)`, `emplace()`
- `at()`, `operator[]` — mais attention à l'index utilisé

**Suppression**

- `pop_back()`
- `erase()` — remove a range
- `clear()` — remove all elements

---

## std::vector — déclarations
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
vector<char> vc;               // empty
vector<int>  v1 = {10, 20, 30};
vector<int>  v2(5);            // 5 integers (zero initialised)
vector<int>  v3(5, -1);        // 5 values at -1
vector<int>  v4(v1);           // copy of v1
```

---

## std::vector — accès indexé
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
std::vector<int> numbers = std::vector<int>(6);

numbers[0] = 1;
numbers[1] = 2;
numbers[2] = 3;
numbers[3] = 4;
numbers[4] = 5;
numbers[5] = 6;

for (int i = 0; i < numbers.size(); i++) {
    std::cout << "value[" << i << "] = " << numbers[i] << "\n";
}
```

---

## std::vector — bilan
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Avantages**

- rapide (si bien utilisé)
- accès aux informations de taille
- taille dynamique
- aligné en mémoire

**Désavantages**

- `push_back()` peut prendre beaucoup de temps
- compliqué d'ajouter / supprimer un élément au milieu

---

## std::list
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <list>   // nouvelle include

std::list<int> numbers;

auto it = numbers.begin();

numbers.insert(it, 1);
numbers.insert(it, 2);
numbers.insert(it, 3);
numbers.insert(it, 4);
numbers.insert(it, 5);
numbers.insert(it, 6);

for (auto value : numbers) {
    std::cout << "value = " << value << "\n";
}
```

---

## std::list — bilan
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Avantages**

- facile d'ajouter / supprimer des éléments
- accès aux informations de taille
- taille dynamique

**Désavantages**

- **pas aligné en mémoire**

---

## Mémoire de l'ordinateur — list
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
std::list<int>(3)

┌─────┬───┐   ┌─────┬───┐   ┌─────┬───┐
│ val │ * │──▶│ val │ * │──▶│ val │ * │──▶ …
└─────┴───┘   └─────┴───┘   └─────┴───┘
```

Chaque nœud est alloué séparément et pointe vers le suivant : on peut insérer partout, mais le parcours saute d'une adresse à l'autre.

---

## std::vector vs std::list
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**`std::vector`**

- quand le nombre d'éléments est connu / change rarement
- quand le vecteur n'a pas besoin d'être modifié

**`std::list`**

- quand les éléments sont créés / détruits souvent dans la liste
- quand on doit manipuler l'ordre (tri, inversion…)

---

# Adaptateurs
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## std::queue
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <queue>   // nouvelle include

std::queue<int> q;

q.push(1);
q.push(2);
q.push(3);
q.push(4);

for (int i = 0; i < 4; i++) {   // essayez avec q.size()
    std::cout << q.front() << "\n";
    q.pop();
}
```

Affiche : `1 2 3 4`

---

## std::queue — FIFO
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**First-in, First-out**

---

## std::queue — bilan
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Avantages**

- peut avoir des variantes (circular-queue, priority-queue, etc.)

**Désavantages**

- difficile à mettre en place
- 2 pointeurs pour les positions

---

## std::stack
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <stack>   // nouvelle include

std::stack<int> s;

s.push(1);
s.push(2);
s.push(3);
s.push(4);

for (int i = 0; i < 4; i++) {   // essayez avec s.size()
    std::cout << s.top() << "\n";   // différence avec la queue
    s.pop();
}
```

Affiche : `4 3 2 1`

---

## std::stack — LIFO
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Last-in, First-out**

---

## std::stack — bilan
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Avantages**

- facile d'implémentation
- un seul point de position

**Désavantages**

- si statique, mauvaise utilisation de la mémoire

---

## std::queue vs std::stack
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**`std::queue`**

- data buffer
- transmission de données asynchrone

**`std::stack`**

- liste de fonctions à appeler
- parsing dans les compilateurs

Note:
La diapo d'origine écrit « std::list » en tête de la seconde colonne :
c'est une coquille, les deux exemples cités (pile d'appels, parsing) sont
bien des cas d'usage de la stack.

---

# Associatifs
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## std::map
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <map>   // nouvelle include

std::map<std::string, int> m;   // Key (unique), Value

std::pair<std::string, int> p("Table", -3);
m.insert(p);                                    // insère un élément existant
m.insert(std::pair<std::string, int>("Poulet", 10));
m.emplace("Nicolas", 1);
m.insert({ "Duncan", 1 });

std::cout << m["Nicolas"] << "\n";

for (auto it = m.begin(); it != m.end(); it++) {
    // first = key, second = value
    std::cout << it->first << ", " << it->second << "\n";
}
```

Affiche, **ordonné par clé** :

```
Duncan, 1
Nicolas, 1
Poulet, 10
Table, -3
```

Note:
Le point à faire remarquer : l'ordre de sortie n'est pas l'ordre
d'insertion. La `map` est triée par clé, en permanence.

---

## std::set
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```cpp
#include <set>   // nouvelle include

std::set<std::string> s;   // Key (unique)

s.emplace("Nicolas");
s.emplace("Duncan");
s.emplace("Poulet");
s.emplace("Table");

for (auto it = s.begin(); it != s.end(); it++) {
    std::cout << *it << "\n";
}
```

Affiche :

```
Duncan
Nicolas
Poulet
Table
```

---

## std::unordered_map & std::unordered_set
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

In case you have too many elements, you'd better use `unordered_map` and `unordered_set`.

In this case, every value is stored according to its **hash** ! This is a hash map, not a map — the order of insertion won't be respected.

```cpp
std::unordered_map<std::string, int> name_value_map;

for (int i = 0; i < 40; ++i)
    name_value_map.insert({ std::to_string(i), i });

for (const auto& element : name_value_map)
    std::cout << element.first << " " << element.second << std::endl;
```
