---
title: GPR-CF-SBD-05 - Relier physique et graphique
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

# Relier physique et graphique
<!-- .slide: class="title" -->
## GPR-CF-SBD-05

<small>Le pont entre les deux mondes</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir afficher ce que la physique calcule, piloter un personnage physique, et réagir aux contacts.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-04 - Le monde Box2D|GPR-CF-SBD-04]].

---

## Le pont

Après chaque pas de simulation, on recopie les positions physiques dans les sprites — et jamais l'inverse.

---

## Dans le bon sens

Écrire directement la position d'un sprite qui a un corps, c'est mentir à la physique.

---

## Conversion d'unités

Multiplier par le facteur d'échelle à l'affichage, diviser à la création : une seule constante, un seul endroit.

---

## Les angles

Box2D compte en radians, SFML en degrés : la conversion s'oublie exactement une fois par projet.

---

## Trois façons de faire bouger

Une force pousse progressivement, une impulsion donne un coup sec, imposer la vitesse répond au doigt.

> [!tip] Widget — `forces_widget.html`
> Un même personnage piloté par trois modes — force, impulsion, vitesse imposée — avec la
> courbe de sa vitesse tracée en dessous. Un curseur de masse montre pourquoi les jeux de
> plateforme finissent presque tous par imposer la vitesse horizontale.

---

## Écouter les contacts

Le monde prévient quand deux formes se touchent et quand elles se séparent : à nous d'écouter.

---

## Qui a touché qui

Une forme peut porter un pointeur vers l'objet de jeu : c'est ainsi qu'on remonte du contact au gobelin.

---

## Le contact n'est pas le gameplay

Pendant la résolution, le monde est verrouillé : on note ce qui s'est passé, on agit après le pas.

> [!tip] Schéma
> La frise d'une image : pas de simulation, contacts collectés dans une file, puis traitement
> du gameplay, puis recopie vers les sprites, puis rendu. Une flèche barrée montre la
> tentation de supprimer un corps au milieu du pas.

---

## Atelier — 20 min

Le personnage physique : déplacement horizontal, saut, sprites synchronisés, et un son au contact du sol.

---

## À retenir

La physique décide, le graphique suit, les contacts se collectent et se traitent après le pas.

---

## Questions ?
