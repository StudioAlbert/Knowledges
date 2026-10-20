---
slides: "[[01 courses/slides/Theory/TC-FT-PCL-01 - Couplage et cohésion]]"
atelier: "[[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer]]"
---
- [x] Pas d'exercices (supprimer note)
- [x] Illustrer par des cas d'usage tiré des repos indiqués en sources
- [x] La slide Atelier renvoie a la fiche d'exercices
	- [x] Proposer un atelier de conception du platformer "Concevoir un platformer"
		- [x] Decrire les fonctionnalités
		- [x] Decrire les classes
		- [x] Definir les relations entre ces classes
		- [x] Rendu attendu, un schema

-----------------
### Sources

https://github.com/SAE-Geneve/CityBuilder_SFML
https://github.com/SAE-Geneve/925-4FSC0PF001-SpaceShooter

## Traité le 20.10 — à vérifier

**Feuille d'exercices supprimée** : `exercises/Theory/TC-FT-PCL-01 - Couplage et cohésion.md`
n'existe plus, et la clé `exercices:` est retirée du frontmatter de cette fiche. Le site ne
rattache donc plus d'exercice **propre** à PCL-01 — c'est voulu. L'atelier partagé, lui, s'y
rattache par `seances:`.

**Deck**, 20 slides, de 13 titres sans contenu. Aucune slide hors cadre.

### Les cas viennent bien de tes deux dépôts

J'ai lu les deux, et ils se répondent si bien que le deck est construit sur le contraste.

**`925-4FSC0PF001-SpaceShooter`** — tout à plat, un seul dossier. `StarshipPlayer` est le cas
d'école, et il est **réel** : il hérite de `sf::Drawable`, tient les textures du vaisseau
**et** du bouclier, l'index d'animation du bouclier, son chrono, le `Motor`, le
`ProjectileManager`, la cadence de tir — et fait `Load`, `Update`, `CheckCollisions`,
`CheckProjectileCollisions`, `HandleEvent`, `SetPosition`, `draw`. La slide *Compter ses
raisons de changer* en dénombre **huit**.

Deux détails de ce dépôt servent d'exemples précis :

- `void Update(const sf::RenderWindow&, float)` — le joueur a besoin de la **fenêtre** pour
  avancer d'une image, juste pour connaître deux bords d'écran. C'est la slide *La seule
  définition qui compte*.
- `EnemyManager::Update` construit un `std::random_device` et un `mt19937` **à chaque image**,
  parce que la décision de spawn vit dans la mise à jour. C'est un défaut de conception qui
  a un coût mesurable — assez rare pour qu'il vaille la note de présentation.

**`CityBuilder_SFML`** — trois couches, `core/` puis `api/` puis `game/`. `core/include/`
tient les maths et les interfaces de l'IA (`bt_node`, `bt_selector`, `a_star`), `api/` les
implémentations (ui, motion, resources, graphics), `game/game.cc` l'assemblage — et il
inclut `ui/button_factory.h` et `ui/clickable.h`, soit exactement le vocabulaire de
l'inversion de dépendance. **Les flèches ne remontent jamais.**

**Schéma** `pcl01_direction_dependances.svg` : à gauche l'étoile du SpaceShooter autour de
`StarshipPlayer`, à droite les trois couches gigognes du CityBuilder.

## Deuxième passe, le 20.10 — l'atelier

[[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer|Concevoir un platformer]]
est créé. **C'est ici qu'il se définit**, et les deux autres séances du bloc le reprennent :

| Séance | Ce qu'elle en fait |
|---|---|
| **PCL-01** | étape 1 — fonctionnalités, classes, relations, et le schéma |
| PCL-03 | étape 2 — y chercher des patterns, et assumer un « non » |
| PCL-04 | étape 3 — trancher chaque flèche d'héritage |

La feuille commence par **le jeu en six lignes**, pour que tout le monde conçoive le même et
que les schémas soient comparables. Les trois sortes de flèches sont imposées — `utilise`,
`contient`, `est un` — parce que c'est exactement le vocabulaire des trois séances.

La **slide Atelier est réécrite** : elle reprend les quatre temps de l'étape 1 et renvoie à
la feuille. L'ancien atelier — dessiner le graphe de dépendances du SpaceShooter — disparaît
du deck, mais sa substance est dans l'étape 1 (les relations, et la classe la plus coûteuse à
changer), et le SpaceShooter reste étudié dans le corps du cours.

> [!check] Vérifié sur le serveur de test
> La feuille se rattache bien aux trois séances par `seances:` : elle apparaît dans l'onglet
> *Exercices* de `/theory/tc-ft-pcl-01/`, et le lien de la slide y mène.

## Deux arbitrages, dont un qui tient toujours

**1. Le widget `couplage_widget.html` n'est toujours pas construit.** Il était proposé par le
squelette, pas par cette fiche, et la direction des dépendances est une image **statique** :
le schéma la montre entièrement. Ce que le widget ajouterait, c'est le **compte** de ce qu'un
changement met en danger, en cliquant une classe. Dis-le si tu le veux.

**2. Le deck nomme un projet d'étudiants comme contre-exemple.** `StarshipPlayer` est lu en
séance avec ses défauts. La note de présentation le dit explicitement : *ne pas en faire un
procès, il marche, il a été livré, c'est le code qu'on écrit tous*. Si le dépôt est celui
d'une promotion encore présente, il vaut peut-être mieux anonymiser — **je ne sais pas qui
l'a écrit**, et c'est ta décision, pas la mienne.
