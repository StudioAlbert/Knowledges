---
title: State, un pattern de gameplay
type: seance
code: GPR-UN-APU-09
status: To prepare
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: Unity
bloc_gsda: Architecture et Patterns Unity
specialisation: "[[Unity]]"
classes:
  - GP-925
date_scheduled: 2026-10-01
manual_order: 32
estimate: 1h
tache: créer de zéro
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# State, un pattern de gameplay

> [!abstract] Séance d'1 h — `GPR-UN-APU-09` · bloc GSDA *Architecture et Patterns Unity*
> GP-925 · salle Leman · **2026-10-01** · 09:30–10:50 (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Rappel des principes d'une machine à états, `enum` + `switch` puis pattern State (`IState`, `StateMachine`), applications au gameplay en schémas : tour par tour, navigation d'interface, QTE, autres cas (arme, IA, porte, déroulé de partie), l'Animator comme machine à états

> [!info] Révision du 28.09
> Séance recentrée sur State. L'Observer passe en `GPR-UN-APU-05`, la composition est abandonnée cette année — voir `01 courses/__reviews/Programme 2027-2028 - APU.md`.

## Ce qu'il y a à faire

**Deck créé le 28.09** — plus rien à découper : `solid_principles_in_unity` ne couvrait pas State.

- **Deck** : [[01 courses/slides/Unity/GPR-UN-APU-09 - Observer, State et composition|GPR-UN-APU-09 - State, un pattern de gameplay]] — 25 slides, `publish: false` tant que non relu, 5 schémas générés (`tools/schemas/apu09_*.py`).
- **Exercices** : [[01 courses/exercises/Unity/GPR-UN-APU-09 - Observer, State et composition|atelier araignée]] rédigé ; pistes 2 à 6 en overview.
- **Widget proposé, non fait** : `state_machine_widget.html` — la machine du héros, boutons de conditions, état courant qui s'allume, transitions impossibles refusées avec explication.

## Matériel

- Sources : [Game Programming Patterns — State](https://gameprogrammingpatterns.com/state.html), [Refactoring.Guru — State](https://refactoring.guru/fr/design-patterns/state), e-book Unity *Level up your code with design patterns and SOLID*
- Schémas : `00 images/apu09_fsm_principes.svg`, `apu09_tour_par_tour.svg`, `apu09_ui_navigation.svg`, `apu09_qte.svg`, `apu09_autres_cas.svg`
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Architecture et Patterns Unity.md`, ligne `09`

## Liens

- Séance précédente : [[GPR-UN-APU-08 - Strategy pattern en Unity]]
- Séance suivante : —

## Notes de préparation

