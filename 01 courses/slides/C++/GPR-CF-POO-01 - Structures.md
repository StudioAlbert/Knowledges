---
title: GPR-CF-POO-01 - Structures
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Programmation Orientée Objet
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: online
---

# Structures
<!-- .slide: class="title" -->
## GPR-CF-POO-01

<small>Ranger ensemble ce qui va ensemble</small>

Note:
Première séance du bloc POO. On part d'un besoin très concret — regrouper les données
d'un ennemi — et on s'arrête à la comparaison `struct` / `class`. Les méthodes, le
découpage `.h` / `.cpp` et les constructeurs viennent en POO-02 à POO-04.
Source : `01.03 - Basics OOP`, partie *Structures* et début de *Class*.

---

## Objectifs

- déclarer une structure, et comprendre qu'elle devient un **type**
- en créer des **instances**, les initialiser, lire et écrire leurs champs
- passer une structure à une fonction **sans la recopier**
- savoir ce qui distingue une `struct` d'une `class`

**Prérequis :** variables, fonctions, tableaux — [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05]].

---

## Six variables pour un seul ennemi

Tout ce qui décrit un gobelin, rangé dans des variables séparées : et pour le deuxième gobelin ?

```cpp
std::string nom = "Gobelin";
int   pv      = 30;
int   degats  = 5;
float vitesse = 2.5f;
float posX    = 0.0f;
float posY    = 0.0f;

// un deuxième gobelin : nom2, pv2, degats2, vitesse2, posX2, posY2…
```

Note:
Faire compter : 10 gobelins = 60 variables, et rien dans le code ne dit que `pv2` va avec
`nom2`. Les entités du jeu — ennemis, joueurs, bâtiments — portent toutes plusieurs
valeurs qui vont ensemble.

---

## Regrouper
<!-- .slide: class="schema" -->

Une structure donne un nom au groupe : le lien entre les valeurs est écrit dans le code.

![[poo01_regrouper.svg]]

---

## Une structure, un concept du jeu

- une `struct` donne un **nom** à un groupe de valeurs
- ce nom devient un **type**, comme `int` ou `std::string`
- un type par concept : `Ennemi`, `Joueur`, `Batiment`, `Arme`
- chaque valeur du groupe s'appelle un **champ**, ou **membre**

---

## Déclarer

La déclaration décrit la forme : elle ne réserve aucune mémoire et ne contient aucune valeur.

```cpp
#include <string>

struct Ennemi
{
    std::string nom;
    int pointsDeVie;
    int defense;
    int attaque;
};   // ne pas oublier le ';'
```

Note:
Le `;` final est l'oubli classique : l'erreur du compilateur tombe alors sur la ligne
suivante, souvent dans un autre fichier. Convention : un nom de type commence par une
majuscule.

---

## Déclaration ou instance
<!-- .slide: class="schema" -->

Déclarer `struct Ennemi` ne crée aucun ennemi : il faut ensuite en instancier.

![[poo01_declaration_instances.svg]]

Note:
Vocabulaire à fixer : le **nom de la structure** (`Ennemi`) est le plan ; le **nom de
l'objet** (`gobelinA`) est ce qu'on manipule vraiment.

---

## Instancier

Chaque instance a ses propres valeurs : deux gobelins partagent leur forme, pas leurs points de vie.

```cpp
Ennemi gobelinA{ "Gobelin", 30, 2, 5 };   // valeurs dans l'ordre des champs
Ennemi gobelinB{ "Gobelin", 30, 2, 5 };

gobelinA.pointsDeVie -= 10;               // seul A est blessé

std::println("{} / {}", gobelinA.pointsDeVie, gobelinB.pointsDeVie);   // 20 / 30
```

---

## Trois façons d'initialiser

L'ordre des champs, leur nom, ou un champ à la fois.

```cpp
Ennemi alien{ "Xénomorphe", 100, 10, 10 };                                  // dans l'ordre

Ennemi orc{ .nom = "Orc", .pointsDeVie = 60, .defense = 5, .attaque = 8 };  // par nom (C++20)

Ennemi troll;                                                              // champ par champ
troll.nom         = "Troll";
troll.pointsDeVie = 120;
troll.defense     = 8;
troll.attaque     = 12;

Ennemi vide{};                                                             // tout à zéro, nom vide
```

Note:
Liste d'initialisation : les valeurs doivent suivre l'ordre de la déclaration. Les
initialiseurs nommés (`.champ = valeur`) sont du **C++20** — et doivent eux aussi suivre
l'ordre des champs. `Ennemi troll;` sans accolades laisse les `int` **non initialisés** :
toujours écrire `{}` si on ne remplit pas tout de suite.

---

## Accéder aux membres

Le point relie l'instance à son champ, et se lit de gauche à droite : « les points de vie de l'alien ».

```cpp
int pvJoueur      = 100;
int attaqueJoueur = 10;

Ennemi alien{ "Xénomorphe", 100, 10, 10 };

pvJoueur          -= alien.attaque;    // l'alien frappe
alien.pointsDeVie -= attaqueJoueur;    // le joueur riposte

std::println("PV du joueur : {}, PV de l'alien : {}", pvJoueur, alien.pointsDeVie);   // 90, 90
```

---

## Une structure dans une structure

Un `Transform` contient deux `Vector2` : on décrit un objet de jeu en emboîtant.

```cpp
struct Vector2    { float x; float y; };
struct Transform  { Vector2 position; Vector2 echelle; };
struct Personnage { std::string nom; Transform transform; };

Personnage heros{ "Aldric", { { 2.0f, 5.0f }, { 1.0f, 1.0f } } };
heros.transform.position.x += 1.5f;    // on lit les points de gauche à droite

std::println("{} est en ({}, {})", heros.nom,
             heros.transform.position.x, heros.transform.position.y);   // Aldric est en (3.5, 5)
```

Note:
C'est exactement la forme du `Transform` de Unity : position, rotation, échelle, chacune
un vecteur. Les accolades imbriquées suivent l'imbrication des structures.

---

## Passer à une fonction

Par valeur, la fonction travaille sur une copie ; par référence, elle modifie l'original.

```cpp
void soigner(Ennemi e)          { e.pointsDeVie += 20; }   // copie : l'original ne bouge pas
void soignerVraiment(Ennemi& e) { e.pointsDeVie += 20; }   // référence : l'original change

void afficher(const Ennemi& e)                              // lecture seule, sans copie
{
    std::println("{:8} PV {:3}  ATK {:2}", e.nom, e.pointsDeVie, e.attaque);
}

Ennemi g{ "Gobelin", 10, 2, 5 };
soigner(g);            // g.pointsDeVie vaut toujours 10
soignerVraiment(g);    // 30
```

Note:
Règle à donner : `Type&` quand la fonction modifie, `const Type&` quand elle lit
seulement, par valeur pour les petits types (`int`, `float`). Une structure peut être
grosse : la copier à chaque appel coûte.

---

## Un tableau de structures

Une vague d'ennemis est un tableau d'`Ennemi`, parcouru comme n'importe quel tableau.

```cpp
Ennemi vague[3]{ { "Gobelin", 30, 2, 5 }, { "Orc", 60, 5, 8 }, { "Troll", 120, 8, 12 } };

for (Ennemi& e : vague)          // & : on modifie chaque ennemi
{
    e.pointsDeVie -= 25;         // une boule de feu touche toute la vague
}
for (const Ennemi& e : vague)    // const & : on lit seulement
{
    afficher(e);                 // Gobelin  PV   5 …
}
```

---

# Et `class` ?
<!-- .slide: class="title" -->

---

## `class` : une struct, à un détail près

La seule différence entre `struct` et `class` : la **visibilité par défaut** de leurs membres.

```cpp
struct Ennemi
{
    /* public: */      // tout est visible de l'extérieur
    std::string nom;
};

class Ennemi
{
    /* private: */     // rien n'est visible de l'extérieur
    std::string nom;
};
```

---

## Visibilité

- `public:` — accessible depuis l'intérieur **et** l'extérieur
- `private:` — accessible **seulement** depuis l'intérieur
- une `struct` commence en `public:`, une `class` en `private:`
- on peut changer de visibilité à tout moment, dans l'une comme dans l'autre

Note:
`protected:` existe aussi : comme `private` vu de l'extérieur, il ne prend son sens qu'avec
l'héritage (POO-06). L'intérêt de `private` — exposer des méthodes plutôt que des données —
est le sujet de POO-02.

---

## Le compilateur vérifie

L'accès à un membre privé ne compile pas : la visibilité se constate à la compilation, pas à l'exécution.

```cpp
class Ennemi { int pointsDeVie; };

struct Coffre
{
private:                  // une struct peut aussi cacher ses membres
    int contenu;
};

Ennemi e;
e.pointsDeVie = 30;       // erreur : 'int Ennemi::pointsDeVie' is private within this context
Coffre c;
c.contenu = 3;            // erreur : 'int Coffre::contenu' is private …
```

Note:
Messages de GCC 14. MSVC : « C2248 : impossible d'accéder à un membre private ». Usage
courant : `struct` pour un agrégat de données sans comportement (`Vector2`, `Ennemi` ici),
`class` dès qu'il y a des méthodes et des données à protéger — la suite, en POO-02.

---

## Atelier — 20 min

Décrire le monstre du jeu en une structure, en instancier trois, et écrire la fonction qui affiche sa fiche.

Note:
Énoncés : [[01 courses/exercises/C++/GPR-CF-POO-01 - Structures|GPR-CF-POO-01 — Exercices]].
En classe, viser les exercices 1 à 4 ; le bestiaire se termine à la maison.

---

## À retenir

- une structure nomme un **concept du jeu** et devient un type
- la déclaration **décrit**, l'instance **contient**
- `Type&` pour modifier, `const Type&` pour lire : jamais de copie inutile
- `struct` et `class` : même outil, visibilité par défaut différente

---

## Questions ?
