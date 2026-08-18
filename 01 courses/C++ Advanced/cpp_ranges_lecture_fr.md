---
theme: white
css:
- _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# C++ Ranges
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Une STL moderne, en 3 heures

<small>6 modules · 10 exemples · 2 exercices · C++20 / C++23</small>

<small>Dépôt : [github.com/SAE-Geneve/CPlusPlus_Course_Ranges](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges)</small>

Note:
Bienvenue. Chaque diapositive renvoie vers un dossier exécutable du dépôt
compagnon — le nom du dossier = le titre de la diapositive.

---

## Module 1 — Pourquoi les Ranges ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>Partie 1/4 · la taxe STL · verbosité</small>

---

### La taxe STL

Une tâche courante avec la STL classique : trier des personnes, extraire
leurs noms, en retrouver une. Remarquez le *cérémonial*.

```cpp
struct Person { std::string name; int age; };
std::vector<Person> people = /* ... */;

// begin()/end() à chaque appel.
std::sort(people.begin(), people.end(),
          [](const Person& a, const Person& b){ return a.age < b.age; });

// reserve + back_inserter à la main, juste pour déplacer des données.
std::vector<std::string> names;
names.reserve(people.size());
std::transform(people.begin(), people.end(),
               std::back_inserter(names),
               [](const Person& p){ return p.name; });

// Une lambda pour le prédicat le plus trivial qui soit.
auto it = std::find_if(people.begin(), people.end(),
                       [](const Person& p){ return p.age == 25; });
```

<small>Trois opérations, et pas une seule ne tient sur une ligne.</small>

Note:
Chaque appel répète `begin()/end()`. Chaque projection ou prédicat devient
une lambda. Déplacer des données entre conteneurs demande un `reserve` et
un inserter à la main. C'est la base que nous allons améliorer.

---
### …Et cela ne vous protégera même pas

Même code que la diapositive précédente — mais chaque extrait cache un bug
que le compilateur accepte sans broncher.

```cpp
// Paire d'itérateurs venant de deux conteneurs différents — compile, UB à l'exécution.
auto it = std::find_if(people.begin(), other.end(),
                       [](const Person& p){ return p.age == 25; });

// On a écrit begin() au lieu de back_inserter — names est vide → écriture hors-bornes.
std::transform(people.begin(), people.end(), names.begin(),
               [](const Person& p){ return p.name; });

// `it` devient pendant dès que l'élément qu'il pointe est supprimé.
people.erase(it);
std::cout << it->name;
```

<small>Chacun de ces extraits compile sans erreur. C'est dans la verbosité
que se cachent les bugs.</small>

Note:
Aucun de ces cas n'est exotique. Ce sont exactement les erreurs que le
boilerplate de la diapo précédente invite — et le système de types ne les
signale jamais.

---

### 01 — Le problème des itérateurs

Les trois mêmes opérations, avec les ranges. Un seul argument par appel,
des projections au lieu de lambdas, et le bug entre conteneurs devient
impossible.

```cpp
std::ranges::sort(people, {}, &Person::age);

auto names = people | std::views::transform(&Person::name)
                    | std::ranges::to<std::vector>();

auto it = std::ranges::find(people, 25, &Person::age);
// Mélanger des conteneurs ne passe plus le typage — le bug runtime disparaît.
```

<small>📁 [`examples/01_the_iterator_problem`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/01_the_iterator_problem)</small>

Note:
Tout ce que montraient les deux dernières diapos — la verbosité *et* les
bugs silencieux — se résume à ceci. Les paires d'itérateurs étaient du
collage faiblement typé ; un range est un argument unique et type-checké.

---

### 02 — Notions de base sur le concept Range

Un **range** est simplement *« quelque chose qui a des itérateurs »* —
n'importe quoi sur quoi on peut appeler `begin()` / `end()`. Presque tous
les conteneurs standards remplissent ce critère, tout comme un tableau C.

```cpp
template <std::ranges::range R>
void show(const R& r) { for (auto&& e : r) /* ... */ ; }

std::vector<int>   v {1, 2, 3};
std::array<int, 3> a {1, 2, 3};
std::string        s {"hi"};
int                c[] {1, 2, 3};      // même un tableau C brut
std::map<int,int>  m {{1, 1}};
show(v); show(a); show(s); show(c); show(m);   // tous des ranges

// ❌ PAS des ranges : std::stack / std::queue / std::priority_queue
//    — ce sont des *adaptateurs* de conteneur : pas de begin()/end().
```

<small>S'il expose `begin()`/`end()`, tout algorithme et toute vue des
ranges l'accepte directement — sans paires d'itérateurs.</small>

<small>📁 [`examples/02_range_concept_basics`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/02_range_concept_basics)</small>

Note:
« Range = itérable » est tout le modèle mental ici. La question plus
profonde — *à quel point* ces itérateurs sont puissants — aura son propre
module plus tard (La hiérarchie des Ranges).

---

### 03 — Notions de base sur les algorithmes de Ranges

Tout classique d'`<algorithm>` a son cousin en `std::ranges::`.
Ils prennent un **range**, pas une paire d'itérateurs.

```cpp
std::vector<int> v{5, 2, 8, 1, 9, 3};

std::ranges::sort(v);
auto it       = std::ranges::find(v, 7);
auto [lo, hi] = std::ranges::minmax_element(v);
auto n        = std::ranges::count_if(v, [](int x){ return x > 5; });
```

Bonus : les types de retour sont des structs (`in`, `out`) — fini la perte
d'information sur l'endroit où l'algorithme s'est arrêté.

<small>📁 [`examples/03_range_algorithms_basics`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/03_range_algorithms_basics)</small>

Note:
Les types de retour de p. ex. `ranges::copy` renvoient à la fois la fin
de l'entrée et la fin de la sortie — utile en chaînage.

---

### 04 — Composer des pipelines avec `|`

On enchaîne les étapes ; tout le pipeline devient un unique passage fusionné.

```cpp
auto revenue = [](const Order& o){ return o.quantity * o.unit_price; };

auto top =
      orders
    | std::views::filter([](const Order& o){ return !o.cancelled; })
    | std::views::transform(revenue);

// Lisez à voix haute : « depuis orders, garder les non-annulées, calculer le revenu. »
```

L'intention se trouve dans la signature du type — pas enfouie dans une
boucle écrite à la main.

<small>📁 [`examples/04_composing_pipelines`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/04_composing_pipelines)</small>

Note:
Les pipelines sont la fonctionnalité vedette. Ils se combinent aussi très
bien avec les projections du Module 2 — les deux combattent le même
ennemi : le bruit impératif.

---

### Pourquoi `auto`, et pas le type

Le type d'un pipeline est un template profondément imbriqué généré par le
compilateur — pratiquement imprononçable, et **pas** une API stable à
écrire en dur.

```cpp
// Type réel ≈ transform_view<filter_view<ref_view<vector<Order>>>, F>
auto pipe = orders
          | std::views::filter([](const Order& o){ return !o.cancelled; })
          | std::views::transform(revenue);

// Insérez ou réordonnez une étape → le type change ; ces lignes, NON :
auto pipe2 = orders
           | std::views::filter([](const Order& o){ return !o.cancelled; })
           | std::views::take(10)              // nouvelle étape
           | std::views::transform(revenue);

for (auto value : pipe2) use(value);           // consommation inchangée
```

`auto` absorbe ce que produisent les adaptateurs : on peut faire évoluer
ou recâbler le pipeline librement — ni la déclaration de la variable, ni
la boucle qui l'itère n'ont à changer.

Note:
Le type de la vue est un détail d'implémentation de la chaîne d'adaptateurs.
L'épeler couple votre code aux étapes exactes ; `auto` (et le concept
`range` pour les paramètres) garde le site d'appel stable au fil de
l'évolution du pipeline.

---
### 05 — Projections & contraintes

Une **projection** est un callable unaire que l'algorithme applique à
chaque élément *avant* de le comparer ou de le tester.

Cas d'usage typiques :

- **Trier / chercher par un champ** — ordonner `people` par `age`, trouver
  par `id`, sans comparateur écrit à la main.
- **Comparer par une clé dérivée** — tri insensible à la casse, plus
  proche de zéro, plus récent d'abord : projeter via `toupper` / `abs` /
  un horodatage.
- **Atteindre à travers une indirection** — trier un
  `vector<unique_ptr<T>>` ou `vector<T*>` par le pointé, pas par la
  valeur du pointeur.

---

La signature est toujours `(range, valeur-ou-comparateur, projection)`.
`{}` veut dire « utiliser la valeur par défaut » (`std::less` / identité).
Un pointeur sur membre est la projection idiomatique.

```cpp
struct Person { int id; std::string name; };
std::vector<Person> people = /* ... */;

// 1 · Par un champ — pointeur sur membre, sans comparateur.
std::ranges::sort(people, {}, &Person::name);
auto p = std::ranges::find(people, 42, &Person::id);

// 2 · Par une clé dérivée — la projection peut être n'importe quel callable.
std::ranges::sort(words, {}, [](auto& s){ return std::tolower(s[0]); });
auto z = std::ranges::min(xs, {}, [](int x){ return std::abs(x); });

// 3 · À travers une indirection — ordonner par le pointé, pas par le pointeur.
std::vector<std::unique_ptr<Person>> ptrs = /* ... */;
std::ranges::sort(ptrs, {}, [](auto& up){ return up->id; });
```

À comparer au boilerplate équivalent en STL classique.

<small>📁 [`examples/05_projections_and_constraints`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/05_projections_and_constraints)</small>

Note:
Sans projections, on écrirait une lambda comparateur pour chaque
« trier/chercher par champ ». La projection garde l'algorithme générique
et le site d'appel déclaratif — un seul concept remplace une pile de
lambdas.

---
### 06 — Vues & "lazy evaluation"

Une **vue** est un range "lazy" et non propriétaire.
La construire est en O(1). Le travail se fait pendant l'itération — et
*uniquement* pour les éléments que vous consommez réellement.

```cpp
std::vector<int> big(1'000'000);   // un million d'éléments

// EAGER : alloue un vector d'un million d'éléments et effectue 1 000 000
// multiplications — puis jette tout sauf les 3 premiers.
std::vector<int> sq;
std::transform(big.begin(), big.end(), std::back_inserter(sq),
               [](int x){ return x * x; });
auto first3 = std::vector(sq.begin(), sq.begin() + 3);

// LAZY : aucune allocation, aucun travail, jusqu'à ce que la boucle tire 3 éléments.
auto v = big | std::views::transform([](int x){ return x * x; })
             | std::views::take(3);
for (int x : v) use(x);            // exactement 3 multiplications, 0 temporaire
```
---
Le coût paresseux est proportionnel à ce que l'on **consomme**, pas à ce
que l'on **a** — ce qui explique aussi pourquoi un range infini fonctionne :

```cpp
for (int x : std::views::iota(0) | std::views::take(5))  // ne bloque jamais
    std::cout << x << ' ';
```

<small>Vues clés : `iota`, `filter`, `transform`, `take`, `drop`, `reverse`.</small>

<small>📁 [`examples/06_views_lazy_evaluation`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/06_views_lazy_evaluation)</small>

Note:
Le bénéfice est concret : même résultat, mais la version eager a fait
~1M multiplications plus une allocation tas, alors que la paresseuse en a
fait 3 et aucune. Une vue est une *recette*, pas un résultat — les ranges
infinis ne « fonctionnent » que parce que rien n'est calculé à l'avance.

---

### `transform` : vue ou algorithme ?

`transform` désigne **deux outils différents** — facile d'appeler le mauvais.

```cpp
std::vector<int> v{1, 2, 3};

// views::transform — VUE paresseuse. Ne touche PAS v. Recalculée à chaque accès.
auto doubled = v | std::views::transform([](int x){ return x*2; });
//   lire doubled → 2 4 6        v vaut toujours {1, 2, 3}

// ranges::transform — ALGORITHME eager. Écrit dans une destination, une fois.
std::ranges::transform(v, v.begin(), [](int x){ return x*2; }); // v → 2 4 6
```

| | `std::views::transform` | `std::ranges::transform` |
|---|---|---|
| Nature | adaptateur de vue paresseux | algorithme eager |
| Mute l'entrée | non | seulement si la dest **est** l'entrée |
| Sortie stockée | aucune — recalculée à chaque passage | oui — dans la dest fournie |

Note:
La vue ne modifie jamais la source et ne met rien en cache — une boucle
en 3 passes appelle la fonction 3× par élément. Pour changer les données,
soit on matérialise la vue, soit on utilise la forme algorithme.

---

## Durées de vie & patterns
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

---

### 07 — Owned views

Les vues sont en général **non propriétaires** — elles ne font qu'emprunter
leurs éléments. Le piège n°1, c'est le dangling.

```cpp
// make_data() construit un vector et le retourne PAR VALEUR (un temporaire).
std::vector<int> make_data() {
    return {1, 2, 3, 4, 5};
}

// ❌ Lier à une VARIABLE LOCALE NOMMÉE puis la vuer. La vue est non propriétaire, donc elle pend dès que `data` sort de portée.
auto bad() {
    std::vector<int> data = make_data();
    return data | std::views::transform([](int x){ return x*2; });
}                          // `data` détruite → la vue retournée pend

// ✅ Piper directement la RVALUE : elle est DÉPLACÉE dans un std::ranges::owning_view qui détient le vector tant que
//    l'objet pipeline existe — sûr à retourner.
auto good() {
    return make_data()
         | std::views::transform([](int x){ return x*2; });
}
```

Règle simple : piper une **lvalue** → la vue *s'y réfère* (vous gérez la
durée de vie) ; piper une **rvalue** → un `owning_view` l'*adopte* (sûr).

<small>📁 [`examples/07_owning_views`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/07_owning_views)</small>

Note:
Les deux fonctions utilisent le *même* `make_data()` — la seule différence
est lvalue vs rvalue. Une variable locale nommée est seulement référencée
(pend) ; le temporaire est adopté par `owning_view` (sûr). C'est toute la
règle.

---

### 08 — Borrowed range

Un **borrowed range** est un range dont les itérateurs restent valides
*même après la disparition de l'expression range elle-même* — parce qu'il
n'a jamais possédé ses éléments ; il ne fait que référer à du stockage
détenu ailleurs.

```cpp
static_assert( std::ranges::borrowed_range<std::string_view>); // réfère
static_assert( std::ranges::borrowed_range<std::span<int>>);   // réfère
static_assert(!std::ranges::borrowed_range<std::string>);      // possède
```

Pourquoi ça compte — l'algorithme vous protège à la **compilation** :

```cpp
auto it = std::ranges::find(std::vector{1,2,3}, 2);
// decltype(it) == std::ranges::dangling — le déréférencer ne compile pas.
```

<small>Un conteneur lvalue est emprunté (il survit à l'appel) ; un
temporaire ne l'est pas. Inscrivez votre propre type via
`std::ranges::enable_borrowed_range`.</small>

<small>📁 [`examples/08_borrowing_views`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/08_borrowing_views)</small>

Note:
« Emprunté » = la validité de l'itérateur n'est pas liée à la durée de vie
de l'objet range. `find` sur un temporaire renvoie `dangling` au lieu
d'un itérateur — le piège de la diapo précédente, attrapé par le système
de types.

---

### 09 — `std::ranges::to`

La pièce manquante : retransformer une vue en conteneur.

```cpp
auto squares = std::views::iota(1, 11)
             | std::views::filter([](int x){ return x % 2 == 0; })
             | std::views::transform([](int x){ return x*x; })
             | std::ranges::to<std::vector<int>>();
```

Fonctionne avec **n'importe quel** conteneur — `vector`, `set`, `map`, le vôtre.

<small>📁 [`examples/09_ranges_to`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/09_ranges_to)</small>

---

## Module 5 — La hiérarchie des Ranges
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

---

### La hiérarchie des Ranges

Le standard classe les ranges en **cinq niveaux** selon la puissance de
leur itérateur. Chaque niveau *raffine* le précédent — c'est un
**sur-ensemble** strict : il garde toutes les garanties et ajoute une capacité.

| Range / vue | Niveau le plus faible satisfait |
|---|---|
| vue `istream`, un générateur | `input_range` |
| `forward_list`, `unordered_set` | `forward_range` |
| `list`, `set`, `map` | `bidirectional_range` |
| `deque` | `random_access_range` |
| `vector`, `array`, `string`, `span` | `contiguous_range` |

<small>`sized_range` est **orthogonal** — pas un niveau. Il garantit
seulement que `std::ranges::size(r)` est en O(1), et peut être vrai (ou
pas) à n'importe quel niveau.</small>

Note:
La même échelle que les anciennes catégories d'itérateurs codaient, mais
remontée au niveau range et transformée en concept vérifiable plutôt
qu'en tag à connaître par cœur. Les diapos suivantes prennent un niveau
chacune.

---

### Niveau 1 — `input_range`

Lire chaque élément **une seule fois**, en avançant uniquement. Avancer
consomme la position — pas de retour en arrière, pas de second passage.

```cpp
// Tokens depuis std::cin — on ne rembobine pas un clavier.
auto in = std::views::istream<int>(std::cin);

for (int x : in) use(x);   // chaque valeur vue exactement une fois
// Itérer `in` à nouveau ne rejouerait PAS les mêmes valeurs.
```

<small>Modèles : `std::ranges::istream_view`, générateurs coroutines,
tout flux produit paresseusement.</small>

Note:
C'est le niveau le plus faible et le plus permissif — les algorithmes qui
n'ont besoin que de toucher chaque élément une fois (p. ex. `for_each`,
`copy`) l'acceptent.

---

### Niveau 2 — `forward_range`

Ajoute le **multi-passage** : sauvegarder un itérateur, parcourir, puis
recommencer et retrouver les mêmes éléments.

```cpp
std::forward_list<int> fl{1, 2, 3};

std::ranges::for_each(fl, pass1);   // premier parcours
std::ranges::for_each(fl, pass2);   // à nouveau — éléments identiques
```

<small>Modèles : `std::forward_list`, `std::unordered_set` / `unordered_map`.
Une liste chaînée simple : on peut repartir de la tête, mais avancer seulement.</small>

Note:
Premier niveau où les algorithmes en deux passes (compter puis traiter)
sont valides.

---

### Niveau 3 — `bidirectional_range`

Tout ce que donne `forward`, **plus `--it`** — on peut aussi marcher en
arrière.

```cpp
std::list<int> l{1, 2, 3};

for (int x : l | std::views::reverse)   // nécessite l'itération en arrière
    std::cout << x;                     // 3 2 1
```

<small>Modèles : `std::list` (doublement chaînée), `std::set`, `std::map`
(arbres). On peut aller à gauche ou à droite — mais atteindre le N-ième
élément demande encore N pas.</small>

Note:
`std::views::reverse` est l'exemple canonique qui *exige* ce niveau.

---

### Niveau 4 — `random_access_range`

Arithmétique d'itérateurs : `it + n`, `it - it2`, `it[n]`, ordre.
Atteindre **n'importe quel** élément est en O(1).

```cpp
auto r = std::views::iota(0, 10);      // 0,1,…,9 — aucun conteneur requis

int x   = r[5];                        // 5 — O(1), sans avancer pas à pas
auto mid = r.begin() + r.size() / 2;   // arithmétique d'itérateur
```

<small>`iota_view` est random-access mais **pas** contigu (pas de tableau
sous-jacent).
C'est pour ça que `std::ranges::sort(std::list{...})` ne compile pas.</small>

Note:
Recherche binaire, `nth_element`, `sort` — tous conditionnés à ce niveau.

---

### Niveau 5 — `contiguous_range`

Le plus fort : les éléments se suivent **consécutivement en mémoire**,
donc `&r[0] + n == &r[n]` et un brut `T*` est un itérateur valide.

```cpp
std::vector<int> v{1, 2, 3, 4};

int* p = std::ranges::data(v);          // un vrai pointeur valide
std::fwrite(p, sizeof(int), v.size(), f); // passé directement à une API C
```

<small>Modèles : `std::vector`, `std::array`, `std::string`, `std::span`.
`std::deque` ne **qualifie pas** — son stockage est par chunks, pas un
seul bloc.</small>

Note:
Le niveau qui permet l'interop avec C, `memcpy` et le SIMD.

---

### Gravir les niveaux — un exemple

Une fonction se contraint au **niveau le plus faible dont elle a
réellement besoin**. Cette contrainte *est* le contrat à la compilation.

```cpp
template <std::ranges::random_access_range R>
auto middle(const R& r) {
    return *(std::ranges::begin(r) + std::ranges::size(r) / 2);
}

middle(std::vector{1,2,3,4});   // ✅ contigu  ⊇ random_access
middle(std::deque{1,2,3,4});    // ✅ exactement random_access
middle(std::list{1,2,3,4});     // ❌ seulement bidirectionnel — ne compile pas
middle(std::views::istream<int>(std::cin)); // ❌ seulement input — ne compile pas
```

<small>Passer un range **plus fort** là où un niveau plus faible est
demandé → OK (sur-ensemble). Passer un **plus faible** → le concept le
rejette, à la compilation, avec l'exigence nommée dans la signature.</small>

Note:
Même principe derrière `sort` qui exige `random_access_range`. Le concept
dans la signature à la fois documente et impose l'exigence — la
convention non écrite « il faut un itérateur random-access » est
maintenant vérifiée.

---

## Module 6 — C++23 & au-delà
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

---

### 10 — `enumerate`, `zip`, `chunk`, `slide`, `cartesian_product`

C++23 comble les manques laissés par C++20.

```cpp
// enumerate → [index, valeur] ; démo complète dans l'Exercice 2 (leaderboard).
for (auto [i, x] : std::views::enumerate(r)) rank(i + 1, x);

for (auto [name, age] : std::views::zip(names, ages))
    std::cout << name << " a " << age << '\n';

// Fenêtre glissante de 3.
for (auto w : std::views::iota(1,7) | std::views::slide(3)) { /* ... */ }

// Toutes les paires (x, y).
for (auto [x, y] : std::views::cartesian_product(xs, ys)) { /* ... */ }
```

<small>Nécessite MSVC 19.34+ / GCC 14+ / Clang 17+.</small>

<small>📁 [`examples/10_cpp23_enumerate_zip_chunk`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/10_cpp23_enumerate_zip_chunk)</small>

Note:
`enumerate` enterre enfin le pattern du compteur manuel `i++`.
`zip` retire `std::transform` à deux itérateurs.

---

## Exercices
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

---

### Exercice 1 — Refactorer une boucle classique

Réécrivez cette boucle impérative en **pipeline de ranges**.

```cpp
struct Student { std::string name; int grade; bool passed; };

// Moyenne des notes des étudiants ayant réussi.
double avg(const std::vector<Student>& s) {
    int sum = 0, count = 0;
    for (const auto& st : s) {
        if (st.passed) { sum += st.grade; ++count; }
    }
    return count ? double(sum) / count : 0;
}
```

**Votre tâche :**

1. Construire une vue qui `filter`e les étudiants ayant **réussi**, puis
   `transform`e chacun en sa **note**.
2. Utiliser des **projections pointeur sur membre** (`&Student::passed`,
   `&Student::grade`) — pas de lambdas écrites à la main.
3. Calculer la moyenne depuis ce range (C++23 `std::ranges::fold_left`,
   ou matérialiser avec `std::ranges::to<std::vector>()` puis accumuler).
4. Garder correct le cas d'entrée vide — retourner `0`, jamais diviser
   par zéro.

<small>Objectif : le corps doit se lire comme sa spécification — *« moyenne
des notes des reçus »* — sans compteurs manuels ni `if`.</small>

Note:
Solution de référence :
`auto passing = s | std::views::filter(&Student::passed)
                  | std::views::transform(&Student::grade);`
C++23 : `int n = std::ranges::distance(passing);` puis
`return n ? double(std::ranges::fold_left(passing, 0, std::plus{})) / n : 0;`
Pré-C++23 : matérialiser `passing` avec `std::ranges::to<std::vector>()`,
puis `std::accumulate`. Objection classique : « mais ma boucle va très
bien » — montrer les taux de bugs sur un vrai codebase.

---

### Exercice 1 — Solution

La boucle se réduit à un pipeline **filter → transform** ; la moyenne est
un simple fold dessus.

```cpp
double avg(const std::vector<Student>& s) {
    auto passing = s | std::views::filter(&Student::passed)
                     | std::views::transform(&Student::grade);

    const auto n = std::ranges::distance(passing);
    if (n == 0) return 0;                       // garde-fou entrée vide

    return double(std::ranges::fold_left(passing, 0, std::plus{})) / n;
}
```

<small>Pré-C++23 — sans `fold_left` : matérialiser puis `accumulate`.</small>

```cpp
auto v = passing | std::ranges::to<std::vector>();
return v.empty() ? 0
                 : double(std::accumulate(v.begin(), v.end(), 0)) / v.size();
```

Note:
Le corps se lit maintenant comme sa spec. `filter`/`transform` sont
paresseux, donc la voie C++23 ne matérialise rien — `fold_left` consomme
la vue directement. Bémol : `distance` parcourt `passing` une fois et le
fold le parcourt à nouveau (deux passes) ; OK ici, mais pour un seul
passage, fold en comptant en même temps.

---

### Exercice 2 — Leaderboard des 3 meilleurs followers

Affichez un classement de vos **3 meilleurs followers** par score.

```cpp
struct Player { int id; std::string name; int score; bool is_follower; };
std::vector<Player> players = /* ... */;

// Classique : copier les followers, trier par score décroissant, afficher 3 avec un rang.
std::vector<Player> f;
for (const auto& p : players)
    if (p.is_follower) f.push_back(p);
std::sort(f.begin(), f.end(),
          [](const Player& a, const Player& b){ return a.score > b.score; });
for (std::size_t i = 0; i < f.size() && i < 3; ++i)
    std::cout << (i + 1) << ". " << f[i].name << " — " << f[i].score << '\n';
```

**Votre tâche :**

1. `filter` les joueurs où `is_follower`, puis **matérialiser**
   (`std::ranges::to<std::vector>()`) — le tri demande un vrai conteneur.
2. `std::ranges::sort` par `score` **décroissant** via la projection
   `&Player::score` + `std::ranges::greater{}` — pas de lambda comparateur.
3. Afficher les 3 premiers avec leur **rang** : `take(3)` pipé dans
   `std::views::enumerate`, ainsi l'index *est* la position.

<small>Pourquoi matérialiser ? `sort` exige un `random_access_range` et
mute en place — une vue `filter` paresseuse ne peut pas être triée
directement.</small>

Note:
Mélange volontaire d'une vue (`filter`) avec un algorithme (`sort`) — le
point pédagogique « vue vs algorithme » / hiérarchie. `enumerate`
transforme le compteur manuel `i++` en rang gratuitement.

---

### Exercice 2 — Solution

```cpp
void leaderboard(const std::vector<Player>& players) {
    auto top = players | std::views::filter(&Player::is_follower)
                        | std::ranges::to<std::vector>();      // triable

    std::ranges::sort(top, std::ranges::greater{}, &Player::score);

    for (auto [i, p] : top | std::views::take(3)
                           | std::views::enumerate)
        std::cout << (i + 1) << ". " << p.name
                  << " — " << p.score << '\n';
}
```

<small>`std::ranges::greater{}` + `&Player::score` = « par score, du plus
élevé au plus bas » sans comparateur. `enumerate` produit `[index, valeur]` ;
`i + 1` est le rang à partir de 1.</small>

Note:
`filter` est paresseux ; `ranges::to` matérialise seulement les followers
(pas tous les joueurs) pour que `sort` reçoive un conteneur contigu.
`take(3)` plafonne la sortie ; `enumerate` fournit le rang. Pré-C++23 :
remplacer `enumerate` par un `zip` avec `std::views::iota(1)`, ou garder
un compteur manuel.

---

## Conclusion
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Quand sortir les ranges

- **Algorithme + conteneur** → `std::ranges::xxx` (toujours)
- **Transformation multi-étape** → vues + `|`
- **Parcours par index/paires** → `enumerate` / `zip`
- **Boucle interne chaude avec du vrai travail** → mesurer ; les ranges
  gagnent en général

### Quand y réfléchir à deux fois

- Besoin de muter les éléments à travers une vue complexe → peut ne pas
  compiler, par design
- Durées de vie — ne jamais retourner une vue sur une variable locale
- Toolchains anciennes — vérifier les macros de test de fonctionnalité
  `__cpp_lib_ranges*`

---

## Ressources
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- 📘 [cppreference : bibliothèque Ranges](https://en.cppreference.com/w/cpp/ranges)
- 📘 [Eric Niebler — range-v3](https://github.com/ericniebler/range-v3) (le prototype)
- 📺 Tristan Brindle — « An Overview of Standard Ranges » (CppCon)
- 📺 Hannes Hauswedell — « From Iterators to Ranges »
- 💻 Ce dépôt : [github.com/SAE-Geneve/CPlusPlus_Course_Ranges](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges)

---

# Questions ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>Code : [github.com/SAE-Geneve/CPlusPlus_Course_Ranges](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges)</small>
