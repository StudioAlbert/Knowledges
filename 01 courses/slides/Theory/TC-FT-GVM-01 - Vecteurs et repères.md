---
title: TC-FT-GVM-01 - Vecteurs et repères
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Géométrie Vectorielle et Matricielle
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

# Vecteurs et repères
<!-- .slide: class="title" -->

### La brique de tout ce qui bouge

<small>TC-FT-GVM-01 · Géométrie Vectorielle et Matricielle</small>

Note:
Première séance du bloc. Tout ce qui bouge dans un jeu — un personnage, une
balle, une caméra, un rayon de lumière — est décrit par des vecteurs. On pose
ici le vocabulaire et les quatre opérations qui serviront toute l'année.

---

## Objectifs

À la fin de la séance, vous savez :

- lire les **composantes** d'un vecteur et le dessiner
- calculer sa **norme**, et le **normaliser**
- **additionner**, **soustraire**, **multiplier par un scalaire**
- dire dans quel **repère** vous travaillez

**Prérequis :** Pythagore — [[01 courses/slides/Theory/TC-FT-TRG-01 - Géométrie du triangle|TC-FT-TRG-01]].

---

# D'abord, pourquoi
<!-- .slide: class="title" -->

---

## Un nombre ne suffit pas

> « L'ennemi avance à 5. »

**5 quoi, vers où ?**

Un **scalaire** porte une quantité : une masse, un temps, des points de vie.

Dès qu'il faut dire **où**, il manque une information — et un seul nombre ne
l'écrira jamais.

Note:
Insister : scalaire = un nombre. Vecteur = une direction *et* une longueur.
C'est toute la distinction de la séance.

---

## À quoi sert un vecteur ?

| La question du jeu | Un seul nombre | Le vecteur |
| --- | --- | --- |
| À quelle vitesse roule la voiture ? | 120 | 120 **et** vers le nord |
| Le vent pousse la flèche de combien ? | 8 | 8 **et** depuis la gauche |
| Où est le trésor ? | à 30 m | à 30 m **et** par là |
| Comment le sol est-il penché ? | 12° | sa **normale** |

Note:
Faire compléter la colonne du milieu par la classe avant d'afficher la droite.
La dernière ligne annonce GVM-02 : une normale est un vecteur, pas un angle.

---

## Composantes

Un vecteur est une **liste de nombres**, une par axe, et rien d'autre.

```
v = (3, 2)          w = (−1, 4, 0)
```

- en 2D : deux nombres, *x* et *y*
- en 3D : trois nombres, *x*, *y* et *z*
- chaque nombre dit **de combien on avance le long de cet axe**

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/vecteur_widget.html#vecteur" data-background-interactive -->

Note:
Attraper B et lire les composantes changer en direct. Faire remarquer qu'on
lit toujours AB = B − A, jamais les coordonnées de B seules.

---

## Point ou vecteur ?

Un **point** dit *où*. Un **vecteur** dit *de combien, et dans quel sens*.

```
AB = B − A
```

Une flèche a une direction et une longueur, mais **pas de point de départ
imposé** : la même flèche dessinée ailleurs reste le même vecteur.

Note:
C'est la confusion numéro un de l'année. `transform.position` est un point,
`velocity` est un vecteur — le moteur les range pourtant dans le même type.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/vecteur_widget.html#origine" data-background-interactive -->

Note:
La case « même vecteur depuis l'origine » est déjà cochée : le même AB est
redessiné en O. Déplacer A **et** B ensemble : le vecteur gris ne bouge pas.

---

# Mesurer
<!-- .slide: class="title" -->

---

## La norme

La norme est la **longueur** de la flèche. C'est Pythagore sur les composantes.

```
‖v‖ = √(x² + y²)

(4, 3)  ->  √(16 + 9) = √25 = 5
```

C'est elle qu'on lit quand le jeu demande **une distance**.

---

## La norme en C++

```cpp
#include <cmath>

struct Vector2 { float x, y; };

float Norme(Vector2 v)
{
    return std::sqrt(v.x * v.x + v.y * v.y);
}

// Norme({4.0f, 3.0f})  ->  5.0f
```

Note:
`std::sqrt` coûte cher. Pour *comparer* deux distances, on compare les carrés
et on ne prend jamais la racine — on y revient en GVM-02.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/vecteur_widget.html#norme" data-background-interactive -->

Note:
Le panneau détaille √(x² + y²) sur les valeurs courantes. Poser B sur (4, 3)
depuis A en (0, 0) pour retrouver le 5 de la slide précédente.

---

## Normaliser

Diviser un vecteur par sa norme donne une **direction pure**, de longueur 1.

```
v / ‖v‖          (4, 3)  ->  (0,8 ; 0,6)
```

- la **direction** est gardée
- la **longueur** est mise de côté, puis redonnée à part
- c'est ce qu'on veut pour **viser**, **avancer**, **orienter**

---

## Normaliser en C++

```cpp
Vector2 Normaliser(Vector2 v)
{
    const float n = Norme(v);
    if (n == 0.0f) return {0.0f, 0.0f};  // pas de direction
    return {v.x / n, v.y / n};
}

// avancer de 4 unités par seconde, quel que soit l'écart
Vector2 d = Normaliser(versCible);
position.x += d.x * 4.0f * dt;
position.y += d.y * 4.0f * dt;
```

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/vecteur_widget.html#normalise" data-background-interactive -->

Note:
La case « vecteur normalisé » est déjà cochée : AB passe en pointillé et la
direction de longueur 1 apparaît. Allonger AB : la flèche rouge ne bouge pas.

---

## Le piège du vecteur nul

Le vecteur `(0, 0)` a une norme de **zéro** — et on ne divise pas par zéro.

- il n'a **pas de direction** : la question n'a pas de réponse
- normaliser sans tester produit un `NaN`, qui contamine tout
- en pratique : **tester la norme avant**, ou la comparer à un epsilon

Note:
Le `NaN` se propage silencieusement : une position devient `NaN`, l'objet
disparaît du monde, et plus rien ne le ramène. Bug classique et pénible.

---

# Combiner
<!-- .slide: class="title" -->

---

## Multiplier par un scalaire

Le scalaire **étire** ou **retourne** le vecteur, sans le sortir de sa droite.

```
k · v = (k·x, k·y)
```

- *k* > 1 : plus long &nbsp;·&nbsp; 0 < *k* < 1 : plus court
- *k* < 0 : **demi-tour**
- *k* = 0 : il ne reste rien

C'est la formule du déplacement : `position + direction × vitesse × dt`.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/vecteur_widget.html#scalaire" data-background-interactive -->

Note:
Faire glisser k de 3 à −2 : le vecteur s'allonge, disparaît à 0, puis repart
à l'envers sur la même droite.

---

## Additionner

Deux déplacements enchaînés valent leur **somme** — composante par composante.

```
u + v = (uₓ + vₓ, u_y + v_y)
```

La poussée du moteur **plus** le courant donnent la trajectoire réelle.

> [!warning] Attention
> ‖u + v‖ **n'est pas** ‖u‖ + ‖v‖ — sauf si les deux pointent exactement pareil.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/vecteur_widget.html#somme" data-background-interactive -->

Note:
Le parallélogramme en pointillé montre les deux chemins. Le panneau compare
‖u + v‖ à ‖u‖ + ‖v‖ : les aligner pour les faire coïncider.

---

## Soustraire

Comme l'addition : **composante par composante**.

```
u − v = (uₓ − vₓ, u_y − v_y)
```

- c'est l'addition de l'opposé : `u − v = u + (−v)`
- le résultat est le vecteur qui **va de v vers u**
- sa **norme** est la distance entre les deux pointes

Note:
Insister : on soustrait deux **vecteurs**, et on obtient un **vecteur**. Le fait
qu'on l'applique ensuite à deux positions est une conséquence, pas la
définition.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/vecteur_widget.html#difference" data-background-interactive -->

Note:
Bouton `u − v` : la flèche rouge part bien de la pointe de v vers celle de u.
Déplacer u sur v pour obtenir le vecteur nul.

---

## Et sur deux positions

Appliquée à deux **points**, la même soustraction donne le vecteur qui va de
l'un vers l'autre. C'est **la** question que le jeu pose sans arrêt :

```
AB = B − A              cible − joueur
```

- sa **direction** → vers où tirer, où regarder, où fuir
- sa **norme** → à quelle distance, et donc : est-ce à portée ?

Note:
Ordre des opérandes : `cible - joueur` pointe vers la cible, l'inverse pointe
vers le joueur. Une erreur de signe ici et le PNJ fuit au lieu d'attaquer.

---

## Les règles qui tiennent

```
u + v = v + u                    l'ordre ne change rien
(u + v) + w = u + (v + w)        le groupement non plus
v + 0 = v                        le vecteur nul ne fait rien
v − v = 0                        l'opposé annule
```

Ce sont les règles de l'addition des nombres : rien de nouveau à mémoriser.

Note:
C'est pour ça qu'on peut enchaîner les sommes de forces — gravité, vent,
poussée, recul — dans n'importe quel ordre, sans y réfléchir.

---

# En mémoire, et dans le moteur
<!-- .slide: class="title" -->

---

## Du vecteur à la structure de données

```cpp
struct Vector2 { float x, y; };

Vector2 joueur{2.0f, 1.0f};
Vector2 cible {5.0f, 5.0f};

Vector2 versCible{cible.x - joueur.x, cible.y - joueur.y};

std::println("direction ({}, {})", versCible.x, versCible.y);
std::println("distance   {}", Norme(versCible));
```

En mémoire : deux ou trois nombres nommés `x`, `y`, `z` — ou indexés de **0 à 2**.

Note:
Lien direct avec POO-01 : `Vector2` est la structure la plus utile qu'on écrira.
Le moteur, lui, l'appelle `Vector2` / `Vector3`, ou `FVector` chez Unreal.

---

## Repères directs et indirects
<!-- .slide: class="schema" -->

La même lettre ne désigne pas le même axe d'un moteur à l'autre.

![[gvm01_reperes.svg]]

---

## Ce qu'il faut vérifier

- quel axe pointe vers le **haut** : `y` chez Unity, `z` chez Unreal
- quelle **main** décrit la rotation : gauche pour les deux, droite en maths
- quelle **unité** vaut 1 : le mètre chez Unity, le centimètre chez Unreal
- et toujours : **l'origine est où ?**

Note:
Un modèle importé couché, un personnage 100 fois trop petit, une rotation qui
part du mauvais côté : c'est presque toujours une de ces quatre lignes.

---

## Atelier — 20 min

Deux positions dans le niveau, et trois questions :

1. quel **vecteur** va de l'une à l'autre ?
2. quelle **distance** les sépare ?
3. à 4 unités par seconde, **où est-on après 3 secondes** ?

Exercices 1 à 3 de la feuille — sur papier d'abord, vérifiés au clavier ensuite.

---

## À retenir

- **soustraire** deux vecteurs en soustrait les composantes — et sur deux
  positions, `cible − joueur` donne la direction
- la **norme** donne la distance
- **normaliser** sépare la direction de la longueur
- le **vecteur nul** ne se normalise pas

Et on vérifie toujours **dans quel repère** on travaille.

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/Theory/TC-FT-GVM-02 - Produits scalaire et vectoriel|TC-FT-GVM-02]] — deux vecteurs, un angle : qui voit qui, et de quel côté.</small>
