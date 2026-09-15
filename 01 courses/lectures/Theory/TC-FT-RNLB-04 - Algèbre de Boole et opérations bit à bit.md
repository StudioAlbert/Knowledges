---
title: Algèbre de Boole et opérations bit à bit
type: seance
code: TC-FT-RNLB-04
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
manual_order: 12
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# Algèbre de Boole et opérations bit à bit

> [!abstract] Séance d'1 h — `TC-FT-RNLB-04` · bloc GSDA *Représentation des Nombres et Logique Binaire*
> GP-926 + WEB-926 + WEB-925 · salle Arve · **2026-09-23** (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Tables de vérité, ET/OU/NON/XOR, commutativité, distributivité, lois de De Morgan, priorité des opérateurs, masques, décalages, drapeaux compactés

## Ce qu'il y a à faire

**Découper un deck existant.** `02 - Introduction to logic - non decimal arithmetic` (6,9 ko) porte 3 heures de ce lot : en extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres tranches vont à `TC-FT-RNLB-01`, `TC-FT-RNLB-02` — les découper en une seule passe évite de rouvrir le deck 3 fois.

## Matériel

- Support : [[01 courses/slides/Theory/TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit|TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit]]
- Slides d'origine : https://docs.google.com/presentation/d/1n-YUpykKSHexQ1hc6MRz3oKSkXam_iX5HYEDIY1dvSc/edit
- Exercices : [[01 courses/exercises/Theory/TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit|TC-FT-RNLB-04 - Algèbre de Boole et opérations bit à bit]]
- Ressources : [[Truth table]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Représentation des Nombres et Logique Binaire.md`, ligne `04`

## Liens

- Séance précédente : [[01 courses/lectures/Theory/TC-FT-RNLB-03 - Flottants IEEE 754]]
- Séance suivante : —

## Notes de préparation

> [!todo] À relire
> Découpé le 2026-09-15 depuis `02 - Introduction to logic - non decimal arithmetic` (opérateurs C++, algèbre de Boole) et la ressource `Truth table`, désormais rattachée à la séance.
> - **Repris** : opérations booléennes, comparaisons, tables ET / OU / NON, commutativité, distributivité, De Morgan, priorité, tables d'incrément / décalage et d'affectation ; exercices 1.1 à 2.2.
> - **Écrit pour la séance** : OU exclusif, construction d'une table, De Morgan dans le code, opérateurs bit à bit, décalages, masques, couleur ARGB, priorité en C++, drapeaux compactés, `std::bitset` ; exercices 3 à 8.
> - **Corrigé au passage** : `>>` et `<<` s'appelaient « roll », ce sont des décalages. Dans le corrigé de l'exercice 2.2, la factorisation écrivait `a || (!b && b)` au lieu de `a && (!b || b)` ; le résultat final `a || !b` était juste.

> [!success]- Corrigé des exercices
> **Ex. 1.2** — 1, 1, 0, 1 (lignes ab de 00 à 11).
> **Ex. 1.3** — ∧ prioritaire sur ∨ : 0, 0, 1, 0, 0, 1, 1, 1 (lignes abc de 000 à 111).
> **Ex. 2.1** — `b` ; avant simplification, `(!a ∧ b) ∨ (a ∧ b)`.
> **Ex. 3** — `vie <= 0 || munitions <= 0` ; `!touche_gauche && !touche_droite` ; `x >= 0 && x < largeur && y >= 0 && y < hauteur`.
> **Ex. 4** — `a & b` = 0101 0100 = 0x54 ; `a | b` = 1101 1110 = 0xDE ; `a ^ b` = 1000 1010 = 0x8A ; `~a` = 0010 1001 = 0x29 ; `a << 2` = 0101 1000 = 0x58 ; `a >> 3` = 0001 1010 = 0x1A.
> **Ex. 5** — `x |= 1u << 0;` → 1010 0001 ; `x &= ~(1u << 7);` → 0010 0001 ; `x ^= 0x0F;` → 0010 1110 ; `(x & (1u << 5)) != 0` → vrai.
> **Ex. 6** — `return static_cast<std::uint8_t>((argb >> 8) & 0xFF);` et `return (argb & 0x00FFFFFFu) | (std::uint32_t{alpha} << 24);`
> **Ex. 8** — `!=` passe avant `&` : le test calcule `etat & (SOLIDE != 0)`, soit `0b0010 & 1`, qui vaut 0. Écrire `(etat & SOLIDE) != 0`.

