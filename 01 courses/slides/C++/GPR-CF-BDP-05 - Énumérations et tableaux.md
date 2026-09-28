---
title: GPR-CF-BDP-05 - Énumérations et tableaux
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
publish: false
---

# Énumérations et tableaux
<!-- .slide: class="title" -->
## GPR-CF-BDP-05

<small>Nommer les cas, ranger les séries</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir nommer un ensemble fini de cas avec une énumération, et manipuler une série de valeurs avec un tableau.

**Prérequis :** conditions et boucles — [[01 courses/slides/C++/GPR-CF-BDP-04 - Branches et boucles|GPR-CF-BDP-04]].

---

## `etat = 2`, et personne ne sait ce que ça veut dire

Un entier qui code un état ne se relit pas, et rien n'empêche d'y mettre 7.

---

## L'énumération nomme les cas

`enum class Etat { Patrouille, Alerte, Poursuite }` remplace trois nombres par trois mots du jeu.

---

## `enum` ou `enum class`

L'énumération nue se mélange aux entiers sans prévenir ; la version `class` refuse, et c'est ce qu'on veut.

---

## Décider avec un `switch`

Un `switch` sans `default` fait signaler par le compilateur le cas qu'on a oublié d'écrire.

---

## Un tableau, cent ennemis

Un tableau range des valeurs du même type, contiguës en mémoire, atteintes par leur index.

---

## L'index commence à zéro

Le dixième élément est à l'index 9, et lire l'index 10 ne provoque aucune erreur immédiate.

> [!tip] Widget — `tableau_index_widget.html`
> Un tableau de dix scores dessiné case par case avec ses index. Un curseur montre la
> valeur lue ; au-delà des bornes, le widget affiche ce qui traîne en mémoire à cet endroit
> plutôt qu'un message d'erreur — la démonstration de la séance.

---

## Indexer par une énumération

`degats[Arme::Epee]` se lit tout seul, et la taille du tableau suit le nombre de cas.

---

## Passer un tableau à une fonction

Un tableau à la mode C perd sa taille en route : il faut la transmettre à côté.

---

## `std::array`, celui qui se souvient

Il connaît sa taille, se copie normalement, et son `at()` vérifie l'index.

---

## Deux dimensions

Une grille de niveau est un tableau de lignes, et l'accès se lit ligne puis colonne.

> [!tip] Widget — `grille_memoire_widget.html`
> Une grille de tuiles 4 sur 6 à gauche, la même mémoire linéaire à droite. Cliquer une
> tuile allume la case correspondante et affiche le calcul de l'index.

---

## Atelier — 20 min

Le tableau de dégâts par type d'arme, puis la grille du niveau affichée en caractères.

---

## À retenir

Une énumération pour les cas nommés, un tableau pour les séries, un index qui part de zéro — et `at()` quand on doute.

---

## Questions ?
