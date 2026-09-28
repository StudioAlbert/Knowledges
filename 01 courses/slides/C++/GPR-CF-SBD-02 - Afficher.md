---
title: GPR-CF-SBD-02 - Afficher
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: SFML et Box2D
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

# Afficher
<!-- .slide: class="title" -->
## GPR-CF-SBD-02

<small>Des pixels au bon endroit</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir afficher et déplacer un sprite, cadrer avec une vue, et animer depuis une planche d'images.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-01 - Boucle de jeu et fenêtre|GPR-CF-SBD-01]].

---

## Texture et sprite

La texture est l'image en mémoire, le sprite est ce qu'on en montre : l'une se charge, l'autre se dessine.

---

## Charger une fois, dessiner mille fois

Recharger une texture à chaque image est l'erreur qui fait tomber le framerate à cinq.

---

## Positionner

Le repère écran a son origine en haut à gauche et son axe vertical vers le bas — l'inverse des maths.

---

## L'origine du sprite

Par défaut le coin, souvent le centre : c'est elle qui décide autour de quoi le sprite tourne.

---

## Déplacer au clavier

Lire l'état des touches dans la mise à jour, et non dans les événements, pour un déplacement continu.

---

## La vue, c'est la caméra

Déplacer la vue plutôt que le monde : le joueur reste au centre sans que rien d'autre bouge.

---

## Le redimensionnement

Sans rien faire, la fenêtre agrandie étire l'image : il faut décider entre étirer, border, ou montrer plus.

> [!tip] Widget — `vue_camera_widget.html`
> Un monde dessiné, un rectangle de vue déplaçable, et une fenêtre redimensionnable à la
> souris. Trois boutons montrent les trois politiques — étirement, bandes noires, champ
> élargi — et leurs conséquences sur ce que le joueur voit du niveau.

---

## Le framebuffer

On dessine dans une image cachée, et l'affichage la montre d'un coup : c'est pour ça qu'on efface et qu'on affiche.

---

## La planche de sprites

Une seule texture, des rectangles découpés dedans : moins de fichiers, moins d'appels.

---

## Animer

Un index d'image qui avance avec le temps, et un rectangle qui suit : l'animation n'est que ça.

> [!tip] Widget — `spritesheet_widget.html`
> Une planche de sprites quadrillée. On choisit la ligne, le nombre d'images et la cadence ;
> le widget joue l'animation à côté et affiche le rectangle courant. Un curseur de cadence
> montre où l'animation devient saccadée ou irréaliste.

---

## Atelier — 20 min

Un personnage animé qui marche dans les quatre directions, suivi par la caméra, dans une fenêtre redimensionnable sans déformation.

---

## À retenir

Texture chargée une fois, origine choisie, vue plutôt que monde, et animation pilotée par le temps.

---

## Questions ?
