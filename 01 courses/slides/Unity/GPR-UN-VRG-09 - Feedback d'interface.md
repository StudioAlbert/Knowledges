---
title: GPR-UN-VRG-09 - Feedback d'interface
type: slides
status: Backlog
subject: Unity
duration_h: 1
bloc_gsda: VFX, Rendu et Game Feel
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

# Feedback d'interface
<!-- .slide: class="title" -->
## GPR-UN-VRG-09

<small>Ce que l'interface doit faire sentir</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir animer un compteur, une barre et un bouton, et savoir ce qui ne doit jamais attendre.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-VRG-08 - Feedback visuel|GPR-UN-VRG-08]].

---

## L'interface parle

Un chiffre qui change sans bouger n'est pas vu ; un chiffre qui monte est lu.

---

## Le compteur qui monte

Jamais de saut à la valeur finale : le trajet est l'information.

---

## La barre de vie

Deux barres superposées, l'une instantanée et l'autre retardée, disent combien on vient de perdre.

> [!tip] Widget — `barre_de_vie_widget.html`
> Une barre de vie avec sa barre de dégât retardée, et trois curseurs — délai, vitesse de
> rattrapage, courbe. Un bouton applique un coup léger, un coup lourd, ou une série rapide ;
> un mode « saut instantané » montre ce que le joueur ne perçoit pas.

---

## Le bouton qui répond

Survol, appui, relâchement, désactivé : quatre états, et le joueur les attend tous.

---

## Les transitions d'écran

Une transition dit d'où l'on vient et où l'on va — et cache ce qui charge.

---

## L'ordre d'apparition

Les éléments qui arrivent en cascade guident le regard là où il faut.

---

## Ce qui doit rester immédiat

Le retour de l'appui, jamais. On anime la conséquence, pas l'accusé de réception.

---

## L'animation qui bloque

Une animation qui empêche d'agir est ressentie comme une latence, même jolie.

---

## Ce que ça coûte

Beaucoup de petites animations font beaucoup de petits calculs : l'interface sait plomber un jeu.

---

## Atelier — 20 min

Animer le score, la barre de vie et les boutons du menu du prototype, sans bloquer l'entrée du joueur.

---

## À retenir

Le trajet est l'information, l'appui se confirme immédiatement, les animations ne bloquent jamais — et l'interface se mesure aussi.

---

## Questions ?
