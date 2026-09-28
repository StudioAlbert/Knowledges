---
title: GPR-CF-SDS-03 - Entrées-sorties fichier
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

# Entrées-sorties fichier
<!-- .slide: class="title" -->
## GPR-CF-SDS-03

<small>Ce qui doit survivre à la fermeture du jeu</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir lire et écrire un fichier, en texte comme en binaire, et se méfier des trois pièges habituels.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SDS-02 - Adaptateurs et conteneurs associatifs|GPR-CF-SDS-02]].

---

## Ce qui doit survivre au programme

Sauvegardes, réglages, meilleurs scores, niveaux : tout ce qu'on ne veut pas recompiler pour changer.

---

## Ouvrir

Ouvrir peut échouer, et un flux qui a échoué se comporte comme un fichier vide.

---

## Toujours fermer

Le destructeur du flux ferme pour vous : c'est la même idée que le destructeur de la séance POO.

---

## Lire en flux

L'extraction avance toute seule et s'arrête sur ce qu'elle ne comprend pas.

---

## Lire ligne par ligne

Pour un fichier de configuration, la ligne est la bonne unité — et se découpe ensuite.

---

## Le curseur

Le flux garde une position de lecture ; revenir au début est un geste explicite.

> [!tip] Widget — `fichier_curseur_widget.html`
> Les octets d'un petit fichier de sauvegarde affichés en ligne, avec le curseur de lecture
> qui avance à chaque opération. Un interrupteur bascule l'affichage entre texte et
> hexadécimal pour montrer que c'est la même donnée lue de deux façons.

---

## Écrire en flux

L'insertion formate : un nombre devient des caractères, et se relit comme tel.

---

## Texte ou binaire

Le texte se lit dans un éditeur mais pèse plus et se parse ; le binaire est compact, exact, et illisible.

---

## Le piège du chemin relatif

Le chemin est relatif au répertoire de travail, qui n'est pas celui de l'exécutable.

---

## Ce qui casse une sauvegarde

Un format sans numéro de version : la partie d'hier ne se relit plus après une mise à jour.

---

## Atelier — 20 min

Lire un fichier de réglages ligne par ligne, écrire le meilleur score, puis sauvegarder l'état du joueur en binaire.

---

## À retenir

Vérifier l'ouverture, laisser le destructeur fermer, choisir texte ou binaire en connaissance de cause, et versionner tout format de sauvegarde.

---

## Questions ?
