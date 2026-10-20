---
slides: "[[01 courses/slides/C++/GPR-CF-SBD-01 - Boucle de jeu et fenêtre]]"
exercices: "[[01 courses/exercises/C++/GPR-CF-SBD - Le platformer, etape par etape]]"
---
- [ ] Reorganiser toutes la section SBD (Renommer lectures, garder le nombre de séances)
	- [ ] Prendre contenu existant et redispatcher
	- [ ] Produire nouveaux decks
	- [ ] Rester pratique, produire citations de code
	- [ ] 1 - Afficher Fenetre + Sprites
	- [ ] 2 - GamePlay - Events
		- [ ] Window close
		- [ ] Window resize
		- [ ] Inputs clavier / Manette
	- [ ] 3 - Deplacer / Animer : Comment gérer le temps ? 
		- [ ] Expliciter cas du delta time
		- [ ] L'utiliser pour les deplacement
		- [ ] Principes des sprites sheets -> cas d'usage en animation
	- [ ] 4 - Box 2D : Deck inchangé
	- [ ] 5 - Relier monde physique / monde graphique
		- [ ] Faire classe de conversion de positions
		- [ ] Collisions
	- [ ] 6 - Mini-séance permettant de répertorier les différents tips techniques et de gameplay d'un platformer
		- [ ] Ground Check
		- [ ] Coyote Time
		- [ ] Le fun dans un platformer
		- [ ] L'accessibilité du game play
- [ ] Review https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples
	- [ ] Transfer the VisualStudio solution to generic CMAKE
	- [ ] Is it Every targets SFML 3 compatible, Review changes
- [ ] Write Down a summative platformer statement
	- [ ] Based on this statement : 01 courses/projects/Unity/_archives_to_cut/2D Platformer
	- [ ] Rephrased for a C++ / SFML / Box2D stack
	- [ ] Rephrased for beginner programmers 

- [x] Dévellopper le contenu en se basant sur les sources
	- [x] Sources complémentaires ci dessous
	- [x] Decks existants
- [ ] Serie de cours orientée pratique
	- [x] Deck rapide — **fait pour SBD-01 seulement**, comme modèle de format
	- [x] Chaque cours se termine par une mise en oeuvre d'1h sur chacune des problematiques
		- [x] Revision des fiches d'exercices en fonction : une seule fiche pour toute la serie
		- [x] l'aboutissement est un platformer => fiche exercice Summative pour ce projet platformer => chaque seance doit etre une etape du projet global => trouver decoupage adequat
- [x] Respect des standards SFML 3 uniquement — **dans ce qui est écrit**, pas encore dans les cinq decks restants
-------------------------------
### Sources complémentaires

- https://www.sfml-dev.org/tutorials/3.1/
- https://www.sfml-dev.org/documentation/3.1.0/
- https://github.com/jayjay1509/platformer
- https://github.com/StudioAlbert/GPR922_GPR4-1_SFML
  
  https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples

## Traité le 20.10 — à vérifier

### Le découpage, qui est la décision centrale

Les six périmètres de séance se plient tout seuls en six étapes d'un même projet. Chaque
séance **ajoute une couche** et ne repart jamais de zéro :

| Séance | Étape | Ce qui marche à la fin de l'heure |
|---|---|---|
| SBD-01 | 1 — la fenêtre et la boucle | un carré qui traverse l'écran en le même temps à 30 et à 144 fps |
| SBD-02 | 2 — le héros à l'écran | sprite animé, piloté au clavier, caméra qui suit |
| SBD-03 | 3 — le son | un bruit de saut, une musique, et la bonne classe pour chacun |
| SBD-04 | 4 — le monde physique | le héros tombe et s'arrête, **sans aucun sprite** |
| SBD-05 | 5 — relier les deux mondes | le sprite suit le corps, et `au sol` est fiable |
| SBD-06 | 6 — le contrôleur | pas de saut en l'air, wall jump, one-way platform |

L'étape 4 est celle qui demande le plus de confiance : on passe une heure à ne **rien**
afficher. C'est délibéré — séparer les deux mondes avant de les relier est tout le propos de
SBD-05.

### Une seule feuille, comme demandé

Les **six** fiches d'exercices sont supprimées et remplacées par
[[01 courses/exercises/C++/GPR-CF-SBD - Le platformer, etape par etape|Le platformer, étape par étape]],
rattachée aux six séances par `seances:` en frontmatter. Les six notes de séance pointent
dessus et annoncent leur numéro d'étape.

Chaque étape porte le même gabarit : **ce qu'on écrit**, les quatre ou cinq gestes, **ce
qu'on vérifie** — une recette unique et non négociable — et **le piège**. Le rendu summative
de fin de série est décrit : le jeu, six étapes visibles dans l'historique git, et une page
d'écrit.

Ce qui a été gardé des anciennes fiches : *le carré qui va trop vite* et *le pas fixe*, qui
étaient les deux meilleurs exercices du lot.

### SFML 3, vérifié sur la doc officielle

Je n'ai pas écrit l'API de mémoire : j'ai lu
[tutorials/3.1/window/events](https://www.sfml-dev.org/tutorials/3.1/window/events/) et
[tutorials/3.1/graphics/sprite](https://www.sfml-dev.org/tutorials/3.1/graphics/sprite/).

| SFML 2 | SFML 3 |
|---|---|
| `sf::VideoMode(800, 600)` | `sf::VideoMode({800u, 600u})` |
| `sf::Event e; while (window.pollEvent(e))` | `while (const std::optional event = window.pollEvent())` |
| `e.type == sf::Event::Closed` | `event->is<sf::Event::Closed>()` |
| `e.key.code == sf::Keyboard::Escape` | `event->getIf<sf::Event::KeyPressed>()`, puis `->scancode` |
| `sf::Sprite s; s.setTexture(t);` | `sf::Sprite s(t);` — la texture est obligatoire |

Ce tableau est dans la feuille d'exercices, en encadré d'avertissement.

> [!warning] Ton propre dépôt est en SFML 2
> `StudioAlbert/GPR922_GPR4-1_SFML` est une très bonne progression — `00-Starter`,
> `01-Window`, `02-Graphics`, `03a` à `03d-Events`, `04-Animation`, `05-Sound`, `06-Text`,
> `07-Fireball` — et c'est d'ailleurs le découpage dont je me suis inspiré. Mais
> `01-Window/src/main.cpp` ouvre encore sa fenêtre avec `sf::VideoMode(800, 600)` : **il ne
> compile pas en SFML 3**. Le donner tel quel aux étudiants les enverrait droit dans le mur
> que la feuille les prévient d'éviter.

### Le deck SBD-01, comme modèle de format

15 slides, aucune hors cadre. Format « deck rapide » : du code SFML 3 plutôt que du texte,
une slide par geste, et la mise en œuvre d'1 h annoncée en fin de deck avec ses quatre
points. C'est le gabarit à juger **avant** que je l'applique aux cinq autres.

**Widget** `boucle_de_jeu_widget.html`, celui que le squelette décrivait :

- onglet *frise* — les blocs d'une image, un curseur de temps de calcul, et le framerate
  obtenu. Dépasser le budget montre que la limite ne sert plus à rien.
- onglet *course* — deux carrés, l'un déplacé par image, l'autre par seconde, à 30, 60 ou
  144 fps. **C'est la démonstration de la séance** : à 144 fps le rouge est à l'arrivée
  quand le vert est au tiers.

## Trois arbitrages

**1. Box2D 2.4, pas Box2D 3.** Les périmètres de SBD-04 et SBD-05 parlent de `b2World`,
`b2Body`, `b2BodyDef` et `b2Fixture` — c'est le vocabulaire de **Box2D 2.4**. Box2D 3 a
supprimé `b2Fixture` (les formes s'attachent au corps) et remplacé les pointeurs par des
poignées (`b2WorldId`, `b2BodyId`). Ta fiche impose SFML 3 et ne dit **rien** de Box2D : j'ai
donc gardé 2.4, pour rester cohérent avec les périmètres. **C'est à trancher**, et ça change
les étapes 4 et 5.

**2. Seul le deck SBD-01 est réécrit.** Les cinq autres sont toujours leurs squelettes, en
`To prepare`. Réécrire six decks sans que tu aies validé le format aurait été six fois le
même pari. SBD-01 est passé en `To check` ; les cinq autres attendent ton avis sur le
gabarit.

**3. Le contenu du rendu summative est une proposition.** Personne ne me l'avait décrit :
j'ai choisi le jeu + l'historique git en six étapes + une page d'écrit. L'historique git est
le point discutable — il contraint les étudiants à committer proprement à chaque séance, ce
qui est une bonne chose mais ajoute une exigence qui n'était pas demandée.

## Ce qui reste

- les decks **SBD-02 à SBD-06**, à passer au format rapide et à SFML 3 ;
- **SBD-03 n'a pas de `review:`** et donc pas de checklist — elle est pourtant dans la série,
  et sa fiche d'exercices a été supprimée avec les autres ;
- le dépôt de départ du projet : la feuille parle d'« un projet CMake avec SFML fourni », il
  n'existe pas encore. Un companion `GPR_CF_SBD_Platformer` serait l'endroit logique.
