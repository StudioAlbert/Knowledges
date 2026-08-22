---
title: C++
type: index
---
# Blocs pédagogiques

Le cours C++ réunit l'ancien *C++ Intro* (module 4FSC0PF001) et l'ancien *C++ Advanced*
en un seul cursus de 9 blocs. Chaque lecture porte une propriété `bloc` ; les blocs
vivent dans `blocs/`, suivent le schéma du vault GSDA (`type: bloc`, `specialisation`,
`prerequis`, `cours`) et totalisent les heures des lectures qui les référencent.

Règle de dimensionnement : **une lecture vaut 3 h**, sauf quand le support annonce
lui-même sa durée (Builder 2 h, Sérialisation 1 h, Behaviour Tree 4 h). Exercices,
formatives et ressources sont rattachés au cursus mais ne comptent pas d'heures.

Le compteur `cours:` de chaque bloc est régénéré par `tools/sync_blocs.py` ; la vue
*Heures par bloc* ci-dessous recalcule la même somme en direct pour la contrôler.

![[01 courses/C++/index_blocs.base]]

# Index des cours

Toutes les lectures, filtrables par bloc : [[index_cours.base|Index]]

![[index_cours.base]]

# Autres dossiers

- `exercices/` · `ressources/` — supports d'accompagnement, sans bloc
- `projets/` — briefs de projets et formatives, rattachés aux blocs par la propriété `projet`
- `drafts/` — lectures non finalisées, hors cursus tant qu'elles ne sont pas promues dans `cours/`
- `exams/` — sujets d'examen ; les dépôts clonés ici sont gitignorés (repos SAE-Geneve séparés)
- `companion projects/` — dépôts compagnons, en sous-modules git
