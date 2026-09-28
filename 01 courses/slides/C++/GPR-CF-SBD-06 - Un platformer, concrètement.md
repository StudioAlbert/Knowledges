---
title: GPR-CF-SBD-06 - Un platformer, concrètement
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

# Un platformer, concrètement
<!-- .slide: class="title" -->
## GPR-CF-SBD-06

<small>Là où la physique rencontre la sensation</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Dernière séance du bloc.

---

## Objectifs

Savoir écrire un contrôleur de plateforme correct, et connaître les astuces qui le rendent agréable.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-05 - Relier physique et graphique|GPR-CF-SBD-05]].

---

## Ce qu'on attend d'un contrôleur

De la précision, de la réactivité, et assez d'indulgence pour que le joueur s'accuse lui-même.

---

## Le vrai problème du saut

Savoir si le personnage est au sol n'est pas une question de position mais de contact.

---

## Le capteur de sol

Une petite forme sous les pieds répond à la question, et elle seule.

---

## Toucher par le côté

Ce n'est pas le fait de toucher qui compte mais l'orientation du contact.

> [!tip] Schéma
> Un personnage contre une plateforme dans quatre situations — dessus, dessous, côté gauche,
> côté droit — avec la normale de contact dessinée et la décision prise dans chaque cas.

---

## Le coyote time

Autoriser le saut quelques centièmes après avoir quitté le bord change tout au ressenti.

---

## Le saut mis en mémoire

Enregistrer l'appui juste avant l'atterrissage évite le saut perdu d'un cheveu.

> [!tip] Widget — `plateforme_widget.html`
> Un réglage de saut en direct : gravité, impulsion, gravité à la descente, coyote time,
> mémoire d'appui. La courbe du saut se dessine à côté et trois préréglages montrent des
> sensations très différentes avec les mêmes formules.

---

## Passer d'une plateforme à l'autre

Le personnage doit pouvoir glisser le long d'un bord sans y rester accroché.

---

## La plateforme à sens unique

On traverse par le bas, on se pose par le haut : le contact s'ignore selon le sens du déplacement.

---

## Le wall jump

Détecter le mur, puis composer une impulsion qui repousse autant qu'elle élève.

---

## Régler, c'est tester

Aucun de ces nombres ne se déduit : ils se trouvent en jouant, et se notent.

---

## Atelier — 20 min

Ajouter au personnage le capteur de sol, le coyote time, la mémoire d'appui, et une plateforme à sens unique.

---

## À retenir

Le sol se détecte par contact, la normale décide, et l'indulgence se règle en centièmes de seconde.

---

## Questions ?
