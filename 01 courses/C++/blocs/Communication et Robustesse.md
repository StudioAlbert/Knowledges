---
type: bloc
specialisation: "[[C++]]"
mineur: Games Programming
prerequis:
  - "[[Patterns]]"
projet:
  - "[[City Builder]]"
cours: 6
---

# Communication et Robustesse

Faire dialoguer des sous-systèmes sans les coupler, et signaler un échec autrement qu'en espérant que l'appelant regarde.

## Objectifs

- Mettre en place un bus d'événements et des signaux entre sous-systèmes
- Peser les compromis du dispatch : couplage, ordre, coût
- Retourner un échec avec `std::expected` plutôt qu'un code ignoré
- Choisir entre exception, valeur d'erreur et assertion selon la nature du problème

## Cours

<!-- cours:auto -->

| # | Cours | Heures | Lien |
| --- | --- | --- | --- |
| 1 | Event Bus & Signals | 3 | [[cpp_event_bus_signals_lecture]] |
| 2 | std::expected & gestion d'erreur | 3 | [[cpp_expected_error_handling_lecture]] |

**Total : 2 cours, 6 h.**

<!-- /cours:auto -->

## Validation

Deux sous-systèmes du projet communiquant par événements, avec chemins d'erreur testés.

## Liens

- Spécialisation : [[C++]]
- Prérequis : [[Patterns]]
- Bloc suivant : [[IA en C++]]
- Index des cours : [[index_cours.base|Index]]
