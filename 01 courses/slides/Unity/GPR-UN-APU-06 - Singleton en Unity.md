---
title: GPR-UN-APU-06 - Singleton en Unity
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

# Singleton en Unity
<!-- .slide: class="title" -->
## GPR-UN-APU-06

<small>Le pattern qu'on utilise trop, et pourquoi</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir écrire un singleton, savoir exactement ce qu'il coûte, et connaître ce qui le remplace.

**Prérequis :** [[01 courses/slides/Theory/TC-FT-PCL-01 - Couplage et cohésion|TC-FT-PCL-01]].

---

## Un seul gestionnaire d'audio

Le besoin est réel : certaines choses n'existent qu'une fois dans le jeu.

---

## Le pattern

Une instance unique, et un point d'accès depuis n'importe où.

---

## Deux promesses, pas une

Garantir l'unicité et offrir un accès global sont deux décisions distinctes — on les confond toujours.

---

## L'écrire en Unity

Un champ statique, une vérification au réveil, et la destruction du doublon.

---

## Ce que ça coûte

Chaque appel crée une dépendance que personne ne voit dans l'inspecteur.

> [!tip] Widget — `singleton_widget.html`
> Le graphe des dépendances d'un projet, d'abord sans les singletons : propre. Un
> interrupteur fait apparaître les arêtes créées par chaque accès statique, et le graphe
> devient illisible. Un compteur affiche le nombre de classes qui dépendent désormais du
> gestionnaire d'audio.

---

## Le singleton qui disparaît

Au changement de scène, l'instance est détruite — et le premier appel suivant échoue.

---

## Les doublons

Deux scènes qui contiennent chacune le gestionnaire : la deuxième écrase ou se fait détruire, selon ce qu'on a écrit.

---

## L'ordre d'initialisation

Deux singletons qui s'appellent l'un l'autre au réveil : le résultat dépend de l'ordre, donc du hasard.

---

## Les alternatives

Passer la dépendance, la référencer dans l'inspecteur, ou la publier dans un asset partagé.

---

## Quand c'est acceptable

Un vrai unique, sans état de partie, appelé par peu de classes — et assumé par écrit.

---

## Atelier — 20 min

Compter les accès statiques d'un projet du groupe, puis remplacer un singleton par une référence injectée.

---

## À retenir

L'unicité et l'accès global sont deux choix ; le second crée des dépendances invisibles, et se justifie au cas par cas.

---

## Questions ?
