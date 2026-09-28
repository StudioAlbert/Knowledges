---
title: GPR-UN-VRG-08 - Feedback visuel
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

# Feedback visuel
<!-- .slide: class="title" -->
## GPR-UN-VRG-08

<small>Faire sentir un coup sans changer une règle</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir régler les cinq retours visuels de base, et comprendre que tout se joue dans les courbes.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-VRG-07 - Ce qu'est le juice|GPR-UN-VRG-07]] et les courbes de `TC-FT-GVM-05`.

---

## Le coup qui se voit

Le joueur ne lit pas les points de vie : il lit l'image.

---

## La secousse de caméra

Quatre réglages seulement — amplitude, durée, fréquence, décroissance — et mille sensations.

> [!tip] Widget — `camera_shake_widget.html`
> Quatre curseurs et un aperçu qui rejoue la secousse en boucle, avec sa courbe
> d'amortissement tracée en dessous. Trois préréglages montrent la différence entre un coup
> de poing, une explosion et un tremblement de terre.

---

## L'arrêt sur image

Geler le jeu deux ou trois images à l'impact donne du poids, et ne coûte rien.

---

## Le coup d'échelle

L'objet touché s'écrase puis reprend sa forme : c'est le retour le moins cher du catalogue.

---

## Le flash de dégât

Un éclair blanc très bref sur la cible dit « touché » plus vite que n'importe quel chiffre.

---

## Les traînées

Une trace derrière l'arme ou le projectile rend le mouvement lisible même à grande vitesse.

---

## Tout se règle en courbes

Un même effet paraît mou ou sec selon sa courbe d'atténuation, pas selon son amplitude.

---

## Le cumul

Dix coups simultanés donnent dix secousses : il faut les additionner avec un plafond.

---

## Ce qui ne doit jamais bouger

L'interface critique, le réticule, le texte : les faire trembler rend le jeu injouable.

---

## Ce que ça coûte

Presque rien en calcul, beaucoup en temps de réglage — et c'est le temps qui se planifie.

---

## Atelier — 20 min

Régler la secousse, l'arrêt sur image et le coup d'échelle du prototype, puis les faire cumuler proprement.

---

## À retenir

Cinq leviers, quatre réglages chacun, une courbe qui décide de la sensation, un plafond pour le cumul — et l'interface qui reste stable.

---

## Questions ?
