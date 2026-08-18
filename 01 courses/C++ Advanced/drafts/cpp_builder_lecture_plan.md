# Plan — Lecture « C++ Builder »

> Plan de production pour transformer le brouillon `C++ Advanced/cpp_builder_lecture.md`
> en une lecture finie, alignée sur le style maison (Obsidian Advanced Slides +
> `_templates/css/sae_styles.css`), avec analyse « bonnes pratiques », contenu
> additionnel léger, et un dépôt compagnon (exemples + prérequis + branche corrigée).
>
> **Langue :** français, pour rester cohérent avec les lectures finalisées
> (`cpp_serialization_lecture_fr.md`, `cpp_ranges_lecture_fr.md`,
> `cpp_behaviour_tree_lecture.md`). Dire si une version EN est préférée.

---

## 0. Conventions de style extraites des lectures finies (checklist de conformité)

À respecter à la lettre pour « coller au CSS des autres lectures » :

- [ ] **Front-matter YAML** identique :
  ```yaml
  ---
  theme: white
  css:
    - _templates/css/sae_styles.css
  slideNumber: true
  transition: slide
  ---
  ```
- [ ] **Diapo titre** : `# Titre` + commentaire de fond
  `<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->`,
  un `###` sous-titre, une ligne `<small>` « N modules · N exemples · 1 exercice · C++17/20 »,
  et une ligne `<small>Dépôt : […]</small>`.
- [ ] **Diapos section** : `## Module X — …` + même `data-background` + `<small>` tagline.
- [ ] **Diapos contenu** : `### …`, prose courte, un seul bloc ` ```cpp `, légende `<small>` finale,
  bloc `Note:` (notes orateur) sous chaque diapo importante.
- [ ] **Séparateur** `---` entre chaque diapo.
- [ ] **Tableaux** pour les compromis / grilles d'évaluation (style « 4 problèmes difficiles »
  de la lecture sérialisation).
- [ ] **Référence d'exemple exécutable** par diapo de code :
  `<small>📁 [`examples/NN_nom`](URL_dépôt/tree/main/examples/NN_nom)</small>`.
- [ ] **Marqueurs visuels** : `✅ / ❌ / ⚠️` dans le texte et les tableaux ; émojis ressources `📘 💻 📺`.
- [ ] CSS : ne **rien** ajouter au CSS — les contraintes (`max-height` des `pre code`,
  `font-size` des tables, fond par défaut) sont déjà gérées. Garder les blocs de code **courts**
  (le CSS plafonne `pre code` à `max-height:200px`).
- [ ] Garder les diapos **peu denses** (`section` plafonnée à `60%` de hauteur).

---

## 1. Lecture reconstruite — déroulé diapo par diapo (rephrasé en douceur)

Le brouillon contient 4 idées clés (constructeur télescopique → builder → chaînage →
smart pointer) + un exercice « Sandwich shop ». On les développe en ~22 diapos, ton pédagogique
doux, sans changer l'intention de l'auteur. Fil rouge : **une classe `Person`** (comme demandé
dans le brouillon, ligne 1) en exemple courant, **`Sandwich`** réservé à l'exercice.

### Plan des modules

1. **Module 1 — Le problème du constructeur télescopique** *(10 min)*
2. **Module 2 — La solution Builder** *(8 min)*
3. **Module 3 — Outils : classe dédiée + mutateurs** *(10 min)*
4. **Module 4 — `build()` retourne le produit** *(7 min)*
5. **Module 5 — Le chaînage (interface fluide)** *(8 min)*
6. **Module 6 — Retourner un smart pointer** *(7 min)*
7. **Exercice — Sandwich shop** *(brief 5 min)*
8. **Synthèse + Ressources**

### Détail des diapos

**[Titre]** `# C++ Builder`
- Sous-titre `### Construire des objets complexes, lisiblement, en 1 heure`
- `<small>6 modules · 6 exemples · 1 exercice · C++17/20</small>`
- `<small>Dépôt : github.com/SAE-Geneve/CPlusPlus_Course_Builder</small>`
- Note : objectif = remplacer un constructeur qui enfle par un point de construction lisible et sûr.

**[Section]** `## Module 1 — Le problème du constructeur télescopique`

**[1.1] L'enflure du constructeur** — montrer `Person` avec 2, puis 5, puis 8 paramètres surchargés.
- Code : la cascade de constructeurs télescopiques.
- 4 douleurs nommées (reprise fidèle des mots du brouillon « readability, extensibility,
  error-prone, how far will you go ») :
  - **Lisibilité** — `Person p{"Ana", 30, true, "", 0, false};` : que veut dire `true` ?
  - **Sites d'appel fragiles** — deux `bool`/`int` adjacents → permutables sans erreur de compilation.
  - **Explosion combinatoire** — chaque champ optionnel double le nombre de surcharges plausibles.
  - **« Jusqu'où irez-vous ? »** — il n'y a pas de point d'arrêt naturel.
- `<small>` : le compilateur accepte `Person{"Ana", 30, true, false}` même si les deux booléens
  sont inversés — exactement la classe de bug que le pattern supprime.

**[1.2] Les fausses pistes** — pourquoi pas juste… ?
- Tableau compromis :

  | Tentative | Limite |
  |---|---|
  | Surcharges multiples | explosion combinatoire, ordre ambigu |
  | Paramètres par défaut | toujours positionnels ; on ne peut « sauter » un champ du milieu |
  | Gros struct + agrégat | aucune validation, aucun invariant garanti |
  | *(C++20)* designated initializers | lisible **mais** pas de validation, ni d'API publique stable |
- Note : le builder n'est pas la seule réponse — la dernière ligne prépare le Module 6/synthèse.

**[Section]** `## Module 2 — La solution Builder`

**[2.1] L'idée** — séparer *quoi construire* de *comment assembler*.
- Schéma texte (style ASCII des autres lectures) :
  ```text
  Client → Builder.set…().set…() → build() → Produit (Person) validé & immuable
  ```
- Rôles GoF nommés : **Product** = `Person`, **Builder** = `PersonBuilder`,
  (optionnel) **Director** = recette réutilisable.
- Note : « Gang of Four », *Design Patterns* (1994) — même cadre culturel que la lecture Visiteur.

**[Section]** `## Module 3 — Outils : classe dédiée + mutateurs`

**[3.1] Une classe builder dédiée + mutateurs** *(brouillon l.9–11)*
- Code : `PersonBuilder` avec un `set_age()`, `set_email()`… **non chaînés** (retour `void`).
- 📁 `examples/01_builder_setters`
- Note : version délibérément naïve ; sert de base avant `build()` et le chaînage.

**[Section]** `## Module 4 — build() retourne le produit`

**[4.1] `build()` assemble et valide** *(brouillon l.13–14)*
- Code : `Person build() const` qui construit le produit **et vérifie les invariants**
  (ex. `age >= 0`, email non vide si requis) → `throw`/`assert` sinon.
- `<small>` : `build()` est le seul endroit où l'objet voit le jour → seul endroit où valider.
- 📁 `examples/02_build_returns_product`

**[Section]** `## Module 5 — Le chaînage (interface fluide)`

**[5.1] Chaque mutateur retourne `*this`** *(brouillon l.16–18)*
- Code : `PersonBuilder& with_age(int)` → `… .with_age(30).with_email("a@b.c").build();`
- `<small>` : `return *this;` — c'est tout ce qui sépare une API verbeuse d'une API fluide.
- 📁 `examples/03_fluent_chaining`
- Note : mentionner le piège **rvalue/lvalue** — si on veut chaîner sur un builder temporaire,
  surcharger `&&` (`PersonBuilder&& with_age(int) &&`) ; à garder léger (1 phrase + renvoi au dépôt).

**[Section]** `## Module 6 — Retourner un smart pointer`

**[6.1] Quand le produit est polymorphe / possédé par tas** *(brouillon l.20–21)*
- Code : `std::unique_ptr<Person> build()` avec `std::make_unique`.
- `<small>` : retourner un `unique_ptr` quand l'appelant doit **posséder** un objet polymorphe
  (hiérarchie `Character : Person`) ; sinon préférer la **valeur** (RVO) — pas de `new` gratuit.
- 📁 `examples/04_smart_pointer_product`

**[6.2] Verrouiller le seul chemin de construction** *(brouillon l.30, étape 4)*
- Code : constructeur de `Person` **privé**, `friend class PersonBuilder` → le builder devient
  l'unique porte d'entrée.
- 📁 `examples/05_private_ctor`
- Note : utile pour garantir qu'aucun `Person` invalide ne peut exister hors d'un `build()` validé.

**[Section]** `## Exercice — Sandwich shop`

**[Ex.1] Le brief** *(reprise fidèle du brouillon l.24–31, reformulé proprement)*
- Point de départ fourni : un `Sandwich` à constructeur télescopique + méthode `content()`
  qui liste son contenu.
- Tâches numérotées :
  1. Remplacer le constructeur par des **accesseurs**, tester via `content()`.
  2. Ajouter une méthode **`build()`**.
  3. Extraire une **classe `SandwichBuilder`** à mutateurs.
  4. **Chaîner** les mutateurs par rubrique (`box`, `bread`, `sauces`, …).
  5. Rendre le **constructeur privé** : le builder devient l'unique chemin de construction.
  6. **Encapsuler les recettes** récurrentes dans des méthodes publiques (rôle *Director* :
     `make_classic_blt()`, `make_vegan()`).
- `<small>📁 [`exercises/sandwich_shop`](…)</small>` + `<small>` corrigé sur la branche `solution/sandwich-shop`.

**[Synthèse]** Tableau « quand utiliser quoi » :

  | Situation | Outil |
  |---|---|
  | Peu de champs, tous requis | constructeur simple |
  | Agrégat trivial, lisibilité seule | designated initializers (C++20) |
  | Beaucoup d'optionnels + invariants à valider | **Builder** |
  | Produit polymorphe / possédé | Builder → `unique_ptr` |
  | Mêmes recettes répétées | Builder + **Director** |
- Règles « toujours » : valider dans `build()` ; un seul chemin de construction ; préférer la
  valeur au pointeur sauf besoin d'ownership polymorphe.

**[Ressources]** Réécriture des sources du brouillon (l.34–37) au format `📘 💻 📺` :
- 📘 refactoring.guru — Builder (C++)
- 📘 platis.solutions — Builder pattern in C++ (2023)
- 📘 « Builder pattern in C++ the right way » (Medium, antwang)
- 💻 Dépôt compagnon `CPlusPlus_Course_Builder`
- 📺 (option) une conf CppCon sur les API fluides / object construction.

**[Questions ?]** diapo de clôture, même fond.

---

## 2. Analyse « bonnes pratiques » du brouillon

### Ce que le brouillon fait déjà bien
- **Progression pédagogique correcte** : problème → solution → outils → variantes → exercice.
- **Exercice concret et gradué** (6 étapes) avec un fil mémoriel fort (le sandwich).
- **Sources réelles** et pertinentes.
- Intuition juste que `build()` doit **retourner le produit** et que le constructeur doit
  finir **privé**.

### Lacunes à combler (légères, sans dénaturer)
1. **Validation absente** — le brouillon ne dit jamais *où* valider les invariants.
   → l'ajouter explicitement dans `build()` (Module 4). C'est l'argument n°1 du pattern.
2. **Valeur vs pointeur** — le brouillon saute au smart pointer sans dire *quand* il faut un
   pointeur. → préciser : valeur par défaut (RVO), `unique_ptr` seulement si polymorphe/possédé.
3. **Quand NE PAS utiliser un Builder** — manque le contrepoint honnête (cf. lectures maison qui
   énoncent toujours le compromis). → ajouter designated initializers / constructeur simple.
4. **Rôle Director non nommé** — l'étape 6 de l'exercice *est* un Director sans le dire.
   → le nommer (vocabulaire GoF, cohérent avec la lecture Visiteur).
5. **Sécurité du chaînage** — risque du builder *moved-from* / temporaire. → 1 phrase + exemple
   dépôt, sans alourdir.
6. **Fautes de frappe** à corriger : « extensively » → *extensibility* ; « constuct » → *construct* ;
   parenthèses non fermées l.25 et l.31 ; numérotation `2.` dupliquée l.27–28.

### Cohérence de style
- Convertir les notes télégraphiques (`=›`, `=>`) en vraies diapos + `Note:`.
- Ajouter les références `📁 examples/…` que toutes les autres lectures portent.

---

## 3. Contenu additionnel léger proposé

À ajouter **seulement si le temps le permet** (rester dans 1 h) :

- **Diapo « le builder ne sert pas qu'aux setters »** : montrer une *recette* (Director) en 4 lignes.
- **Encadré C++20** : `Person p{ .name="Ana", .age=30 };` (designated initializers) comme
  alternative légère — renforce le contrepoint « quand ne pas builder ».
- **Une ligne sur les builders compile-time / `consteval`** (juste un renvoi, pour les curieux).
- **Mini-comparatif** Builder vs Factory (1 ligne dans la synthèse) : Factory choisit *quel*
  type ; Builder configure *comment* l'assembler.
- **Note d'invariant** : un objet `Person` validé est *immuable* après `build()` (champs `const`
  ou pas de setters publics) → relie au thème « état valide par construction ».

---

## 4. Dépôt compagnon proposé

Aligné sur la convention maison `SAE-Geneve/CPlusPlus_Course_<Topic>`
(cf. `CPlusPlus_Course_Ranges`, `CPlusPlus_Course_Template`).

> ⚠️ Le scope GitHub de cette session est limité à `studioalbert/knowledges` ; je ne peux pas
> créer le dépôt `SAE-Geneve/CPlusPlus_Course_Builder` d'ici. Cette section décrit donc le
> **contenu prêt à pousser** ; à confirmer si l'on crée le dépôt manuellement ou si on
> m'autorise un autre emplacement.

### Nom : `CPlusPlus_Course_Builder`

### Arborescence
```text
CPlusPlus_Course_Builder/
├── README.md                 # objectifs, prérequis, build, table des exemples
├── CMakeLists.txt            # add_subdirectory pour chaque exemple + exercice
├── .gitignore                # build/, .idea/, etc.
├── examples/
│   ├── 01_builder_setters/        # Module 3 — mutateurs non chaînés
│   ├── 02_build_returns_product/  # Module 4 — build() + validation
│   ├── 03_fluent_chaining/        # Module 5 — return *this
│   ├── 04_smart_pointer_product/  # Module 6 — unique_ptr + polymorphisme
│   └── 05_private_ctor/           # Module 6 — friend + ctor privé
└── exercises/
    └── sandwich_shop/
        ├── README.md         # le brief (6 étapes)
        ├── include/sandwich.h    # Sandwich télescopique + content()  (POINT DE DÉPART)
        ├── src/main.cc           # scénario de test (asserts attendus)
        └── CMakeLists.txt
```
Chaque dossier `examples/NN_*` contient un `main.cc` autonome + `CMakeLists.txt`, **compilable
seul** (même règle que le dépôt Ranges : nom de dossier = titre de diapo).

### Prérequis (à mettre dans le README du dépôt)
- Compilateur **C++17** minimum (C++20 pour la diapo designated initializers).
- **CMake ≥ 3.16**.
- Notions supposées acquises (renvoi aux lectures précédentes du module) :
  `class`/`struct`, constructeurs & surcharge, références, `const`-correctness,
  `std::unique_ptr` / `std::make_unique`, bases de l'héritage & du polymorphisme.
- Aucune dépendance tierce (volontairement, contrairement à la lecture Boost).

### Branche corrigée
- Branche **`solution/sandwich-shop`** = `main` + corrigé complet de `exercises/sandwich_shop/`
  (les 6 étapes implémentées : accesseurs → `build()` → `SandwichBuilder` → chaînage →
  ctor privé + `friend` → méthodes-recettes Director), avec `src/main.cc` dont tous les
  `assert` passent.
- `main` reste le **point de départ** (constructeur télescopique seulement) pour que les
  étudiants partent d'une base qui compile.

### Contenu des 5 exemples (esquisse)
1. `01_builder_setters` — `PersonBuilder` à setters `void`, montre la verbosité avant chaînage.
2. `02_build_returns_product` — ajoute `Person build() const` + validation (`throw` si invalide).
3. `03_fluent_chaining` — setters renvoient `PersonBuilder&` ; site d'appel fluide.
4. `04_smart_pointer_product` — `build()` → `unique_ptr<Person>`, hiérarchie `Character : Person`.
5. `05_private_ctor` — ctor `Person` privé + `friend class PersonBuilder`.

---

## 5. Livrables & étapes d'exécution (après validation de ce plan)

1. Réécrire `C++ Advanced/cpp_builder_lecture.md` selon le déroulé §1 (français, conventions §0).
2. Garder le brouillon original en historique git (le fichier est versionné) ou le déplacer dans
   `drafts/` si on veut séparer brouillon et version finie (à confirmer).
3. Préparer le contenu du dépôt compagnon (§4) — soit dans un dossier local à pousser vers
   `SAE-Geneve/CPlusPlus_Course_Builder`, soit à un emplacement que vous indiquez (scope GitHub
   actuel = `studioalbert/knowledges` uniquement).
4. Brancher les liens `📁 examples/…` de la lecture sur les URL réelles du dépôt.
5. Commit + push sur `claude/cpp-builder-lecture-plan-3rxX5`.

### Questions ouvertes à trancher
- **Langue** : FR (défaut, cohérent) ou EN ?
- **Brouillon** : on écrase `cpp_builder_lecture.md` ou on garde le brouillon à côté ?
- **Dépôt** : je prépare les fichiers en local (vous créez/poussez le repo SAE-Geneve), ou
  vous m'autorisez un autre dépôt dans le scope ?
- **Portée build** : je rédige seulement la lecture maintenant, ou lecture **+** squelette du
  dépôt compagnon dans la foulée ?
