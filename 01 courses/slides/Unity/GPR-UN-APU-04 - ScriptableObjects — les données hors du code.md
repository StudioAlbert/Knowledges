---
title: GPR-UN-APU-04 - ScriptableObjects — les données hors du code
type: slides
status: Backlog
subject: Unity
duration_h: 1
bloc_gsda: Architecture et Patterns Unity
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

# ScriptableObjects
<!-- .slide: class="title" -->
## GPR-UN-APU-04

<small>Les données hors du code</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir sortir les réglages du code vers des assets, et rendre le jeu modifiable sans recompiler.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-APU-01 - SOLID en Unity|GPR-UN-APU-01]].

---

## Les chiffres écrits dans le code

Changer l'équilibrage demande un programmeur, une compilation, et un commit — pour rien.

---

## Un asset qui ne contient que des données

Un `ScriptableObject` est un fichier du projet, pas un objet de la scène.

---

## Asset ou instance de scène

L'un existe une fois dans le projet, l'autre autant de fois qu'on en pose dans le niveau.

> [!tip] Schéma
> Deux colonnes : le projet avec ses assets de configuration, la scène avec ses instances,
> et les flèches de référence qui vont toujours de la scène vers l'asset — jamais l'inverse.

---

## Créer le sien

Une classe, un attribut de menu, et l'asset se crée par un clic droit.

---

## Ce qu'un designer peut en faire

Régler, dupliquer, comparer, versionner — sans ouvrir l'éditeur de code.

---

## Vingt armes, zéro ligne de plus

Chaque variante est un asset : le prefab et le script restent uniques.

> [!tip] Widget — `scriptableobject_widget.html`
> Un prefab d'ennemi au centre, trois assets de configuration à gauche. Glisser un asset
> change les statistiques affichées sans toucher au prefab. Un bouton « modifier pendant le
> jeu » montre la valeur qui reste modifiée après l'arrêt — le piège de la séance.

---

## Le piège de l'état partagé

Un asset modifié à l'exécution garde sa nouvelle valeur dans l'éditeur, et parfois dans le build.

---

## Ce qu'on y met, ce qu'on n'y met pas

Des réglages et des données de référence, oui ; l'état courant d'une partie, non.

---

## Organiser ses assets

Un dossier par famille, un nom qui se lit, et des valeurs par défaut qui tiennent debout.

---

## Atelier — 20 min

Sortir les statistiques des trois ennemis du Dungeon Crawler vers des assets, et en créer deux variantes sans code.

---

## À retenir

Les données dans des assets, le code générique, l'état de partie ailleurs — et attention à ce qui reste modifié après l'arrêt.

---

## Questions ?
