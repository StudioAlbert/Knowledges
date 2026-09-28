---
title: GPR-CF-SDS-06 - Les algorithmes, un par un
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

# Les algorithmes, un par un
<!-- .slide: class="title" -->
## GPR-CF-SDS-06

<small>Le catalogue, et le piège qu'il contient</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Dernière séance du bloc.

---

## Objectifs

Savoir quel algorithme répond à quelle question, et connaître l'idiome de suppression qui trompe tout le monde.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SDS-05 - Itérateurs et algorithmes|GPR-CF-SDS-05]].

---

## Un catalogue, pas une liste à apprendre

On ne retient pas les noms : on retient les six intentions, et on cherche le nom au moment voulu.

---

## Copier

Copier un intervalle, ou seulement ce qui satisfait une condition, vers une autre séquence.

---

## Compter

Compter les éléments égaux à une valeur, ou ceux qui satisfont un prédicat.

---

## Chercher

Trouver le premier qui convient — et se souvenir que « pas trouvé » se compare à la fin, pas à zéro.

---

## Supprimer, en deux temps

L'algorithme de suppression ne supprime rien : il range ce qui reste au début et rend la nouvelle fin.

> [!tip] Widget — `remove_erase_widget.html`
> Un vecteur d'ennemis dessiné en cases. L'étape de suppression déplace les survivants vers
> la gauche et laisse une traîne d'éléments périmés, avec la taille du conteneur inchangée ;
> l'étape suivante coupe la traîne. Un bouton « oublier la deuxième étape » montre le bug
> qu'on voit tous les ans.

---

## La version qui fait tout

La forme moderne fait les deux étapes d'un coup et supprime vraiment.

---

## Trier, mélanger

Trier avec un comparateur maison, mélanger avec un générateur explicite — jamais avec l'ancien tirage.

---

## Les questions

Est-ce que tous, au moins un, aucun : trois algorithmes pour trois questions fréquentes.

---

## Les permutations

Énumérer les ordres possibles, ou faire tourner une séquence sans la recopier.

---

## Les ensembles

Union, intersection, différence : disponibles sur des séquences triées, sans conteneur associatif.

---

## Déplacer plutôt que copier

Déplacer transfère le contenu et laisse la source vide : gratuit quand la copie est chère.

---

## Atelier — 20 min

Nettoyer la vague d'ennemis morts, trier les survivants par menace, et fusionner deux listes de butin.

---

## À retenir

Six intentions, un catalogue à consulter, l'idiome de suppression en deux temps, et le déplacement quand la copie coûte.

---

## Questions ?
