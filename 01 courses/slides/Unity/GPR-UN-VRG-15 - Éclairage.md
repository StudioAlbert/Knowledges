---
title: GPR-UN-VRG-15 - Éclairage
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

# Éclairage
<!-- .slide: class="title" -->
## GPR-UN-VRG-15

<small>Ce qui transforme un décor gris en lieu</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir choisir un type de lumière, décider ce qui est précalculé, et mesurer ce que l'éclairage coûte.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-VRG-13 - Les render pipelines|GPR-UN-VRG-13]] et `GPR-UN-VRG-14`.

---

## La lumière fait le lieu

Le même couloir est un abri ou une menace selon d'où vient la lumière.

---

## Quatre types de lumières

Directionnelle pour le soleil, ponctuelle pour une torche, spot pour une lampe, surfacique pour une fenêtre.

---

## Temps réel ou précalculé

Ce qui ne bouge jamais peut être calculé une fois pour toutes ; le reste se paie à chaque image.

---

## Le lightmapping

La lumière et ses ombres sont cuites dans une texture, et ne coûtent plus rien à l'exécution.

> [!tip] Widget — `eclairage_widget.html`
> Une pièce en vue isométrique avec quatre lumières commutables. Un interrupteur bascule
> entre temps réel et précalculé, un compteur affiche le coût estimé par image, et un curseur
> de résolution de lightmap montre le compromis entre qualité, poids sur le disque et temps
> de cuisson.

---

## Et ce qui bouge

Un objet mobile ne peut pas être cuit : il échantillonne la lumière alentour par des sondes.

---

## L'illumination globale

La lumière rebondit : sans ces rebonds, les zones d'ombre sont noires et mortes.

---

## Les réflexions

Une sonde de réflexion donne au sol mouillé ce qu'il doit refléter, à un coût maîtrisé.

---

## L'exposition

Régler l'exposition, c'est décider ce qui est lisible — avant de toucher au reste.

---

## Ce que ça coûte

Le prix se paie en lumières qui atteignent le même pixel, pas en lumières dans la scène.

---

## Atelier — 20 min

Éclairer une salle de donjon : une source principale précalculée, une torche animée en temps réel, des sondes pour le joueur.

---

## À retenir

Le type de lumière dit l'intention, la cuisson décide du coût, les sondes rattrapent ce qui bouge, et l'exposition se règle en premier.

---

## Questions ?
