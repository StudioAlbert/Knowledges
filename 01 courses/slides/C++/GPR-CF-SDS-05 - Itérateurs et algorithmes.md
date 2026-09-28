---
title: GPR-CF-SDS-05 - Itérateurs et algorithmes
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Structures de Données et STL
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

# Itérateurs et algorithmes
<!-- .slide: class="title" -->
## GPR-CF-SDS-05

<small>Dire ce qu'on veut, pas comment parcourir</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir ce qu'est un itérateur, passer une fonction à un algorithme, et remplacer ses boucles par la bibliothèque.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SDS-01 - Séquences|GPR-CF-SDS-01]].

---

## Parcourir sans savoir quoi

Un itérateur désigne une position dans une séquence, quelle que soit la séquence.

---

## Début et fin

La fin désigne l'endroit juste après le dernier élément : c'est ce qui permet la boucle vide.

---

## Déplacer

Avancer d'un cran est la seule opération garantie ; sauter de dix ne l'est pas partout.

> [!tip] Widget — `iterateur_widget.html`
> Un conteneur dessiné en cases, avec les marqueurs de début et de fin. On avance
> l'itérateur pas à pas, on définit un intervalle, et le widget montre quel algorithme
> consommerait quoi. Une suppression en cours de parcours fait apparaître l'itérateur devenu
> invalide.

---

## L'intervalle

Deux itérateurs définissent un intervalle, et tous les algorithmes travaillent là-dessus.

---

## Une fonction en paramètre

Un prédicat répond vrai ou faux, une fonction unaire transforme — et la lambda les écrit sur place.

---

## La bibliothèque d'algorithmes

Ce que vous êtes en train d'écrire à la main existe déjà, testé et nommé.

---

## Les ranges

La version moderne prend le conteneur entier et s'enchaîne : moins de bruit, même sens.

---

## Les politiques d'exécution

Un argument de plus, et l'algorithme s'exécute sur plusieurs cœurs — quand cela vaut la peine.

---

## Les familles

Chercher, compter, transformer, trier, partitionner, réduire : six intentions couvrent presque tout.

---

## L'itérateur qui ne vaut plus rien

Modifier le conteneur pendant qu'on le parcourt invalide ce qu'on tient : la règle de `GPR-CF-SDS-01` revient.

---

## Atelier — 20 min

Remplacer quatre boucles écrites à la main par les algorithmes correspondants, sans changer le résultat.

---

## À retenir

Un intervalle, un prédicat, un algorithme nommé — et on ne réécrit plus de boucle sans raison.

---

## Questions ?
