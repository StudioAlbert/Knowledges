---
title: GPR-CF-POO-04 - Cycle de vie de l'objet
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

# Cycle de vie de l'objet
<!-- .slide: class="title" -->

### Naître dans un état valide, mourir en rangeant

<small>GPR-CF-POO-04 · Programmation Orientée Objet</small>

Note:
POO-02 a fermé la classe, POO-03 l'a sortie dans ses fichiers. Reste la question
qu'on avait laissée de côté : qui remplit les attributs au départ, et qui range
derrière ?

---

## Objectifs

À la fin de la séance, vous savez :

- écrire un **constructeur**, avec ou sans paramètres
- dire ce que désigne **`this`**
- prévoir l'**ordre** dans lequel les membres s'initialisent
- dire **quand** le destructeur passe, sans jamais l'appeler

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-02 - Classes et visibilité|GPR-CF-POO-02]].

---

# Naître
<!-- .slide: class="title" -->

---

## Un objet sans constructeur

```cpp
class Monstre
{
public:
    std::string nom;
    int pointsDeVie;
};

Monstre m;
std::println("{} : {} pv", m.nom, m.pointsDeVie);
```

`pointsDeVie` ne vaut pas 0 : il ne vaut **rien de précis**.

Note:
À montrer en direct. La valeur change d'une exécution à l'autre, ou ne change
pas, selon ce qui traînait dans la pile — c'est exactement ce qui rend ce bug
introuvable. La `std::string`, elle, se construit vide toute seule : elle a son
propre constructeur. L'`int` n'en a pas.

---

## Le constructeur par défaut

```cpp
class Monstre
{
public:
    Monstre()
    {
        nom_ = "Gobelin";
        pointsDeVie_ = 30;
    }

private:
    std::string nom_;
    int pointsDeVie_;
};
```

Même nom que la classe, **aucun type de retour**. Personne ne l'appelle : il part
tout seul, à la déclaration.

---

## Ce qu'il garantit

- un objet **jamais** à moitié construit
- la règle écrite **une fois**, pas à chaque création
- l'extérieur ne peut pas l'oublier : il n'y a pas d'autre chemin

---

## Construire avec des paramètres

```cpp
class Monstre
{
public:
    Monstre(std::string nom, int pointsDeVie)
    {
        nom_ = std::move(nom);
        pointsDeVie_ = pointsDeVie;
    }
};

Monstre gobelin{"Gobelin", 30};
Monstre troll{"Troll", 120};
```

Ce que le constructeur **exige** ne peut pas être oublié par celui qui crée l'objet.

---

## `this`

```cpp
Monstre(std::string nom, int pointsDeVie)
{
    this->nom_ = std::move(nom);
    this->pointsDeVie_ = pointsDeVie;
}
```

`this` est un **pointeur sur l'objet courant**, celui sur lequel la méthode a été
appelée. Il lève l'ambiguïté quand le paramètre porte le nom du membre.

Note:
Avec le suffixe `_` sur les membres, l'ambiguïté n'existe pas et `this->` est
superflu. Il reste utile ailleurs : rendre `*this`, se passer en argument à une
autre fonction, ou s'enregistrer auprès d'un gestionnaire.

---

## Valeurs par défaut

```cpp
Monstre(std::string nom, int pointsDeVie = 30, int degats = 5);

Monstre gobelin{"Gobelin"};
Monstre troll{"Troll", 120};
Monstre boss{"Boss", 400, 25};
```

Un constructeur au lieu de trois qui se ressemblent. Les paramètres par défaut se
mettent **à la fin**, jamais au milieu.

---

# L'ordre
<!-- .slide: class="title" -->

---

## La liste d'initialisation

```cpp
class Monstre
{
public:
    Monstre(std::string nom, int pointsDeVie)
        : nom_(std::move(nom)), pointsDeVie_(pointsDeVie)
    {
    }
};
```

Entre les deux-points et l'accolade, chaque membre est **construit directement**
avec sa valeur.

---

## Initialiser n'est pas affecter

- dans la **liste** : le membre naît déjà bon, une seule opération
- dans le **corps** : il naît vide, puis on l'écrase, deux opérations
- un membre `const` ou une référence n'a **que** la liste

Sur un `int` ça ne se voit pas. Sur une `std::string`, c'est une allocation pour rien.

---

## L'ordre surprend toujours

```cpp
class Monstre
{
public:
    Monstre(int max)
        : pointsDeVieMax_(max), pointsDeVie_(pointsDeVieMax_)
    {
    }

private:
    int pointsDeVie_;        // déclaré en premier
    int pointsDeVieMax_;     // déclaré en second
};
```

L'ordre de la liste ne compte pas. Seul celui de la **déclaration** compte.

---

## Ce qui se passe vraiment
<!-- .slide: class="schema" -->

`Monstre(int max) : pointsDeVieMax_(max), pointsDeVie_(pointsDeVieMax_)`

![[poo04_ordre_initialisation.svg]]

Note:
Le membre lu n'est pas encore construit, et rien ne s'en plaint. `pointsDeVie_`
est déclaré en premier, donc initialisé en premier, à partir d'un
`pointsDeVieMax_` qui ne vaut encore rien. Le programme tourne et donne un
nombre — un nombre faux, différent selon la machine.

---

## La règle

- écrire la liste **dans l'ordre de déclaration**, toujours
- éviter qu'un membre ait besoin d'un autre pour naître
- l'avertissement existe, mais il est **éteint par défaut**

```text
cl /W4           ne dit rien
cl /W4 /w15038   warning C5038: 'pointsDeVieMax_' va être initialisé
                 après 'pointsDeVie_'
```

---

# Mourir
<!-- .slide: class="title" -->

---

## Le destructeur

```cpp
class Monstre
{
public:
    ~Monstre()
    {
        std::println("{} disparait", nom_);
    }
};
```

Le nom de la classe précédé d'un **tilde**. Aucun paramètre, aucun retour, un
seul par classe. On ne l'appelle jamais : il est appelé.

---

## Quand exactement

```text
main : avant
  + Gobelin : constructeur
    Gobelin agit
main : apres
  - Gobelin : destructeur
```

Le destructeur passe **après** la dernière ligne du `main` : à l'accolade
fermante, pas à la dernière instruction.

Note:
Trace réelle du companion, étape `01_dans_le_main`. Faire prédire la sortie avant
de l'afficher : la moitié de la classe place la destruction avant `main : apres`.

---

## La portée se dépile

```text
main : avant
  + Gobelin : constructeur
  + Troll : constructeur
main : apres
  - Troll : destructeur
  - Gobelin : destructeur
```

Le dernier construit est le **premier détruit**. Toujours.

Note:
Étape `03_deux_entites`. L'étape `02_dans_une_fonction` montre la même règle sur
une portée plus courte : l'objet d'une fonction meurt avant que le `main`
reprenne la main, donc entre deux lignes du `main`.

---

## Ce qu'on libère

- un fichier ouvert, une socket, un verrou
- une texture, un son, un buffer sur la carte graphique
- une place dans une liste que quelqu'un d'autre tient

Tout ce qui n'est pas une simple valeur a été **emprunté** à quelqu'un.

---

## Atelier — 20 min

Le companion écrit une ligne à chaque naissance et à chaque mort.

1. lancer `01_dans_le_main` — mais **prédire la trace avant** de la lire
2. recommencer avec `02_dans_une_fonction`, puis `03_deux_entites`
3. mettre une entité dans un bloc `{ }` au milieu du `main` : où passe sa mort ?
4. donner à `Monstre` un constructeur complet et un destructeur bavard

---

## À retenir

- le constructeur garantit un objet **valide dès sa naissance**
- la liste d'initialisation suit l'ordre de **déclaration**, pas le sien
- le destructeur passe à l'accolade fermante, dans l'ordre **inverse**
- on n'appelle ni l'un ni l'autre : tout est automatique

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/C++/GPR-CF-POO-05 - Static et surcharge d'opérateur|GPR-CF-POO-05]] — ce qui appartient à la classe plutôt qu'à l'objet.</small>
