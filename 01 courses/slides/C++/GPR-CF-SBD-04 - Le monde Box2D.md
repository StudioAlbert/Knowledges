---
title: GPR-CF-SBD-04 - Le monde Box2D
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: SFML et Box2D
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

# Le monde Box2D
<!-- .slide: class="title" -->
## GPR-CF-SBD-04

<small>Un monde qui calcule, et qui ne dessine rien</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir créer un monde physique, y poser des corps du bon type, et comprendre que ce monde ignore l'écran.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-01 - Boucle de jeu et fenêtre|GPR-CF-SBD-01]].

---

## Un monde parallèle

La physique calcule des positions ; personne ne les voit tant qu'on ne les recopie pas.

---

## Le monde

Une gravité, une liste de corps, et une méthode qui fait avancer le temps.

---

## Le pas de simulation

Un pas fixe donne des résultats reproductibles ; un pas variable donne des bugs impossibles à rejouer.

---

## Un corps

On décrit d'abord ce qu'on veut, puis le monde le fabrique — et c'est lui qui le possède.

---

## Trois types de corps

Statique pour le décor, cinématique pour ce qu'on pilote à la main, dynamique pour ce que la physique décide.

> [!tip] Widget — `box2d_corps_widget.html`
> Un bac à sable avec un corps de chaque type et un curseur de poussée. Le widget montre ce
> qui bouge, ce qui pousse sans être poussé, et ce qui ignore tout le monde. Des curseurs de
> densité, friction et restitution changent le comportement en direct.

---

## Une forme

Rectangle, cercle, polygone : la forme physique n'a rien à voir avec l'image affichée.

---

## La fixture

C'est la forme plus ses propriétés de matière — densité, frottement, rebond ; l'équivalent du collider et de son matériau sous Unity.

---

## Les unités

Box2D travaille en mètres et en kilogrammes : un personnage fait 1,8 et non 180.

> [!tip] Schéma
> Deux mondes côte à côte, l'un en pixels et l'autre en mètres, avec le facteur de
> conversion au milieu et le même personnage dessiné dans chacun — plus la liste des
> symptômes quand on oublie la conversion.

---

## Créer un corps dynamique

Définition, corps, forme, fixture : quatre étapes, toujours dans cet ordre.

---

## Ce que le monde fait tout seul

Intégration, détection des contacts, résolution : le travail qu'on ne veut surtout pas écrire.

---

## Atelier — 20 min

Un sol statique, trois caisses dynamiques, une plateforme cinématique qui va et vient, et les positions affichées dans la console.

---

## À retenir

Un monde, un pas fixe, le bon type de corps, des mètres — et rien à l'écran avant la séance suivante.

---

## Questions ?
