---
title: TC-FT-GVM-04 - Espaces et changements de repère
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

# Espaces et changements de repère
<!-- .slide: class="title" -->
## TC-FT-GVM-04

<small>Le même point, selon qui regarde</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir nommer les espaces d'un moteur, passer de l'un à l'autre, et inverser une transformation.

**Prérequis :** [[01 courses/slides/Theory/TC-FT-GVM-03 - Matrices et transformations|TC-FT-GVM-03]].

---

## Quatre espaces

Objet, monde, vue, écran : un point y a quatre coordonnées différentes et une seule position.

> [!tip] Schéma
> Une bande horizontale en quatre cases, une par espace, avec la matrice qui fait passer de
> l'une à l'autre écrite sur chaque flèche — et le même point dessiné dans chacune.

---

## La chaîne

Chaque étape est une multiplication, et la chaîne complète est un seul produit précalculé.

---

## La hiérarchie

Un enfant est placé dans le repère de son parent : déplacer le parent déplace tout le monde.

---

## Le repère local

Travailler en local simplifie tout : la porte s'ouvre autour de son gond, pas autour de l'origine du monde.

---

## Revenir en arrière

L'inverse d'une transformation ramène du monde vers le local — et c'est ce que fait un clic de souris.

---

## L'inverse des petites matrices

En deux et trois dimensions, l'inverse s'écrit en forme fermée : pas besoin d'algorithme général.

---

## L'inverse d'une rotation

C'est sa transposée : gratuit, exact, et à privilégier dès qu'on sait que la matrice est orthogonale.

---

## Changer de base

Exprimer un vecteur dans un autre repère, c'est le projeter sur les axes de ce repère.

> [!tip] Widget — `espaces_widget.html`
> Un point déplaçable et trois repères imbriqués — monde, véhicule, tourelle. Le widget
> affiche en direct les coordonnées du point dans les trois, la matrice de passage utilisée,
> et l'effet d'une rotation ou d'une échelle appliquée à un niveau intermédiaire.

---

## Le piège de l'échelle non uniforme

Une échelle différente selon les axes déforme les angles des enfants, et les normales avec.

---

## Du monde à l'écran

Projection puis mise à l'échelle du viewport : la dernière étape, celle qui produit des pixels.

---

## Atelier — 20 min

Convertir un clic de souris en position du monde, puis en position locale d'un objet tourné et mis à l'échelle.

---

## À retenir

Quatre espaces, une chaîne de matrices, l'inverse pour remonter, la transposée quand c'est une rotation — et attention à l'échelle non uniforme.

---

## Questions ?
