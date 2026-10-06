---
status: To do
manual_order: 3
parent:
  - "[[APU 04 APU 05 APU 09 deviennent]]"
slides:
  - "[[01 courses/slides/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|Slides APU-05]]"
exercices:
  - "[[01 courses/exercises/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|Exos APU-05]]"
---
- [ ] Faire propositions dans cette note des différentes situations dans un jeu de voiture qui permettent d'utiliser le pattern; relier ces situations a une implementation parmi les 3 identifiées 

- Sources :
	- https://learn.unity.com/tutorial/create-modular-and-maintainable-code-with-the-observer-pattern
	- https://gist.github.com/adammyhre/353195d4870e8fd0cc0028659e66f208
	- https://www.unitydesignpatterns.com/patterns/observer
	- https://gameprogrammingpatterns.com/observer.html
	- https://refactoring.guru/design-patterns/observer
	- Scriptable Events : https://github.com/StudioAlbert/MallLifeStealthGame/tree/main/MallLife-UnityProject/Assets/03%20-%20Scripts/_Datas/Events

## Traité le 28.09 — à vérifier

- **Deck** réécrit : [[01 courses/slides/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven]] — *Observer, prévenir sans connaître*, 21 slides, `publish: false`.
	- Problème (branche `01-srp` : `PlayerHealth → HealthBar`), schéma avant / après, le pattern.
	- Trois façons : `event Action` (sujet, observateur), `UnityEvent`, canal en SO (schéma + `GenericEventChannelSO` et `AlertManager` de MallLife), tableau de choix.
	- Pièges : abonné fantôme (la lambda de `QuestManager`), `event` ou pas, traçabilité ; `Observable<T>` d'après le gist.
- **Atelier** rédigé ; pistes maison en overview.
- Sources : toutes lues sauf le dépôt MallLife en ligne (robots.txt) — lu en local dans `D:\_dev\repos\unity\MallLifeStealthGame`.
- **Refactoring.Guru** n'a pas pu être relu (lien conservé tel quel).

> [!warning] Renommer dans Obsidian
> Fichiers `… - ScriptableObjects — architecture data-driven.md` (lectures, slides, exercises) → `GPR-UN-APU-05 - Observer, prévenir sans connaître`.
