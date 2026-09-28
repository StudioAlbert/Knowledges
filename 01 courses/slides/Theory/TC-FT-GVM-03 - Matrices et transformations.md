---
title: TC-FT-GVM-03 - Matrices et transformations
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

# Matrices et transformations
<!-- .slide: class="title" -->
## TC-FT-GVM-03

<small>Une matrice, c'est un mouvement écrit</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Séance dense : le déterminant et les coordonnées homogènes sont
les deux points à ne pas sacrifier.

---

## Objectifs

Savoir lire une matrice comme une transformation, composer dans le bon ordre, et comprendre ce que dit son déterminant.

**Prérequis :** [[01 courses/slides/Theory/TC-FT-GVM-02 - Produits scalaire et vectoriel|TC-FT-GVM-02]].

---

## Une matrice, c'est une transformation

Ses colonnes disent où partent les axes : tout le reste en découle.

---

## Taille, entrées, diagonale

Lignes par colonnes, l'ordre est une convention qu'on ne discute pas mais qu'on vérifie.

---

## La transposée

Échanger lignes et colonnes ; une matrice symétrique ne change pas, une antisymétrique change de signe.

---

## Additionner

Terme à terme, et seulement entre matrices de même taille — sans intérêt géométrique particulier.

---

## Multiplier, c'est composer

Le produit de deux matrices est la transformation qui applique l'une puis l'autre.

---

## L'ordre compte

Tourner puis déplacer ne donne pas déplacer puis tourner, et le produit non plus.

> [!tip] Widget — `matrice_widget.html`
> Un carré unité et une matrice deux par deux éditable, avec les deux vecteurs colonnes
> dessinés. Le carré se déforme en direct ; deux matrices peuvent être composées dans les
> deux ordres pour voir la différence, et le déterminant est affiché comme l'aire du
> parallélogramme obtenu.

---

## L'identité

Celle qui ne fait rien : le point de départ, et le test de toute implémentation.

---

## Le déterminant

Il mesure comment l'aire — ou le volume — est multipliée, et son signe dit si l'orientation s'inverse.

---

## Les transformations du plan

Rotation, mise à l'échelle, réflexion, cisaillement : quatre matrices à reconnaître d'un coup d'œil.

---

## La translation ne rentre pas

Déplacer n'est pas une multiplication : c'est pour cela qu'on ajoute une dimension.

---

## Les coordonnées homogènes

Une composante de plus, et la translation devient une matrice comme les autres.

---

## La matrice orthogonale

Rotation pure, sans déformation : son inverse est sa transposée, et c'est très pratique.

---

## L'ordre des opérations

Échelle, puis rotation, puis translation : la convention des moteurs, et la source de la moitié des bugs.

---

## Atelier — 20 min

Composer à la main la matrice qui place un sprite : échelle, rotation, position — puis vérifier sur trois points.

---

## À retenir

Les colonnes disent où vont les axes, le produit compose, l'ordre compte, le déterminant mesure l'aire et l'orientation.

---

## Questions ?
