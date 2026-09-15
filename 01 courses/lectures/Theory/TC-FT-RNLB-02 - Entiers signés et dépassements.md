---
title: Entiers signés et dépassements
type: seance
code: TC-FT-RNLB-02
status: To check
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: Theory
bloc_gsda: Représentation des Nombres et Logique Binaire
specialisation: "[[Fondamentaux Théoriques]]"
classes:
  - GP-926
  - WEB-926
  - WEB-925
date_scheduled: 2026-09-30
manual_order: 6
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# Entiers signés et dépassements

> [!abstract] Séance d'1 h — `TC-FT-RNLB-02` · bloc GSDA *Représentation des Nombres et Logique Binaire*
> GP-926 + WEB-926 + WEB-925 · salle Arve · **2026-09-16** (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Complément à deux, plages représentables, dépassement signé et non signé, types de taille fixe, taille des types en mémoire selon la plateforme

## Ce qu'il y a à faire

**Découper un deck existant.** `01.01 - Programming Basics - if, loops` (17,9 ko) porte 5 heures de ce lot : en extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres tranches vont à `GPR-CF-BDP-01`, `GPR-CF-BDP-02`, `GPR-CF-BDP-03`, `GPR-CF-BDP-04` — les découper en une seule passe évite de rouvrir le deck 5 fois.

## Matériel

- Support : [[01 courses/slides/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements|TC-FT-RNLB-02 - Entiers signés et dépassements]]
- Slides d'origine : https://docs.google.com/presentation/d/1BWCyCFyfi5hxUMsSEnCvPpweoJpYSvnvFNRjcZIJTmU/edit (01.01 - Programming Basics)
- Slides d'origine : https://docs.google.com/presentation/d/1n-YUpykKSHexQ1hc6MRz3oKSkXam_iX5HYEDIY1dvSc/edit (02 - Introduction to logic)
- Exercices : [[01 courses/exercises/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements|TC-FT-RNLB-02 - Entiers signés et dépassements]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Représentation des Nombres et Logique Binaire.md`, ligne `02`

## Liens

- Séance précédente : [[01 courses/lectures/Theory/TC-FT-RNLB-01 - Bases et changements de base]]
- Séance suivante : [[01 courses/lectures/Theory/TC-FT-RNLB-03 - Flottants IEEE 754]]

## Notes de préparation

> [!todo] À relire
> Découpé le 2026-09-15 depuis `01.01 - Programming Basics - if, loops` (taille en mémoire sous Windows) et `02 - Introduction to logic - non decimal arithmetic` (opérateurs arithmétiques). Aucun support ne couvrait le reste :
> - **Écrit pour la séance** : Pac-Man, plages, bit de signe, complément à deux, dépassements non signé et signé, mélange signé / non signé, promotion, détection, taille selon la plateforme, types de taille fixe, exemples réels.
> - **Exercices** : tous écrits pour la séance ; l'exercice 3 entraîne la validation du bloc (prévision d'un dépassement).

> [!success]- Corrigé des exercices
> **Ex. 1** — 4 096 valeurs, de −2 048 à 2 047. `uint8_t` ; `uint32_t` ou `int32_t` ; `int8_t` ; `int64_t` (≈ 1,8 × 10¹² ms en 2026, bien au-delà de 2³²).
> **Ex. 2** — 100 = 0110 0100 ; −100 = 1001 1100 ; −1 = 1111 1111 ; −128 = 1000 0000. Décodage : −127 ; −32 ; 127 ; −86. Le bit de poids fort pèse −128 : le plus grand positif est 0111 1111 = 127.
> **Ex. 3** — a = 4 ; b = 246 ; c = −25 536, sans comportement indéfini : le calcul se fait en `int` (40 000), et c'est la conversion vers `int16_t` qui fait le tour — définie depuis C++20, définie par l'implémentation avant ; d : comportement indéfini ; e = 4 294 967 295 ; h = 300, de type `int`.
> **Ex. 4** — Vide : `v.size() - 1` fait le tour, `v[4294967295]` lit hors du tableau. `{1, 2, 3}` : affiche 3, 2, 1, puis `i` passe de 0 à 4 294 967 295 et la lecture continue hors du tableau, car `i >= 0` est toujours vrai. Correction : `for (std::size_t i = v.size(); i > 0; --i) std::cout << v[i - 1] << '\n';`
> **Ex. 5** — `(1, 2)` → vrai, 3 ; `(INT32_MAX, 1)` → faux ; `(INT32_MIN, -1)` → faux ; `(INT32_MAX, INT32_MIN)` → vrai, −1. Tester `b > 0 && a > max - b`, puis `b < 0 && a < min - b`.
> **Ex. 6** — Windows 64 bits : 1, 2, 4, 4, 8, 2, 8, 8. Linux 64 bits : 1, 2, 4, 8, 8, 4, 8, 8.

