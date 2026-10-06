---
title: Interpolation et courbes
type: seance
code: TC-FT-GVM-05
status: Ready
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: Theory
bloc_gsda: Géométrie Vectorielle et Matricielle
specialisation: "[[Fondamentaux Théoriques]]"
classes:
  - GP-925
  - GP-926
manual_order: 46
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
date_scheduled: 2026-10-08
---

# Interpolation et courbes

> [!abstract] Séance d'1 h — `TC-FT-GVM-05` · bloc GSDA *Géométrie Vectorielle et Matricielle*
> GP-925 + GP-926 · salle Arve · **2026-10-08** · 09:30–10:50 (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Lerp, rotation en 2D et en 3D, fonctions paramétriques, normalisation d'un paramètre, courbes d'easing (smooth start, smooth stop, smoother step, smooth arch)

## Ce qu'il y a à faire

**Découper un deck existant.** `08 - Theorical Notions of graphics programming - Maths` (20,0 ko) porte 8 heures de ce lot : en extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres tranches vont à `TC-FT-RNLB-03`, `TC-FT-TRG-01`, `TC-FT-TRG-02`, `TC-FT-RDE-02`, `TC-FT-RDE-03`, `TC-FT-GVM-01`, `TC-FT-GVM-02` — les découper en une seule passe évite de rouvrir le deck 8 fois.

## Plan et exercices

> [!done] Deck et widgets développés le 06.10.2026
> - **Deck** : [[01 courses/slides/Theory/TC-FT-GVM-05 - Interpolation et courbes|Slides GVM-05]] — 33 slides,
>   `publish: true`, bâti sur l'ossature posée à la main (*Animer…*, *Aller de A à B*,
>   *Clamp vs clamp*, *le clip d'animation*, *la fonction cyclique*).
> - **Widgets** : `fonctions_temps_widget.html` (droite non bornée, sinus paramétrable,
>   dents de scie, Lerp clampé ou non) et `quaternion_widget.html` (ordre des angles
>   d'Euler, gimbal lock mesuré sur un cardan, slerp contre interpolation d'angles).
>   Ils remplacent l'`easing_widget.html` proposé dans le plan, non construit.
> - **Exercices** : [[01 courses/exercises/Theory/TC-FT-GVM-05 - Interpolation et courbes|Exos GVM-05]] —
>   **encore à l'état d'overview**, la note de révision ne demandait pas de les rédiger.

## Matériel

- Support : [[08 - Theorical Notions of graphics programming - Maths]] — `01 courses/lectures/C++/08 - Theorical Notions of graphics programming - Maths.md` (20,0 ko)
    - Slides d'origine : https://docs.google.com/presentation/d/1MyyUSkqldoEikta8TUQdn0hG3AnSXnd81yfQcC0hGMc/edit
    - Exercices : [[Exercices - 08 - Introduction to Maths]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Géométrie Vectorielle et Matricielle.md`, ligne `05`
- Sources :
	- 

## Liens

- Séance précédente : [[TC-FT-GVM-04 - Espaces et changements de repère]]
- Séance suivante : —

## Notes de préparation

