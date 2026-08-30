---
type: bloc
specialisation: "[[01 courses/PCG/intro|PCG]]"
mineur: Games Programming
prerequis:
  - "[[Fondamentaux de la génération procédurale]]"
projet: []
cours: 6
---

# Algorithmes de génération

Les familles d'algorithmes qui produisent réellement une carte : graphes, automates cellulaires, et effondrement de fonction d'onde.

## Objectifs

- Modéliser un niveau comme un graphe et en générer une topologie jouable
- Implémenter un automate cellulaire et régler ses règles pour obtenir une caverne exploitable
- Expliquer le cycle observe / effondre / propage de WaveFunctionCollapse
- Diagnostiquer une contradiction WFC et choisir une stratégie de reprise

## Cours

<!-- cours:auto -->

| # | Cours | Heures | Lien |
| --- | --- | --- | --- |
| 1 | Graphs & Cellular Automata | 3 | [[pcg_graph_cellular_automaton]] |
| 2 | WaveFunctionCollapse | 3 | [[pcg_wave_function_collapse]] |

**Total : 2 cours, 6 h.**

<!-- /cours:auto -->

## Validation

Une carte générée par l'une des trois familles, avec le jeu de contraintes qui garantit qu'elle est toujours traversable.

## Liens

- Spécialisation : [[01 courses/PCG/intro|PCG]]
- Prérequis : [[Fondamentaux de la génération procédurale]]
- Théorie associée : [[Théorie des Graphes et Recherche de Chemin]]
- Index des cours : [[index_cours.base|Index]]
