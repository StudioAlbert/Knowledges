---
title: Bases et changements de base
type: seance
code: TC-FT-RNLB-01
status: Ready
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: Theory
bloc_gsda: Représentation des Nombres et Logique Binaire
specialisation: "[[Fondamentaux Théoriques]]"
classes:
  - GP-926
  - WEB-926
  - WEB-925
date_scheduled: 2026-09-16
manual_order: 68
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# Bases et changements de base

> [!abstract] Séance d'1 h — `TC-FT-RNLB-01` · bloc GSDA *Représentation des Nombres et Logique Binaire*
> GP-926 + WEB-926 + WEB-925 · salle Arve · **2026-09-09** (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Poids des chiffres, binaire, octal, hexadécimal, conversions dans les deux sens, table hexadécimale, notation littérale en C++

## Ce qu'il y a à faire

**Découper un deck existant.** `02 - Introduction to logic - non decimal arithmetic` (6,9 ko) porte 3 heures de ce lot : en extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres tranches vont à `TC-FT-RNLB-02`, `TC-FT-RNLB-04` — les découper en une seule passe évite de rouvrir le deck 3 fois.

## Matériel

- Support : [[01 courses/slides/Theory/TC-FT-RNLB-01 - Bases et changements de base|TC-FT-RNLB-01 - Bases et changements de base]]
- Exercices : [[01 courses/exercises/Theory/TC-FT-RNLB-01 - Bases et changements de base|TC-FT-RNLB-01 - Bases et changements de base]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Représentation des Nombres et Logique Binaire.md`, ligne `01`

## Liens

- Séance précédente : —
- Séance suivante : [[01 courses/lectures/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements]]

## Notes de préparation

> [!todo] À relire
> Découpé le 2026-09-15 depuis `02 - Introduction to logic - non decimal arithmetic` (partie « Arithmétique non décimale ») et les fiches d'exercices 02 et 08.
> - **Repris** : poids des chiffres, base 9, binaire, hexadécimal et sa table ; le tableau des conversions de la fiche 02 et les exercices 1 à 3 de la fiche 08.
> - **Écrit pour la séance** : règles d'une base, pourquoi le binaire, puissances de 2, paquets de 4 bits, octal, méthodes de conversion, littéraux C++, piège de l'octal, affichage dans une autre base ; exercices 4 et 5.

> [!success]- Corrigé des exercices
> **Ex. 1** — 155 ; 250 ; 493 ; 284.
> **Ex. 2** — 201 = 1100 1001 = 0xC9 ; 2026 = 111 1110 1010 = 0x7EA ; 493 = 755₈ = 111 101 101.
> **Ex. 3** — AF = 175 = 1010 1111 ; ACD = 2765 = 1010 1100 1101 ; AB2 = 2738 = 1010 1011 0010 ; FF = 255 = 1111 1111 ; 147 = 0x93 = 1001 0011 ; 39554 = 0x9A82 ; 15637 = 0x3D15 = 0011 1101 0001 0101 ; 2856 = 0xB28 = 1011 0010 1000.
> **Ex. 4** — `31 16 15 1024`, puis `2f 17`, puis `00001111 0x400`. Un `0` en tête annonce un octal, et 9 n'est pas un chiffre octal.
> **Ex. 5** — `std::cout << std::format("{} = {:#x} = {:#o} = {:#018b}\n", n, n, n, n);`

