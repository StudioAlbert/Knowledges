---
title: GPR-CF-POO-04 - Cycle de vie de l'objet
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

# Cycle de vie de l'objet
<!-- .slide: class="title" -->
## GPR-CF-POO-04

<small>Naître dans un état valide, mourir en rangeant</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir écrire des constructeurs, connaître l'ordre d'initialisation, et savoir quand le destructeur passe.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-02 - Classes et visibilité|GPR-CF-POO-02]].

---

## Un objet naît, vit, meurt

Entre les deux, il doit toujours être dans un état que le reste du jeu peut utiliser.

---

## `this`

Dans une méthode, `this` désigne l'objet sur lequel on travaille : il lève les ambiguïtés de nom.

---

## Le constructeur par défaut

Sans constructeur, les champs d'une classe ne valent rien de précis — et un monstre à zéro point de vie naît mort.

---

## Construire avec des paramètres

Le constructeur est la seule porte d'entrée : ce qu'il exige ne peut pas être oublié.

---

## Valeurs par défaut

Des paramètres par défaut évitent quatre constructeurs qui se ressemblent.

---

## La liste d'initialisation

Initialiser, ce n'est pas affecter dans le corps : la liste construit directement chaque membre.

---

## L'ordre surprend toujours

Les membres s'initialisent dans l'ordre de leur déclaration, pas dans celui de la liste.

> [!tip] Widget — `cycle_de_vie_widget.html`
> Un bloc de code avec des portées imbriquées et trois objets. En avançant ligne à ligne,
> le widget empile les constructions et dépile les destructions, affiche l'ordre réel des
> membres, et signale le cas où un membre est utilisé avant d'être initialisé.

---

## Le destructeur

Il est appelé une fois, automatiquement, et c'est là qu'on rend ce qu'on a emprunté.

---

## Quand exactement

À la fin de la portée, à la destruction du conteneur, ou à la fin du programme — et dans l'ordre inverse de la construction.

---

## Ce qu'on libère

Un fichier ouvert, une texture chargée, une place dans une liste : tout ce qui n'est pas une simple valeur.

---

## Atelier — 20 min

Donner à `Monstre` trois constructeurs et un destructeur bavard, puis observer l'ordre des messages dans une vague d'ennemis.

---

## À retenir

Le constructeur garantit l'état valide, la liste d'initialisation respecte l'ordre de déclaration, le destructeur range — et tout est automatique.

---

## Questions ?
