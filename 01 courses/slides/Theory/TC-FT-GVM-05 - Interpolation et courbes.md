---
title: TC-FT-GVM-05 - Interpolation et courbes
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
publish: false
---

# Interpolation et courbes
<!-- .slide: class="title" -->
## TC-FT-GVM-05

<small>Entre A et B, tout se joue dans la courbe</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir interpoler entre deux valeurs, normaliser un paramètre de temps, et choisir la courbe qui donne la bonne sensation.

**Prérequis :** [[01 courses/slides/Theory/TC-FT-GVM-01 - Vecteurs et repères|TC-FT-GVM-01]].

---

## Aller de A à B

Tout ce qui bouge dans un jeu est une valeur qui passe d'une autre en un certain temps.

---

## Lerp

Un paramètre entre 0 et 1 mélange deux valeurs : 0 donne la première, 1 la seconde.

---

## Normaliser le temps

Le paramètre s'obtient en divisant le temps écoulé par la durée voulue — et se borne à 1.

---

## Interpoler quoi

Positions, couleurs, volumes sonores : tout ce qui s'additionne et se multiplie. Les angles, eux, méritent une précaution.

---

## Tourner en 2D

Une rotation dans le plan est un mélange de sinus et de cosinus des deux composantes.

---

## Tourner en 3D

En 3D, on tourne autour d'un axe, et l'ordre des rotations change le résultat — d'où les séances suivantes.

---

## Fonctions paramétriques

Une courbe est un point qui dépend d'un paramètre ; le parcourir, c'est faire varier ce paramètre.

---

## Le mouvement linéaire ne trompe personne

Une vitesse constante sur toute la durée donne cette sensation de tiroir mécanique.

---

## Smooth start, smooth stop

Élever le paramètre à une puissance accélère au départ ; le miroir freine à l'arrivée.

> [!tip] Widget — `easing_widget.html`
> Les courbes d'easing tracées dans un carré de 0 à 1, sélectionnables. Un curseur de temps
> déplace simultanément le point sur la courbe et une bille sur une piste, pour relier la
> forme de la courbe à la sensation. Deux courbes peuvent être comparées côte à côte.

---

## Smoother step

Une courbe en S démarre et finit au repos : c'est le passe-partout des interfaces.

---

## Smooth arch

Une courbe qui monte puis redescend décrit un saut, un pop d'icône, un flash de dégât.

---

## Atelier — 20 min

Animer l'ouverture d'une porte et le remplissage d'une barre de vie avec trois courbes différentes, et dire laquelle va à quoi.

---

## À retenir

Un paramètre normalisé, une valeur de départ, une valeur d'arrivée, et une courbe : c'est toute l'animation procédurale.

---

## Questions ?
