---
status: To check
manual_order: 4
parent:
  - "[[APU 04 APU 05 APU 09 deviennent]]"
slides:
  - "[[01 courses/slides/Unity/GPR-UN-APU-09 - Observer, State et composition|Slides APU-09]]"
exercices:
  - "[[01 courses/exercises/Unity/GPR-UN-APU-09 - Observer, State et composition|Exos APU-09]]"
---
- Rappeller les principes d'une State Machine
- Proposer des exemples sous formes de schémas appliqués :
	- Tour par tour : Chaque Tour de Jeu est un State,  les entités suivent la State Machine
	- UI : Cheminement dans une interface, QTE
	- *Proposer autres cas d'usage*

## Traité le 28.09 — à vérifier (séance du 01.10)

- **Deck** réécrit : [[01 courses/slides/Unity/GPR-UN-APU-09 - Observer, State et composition]] — 25 slides, `publish: false` à passer à `true` après relecture.
	- Rappel : problème des booléens, trois mots (état, transition, état courant), schéma du héros de platformer, règles.
	- Code : `enum` + `switch`, `IState`, `StateMachine`.
	- Schémas : tour par tour (machine du jeu + machine des unités, liées par `Enter`), navigation d'interface, QTE, quatre autres cas (arme, garde, porte, partie) ; code d'un tour et d'un QTE.
	- Clôture : l'Animator est une machine, quand passer au hiérarchique / arbre de comportement.
- **Atelier** : l'araignée du Dungeon Crawler (branche `main`) — dessin puis `enum` + `switch` ; pistes maison 2 à 6 en overview.
- **Schémas** : `tools/schemas/apu09_*.py` → `00 images/*.svg` + `Excalidraw/`. Les scripts s'appuient sur un nouveau `tools/schemas/schema_lib.py` (boîtes, flèches, cercles).
- Composition retirée ; Observer → APU-05.

> [!warning] Renommer dans Obsidian
> Les fichiers gardent leur ancien nom (`… - Observer, State et composition.md`) dans `lectures/`, `slides/` et `exercises/`. Les renommer dans Obsidian en `GPR-UN-APU-09 - State, un pattern de gameplay` met les liens à jour tout seul.
