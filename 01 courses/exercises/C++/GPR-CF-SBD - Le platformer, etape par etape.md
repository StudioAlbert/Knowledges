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

## Étape 1 — La fenêtre et les sprites

> Séance [[01 courses/slides/C++/GPR-CF-SBD-01 - Afficher la fenêtre et les sprites|GPR-CF-SBD-01]]

**Ce qu'on écrit** : une fenêtre qui s'ouvre et se ferme, la boucle `effacer / dessiner /
afficher`, un décor en formes, et le héros à l'écran.

1. ouvrir la fenêtre **sans** traiter les événements, constater qu'elle ne répond plus,
   puis ajouter la boucle. Dire en une phrase **qui** ferme la fenêtre.
2. faire varier la couleur de fond, puis retirer l'effacement et décrire ce qu'on voit.
3. poser un sol et deux plateformes en `sf::RectangleShape`, aux bonnes positions.
4. charger un PNG et afficher le héros dessus. Provoquer le **carré blanc** exprès en
   laissant mourir la texture, puis corriger.

**Ce qu'on vérifie** : la fenêtre se ferme à la croix **et** à Échap, et le héros s'affiche
sans carré blanc.

> [!tip] Le piège
> `sf::Sprite` ne copie pas la texture, il garde un **pointeur** dessus. Une texture locale
> qui meurt à la fin de la fonction donne un sprite blanc, sans erreur ni plantage.

---

## Étape 2 — Le gameplay et les événements

> Séance [[01 courses/slides/C++/GPR-CF-SBD-02 - Gameplay et événements|GPR-CF-SBD-02]]

**Ce qu'on écrit** : tout ce que la fenêtre reçoit — fermeture, redimensionnement, clavier,
manette — la différence entre un événement et un état, et le son, qui se branche au même
endroit.

1. traiter `Closed` et `Resized` : la vue doit suivre sans déformer le décor.
2. piloter le héros au **clavier**, d'abord avec `KeyPressed`, puis avec
   `sf::Keyboard::isKeyPressed`. Dire pourquoi le second convient au déplacement et le
   premier au saut.
3. brancher une **manette** : axes pour le déplacement, bouton pour le saut, et un repli
   propre quand aucune manette n'est branchée.
4. afficher à l'écran le dernier événement reçu — c'est l'outil de débogage de toute la
   série.
5. **le son** : un bruit de saut en `sf::Sound`, une musique de fond en `sf::Music`.
   Inverser volontairement les deux classes, mesurer la mémoire dans les deux cas, et
   expliquer l'écart.

**Ce qu'on vérifie** : le héros se déplace de la même façon au clavier et à la manette,
redimensionner la fenêtre ne déforme rien, et le saut fait du bruit.

> [!tip] Le piège
> Un **événement** dit « ça vient de changer », un **état** dit « c'est comme ça maintenant ».
> Déplacer un personnage sur `KeyPressed` donne le hoquet de la répétition clavier ; le faire
> sauter sur `isKeyPressed` donne un saut par image.
>
> Et pour le son, c'est le carré blanc de l'étape 1 qui revient : `sf::Sound` pointe vers son
> `sf::SoundBuffer`, exactement comme `sf::Sprite` vers sa `sf::Texture`.

---

## Étape 3 — Déplacer et animer : le temps

> Séance [[01 courses/slides/C++/GPR-CF-SBD-03 - Déplacer et animer|GPR-CF-SBD-03]]

**Ce qu'on écrit** : un `sf::Clock`, un déplacement qui ne dépend pas de la machine, et une
animation qui défile à cadence fixe.

1. mesurer le temps écoulé entre deux images, **une seule fois** par tour de boucle.
2. déplacer le carré en ajoutant une valeur **par image**, mesurer sa vitesse à 30 puis à
   144 images par seconde, et corriger en passant par le temps écoulé.
3. limiter le framerate, puis se synchroniser à l'écran, et afficher le framerate réel dans
   le titre.
4. découper la sprite sheet avec `setTextureRect` et faire défiler les poses à cadence fixe,
   **indépendante** du framerate.

**Ce qu'on vérifie** : le héros traverse l'écran en le **même temps** à 30 et à 144 images
par seconde, et son animation tourne à la même vitesse dans les deux cas.

> [!tip] Le piège
> `position += vitesse` est faux. C'est `position += vitesse * dt`. Tout le reste de la
> série en dépend : une physique nourrie d'un `dt` faux donne des sauts qui changent de
> hauteur selon la machine.

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

**Ce qu'on écrit** : une classe qui convertit mètres et pixels, la copie des positions vers
les sprites, et un `ContactListener` qui dit quand le héros touche le sol.

1. écrire une **classe de conversion** — `Metres(pixels)`, `Pixels(metres)` — et la seule
   constante du projet qui dit combien de pixels vaut un mètre. Plus aucun calcul à la main
   ailleurs.
2. à chaque image, recopier position et angle du corps vers le sprite. Dans ce sens
   **uniquement**.
3. brancher un `ContactListener`, et afficher un message à chaque contact.
4. utiliser `UserData` pour retrouver l'objet de jeu depuis le contact, et savoir **quel**
   objet a touché quoi.
5. en déduire un booléen `au sol`, et l'afficher à l'écran.
6. **reprendre votre schéma de conception** et dire, en deux lignes, ce que la physique a
   imposé que vous n'aviez pas prévu.

**Ce qu'on vérifie** : le sprite suit exactement le corps, et le booléen `au sol` est vrai
quand le héros est posé, faux quand il est en l'air.

> [!tip] Le piège
> La copie va **du physique vers le graphique**, jamais l'inverse. Déplacer un sprite à la
> main pendant que Box2D simule donne deux vérités qui divergent, et un personnage qui
> tremble.

---

## Étape 6 — Les ficelles d'un platformer

> Séance [[01 courses/slides/C++/GPR-CF-SBD-06 - Les ficelles d'un platformer|GPR-CF-SBD-06]]

**Ce qu'on écrit** : ce qui sépare « un corps physique » d'« un personnage agréable à
jouer ». Aucune de ces ficelles ne se déduit d'une équation.

1. **ground check** fiable : distinguer un contact sous les pieds d'un contact latéral, et
   ne pas autoriser le saut sur un mur.
2. **coyote time** : le saut reste possible quelques centièmes de seconde après avoir quitté
   le sol. Choisir la valeur qui vous paraît juste, et la justifier.
3. **jump buffer** : une touche pressée juste avant l'atterrissage déclenche le saut dès le
   contact.
4. **wall jump** et **one way platform** : un saut au contact d'un mur, et une plateforme
   qu'on traverse par en dessous.
5. écrire en une page **ce qui rend votre saut agréable** : les trois réglages que vous avez
   touchés, et ce que chacun change pour le joueur.

**Ce qu'on vérifie** : les cinq comportements, un par un, dans un niveau qui les contient
tous — et quelqu'un d'autre que vous doit pouvoir y jouer sans explication.

> [!tip] Le piège
> Un platformer agréable n'est jamais de la physique pure. Le *coyote time* ne se déduit
> d'aucune équation : c'est une décision de game design, et elle s'écrit en dur.
> L'accessibilité non plus — touches reconfigurables, pas de combinaison à trois doigts, et
> un niveau qui pardonne.

---

## Le rendu — summative de la série

L'énoncé complet est sur sa propre feuille :
[[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]].
Lisez-la **maintenant**, pas à la sixième séance : elle dit ce que chaque étape doit vous
laisser entre les mains.

> [!check] Grille d'auto-évaluation
>
> | Je sais… | Vérification |
> |---|---|
> | ouvrir une fenêtre et afficher | le héros s'affiche, et je sais dire pourquoi un sprite devient blanc |
> | traiter les entrées | clavier et manette donnent le même déplacement, la fenêtre se redimensionne proprement |
| choisir sa classe audio | je sais dire pourquoi une musique n'est pas un `sf::Sound` |
> | gérer le temps | la vitesse et l'animation ne dépendent pas du framerate |
> | faire vivre un monde physique | le héros tombe et s'arrête sans sprite |
> | relier les deux mondes | la conversion passe par une seule classe, et `au sol` est fiable |
> | rendre le jeu agréable | coyote time et jump buffer réglés, et je sais dire ce qu'ils changent |
