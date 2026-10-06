---
title: GPR-CF-POO-02 - Classes et visibilité
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

# Classes et visibilité
<!-- .slide: class="title" -->

### Ce que l'objet montre, ce qu'il garde

<small>GPR-CF-POO-02 · Programmation Orientée Objet</small>

Note:
Suite directe de POO-01. On sait regrouper des données dans un type. Reste à y
mettre le **comportement**, et à empêcher le reste du programme de casser les
règles du jeu. Pas de constructeur ici : c'est POO-04.

---

## Objectifs

À la fin de la séance, vous savez :

- écrire une **méthode** et l'appeler sur un objet
- choisir ce qui est **public** et ce qui est **privé**
- faire tenir une **règle du jeu** par l'objet lui-même
- employer juste les mots : attribut, méthode, instance, interface

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-01 - Structures|GPR-CF-POO-01]].

---

# Le problème
<!-- .slide: class="title" -->

---

## Une structure que n'importe qui peut casser

```cpp
struct Joueur
{
    int pointsDeVie = 100;
    int pointsDeVieMax = 100;
};

Joueur heros;

heros.pointsDeVie = -50;      // compile
heros.pointsDeVie = 999999;   // compile aussi
```

Rien dans le code ne dit que c'est interdit.

---

## La règle n'existe nulle part

« Les points de vie restent entre 0 et le maximum » — où est-ce écrit ?

- dans le code du combat ? il faudra y penser **à chaque fois**
- dans le code des pièges, des soins, du poison, de la chute ?
- le jour où on oublie un endroit, le bug est là, et il est **silencieux**

Une règle répétée partout est une règle qui **n'existe pas**.

Note:
Faire lister par la classe tous les endroits qui touchent aux pv dans un jeu
réel. On arrive vite à dix. C'est l'argument de toute la séance.

---

# Les méthodes
<!-- .slide: class="title" -->

---

## Une fonction qui vit dans l'objet

```cpp
class Joueur
{
public:
    void subirDegats(int degats)
    {
        pointsDeVie_ = std::max(0, pointsDeVie_ - degats);
    }

private:
    int pointsDeVie_ = 100;
};
```

La méthode **connaît déjà** les données de son objet : elles ne sont pas en paramètre.

---

## L'appeler sur un objet

```cpp
Joueur heros;

heros.subirDegats(30);     // 100 -> 70
heros.subirDegats(9999);   // 70 -> 0, et pas -9929
```

- même notation que pour un champ : `objet.méthode(…)`
- chaque objet a **ses** valeurs ; la méthode travaille sur celles de `heros`
- la borne est écrite **une seule fois**, dans la méthode

Note:
Sortie réelle du programme de la séance : `Heros : 70/100 pv` puis
`Heros : 0/100 pv`. Le `std::max` est la règle, et elle ne peut plus être
oubliée par un appelant.

---

## Le membre et le paramètre

```cpp
void soigner(int soin)
{
    pointsDeVie_ = std::min(pointsDeVieMax_, pointsDeVie_ + soin);
}
```

- `soin` est un **paramètre** : il vient de l'appelant, il disparaît à la fin
- `pointsDeVie_` est un **attribut** : il appartient à l'objet, il lui survit
- le `_` final est une **convention** d'écriture, pas une règle du langage

Note:
D'autres conventions existent (`m_pointsDeVie`, `this->pointsDeVie`). Celle du
cours est le suffixe `_`. L'important est de distinguer d'un coup d'œil ce qui
appartient à l'objet de ce qui passe.

---

# Encapsuler
<!-- .slide: class="title" -->

---

## Rappel : public et privé

- `public:` — accessible depuis l'intérieur **et** l'extérieur
- `private:` — accessible **seulement** depuis l'intérieur
- une `struct` commence en `public:`, une `class` en `private:`

Vu en POO-01. Ce qui change aujourd'hui : **à quoi ça sert**.

---

## Ce que l'objet montre, ce qu'il garde
<!-- .slide: class="schema" -->

Le privé n'est pas du secret : c'est la promesse que personne ne contournera la règle.

![[poo02_encapsulation.svg]]

---

## Le compilateur tient la promesse

```cpp
Joueur heros;

heros.subirDegats(9999);     // d'accord : 0 pv
heros.pointsDeVie_ = -50;    // erreur de compilation
```

```text
error C2248: 'Joueur::pointsDeVie_' : impossible d'accéder à
             private membre déclaré(e) dans la classe 'Joueur'
```

Ce n'est pas une convention d'équipe : c'est **refusé à la compilation**.

Note:
Message de MSVC, vérifié. GCC dit la même chose autrement :
`'int Joueur::pointsDeVie_' is private within this context`.

---

## L'interface, c'est ce qui est public

L'extérieur demande un **service**, pas un accès.

- `subirDegats(12)` — et non `pointsDeVie -= 12`
- `estVivant()` — et non `pointsDeVie > 0` recopié partout
- `ouvrirPorte()` — et non `cles -= 1`

Le reste du jeu parle de **ce qu'il veut**, pas de comment c'est rangé.

---

## Pourquoi cacher

Ce qui est caché peut changer demain **sans casser le reste du jeu**.

- passer les pv de `int` à `float` : un seul fichier à toucher
- ajouter une armure qui réduit les dégâts : dans `subirDegats`, et nulle part ailleurs
- journaliser chaque coup reçu : une ligne, au bon endroit

Note:
C'est l'argument qui tient toute l'année, et la raison du bloc *Couplage et
cohésion* en TC-FT-PCL-01 : moins l'extérieur en sait, moins il casse.

---

## Accesseurs, et quand s'en passer

```cpp
int pointsDeVie() const { return pointsDeVie_; }   // n'encapsule rien
bool estVivant()  const { return pointsDeVie_ > 0; }
```

- un accesseur qui rend juste le champ **rouvre** ce qu'on venait de fermer
- la bonne question : *de quoi l'appelant a-t-il besoin ?*
- souvent d'un **verdict** (`estVivant`), pas d'un nombre

En lecture seule, un accesseur reste utile — pour l'afficher, par exemple.

---

# Classe et instance
<!-- .slide: class="title" -->

---

## Le plan et les objets

```cpp
Joueur equipe[3];       // trois objets, un seul plan

for (const Joueur& j : equipe)
{
    j.afficherFiche();
}
```

- la **classe** `Joueur` est une définition : elle n'existe pas à l'exécution
- chaque **instance** a ses propres attributs, en mémoire
- les méthodes, elles, sont écrites **une fois** pour toutes les instances

---

## `class` ou `struct` : le choix dit l'intention

| On écrit | Quand |
| --- | --- |
| `struct` | un **agrégat** de données, sans règle à tenir — `Vector2`, `Ennemi` de POO-01 |
| `class` | des données **à protéger**, et des méthodes qui tiennent les règles |

Techniquement, seule la visibilité par défaut change. **Pour le lecteur**, tout change.

---

## Le vocabulaire

| Le mot | Ce que c'est |
| --- | --- |
| **attribut** (membre) | une donnée qui appartient à l'objet |
| **méthode** | une fonction qui appartient à l'objet |
| **instance** (objet) | un exemplaire de la classe, en mémoire |
| **interface** | tout ce qui est public : ce que l'extérieur peut demander |
| **encapsulation** | ranger la donnée derrière le comportement |

Note:
Ces cinq mots reviennent jusqu'en fin d'année, et en entretien d'embauche.
Les faire répéter avec l'exemple `Joueur` sous les yeux.

---

## Atelier — 20 min

Reprendre le `Monstre` de la séance précédente et le **fermer** :

1. passer les données au privé, et faire recompiler le programme existant
2. écrire `subirDegats` et `soigner` qui bornent la vie entre 0 et le maximum
3. prouver par un appel de **9999 dégâts** que la règle tient

Exercices 1, 2 et 4 de la feuille ; le 5 est le bilan, à finir à la maison.

---

## À retenir

- les **données au privé**, le **comportement au public**
- chaque règle du jeu est tenue par l'objet qui la porte, **une seule fois**
- un accesseur qui rend juste le champ n'encapsule rien
- `class` ou `struct` : techniquement la visibilité, pour le lecteur l'intention

---

# Questions ?
<!-- .slide: class="title" -->

