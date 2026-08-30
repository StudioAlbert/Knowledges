---
title: Import slides AI / PCG — doublons
type: historique
date: 2026-08-30
---

# Import des slides Google « AI » et « PCG » — rapport de doublons

Import du dossier Drive
[*Cours*](https://drive.google.com/drive/folders/1930LEpQopdJ0lx9Jf_W4crc5FyQv7c1Y),
13 présentations numérotées `00` → `10`, réparties en deux cours du vault :

| Cours | Decks | Notes créées |
| --- | --- | --- |
| [[01 courses/PCG/intro\|PCG]] | `00` → `03` | 4 cours, 1 feuille d'exercices, 1 annexe |
| [[01 courses/AI/intro\|AI]] | `04` → `10` | 6 cours, 1 ressource |

Les trois sous-dossiers Drive (*Game design*, *Level Design*, *UX - UI*) sont hors
périmètre et n'ont pas été importés.

Rien n'a été supprimé ni fusionné. Ce document liste ce qui se recouvre, pour
arbitrage.

## 1. Recouvrement total — à trancher

### 09 Decisions algorithms ≈ `ai_decision_making_lecture.md`

[[ai_decision_algorithms]] (nouveau) et
[[ai_decision_making_lecture]] (déjà dans le vault, dans
`01 courses/Game programming - Généralités/`) sont **le même cours**.

- même titre de deck : *AI Fundamentals / Decision Making*
- même plan : AI Engine → State Pattern → Behaviour Trees → GOAP
- mêmes exemples : l'Animator Unity comme FSM, l'arbre « Have dinner »,
  le workshop du voleur, les mêmes références GOAP

La note existante est **plus développée** (~50 slides, taxonomie des nœuds,
exemple « fully expanded », section *Recap*) : elle a manifestement déjà été
rédigée à partir de ce même deck.

> **Décision à prendre** : garder une seule des deux. Si c'est
> `ai_decision_making_lecture.md`, la déplacer dans `01 courses/AI/cours/`,
> lui donner `bloc: "[[Decision Making]]"` et `duration_h`, et supprimer
> [[ai_decision_algorithms]]. Sinon l'inverse. En l'état les deux existent.

### 10 Unity Advanced ≈ `singletons_in_unity.md`

Le deck `10` ne parle **pas d'IA** : c'est un cours d'architecture Unity sur les
classes statiques, le singleton et le service locator. Il recouvre
[[singletons_in_unity]] (6 h, bloc *Architecture et Design Patterns*), qui est
nettement plus complet — code C# et captures d'écran.

Il a donc été rangé en `01 courses/AI/ressources/ai_unity_advanced.md` plutôt
qu'en `cours/`, sans `duration_h` ni `bloc`, pour ne pas polluer le curriculum
IA. **Il est probablement à supprimer** : la note Unity le remplace entièrement.

## 2. Recouvrements partiels — angles différents, à conserver

Ceux-là ne sont pas des doublons : le cours importé traite la théorie, la note
existante traite l'implémentation dans un moteur ou un langage. À croiser par
des liens plutôt qu'à fusionner.

| Cours importé | Note existante | Angle de la note existante |
| --- | --- | --- |
| [[ai_pathfinding]] | [[cpp_a_star_\|A* — Pathfinding en C++ moderne]] | implémentation C++ |
| [[ai_pathfinding]] | [[ai_pathfinding_nav_mesh]], [[pathfinding_navmeshagent]] | NavMeshAgent Unity |
| [[ai_decision_algorithms]] | [[cpp_behaviour_tree_lecture\|Behaviour Trees en C++ moderne]] | implémentation C++ |
| [[ai_decision_algorithms]] | [[finite_state_machine]], [[behavior_tree]], [[goal_driven_behaviour]] | scripts Unity |
| [[ai_decision_algorithms]] | [[behavior_graph_tutorial\|Unity Behavior Graph]] | outil Unity 6 |
| [[ai_steering_behavior]] | [[autonomous_behaviours]] | scripts Unity |
| [[ai_world_representation]] | [[chapter_1_what_to_sense]], [[chapter_1_perceptions]] | perception, API Unity |
| [[ai_fundamentals]] | [[unity_ai_core_principles]], [[unity_ai_utility_ai]] | architecture IA Unity |
| [[pcg_graph_cellular_automaton]] | [[Théorie des Graphes et Recherche de Chemin]] | bloc théorique |
| [[ai_decision_algorithms]] | [[Théorie de la Décision pour l'IA]] | bloc théorique |

Les deux blocs Theory listés ci-dessus gagneraient à pointer vers ces nouveaux
cours dans leur colonne `Source` — leur tableau est tenu à la main.

## 3. Doublon interne au vault, antérieur à cet import

`01 courses/Unity/cours/ai_pathfinding_behaviour_tree_state_machine/` et
`01 courses/Unity/cours/ai_pathfinding_nav_mesh/` contiennent **deux sous-arbres
identiques** :

```text
autonomous_behaviours.md
autonomous_behaviours/behavior_tree.md
autonomous_behaviours/behavior_tree/behavior_graph_tutorial.md
autonomous_behaviours/finite_state_machine.md
autonomous_behaviours/goal_driven_behaviour.md
pathfinding_navmeshagent.md
```

Vérifié par `diff -r` : les six fichiers ne diffèrent **que par la ligne
`parent:`** de leur frontmatter, réécrite pour pointer vers le dossier parent
correspondant. Le contenu est identique au caractère près.

C'est ce qui explique les titres en double dans `index_cours.base`
(*Autonomous behaviours*, *Behavior Tree*, *Finite state machine*,
*Goal Driven Behaviour*, *Pathfinding : NavMeshAgent*, apparaissant chacun deux
fois).

Non touché — c'est un nettoyage Unity, indépendant de cet import.

## 4. Figures à réexporter à la main

L'API Drive ne rend que le **texte** d'une présentation : aucune image n'a pu
être récupérée, et les schémas sont sortis sous forme d'étiquettes en vrac. Ils
ont été redessinés en ASCII. Les endroits où la figure d'origine manque
vraiment sont marqués dans les notes :

```bash
grep -rn "TODO: figure d'origine" "01 courses/PCG" "01 courses/AI"
```

État au moment de l'import :

| Note | Figure manquante |
| --- | --- |
| [[pcg_introduction]] | exemple d'animation procédurale ; illustrations dés / semis de points |
| [[pcg_graph_cellular_automaton]] | grilles d'automate cellulaire, step 0 à step 3 |
| [[ai_pathfinding]] | grille complète des valeurs `f`/`g`/`h` de l'exemple A\* |
| [[ai_steering_behavior]] | captures RTS et flocking |
| [[ai_enemy_design]] | symbole d'attaque périlleuse |

Les fonds de slide réutilisent les images déjà présentes dans `00 images/`.

## 5. Reconstruction assumée

Le deck `07 Pathfinding` déroule l'algorithme de Dijkstra sur un graphe dont
seuls les **libellés et les distances** ont survécu à l'extraction, pas les
arêtes. Le graphe de [[ai_pathfinding]] a été reconstruit comme le jeu d'arêtes
cohérent avec toutes les distances affichées dans le deck (`A=0, B=4, C=8,
D=12, F=9, I=11, E=15→14, H=25→19, J=21`, chemin final `A→B→D→H = 19`).

Quatre poids présents sur les planches d'origine (`6, 9, 11, 2`) portaient sur
des arêtes non déductibles et n'ont pas été repris. La slide le mentionne.
