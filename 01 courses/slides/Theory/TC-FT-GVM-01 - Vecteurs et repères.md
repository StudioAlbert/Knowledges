---
title: TC-FT-GVM-01 - Vecteurs et repères
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Géométrie Vectorielle et Matricielle
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

# Vecteurs et repères
<!-- .slide: class="title" -->
## TC-FT-GVM-01

<small>La brique de tout ce qui bouge</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Première séance du bloc.

---

## Objectifs

Savoir lire, mesurer, normaliser et combiner des vecteurs, et savoir dans quel repère on travaille.

---

## Un nombre ne suffit pas

Une vitesse de 5 ne dit pas où l'on va : il manque la direction.

---

## Composantes

Un vecteur est une liste de nombres, une par axe, et rien d'autre.

---

## Le dessin qui ne trompe pas

Une flèche a une direction et une longueur, mais pas de point de départ imposé.

> [!tip] Widget — `vecteur_widget.html`
> Un plan cartésien où l'on attrape l'extrémité d'un vecteur à la souris. Le widget affiche
> en direct ses composantes, sa norme et sa version normalisée, et un second vecteur permet
> de visualiser somme et différence par la règle du parallélogramme. Il resservira en
> `TC-FT-GVM-02`.

---

## Norme

La norme est la longueur de la flèche, et c'est Pythagore appliqué aux composantes.

---

## Normaliser

Diviser par sa norme donne une direction pure, de longueur 1 — ce qu'on veut pour viser.

---

## Multiplier par un scalaire

Le scalaire étire ou retourne le vecteur, sans changer sa droite support.

---

## Additionner

Deux déplacements enchaînés valent leur somme : c'est ainsi qu'on compose vitesse et vent.

---

## Soustraire

`cible - joueur` est le vecteur qui va de l'un vers l'autre — la question que le jeu pose sans arrêt.

---

## Le vecteur nul et les règles du jeu

L'addition est commutative et associative, le vecteur nul ne change rien — et il ne se normalise pas.

---

## Du vecteur à la structure de données

En mémoire, un vecteur est trois nombres nommés `x`, `y`, `z`, ou indexés de 0 à 2.

---

## Repères directs et indirects

Selon le moteur, l'axe vertical est `y` ou `z`, et la main qui décrit la rotation change.

> [!tip] Schéma
> Trois trièdres côte à côte — Unity, Unreal, et le repère mathématique usuel — avec la
> main droite ou gauche dessinée dessous et la couleur de chaque axe.

---

## Atelier — 20 min

Calculer la direction et la distance entre deux positions du niveau, puis en déduire une vitesse de déplacement constante.

---

## À retenir

Soustraire donne la direction, la norme donne la distance, normaliser sépare les deux — et on vérifie toujours dans quel repère on est.

---

## Questions ?
