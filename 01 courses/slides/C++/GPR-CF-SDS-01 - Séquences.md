---
title: GPR-CF-SDS-01 - Séquences
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Structures de Données et STL
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

# Séquences
<!-- .slide: class="title" -->
## GPR-CF-SDS-01

<small>Ranger une série, et savoir ce que ça coûte</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Première séance du bloc.

---

## Objectifs

Savoir choisir entre tableau fixe, vecteur et liste, et savoir ce que chaque opération coûte.

**Prérequis :** tableaux — [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05]].

---

## Trois façons de ranger une série

Taille figée, taille qui change, ou éléments éparpillés : le choix se fait sur l'usage, pas sur le goût.

---

## Le tableau de taille fixe

Sa taille est connue à la compilation, il vit sur la pile, et il ne coûte rien.

---

## La pile et le tas

Ce qui est sur la pile disparaît avec la portée ; ce qui est sur le tas se demande et se rend.

> [!tip] Schéma
> Deux colonnes, pile et tas, avec un tableau fixe dans l'une et les données d'un vecteur
> dans l'autre — l'objet vecteur restant sur la pile avec son pointeur, sa taille et sa
> capacité.

---

## Le vecteur

Il grandit quand on lui ajoute des éléments, et c'est le conteneur par défaut.

---

## Croissance et réallocation

Quand la capacité est atteinte, tout déménage : les adresses changent, et ce qui les retenait devient faux.

> [!tip] Widget — `vector_croissance_widget.html`
> On ajoute des éléments un par un ; le widget montre la taille, la capacité, le moment
> exact du déménagement et l'adresse du premier élément qui change. Un bouton `reserve`
> montre les déménagements qui n'ont plus lieu.

---

## Les opérations et leur prix

Ajouter à la fin est gratuit en moyenne, insérer au début décale tout le reste.

---

## Accès indexé

L'accès direct est immédiat, et ne vérifie rien — sauf avec `at()`.

---

## La liste chaînée

Chaque élément sait où est le suivant : insérer au milieu ne déplace personne.

---

## C'est la mémoire qui décide

Un vecteur est contigu, donc le processeur le devine ; une liste saute partout, donc il attend.

---

## Le verdict

En pratique, on prend un vecteur — et on justifie toute autre réponse par une mesure.

---

## Atelier — 20 min

Remplir un vecteur de mille ennemis en observant sa capacité, puis comparer l'insertion en tête et en queue.

---

## À retenir

Taille fixe si elle est connue, vecteur par défaut, liste seulement sur preuve — et jamais d'adresse conservée à travers une réallocation.

---

## Questions ?
