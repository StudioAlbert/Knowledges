---
type: bloc
specialisation: "[[C++]]"
mineur: Games Programming
prerequis:
  - "[[Generique, prog fonctionnelle]]"
  - "[[Patterns]]"
projet:
  - "[[City Builder]]"
cours: 10
---

# IA en C++

Faire décider et se déplacer un agent : recherche de chemin sur une grille, puis structuration de son comportement.

## Objectifs

- Implémenter A* et en justifier l'heuristique
- Profiler et optimiser une recherche de chemin sur une carte réelle
- Structurer un comportement en arbre : séquence, sélecteur, décorateur
- Lire et étendre une implémentation existante plutôt que la réécrire

## Cours

<!-- cours:auto -->

| # | Cours | Heures | Lien |
| --- | --- | --- | --- |
| 1 | A* — Pathfinding en C++ moderne | 3 | [[cpp_a_star_]] |
| 2 | Behaviour Trees en C++ moderne | 4 | [[cpp_behaviour_tree_lecture]] |
| 3 | Setup — vcpkg, CMake | 3 | [[Maths, algorithmie - Theorie des graphes]] |

**Total : 3 cours, 10 h.**

<!-- /cours:auto -->

## Validation

Agent du City Builder qui trouve son chemin et enchaîne ses tâches par arbre de comportement.

## Liens

- Spécialisation : [[C++]]
- Prérequis : [[Generique, prog fonctionnelle]] · [[Patterns]]
- Bloc suivant : —
- Index des cours : [[index_cours.base|Index]]
