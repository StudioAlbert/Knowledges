---
title: Cycle de vie de l'objet
type: seance
code: GPR-CF-POO-04
review:
  - "[[01 courses/__reviews/GPR-CF-POO-04 - Cycle de vie de l'objet|Review POO-04]]"
status: Post-mortem
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: C++
bloc_gsda: Programmation Orientée Objet
specialisation: "[[C++ Fondamentaux]]"
classes:
  - GP-926
  - WEB-926
date_scheduled: 2026-10-14
manual_order: 20
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# Cycle de vie de l'objet

> [!abstract] Séance d'1 h — `GPR-CF-POO-04` · bloc GSDA *Programmation Orientée Objet*
> GP-926 + WEB-926 · salle Arve · **2026-10-14** · 11:10–12:30 (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

`this` comme pointeur sur l'objet, constructeur par défaut, constructeur avec paramètres, valeurs par défaut, ordre d'initialisation, destructeur et moment de l'appel

## Ce qu'il y a à faire

**Découper un deck existant.** `01.03 - Basics OOP` (12,6 ko) porte 4 heures de ce lot : en extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres tranches vont à `GPR-CF-POO-01`, `GPR-CF-POO-02`, `GPR-CF-POO-03` — les découper en une seule passe évite de rouvrir le deck 4 fois.

## Plan et exercices

> [!done] Deck rédigé et companion construit le 12.10.2026
> - **Deck** : [[01 courses/slides/C++/GPR-CF-POO-04 - Cycle de vie de l'objet|Slides POO-04]] — 23 slides,
>   `publish: draft` le temps de la révision.
> - **Schéma** : `poo04_ordre_initialisation.svg` — l'ordre qu'on écrit, l'ordre qui a lieu,
>   et le membre lu avant d'exister.
> - **Companion** : [[01 courses/resources/C++/GPR-CF-POO-04 - Projet companion Naître et mourir|Projet companion]]
>   — une `Entity` qui annonce sa naissance et sa mort, trois situations, trois traces.
> - **Pas de widget** : `cycle_de_vie_widget.html` reste proposé, pas construit.
> - **Exercices** : [[01 courses/exercises/C++/GPR-CF-POO-04 - Cycle de vie de l'objet|Exos POO-04]] —
>   toujours à l'état d'overview, hors périmètre de cette révision.

## Matériel

- Support : [[01.03 - Basics OOP]] — `01 courses/lectures/C++/01.03 - Basics OOP.md` (12,6 ko)
    - Slides d'origine : https://docs.google.com/presentation/d/1QLO3rd0kv_2HUXWMEFXyjeRFwY4moBj9RAYhGvvDl4g/edit
    - Exercices : [[Exercices - 04 - OOP]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Programmation Orientée Objet.md`, ligne `04`

## Liens

- Séance précédente : [[GPR-CF-POO-03 - Découpage en fichiers]]
- Séance suivante : [[GPR-CF-POO-05 - Static et surcharge d'opérateur]]

## Notes de préparation

