---
title: Flottants IEEE 754
type: seance
code: TC-FT-RNLB-03
status: To check
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: Theory
bloc_gsda: Représentation des Nombres et Logique Binaire
specialisation: "[[Fondamentaux Théoriques]]"
classes:
  - GP-926
  - WEB-926
  - WEB-925
date_scheduled: 2026-09-17
manual_order: 10
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# Flottants IEEE 754

> [!abstract] Séance d'1 h — `TC-FT-RNLB-03` · bloc GSDA *Représentation des Nombres et Logique Binaire*
> GP-926 + WEB-926 + WEB-925 · salle Arve · **2026-09-17** (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Signe, exposant, mantisse, précision et epsilon, valeurs spéciales, pourquoi `==` ment sur les flottants, notations numériques et implémentation machine

## Ce qu'il y a à faire

**Découper un deck existant.** `08 - Theorical Notions of graphics programming - Maths` (20,0 ko) porte 8 heures de ce lot : en extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres tranches vont à `TC-FT-TRG-01`, `TC-FT-TRG-02`, `TC-FT-RDE-02`, `TC-FT-RDE-03`, `TC-FT-GVM-01`, `TC-FT-GVM-02`, `TC-FT-GVM-05` — les découper en une seule passe évite de rouvrir le deck 8 fois.

## Matériel

- Support : [[01 courses/slides/Theory/TC-FT-RNLB-03 - Flottants IEEE 754|TC-FT-RNLB-03 - Flottants IEEE 754]]
- Slides d'origine : https://docs.google.com/presentation/d/1MyyUSkqldoEikta8TUQdn0hG3AnSXnd81yfQcC0hGMc/edit
- Exercices : [[01 courses/exercises/Theory/TC-FT-RNLB-03 - Flottants IEEE 754|TC-FT-RNLB-03 - Flottants IEEE 754]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Représentation des Nombres et Logique Binaire.md`, ligne `03`

## Liens

- Séance précédente : [[01 courses/lectures/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements]]
- Séance suivante : [[01 courses/lectures/Theory/TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit]]

## Notes de préparation

> [!todo] À relire
> Découpé le 2026-09-15 depuis `08 - Theorical Notions of graphics programming - Maths`, section « Les nombres en machine » : notations numériques, implémentation machine, hexadécimal. Le deck d'origine ne parlait pas d'IEEE 754 :
> - **Écrit pour la séance** : notation scientifique, fractions binaires, structure du `float` et du `double`, littéraux, lecture et codage en hexadécimal, epsilon, écart entre flottants, positions dans un moteur, valeurs spéciales, NaN, comparaisons, conversion vers l'entier.
> - **Exercices** : tous écrits pour la séance ; l'exercice 2 entraîne la validation du bloc (lecture d'un flottant donné en hexadécimal).

> [!success]- Corrigé des exercices
> **Ex. 1** — 0,1 ; 0,01 ; 0,101 ; 101,11. 0,2 = 0,0011 0011…₂ : le motif se répète sans fin, 0,2 n'a pas d'écriture binaire finie.
> **Ex. 2** — `0x40000000` : +, exposant 128 → 1, mantisse nulle → 2,0. `0xBF000000` : −, 126 → −1, mantisse nulle → −0,5. `0x42C80000` : +, 133 → 6, 1,1001₂ = 1,5625 → 100,0. `0x41A40000` : +, 131 → 4, 1,01001₂ = 1,28125 → 20,5. `0x80000000` : −0. `0x7F800000` : +∞.
> **Ex. 3** — 3,0 = `0x40400000` ; −2,5 = `0xC0200000` ; 0,15625 = `0x3E200000` ; 1000,0 = `0x447A0000`.
> **Ex. 4** — `true` ; `false` ; `inf true` ; `false true` ; `-7 -8` ; `true`.
> **Ex. 5** — Non : après 10 pas, `x` vaut 2.0000002, jamais exactement `2.0f`, et la boucle continue. `for (int i = 0; i <= 10; ++i) std::cout << i * 0.2f << '\n';`
> **Ex. 6** — vrai (les arrondis tombent au même endroit) ; vrai (écart 1e-8 ≤ 1e-6) ; vrai (`100000.01f` est arrondi à 100000.0078, écart relatif 7,8 × 10⁻⁸) ; faux ; faux (toute comparaison avec NaN est fausse).
> **Ex. 7** — L'écart entre deux `float` voisins vaut 2^(e − 23) : au moins 1 cm dès 2¹⁷ = 131 072 m, au moins 1 m dès 2²³ = 8 388 608 m. Solutions : origine flottante, positions en `double`, monde découpé en cellules à coordonnées locales.

