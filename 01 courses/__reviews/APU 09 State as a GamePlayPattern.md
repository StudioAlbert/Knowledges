---
status: To check
manual_order: 2
parent:
  - "[[APU 04 APU 05 APU 09 deviennent]]"
slides:
  - "[[01 courses/slides/Unity/GPR-UN-APU-09 - Observer, State et composition|Slides APU-09]]"
exercices:
  - "[[01 courses/exercises/Unity/GPR-UN-APU-09 - Observer, State et composition|Exos APU-09]]"
url_test: http://localhost:50822/unity/gpr-un-apu-09/
---

- [x] Proposer Companion Unity permettant d'explorer les cas d'usage
	- [x] une scene par cas d'usage
	- [x] une UI pour visualiser l'etat des states machines
	- [x] l'utilisation de la state machine generique issue de ce repo https://github.com/StudioAlbert/MallLifeStealthGame/tree/main/MallLife-UnityProject/Assets/03%20-%20Scripts/Core/StateMachine
	- [x] Cas d'usage :
		- [x] Hero : Jumping, Landing, Grounded (Simple cube jumping on Bar Space presses, Landing cooldown via coroutine)
		- [x] Guard : Idle, Patrolling, OnAlarm
		- [x] QTE : Invite, Confirn, Fail, Success, Closing => every state display a UI Panel, and transition are mapped on UI buttons (Canvas)
		- [x] Tour par tour : pas d'idée de gameplay, kind of Xcom Game, 2 Tourelles se tirant dessus, une est controllée par le joueur, l'autre est en auto. Le joueur passe le tour avec un bouton next, l'IA passe quand elle est a court de munitions
- [x] Presenter la state machine generique du repo ci dessus

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

## Traité le 06.10 — à vérifier (séance du 15.10)

- **Companion** : `01 courses/companion projects/Unity/GPR-UN-APU-09 - State machine`,
  sous-module du vault, dépôt public
  [GPR_UN_APU_09_StateMachine](https://github.com/StudioAlbert/GPR_UN_APU_09_StateMachine).
  Unity 6000.3.25f1, URP. Quatre scènes : `01 - Hero`, `02 - Guard`, `03 - QTE`,
  `04 - TurnBased`. Démos techniques volontairement minimalistes — primitives et panneau de
  debug, pas de jeu.
- **Machine générique** reprise **telle quelle** du dépôt MallLife (décision du 06.10 : les
  correctifs viendront plus tard, aucun défaut n'est apparu à l'usage).
- **UI de visualisation** : `StateMachineDebugPanel` (IMGUI) liste toutes les machines de la
  scène ; une démo n'a qu'à implémenter `IStateMachineProbe`. Rien à câbler.
- **Deck** : nouvelle section « Une machine réutilisable » — schéma
  `apu09_machine_generique.svg` (généré par `tools/schemas/apu09_machine_generique.py`),
  `AddTransition` / `AddAnyTransition`, ce que fait `Tick`, et les quatre démos. Corrigé au
  passage : il manquait un séparateur avant « À retenir », qui se collait à la slide
  précédente.
- **Notes de séance et d'exercices** mises à jour pour pointer le companion.

> [!warning] Restes à vérifier à la main
> - **Les deux scènes au clavier n'ont pas pu être vérifiées au-delà du premier frame.**
>   La boucle de l'éditeur ne tournait qu'en pas-à-pas, et ni l'injection Input System ni
>   `simulate_key` n'atteignaient la fenêtre de `wasPressedThisFrame`. `03 - QTE` et
>   `04 - TurnBased` (pilotées par boutons) ont été jouées de bout en bout ; `01 - Hero`
>   (Espace) et `02 - Guard` (A / R) demandent une minute de vérification manuelle.
> - **Date de la séance** : le frontmatter de la note de séance dit le 15.10, son encadré
>   le 01.10. Aurora fait autorité.
> - `PlayerSettings.runInBackground` a été activé dans le companion.
