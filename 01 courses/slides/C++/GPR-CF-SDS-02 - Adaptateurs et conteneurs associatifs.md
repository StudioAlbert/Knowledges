---
title: GPR-CF-SDS-02 - Adaptateurs et conteneurs associatifs
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

# Adaptateurs et conteneurs associatifs
<!-- .slide: class="title" -->
## GPR-CF-SDS-02

<small>Choisir son conteneur, c'est choisir son accès</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir reconnaître un besoin de file, de pile, ou d'accès par clé, et choisir le conteneur qui va avec.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SDS-01 - Séquences|GPR-CF-SDS-01]].

---

## La seule bonne question

Comment vais-je chercher mes données : par position, par ordre d'arrivée, ou par nom ?

---

## La file

Premier arrivé, premier servi : les actions du joueur, les messages réseau, les ennemis à faire apparaître.

---

## La pile

Dernier arrivé, premier servi : l'annulation, les écrans empilés, le parcours en profondeur.

---

## File ou pile

Le même algorithme de recherche de chemin explore large avec une file, et profond avec une pile.

> [!tip] Schéma
> La même grille explorée deux fois, à gauche avec une file et à droite avec une pile, avec
> l'ordre de visite numéroté dans chaque case — la différence saute aux yeux.

---

## Chercher par clé

La table associative range des valeurs sous des clés, et retrouve sans parcourir.

---

## L'ensemble

Quand seule l'appartenance compte, l'ensemble dit oui ou non, sans doublon possible.

---

## Trié ou pas

La version triée parcourt dans l'ordre ; la version hachée cherche plus vite mais ne promet aucun ordre.

> [!tip] Widget — `conteneurs_widget.html`
> On décrit son besoin en trois clics — j'ajoute où, je cherche comment, l'ordre
> importe-t-il — et le widget désigne le conteneur, son coût par opération, et ce qu'il
> refuse de faire. Un second onglet fait courir une recherche sur cent mille clés dans les
> deux versions.

---

## Ce que chaque opération coûte

Ajouter, chercher, supprimer, parcourir : quatre colonnes, et aucun conteneur gagnant partout.

---

## Ce que la clé doit savoir faire

Trié, elle doit se comparer ; haché, elle doit se hacher — un type maison n'y a pas droit gratuitement.

---

## Atelier — 20 min

Une file d'actions, une pile d'annulation, un inventaire par nom, et un ensemble de succès obtenus.

---

## À retenir

L'accès dicte le conteneur, l'ordre coûte, le hachage va vite — et le vecteur reste souvent la bonne réponse.

---

## Questions ?
