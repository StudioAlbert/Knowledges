---
title: Chaînes de caractères
type: seance
code: GPR-CF-BDP-06
status: To prepare
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: C++
bloc_gsda: Bases de la Programmation
specialisation: "[[C++ Fondamentaux]]"
classes:
  - GP-926
  - WEB-926
date_scheduled: 2026-10-01
manual_order: 14
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# Chaînes de caractères

> [!abstract] Séance d'1 h — `GPR-CF-BDP-06` · bloc GSDA *Bases de la Programmation*
> GP-926 + WEB-926 · salle Arve · **2026-10-01** · 15:10–16:30 (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

`std::string`, concaténation, `to_string()`, longueur, accès par `[]` et par `at()`, saisie utilisateur, `compare()`, `find()`, `substr()`, `operator +`

## Ce qu'il y a à faire

**Découper un deck existant.** `01.02 - Programming Basics 2-2 - enum, string` (8,9 ko) porte 2 heures de ce lot : en extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres tranches vont à `GPR-CF-BDP-05` — les découper en une seule passe évite de rouvrir le deck 2 fois.

## Plan et exercices — overview à valider

> [!todo] Produit les 27 et 28 septembre 2026, en attente de validation
> - **Plan du deck** : [[01 courses/slides/C++/GPR-CF-BDP-06 - Chaînes de caractères|GPR-CF-BDP-06 - Chaînes de caractères]] — 14 slides, `publish: false` · widgets proposés : `string_index_widget.html` ; 1 schéma à dessiner.
> - **Overview des exercices** : [[01 courses/exercises/C++/GPR-CF-BDP-06 - Chaînes de caractères|GPR-CF-BDP-06 - Chaînes de caractères]] — 4 courts, 1 complet, 1 difficile.
>
> Rien n'est rédigé : chaque slide ne porte qu'un titre et une phrase directrice, chaque
> exercice qu'une piste de deux ou trois lignes. C'est la base des développements à venir.

## Matériel

- Support : [[01.02 - Programming Basics 2-2 - enum, string]] — `01 courses/lectures/C++/01.02 - Programming Basics 2-2 - enum, string.md` (8,9 ko)
    - Slides d'origine : https://docs.google.com/presentation/d/1DrM5b7TMMJdhrlZ51s9zpXgYptxFx5H6AD1o7Ni1Nl4/edit
    - Exercices : [[Exercices - 01b - Programming Basics (2-2) - enum, arrays, string]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Bases de la Programmation.md`, ligne `06`

## Liens

- Séance précédente : [[GPR-CF-BDP-05 - Énumérations et tableaux]]
- Séance suivante : —

## Notes de préparation

### Révision du 28.09

- **Chaîne à la C** : schéma `00 images/bdp06_chaine_c.svg` (« Sebastien », codes ASCII, `'\0'`, pointeur) + snippet de lecture caractère par caractère.
- **std::string comme objet** : 3 fonctionnalités (mémoire gérée, taille connue, sémantique de valeur) + schéma `bdp06_std_string.svg` (pointeur, taille, capacité, `c_str()`) + snippet « en action ».
- **Un snippet par slide de fonctionnalité** (concaténer, nombre ↔ texte, longueur, accès, saisie, comparer, chercher, découper), tous compilés et exécutés (GCC 14, C++23).
- **Schéma** `bdp06_to_string_stoi.svg` et **widget** `00 widgets/_widgets/string_index_widget.html` (`#index`, `#substr`, `#find`) : slide visuel + slide code, qui se complètent.
