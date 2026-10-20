---
seances: [GPR-CF-SBD-01, GPR-CF-SBD-02, GPR-CF-SBD-03, GPR-CF-SBD-04, GPR-CF-SBD-05, GPR-CF-SBD-06]
---
# Le platformer, étape par étape

**Une seule feuille pour les six séances, et un seul projet.** Chaque séance se termine par
une heure de mise en œuvre qui ajoute une couche à ce projet. À la fin, vous avez un
platformer jouable — et vous l'avez écrit en six fois, sans jamais repartir de zéro.

> [!note] Le jeu a déjà été conçu
> C'est le platformer que vous avez dessiné en
> [[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer|Concevoir un platformer]],
> dans le bloc *Principes de Conception Logicielle*. Reprenez ce schéma : les classes de
> votre étape 1 sont celles que vous allez écrire ici.

> [!warning] SFML 3, et rien d'autre
> La plupart des exemples qui traînent sur le web sont en SFML 2, et **ils ne compilent pas**
> en SFML 3. Les différences qui vous toucheront :
>
> | SFML 2 | SFML 3 |
> |---|---|
> | `sf::VideoMode(800, 600)` | `sf::VideoMode({800u, 600u})` |
> | `sf::Event e; while (window.pollEvent(e))` | `while (const std::optional event = window.pollEvent())` |
> | `e.type == sf::Event::Closed` | `event->is<sf::Event::Closed>()` |
> | `e.key.code == sf::Keyboard::Escape` | `event->getIf<sf::Event::KeyPressed>()`, puis `->scancode == sf::Keyboard::Scancode::Escape` |
> | `sf::Sprite s; s.setTexture(t);` | `sf::Sprite s(t);` — la texture est **obligatoire** |
> | `s.setPosition(10.f, 50.f)` | `s.setPosition({10.f, 50.f})` |
>
> Référence : [tutoriels SFML 3.1](https://www.sfml-dev.org/tutorials/3.1/) et
> [documentation 3.1.0](https://www.sfml-dev.org/documentation/3.1.0/).

---

## Étape 1 — La fenêtre et la boucle

> Séance [[01 courses/slides/C++/GPR-CF-SBD-01 - Boucle de jeu et fenêtre|GPR-CF-SBD-01]]

**Ce qu'on écrit** : une fenêtre qui s'ouvre et se ferme, une boucle `effacer / dessiner /
afficher`, un `sf::Clock` qui donne le temps écoulé, et un carré pilotable au clavier.

1. ouvrir la fenêtre **sans** traiter les événements, constater qu'elle ne répond plus,
   puis ajouter la boucle. Dire en une phrase **qui** ferme la fenêtre.
2. faire varier la couleur de fond avec le temps, puis retirer l'effacement et décrire ce
   qu'on voit.
3. déplacer le carré en ajoutant une valeur **par image**, mesurer sa vitesse à 30 puis à
   144 images par seconde, et corriger en passant par le temps écoulé.
4. limiter le framerate, puis se synchroniser à l'écran, et afficher le framerate réel dans
   le titre.

**Ce qu'on vérifie** : le carré traverse l'écran en le **même temps** à 30 et à 144 images
par seconde. C'est la seule recette de l'étape, et elle ne se discute pas.

> [!tip] Le piège
> `position += vitesse` est faux. C'est `position += vitesse * dt`. Tout le reste de la
> série en dépend : une physique nourrie d'un `dt` faux donne des sauts qui changent de
> hauteur selon la machine.

---

## Étape 2 — Le héros à l'écran

> Séance [[01 courses/slides/C++/GPR-CF-SBD-02 - Afficher|GPR-CF-SBD-02]]

**Ce qu'on écrit** : une texture, un sprite, une animation par découpe de sprite sheet, le
déplacement au clavier, et une vue qui suit le héros.

1. charger une texture et afficher le héros. Le **sortir de sa portée** volontairement, et
   expliquer le carré blanc.
2. découper la sprite sheet et faire défiler les images à cadence fixe — indépendante du
   framerate.
3. piloter le héros au clavier, en réutilisant le `dt` de l'étape 1.
4. ajouter une `sf::View` qui le suit, et gérer le redimensionnement de la fenêtre sans
   déformer l'image.

**Ce qu'on vérifie** : l'animation tourne à la même vitesse quel que soit le framerate, et
redimensionner la fenêtre ne déforme rien.

> [!tip] Le piège
> `sf::Sprite` ne copie pas la texture, il garde un **pointeur** dessus. Une texture
> locale qui meurt à la fin de la fonction donne un sprite blanc — et c'est exactement
> l'exercice 1.

---

## Étape 3 — Le son

> Séance [[01 courses/slides/C++/GPR-CF-SBD-03 - Son|GPR-CF-SBD-03]]

**Ce qu'on écrit** : un bruit de saut, une musique de fond, et la bonne classe pour chacun.

1. jouer un son court au saut avec `sf::Sound`, et une musique de fond avec `sf::Music`.
2. mesurer la mémoire occupée dans les deux cas, et expliquer l'écart.
3. inverser volontairement les deux classes — la musique en `sf::Sound` — et décrire ce qui
   se passe au chargement.

**Ce qu'on vérifie** : vous savez dire, devant un fichier audio, laquelle des deux classes
l'ouvrir — et pourquoi.

> [!tip] Le piège
> `sf::Sound` a le même problème que `sf::Sprite` : il pointe vers un `sf::SoundBuffer` qui
> doit lui survivre. Un buffer local, et le son ne sort pas.

---

## Étape 4 — Le monde physique

> Séance [[01 courses/slides/C++/GPR-CF-SBD-04 - Le monde Box2D|GPR-CF-SBD-04]]

**Ce qu'on écrit** : un monde Box2D, un sol statique, un héros dynamique qui tombe dedans.
**Rien n'est encore dessiné** : on observe par la console.

1. créer le monde et sa gravité, et faire avancer la simulation dans la boucle.
2. créer le sol en corps **statique**, et le héros en corps **dynamique**.
3. afficher la position du héros à chaque image, et le voir tomber puis s'arrêter.
4. essayer les trois types de corps sur une plateforme mobile, et dire lequel convient.

**Ce qu'on vérifie** : le héros tombe, touche le sol, et s'arrête — sans qu'aucun sprite
n'existe encore.

> [!tip] Le piège
> Le monde physique est en **mètres**, l'écran en **pixels**. Décidez le facteur de
> conversion maintenant, écrivez-le une fois, et ne le recalculez jamais à la main. Un héros
> de 180 pixels de haut fait 180 mètres pour Box2D : il tombera comme un immeuble.

---

## Étape 5 — Relier les deux mondes

> Séance [[01 courses/slides/C++/GPR-CF-SBD-05 - Relier physique et graphique|GPR-CF-SBD-05]]

**Ce qu'on écrit** : la copie des positions du monde physique vers les sprites, et un
`ContactListener` qui dit quand le héros touche le sol.

1. à chaque image, recopier position et angle du corps vers le sprite. Dans ce sens
   **uniquement**.
2. brancher un `ContactListener`, et afficher un message à chaque contact.
3. utiliser `UserData` pour retrouver l'objet de jeu depuis le contact, et savoir **quel**
   objet a touché quoi.
4. en déduire un booléen `au sol`, et l'afficher à l'écran.
5. **reprendre votre schéma de conception** et dire, en deux lignes, ce que la physique a
   imposé que vous n'aviez pas prévu.

**Ce qu'on vérifie** : le sprite suit exactement le corps, et le booléen `au sol` est vrai
quand le héros est posé, faux quand il est en l'air.

> [!tip] Le piège
> La copie va **du physique vers le graphique**, jamais l'inverse. Déplacer un sprite à la
> main pendant que Box2D simule donne deux vérités qui divergent, et un personnage qui
> tremble.

---

## Étape 6 — Le contrôleur de plateforme

> Séance [[01 courses/slides/C++/GPR-CF-SBD-06 - Un platformer, concrètement|GPR-CF-SBD-06]]

**Ce qu'on écrit** : ce qui sépare « un corps physique » d'« un personnage de platformer ».

1. **ne pas sauter en l'air** : le saut n'est possible que si `au sol` est vrai.
2. **toucher le sol par le côté** : distinguer un contact sous les pieds d'un contact
   latéral, et ne pas autoriser le saut sur un mur.
3. **passer d'une plateforme à l'autre** sans rester accroché à l'arête.
4. **wall jump** : un saut possible au contact d'un mur, qui repousse à l'opposé.
5. **one way platform** : on la traverse par en dessous, on se pose dessus par en haut.

**Ce qu'on vérifie** : les cinq comportements, un par un, dans un niveau qui les contient
tous les cinq.

> [!tip] Le piège
> Un platformer agréable n'est jamais de la physique pure. Le *coyote time* — quelques
> centièmes de seconde pendant lesquels le saut reste possible après avoir quitté le sol —
> ne se déduit d'aucune équation. C'est une décision de game design, et elle s'écrit en dur.

---

## Le rendu — summative de la série

À rendre à la fin de la sixième séance, en un seul dépôt :

| | Ce qui est attendu |
|---|---|
| **le jeu** | un platformer jouable, avec un niveau qui contient sol, plateformes, un mur à wall-jumper et une plateforme traversable |
| **le code** | six étapes visibles dans l'historique git — une par séance |
| **l'écrit** | une page : le facteur mètre/pixel choisi et pourquoi, la façon dont `au sol` est détecté, et ce que vous avez réglé à la main plutôt que par la physique |

> [!check] Grille d'auto-évaluation
>
> | Je sais… | Vérification |
> |---|---|
> | écrire une boucle de jeu correcte | la vitesse ne dépend pas du framerate |
> | afficher et animer | l'animation tourne à cadence fixe, la fenêtre se redimensionne proprement |
> | choisir sa classe audio | je sais dire pourquoi la musique n'est pas un `sf::Sound` |
> | faire vivre un monde physique | le héros tombe et s'arrête sans sprite |
> | relier les deux mondes | la copie va dans un seul sens, et `au sol` est fiable |
> | écrire un contrôleur | les cinq comportements de l'étape 6 marchent dans le même niveau |
