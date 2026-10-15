---
title: GPR-CF-POO-05 - Static et surcharge d'opérateur
type: slides
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
---

# Static et surcharge d'opérateur
<!-- .slide: class="title" -->

### Ce qui appartient à la classe, et ce qui se lit comme des maths

<small>GPR-CF-POO-05 · Programmation Orientée Objet</small>

Note:
Avant-dernière séance du bloc. Deux sujets sans rapport l'un avec l'autre, mais
qui répondent à la même envie : écrire ce qu'on veut dire, à l'endroit où ça a un
sens.

---

## Objectifs

À la fin de la séance, vous savez :

- dire ce qu'un membre **`static`** partage, et avec qui
- le **définir** là où il faut, et reconnaître l'erreur quand vous l'oubliez
- donner à une classe les **opérateurs** qui rendent le code lisible
- choisir entre **méthode membre** et **fonction libre**

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-04 - Cycle de vie de l'objet|GPR-CF-POO-04]].

---

# Ce qui appartient à la classe
<!-- .slide: class="title" -->

---

## Combien d'ennemis vivants ?

La question ne concerne **aucun** ennemi en particulier.

- la mettre dans un ennemi : chacun aurait son propre compteur
- la mettre en variable globale : n'importe qui peut la fausser
- la mettre **dans la classe, hors des objets** : c'est `static`

Note:
Faire poser la question à la classe avant de donner la réponse : où écririez-vous
ce compteur ? La variable globale est la réponse spontanée, et c'est l'occasion
de dire ce qui ne va pas avec — personne ne garantit plus qu'elle soit juste.

---

## L'attribut `static`

```cpp
class Monstre
{
public:
    Monstre()  { ++vivants_; }
    ~Monstre() { --vivants_; }

    static int vivants() { return vivants_; }

private:
    static int vivants_;      // une seule case, pour toute la classe
};
```

Le constructeur et le destructeur de POO-04 tiennent le compteur à jour tout seuls.

---

## Une case, pas une par objet
<!-- .slide: class="schema" -->

Trois objets, trois `pointsDeVie_` — et un seul `vivants_`.

![[poo05_static_partage.svg]]

---

## Ce que ça donne

```text
Monstre a;
{
    Monstre b, c;
    Monstre::vivants()   ->  3
}
Monstre::vivants()       ->  1
```

Le compteur suit les portées de POO-04, sans qu'on lui demande rien.

Note:
Sortie réelle, vérifiée au compilateur. Noter l'appel : `Monstre::vivants()`, sur
la **classe**, sans objet. `a.vivants()` compile aussi, et c'est trompeur : ça
laisse croire que la réponse dépend de `a`.

---

## Où il se définit

```cpp
// monstre.h
class Monstre
{
    static int vivants_;      // la déclaration : « il existe »
};

// monstre.cpp
int Monstre::vivants_ = 0;    // la définition : la case, et sa valeur
```

Déclarer ne réserve rien. La case existe **une fois**, donc dans **un seul** source.

---

## L'oubli classique

```text
error LNK2019: symbole externe non résolu
               "private: static int Monstre::vivants_"
               référencé dans la fonction "Monstre::Monstre(void)"
fatal error LNK1120: 1 externes non résolus
```

L'**éditeur de liens**, comme en POO-03 : la déclaration était là, la définition
manquait.

---

## La méthode `static`

- s'appelle sur la **classe**, pas sur un objet
- n'a donc **pas de `this`**
- ne peut toucher que les membres `static`
- sert d'usine, de compteur, de conversion — jamais de fourre-tout

`Monstre::vivants()` a un sens. `Monstre::soigner()` n'en a aucun : qui soigner ?

---

## `static` n'est pas une globale déguisée

Elle en garde les défauts : une seule valeur pour tout le programme, et tout le
monde la voit changer.

- bon pour ce qui est **vraiment unique** : un compteur, une constante
- mauvais pour ce qui est « pratique à atteindre d'ici »
- ingérable en test : deux tests partagent la même case

Note:
C'est la porte d'entrée du singleton, qu'on verra en Unity (APU-06). La question
à garder : est-ce unique par nature, ou juste unique pour l'instant ?

---

# Les opérateurs
<!-- .slide: class="title" -->

---

## Avant

```cpp
Vector2 position = Ajouter(position, Multiplier(vitesse, dt));
```

On lit l'appel de fonction, pas le calcul. Pourtant tout le monde sait écrire :

<p class="formule">position = position + vitesse · dt</p>

---

## `operator+`

```cpp
struct Vector2
{
    float x = 0.0f;
    float y = 0.0f;

    Vector2 operator+(const Vector2& autre) const
    {
        return {x + autre.x, y + autre.y};
    }
};

const Vector2 c = a + b;      // (4, 5) pour (3,4) + (1,1)
```

Un nom de méthode un peu spécial, et rien de plus.

---

## Membre ou fonction libre

```cpp
Vector2 operator*(float k) const;              // membre : v * 2.0f
Vector2 operator*(float k, const Vector2& v);  // libre  : 2.0f * v
```

```text
error C2677: '*' binaire : aucun opérateur global trouvé
             qui accepte le type 'Vector2'
```

La méthode membre impose **l'objet à gauche**. Pour `2.0f * v`, il faut une
fonction libre.

---

## Comparer

```cpp
struct Vector2
{
    float x = 0.0f;
    float y = 0.0f;

    bool operator==(const Vector2&) const = default;
};

std::ranges::find(positions, cible);   // marche, maintenant
```

`= default` demande au compilateur de comparer champ à champ. `==` et `<` sont ce
que la bibliothèque standard attend pour chercher et pour trier.

Note:
Depuis C++20, `operator<=>` donne les quatre comparaisons d'ordre d'un coup, et
`= default` marche aussi dessus. À mentionner, sans y passer du temps : ce qui
compte ici, c'est que `find` et `sort` ne demandent pas une méthode à nous, mais
les opérateurs attendus.

---

## Les pièges

- on ne surcharge que ce qui **va de soi** : `+` additionne, point
- un opérateur qui surprend coûte plus cher qu'une méthode bien nommée
- `a + b` ne doit modifier ni `a` ni `b` — d'où le `const`
- il n'y a pas d'opérateur « attaquer » : ça, ça se nomme

---

## Atelier — 20 min

Reprendre `Vector2`, et lui donner ce qui lui manque.

1. `operator+`, puis `operator*` par un scalaire — **des deux côtés**
2. `operator==` en `= default`, et le vérifier avec `std::ranges::find`
3. un compteur `static` d'instances créées, tenu par le constructeur
4. afficher le compteur après une boucle qui crée 100 vecteurs dans une portée

---

## À retenir

- `static` appartient à la **classe** : une case, déclarée dans le `.h`, définie
  dans **un** `.cpp`
- une méthode `static` n'a pas de `this`, donc pas d'objet
- un opérateur ne s'écrit que s'il **va de soi** ; sinon, une méthode nommée
- `==` et `<` sont la porte d'entrée de `find` et de `sort`

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme|GPR-CF-POO-06]] — écrire une fois ce que plusieurs classes ont en commun.</small>
