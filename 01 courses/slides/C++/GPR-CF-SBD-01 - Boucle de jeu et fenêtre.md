---
title: GPR-CF-SBD-01 - Boucle de jeu et fenêtre
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

# Boucle de jeu et fenêtre
<!-- .slide: class="title" -->
## GPR-CF-SBD-01

<small>Ce qui tourne soixante fois par seconde</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Première séance du bloc SFML et Box2D.

---

## Objectifs

Savoir ouvrir une fenêtre, écrire une boucle de jeu correcte, et rendre le mouvement indépendant du framerate.

**Prérequis :** classes et CMake — [[01 courses/slides/C++/GPR-CF-EDC-03  - Premier projet CMake|GPR-CF-EDC-03]].

---

## Un jeu est une boucle

Lire les entrées, mettre à jour le monde, dessiner — et recommencer jusqu'à ce qu'on ferme la fenêtre.

---

## Deux mondes

Le monde graphique montre, le monde physique décide : ce sont deux jeux de données qu'il faudra relier.

---

## Ce qu'un moteur fait pour vous

Fenêtre, images, sons, entrées, temps : ce que personne n'a envie de réécrire.

---

## SFML, module par module

Fenêtre, graphique, audio, système, réseau — chacun utile, aucun obligatoire.

---

## Ouvrir une fenêtre

Trois lignes suffisent, et la fenêtre se referme aussitôt si on oublie la boucle.

---

## La boucle, dans le bon ordre

Événements, mise à jour, effacement, dessin, affichage : inverser deux étapes se voit immédiatement.

> [!tip] Widget — `boucle_de_jeu_widget.html`
> La frise d'une image : les blocs entrées, mise à jour, rendu, attente. Un curseur règle le
> temps de calcul et le widget montre le framerate obtenu. Un second mode fait courir deux
> personnages, l'un déplacé par image et l'autre par seconde, à 30 puis à 144 images par
> seconde — la démonstration de la séance.

---

## Les événements

Fermer la fenêtre est un événement comme un autre : sans lui, le programme ne s'arrête pas.

---

## Le temps entre deux images

La durée de l'image précédente est la seule mesure fiable du temps qui passe.

---

## Limiter le framerate

Plafonner ou se synchroniser à l'écran, c'est éviter de faire tourner le ventilateur pour rien.

---

## Le piège du déplacement par image

Ajouter deux pixels par image donne un jeu deux fois plus rapide sur une machine deux fois plus rapide.

---

## Atelier — 20 min

Une fenêtre, un carré déplaçable au clavier, un framerate affiché, et un mouvement identique à 30 et à 144 images par seconde.

---

## À retenir

Une boucle dans le bon ordre, les événements traités, et toute vitesse exprimée par seconde — jamais par image.

---

## Questions ?
