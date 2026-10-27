---
title: Déplacer et animer
type: seance
code: GPR-CF-SBD-03
status: Ready
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: C++
bloc_gsda: SFML et Box2D
specialisation: "[[C++ Fondamentaux]]"
classes:
  - GP-926
manual_order: 0.75
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
date_scheduled: 2026-10-28
review:
  - "[[01 courses/__reviews/GPR-CF-SBD-03 - Déplacer et animer|Review SBD-03]]"
  - "[[GPR-CF-SBD-xx - SFML]]"
---

# Déplacer et animer

> [!abstract] Séance d'1 h — `GPR-CF-SBD-03` · bloc GSDA *SFML et Box2D*
> GP-926 · salle Arve · **2026-10-28** · 13:30–14:50 (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Jouer un son, `sf::Sound` et `sf::Music`, ce que chacun charge en mémoire, conclusion sur le monde graphique

## Résumé proposé pour Aurora

> [!quote] À recopier dans Aurora — remplace le *À couvrir* ci-dessus
> `sf::Clock` et le `dt` mesuré une fois par image, le piège du déplacement par image, `setFramerateLimit` contre `setVerticalSyncEnabled`, découper une sprite sheet avec `sf::IntRect`, faire défiler les poses à cadence fixe, changer d'animation sans la redémarrer

## Ce qu'il y a à faire

Le découpage est fait et le deck est rédigé. Le support d'origine reste cité sous
*Matériel*.

## Plan et exercices

> [!done] Rédigé — relu le 2026-10-26
> - **Deck** : [[01 courses/slides/C++/GPR-CF-SBD-03 - Déplacer et animer|GPR-CF-SBD-03 - Déplacer et animer]] — 15 slides, atelier d'1 h compris · widget `boucle_de_jeu_widget.html`.
> - **Démonstration** : cibles `TimeClock`, `Animation`, `AnimationClass` et `MoveAndJump` du dépôt d'exemples SFML.
> - **Rendu** : [[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]], le seul exercice de la série.

## Matériel

- Support : [[10 - SFML]] — `01 courses/lectures/C++/10 - SFML.md` (10,3 ko)
    - Slides d'origine : https://docs.google.com/presentation/d/1IFFIopIjzAz-iy2_iQp-1pxJNNpdivqmUn3hlo5bm1M/edit
    - Exercices : [[Exercices - 10 - SFML]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/SFML et Box2D.md`, ligne `03`

## Liens

- Séance précédente : [[GPR-CF-SBD-02 - Gameplay et événements]]
- Séance suivante : [[GPR-CF-SBD-04 - Le monde Box2D]]

## Notes de préparation

