---
slides: "[[01 courses/slides/C++/GPR-CF-SBD-01 - Afficher la fenêtre et les sprites]]"
exercices: "[[01 courses/exercises/C++/GPR-CF-SBD - Le platformer, etape par etape]]"
---
- [x] Reorganiser toutes la section SBD (Renommer lectures, garder le nombre de séances)
- [x] Slide **Un jeu est une boucle** : citer le snippet SFML de base
- [x] Supprimer la slide **Deux mondes**
- [x] Supprimer la slide **Ce qu'un moteur fait pour vous**
	- [x] Prendre contenu existant et redispatcher
	- [x] Produire nouveaux decks
	- [x] Rester pratique, produire citations de code
	- [x] 1 - Afficher Fenetre + Sprites
	- [x] 2 - GamePlay - Events
		- [x] Window close
		- [x] Window resize
		- [x] Inputs clavier / Manette
	- [x] 3 - Deplacer / Animer : Comment gérer le temps ? 
		- [x] Expliciter cas du delta time
		- [x] L'utiliser pour les deplacement
		- [x] Principes des sprites sheets -> cas d'usage en animation
	- [x] 4 - Box 2D : Deck inchangé
	- [x] 5 - Relier monde physique / monde graphique
		- [x] Faire classe de conversion de positions
		- [x] Collisions
	- [x] 6 - Mini-séance permettant de répertorier les différents tips techniques et de gameplay d'un platformer
		- [x] Ground Check
		- [x] Coyote Time
		- [x] Le fun dans un platformer
		- [x] L'accessibilité du game play
- [x] Review https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples
	- [x] Transfer the VisualStudio solution to generic CMAKE
	- [x] Is it Every targets SFML 3 compatible, Review changes
- [x] Write Down a summative platformer statement
	- [x] Based on this statement : 01 courses/projects/Unity/_archives_to_cut/2D Platformer
	- [x] Rephrased for a C++ / SFML / Box2D stack
	- [x] Rephrased for beginner programmers 

- [x] Dévellopper le contenu en se basant sur les sources
	- [x] Sources complémentaires ci dessous
	- [x] Decks existants
- [x] Serie de cours orientée pratique
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

## Traité le 20.10 — la série est réorganisée

### Les six séances, renommées

| Code | Avant | Maintenant |
|---|---|---|
| SBD-01 | Boucle de jeu et fenêtre | **Afficher la fenêtre et les sprites** |
| SBD-02 | Afficher | **Gameplay et événements** |
| SBD-03 | Son | **Déplacer et animer** |
| SBD-04 | Le monde Box2D | inchangé |
| SBD-05 | Relier physique et graphique | inchangé |
| SBD-06 | Un platformer, concrètement | **Les ficelles d'un platformer** |

Les notes de séance **et** les decks sont renommés, et toutes les références du vault
suivent : la feuille d'exercices, les archives, le kanban. Aucun lien cassé.

> [!warning] Le son sort du programme
> SBD-03 s'appelait *Son* et devient *Déplacer et animer*. Ton nouveau plan ne place
> l'audio nulle part — ni dans les six séances, ni dans la feuille. Le dépôt d'exemples a
> pourtant deux cibles prêtes, `Audio` et `Sound`, et ce sont **les seules avec HelloWorld
> et TimeClock à compiler en SFML 3**. Si l'audio doit revenir quelque part, dis où ; sinon
> je le laisse sorti.

### Le contenu, redispatché

La feuille d'exercices suit le nouveau découpage, étape par étape :

| Étape | Ce qu'on écrit maintenant |
|---|---|
| 1 | fenêtre, boucle `effacer / dessiner / afficher`, formes, sprite, et le carré blanc provoqué exprès |
| 2 | `Closed` et `Resized`, clavier **puis** manette, et la différence événement / état |
| 3 | `sf::Clock`, le `dt`, le framerate, et la sprite sheet à cadence fixe |
| 4 | Box2D, inchangé |
| 5 | **une classe de conversion mètres / pixels**, la copie des positions, le `ContactListener` |
| 6 | ground check, **coyote time**, **jump buffer**, wall jump, one way — et une page sur ce qui rend le saut agréable |

L'étape 6 gagne l'accessibilité, que ton plan demandait et qui n'était nulle part : touches
reconfigurables, pas de combinaison à trois doigts, un niveau qui pardonne.

### Le deck SBD-01

Réécrit sur le nouveau périmètre, 16 slides. Il ne parle plus ni de la boucle de jeu
temporelle ni des deux mondes : **tout le temps part en SBD-03**, et les deux slides que tu
as barrées — *Deux mondes* et *Ce qu'un moteur fait pour vous* — ont disparu.

Le code est cité, pas paraphrasé : le programme minimal est `HelloWorld` du dépôt
d'exemples, repris tel quel. Quatre blocs de code SFML 3, un piège par slide.

### Le dépôt d'exemples, audité

`StudioAlbert/GPR-CF-SBD-XX---SFML-Examples`, dix-huit cibles passées au crible des
marqueurs qui ne compilent pas en SFML 3.

| État | Cibles |
|---|---|
| **compile en SFML 3** | `Audio`, `ConstMethods`, `HelloWorld`, `TimeClock` |
| `sf::Event` déclaré à l'avance, `pollEvent(e)` | `Events-a` à `-d`, `Graphics`, `LevelEditor`, `MoveAndJump`, `Sound`, `Views`, `Views.cpp` |
| `sprite.setTexture()` | `Animation`, `AnimationClass`, `Events-c`, `Events-d`, `Motor`, `OOPHero`, `Views` |
| `setPosition(x, y)` / `setOrigin(x, y)` | `Events-a`, `Events-c`, `Events-d`, `Graphics`, `LevelEditor`, `Motor`, `MoveAndJump`, `Views` |

**Quatre sur dix-huit sont propres.** Un détail au passage : `Views.cpp` existe à la racine
**et** dans `Views/`, en double.

## Ce qui reste, et que je n'ai pas fait

1. **Les decks SBD-02 à SBD-06** — renommés, mais toujours leurs squelettes. Ils sont dans
   la file, chacun à son tour.
2. **La migration CMake du dépôt d'exemples** — la solution Visual Studio est toujours là, et
   quatorze cibles sont à porter en SFML 3. C'est un chantier dans un dépôt externe, pas une
   révision de séance : dis-moi si je l'ouvre, et dans quel ordre.
3. **L'énoncé summative** — la source `_archives_to_cut/2D Platformer` est lue : genre,
   features attendues, deux options à choisir dont le coyote time et le wall jump, et des
   références Mario. Elle est écrite pour Unity et pour un public qui connaît déjà un moteur.
   La transposition C++ / SFML / Box2D reste à écrire.

## Les quatre decks restants, écrits le 20.10

| Deck | Slides | Hors cadre | Ce qu'il porte |
|---|---|---|---|
| SBD-03 — Déplacer et animer | 15 | 0 | le `dt` mesuré une fois, le piège du déplacement par image, limiter ou se synchroniser, la planche découpée à cadence fixe |
| SBD-04 — Le monde Box2D | 13 | 0 | le monde, le **pas fixe** rattrapé par un `while`, les trois types de corps, la forme et sa matière, les unités |
| SBD-05 — Relier | 15 | 0 | la classe de conversion, les deux axes Y opposés, la copie dans un seul sens, le `ContactListener` et `UserData` |
| SBD-06 — Les ficelles | 20 | 0 | capteur de sol et **compteur**, coyote time, jump buffer, wall jump, le fun, l'accessibilité |

Le widget `boucle_de_jeu_widget` **change de séance** : il mesurait le temps, il part donc en
SBD-03, sur son onglet `#course`. SBD-01 ne le porte plus.

**Schéma neuf** `sbd04_metres_pixels.svg` : les deux mondes côte à côte, le facteur au
milieu, les deux fonctions de conversion, et la bande rouge des symptômes quand on oublie —
un héros de 180 mètres, une gravité qui paraît nulle, des forces sans effet. C'est la figure
que SBD-05 reprend en classe de conversion.

Trois ficelles de SBD-06 ne venaient d'aucun squelette et me paraissent indispensables :

- **le compteur de contacts** au lieu d'un booléen — un booléen casse sur toute arête entre
  deux tuiles de sol, et le héros perd le droit de sauter une image sur deux ;
- **l'entrée ignorée quelques dixièmes après un wall jump**, sans quoi le personnage recolle
  au mur et la ficelle ne marche pas ;
- **l'accessibilité liée au game feel** : coyote time et jump buffer sont des mesures
  d'accessibilité avant d'être des astuces.

## Ce qui reste ouvert

1. **Box2D 2.4, toujours pas tranché.** Les quatre decks écrivent `b2World`, `b2BodyDef`,
   `b2Fixture`, `b2ContactListener` — c'est Box2D **2.4**. Box2D 3 a supprimé `b2Fixture` et
   remplacé les pointeurs par des poignées (`b2WorldId`, `b2BodyId`), donc **tout le code de
   SBD-04, 05 et 06 serait à réécrire**. J'ai gardé 2.4 parce que c'est le vocabulaire de tes
   périmètres d'origine. Si tu veux Box2D 3, c'est maintenant qu'il faut le dire.
2. **`box2d_corps_widget.html` n'est pas construit.** Le squelette de SBD-04 le proposait : un
   bac à sable avec un corps de chaque type, un curseur de poussée, et densité / friction /
   restitution en direct. Le tableau des trois types le remplace pour l'instant.
3. **Aucun des quatre decks ne cite le dépôt d'exemples.** Tu étais en train de le migrer en
   CMake pendant que je les écrivais, et `Motor`, `MoveAndJump` et `LevelEditor` sont encore
   en SFML 2 — je ne voulais pas y envoyer les étudiants. Dès qu'ils compilent, SBD-03, 05 et
   06 ont chacune une cible à citer.
