---
title: GPR-UN-APU-07 - Singleton générique et persistant
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

# Singleton générique et persistant
<!-- .slide: class="title" -->
## GPR-UN-APU-07

<small>Si on en fait un, qu'il soit tenu</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir écrire un singleton générique, le faire survivre aux scènes, et contraindre son usage pour qu'il reste tenable.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-APU-06 - Singleton en Unity|GPR-UN-APU-06]].

---

## Écrire le même code quatre fois

Quatre gestionnaires, quatre fois la même vérification au réveil : c'est de la duplication.

---

## Le composant générique

Une classe de base paramétrée par son propre type, et chaque gestionnaire en hérite.

---

## Ce que la généricité résout

Elle enlève la duplication, mais ne change rien au couplage : le problème de la séance précédente reste entier.

---

## Survivre au changement de scène

Un objet marqué persistant traverse les chargements — et n'appartient plus à aucune scène.

---

## Le piège de la persistance

Ce qui survit garde aussi son état : la partie suivante commence avec les scores de la précédente.

> [!tip] Widget — `bootstrap_widget.html`
> La frise du démarrage : chargement de scène, réveils dans un ordre arbitraire, premiers
> appels. Un interrupteur remplace le réveil libre par un bootstrap explicite, et les accès
> à une instance non prête disparaissent de la frise.

---

## Un singleton régulé

Interdire l'accès avant l'initialisation vaut mieux qu'une instance créée dans le dos du programmeur.

---

## L'ordre, explicitement

Un point d'entrée unique qui initialise dans l'ordre voulu remplace la loterie des réveils.

---

## Contraindre volontairement

Exposer une interface étroite plutôt que la classe entière limite ce que le reste du jeu peut en faire.

---

## Le rechargement en éditeur

En éditeur, les champs statiques survivent au rechargement du code : un état fantôme qui n'existe pas dans le build.

---

## Atelier — 20 min

Transformer deux gestionnaires en singletons génériques persistants, puis les initialiser depuis un bootstrap ordonné.

---

## À retenir

Générique pour ne pas dupliquer, persistant si on assume l'état, régulé pour interdire l'accès trop tôt, et un ordre écrit plutôt que subi.

---

## Questions ?
