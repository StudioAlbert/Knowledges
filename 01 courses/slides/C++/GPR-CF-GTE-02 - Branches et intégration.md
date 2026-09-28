---
title: GPR-CF-GTE-02 - Branches et intégration
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Git et Travail en Équipe
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

# Branches et intégration
<!-- .slide: class="title" -->
## GPR-CF-GTE-02

<small>Travailler à côté, puis revenir</small>

Note:
**Plan de séance — à développer.** Chaque slide porte son titre et sa phrase directrice ;
les widgets et schémas sont décrits, pas encore écrits. `publish: false` tant que le deck
n'est pas rédigé.

---

## Objectifs

Savoir ouvrir une branche, la ramener dans `main` par merge ou par rebase, et résoudre un conflit sans casser le travail des autres.

**Prérequis :** dépôt, commit, remote — [[01 courses/slides/C++/GPR-CF-GTE-01 - Principes et premier dépôt|GPR-CF-GTE-01]].

---

## Pourquoi on ne travaille pas dans `main`

Une branche isole un travail en cours du code qui doit rester jouable.

---

## Créer et changer de branche

`git switch -c saut-double` crée la branche et y bascule d'un seul geste.

---

## Où pointe `HEAD`

Une branche n'est qu'une étiquette sur un commit ; `HEAD` dit sur laquelle vous êtes.

> [!tip] Widget — `git_graph_widget.html`
> Graphe de commits interactif : des boutons *commit*, *branch*, *switch*, *merge* et
> *rebase* font pousser l'historique sous les yeux de l'étudiant, avec `HEAD` et les
> étiquettes de branche qui se déplacent. Le même graphe sert pour les trois slides
> suivantes.

---

## Merge : garder les deux histoires

Le merge fabrique un commit de plus qui joint les deux lignes, et ne touche à rien de ce qui existait.

---

## Rebase : réécrire la sienne

Le rebase rejoue vos commits au-dessus de `main` : l'histoire devient linéaire, mais ce sont de nouveaux commits.

> [!tip] Widget — réutiliser `git_graph_widget.html`
> Deux graphes côte à côte, même départ : *merge* à gauche, *rebase* à droite. Un curseur
> montre quels commits ont changé d'identité.

---

## La règle qui évite les drames

On ne rebase jamais une branche que quelqu'un d'autre a déjà récupérée.

---

## Un conflit n'est pas une erreur

Git s'arrête quand deux branches ont modifié les mêmes lignes : il demande un arbitrage humain.

---

## Résoudre un conflit

On garde ce qui doit vivre, on supprime les marqueurs, on teste, puis on commit la résolution.

> [!tip] Widget — `git_conflict_widget.html`
> Trois panneaux — *ma version*, *la leur*, *résolution* — sur un `GameManager.cs` en
> conflit. L'étudiant compose la résolution ligne à ligne ; le widget refuse de valider
> tant qu'un marqueur de conflit subsiste.

---

## Pull request et revue

La pull request transforme l'intégration en conversation : on propose, on relit, puis on fusionne.

---

## GitHub, GitLab, forge locale

Le même Git en dessous, des services différents au-dessus — et l'école en héberge un.

> [!tip] Schéma
> Un dépôt local au centre, trois remotes autour (GitHub, GitLab, forge SAE) ; les flèches
> montrent que `push` et `pull` sont identiques dans les trois cas.

---

## Atelier — 20 min

Par binôme : deux branches, un conflit provoqué sur le même fichier, une pull request relue par l'autre.

---

## À retenir

Une branche par intention, un rebase avant de proposer, un merge pour intégrer — et jamais de réécriture sur ce qui est partagé.

---

## Questions ?
