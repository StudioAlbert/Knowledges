---
title: Relier physique et graphique
type: seance
code: GPR-CF-SBD-05
status: Ready
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: C++
bloc_gsda: SFML et Box2D
specialisation: "[[C++ Fondamentaux]]"
classes:
  - GP-926
manual_order: 0.9375
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
date_scheduled: 2026-10-29
review:
  - "[[01 courses/__reviews/GPR-CF-SBD-05 - Relier physique et graphique|Review SBD-05]]"
  - "[[GPR-CF-SBD-xx - SFML]]"
---

# Relier physique et graphique

> [!abstract] Séance d'1 h — `GPR-CF-SBD-05` · bloc GSDA *SFML et Box2D*
> GP-926 · salle Arve · **2026-10-29** · 15:10–16:30 (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Copier les valeurs du monde physique vers le monde graphique, déplacer le personnage, `ContactListener`, `UserData` pour retrouver l'objet de jeu depuis un contact

## Résumé proposé pour Aurora

> [!quote] À recopier dans Aurora — remplace le *À couvrir* ci-dessus
> Une seule classe de conversion mètres-pixels, les deux axes Y qui s'opposent, recopier position et angle du physique vers le graphique, `b2Body_SetTransform` `ApplyForceToCenter` et `SetLinearVelocity`, lire `b2World_GetContactEvents` après le pas, `userData` pour retrouver l'objet de jeu, pourquoi « au sol » n'est pas un contact

## Ce qu'il y a à faire

Le découpage est fait et le deck est rédigé. Le support d'origine reste cité sous
*Matériel*.

## Plan et exercices

> [!done] Rédigé — relu le 2026-10-26
> - **Deck** : [[01 courses/slides/C++/GPR-CF-SBD-05 - Relier physique et graphique|GPR-CF-SBD-05 - Relier physique et graphique]] — 15 slides, atelier d'1 h compris.
> - **Démonstration** : cibles `Views` et `Motor` du dépôt d'exemples SFML.
> - **Rendu** : [[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]], le seul exercice de la série.

## Matériel

- Support : [[11 - Box 2D]] — `01 courses/lectures/C++/11 - Box 2D.md` (9,5 ko)
    - Slides d'origine : https://docs.google.com/presentation/d/1WjpVxwYO2RImfP0aQ01sj5HMEUIAEMwjGJP-Slcmj-g/edit
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/SFML et Box2D.md`, ligne `05`

## Liens

- Séance précédente : [[GPR-CF-SBD-04 - Le monde Box2D]]
- Séance suivante : [[GPR-CF-SBD-06 - Le game feel d'un platformer]]

## Notes de préparation

