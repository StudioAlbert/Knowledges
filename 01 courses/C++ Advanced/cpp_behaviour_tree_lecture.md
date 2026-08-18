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

Une condition simple. 

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

## Bloc 3 — TP 1 : premier NPC errant
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">45' · TP · dans le projet CityBuilder</small>

<small style="color:#fff;">But : une unité qui **erre** sur la carte, pilotée par un BT.</small>

---

### Point de départ — tag `925-tp-bt-starter`

```bash
git checkout 925
```

Vous héritez d'un jeu **propre** : boucle SFML (fenêtre, `dt`, events),
caméra (drag/zoom), tilemap + terrain. **Aucune IA.**

On ajoute un NPC piloté par un BT que **vous** écrivez dans `core/ai/`.

---

### Le `Motor` — fourni (1/2) : l'API

Le déplacement vous est **donné** (`api/include/motion/motor.h`). Pas de pathfinding.

```cpp
class Motor {
 public:
  void Update(float dt);                 // à chaque frame
  float RemainingDistance() const;       // distance restant à parcourir
  void SetSpeed(float speed);
  void SetPosition(sf::Vector2f p);
  void SetDestination(sf::Vector2f d);
  const sf::Vector2f& GetPosition() const;
};
```

---

### Le `Motor` — fourni (2/2) : comment ça marche

```cpp
void Motor::Update(float dt) {
  sf::Vector2f d = destination_ - position_;
  remainingDistance_ = d.length();
  if (remainingDistance_ < speed_ * dt) {     // assez près → on colle
    position_ = destination_;
    return;
  }
  position_ += d.normalized() * speed_ * dt;  // sinon, un pas vers la cible
}
```

→ interpolation linéaire vers la cible. **`MoveToDestination()` se résume à tester
`RemainingDistance()`** — le `Motor` est une boîte noire.

---

### À livrer

1. Starter
	1. `api/ai/npc.{h,cc}` : sprite + `Motor` + un `bt_root_`, il y a un npc de base
	2. Éléments de base `Node`/`Status`, 
	3. Implementer une première action : Move to destination 
		1. créer la classe générique `Action`( utilisation de `std::function` pour l'éxécution d'une fonction externe)
		2. implémenter une première action concrète : Move to destination en utilisant la classe Motor
	4. Implémenter le noeud Composite `Sequence`
		1. Classe générique core/ai/composite integrant un vecteur de ** `unique_ptr`** comme liste de noeuds
		2. Classe concrète api/ai/sequence qui override le tick afin de respecter les règles de renvoi du status evoqué dans le cours
		3. remplacer le noeud action du npc par le noeud sequence, l'action est maintenant un enfant de la sequence.
		4. créer une nouvelle action PickRandomdestination
2. Attention au `core/CMakeLists.txt` : Passage de INTERFACE à inclusion normale

---

### Corrigé — `core/ai` : Node & Action

```cpp
// core/include/ai/bt_node.h
enum class Status { kFailure, kRunning, kSuccess };

class Node {
 public:
  Node() = default;
  virtual ~Node() = default;
  Node(const Node&) = delete;
  Node& operator=(const Node&) = delete;
  Node(Node&&) noexcept = default;
  Node& operator=(Node&&) noexcept = default;
  virtual void   Reset() = 0;
  virtual Status Tick()  = 0;
 protected:
  Status status_ = Status::kFailure;
};

// core/include/ai/bt_action.h
class Action : public Node {
  std::function<Status()> action_;
 public:
  explicit Action(std::function<Status()> a) : action_(std::move(a)) {}
  void Reset() override {}
  Status Tick() override { return action_(); }
};
```

---

### Corrigé — `core/ai` : Composite & Sequence

```cpp
// core/include/ai/bt_composite.h
class Composite : public Node {
 protected:
  std::vector<std::unique_ptr<Node>> children_;
  int childIdx_ = 0;
 public:
  void Reset() override { childIdx_ = 0; }
  void AddChild(std::unique_ptr<Node> c) { children_.push_back(std::move(c)); }
};

// core/src/ai/bt_sequence.cc
Status Sequence::Tick() {
  while (childIdx_ < (int)children_.size()) {
    const Status s = children_[childIdx_]->Tick();
    if (s == Status::kFailure) { Reset(); return Status::kFailure; }
    if (s == Status::kRunning) return Status::kRunning;
    childIdx_++;
  }
  Reset();
  return Status::kSuccess;
}
```

---

### Corrigé — `api/ai/npc.h`

```cpp
class Npc {
 public:
  void Setup(std::string_view sprite_path, sf::Vector2f world_size,
             sf::Vector2f start_position);
  void Update(float dt);
  void Draw(sf::RenderWindow& window);
 private:
  core::ai::behaviour_tree::Status PickRandomDestination();
  core::ai::behaviour_tree::Status MoveToDestination() const;

  static constexpr float kSpeed = 200.f;
  std::unique_ptr<sf::Texture> texture_ = std::make_unique<sf::Texture>();
  std::optional<sf::Sprite> sprite_;
  motion::Motor motor_;
  std::unique_ptr<core::ai::behaviour_tree::Node> bt_root_;
  sf::Vector2f world_size_{};
  std::mt19937 rng_{std::random_device{}()};
};
```

---

### Corrigé — `api/ai/npc.cc`

```cpp
void Npc::Setup(std::string_view path, sf::Vector2f world, sf::Vector2f start) {
  world_size_ = world;
  if (texture_->loadFromFile(std::string(path))) sprite_ = sf::Sprite(*texture_);
  motor_.SetPosition(start);
  motor_.SetDestination(start);            // immobile jusqu'au 1er tirage
  motor_.SetSpeed(kSpeed);

  auto wander = std::make_unique<Sequence>();
  wander->AddChild(std::make_unique<Action>([this]{ return PickRandomDestination(); }));
  wander->AddChild(std::make_unique<Action>([this]{ return MoveToDestination(); }));
  bt_root_ = std::move(wander);
}

void Npc::Update(float dt) { motor_.Update(dt); if (bt_root_) bt_root_->Tick(); }

Status Npc::PickRandomDestination() {
  std::uniform_real_distribution<float> x(0.f, world_size_.x), y(0.f, world_size_.y);
  motor_.SetDestination({x(rng_), y(rng_)});
  return Status::kSuccess;
}
Status Npc::MoveToDestination() const {
  return motor_.RemainingDistance() <= 0.001f ? Status::kSuccess : Status::kRunning;
}
```

---

### Corrigé — câblage `game/src/game.cc`

```cpp
namespace {                                 // namespace anonyme (état du module)
  // ... window_, camera_, map_ ...
  api::ai::Npc npc_;                         // ← nouvel état

  void Setup() {
    // ...
    npc_.Setup("_assets/kenney_medieval-rts/PNG/Default size/Unit/medievalUnit_01.png",
               world_size, {world_size.x * 0.5f, world_size.y * 0.5f});
  }
}

// dans Loop(), chaque frame :
camera_.Update(dt);  camera_.Apply(window_);
npc_.Update(dt);                            // ← logique

window_.clear();
map_.Draw(window_);
npc_.Draw(window_);                         // ← rendu
window_.display();
```

---

### Checkpoint attendu

- Le projet compile (cible `city_builder_game`).
- Une unité apparaît au centre et **erre** d'un point aléatoire à l'autre.
- Caméra (drag/zoom) toujours fonctionnelle.
- Boucle de la `Sequence` : pioche une destination (success) → se déplace
  (running) → arrive → reset → nouvelle destination.

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

## Bloc 5 — TP 2 : étoffer le comportement
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">45' · TP</small>

---

### Objectifs

1. Pour la suite :
	1. vous créerez sur le modele de la séquence un sélecteur, le tick respectant ses propres regles de renvoi des statuts
	2. ce sélecteur permet de  choisir ensuite les différentes séquences du comportement voulu voir slidedu npc affamé
2. Ajouter `Selector` dans `core/ai` (miroir de `Sequence`).
3. Confirmer la **rule of five** sur `Node` / `Composite` (movable-only).
4. Donner au NPC un 2ᵉ comportement : **se reposer quand il est fatigué**, sinon errer.
5. Racine = `Selector(repos, errance)`.

---

### Arbre cible du NPC

```text
Selector (root)
├── Sequence "repos"
│    ├── IsTired                  // énergie <= seuil ?
│    └── Rest                     // running jusqu'à énergie pleine
└── Sequence "errance"
     ├── PickRandomDestination
     └── MoveToDestination
```

<small>Le Selector tente le repos d'abord ; `IsTired` échoue tant que l'énergie est
haute → on retombe sur l'errance.</small>

---

### Corrigé — `Selector`

```cpp
// core/src/ai/bt_selector.cc
Status Selector::Tick() {
  while (childIdx_ < (int)children_.size()) {
    const Status s = children_[childIdx_]->Tick();
    if (s == Status::kSuccess) { Reset(); return Status::kSuccess; }
    if (s == Status::kRunning) return Status::kRunning;
    childIdx_++;
  }
  return Status::kFailure;
}
```

Succès court-circuite, échec continue — exactement l'inverse de `Sequence`.

---

### Corrigé — énergie (`npc`)

```cpp
// npc.h : nouveaux membres
float energy_ = kMaxEnergy;
float tick_dt_ = 0.f;
static constexpr float kTiredThreshold = 20.f;
static constexpr float kEnergyDrain = 6.f;   // /s en mouvement
static constexpr float kEnergyRegen = 25.f;  // /s au repos

// npc.cc — Update() mémorise dt : tick_dt_ = dt;
Status Npc::IsTired() const {
  return energy_ <= kTiredThreshold ? Status::kSuccess : Status::kFailure;
}
Status Npc::Rest() {
  energy_ = std::min(kMaxEnergy, energy_ + kEnergyRegen * tick_dt_);
  return energy_ >= kMaxEnergy ? Status::kSuccess : Status::kRunning;
}
Status Npc::MoveToDestination() {            // draine l'énergie en chemin
  if (motor_.RemainingDistance() <= 0.001f) return Status::kSuccess;
  energy_ = std::max(0.f, energy_ - kEnergyDrain * tick_dt_);
  return Status::kRunning;
}
```

---

### Corrigé — racine `Selector(repos, errance)`

```cpp
auto rest = std::make_unique<Sequence>();
rest->AddChild(std::make_unique<Action>([this]{ return IsTired(); }));
rest->AddChild(std::make_unique<Action>([this]{ return Rest(); }));

auto wander = std::make_unique<Sequence>();
wander->AddChild(std::make_unique<Action>([this]{ return PickRandomDestination(); }));
wander->AddChild(std::make_unique<Action>([this]{ return MoveToDestination(); }));

auto root = std::make_unique<Selector>();
root->AddChild(std::move(rest));
root->AddChild(std::move(wander));
bt_root_ = std::move(root);
```

---

### Checkpoint

- 0 leak (aucun `new` / `delete`).
- Le NPC erre, puis **s'arrête pour récupérer** quand l'énergie passe sous le seuil, puis repart.
- Tentative de `Sequence s = autre;` → **erreur de compilation** (movable-only). ✓

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

### Piste B — Fluent builder

---

What is builder pattern?

---

Burger example : Part 1
Problem is too many combinations

---

Burger example : Part 2
Make accessors and methods allowing to build each part

---

Part 3 : Everything together, what a builder can build

---

```cpp
class TreeBuilder {
  std::unique_ptr<Node> root_;
  // ...
 public:
  TreeBuilder& Sequence();
  TreeBuilder& Selector();
  TreeBuilder& End();
  std::unique_ptr<Node> Build();

  // Feuille : stocke le callable via TypedAction (pas de std::function)
  template <typename Fn>
  TreeBuilder& Action(Fn fn);
};
```

- Reconstruire l'arbre du NPC (TP 2) avec ce builder.
- Comparer la lisibilité.

---

### Piste C — Implémentation : pile de Composite courants

```cpp
// bt_builder.h : Action est un template inline (utilise TypedAction)
template <typename Fn>
TreeBuilder& TreeBuilder::Action(Fn fn) {
  Attach(MakeAction(std::move(fn)));   // pas de std::function
  return *this;
}

// bt_builder.cc
void TreeBuilder::Attach(std::unique_ptr<Node> node) {
  if (stack_.empty()) root_ = std::move(node);
  else                stack_.top()->AddChild(std::move(node));
}

TreeBuilder& TreeBuilder::Sequence() {
  auto node = std::make_unique<class Sequence>();  // "class" = le type, pas la méthode
  auto* raw = node.get();              // emprunt non-owning
  Attach(std::move(node));             // l'arbre prend l'ownership
  stack_.push(raw);                    // on retient le contexte courant
  return *this;
}
// Selector() : identique avec class Selector

TreeBuilder& TreeBuilder::End()   { stack_.pop(); return *this; }
std::unique_ptr<Node> TreeBuilder::Build() { return std::move(root_); }
```

---

### Piste C — Réécriture de l'arbre du NPC

```cpp
bt_root_ = TreeBuilder()
  .Selector()
    .Sequence()                                          // repos
      .Action([this]{ return IsTired(); })
      .Action([this]{ return Rest();    })
    .End()
    .Sequence()                                          // errance
      .Action([this]{ return PickRandomDestination(); })
      .Action([this]{ return MoveToDestination();     })
    .End()
  .End()
  .Build();
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

<small style="color:#fff;">Départ : tag `925-tp-bt-starter` · Corrigé : branche `925-tp-bt-corrected` (1 commit par TP)</small>

<small style="color:#fff;">Code : `core/src/ai/bt_*.cc` · `api/src/ai/npc.cc` · `game/src/game.cc`</small>
