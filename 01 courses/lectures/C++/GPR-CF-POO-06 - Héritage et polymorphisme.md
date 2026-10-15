---
title: Héritage et polymorphisme
type: seance
code: GPR-CF-POO-06
review:
  - "[[01 courses/__reviews/GPR-CF-POO-06 - Héritage et polymorphisme|Review POO-06]]"
status: Post-mortem
projet: Module 1 — 7 sept. → 13 nov. 2026
subject: C++
bloc_gsda: Programmation Orientée Objet
specialisation: "[[C++ Fondamentaux]]"
classes:
  - GP-926
  - WEB-926
date_scheduled: 2026-10-14
manual_order: 25
estimate: 1h
tache: découper
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# Héritage et polymorphisme

> [!abstract] Séance d'1 h — `GPR-CF-POO-06` · bloc GSDA *Programmation Orientée Objet*
> GP-926 + WEB-926 · salle Arve · **2026-10-14** · 13:30–14:50 (Module 1 — 7 sept. → 13 nov. 2026)

## À couvrir

Principe de l'héritage, le code, les deux points à retenir, mode d'héritage, héritage multiple et ses pièges, méthodes `virtual`, démonstration du dispatch, méthode virtuelle pure et classe abstraite

## Ce qu'il y a à faire

**Découper un deck existant.** `04 - OOP Advanced` (10,1 ko) porte 2 heures de ce lot : en extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres tranches vont à `GPR-CF-POO-05` — les découper en une seule passe évite de rouvrir le deck 2 fois.

## Plan et exercices

> [!done] Deck rédigé le 12.10.2026, à partir de [[04 - OOP Advanced]]
> - **Deck** : [[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme|Slides POO-06]] — 18 slides,
>   `publish: online` depuis le 15.10. Reprend les tranches *Héritage* et
>   *Polymorphisme* du support d'origine ; `static` et les opérateurs restent à POO-05.
> - **Schéma** : `poo06_diamant.svg` — le diamant, et la base plus interface qui l'évite.
> - **Formative, et elle seule** : [[01 courses/exercises/C++/GPR-CF-POO-06 - Héritage et polymorphisme - Formative|Formative — l'armurerie]]
>   — cinq armes, cinq types, un menu sans un seul test sur le type. Écrite sur la
>   hiérarchie `Weapon` / `Firearm` / `Melee` fournie par l'auteur. Publiée depuis
>   `exercises/C++/` comme l'exercice de la séance (`seances: GPR-CF-POO-06`).
> - **Companion** : [[01 courses/resources/C++/GPR-CF-POO-06 - Projet companion Le stand de tir|Projet companion]]
>   — une arme, une classe sans parent, un menu qui l'appelle. Le point de départ.
> - **Pas de widget** : `dispatch_widget.html` reste proposé, pas construit — les deux
>   sorties console du deck sont réelles, vérifiées au compilateur.
> - **Pas d'atelier** : supprimé le 12.10, la formative le remplace — elle est la seule
>   feuille de la séance.

## Matériel

- Support : [[04 - OOP Advanced]] — `01 courses/lectures/C++/04 - OOP Advanced.md` (10,1 ko)
    - Slides d'origine : https://docs.google.com/presentation/d/1ybWagXO7WpCXxiYdodSQqti90s-RkA6_kW-3hcnMjuo/edit
    - Exercices : [[Exercices - 04 - OOP]]
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Programmation Orientée Objet.md`, ligne `06`

## Liens

- Séance précédente : [[GPR-CF-POO-05 - Static et surcharge d'opérateur]]
- Séance suivante : —

## Notes de préparation

