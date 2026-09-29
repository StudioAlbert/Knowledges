---
status: To do
manual_order: 2
parent: "[[APU 04 APU 05 APU 09 deviennent]]"
slides:
  - "[[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|Slides APU-04]]"
exercices:
  - "[[01 courses/exercises/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|Exos APU-04]]"
---
(Adapter sources connues ne pas decouper le deck, creer le deck)

- [ ] Nouveau projet exemple :
	- [ ] Jeu de tourelle autos, elle visent la souris et tirent devant elles
		- [ ] Tir factice : RayCast + Particle System
		- [ ] Cible = Tour
	- [ ] Chaque tourelle dispose des caracteristiques suivantes :
		- [ ] Cadence de tir
		- [ ] degats
		- [ ] munitions max
		- [ ] temps de rechargement
		- [ ] ces stats donnent lieu a l'usage de scriptable objects, et permettent la creation de profils de tourelles - Niveau 1, 2, 3, etc...
	- [ ] Use Case Shared datas
		- [ ] Chaque rechargement coute de l'or (or global = int value)
		- [ ] un timer s'ecoule, quand il est atteint le jeu s'arrette (compteur = int value)
		- [ ] la liste des cibles-tours detruites et inactives est stockee dans un runtime set
			- [ ] Demonstation via une scene Game et une scene Shop, quand on passe du shop au game, le statut des cible (inactives ou non) est preserve via un runtime set 
- [ ] Apres validation du projet => Nouveau Plan
	- [ ] Principe de base des Scriptable objects : BaseCode + Assets duplication / variants
	- [ ] Use case : datas
		- [ ] Model / View / presenter 
		- [ ] Weapon profile
	- [ ] Use case : Shared datas
		- [ ] Bind datas to UI Toolkit
		- [ ] Float value
		- [ ] Runtime set
	- [ ] Advanced use case : Event channel
		- [ ] Simple exemple de code extrait du repo : https://github.com/StudioAlbert/MallLifeStealthGame
	- [ ] Les exemples de code sont tirés du projet


## Traité le 28.09 — à vérifier

- **Deck créé** : [[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code]] — 17 slides, `publish: false`, sans découpage.
	- Adapté de `scriptable_objects.md` : `LootData` + tableau des 4 profils, `FloatValue` (variable partagée), Runtime Set.
	- Ajouts depuis le manuel et l'e-book Unity : asset vs instance (schéma), flyweight / mémoire, le piège de l'état qui persiste (éditeur vs build), ce qu'on y met ou pas.
	- Les canaux d'événement sont renvoyés à APU-05.
- **Atelier** : statistiques d'ennemis du Dungeon Crawler en `EnemyStats`, araignée géante sans code ; pistes maison en overview.

> [!warning] Renommer dans Obsidian
> `… - ScriptableObjects — les données hors du code.md` peut garder son nom, ou devenir `GPR-UN-APU-04 - ScriptableObjects` (le titre du deck a été raccourci).
