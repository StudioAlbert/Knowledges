---
type: bloc
specialisation: "[[Theory]]"
mineur: Games Programming
prerequis:
  - "[[Complexité et Coût des Algorithmes]]"
projet: []
cours: 4
---

# Théorie des Graphes et Recherche de Chemin

Le graphe comme modèle : d'abord le vocabulaire et les parcours, ensuite seulement les algorithmes de plus court chemin.

## Objectifs

- Modéliser un problème de jeu sous forme de graphe et choisir sa représentation
- Dérouler un parcours en largeur et en profondeur, et dire lequel répond à quelle question
- Expliquer la relaxation d'arête au cœur de Dijkstra
- Justifier une heuristique A* par son admissibilité

## Cours

| # | Cours (1h) | Contenu | Source |
| --- | --- | --- | --- |
| 1 | Graphes : vocabulaire et représentations | Sommets, arêtes, orientation, pondération, matrice d'adjacence contre liste d'adjacence, grille comme graphe implicite | [[Maths, algorithmie - Theorie des graphes]] |
| 2 | Parcours | Largeur et profondeur, file contre pile, composantes connexes, détection de cycle, ordre topologique | [[Maths, algorithmie - Theorie des graphes]] |
| 3 | Plus court chemin | Relaxation, Dijkstra, file de priorité, pourquoi les poids négatifs cassent tout | — |
| 4 | A* et heuristiques | Fonction f = g + h, admissibilité et cohérence, comparaison avec Dijkstra, choix d'heuristique sur grille | [[cpp_a_star_]] |

## Validation

Comparaison mesurée de deux heuristiques A* sur une même carte, résultats commentés.

## Liens

- Spécialisation : [[Theory]]
- Prérequis : [[Complexité et Coût des Algorithmes]]
- Index des blocs : [[index_blocs.base|Index]]
