---
title: Fonctions
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Bases de la Programmation
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: true
---

# Fonctions
<!-- .slide: class="title" -->

### Écrire une fois, appeler partout

<small>GPR-CF-BDP-03 · Bases de la Programmation</small>

Note:
On sait écrire des variables et des opérations dans `main`. Cette séance
apprend à ranger ce code en blocs nommés et réutilisables : c'est la
première vraie brique d'un programme lisible.

---

## Objectifs

À la fin de la séance, vous savez :

- expliquer **pourquoi** on découpe un programme en fonctions
- lire et écrire une **signature** : type de retour, nom, paramètres
- dire ce qu'est la fonction **`main`** et ce que signifie sa valeur de retour
- **pré-déclarer** une fonction pour l'utiliser avant sa définition
- **surcharger** une fonction : même nom, paramètres différents

**Prérequis :** variables, types de base et opérations — [[01 courses/slides/C++/GPR-CF-BDP-02 - Premières lignes de C++|GPR-CF-BDP-02]].

---

# Signature, paramètres, retour
<!-- .slide: class="title" -->

---

## Anatomie d'une fonction

```cpp
Type-de-retour  nom (paramètres)
{
    return valeur;
}
```

| Partie         | Rôle                                        | Exemple                       |
| -------------- | ------------------------------------------- | ----------------------------- |
| type de retour | ce que la fonction renvoie                  | `int`, `float`, `void` (rien) |
| nom            | ce qu'elle fait, en verbe                   | `calculer_degats`             |
| paramètres     | ce qu'elle reçoit, séparés par des virgules | `int force, int armure`       |
| **signature**  | nom + types des paramètres                  | `calculer_degats(int, int)`   |

---

## Paramètres et valeur de retour

```cpp
int degats_finaux(int attaque, int armure)   // deux paramètres
{
    int resultat = attaque - armure;
    if (resultat < 0)
        return 0;                            // return arrête la fonction
    return resultat;
}

void afficher_vie(int vie)                   // void : ne renvoie rien
{
    std::cout << "Vie : " << vie << "\n";
}
```

- les paramètres sont des **copies** : modifier `attaque` dans la fonction ne change pas la variable de l'appelant
- une fonction non `void` doit **toujours** atteindre un `return`

Note:
Le passage par référence (`int&`) viendra plus tard. Pour l'instant, on
retient qu'une fonction reçoit des copies et communique son résultat par
`return`.

---

# La fonction `main`
<!-- .slide: class="title" -->

---

## `main` : le point d'entrée

```cpp
#include <iostream>

void main() { }        // ??? refusé par la norme

int main() { }         // valide : return 0 implicite

int main(int ac, char** av)
{
    std::cout << "Hello World!\n";
    return 0;
}
```

- le programme commence **toujours** par `main`, et s'arrête quand elle se termine
- elle renvoie un `int` au système : **0** = tout s'est bien passé, autre chose = erreur
- la forme `(int ac, char** av)` reçoit les arguments de la ligne de commande

Note:
`void main()` compile sous MSVC par tolérance, mais n'est pas du C++
standard. `main` est la seule fonction non `void` où l'on peut omettre le
`return` : il vaut alors 0.

---
## Le problème

```cpp
int main()
{
    int degats_epee = 12 * 2 - 3;
    std::cout << "Épée : " << degats_epee << "\n";

    int degats_hache = 15 * 2 - 3;
    std::cout << "Hache : " << degats_hache << "\n";

    int degats_arc = 9 * 2 - 3;
    std::cout << "Arc : " << degats_arc << "\n";
}
```

La règle « × 2 − 3 » est écrite trois fois. Le jour où elle change, il faut penser à la corriger **partout**.

---

# Pourquoi découper
<!-- .slide: class="title" -->

---

## Pourquoi utiliser des fonctions ?

- **ne jamais copier-coller** du code : une règle, un seul endroit
- **encapsuler** une routine : on l'utilise sans relire son contenu
- **nommer** une intention : `calculer_degats(force)` se lit mieux que `force * 2 - 3`
- **tester** une petite partie du programme à la fois

---

## Le même programme, découpé

```cpp
int calculer_degats(int force)
{
    return force * 2 - 3;
}

int main()
{
    std::cout << "Épée : "  << calculer_degats(12) << "\n";
    std::cout << "Hache : " << calculer_degats(15) << "\n";
    std::cout << "Arc : "   << calculer_degats(9)  << "\n";
}
```

La règle change ? **Une** ligne à modifier.

---
# Pré-déclaration
<!-- .slide: class="title" -->

---

## Déclarer avant d'utiliser

Le compilateur lit le fichier **de haut en bas** : une fonction doit être connue avant d'être appelée.

```cpp
int compute_value(int a, int b);   // déclaration : la signature, suivie de ;

int main()
{
    return compute_value(12, 42);  // OK : déjà déclarée
}

int compute_value(int a, int b)    // définition : le corps
{
    return a + b;
}
```

Note:
Sans la première ligne, MSVC répond « identificateur introuvable ». La
déclaration est une promesse : « cette fonction existe, son corps est plus
loin ». C'est exactement ce qu'on mettra dans les fichiers `.h`.

---

## Syntaxe alternative (pour info)

Il existe une « nouvelle » façon de déclarer les fonctions. Elle est valide, mais pas encore la façon recommandée de le faire.

```cpp
int  compute_value(int a, int b);

auto compute_value(int a, int b) -> int;
```

Les deux lignes déclarent **la même** fonction : le type de retour est simplement écrit à la fin.

---

# Surcharge
<!-- .slide: class="title" -->

---

## Même nom, paramètres différents

```cpp
int   maximum(int a, int b)          { return a > b ? a : b; }
float maximum(float a, float b)      { return a > b ? a : b; }
int   maximum(int a, int b, int c)   { return maximum(maximum(a, b), c); }

int main()
{
    maximum(3, 7);          // appelle la version (int, int)
    maximum(2.5f, 1.0f);    // appelle la version (float, float)
    maximum(4, 9, 1);       // appelle la version à 3 paramètres
}
```

Le compilateur choisit selon le **nombre** et le **type** des arguments.

---

## Les limites de la surcharge

- le type de retour **ne suffit pas** à distinguer deux fonctions :

```cpp
int   lire_valeur();
float lire_valeur();     // erreur : même signature
```

- attention aux appels **ambigus** :

```cpp
maximum(3, 2.5f);        // erreur : (int, int) ou (float, float) ?
```

Note:
Les deux conversions sont aussi valables l'une que l'autre, le compilateur
refuse de choisir. On corrige en rendant le type explicite : `3.0f`.

---

# Clôture
<!-- .slide: class="title" -->

---

## À retenir

- une fonction évite le copier-coller et **nomme** une intention
- signature = nom + types des paramètres ; `void` si rien n'est renvoyé
- les paramètres sont des **copies**, le résultat sort par `return`
- `main` est le point d'entrée et renvoie **0** si tout va bien
- déclarer **avant** d'appeler ; surcharger = même nom, paramètres différents

---

## Exercices

- **la calculette** : écrire, surcharger et combiner des fonctions
- **le combat de monstres** : découper un `main` monolithique en fonctions

Énoncés : [[01 courses/exercises/C++/GPR-CF-BDP-03 - Fonctions]]
