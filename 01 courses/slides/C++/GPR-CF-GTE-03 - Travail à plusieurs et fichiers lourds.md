---
title: GPR-CF-GTE-03 - Travail à plusieurs et fichiers lourds
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Git et Travail en Équipe
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

# Travail à plusieurs et fichiers lourds
<!-- .slide: class="title" -->
## GPR-CF-GTE-03

<small>Un dépôt de jeu, ce n'est pas que du texte</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Dernière séance du bloc.

---

## Objectifs

Savoir travailler avec un dépôt distant, nommer ses versions, et empêcher un projet de jeu de devenir injouable à cloner.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-GTE-02 - Branches et intégration|GPR-CF-GTE-02]].

---

## Le dépôt qui n'est pas sur votre machine

Un remote n'est qu'une adresse et un nom : `origin` n'a rien de magique.

---

## `fetch`, `pull`, `push`

`fetch` regarde, `pull` regarde et intègre, `push` publie — et seul `pull` peut vous surprendre.

> [!tip] Schéma
> Trois zones — dépôt local, remote, copie de travail — et les trois commandes dessinées
> comme des flèches entre elles, avec ce que chacune touche et ce qu'elle ne touche pas.

---

## Écrire un message qui servira

Le message s'écrit pour celui qui cherchera la cause d'un bug dans six mois.

---

## Marquer une version

Un tag épingle le commit exact d'un build jouable : c'est ce qu'on rend, et ce qu'on retrouve.

---

## Les sous-modules

Un dépôt dans un dépôt, utile pour partager un moteur ou un projet compagnon entre plusieurs jeux.

---

## Le piège du sous-module

Le parent ne retient pas une branche mais un commit précis : oublier de le mettre à jour est l'erreur classique.

---

## Pourquoi Git déteste les binaires

Une texture modifiée dix fois, c'est dix textures stockées : l'historique garde tout, pour toujours.

> [!tip] Widget — `git_poids_widget.html`
> Un simulateur de dépôt : on choisit un nombre de textures, leur poids, et le nombre de
> modifications. Le widget affiche la taille du clone en Git nu, puis la même avec LFS, et
> le temps de clonage estimé en salle.

---

## `.gitattributes`

C'est là qu'on déclare ce qui est binaire, comment traiter les fins de ligne, et ce qui ne doit jamais être fusionné.

---

## Git LFS

Le dépôt ne stocke plus le fichier mais un pointeur ; le fichier vit à côté.

---

## Ce qui ne doit jamais entrer

Les dossiers générés, les builds, les caches d'éditeur : tout ce qui se reconstruit se régénère.

---

## Atelier — 20 min

Préparer le dépôt du projet de jeu : ignore, attributes, LFS sur les textures et les sons, et un tag sur la première version jouable.

---

## À retenir

Un remote nommé, des messages utiles, des versions taguées, et les gros fichiers déclarés avant le premier commit — pas après.

---

## Questions ?
