---
title: GPR-CF-POO-06 - Héritage et polymorphisme
type: slides
status: To check
subject: C++
duration_h: 1
bloc_gsda: Programmation Orientée Objet
specialisation: C++ Fondamentaux
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: draft
---

# Héritage et polymorphisme
<!-- .slide: class="title" -->

### Un seul appel, plusieurs comportements

<small>GPR-CF-POO-06 · Programmation Orientée Objet</small>

Note:
Dernière séance du bloc POO. On a une classe qui tient ses règles (POO-02), qui
vit dans ses fichiers (POO-03), qui naît et meurt proprement (POO-04). Reste à
écrire **une fois** ce que plusieurs classes ont en commun.

---

## Objectifs

À la fin de la séance, vous savez :

- **factoriser** ce que plusieurs classes ont en commun
- dire ce que **`virtual`** change au moment de l'appel
- écrire une **classe abstraite**, et dire à quoi elle sert
- reconnaître les deux pièges : le **diamant** et le **destructeur**

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-05 - Static et surcharge d'opérateur|GPR-CF-POO-05]].

---

# Hériter
<!-- .slide: class="title" -->

---

## Trois ennemis, 80 % de code identique

```cpp
class Gobelin
{
public:
    void avancer(float dt);        // identique
    void subirDegats(int degats);  // identique
    void attaquer();               // 3 de dégâts
private:
    int pointsDeVie_ = 30;         // identique
};

class Golem { /* les trois mêmes, et attaquer() à 12 */ };
class Archer { /* les trois mêmes, et attaquer() à 5  */ };
```

Un bug dans `subirDegats`, c'est **trois** corrections — et une qu'on oublie.

---

## La base

```cpp
class Monstre
{
public:
    Monstre(std::string nom, int pointsDeVie);
    void subirDegats(int degats);
    void afficher() const;

protected:
    int pointsDeVie_;      // les enfants y accèdent

private:
    std::string nom_;      // les enfants, non
};
```

`protected`, c'est « privé, sauf pour mes enfants ».

---

## L'enfant

```cpp
class Dragon : public Monstre
{
    using Monstre::Monstre;        // on hérite aussi des constructeurs

public:
    void cracherDuFeu()
    {
        pointsDeVie_ -= 5;                   // protected : d'accord
        std::println("{} crache", nom_);     // private : refusé
    }
};
```

```text
error C2248: 'Monstre::nom_' : impossible d'accéder à private membre
             déclaré(e) dans la classe 'Monstre'
```

---

## Les deux points à retenir

- un dragon **est un** monstre — pas « a un », c'est une autre histoire
- le constructeur du **parent** s'exécute avant celui de l'enfant
- `using Monstre::Monstre;` évite de recopier les constructeurs
- `protected` ouvre aux enfants ce que `private` ferme à tout le monde

Note:
« Est un » est le test qui décide. Un dragon est un monstre : héritage. Un
monstre a une arme : attribut. Confondre les deux donne des hiérarchies qu'on ne
peut plus défaire — on y revient en TC-FT-PCL-04, composition contre héritage.

---

## Le mode d'héritage

```cpp
class A {
public:    int x;
protected: int y;
private:   int z;
};

class B : public A    { /* x public,    y protected, z inaccessible */ };
class C : protected A { /* x protected, y protected, z inaccessible */ };
class D : private A   { /* x private,   y private,   z inaccessible */ };
```

Le mode ne fait que **réduire** la visibilité. `public` est le seul qui garde la
relation « est un » visible de l'extérieur.

---

## L'héritage multiple, et le diamant
<!-- .slide: class="schema" -->

Deux parents, un seul aïeul : l'enfant reçoit ses données en double.

![[poo06_diamant.svg]]

Note:
`virtual` sur l'héritage résout le diamant en C++, mais c'est une rustine : la
question à se poser est pourquoi deux parents portent des données. La réponse
tient presque toujours en une base et une interface.

---

# Choisir à l'exécution
<!-- .slide: class="title" -->

---

## Un seul tableau, plusieurs types

```cpp
std::vector<std::unique_ptr<Monstre>> vague;
vague.push_back(std::make_unique<Gobelin>("Gobelin", 30));
vague.push_back(std::make_unique<Dragon>("Smaug", 400));

for (const auto& monstre : vague)
    monstre->attaquer();
```

Le code ne sait pas ce qu'il tient. Il faut que **l'objet** décide.

---

## `virtual`

```cpp
class Monstre
{
public:
    virtual void attaquer() { std::println("Monstre attaque"); }
            void avancer()  { std::println("Monstre avance"); }
};

class Dragon : public Monstre
{
public:
    void attaquer() override { std::println("Dragon crache le feu"); }
    void avancer()           { std::println("Dragon vole"); }
};
```

Une seule méthode est `virtual`. L'autre est là pour la comparaison.

---

## Ce que ça change

```text
Monstre* m = new Dragon();

m->attaquer();   ->  Dragon crache le feu      (virtual)
m->avancer();    ->  Monstre avance            (pas virtual)
```

Même pointeur, même objet, deux lignes à côté. Sans `virtual`, c'est le type du
**pointeur** qui décide ; avec, c'est le type de l'**objet**.

Note:
Sortie réelle, vérifiée au compilateur. Tout le polymorphisme tient dans ces deux
lignes : les faire prédire avant de les afficher. `override` n'est pas obligatoire,
mais il fait dire au compilateur « cette méthode ne redéfinit rien » le jour où
une signature bouge.

---

## La classe abstraite

```cpp
class Monstre
{
public:
    virtual void attaquer() = 0;     // pas de corps : à la charge des enfants
    virtual ~Monstre() = default;
};

Monstre m;   // refusé
```

```text
error C2259: 'Monstre' : impossible d'instancier une classe abstraite
```

Une base qui ne promet qu'un **contrat**. Le refus est le but, pas un effet de bord.

---

## Le destructeur virtuel

```cpp
Monstre* m = new Dragon();
delete m;
```

```text
destructeur virtuel          destructeur ordinaire

~Dragon                      ~Monstre
~Monstre
```

Sans `virtual` sur le destructeur de la base, **`~Dragon` n'est jamais appelé** —
et tout ce que le dragon avait emprunté reste pris.

Note:
Sortie réelle, vérifiée au compilateur. MSVC ne dit rien, même en `/W4` : aucun
avertissement, aucun crash, juste une fuite silencieuse. D'où la règle sans
exception : une classe destinée à être héritée a un destructeur `virtual`.

---

## La formative

Un stand de tir. Cinq armes, cinq types, un menu de `1` à `5`.

- le companion donne **une** arme et **une** classe, sans parent
- en ajouter une deuxième par copier-coller suffit à poser le problème
- la contrainte : le menu ne teste **jamais** le type de l'arme
- le test final : une sixième arme, sans toucher ni la base ni le menu

Énoncé : [[01 courses/projects/C++/Formative - OOP - L'armurerie|Formative — l'armurerie]].

---

## À retenir

- l'héritage factorise ce qui est **commun** ; « est un », jamais « a un »
- `virtual` laisse l'**objet** décider, pas le pointeur
- la classe abstraite fixe un **contrat** qu'on ne peut pas instancier
- une base qu'on hérite a un **destructeur virtuel**, toujours

---

# Questions ?
<!-- .slide: class="title" -->

### Fin du bloc

<small>Six séances : la structure, la classe, les fichiers, la vie de l'objet, `static` et les opérateurs, et l'héritage.</small>
