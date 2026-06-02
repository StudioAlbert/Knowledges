---
theme: white
css:
- _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Behaviour Trees en C++ moderne
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Workshop · 4h · cours + TP incrémental</small>

<small style="color:#fff;">Codebase de référence : `core::ai::behaviour_tree`</small>

Note:
Vous connaissez le pattern BT via Unity. Aujourd'hui on le réécrit en C++
en partant d'une approche naïve, puis en l'amenant vers une lib idiomatique.

---
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->
## Déroulé

<div style="color:#fff;">

- **20'** · Bloc 1 — Rappel BT & vocabulaire *(cours)*
- **30'** · Bloc 2 — Première approche : héritage *(cours)*
- **45'** · Bloc 3 — TP 1 : `Node`, `Action`, première `Sequence` *(TP)*
- **30'** · Bloc 4 — Polymorphisme & ownership *(cours)*
- **45'** · Bloc 5 — TP 2 : `unique_ptr`, `Selector`, rule of five *(TP)*
- **30'** · Bloc 6 — Limites & optimisations *(cours)*
- **40'** · Bloc 7 — TP 3 : refactor (typed Action, builder) *(TP)*
- **20'** · Bloc 8 — Bilan & QA

</div>

---

## Bloc 1 — Rappel BT
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">20' · cours</small>

---

### BT ≠ FSM

**FSM**
- États + transitions
- Explose en arêtes (n²)
- Comportement = état courant

**BT**
- Arbre **tické** chaque frame
- Compose par hiérarchie
- Comportement = parcours

→ ajouter un comportement = ajouter une branche, pas recâbler n transitions.

---

### Le contrat : `Status`

```cpp
enum class Status { kFailure, kRunning, kSuccess };
```

- `kSuccess` — fini, OK
- `kFailure` — fini, KO
- `kRunning` — pas fini, rappelle-moi au prochain tick

Tout nœud, feuille ou composite, respecte ce contrat.

---

### Familles de nœuds

- **Leaf** — `Action`, `Condition` : fait quelque chose.
- **Composite** — `Sequence` (ET), `Selector` (OU) : compose des enfants.
- **Decorator** — `Inverter`, `Repeater`… : transforme le statut d'un enfant. *(hors scope aujourd'hui)*

---

### Sémantique des composites

|              | Enfant → Success      | Enfant → Failure      | Enfant → Running     |
|--------------|-----------------------|-----------------------|----------------------|
| **Sequence** | continue              | **retourne Failure**  | retourne Running     |
| **Selector** | **retourne Success**  | continue              | retourne Running     |

Sequence = ET court-circuité &nbsp;·&nbsp; Selector = OU court-circuité

---

### Exemple — NPC affamé

```text
Selector (priorité)
├── Sequence "manger"
│    ├── CheckHunger
│    ├── Move (vers cantine)
│    └── Eat
├── Sequence "travailler"
│    ├── PickResource
│    ├── Move
│    └── GetResource
└── Idle
```

<small>Tiré directement de `NpcBehaviourTree::SetupBehaviourTree`.</small>

---

## Bloc 2 — Première approche
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">30' · cours</small>

<small style="color:#fff;">On écrit la version "évidente". On verra ce qui coince.</small>

---

### Le nœud de base

```cpp
enum class Status { kFailure, kRunning, kSuccess };

class Node {
 public:
  virtual ~Node() = default;
  virtual Status Tick()  = 0;
  virtual void   Reset() = 0;
};
```

- `virtual ~Node()` → destruction polymorphe sûre.
- `= 0` → contrat, pas d'implémentation par défaut.
- `enum class` → pas de conversion implicite, pas de pollution du scope.

---

### Pourquoi l'héritage ici ?

- Le contrat `Tick` / `Reset` impose un **comportement commun** à tous les nœuds.
- Conséquence : les nœuds deviennent **interchangeables** — un parent ne connaît que `Node*`, jamais le type concret de son enfant.
- Permet d'**étendre la complexité au fil du temps** : ajouter un nouveau type de feuille ne touche à aucun nœud existant.
- Open / Closed Principle appliqué : ouvert à l'extension, fermé à la modification.

<small>C'est *la* raison pour laquelle on accepte le coût d'un `virtual`.</small>

---

### Une feuille : `CheckHungerAction`

```cpp
class CheckHungerAction : public Node {
  float& hunger_;
 public:
  explicit CheckHungerAction(float& h) : hunger_(h) {}

  Status Tick() override {
    return hunger_ >= 100 ? Status::kSuccess : Status::kFailure;
  }
  void Reset() override {}
};
```

Une condition simple. Le parent ne saura jamais qu'elle existe — il verra un `Node*`.

---

### Deuxième feuille : `GoToCafeteriaAction`

```cpp
class GoToCafeteriaAction : public Node {
  Motor& motor_;
  Vector2 target_;
 public:
  GoToCafeteriaAction(Motor& m, Vector2 t)
      : motor_(m), target_(t) {}

  Status Tick() override {
    if (motor_.AtPosition(target_)) return Status::kSuccess;
    motor_.MoveTowards(target_);
    return Status::kRunning;
  }
  void Reset() override {}
};
```

Deux feuilles, déjà deux classes. Imagine un NPC avec 20 actions…

→ inflation de classes à venir. On y reviendra (Bloc 6).

---

### Premier composite — comment stocker les enfants ?

- Un `Sequence` doit stocker `CheckHungerAction`, `GoToCafeteriaAction`, etc. — des **types différents**.
- **Le C++ ne sait pas faire de polymorphisme sans pointeur (ou référence) — sinon il *slice*.**
- Stocker `Node` par valeur → seul le sous-objet `Node` est conservé, la partie dérivée est tronquée.
- `Node` est **abstrait par design** : il ne peut pas être instancié seul de toute façon.

→ Conclusion : on stocke des **pointeurs**. Première version : `Node*`.

---

### Premier composite : `Sequence`

```cpp
class Sequence : public Node {
  std::vector<Node*> children_;   // ⚠ raw pointers
  int idx_ = 0;
 public:
  void AddChild(Node* c) { children_.push_back(c); }

  Status Tick() override {
    while (idx_ < children_.size()) {
      auto s = children_[idx_]->Tick();
      if (s == Status::kFailure) { idx_ = 0; return s; }
      if (s == Status::kRunning) return s;
      ++idx_;
    }
    idx_ = 0;
    return Status::kSuccess;
  }
  void Reset() override { idx_ = 0; }
};
```

Ça compile, ça tourne — direction TP 1.

---

## Bloc 3 — TP 1 : Squelette
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">45' · TP</small>

<small style="color:#fff;">Scénario console : un robot aspirateur.</small>

---

### Scénario

```cpp
struct World {
  float battery = 100.f;
  bool  dirt    = false;
  bool  on_dock = false;
  int   ticks   = 0;
};
```

Vous tickez à la main dans une boucle `for`. Pas de SFML, pas de moteur.

---

### À livrer

- `enum class Status`
- `class Node` abstraite (`Tick`, `Reset`)
- `class Action : public Node` recevant `std::function<Status()>`
- `class Sequence : public Node` avec **raw pointers** (volontaire)
- `main` : `Sequence(CheckBattery, GoToDock, Charge)` tické 30 fois

<small>**Note** : votre programme va *fuir*. C'est normal — on corrigera au TP 2.</small>

---

### Corrigé — éléments clés *(1/2)*

```cpp
enum class Status { kFailure, kRunning, kSuccess };

class Node {
 public:
  virtual ~Node() = default;
  virtual Status Tick()  = 0;
  virtual void   Reset() = 0;
};

class Action : public Node {
  std::function<Status()> fn_;
 public:
  explicit Action(std::function<Status()> f) : fn_(std::move(f)) {}
  Status Tick() override { return fn_(); }
  void Reset() override {}
};
```

---

### Corrigé — première Sequence + main *(2/2)*

```cpp
class Sequence : public Node {
  std::vector<Node*> children_;   // leaks assumés
  int idx_ = 0;
 public:
  void AddChild(Node* c) { children_.push_back(c); }
  Status Tick() override {
    while (idx_ < (int)children_.size()) {
      auto s = children_[idx_]->Tick();
      if (s == Status::kFailure) { idx_ = 0; return s; }
      if (s == Status::kRunning) return s;
      ++idx_;
    }
    idx_ = 0; return Status::kSuccess;
  }
  void Reset() override { idx_ = 0; }
};

int main() {
  World w;
  auto* seq = new Sequence();
  seq->AddChild(new Action([&]{ return w.battery < 20 ? Status::kSuccess : Status::kFailure; }));
  seq->AddChild(new Action([&]{ /* GoToDock */ return Status::kSuccess; }));
  seq->AddChild(new Action([&]{ w.battery += 5;
      return w.battery >= 100 ? Status::kSuccess : Status::kRunning; }));
  for (int i = 0; i < 30; ++i) { seq->Tick(); w.battery -= 1; }
  // delete seq; mais pas ses enfants → leak
}
```

---

### Checkpoint attendu

- Compile sans warning.
- Affiche le statut renvoyé par la racine à chaque tick.
- Le robot va au dock et charge quand la batterie est basse.
- Valgrind / ASan : **leak** sur les `new`. On en parlera.

---

## Bloc 4 — Polymorphisme & ownership
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">30' · cours</small>

---

### Les questions qui fâchent

Vous venez d'écrire du code qui fuit. Pourquoi ?

1. Qui possède les enfants ? Le parent ? Le code qui les a créés ?
2. Que se passe-t-il à la destruction du `Sequence` ?
3. Et si je copie un nœud accidentellement (passage par valeur) ?
4. Et si deux `Sequence` pointent vers la même feuille ?

→ Il manque une notion : **l'ownership**.

---

### Raw pointer : aucune intention exprimée

- `Node*` dit "voici une adresse". Rien sur *qui* l'a créée, *qui* doit la libérer.
- Le parent doit-il `delete` ses enfants ? Si oui, et l'enfant a été partagé ailleurs ?
- Risques classiques :
  - **Leak** — personne ne `delete`
  - **Double-free** — deux propriétaires se croient seuls
  - **Dangling** — un détruit, l'autre déréférence

→ Le raw pointer est un outil de bas niveau. On lui ajoute du **sens**.

---

### `std::unique_ptr` : ownership unique et explicite

- **Un seul propriétaire** à tout instant.
- **Destruction automatique** en sortie de scope ou à la destruction du conteneur.
- Transfert via `std::move`, **copie interdite** à la compilation.
- Modèle "un enfant = un parent" → exactement ce qu'un arbre demande.
- *Aparté* : `std::shared_ptr` existe (ownership partagé, refcount atomique) — inutile ici, aucun nœud n'a deux parents.
- **Coût : zéro.** Taille = un pointeur brut, pas de refcount, pas d'overhead runtime.

---

### Récapitulatif — quel pointeur pour un BT ?

| Type           | Ownership   | Coût               | Verdict BT |
|----------------|-------------|--------------------|------------|
| `Node*`        | ambigu      | 0                  | leaks      |
| `shared_ptr`   | partagé     | refcount atomique  | overkill   |
| `unique_ptr`   | **unique**  | ~0                 | ✓          |

Un enfant a **un seul parent**. `unique_ptr` exprime exactement ça.

---

### Le bon stockage

```cpp
class Composite : public Node {
 protected:
  std::vector<std::unique_ptr<Node>> children_;
  int childIdx_ = 0;
 public:
  void AddChild(std::unique_ptr<Node> c) {
    children_.push_back(std::move(c));
  }
  void Reset() override { childIdx_ = 0; }
};
```

Destruction en cascade gratuite. Pas de `delete` à écrire.

---

### Rule of five — pourquoi *movable-only* ?

```cpp
class Node {
 public:
  Node() = default;
  virtual ~Node() = default;

  Node(const Node&)            = delete;   // ❌ pas de copie
  Node& operator=(const Node&) = delete;

  Node(Node&& o) noexcept { std::swap(status_, o.status_); }
  Node& operator=(Node&& o) noexcept {
    std::swap(status_, o.status_); return *this;
  }
 protected:
  Status status_ = Status::kFailure;
};
```

- Copier un nœud polymorphe → slicing + double-ownership.
- Déplacer → OK, on transfère l'*identité*.

---

### Construction d'un arbre

```cpp
auto seq = std::make_unique<Sequence>();
seq->AddChild(std::make_unique<Action>([&]{ return CheckHunger(); }));
seq->AddChild(std::make_unique<Action>([&]{ return Move(); }));
seq->AddChild(std::make_unique<Action>([&]{ return Eat(); }));

auto root = std::make_unique<Selector>();
root->AddChild(std::move(seq));
root->AddChild(std::make_unique<Action>([&]{ return Idle(); }));
```

Verbeux ? Oui. On y reviendra (Bloc 6).

---

## Bloc 5 — TP 2 : Refactor propre
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">45' · TP</small>

---

### Objectifs

1. Remplacer `vector<Node*>` par `vector<unique_ptr<Node>>`.
2. Extraire `class Composite` factorisant `children_`, `childIdx_`, `AddChild`, `Reset`.
3. Implémenter `Selector` (miroir de `Sequence`).
4. Appliquer la **rule of five** sur `Node` et `Composite` (movable-only).
5. Construire l'arbre complet du robot et le ticker 30 fois.

---

### Arbre cible du robot

```text
Selector (root)
├── Sequence "recharge"
│    ├── CheckBatteryLow      // batterie < 20 ?
│    ├── GoToDock             // déplace
│    └── Charge               // running tant que < 100
├── Sequence "nettoie"
│    ├── DetectDirt
│    ├── GoToDirt
│    └── Vacuum
└── Patrol
```

---

### Corrigé — `Composite` & `Selector`

```cpp
class Composite : public Node {
 protected:
  std::vector<std::unique_ptr<Node>> children_;
  int idx_ = 0;
 public:
  void AddChild(std::unique_ptr<Node> c) { children_.push_back(std::move(c)); }
  void Reset() override { idx_ = 0; }
};

class Sequence : public Composite {
 public:
  Status Tick() override {
    while (idx_ < (int)children_.size()) {
      auto s = children_[idx_]->Tick();
      if (s == Status::kFailure) { Reset(); return s; }
      if (s == Status::kRunning) return s;
      ++idx_;
    }
    Reset(); return Status::kSuccess;
  }
};

class Selector : public Composite {
 public:
  Status Tick() override {
    while (idx_ < (int)children_.size()) {
      auto s = children_[idx_]->Tick();
      if (s == Status::kSuccess) { Reset(); return s; }
      if (s == Status::kRunning) return s;
      ++idx_;
    }
    return Status::kFailure;
  }
};
```

---

### Corrigé — Rule of five sur `Node`

```cpp
class Node {
 public:
  Node() = default;
  virtual ~Node() = default;
  Node(const Node&) = delete;
  Node& operator=(const Node&) = delete;
  Node(Node&&) noexcept = default;
  Node& operator=(Node&&) noexcept = default;
  virtual Status Tick()  = 0;
  virtual void   Reset() = 0;
};
```

Tentative de copie d'un `Sequence` ? **Erreur de compilation**. C'est l'effet recherché.

---

### Checkpoint

- Aucun `new` / `delete` dans votre code.
- ASan : **0 leak**.
- Recharge prioritaire si batterie basse, même si saleté présente.
- Tentative de `Sequence s = autre;` → **erreur de compilation**. ✓

---

## Bloc 6 — Limites & optimisations
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">30' · cours</small>

<small style="color:#fff;">Deux axes critiques sur l'implémentation actuelle.</small>

---

### Axe 1 — `std::function` vs héritage

```cpp
class Action : public Node {
  std::function<Status()> action_;   // TODO: use inheritance instead
 public:
  explicit Action(std::function<Status()> a) : action_(std::move(a)) {}
  Status Tick() override { return action_(); }
};
```

- **+** ergonomie : lambdas capturant le contexte.
- **−** **type erasure** → indirection virtuelle en plus du `virtual Tick`.
- **−** allocation heap possible (SBO non garantie).
- **−** debug peu lisible (stack trace anonyme).

---

### "Type erasure" — kézako ?

Schéma de ce que `std::function` fait *en interne* :

```cpp
class function_status {
  struct Concept {                          // interface interne
    virtual Status invoke() = 0;
    virtual ~Concept() = default;
  };
  template <typename Fn>
  struct Model : Concept {                  // un wrapper par type concret
    Fn fn;
    explicit Model(Fn f) : fn(std::move(f)) {}
    Status invoke() override { return fn(); }
  };
  std::unique_ptr<Concept> ptr_;            // ⚠ alloc heap !

 public:
  template <typename Fn>
  function_status(Fn f)
      : ptr_(std::make_unique<Model<Fn>>(std::move(f))) {}

  Status operator()() { return ptr_->invoke(); }
};
```

→ le type concret de la lambda est **oublié**, l'appel passe par un `virtual`. Donc : indirection + alloc + pas d'inlining.

---

### Alternative typée — la lib

```cpp
template <typename Fn>
class TypedAction : public Node {
  Fn fn_;
 public:
  explicit TypedAction(Fn fn) : fn_(std::move(fn)) {}
  Status Tick() override { return fn_(); }
  void Reset() override {}
};

template <typename Fn>
auto MakeAction(Fn fn) {
  return std::make_unique<TypedAction<Fn>>(std::move(fn));
}
```

Le type de la lambda est **préservé** dans le template. Pas de wrapper, pas d'alloc cachée.

---

### Alternative typée — en situation

```cpp
// Avant (avec std::function via Action) :
seq->AddChild(std::make_unique<Action>(
    [this]{ return CheckHunger(); }));

// Après (avec TypedAction) :
seq->AddChild(MakeAction(
    [this]{ return CheckHunger(); }));
//   ^^^^^^^^^^ déduit Fn, zéro alloc, inlinable
```

Aucune perte d'ergonomie côté appelant. Gain de perf invisible.

→ exactement ce que le `TODO` de `bt_action.h` du jeu suggère.

---

### Axe 2 — Ergonomie de construction

```cpp
// ce qu'on écrit aujourd'hui :
auto seq = std::make_unique<Sequence>();
seq->AddChild(std::make_unique<Action>([this]{ return CheckHunger(); }));
seq->AddChild(std::make_unique<Action>([this]{ return Move();        }));
seq->AddChild(std::make_unique<Action>([this]{ return Eat();         }));
```

```cpp
// ce qu'on aimerait :
auto tree = BT::Selector()
  .Child(BT::Sequence()
    .Action([this]{ return CheckHunger(); })
    .Action([this]{ return Move();        })
    .Action([this]{ return Eat();         }))
  .Action([this]{ return Idle(); })
  .Build();
```

---

### Récapitulatif des trade-offs

| Axe             | Avantage actuel    | Coût                 | Refactor       |
|-----------------|--------------------|----------------------|----------------|
| `function<>`    | lambdas simples    | indirection + alloc  | template typed |
| construction    | explicite          | très verbeux         | builder fluide |

---

## Bloc 7 — TP 3 : Refactor & critique
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">40' · TP</small>

<small style="color:#fff;">Par binôme : choisir **une** piste, mesurer, présenter.</small>

<small style="color:#fff;">**Selon le temps restant** : les pistes peuvent être terminées en autonomie après le workshop ; les corrigés sont fournis dans ce deck.</small>

---

### Piste A — Action typée

- Remplacer `std::function` par un `TypedAction<Fn>` + factory `MakeAction`.
- Mesurer 1M de ticks avec `std::chrono`.
- Comparer taille binaire (`size` sur l'exécutable).

---

### Piste C — Builder fluide

```cpp
class TreeBuilder {
  std::unique_ptr<Node> root_;
  // ...
 public:
  TreeBuilder& Sequence();
  TreeBuilder& Selector();
  TreeBuilder& Action(std::function<Status()> f);
  TreeBuilder& End();
  std::unique_ptr<Node> Build();
};
```

- Réécrire le `main` du TP 2 avec ce builder.
- Comparer la lisibilité.

---

### Piste C — Implémentation : pile de Composite courants

```cpp
class TreeBuilder {
  std::unique_ptr<Node> root_;
  std::stack<Composite*> stack_;

  void Attach(std::unique_ptr<Node> node) {
    if (stack_.empty()) {
      root_ = std::move(node);
    } else {
      stack_.top()->AddChild(std::move(node));
    }
  }

 public:
  TreeBuilder& Sequence() {
    auto s = std::make_unique<::Sequence>();
    auto* raw = s.get();             // emprunt non-owning
    Attach(std::move(s));            // l'arbre prend l'ownership
    stack_.push(raw);                // on retient le contexte courant
    return *this;
  }

  TreeBuilder& Selector() {
    auto s = std::make_unique<::Selector>();
    auto* raw = s.get();
    Attach(std::move(s));
    stack_.push(raw);
    return *this;
  }

  TreeBuilder& Action(std::function<Status()> f) {
    Attach(std::make_unique<::Action>(std::move(f)));
    return *this;                    // les feuilles n'empilent rien
  }

  TreeBuilder& End() { stack_.pop(); return *this; }

  std::unique_ptr<Node> Build() { return std::move(root_); }
};
```

---

### Piste C — Réécriture du `main` TP 2

```cpp
auto tree = TreeBuilder()
  .Selector()                                            // root
    .Sequence()                                          // recharge
      .Action([&]{ return CheckBatteryLow(w); })
      .Action([&]{ return GoToDock(w);        })
      .Action([&]{ return Charge(w);          })
    .End()
    .Sequence()                                          // nettoie
      .Action([&]{ return DetectDirt(w);      })
      .Action([&]{ return GoToDirt(w);        })
      .Action([&]{ return Vacuum(w);          })
    .End()
    .Action([&]{ return Patrol(w); })
  .End()
  .Build();

for (int i = 0; i < 30; ++i) tree->Tick();
```

→ la forme du code reflète enfin la forme de l'arbre.

---

### Corrigé Piste A — `TypedAction`

```cpp
template <typename Fn>
class TypedAction : public Node {
  Fn fn_;
 public:
  explicit TypedAction(Fn fn) : fn_(std::move(fn)) {}
  Status Tick() override { return fn_(); }
  void Reset() override {}
};

template <typename Fn>
std::unique_ptr<Node> MakeAction(Fn fn) {
  return std::make_unique<TypedAction<Fn>>(std::move(fn));
}

// Bench : 1M ticks, comparer std::function vs TypedAction
auto t0 = std::chrono::steady_clock::now();
for (int i = 0; i < 1'000'000; ++i) tree->Tick();
auto dt = std::chrono::steady_clock::now() - t0;
```

---

### Présentation croisée

- Chaque binôme montre 5 min : diff + mesure + verdict.
- Question commune : *"vaut le coup d'intégrer ça dans la base de code du jeu ?"*

---

## Bloc 8 — Bilan
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

---

### Ce que vous repartez avec

- Une lib BT minimale que **vous avez écrite**.
- La compréhension de *pourquoi* chaque choix dans le code du jeu :
  - héritage + `virtual` → interchangeabilité
  - `unique_ptr` → ownership explicite
  - rule of five, movable-only → sécurité à la compilation
- Une opinion argumentée sur les trade-offs réels.

---

### Pour aller plus loin

- Décorateurs : `Inverter`, `Repeater`, `UntilSuccess`.
- Parallel composite (sémantique & pièges de synchronisation).
- Blackboard partagé entre nœuds.
- Sérialisation d'un arbre (JSON / éditeur visuel).
- BT data-oriented : nœuds en SoA, tick batch — gros gain perf.

---

## Questions ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Code de référence : `core/src/ai/` · `api/src/ai/npc_behaviour_tree.cc`</small>
