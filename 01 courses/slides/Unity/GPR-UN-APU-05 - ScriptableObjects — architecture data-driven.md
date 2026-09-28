---
title: GPR-UN-APU-05 - ScriptableObjects — architecture data-driven
type: slides
status: Backlog
subject: Unity
duration_h: 1
bloc_gsda: Architecture et Patterns Unity
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

# ScriptableObjects
<!-- .slide: class="title" -->
## GPR-UN-APU-05

<small>Architecture data-driven</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir faire communiquer des objets et des scènes par des assets, et connaître les limites de l'approche.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|GPR-UN-APU-04]].

---

## Deux scènes qui doivent se parler

L'interface est dans une scène, le gameplay dans une autre : aucune référence directe n'est possible.

---

## La variable partagée

Un asset qui contient la vie du joueur : tout le monde le lit, personne ne se connaît.

---

## L'événement en asset

Un canal nommé dans le projet : le gameplay y crie, l'interface y écoute.

---

## Câbler dans l'inspecteur

Le designer relie l'émetteur au récepteur sans écrire de code, et le voit dans la scène.

> [!tip] Widget — `so_event_widget.html`
> Deux scènes côte à côte, un canal d'événement en asset au milieu. Le bouton « le joueur
> prend un coup » traverse le canal et fait réagir les abonnés de l'autre scène ; on peut
> couper un abonné et voir ce qui cesse de réagir.

---

## Ce que ça découple vraiment

Les scènes deviennent indépendantes, testables séparément, et chargeables dans n'importe quel ordre.

---

## L'état qui persiste

Une variable partagée conserve sa valeur entre deux parties : il faut décider qui la remet à zéro, et quand.

---

## Ce que la sérialisation ne sait pas faire

Pointer un objet de scène depuis un asset, ni retrouver un type dérivé sans aide.

---

## Quand c'est trop

Tout mettre en assets rend le projet aussi illisible qu'un `GameManager` de mille lignes.

---

## Retrouver qui a écrit

Un canal sans journal devient indébogable : prévoir un mode verbeux dès le départ.

---

## Atelier — 20 min

Faire communiquer la scène d'interface et la scène de jeu par un canal d'événement et une variable partagée.

---

## À retenir

Un asset comme canal découple les scènes, l'état partagé doit être remis à zéro, et le câblage a besoin d'être traçable.

---

## Questions ?
