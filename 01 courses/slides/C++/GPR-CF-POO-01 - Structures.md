---
title: GPR-CF-POO-01 - Structures
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

# Structures
<!-- .slide: class="title" -->
## GPR-CF-POO-01

<small>Ranger ensemble ce qui va ensemble</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Première séance du bloc POO.

---

## Objectifs

Savoir déclarer une structure, en créer des instances, y accéder, et la passer à une fonction sans la recopier.

**Prérequis :** variables, fonctions, tableaux — [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05]].

---

## Six variables pour un seul ennemi

`posX`, `posY`, `pv`, `degats`, `vitesse`, `nom` : leur cohérence n'existe que dans la tête du programmeur.

> [!tip] Schéma
> À gauche, six variables éparpillées avec des flèches pointillées pour dire « ça va
> ensemble » ; à droite, une seule boîte `Ennemi` qui les contient. Le même schéma sert de
> conclusion en fin de séance.

---

## Une structure, un concept du jeu

Une `struct` donne un nom à un groupe de valeurs, et ce nom devient un type.

---

## Déclarer

La déclaration décrit la forme : elle ne réserve aucune mémoire et ne contient aucune valeur.

---

## Déclaration ou instance

Déclarer `struct Ennemi` ne crée pas d'ennemi ; il faut ensuite en instancier un.

> [!tip] Widget — `struct_memoire_widget.html`
> On compose une structure en ajoutant des champs (`int pv`, `float vitesse`,
> `std::string nom`) ; le widget affiche à gauche la déclaration C++ produite, à droite la
> case mémoire d'une instance avec la valeur de chaque champ, et en bas la taille totale.

---

## Instancier

Chaque instance a ses propres valeurs : deux gobelins partagent leur forme, pas leurs points de vie.

---

## Accéder aux membres

Le point relie l'instance à son champ, et se lit de gauche à droite comme une phrase.

---

## Une structure dans une structure

Un `Transform` contient deux `Vector2` : rien n'interdit d'emboîter, et c'est ainsi qu'on décrit un objet de jeu.

---

## Passer à une fonction

Par valeur, la fonction travaille sur une copie ; par référence, elle modifie l'original.

---

## Un tableau de structures

Une vague d'ennemis est un tableau de `Ennemi`, parcouru comme n'importe quel tableau.

---

## Atelier — 20 min

Décrire le monstre du jeu en une structure, en instancier trois, et écrire la fonction qui affiche sa fiche.

---

## À retenir

Une structure nomme un concept du jeu ; la déclaration décrit, l'instance contient, et la référence évite la copie.

---

## Questions ?
