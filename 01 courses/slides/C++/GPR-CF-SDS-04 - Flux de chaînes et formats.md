---
title: GPR-CF-SDS-04 - Flux de chaînes et formats
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

# Flux de chaînes et formats
<!-- .slide: class="title" -->
## GPR-CF-SDS-04

<small>Des données que le designer peut écrire</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir découper et fabriquer des chaînes avec un flux, lire un format structuré, et valider ce qu'on lit.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SDS-03 - Entrées-sorties fichier|GPR-CF-SDS-03]] et les chaînes de `GPR-CF-BDP-06`.

---

## Une chaîne qu'on lit comme un fichier

Le flux de chaînes applique à une chaîne tout ce qu'on sait faire sur un fichier.

---

## Découper une ligne

Extraire un mot, un nombre, un mot : le flux s'arrête tout seul aux séparateurs.

---

## Fabriquer une chaîne

Assembler du texte et des nombres sans concaténation laborieuse, et sans fichier.

---

## Pourquoi un format structuré

Un fichier maison marche jusqu'au jour où il faut y ajouter un champ.

---

## XML

Verbeux, mais explicite et outillé : encore partout dans les chaînes de production.

---

## JSON

Compact, lisible, et suffisant pour presque toutes les données de jeu.

---

## Un exemple commenté

La fiche d'une arme : nom, dégâts, cadence, liste d'effets, sous-objet de réglages.

> [!tip] Widget — `json_schema_widget.html`
> Un éditeur de fiche d'arme en JSON, avec son schéma à côté. Chaque frappe revalide : champ
> manquant, type faux, valeur hors bornes, champ inconnu — le widget affiche le message
> d'erreur qu'un bon chargeur devrait produire.

---

## Le schéma

Ce qui est obligatoire, ce qui est optionnel, et quelles valeurs sont admises — écrit noir sur blanc.

---

## Valider ce qu'on lit

Un fichier de données vient du disque, donc de n'importe où : on ne le croit jamais sur parole.

---

## Ce que font les moteurs

Unity sérialise ses assets exactement comme ça, avec un schéma implicite et des valeurs par défaut.

---

## Atelier — 20 min

Lire une fiche d'arme en JSON, la valider champ par champ, et refuser proprement un fichier incomplet.

---

## À retenir

Le flux de chaînes découpe et assemble, un format structuré survit aux évolutions, et toute donnée lue se valide.

---

## Questions ?
