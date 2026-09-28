---
title: GPR-CF-POO-05 - Static et surcharge d'opérateur
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
publish: false
---

# Static et surcharge d'opérateur
<!-- .slide: class="title" -->
## GPR-CF-POO-05

<small>Ce qui appartient à la classe, et ce qui se lit comme des maths</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir ce que `static` partage, et donner à une classe les opérateurs qui rendent le code lisible.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-04 - Cycle de vie de l'objet|GPR-CF-POO-04]].

---

## Combien d'ennemis vivants ?

La question ne concerne aucun ennemi en particulier : elle concerne la classe.

---

## L'attribut `static`

Une seule case mémoire pour toutes les instances, qui survit à chacune d'elles.

> [!tip] Widget — `static_partage_widget.html`
> Cinq instances dessinées côte à côte, chacune avec ses propres champs, et une case
> `static` à part. Créer ou détruire une instance met à jour le compteur partagé ; modifier
> le champ d'une instance ne touche pas les autres, et modifier le `static` bouge partout.

---

## La méthode `static`

Elle s'appelle sur la classe, sans instance — donc sans `this`.

---

## Où ça se définit

Déclaré dans la classe, l'attribut `static` a besoin d'une définition dans le source.

---

## Le `static` n'est pas une variable globale déguisée

Il reste partagé par tout le programme : à utiliser pour ce qui est vraiment unique.

---

## Surcharger un opérateur

Additionner deux vecteurs doit s'écrire avec un plus, pas avec un appel de fonction.

---

## Membre ou fonction libre

L'opérateur membre impose l'objet à gauche ; la fonction libre traite les deux côtés sur le même pied.

---

## Comparer

Donner `==` et `<` à une classe, c'est rendre possibles la recherche et le tri.

---

## Les pièges

Un opérateur qui surprend est pire qu'une méthode nommée : on ne surcharge que ce qui va de soi.

---

## Atelier — 20 min

Donner à `Vector2` ses opérateurs d'addition, de multiplication par un scalaire et d'égalité, puis compter les instances créées avec un `static`.

---

## À retenir

`static` appartient à la classe, l'opérateur appartient au sens commun — et tout ce qui surprend le lecteur se nomme plutôt qu'il ne se surcharge.

---

## Questions ?
