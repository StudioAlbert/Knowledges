---
status: To check
manual_order: 2
parent: "[[APU 04 APU 05 APU 09 deviennent]]"
slides:
  - "[[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|Slides APU-04]]"
exercices:
  - "[[01 courses/exercises/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|Exos APU-04]]"
---
(Adapter sources connues ne pas decouper le deck, creer le deck)

- [x] Nouveau projet exemple :
	- [x] Jeu de tourelle autos, elle visent la souris et tirent devant elles
		- [x] Tir factice : RayCast + Particle System
		- [x] Cible = Tour
	- [x] Chaque tourelle dispose des caracteristiques suivantes :
		- [x] Cadence de tir
		- [x] degats
		- [x] munitions max
		- [x] temps de rechargement
		- [x] ces stats donnent lieu a l'usage de scriptable objects, et permettent la creation de profils de tourelles - Niveau 1, 2, 3, etc...
	- [x] Use Case Shared datas
		- [x] Chaque rechargement coute de l'or (or global = int value)
		- [x] un timer s'ecoule, quand il est atteint le jeu s'arrette (compteur = int value)
		- [x] la liste des cibles-tours detruites et inactives est stockee dans un runtime set
			- [x] Demonstation via une scene Game et une scene Shop, quand on passe du shop au game, le statut des cible (inactives ou non) est preserve via un runtime set 
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

## Traité le 29.09 — projet companion à valider

Projet `01 courses/companion projects/Unity/GPR-UN-APU-04 - ScriptableObjects`
(Unity 6000.4.12f1, URP), sous-module du vault, dépôt public
[StudioAlbert/GPR_UN_APU_04_ScriptableObjects](https://github.com/StudioAlbert/GPR_UN_APU_04_ScriptableObjects).

Décors : [Kenney Tower Defense Kit](https://kenney.nl/assets/tower-defense-kit) (CC0),
réduit au FBX et rangé par le skill de renommage dans la structure numérotée `00`–`08`.

**Ce qui tourne**, vérifié en Play mode :

| Point du cahier des charges | État |
|---|---|
| 3 tourelles visent la souris, tirent seules | ✅ raycast + éclair de canon + trait de tir |
| 6 cibles-tours encaissent et tombent | ✅ avec effet de chute détaché |
| `TurretProfile` × 3 (Mk I / II / III) | ✅ cadence, dégâts, portée, chargeur, rechargement, prix, couleur |
| Rechargement payé en or (`IntVariable`) | ✅ sans or, la tourelle reste muette |
| Chrono partagé, fin de partie | ✅ à zéro les tourelles cessent le feu, panneau de fin |
| Runtime set des cibles debout | ✅ inscription en `OnEnable` / `OnDisable` |
| Cibles détruites préservées Jeu ↔ Boutique | ✅ via des assets `TowerId`, jamais des objets de scène |
| HUD + boutique en UI Toolkit | ✅ UXML / USS, présentateurs séparés des données |

**Ajouts par rapport au cahier des charges**, à valider ou retirer :

- une cible détruite **rapporte 30 or**. Sans cela l'or de départ était consommé en
  ~30 s et la boutique restait inatteignable ; et c'est un deuxième écrivain sur le
  même asset partagé, ce qui sert le propos.
- la boutique vend le **profil suivant** (`TurretProfileVariable`), lu par la tourelle
  de droite : une donnée partagée peut être une référence, pas seulement un nombre.
  Les deux autres tourelles gardent un profil posé dans l'Inspector, pour montrer les
  deux cas côte à côte.

**Réserves :**

- `com.unity.pipeline` est encore dans le manifeste (il sert à piloter l'éditeur).
  À retirer avant publication aux étudiants, comme pour le Dungeon Crawler.
- `Assets/UI Toolkit/` est créé par Unity hors de la structure numérotée ; laissé en
  place, il contient le thème par défaut référencé par les `PanelSettings`.

## Reprise en main — chantier en cours

Le projet est repassé entre les mains de l'auteur après la livraison ci-dessus :

- champs sérialisés en `_camelCase`, `accent` devenu `Color`, `shotsPerSecond` devenu
  `ShootingRate` ; les trois profils ont été ressaisis (Mk I rapide et faible, Mk II
  intermédiaire, Mk III lent et lourd).
- la visée passe par un `MousePointer` partagé qui lance un raycast sur la géométrie
  au lieu de projeter sur un plan, et affiche un repère sous le curseur.
- le tir devient une coroutine, lancée seulement quand le pointeur accroche une
  surface — ce qui règle la réserve « les tourelles tirent dans le vide ».

> [!warning] Connu et assumé
> Le rechargement est cassé : dans `Turret.Update`, la branche `_ammo <= 0` n'arrête
> pas la coroutine, donc une tourelle sans or continue de tirer et les munitions
> passent en négatif. Restent aussi des `Debug.Log` à chaque tir et un
> `_mousePointer` déréférencé sans garde ligne 93.

**Ensuite**, une fois le chantier stabilisé : réécrire le deck sur ce projet (le plan
ci-dessus), les 17 slides actuelles s'appuyant encore sur le Dungeon Crawler.
