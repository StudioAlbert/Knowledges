---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Sérialisation & Systèmes de Sauvegarde
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Aplatir des objets sur disque, et inversement, en 1 heure

<small>6 parties · texte vs binaire · 3 approches · 1 exercice · C++17/20</small>

Note:
Objectif de cette heure : être capable de sauvegarder un état de jeu sur
disque et de le recharger, et savoir *laquelle* des trois techniques
choisir. On termine sur un système de sauvegarde de tilemap que vous
pourrez intégrer directement au City Builder.

---

## Programme
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

1. **Partie 1** — Qu'est-ce que la sérialisation ? *(8 min)*
2. **Partie 2** — Pourquoi sérialiser ? Sauvegarder & transmettre *(7 min)*
3. **Partie 3** — Texte vs Binaire *(7 min)*
4. **Partie 4** — Solution 1 : mémoire brute / `reinterpret_cast` *(9 min)*
5. **Partie 5** — Solution 2 : Boost.Serialization *(9 min)*
6. **Partie 6** — Solution 3 : le patron Visiteur + tilemap *(16 min)*
7. **Exercice** — Un système de sauvegarde de tilemap *(brief 4 min)*

---

## Partie 1 — Qu'est-ce que la Sérialisation ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>aplatir · transporter · ressusciter</small>

---

### L'Analogie du Téléporteur

> Prendre un objet (ou un graphe d'objets), l'**aplatir** en un flux
> unidimensionnel de bits, déplacer ce flux à travers l'*espace*
> (un câble) ou le *temps* (un disque), puis **inverser** le processus
> et ressusciter le ou les objets d'origine.

```text
   Graphe d'objets         Flux d'octets          Graphe d'objets
  ┌─────────┐              0100110...            ┌─────────┐
  │ TileMap │  ──sérialise──▶  📀 / 🌐  ──désérialise──▶ │ TileMap │
  └─────────┘                                    └─────────┘
   (ici, maintenant)                              (ailleurs, plus tard)
```

<small>« Comme le téléporteur de Star Trek. » — FAQ sérialisation d'isocpp.org</small>

Note:
Deux directions, un seul contrat : quel que soit l'ordre dans lequel
`serialize` écrit les champs, `deserialize` doit les relire dans
*exactement* le même ordre. Cette symétrie est l'unique invariant sur
lequel repose toute la séance.

---

### L'Unique Invariant

`serialize` et `deserialize` sont des images miroir. Mêmes champs,
**même ordre**, sinon le flux se désynchronise.

```cpp
struct Tile { int id; bool walkable; };

void save(std::ostream& os, const Tile& t) {
    os << t.id << ' ' << t.walkable << '\n';   // id, puis walkable
}

void load(std::istream& is, Tile& t) {
    is >> t.id >> t.walkable;                   // id, puis walkable
}                                               // ❌ inversez-les → données corrompues
```

<small>Aucune exception, aucun crash — juste un `walkable` qui était
auparavant un `id`. Les bugs de désynchronisation sont le piège n°1 de
la sérialisation faite à la main.</small>

Note:
C'est pour cela que tout format robuste écrit un *numéro de version en
premier* et c'est pour cela que les bibliothèques existent : elles
maintiennent les deux côtés en phase pour vous. On y arrive à la fin.

---

## Partie 2 — Pourquoi Sérialiser ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>deux cas d'usage : sauvegarder & transmettre</small>

---

### Deux Cas d'Usage, Un Seul Mécanisme

| Cas d'usage | À travers… | Contrainte dominante |
|---|---|---|
| **Sauvegarde** (fichier de save, historique d'undo, config) | le *temps* (disque) | versioning — les anciennes saves doivent toujours se charger |
| **Transmission** (netcode, IPC, RPC) | l'*espace* (réseau) | endianness & taille — les machines diffèrent |

Le mécanisme est identique ; les **contraintes diffèrent**. Un système
de save pardonne la latence mais ne pardonne jamais une save cassée.

Note:
Gardez cette distinction à l'esprit pour chaque diapo ultérieure :
quand on dit « écrire un numéro de version », c'est la contrainte de
*sauvegarde* qui parle. Quand on dit « ordre des octets réseau »,
c'est la contrainte de *transmission*. Même code, non-négociables
différents.

---

### Ce Qui Rend la Tâche Difficile

Une `struct` plate d'`int`s est triviale. Un vrai état de jeu, non :

- **Pointeurs / références** — une adresse n'a aucun sens lors de
  l'exécution suivante. Elle doit devenir un *id* stable, puis être
  reliée au chargement.
- **Polymorphisme** — un `Building*` peut en réalité être une `House`.
  Le flux doit enregistrer *quel* type concret reconstruire.
- **Partage & cycles** — deux PNJ pointent vers un même `BehaviourTree`.
  Une récursion naïve le duplique (ou boucle à l'infini).
- **Versioning** — la v2 du jeu doit toujours ouvrir une save v1.

<small>Tout dans les Parties 4–6 est une réponse différente à *ces
quatre* problèmes.</small>

Note:
Les données plates sont résolues en cinq minutes. L'ingénierie
intéressante porte sur l'identité (pointeurs), le type (polymorphisme),
les graphes (partage/cycles) et l'évolution (versioning). Gardez ces
quatre éléments comme grille d'évaluation pour chaque solution.

---

## Partie 3 — Texte vs Binaire
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>la première décision de conception</small>

---

### Le Tableau des Compromis

| | **Texte** (JSON, XML, `<<`) | **Binaire** (`fwrite`, packé) |
|---|---|---|
| Lisible / déboguable | ✅ vérifiable à l'œil | ❌ besoin d'un visualiseur hex |
| Soucis de `sizeof` / endianness | ✅ aucun | ⚠️ à votre charge |
| Taille sur disque / réseau | ❌ plus gros | ✅ compact |
| CPU pour encoder/décoder | ❌ plus | ✅ moins de cycles |
| Diff-able dans git, éditable | ✅ oui | ❌ non |

> « Une seule taille ne convient pas à tout. » — FAQ isocpp. Choisissez
> selon le cas d'usage, pas par habitude.

Note:
Le défaut honnête pour *la config et les petits fichiers de save* est
le texte : la déboguabilité écrase le coût en taille. Le binaire
gagne sa place sur le réseau et sur les gros assets/niveaux où les
octets et les cycles comptent réellement.

---

### La Taxe Cachée du Binaire : Endianness & `sizeof`

Dès qu'un bloc binaire traverse les machines, un `fwrite` brut vous
trahit.

```cpp
uint32_t hp = 1000;
fwrite(&hp, sizeof hp, 1, f);   // une machine little-endian écrit 0xE8 03 00 00
                                // une machine big-endian le lit comme 3 892 379 648
```

Solution : adouber **un seul** format canonique « réseau » et faire
passer toute valeur multi-octets par des helpers de conversion.

```cpp
uint32_t to_net(uint32_t h)   { return htonl(h); }   // hôte → réseau
uint32_t from_net(uint32_t n) { return ntohl(n); }   // réseau → hôte
```

<small>Centralisez ça dans un seul header. Ne saupoudrez jamais `htonl`
aux sites d'appel — c'est ainsi qu'une machine se retrouve à moitié
convertie.</small>

Note:
`sizeof(long)` diffère aussi selon les plateformes/compilateurs —
préférez les types à largeur fixe de `<cstdint>` (`uint32_t`, `int64_t`)
dans tout format binaire. Le texte évite entièrement ces deux problèmes,
c'est son super-pouvoir discret.

---

## Partie 4 — Solution 1 : Mémoire Brute
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>`reinterpret_cast` — l'outil rapide et tranchant</small>

---

### La Victoire Naïve

Pour une struct **trivialement copiable**, la sérialisation tient en
un `fwrite`.

```cpp
struct Tile { int id; bool walkable; };          // POD, aucun pointeur
static_assert(std::is_trivially_copyable_v<Tile>);

std::vector<Tile> map = /* ... */;

std::ofstream os("level.bin", std::ios::binary);
os.write(reinterpret_cast<const char*>(map.data()),
         map.size() * sizeof(Tile));             // toute la map, un seul appel
```

La relecture est le miroir : `resize`, puis `read` dans `data()`.

<small>Vraiment le bon outil pour des tableaux de POD en masse — une
tilemap de `Tile`s plats se sauvegarde et se charge en microsecondes.</small>

Note:
Ce n'est pas un homme de paille. Pour de grands tableaux de données
trivialement copiables (heightmaps, grilles de tuiles, buffers de
particules) une copie de bloc brute est la réponse la *plus rapide
possible* et parfaitement correcte. Le problème ne réside que dans les
conditions aux limites de la diapo suivante.

---

### Là Où `reinterpret_cast` Mord

Le même one-liner devient indéfini ou faux dès que l'une de ces
conditions est vraie :

```cpp
struct Bad {
    std::string name;          // ❌ possède un pointeur tas → vous écririez
                               //    le POINTEUR, pas les caractères
    Tile* current;             // ❌ adresse invalide à la prochaine exécution
    virtual ~Bad();            // ❌ pointeur vtable cuit dans les octets
};
```

- **Pointeurs / `std::string` / `std::vector`** → vous sérialisez une
  adresse, pas les données qu'elle possède.
- **vtables** → le premier mot d'un objet polymorphe est un pointeur
  local au processus. Garbage au rechargement.
- **Padding & `sizeof`** → le blob n'est pas portable entre
  compilateurs/architectures.
- **Aucun champ de version** → modifier un membre brique toutes les
  anciennes saves.

<small>Règle : la copie brute est réservée aux données *feuilles*
`is_trivially_copyable` uniquement. Tout ce qui a de l'ownership ou
du polymorphisme exige le Partie 5 ou 6.</small>

Note:
Notez la Solution 1 face à nos quatre problèmes difficiles :
pointeurs ❌, polymorphisme ❌, partage/cycles ❌, versioning ❌. Elle
gagne exactement un scénario — les données POD plates en masse — et y
est imbattable. Connaissez la frontière ; ne la dépassez pas.

---

## Partie 5 — Solution 2 : Boost.Serialization
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>la bibliothèque clé en main</small>

---

### Un Template, Deux Directions

L'astuce centrale de Boost : vous écrivez **une seule** fonction
`serialize`. Le même code sauvegarde *et* charge — c'est l'archive qui
décide de la direction.

```cpp
#include <boost/serialization/access.hpp>

class Tile {
    friend class boost::serialization::access;

    template <class Archive>
    void serialize(Archive& ar, const unsigned int version) {
        ar & id_ & walkable_;        // operator& = "<<" ou ">>" selon le besoin
    }
    int id_; bool walkable_;
};
```

<small>`ar &` est lecture-ou-écriture selon que `Archive` est une
archive d'*entrée* ou de *sortie* — la liste des champs s'écrit **une
seule fois**.</small>

Note:
Cette idée « une fonction, deux directions » est le point à retenir le
plus important de toute la séance. Elle supprime le piège de
désynchronisation du Partie 1 *par construction* : il n'existe qu'un
ordre de champs car il n'existe qu'une fonction. Le Partie 6 nomme le
patron de conception sous-jacent — le Visiteur — et montre qu'il est
utile bien au-delà de Boost.

---

### Sauvegarde & Chargement

Le type d'archive au site d'appel choisit texte / binaire / XML — le
corps de `serialize` ne change jamais.

```cpp
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>

void save(const TileMap& m) {
    std::ofstream ofs("save.txt");
    boost::archive::text_oarchive oa(ofs);
    oa << m;                       // profond, récursif, automatique
}

void load(TileMap& m) {
    std::ifstream ifs("save.txt");
    boost::archive::text_iarchive ia(ifs);
    ia >> m;                       // pointeurs reliés pour vous
}
```

<small>Remplacez `text_*archive` → `binary_*archive` pour une sortie
compacte. Pas une ligne de `serialize` ne change.</small>

Note:
Le bénéfice : pointeurs, `std::vector`, `std::map`, objets partagés et
cycles sont tous gérés automatiquement — Boost suit l'identité des
objets et reconstruit le graphe. Ce sont les trois problèmes difficiles
qu'a ratés la mémoire brute, résolus par la bibliothèque.

---

### Polymorphisme & Versioning — Gratuitement

```cpp
// Derived enregistre sa base pour qu'un Building* qui est en réalité
// une House se reconstruise comme House :
template <class Archive>
void House::serialize(Archive& ar, const unsigned int) {
    ar & boost::serialization::base_object<Building>(*this);
    ar & rooms_;
}

// Versioning : on incrémente le numéro, on branche dessus. Les
// anciennes saves se chargent toujours.
template <class Archive>
void Tile::serialize(Archive& ar, const unsigned int version) {
    ar & id_;
    if (version > 0) ar & biome_;        // champ ajouté en v1
}
BOOST_CLASS_VERSION(Tile, 1)
```

<small>Les quatre problèmes difficiles : ✅ pointeurs ✅ polymorphisme
✅ partage/cycles ✅ versioning. Le coût est la dépendance Boost.</small>

Note:
Boost est la réponse pragmatique en production quand vous pouvez
absorber la dépendance. Le compromis : coût de compilation lourd, une
dépendance non triviale, et de la « magie » difficile à déboguer quand
elle se comporte mal. Le partie suivant est totalement indépendant de
tout ça : un patron de conception général — le Visiteur — appliqué
directement à vos propres types.

---

## Partie 6 — Solution 3 : Le Patron Visiteur
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

L'un des patrons originaux du **Gang of Four** — Gamma, Helm, Johnson &
Vlissides, *Design Patterns* (1994).

<small>un patron OO général — *puis* appliqué au save/load</small>


Note:
« Gang of Four » (GoF) est le surnom de ces quatre auteurs et de leur
livre de 1994, qui a catalogué pour la première fois le Visiteur aux
côtés d'une vingtaine d'autres patrons. Oubliez la sérialisation
pendant trois diapos : on apprend Visiteur comme un outil autonome sur
un exemple de géométrie, puis on montre que le save/load n'en est
qu'une application.

---

Métaphore du représentant insupportable en assurance

![[Pasted image 20260525221008.png]]

Chaque client potentiel dispose d'une assurance différente (Risque industriel, habitation, Cambriolage) pourtant tout le monde est couvert.


---

![[Pasted image 20260525222024.png]]

---

### Le Problème Que Résout le Visiteur

Vous avez une hiérarchie de classes **stable**. Vous avez sans cesse
besoin de **nouvelles opérations** — et chaque nouvelle
opération force une édition de *chaque* classe.

```cpp
struct Shape  { virtual ~Shape() = default; };
struct Circle : Shape { double r; };
struct Square : Shape { double side; };

// Besoin de area() ?       → ajouter une méthode à Circle ET Square.
// Besoin de perimeter() ?  → ajouter une méthode à Circle ET Square.
// Besoin de draw, hash, serialize… ? → toucher à chaque classe, à chaque fois.
```

<small>Ajouter un *type* est rare. Ajouter une *opération* est constant.
Les méthodes optimisent pour le cas rare et éparpillent des
préoccupations sans rapport (géométrie + I/O + rendu) à travers les
classes de données.</small>

Note:
C'est la motivation manuel-scolaire du Visiteur. L'asymétrie — types
stables, ensemble d'opérations croissant — est exactement la situation
d'un système de save (save, load, debug-dump, hash, net-pack… sur les
mêmes types).

---

### L'Idée : Extraire l'Opération

Mettez chaque opération dans son propre objet **Visiteur**. Chaque
classe ne garde **qu'une** méthode — `accept` — dont l'unique rôle est
de rappeler le visiteur.

```cpp
struct Visitor {                       // l'interface de l'opération
    virtual void visit(Circle&) = 0;
    virtual void visit(Square&) = 0;
};

struct Shape  { virtual void accept(Visitor&) = 0; };

struct Circle : Shape { double r;
    void accept(Visitor& v) override { v.visit(*this); } };
struct Square : Shape { double side;
    void accept(Visitor& v) override { v.visit(*this); } };
```

<small>`accept` est la *seule* chose dont la hiérarchie aura jamais
besoin. Une nouvelle opération = une nouvelle classe Visiteur, avec
**zéro édition** de Circle/Square.</small>

Note:
L'appel en deux temps — `shape.accept(v)` puis `v.visit(concret)` — est
le *double dispatch* : le type d'exécution *des deux* (élément ET
visiteur) sélectionne le code. Les appels virtuels C++ sont en single
dispatch et ne peuvent pas exprimer cela en un seul appel ; `accept`
est l'astuce qui le récupère.

---

### Un Visiteur Concret

L'opération entière vit dans le visiteur. La hiérarchie n'a jamais
changé.

```cpp
struct AreaVisitor : Visitor {
    double area = 0;
    void visit(Circle& c) override { area = 3.14159 * c.r * c.r; }
    void visit(Square& s) override { area = s.side * s.side; }
};

Circle c{2.0};
AreaVisitor av;
c.accept(av);                 // av.area == 12.56…

// Nouveau besoin demain → écrire PerimeterVisitor.
// Circle et Square : non touchés.
```

<small>Rôles GoF : **Element** = `Shape`, **ConcreteElement** =
`Circle`/`Square`, **Visitor** = l'interface, **ConcreteVisitor** =
`AreaVisitor`.</small>

Note:
Énoncez le compromis honnêtement : Visiteur rend les nouvelles
*opérations* peu chères mais les nouveaux *types d'éléments* coûteux —
chaque visiteur doit acquérir une surcharge `visit`. Utilisez-le donc
seulement quand la hiérarchie est stable et que les opérations se
multiplient. Diapo suivante : c'est précisément le cas du save/load.

---

### Pourquoi le Visiteur Convient au Save / Load

La sérialisation a une **structure stable** (vos types de données) et
un **ensemble croissant d'opérations** qui parcourent toutes la *même
liste de champs* :

| ConcreteVisitor | Parcourt les champs pour…              |
| --------------- | -------------------------------------- |
| **Save**        | écrire chaque champ dans un flux       |
| **Load**        | lire chaque champ depuis un flux       |
| Debug-dump      | imprimer chaque champ dans le log      |
| Hash            | injecter chaque champ dans un checksum |
| Net-pack        | écrire chaque champ en ordre réseau    |

Le type déclare ses champs **une seule fois** (son `accept`). Save et
Load sont **deux visiteurs** sur cette unique déclaration — *pas* deux
fonctions miroir écrites à la main qui peuvent dériver l'une de
l'autre (le piège du Partie 1).

Note:
C'est la chute vers laquelle pointe tout l'arc côté utilisateur. Save
et load ne sont pas une paire miroir fragile — ce sont deux
ConcreteVisitors sur une unique déclaration de champs. Structure
déclarée une fois ; verbes variant librement.

---

### Deux Visiteurs Concrets : Writer & Reader

Pour le save/load les **éléments** sont vos types de données ; les
**opérations** sont un writer et un reader — deux ConcreteVisitors,
exactement comme `AreaVisitor`. On nomme les contrats avec deux
`concept`s C++20, pour que les signatures se documentent elles-mêmes.

```cpp
// Type-feuille streamable dans les deux sens.
template <class T>
concept Serializable = requires(std::ostream& os, std::istream& is, T& x) {
    { os << x };
    { is >> x };
};

// Visiteur qui expose un callback make_field(T&).
template <class V>
concept FieldVisitor = requires(V& v, int& probe) {
    { v.make_field(probe) };
};

struct Writer {                     // ConcreteVisitor : « save »
    std::ostream& os;
    template <Serializable T> void make_field(const T& x) { os << x << ' '; }
};

struct Reader {                     // ConcreteVisitor : « load »
    std::istream& is;
    template <Serializable T> void make_field(T& x) { is >> x; }
};
```

<small>`make_field()` est le callback `visit` — un verbe, pas un nom :
le visiteur *enregistre* ou *restaure* un champ. Les concepts rendent
l'intention lisible dans toutes les signatures qui suivent.</small>

Note:
Les concepts remplacent le commentaire-en-prose : `Serializable` dit
« ce type est une feuille streamable » et `FieldVisitor` dit « ce
visiteur sait enregistrer un champ ». Les erreurs de compilation
deviennent localisées et lisibles au lieu d'exploser dans les
internals du template. Le probe-type `int&` du concept évite le piège
des deux directions (Writer prend `const T&`, Reader prend `T&`) tout
en garantissant un contrat utile.

---

### Un Seul `serialize`, Réutilisé par les Deux

Chaque type liste ses champs **une seule fois** dans `serialize`.
Passez-lui un `Writer` et il sauvegarde ; passez-lui un `Reader` et il
charge. L'ordre ne peut jamais diverger.

```cpp
struct Tile {
    int id; bool walkable;
    template <FieldVisitor V> void serialize(V& v) {
        v.make_field(id); v.make_field(walkable);
    }
};

struct TileMap {
    int w, h;
    std::vector<Tile> tiles;
    template <FieldVisitor V> void serialize(V& v) {
        v.make_field(w); v.make_field(h);
        std::size_t n = tiles.size();
        v.make_field(n);         // count : écrit au save, lu au load
        tiles.resize(n);         // no-op au save ; dimensionne le vector au load
        for (auto& t : tiles) t.serialize(v);   // récurrence dans le graphe
    }
};
```

<small>Une liste de champs, deux comportements — le piège de
désynchronisation du Partie 1 a disparu *par construction*. La
contrainte `FieldVisitor V` *exige* `make_field` à la compilation.</small>

Note:
`v.make_field(n)` puis `tiles.resize(n)` rend la symétrie littérale :
les deux mêmes lignes écrivent-puis-noop au save et
lisent-puis-grossissent au load. Comparez aux deux fonctions écrites à
la main du Partie 1 qui pouvaient dériver — ici il n'y a qu'un ordre
car il n'y a qu'une fonction.

---

### En Pratique : Sérialiser une Tilemap

Mise en commun — une save versionnée et auto-vérifiante :

```cpp
constexpr uint32_t kMagic = 0x544D4150;   // 'TMAP'
constexpr uint32_t kVersion = 1;

void save_map(const TileMap& m, const std::string& path) {
    std::ofstream ofs(path);
    Writer w{ofs};
    uint32_t magic = kMagic, ver = kVersion;
    w.make_field(magic); w.make_field(ver);     // header EN PREMIER — toujours
    const_cast<TileMap&>(m).serialize(w);
}

void load_map(TileMap& m, const std::string& path) {
    std::ifstream ifs(path);
    Reader r{ifs};
    uint32_t magic, ver;
    r.make_field(magic); r.make_field(ver);
    if (magic != kMagic)  throw std::runtime_error("not a tilemap");
    if (ver  != kVersion) throw std::runtime_error("version mismatch");
    m.serialize(r);
}
```

<small>Numéro magique = « est-ce seulement mon fichier ? ». Version =
« puis-je encore le lire ? ». Tous deux écrits *avant* la charge
utile.</small>

Note:
C'est toute la séance en une diapo : choisir le texte ici pour la
déboguabilité (Partie 3), rejeter le raccourci du cast brut parce que
`tiles` possède un vector (Partie 4), appliquer le patron Visiteur pour
que save et load partagent une liste de champs (Partie 6), et tout
verrouiller derrière magic + version (l'invariant du Partie 1,
appliqué).

---

## Exercice — Un Système de Sauvegarde de Tilemap
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

---

### Exercice — Construisez-le

Implémentez `save_map` / `load_map` pour la grille du City Builder en
utilisant les **visiteurs Writer / Reader** du Partie 6.

**Votre tâche :**

1. Écrire `Writer` / `Reader`, chacun avec un `make_field()` contraint
   par le concept `Serializable`.
2. Donner à `Tile` et `TileMap` un unique `serialize(V&)` chacun,
   contraint par le concept `FieldVisitor`.
3. Écrire un en-tête **numéro magique + version** avant la charge utile ;
   rejeter un mauvais magic et une version future au chargement.
4. Test aller-retour : `save_map(m, "t.sav"); load_map(m2, "t.sav");`
   puis `assert(m == m2)`.
5. **Bonus :** ajouter un champ `biome` gardé par `version >= 2` ;
   prouver qu'un fichier v1 se charge toujours avec le lecteur v2.

<small>Objectif : éprouver *pourquoi* la conception à une seule
fonction supprime la classe de bugs de désynchronisation — essayez d'en
introduire un et observez-le ne pas compiler.</small>

Note:
Le bonus est la vraie leçon : l'évolution versionnée est la contrainte
qui sépare un jouet d'un système de save. Si un fichier v1 se charge
proprement sous du code v2, la conception est saine.

---

## Synthèse
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Quelle Solution, Quand

| Situation | À utiliser |
|---|---|
| Tableau en masse de POD trivialement copiables | **Mémoire brute** (Sol. 1) |
| Production, graphe complexe, dépendance acceptable | **Boost** (Sol. 2) |
| Besoin de contrôle / aucune dépendance sur vos propres types | **Patron Visiteur** (Sol. 3) |
| Données réseau entre machines | binaire + ordre des octets réseau |
| Config / petite save / diff-able dans git | format texte |

### Toujours

- Numéro magique + **version** avant toute charge utile.
- Une seule liste de champs, utilisée dans les deux sens (pas de
  dérive save/load).
- Types à largeur fixe & ordre réseau pour tout binaire sur le réseau.

---

## Ressources
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- 📘 [isocpp.org — FAQ Sérialisation](https://isocpp.org/wiki/faq/serialization)
- 📘 [SJSU — Cours C++ Serialization (pointer swizzling)](https://www.cs.sjsu.edu/faculty/pearce/parties/lectures/cpp/advanced/Serialization.htm)
- 📘 [Documentation Boost.Serialization](https://www.boost.org/doc/libs/release/libs/serialization/doc/index.html)
- 💻 [Boost.Serialization `demo.cpp`](https://www.boost.org/doc/libs/1_36_0/libs/serialization/example/demo.cpp)
- 📺 CppCon 2022 — Yu Qi, *A Faster Serialization Library Based on Compile-time Reflection & C++20*
- 📺 CppCon 2022 — Eyal Zedaka, *Killing C++ Serialization Overhead & Complexity*

---

# Questions ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>Suite : brancher les visiteurs Writer / Reader sur la tilemap du City Builder.</small>
