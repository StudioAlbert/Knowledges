---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# C++ Builder
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Construire des objets complexes, lisiblement, en 1 heure

<small>6 modules · 6 exemples · 1 exercice · C++17/20</small>

<small>Dépôt : [github.com/StudioAlbert/cpp_builder_pattern_course_companion](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion)</small>

Note:
Objectif de cette heure : remplacer un constructeur qui enfle au fil des
champs par un point de construction lisible, sûr et validé. On suit une
classe `Person` tout du long, et on termine sur un exercice « Sandwich
shop » que vous refactorez vous-mêmes. Chaque diapo de code renvoie à un
dossier exécutable du dépôt compagnon — le nom du dossier = le titre.

---
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->
## Sources

<div style="color:#fff;">

Code runnable du cours (sous-module `git`) :

- 🔗 [github.com/StudioAlbert/cpp_builder_pattern_course_companion](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion)

Inclus localement :

- `companions/cpp_builder_pattern_course_companion/examples/` — un dossier par module
- `companions/cpp_builder_pattern_course_companion/exercises/sandwich_shop/` — exercice (starter + solution)

</div>

---

## Programme
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

1. **Module 1** — Le problème du constructeur télescopique *(10 min)*
2. **Module 2** — La solution Builder *(8 min)*
3. **Module 3** — Champs privés + `friend` + mutateurs `With*` *(10 min)*
4. **Module 4** — `build()` retourne le produit *(7 min)*
5. **Module 5** — Le chaînage (interface fluide) *(8 min)*
6. **Module 6** — Smart pointer · verrouiller le constructeur *(7 min)*
7. **Exercice** — Sandwich shop *(brief 5 min)*

---

## Module 1 — Le problème du constructeur télescopique
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>lisibilité · sites d'appel fragiles · explosion combinatoire</small>

---

### Trop de constructeurs tuent le constructeur

Au début un seul paramètre. Puis le besoin grandit, et les constructeurs
se mettent à enchaîner — chacun déléguant au suivant.

```cpp
class Person {
public:
    Person(std::string name);
    Person(std::string name, int age);
    Person(std::string name, int age, std::string email);
    Person(std::string name, int age, std::string email, bool premium);
    Person(std::string name, int age, std::string email,
           bool premium, bool newsletter);            // … jusqu'où ?
};
```

<small>📁 [`examples/00_telescoping_constructor`](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion/tree/main/examples/00_telescoping_constructor)</small>

Note:
C'est le « telescoping constructor » : chaque champ optionnel ajoute une
surcharge. Le code compile parfaitement — et c'est précisément le piège.
On nomme les quatre douleurs à la diapo suivante.

---

### Quatre limites

```cpp
Person c{"Cy", 40, "cy@example.com", false, true};   // que valent ces flags ?
```

- **Lisibilité** — au site d'appel, `false, true` ne dit rien : *premium ?
  newsletter ?* Il faut ouvrir l'en-tête pour deviner.
- **Sites d'appel fragiles** — deux `bool` (ou deux `int`) adjacents se
  permutent sans la moindre erreur de compilation.
- **Explosion combinatoire** — chaque champ optionnel double le nombre de
  surcharges plausibles.
- **« Jusqu'où irez-vous ? »**

<small>Le compilateur accepte les deux booléens inversés. C'est exactement
la classe de bug que le pattern Builder supprime.</small>

Note:
Garder ces quatre limites en tête : ce sont la grille d'évaluation de
chaque solution qui suit. Le Builder répond aux quatre ; les fausses
pistes de la diapo suivante n'en couvrent aucune complètement.

---

### Les fausses pistes

Avant le Builder, on tente souvent — et on bute :

| Tentative | Limite |
|---|---|
| Surcharges multiples | explosion combinatoire, ordre ambigu |
| Paramètres par défaut | positionnels : impossible de « sauter » un champ du milieu |
| Gros `struct` agrégat | aucune validation, aucun invariant garanti |
| *(C++20)* designated initializers | lisible, mais ni validation ni API publique stable |

> Aucune de ces pistes ne traite *à la fois* la lisibilité, la sûreté et la
> validation. C'est le créneau du Builder.

Note:
Les designated initializers (`Person{ .name="Ana", .age=30 }`) sont une
vraie alternative légère quand il n'y a pas d'invariant à vérifier — on y
revient en synthèse. Le Builder gagne dès qu'il faut *valider* l'objet ou
exposer une API de construction stable.

---

## Module 2 — La solution Builder
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>séparer *quoi construire* de *comment assembler*</small>

---

### L'idée

Un objet dédié accumule les choix, puis fabrique le produit en une fois.

```text
Client ──▶ Builder.setX()…setY() ──▶ build() ──▶ Person  (validée, prête)
            (état partiel, mutable)              (état final, cohérent)
```

Rôles du **Gang of Four** :

- **Product** = `Person` — l'objet final.
- **Builder** = `PersonBuilder` — accumule la configuration.
- **Director** *(optionnel)* = une recette réutilisable (ex. `makeVegan()`).

<small>Référence : Gamma, Helm, Johnson & Vlissides, *Design Patterns* (1994).</small>

Note:
« Gang of Four » (GoF) : les quatre auteurs du livre de 1994 qui ont
catalogué le Builder aux côtés du Visiteur (vu dans la séance
sérialisation). L'idée centrale : le produit ne voit le jour qu'à
`build()`, jamais à moitié construit.

---

## Module 3 — Champs privés + `friend` + mutateurs `With*`
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>le builder écrit dans le produit · l'encapsulation reste intacte</small>

---

### Le builder écrit dans le produit

Le **produit** garde ses champs `private` et déclare le builder `friend`. Le
**builder** détient le produit en cours (`product_`) et chaque mutateur `With*`
y écrit directement — aucun champ dupliqué.

```cpp
class Person {
    friend class PersonBuilder;          // seul le builder touche les champs
public:
    void Print() const;                  // lecture seule, aucun setter public
private:
    std::string name_;
    int age_ = 0;                        // défauts → champs vraiment optionnels
    std::string email_;
    bool premium_ = false;
};

class PersonBuilder {
    Person product_;                     // le produit en cours de construction
public:
    void WithName(std::string_view n)  { product_.name_    = n; }
    void WithAge(int age)              { product_.age_     = age; }
    void WithEmail(std::string_view e) { product_.email_   = e; }
    void WithPremium(bool premium)     { product_.premium_ = premium; }

    Person Build() const { return product_; }
};
```

<small>`friend` donne au builder l'accès aux membres privés : `Person` n'expose
ni constructeur public ni setter — impossible de fabriquer un `Person` à
moitié valide depuis l'extérieur.</small>

<small>📁 [`examples/01_build_returns_product`](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion/tree/main/examples/01_build_returns_product)</small>

Note:
Mutateurs `void` ici : pas encore de chaînage (Module 5). L'essentiel est le
design — champs privés + `friend` + produit embarqué — qui gagne d'un coup la
lisibilité (chaque champ est nommé) et l'encapsulation (aucun accès direct aux
champs de `Person`). La validation arrive au Module 4, dans `Build()`.

---

## Module 4 — build() retourne le produit
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>le seul endroit où l'objet naît · donc le seul endroit où valider</small>

---

### `build()` assemble **et valide**

L'objet ne voit le jour qu'à `build()`. C'est donc le point unique où
vérifier les invariants — un `Person` invalide ne peut jamais exister.

```cpp
Person Build() const {
    // Un seul endroit pour valider, avant que le Person n'existe.
    if (product_.name_.empty()) throw std::invalid_argument("name is required");
    if (product_.age_ < 0)      throw std::invalid_argument("age cannot be negative");
    return product_;                 // copie du produit embarqué
}
```

<small>Tant qu'aucun `build()` n'a réussi, on manipule un *builder*, pas un
`Person`. La validation centralisée ici remplace des `assert` éparpillés
dans tous les constructeurs.</small>

<small>📁 [`examples/01_build_returns_product`](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion/tree/main/examples/01_build_returns_product)</small>

Note:
C'est l'argument numéro un du pattern, et celui que le brouillon ne
nommait pas : **où** valider. Réponse : dans `build()`, une fois, avant
de matérialiser le produit. Le brief de l'exercice s'appuie là-dessus.

---

## Module 5 — Le chaînage (interface fluide)
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>`return *this;` — c'est tout</small>

---

### Chaque mutateur retourne `*this`

Renvoyer une **référence au builder** suffit à enchaîner les appels : la
configuration devient une seule expression lisible.

```cpp
PersonBuilder& WithName(std::string_view n) { product_.name_  = n; return *this; }
PersonBuilder& WithAge(int age)            { product_.age_   = age; return *this; }
PersonBuilder& WithEmail(std::string_view e){ product_.email_ = e; return *this; }
PersonBuilder& WithPremium(bool p = true)  { product_.premium_ = p; return *this; }

// Site d'appel :
Person ana = PersonBuilder{}
                 .WithName("Ana")
                 .WithAge(30)
                 .WithEmail("ana@example.com")
                 .WithPremium()
                 .Build();
```

<small>C'est l'*interface fluide*. Une seule ligne sépare une API verbeuse
d'une API qui se lit d'un trait : `return *this;`.</small>

<small>📁 [`examples/02_fluent_chaining`](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion/tree/main/examples/02_fluent_chaining)</small>

Note:
Subtilité à connaître sans s'y attarder : pour chaîner *sur un temporaire*,
on peut surcharger les mutateurs avec un qualificatif `&&`
(`PersonBuilder&& WithAge(int) &&`). Ici l'exemple chaîne sur un rvalue et
fonctionne car les références lvalue se lient au temporaire le temps de
l'expression complète. Détail dans le dépôt.

---

## Module 6 — Retourner un smart pointer
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>valeur par défaut · pointeur seulement si polymorphe / possédé</small>

---

### Quand le produit est polymorphe

Si l'appelant doit **posséder** un objet d'une hiérarchie, `build()` peut
rendre un `std::unique_ptr`.

```cpp
class Character : public Person { /* … */ };

class CharacterBuilder {
public:
    std::unique_ptr<Person> Build() const {
        return std::make_unique<Character>(name_, level_);   // dispatch virtuel
    }
};

std::unique_ptr<Person> hero = CharacterBuilder{"Mage"}.WithLevel(7).Build();
```

<small>⚠️ Par défaut, **retournez par valeur** (la RVO évite toute copie). Le
`unique_ptr` se justifie quand le produit est polymorphe ou possédé par le
tas — pas pour faire un `new` gratuit.</small>

<small>C'est le **seul** exemple où le builder n'embarque *pas* le produit par
valeur : copier un `Character` dans un `Person` le tronquerait (*slicing*).
D'où des champs parallèles + `make_unique` du type concret.</small>

<small>📁 [`examples/03_smart_pointer_product`](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion/tree/main/examples/03_smart_pointer_product)</small>

Note:
Le piège fréquent : croire que « Builder » implique « pointeur ». Non. La
valeur est le défaut moderne et le plus rapide. Le pointeur intelligent
n'entre que pour l'ownership d'un type polymorphe.

---

### Verrouiller le seul chemin de construction

Constructeur **privé** + `friend` : le builder devient l'unique porte
d'entrée. Aucun code ne peut fabriquer un `Person` non validé.

```cpp
class Person {
    friend class PersonBuilder;          // seul autorisé à créer un Person
    Person() = default;                  // ctor par défaut privé
    // … champs privés …
};

// Person p;   // ❌ ne compile pas : même le ctor par défaut est privé
Person ok = PersonBuilder{}.WithName("Ana").WithAge(30).Build();   // ✅
```

<small>Garantie forte : *tout* `Person` qui existe est passé par `build()`,
donc par la validation. C'est l'étape 5 de l'exercice.</small>

<small>📁 [`examples/04_private_ctor`](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion/tree/main/examples/04_private_ctor)</small>

Note:
On relie ici les deux idées : `build()` valide (Module 4) et le ctor privé
rend ce chemin obligatoire (Module 6). Ensemble = « valide par
construction ». L'exercice les fait implémenter dans l'ordre.

---

## Exercice — Sandwich shop
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

---

### Le brief

Point de départ fourni : une classe `Sandwich` à **constructeur
télescopique**, avec une méthode `Content()` qui liste son contenu (servez-
vous-en pour tester chaque étape).

**Votre tâche :**

1. Remplacer le constructeur par des **accesseurs** ; tester via `Content()`.
2. Ajouter une méthode **`Build()`**.
3. Extraire une classe **`SandwichBuilder`** à mutateurs.
4. **Chaîner** les mutateurs par rubrique (`box`, `bread`, `sauces`, …).
5. Rendre le **constructeur privé** : le builder devient l'unique chemin.
6. Encapsuler les **recettes** récurrentes en méthodes publiques (rôle
   *Director* : `Blt()`, `Vegan()`).

<small>📁 [`exercises/sandwich_shop`](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion/tree/main/exercises/sandwich_shop) · corrigé sur la branche `solution/sandwich-shop`</small>

Note:
La cible : reconstruire un BLT avec une API fluide et nommée, puis prouver
qu'un `Sandwich` ne peut plus naître hors d'un `build()`. Le corrigé
complet (6 étapes) vit sur la branche `solution/sandwich-shop` du dépôt.

---

## Synthèse
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Quel outil, quand

| Situation | Outil |
|---|---|
| Peu de champs, tous requis | constructeur simple |
| Agrégat trivial, lisibilité seule | designated initializers *(C++20)* |
| Beaucoup d'optionnels + invariants à valider | **Builder** |
| Produit polymorphe / possédé | Builder → `unique_ptr` |
| Mêmes recettes répétées | Builder + **Director** |

### Toujours

- **Valider dans `build()`** — un seul endroit, avant de matérialiser.
- **Un seul chemin de construction** (ctor privé + `friend`).
- **Préférer la valeur** au pointeur, sauf ownership polymorphe.

---

## Ressources
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- 📘 [refactoring.guru — Builder (C++)](https://refactoring.guru/design-patterns/builder/cpp/example)
- 📘 [platis.solutions — Builder pattern in C++ (2023)](https://platis.solutions/blog/2023/01/03/builder-pattern-cpp/)
- 📘 [« Builder pattern in C++ the right way » — A. Wang](https://medium.com/@antwang/builder-pattern-in-c-the-right-way-e943abbe0d2d)
- 📘 [« Builder Pattern in C++ » — K. Sharma](https://medium.com/@kamresh485/builder-pattern-in-c-6ffaeb44afe7)
- 💻 Dépôt compagnon : [github.com/StudioAlbert/cpp_builder_pattern_course_companion](https://github.com/StudioAlbert/cpp_builder_pattern_course_companion)

---

# Questions ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>Suite : refactorez le Sandwich shop derrière un `SandwichBuilder`.</small>
