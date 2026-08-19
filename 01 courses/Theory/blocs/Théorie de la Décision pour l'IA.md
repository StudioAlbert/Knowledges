---
type: bloc
specialisation: "[[Theory]]"
mineur: Games Programming
prerequis:
  - "[[Théorie des Graphes et Recherche de Chemin]]"
projet: []
cours: 4
---

# Théorie de la Décision pour l'IA

Les trois familles de décision d'un agent non joueur, du plus rigide au plus continu, et ce que chacune coûte à écrire et à déboguer.

## Objectifs

- Décrire le modèle du monde dont dispose un agent, et le distinguer du monde réel
- Écrire une machine à états et nommer le seuil où elle devient ingérable
- Lire un arbre de comportement et prévoir son statut de retour
- Noter une action en Utility AI et justifier sa courbe de réponse

## Cours

| # | Cours (1h) | Contenu | Source |
| --- | --- | --- | --- |
| 1 | Percevoir : le modèle du monde | Capteurs, détection contre mémoire, état du monde, cartes d'influence, connaissance partagée d'équipe | [[chapter_1_what_to_sense]] |
| 2 | Machines à états | États, transitions, gardes, hiérarchie, explosion combinatoire des transitions | [[ai_pathfinding_behaviour_tree_state_machine]] |
| 3 | Arbres de comportement | Séquence, sélecteur, décorateur, statut de retour, tick et reprise, nœuds mémoire | [[cpp_behaviour_tree_lecture]] |
| 4 | Utility theory | Considérations, normalisation entre 0 et 1, courbes de réponse, sélection d'action, réglage par variantes | [[unity_ai_utility_ai]] |

## Validation

Même comportement d'agent implémenté deux fois, en machine à états puis en Utility AI, comparaison écrite.

## Liens

- Spécialisation : [[Theory]]
- Prérequis : [[Théorie des Graphes et Recherche de Chemin]]
- Index des blocs : [[index_blocs.base|Index]]
