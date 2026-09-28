---
title: TC-FT-GVM-02 - Produits scalaire et vectoriel
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

# Produits scalaire et vectoriel
<!-- .slide: class="title" -->
## TC-FT-GVM-02

<small>Deux opérations, et la moitié des questions du gameplay</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir répondre par un produit scalaire ou vectoriel aux questions d'angle, de côté, de projection et de normale.

**Prérequis :** [[01 courses/slides/Theory/TC-FT-GVM-01 - Vecteurs et repères|TC-FT-GVM-01]].

---

## Deux vecteurs, un nombre

Le produit scalaire mesure à quel point deux directions sont d'accord.

---

## Le signe suffit souvent

Positif, l'ennemi est devant ; négatif, derrière ; nul, exactement sur le côté.

---

## Retrouver l'angle

Divisé par les deux normes, le produit scalaire donne le cosinus de l'angle — donc l'angle.

---

## Projeter

La projection est l'ombre d'un vecteur sur un autre, et elle se calcule sans trigonométrie.

> [!tip] Widget — `produit_scalaire_widget.html`
> Deux vecteurs manipulables à la souris. Le widget affiche le produit scalaire, son signe,
> l'angle, et dessine la projection de l'un sur l'autre avec le rejet en pointillés. Un mode
> « cône de vision » colore le plan selon le signe.

---

## Rejet et décomposition

Tout vecteur se décompose en une part parallèle et une part perpendiculaire à une direction donnée.

---

## Réfléchir

Une balle rebondit en retournant sa composante perpendiculaire au mur, et rien d'autre.

---

## Deux vecteurs, un vecteur

Le produit vectoriel donne une direction perpendiculaire aux deux, et sa longueur mesure l'aire.

---

## Perpendiculaire en 2D et en 3D

En 2D, on échange les composantes et on change un signe ; en 3D, c'est le produit vectoriel.

---

## À gauche ou à droite

Le signe du produit vectoriel en 2D dit de quel côté de sa ligne de regard se trouve la cible.

> [!tip] Widget — `orientation_widget.html`
> Un garde avec sa direction de regard et une cible déplaçable. Le widget affiche le signe
> du produit vectoriel, la réponse « à gauche / à droite / aligné », et colore le demi-plan
> correspondant.

---

## La normale d'une surface

Deux arêtes d'un triangle, un produit vectoriel, et on sait où le triangle regarde.

---

## Aire et volume

La norme du produit vectoriel est l'aire du parallélogramme ; le produit mixte en est le volume.

---

## Indépendance, base, espace

Trois vecteurs de volume nul sont coplanaires : ils ne peuvent pas servir de base.

---

## Atelier — 20 min

Le garde voit-il le joueur : test de distance, test d'angle par produit scalaire, puis côté par produit vectoriel.

---

## À retenir

Le scalaire répond « à quel point d'accord », le vectoriel répond « perpendiculaire à quoi, et de quel côté ».

---

## Questions ?
