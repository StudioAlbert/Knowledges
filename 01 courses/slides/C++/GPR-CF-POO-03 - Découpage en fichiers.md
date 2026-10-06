---
title: GPR-CF-POO-03 - Découpage en fichiers
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

# Découpage en fichiers
<!-- .slide: class="title" -->

### Ce qu'on promet, et où on le tient

<small>GPR-CF-POO-03 · Programmation Orientée Objet</small>

Note:
Troisième séance du bloc. La classe de POO-02 vit encore dans `main.cpp`. On la
sort, on apprend ce que fait vraiment `#include`, et pourquoi un en-tête se
protège.

---

## Objectifs

À la fin de la séance, vous savez :

- séparer une classe en **`.h`** et **`.cpp`**
- expliquer ce que fait vraiment `#include`
- protéger un en-tête de la **double inclusion**
- décider ce qui se montre, et ce qui reste caché

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-02 - Classes et visibilité|GPR-CF-POO-02]].

---

# Pourquoi découper
<!-- .slide: class="title" -->

---

## Un seul fichier, jusqu'au jour où

À 800 lignes, `main.cpp` pose trois problèmes :

- on ne **retrouve** plus rien
- deux personnes ne peuvent plus y travailler **en même temps** sans conflit
- la moindre virgule fait **tout recompiler**

Le découpage ne rend pas le code plus intelligent. Il le rend **praticable**.

Note:
Le deuxième point parle directement de GTE-02 : deux branches qui touchent le
même fichier de 800 lignes, c'est un conflit garanti à chaque merge.

---

## Un concept, un duo de fichiers

- `Joueur.h` + `Joueur.cpp`
- `Vector2.h` + `Vector2.cpp`
- `main.cpp`, qui n'a pas d'en-tête : personne n'a besoin de l'inclure

La règle tient en une phrase : **un concept du jeu, un duo de fichiers**.

---

# Ce que fait vraiment `#include`
<!-- .slide: class="title" -->

---

## Le header promet, le source tient

```cpp
// Joueur.h — ce qui existe
#pragma once
#include <string>

class Joueur
{
public:
    void subirDegats(int degats);
    bool estVivant() const;

private:
    std::string nom_ = "Kael";
    int pointsDeVie_ = 100;
};
```

L'en-tête **annonce**. Il ne dit pas comment.

---

## Le source tient la promesse

```cpp
// Joueur.cpp — comment ça marche
#include "Joueur.h"

#include <algorithm>

void Joueur::subirDegats(int degats)
{
    pointsDeVie_ = std::max(0, pointsDeVie_ - degats);
}

bool Joueur::estVivant() const
{
    return pointsDeVie_ > 0;
}
```

`Joueur::` dit à quelle classe appartient la méthode.

Note:
Trois choses à montrer au tableau : le `Joueur::` devant chaque nom, le `const`
qui se répète dans les deux fichiers, et le `#include <algorithm>` qui reste
dans le `.cpp` — personne d'autre n'a besoin de le savoir.

---

## Une inclusion est un copier-coller
<!-- .slide: class="schema" -->

Le compilateur ne voit pas vos fichiers : il voit un seul long fichier.

![[poo03_unite_compilation.svg]]

---

## Quand le même en-tête arrive deux fois

```cpp
#include "Vector2.h"
#include "Vector2.h"     // par deux chemins différents, dans un vrai projet
```

```text
error C2011: 'Vector2' : redéfinition du type 'struct'
```

Le copier-coller a eu lieu **deux fois** : la classe est déclarée deux fois, et
le compilateur refuse.

Note:
Vérifié au compilateur. Dans un vrai projet personne n'écrit deux fois la même
ligne : `main.cpp` inclut `Joueur.h` et `Salle.h`, qui incluent tous les deux
`Vector2.h`. Le résultat est le même.

---

## Gardes d'inclusion

```cpp
#pragma once                  // la version courte, partout aujourd'hui

// -- ou, en portable strict --
#ifndef VECTOR2_H
#define VECTOR2_H
struct Vector2 { float x, y; };
#endif // VECTOR2_H
```

La garde fait **ignorer** la deuxième lecture. Première ligne de **tout** en-tête,
sans exception.

---

# Ce qui va où
<!-- .slide: class="title" -->

---

## Ce qui va dans l'en-tête

- la **classe**, ses attributs, la **signature** de ses méthodes
- les `#include` dont la **déclaration** a besoin — ici `<string>`, pour `nom_`
- rien d'autre

Tout ce qui est dans l'en-tête est recopié chez **tous** ceux qui l'incluent.

---

## Ce qui reste dans le source

- le **corps** des méthodes
- les `#include` dont seul le code a besoin — `<algorithm>`, `<print>`
- les fonctions d'aide que personne d'autre ne doit voir

Changer un corps de méthode ne fait recompiler que **ce fichier**.

Note:
C'est le même raisonnement que `private` en POO-02, un cran au-dessus : moins
l'extérieur en sait, moins il est touché quand ça change.

---

## Deux façons d'inclure

```cpp
#include <string>      // la bibliothèque : chevrons
#include "Joueur.h"    // votre projet : guillemets
```

- les **chevrons** cherchent dans les dossiers du compilateur
- les **guillemets** cherchent d'abord à côté du fichier courant
- ordre conseillé : son propre en-tête, puis la bibliothèque, puis le reste

---

## Inclure le moins possible

Un en-tête qui inclut tout fait recompiler tout le projet au moindre changement.

- dans l'en-tête : seulement ce que la **déclaration** exige
- un attribut par **valeur** → il faut le type complet
- un **pointeur** ou une **référence** → une simple annonce suffit

---

## Forward declaration

```cpp
// Joueur.h
#pragma once

class Arme;            // « Arme existe » — et rien de plus

class Joueur
{
public:
    void equiper(Arme* arme);

private:
    Arme* arme_ = nullptr;
};
```

Le `#include "Arme.h"` descend alors dans `Joueur.cpp`, où le code en a vraiment besoin.

Note:
C'est aussi la seule sortie quand deux classes se connaissent mutuellement :
`Joueur` connaît son `Arme`, `Arme` connaît son porteur. Deux `#include`
croisés ne compilent jamais ; une annonce de chaque côté, si.

---

# Le projet suit
<!-- .slide: class="title" -->

---

## Le `CMakeLists.txt`

```cmake
add_executable(Donjon
    main.cpp
    Joueur.cpp
    Vector2.cpp
)
```

- chaque **`.cpp`** ajouté se déclare ici
- les **`.h`** n'y apparaissent pas : ils ne se compilent pas tout seuls
- oublier un `.cpp`, c'est une erreur de l'**éditeur de liens**, pas du compilateur

---

## Deux familles d'erreurs

| Le message | Qui parle | Ce qui manque |
| --- | --- | --- |
| `error C2065 : identificateur non déclaré` | le **compilateur** | la **déclaration** — un `#include` oublié |
| `error LNK2019 : symbole externe non résolu` | l'**éditeur de liens** | la **définition** — un `.cpp` oublié, ou un corps jamais écrit |

```text
LNK2019: symbole externe non résolu "public: void Joueur::subirDegats(int)"
         référencé dans la fonction main
```

Note:
Vérifié au compilateur. Savoir lire laquelle des deux on a sous les yeux fait
gagner un quart d'heure à chaque fois : le compilateur se plaint d'un fichier
et d'une ligne, l'éditeur de liens d'un `.obj` et d'un symbole.

---

## Atelier — 20 min

Sortir la classe `Joueur` de `main.cpp` :

1. créer `Joueur.h` et `Joueur.cpp`, avec `#pragma once`
2. déplacer la déclaration dans l'en-tête, les corps dans le source
3. ajouter `Joueur.cpp` au `CMakeLists.txt`, et recompiler
4. retirer la garde, recompiler, **lire l'erreur**, puis la remettre

Exercices 1 et 2 de la feuille ; le 5 est le bilan, à finir à la maison.

---

## À retenir

- **un concept, un duo de fichiers** — et une garde par en-tête
- `#include` est un **copier-coller** : tout ce qui est dans l'en-tête se propage
- dans l'en-tête, seulement ce que les autres doivent savoir
- compilateur = déclaration manquante &nbsp;·&nbsp; éditeur de liens = définition manquante

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/C++/GPR-CF-POO-04 - Cycle de vie de l'objet|GPR-CF-POO-04]] — naître et mourir proprement.</small>
