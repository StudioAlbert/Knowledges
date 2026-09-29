---
title: ScriptableObjects
type: seance
code: GPR-UN-APU-04
status: To prepare
projet: Module 2 — 23 nov. 2026 → 12 févr. 2027
subject: Unity
bloc_gsda: Architecture et Patterns Unity
specialisation: "[[Unity]]"
classes: [GP-926]
manual_order: 56
estimate: 1h
tache: adapter + écrire
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# ScriptableObjects

> [!abstract] Séance d'1 h — `GPR-UN-APU-04` · bloc GSDA *Architecture et Patterns Unity*
> GP-926 · salle Arve · **non datée** (Module 2 — 23 nov. 2026 → 12 févr. 2027)

## À couvrir

Ce qu'est un `ScriptableObject`, asset contre instance de scène, `[CreateAssetMenu]`, profils de données (loot, ennemis), configuration éditable par le designer ; variable partagée et Runtime Set ; le piège de l'état qui persiste dans l'éditeur

> [!info] Révision du 28.09
> Tout le sujet tient désormais dans cette séance (le deck n'est plus découpé en deux). Les événements en ScriptableObject passent en `GPR-UN-APU-05` avec l'Observer — voir `01 courses/__reviews/Programme 2027-2028 - APU.md`.

## Ce qu'il y a à faire

**Deck créé le 28.09**, sans découpage : adapté de `scriptable_objects` (plan dungeon : loot, valeurs, runtime set) et des sources Unity.

- **Deck** : [[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|GPR-UN-APU-04 - ScriptableObjects]] — 17 slides, `publish: false`, 1 schéma généré (`tools/schemas/apu04_asset_instances.py`).
- **Exercices** : [[01 courses/exercises/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|atelier]] rédigé (Dungeon Crawler, branche `main`) ; pistes 2 à 6 en overview.
- **Widget proposé, non fait** : `scriptableobject_widget.html` — un prefab, trois assets à glisser, un bouton « modifier pendant le jeu » qui montre la valeur restée modifiée.

## Matériel

- Support : [[scriptable_objects]] — `01 courses/lectures/Unity/scriptable_objects.md` (2,9 ko), repris en entier
- Sources : [Manuel Unity — ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html), [e-book *Create modular game architecture in Unity with ScriptableObjects*](https://unity.com/resources/create-modular-game-architecture-with-scriptable-objects-ebook), [Separate game data and logic](https://unity.com/how-to/separate-game-data-logic-scriptable-objects), [Ryan Hipple, Unite Austin 2017](https://www.youtube.com/watch?v=raQ3iHhE_Kk)
- Schéma : `00 images/apu04_asset_instances.svg`
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Architecture et Patterns Unity.md`, ligne `04`

## Liens

- Séance précédente : [[GPR-UN-APU-01 - SOLID en Unity — SRP et OCP, LSP et ISP, DIP et atelier]]
- Séance suivante : [[GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|GPR-UN-APU-05 - Observer, prévenir sans connaître]]

## Notes de préparation

