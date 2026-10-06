# Exercices — GPR-CF-POO-03 — Découpage en fichiers

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-03 - Découpage en fichiers|GPR-CF-POO-03 - Découpage en fichiers]]

Tous les exercices partent du **même projet companion** : un mini jeu de donjon d'environ
300 lignes, entièrement dans un seul `main.cpp`. Il marche — il est juste illisible.

> Dossier : `01 courses/companion projects/C++/GPR-CF-POO-03 - Découpage en fichiers/`
> — ouvrir le `CMakeLists.txt` dans CLion, ou `cmake -S . -B build && cmake --build build`.

Quatre concepts y cohabitent, marqués par des bandeaux de commentaires :

| Concept | Ce qu'il porte | Dépend de |
|---|---|---|
| `Vector2` | une position, `Ajouter`, `Identiques`, `EnTexte` | rien |
| `Journal` | la liste des événements, et son affichage | rien |
| `Entite` | nom, vie, dégâts, position | `Vector2` |
| `Salle` | nom, description, position, son monstre | `Vector2`, `Entite` |

**La règle commune à tous les exercices : le jeu doit se comporter exactement pareil après
qu'avant.** Lancez-le une fois avant de commencer, et notez ce qu'il affiche.

## Courts — valider la compréhension

### 1 — Sortir une classe

> [!abstract] Objectifs
> le duo `.h` / `.cpp`, la garde, et le `CMakeLists.txt` qui suit

On commence par `Vector2`, qui ne dépend de personne.

1. Créer `Vector2.h` : `#pragma once` en première ligne, puis la structure et les
   **signatures** des trois fonctions.
2. Créer `Vector2.cpp` : `#include "Vector2.h"` en première ligne, puis les trois **corps**.
3. Les retirer de `main.cpp`, qui inclut désormais `"Vector2.h"`.
4. Ajouter `Vector2.cpp` au `CMakeLists.txt`. **Pas** le `.h`.
5. Recompiler et rejouer : même comportement, à la lettre.

> [!tip] De quoi `Vector2.h` a-t-il besoin ?
> `EnTexte` rend une `std::string` : la **signature** l'exige, donc `<string>` monte dans
> l'en-tête. `std::to_string` n'est utilisé que dans le corps : son inclusion reste dans le
> `.cpp`. C'est toute la question de l'exercice 3.

### 2 — Provoquer la double inclusion

> [!abstract] Objectifs
> voir de ses yeux ce que la garde empêche, et lire le message

1. Retirer le `#pragma once` de `Vector2.h`.
2. Inclure `"Vector2.h"` **deux fois** de suite dans `main.cpp`.
3. Recompiler, et **recopier l'erreur** dans le rendu.
4. L'expliquer en une phrase, en partant du schéma du cours.
5. Remettre la garde.

```text
error C2011: 'Vector2' : redéfinition du type 'struct'
```

> [!tip] Dans un vrai projet
> Personne n'écrit deux fois la même ligne. Mais `main.cpp` inclura bientôt `Entite.h`
> **et** `Salle.h`, qui incluent tous les deux `Vector2.h`. Le résultat est identique —
> et c'est pour ce cas-là que la garde existe.

### 3 — Ce qui n'a rien à faire dans un en-tête

> [!abstract] Objectifs
> trier ce qui doit monter dans l'en-tête et ce qui doit rester dans le source

En sortant `Journal`, écrivez volontairement ce `Journal.h` :

```cpp
#pragma once

#include <iostream>     // (a)
#include <string>
#include <vector>

using namespace std;    // (b)

class Journal
{
public:
    void ecrire(const string& ligne) { lignes_.push_back(ligne); }   // (c)
    void afficherTout() const;
    void afficherDernier() const;

private:
    vector<string> lignes_;
};
```

1. Dire pour **(a)**, **(b)** et **(c)** pourquoi c'est un problème — pas « c'est interdit »,
   mais *ce que ça provoque chez celui qui inclut cet en-tête*.
2. Corriger les trois.
3. `<vector>` et `<string>`, eux, doivent-ils rester ? Justifier.

> [!tip] Les trois réponses, en une ligne chacune
> **(a)** `<iostream>` n'est utilisé que par les corps : il fait recompiler plus lentement
> tous les fichiers qui incluent `Journal.h`, pour rien.
> **(b)** `using namespace std` dans un en-tête s'impose à **tout** fichier qui l'inclut,
> sans qu'il l'ait demandé — on ne décide pas à la place des autres.
> **(c)** un corps dans l'en-tête fait recompiler tous ses utilisateurs dès qu'on le change.
> **(3)** oui : `vector<string> lignes_` est un **attribut**, la déclaration en a besoin.

### 4 — L'en-tête qui mentait

> [!abstract] Objectifs
> distinguer une erreur du compilateur d'une erreur de l'éditeur de liens

1. Dans `Entite.h`, déclarer une méthode `void soigner(int soin);`.
2. **Ne pas l'implémenter.** Compiler. Que se passe-t-il ?
3. L'appeler depuis `main.cpp`. Compiler à nouveau.
4. Recopier le message, dire **qui** parle — compilateur ou éditeur de liens — et à quel
   moment l'erreur apparaît.
5. Même question si vous oubliez d'ajouter `Entite.cpp` au `CMakeLists.txt`.

```text
error LNK2019: symbole externe non résolu "public: void Entite::soigner(int)"
               référencé dans la fonction main
```

> [!tip] Pourquoi l'étape 2 ne produit rien
> Déclarer sans définir est parfaitement légal tant que **personne n'appelle**. L'éditeur de
> liens ne cherche que les symboles réellement utilisés. C'est la différence entre la
> *promesse* (l'en-tête) et le fait de la *tenir* (le source).

## Complet — reprendre toute la séance

### 5 — Découper le donjon

> [!abstract] Objectifs
> les quatre concepts, quatre duos de fichiers, inclusions minimales, et le projet à jour

Aller au bout du découpage, dans l'ordre des dépendances : `Vector2` et `Journal` d'abord,
puis `Entite`, puis `Salle`.

1. Quatre duos `.h` / `.cpp`, une garde par en-tête.
2. `main.cpp` ne garde que la fonction `main`, `salleEn` et `afficherAide`.
3. Dans chaque en-tête, **uniquement** les inclusions que la déclaration exige.
4. `CMakeLists.txt` à jour : quatre `.cpp` ajoutés, aucun `.h`.
5. Rejouer la partie notée au début : même affichage, même journal, même nombre
   d'événements.

**Le rendu** : le projet qui compile, **plus** le schéma des inclusions obtenues, dessiné à
la main — un rectangle par fichier, une flèche par `#include`.

> [!check] Grille d'auto-évaluation
>
> | Je sais… | Vérification |
> |---|---|
> | créer un duo `.h` / `.cpp` | quatre duos, et `main.cpp` n'a plus que trois fonctions |
> | protéger un en-tête | `#pragma once` en première ligne des quatre `.h` |
> | n'inclure que le nécessaire | `Vector2.h` n'inclut pas `<vector>`, `Journal.h` n'inclut pas `<iostream>` |
> | tenir le projet à jour | quatre `.cpp` dans `CMakeLists.txt`, aucun `.h` |
> | ne rien casser | la partie notée au début donne exactement le même affichage |
> | lire une erreur de lien | je sais dire, devant LNK2019, quel fichier manque |

## Difficile — se projeter

### 6 — La dépendance circulaire

> [!abstract] Objectifs
> la déclaration anticipée, ce qu'elle permet et ce qu'elle interdit

Ajouter une classe `Arme` au donjon. `Entite` doit connaître son arme, et `Arme` doit
connaître son porteur, pour le journal.

1. Écrire naïvement les deux en-têtes, chacun incluant l'autre. Compiler, et constater.
2. Résoudre par **déclaration anticipée** (`class Arme;`) et **pointeur** d'un côté.
3. De ce côté-là, que peut encore promettre l'en-tête ? Que ne peut-il plus faire ?
   Essayer d'appeler une méthode d'`Arme` depuis `Entite.h` et lire ce que dit le
   compilateur.
4. **Mesurer** : compiler le projet complet deux fois, une fois avec le `#include` dans
   l'en-tête, une fois avec l'annonce, et comparer les temps.

> [!tip] Ce que l'annonce permet
> Une déclaration anticipée suffit pour un **pointeur** ou une **référence** : leur taille
> est connue sans connaître le type. Elle ne suffit pas pour un attribut **par valeur**, ni
> pour appeler quoi que ce soit — le compilateur sait que le type existe, pas ce qu'il
> contient.
