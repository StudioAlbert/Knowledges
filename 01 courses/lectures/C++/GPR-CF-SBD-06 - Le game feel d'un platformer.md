---
title: Le game feel d'un platformer
type: seance
code: GPR-CF-SBD-06
status: Ready
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: C++
bloc_gsda: SFML et Box2D
specialisation: "[[C++ Fondamentaux]]"
classes:
  - GP-926
manual_order: 0.96875
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
date_scheduled: 2026-11-04
url_test: http://localhost:3001/cpp/gpr-cf-sbd-06/
review:
  - "[[GPR-CF-SBD-xx - SFML]]"
  - "[[01 courses/__reviews/GPR-CF-SBD-06 - Le game feel d'un platformer|Review SBD-06]]"
---

# Le game feel d'un platformer

> [!abstract] Séance d'1 h — `GPR-CF-SBD-06` · bloc GSDA *SFML et Box2D*
> GP-926 · salle Arve · **2026-11-04** · 09:30–10:50 (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Objectifs d'un contrôleur de plateforme, ne pas sauter en l'air, toucher le sol par le côté, passer d'une plateforme à une autre, wall jump, one way platform

## Résumé proposé pour Aurora

> [!quote] À recopier dans Aurora — remplace le *À couvrir* ci-dessus
> Ce qui rend un saut agréable, coyote time et jump buffer, hauteur variable et gravité asymétrique, le wall jump, l'accessibilité en trois décisions, le capteur de sol et son compteur, la plateforme à sens unique avec `b2World_SetPreSolveCallback`, régler en jouant et faire jouer le voisin

## Ce qu'il y a à faire

Le découpage est fait et le deck est rédigé. Le support d'origine reste cité sous
*Matériel*.

## Plan et exercices

> [!done] Rédigé — relu le 2026-10-26
> - **Deck** : [[01 courses/slides/C++/GPR-CF-SBD-06 - Le game feel d'un platformer|GPR-CF-SBD-06 - Le game feel d'un platformer]] — 21 slides, sans atelier · widget `saut_fun_widget.html`.
> - **Démonstration** : cibles `MoveAndJump` et `LevelEditor` du dépôt d'exemples SFML.
> - **Rendu** : [[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]], le seul exercice de la série.
> - **Formative** : [[01 courses/exercises/C++/GPR-CF-SBD-06 - Formative, un saut qui fait envie|Un saut qui fait envie]], suivie d'un playtest collectif la semaine d'après.

## Matériel

- Support : [[11 - Box 2D]] — `01 courses/lectures/C++/11 - Box 2D.md` (9,5 ko)
    - Slides d'origine : https://docs.google.com/presentation/d/1WjpVxwYO2RImfP0aQ01sj5HMEUIAEMwjGJP-Slcmj-g/edit
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/SFML et Box2D.md`, ligne `06`

## Liens

- Séance précédente : [[GPR-CF-SBD-05 - Relier physique et graphique]]
- Séance suivante : —

## Notes de préparation

