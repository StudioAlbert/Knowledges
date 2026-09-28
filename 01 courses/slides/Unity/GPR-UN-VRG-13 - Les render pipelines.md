---
title: GPR-UN-VRG-13 - Les render pipelines
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

# Les render pipelines
<!-- .slide: class="title" -->
## GPR-UN-VRG-13

<small>Choisir avant de commencer, pas après</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir ce qu'un pipeline de rendu décide à votre place, lequel choisir selon la cible, et ce que coûte un changement d'avis.

---

## Qui décide de l'ordre du rendu

Le pipeline décide quand chaque objet est dessiné, comment la lumière l'atteint, et ce qui est possible ensuite.

---

## Le pipeline intégré

Celui de tous les tutoriels anciens : encore présent, plus vraiment développé.

---

## URP

Le choix par défaut aujourd'hui : portable, outillé, suffisant pour la grande majorité des jeux.

---

## HDRP

Pour le rendu réaliste haut de gamme, avec les exigences matérielles qui vont avec.

---

## Écrire le sien

L'architecture permet de définir son propre pipeline — rarement nécessaire, parfois décisif.

---

## Ce que chacun impose

Des shaders incompatibles, des réglages de lumière différents, des fonctionnalités présentes d'un côté et absentes de l'autre.

> [!tip] Widget — `pipelines_widget.html`
> Un tableau comparatif des trois pipelines sur une dizaine de critères, et un second onglet
> « et si je migre » : on cochant ce que le projet utilise, le widget liste ce qui casserait,
> ce qui se convertit automatiquement, et ce qui devra être refait à la main.

---

## Choisir selon la cible

Mobile, PC modeste, console, casque : la cible tranche presque toujours la question.

---

## Le coût d'une migration

Les matériaux deviennent roses, et c'est le symptôme le plus bénin.

---

## Ce qui ne se migre pas

Les shaders écrits à la main, les effets dépendant du pipeline, et les réglages d'éclairage cuits.

---

## Décider tôt

Le choix se fait à la création du projet ; après trois mois, il se paie en semaines.

---

## Atelier — 20 min

Sur un projet du groupe : identifier le pipeline en place, ce qu'il impose, et ce qu'une migration coûterait.

---

## À retenir

Le pipeline décide du rendu et des shaders possibles, la cible dicte le choix, et on décide au premier jour.

---

## Questions ?
