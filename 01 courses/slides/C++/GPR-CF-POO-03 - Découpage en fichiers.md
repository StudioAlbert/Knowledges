---
title: GPR-CF-POO-03 - Découpage en fichiers
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Programmation Orientée Objet
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

# Découpage en fichiers
<!-- .slide: class="title" -->
## GPR-CF-POO-03

<small>Ce qu'on promet, et où on le tient</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir séparer une classe en `.h` et `.cpp`, protéger un en-tête de la double inclusion, et décider ce qui se montre.

**Prérequis :** classes et visibilité — [[01 courses/slides/C++/GPR-CF-POO-02 - Classes et visibilité|GPR-CF-POO-02]].

---

## Un seul fichier, jusqu'au jour où

À 800 lignes, `main.cpp` devient illisible, et deux personnes ne peuvent plus y travailler en même temps.

---

## Le header promet, le source tient

L'en-tête annonce ce qui existe ; le source dit comment ça marche.

---

## Ce que voit vraiment le compilateur

Une inclusion est un copier-coller : le compilateur ne voit qu'un seul long fichier par unité de compilation.

> [!tip] Schéma
> Trois fichiers à gauche (`main.cpp`, `Joueur.h`, `Vector2.h`), à droite l'unique fichier
> que le préprocesseur fabrique, blocs recopiés et surlignés. Les flèches donnent l'ordre
> de recopie.

---

## Quand le même en-tête arrive deux fois

Deux inclusions du même en-tête déclarent deux fois la même classe, et le compilateur refuse.

---

## Gardes d'inclusion

Une garde fait ignorer la deuxième lecture d'un en-tête, et `#pragma once` en est la version courte.

> [!tip] Widget — `inclusion_widget.html`
> Le graphe d'inclusions d'un mini projet, avec un interrupteur qui active ou coupe les
> gardes. Le widget compte combien de fois chaque en-tête est lu et affiche l'erreur de
> redéfinition exacte quand on les retire.

---

## Ce qui va dans l'en-tête

La classe, ses membres, la signature de ses méthodes — et rien qui coûte à compiler.

---

## Ce qui reste dans le source

Le corps des méthodes, les détails, et les inclusions dont seul le code a besoin.

---

## Inclure le moins possible

Un en-tête qui inclut tout fait recompiler tout le projet au moindre changement.

---

## Le projet suit

Chaque source ajouté se déclare dans le `CMakeLists.txt` ; l'en-tête, lui, n'y apparaît pas.

---

## Atelier — 20 min

Sortir la classe `Joueur` de `main.cpp` vers son duo de fichiers, avec garde d'inclusion, et recompiler.

---

## À retenir

Un concept par duo de fichiers, une garde par en-tête, et dans l'en-tête seulement ce que les autres doivent savoir.

---

## Questions ?
