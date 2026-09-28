---
title: GPR-UN-VRG-14 - Shaders, matériaux, textures, UV
type: slides
status: Backlog
subject: Unity
duration_h: 1
bloc_gsda: VFX, Rendu et Game Feel
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

# Shaders, matériaux, textures, UV
<!-- .slide: class="title" -->
## GPR-UN-VRG-14

<small>Le vocabulaire avant les nœuds</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir ce qu'un shader calcule, distinguer shader et matériau, et comprendre comment une image se pose sur une surface.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-VRG-13 - Les render pipelines|GPR-UN-VRG-13]].

---

## Ce que fait un shader

Un petit programme exécuté pour chaque sommet, puis pour chaque pixel — des millions de fois par image.

---

## Deux étapes

Le premier programme place la géométrie, le second décide de la couleur de chaque pixel.

> [!tip] Schéma
> La chaîne complète : sommets, transformation, découpage en pixels, programme de pixel,
> écriture à l'écran — avec le nombre d'exécutions écrit à chaque étape pour un triangle
> plein écran.

---

## Shader et matériau

Le shader est le programme, le matériau est un jeu de valeurs pour ce programme.

---

## Une texture, quatre canaux

Rouge, vert, bleu, alpha : quatre images en une, et les trois derniers servent souvent à autre chose qu'à la couleur.

---

## Les UV

Chaque sommet porte une coordonnée dans l'image : c'est elle qui décide de ce qui s'affiche où.

> [!tip] Widget — `uv_widget.html`
> Un quad avec ses quatre coordonnées de texture déplaçables à la souris, et la texture
> affichée à côté avec le quadrilatère correspondant dessiné dessus. Des curseurs de
> répétition et de décalage montrent l'effet, et un mode « hors bornes » compare répétition,
> bornage et miroir.

---

## Sortir des bornes

Au-delà de zéro et un, l'image se répète, se borne ou se reflète — c'est un réglage, pas un bug.

---

## Les formats

Compression, mipmaps, taille : ce qui décide du poids en mémoire et de la netteté à distance.

---

## Ce qui coûte

Un échantillonnage de texture coûte cher, une condition dans un programme de pixel coûte parfois plus.

---

## Lire un shader existant

Savoir repérer les entrées, les textures et la sortie suffit à comprendre 90 % des shaders de jeu.

---

## Atelier — 20 min

Déplier les UV d'un cube, y poser un atlas, et montrer l'effet de la répétition et du décalage.

---

## À retenir

Le shader est un programme par pixel, le matériau ses réglages, la texture quatre canaux, et les UV le pont entre les deux.

---

## Questions ?
