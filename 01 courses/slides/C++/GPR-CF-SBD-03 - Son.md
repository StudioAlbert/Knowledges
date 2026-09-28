---
title: GPR-CF-SBD-03 - Son
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

# Son
<!-- .slide: class="title" -->
## GPR-CF-SBD-03

<small>La moitié du ressenti, pour un dixième du travail</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Séance qui clôt le monde graphique du bloc.

---

## Objectifs

Savoir jouer un effet et une musique, choisir lequel des deux, et éviter les deux pièges classiques.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-02 - Afficher|GPR-CF-SBD-02]].

---

## Le son dit au joueur que ça a marché

Un coup sans son n'a pas porté, même si les points de vie ont baissé.

---

## Charger un son

Le fichier devient un tampon de données brutes, exactement comme une image devient une texture.

---

## Les sons courts

Un tir, un pas, un ramassage : tout en mémoire, joué instantanément, et autant de fois qu'on veut.

---

## Les musiques

Trois minutes d'orchestre ne se chargent pas : elles se lisent au fil de la lecture.

> [!tip] Widget — `audio_memoire_widget.html`
> Deux barres de mémoire côte à côte : un effet de 0,3 seconde et une musique de trois
> minutes, avec leur poids décompressé réel. Un bouton « jouer trente sons » montre la
> limite de canaux simultanés et ce qui se passe au-delà.

---

## Le piège du tampon détruit

Un son qui joue pendant que son tampon disparaît donne un silence, ou un crash.

---

## Combien de sons à la fois

Le nombre de canaux est limité : trente explosions simultanées, ce n'est ni utile ni audible.

---

## Volume, hauteur, boucle

Une légère variation de hauteur à chaque tir suffit à faire disparaître l'effet de répétition.

---

## Le son dans l'espace

Un son placé dans le monde s'atténue avec la distance, et le moteur s'en occupe si on le lui dit.

---

## Bilan du monde graphique

Fenêtre, boucle, sprites, caméra, animation, son : de quoi faire un jeu complet, sans une ligne de physique.

---

## Atelier — 20 min

Ajouter au personnage animé un son de pas, un son de saut à hauteur variable, et une musique de fond en boucle.

---

## À retenir

Les effets courts en mémoire, les musiques en flux, les tampons qui survivent à leur lecture, et une variation de hauteur pour ne pas lasser.

---

## Questions ?
