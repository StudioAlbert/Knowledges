---
title: TC-FT-PCL-01 - Couplage et cohésion
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Principes de Conception Logicielle
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

# Couplage et cohésion
<!-- .slide: class="title" -->
## TC-FT-PCL-01

<small>Pourquoi un petit changement casse tout</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Première séance du bloc.

---

## Objectifs

Savoir lire les dépendances d'un projet, estimer la portée d'un changement, et nommer ce qui rend un code fragile.

---

## Le script de deux mille lignes

Tout le monde en a écrit un : il marche, et plus personne n'ose y toucher.

---

## Dépendance

A dépend de B si changer B peut casser A — c'est la seule définition qui compte.

---

## La direction compte

Que l'interface dépende du gameplay est normal ; l'inverse est une dette.

---

## Couplage

Le couplage se mesure au nombre de choses qu'il faut connaître pour en modifier une.

---

## Cohésion

Une classe est cohésive quand tout ce qu'elle contient parle du même sujet.

---

## La portée d'un changement

La bonne question n'est pas « est-ce que ça marche » mais « qu'est-ce que je dois retester ».

> [!tip] Widget — `couplage_widget.html`
> Le graphe des classes d'un petit jeu. Cliquer une classe allume tout ce que sa
> modification met en danger, et affiche le compte. Un interrupteur « extraire une
> interface » montre le même graphe une fois la dépendance inversée, et le compte qui tombe.

---

## Responsabilité unique

Une classe ne doit avoir qu'une seule raison de changer — pas une seule fonction.

---

## Les symptômes

Un fichier que tout le monde modifie, des noms en `Manager`, des paramètres booléens, et la peur de renommer.

---

## La dette de conception

Elle ne se voit pas dans le jeu, elle se paie en temps à chaque nouvelle fonctionnalité.

---

## Atelier — 20 min

Dessiner le graphe de dépendances d'un projet Unity du groupe, puis désigner la classe dont la modification est la plus coûteuse.

---

## À retenir

Peu de dépendances, dans le bon sens, et chaque classe sur un seul sujet : le reste du bloc n'est que l'application de ces trois phrases.

---

## Questions ?
