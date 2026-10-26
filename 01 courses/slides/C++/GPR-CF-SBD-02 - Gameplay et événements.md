---
title: GPR-CF-SBD-02 - Gameplay et événements
type: slides
subject: C++
duration_h: 1
bloc_gsda: SFML et Box2D
specialisation: C++ Fondamentaux
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
---

# Gameplay et événements
<!-- .slide: class="title" -->

### Étape 2 du platformer

<small>GPR-CF-SBD-02 · SFML et Box2D</small>

Note:
La fenêtre de SBD-01 affiche, mais elle n'écoute rien. Cette séance la rend
vivante : ce que le système lui dit, ce que le joueur lui fait, et — en fin
d'heure — le son, qui se branche exactement au même endroit.

---

## Objectifs

À la fin de la séance, vous savez :

- traiter `Closed`, `Resized` et le **focus**
- distinguer un **événement** d'un **état**, et choisir le bon
- lire une **manette**, et survivre à son absence
- jouer un son court et une musique, sans confondre les deux

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-01 - Afficher la fenêtre et les sprites|GPR-CF-SBD-01]].

---

# Ce que la fenêtre vous dit
<!-- .slide: class="title" -->

---

## La boucle d'événements

```cpp
while (const std::optional event = window.pollEvent())
{
    if (event->is<sf::Event::Closed>())
        window.close();

    else if (const auto* key = event->getIf<sf::Event::KeyPressed>())
        if (key->scancode == sf::Keyboard::Scancode::Escape)
            window.close();
}
```

`is<T>()` teste le type. `getIf<T>()` rend un **pointeur**, ou `nullptr`.

Note:
Un seul `pollEvent` par image, tout en haut de la boucle. Ne pas en mettre deux
dans deux fonctions différentes : le second ne verra jamais rien, la file est
déjà vide.

---

## Perdre le focus, et revenir

```cpp
if (event->is<sf::Event::FocusLost>())
    jeu.Pause();

if (event->is<sf::Event::FocusGained>())
    jeu.Reprendre();
```

Le joueur a cliqué ailleurs : **mettez le jeu en pause**. C'est deux lignes, et
ça évite de mourir pendant qu'on répond à un message.

---

## Redimensionner sans déformer

```cpp
if (const auto* resized = event->getIf<sf::Event::Resized>())
{
    const sf::Vector2f taille(resized->size);
    window.setView(sf::View(sf::FloatRect({0.f, 0.f}, taille)));
}
```

Sans cette ligne, agrandir la fenêtre **étire** le décor. Avec elle, on voit
simplement plus de monde.

Note:
`resized->size` est un `Vector2u` : la taille en pixels, pas un `width` et un
`height` séparés comme en SFML 2. Montrer les deux comportements en direct —
avec et sans `setView` — c'est l'exercice 1.

---

# Événement, ou état ?
<!-- .slide: class="title" -->

---

## Les deux questions ne sont pas les mêmes

- un **événement** dit « ça vient de changer » — il arrive **une fois**
- un **état** dit « c'est comme ça maintenant » — il se lit **à chaque image**

Confondre les deux donne les deux bugs classiques de la série : un personnage
qui hoquette, ou qui saute cent fois par seconde.

---

## Le saut, le déplacement

```cpp
// le saut : un événement, une fois
if (const auto* key = event->getIf<sf::Event::KeyPressed>())
    if (key->scancode == sf::Keyboard::Scancode::Space)
        heros.Sauter();

// le déplacement : un état, à chaque image
if (sf::Keyboard::isKeyPressed(sf::Keyboard::Scan::Left))
    heros.Deplacer(-1.f);
```

`KeyPressed` subit la **répétition clavier** du système ; `isKeyPressed` non.

Note:
Faire l'inverse en direct : déplacer sur `KeyPressed` donne le hoquet d'un
traitement de texte — une fois, un silence, puis la rafale. Sauter sur
`isKeyPressed` donne un saut par image tant que la touche est tenue.

---

# La manette
<!-- .slide: class="title" -->

---

## Elle n'est peut-être pas là

```cpp
if (!sf::Joystick::isConnected(0))
    return;                                  // le clavier reste seul maître

const float x = sf::Joystick::getAxisPosition(0, sf::Joystick::Axis::X);
if (std::abs(x) > 20.f)                      // zone morte, en pourcentage
    heros.Deplacer(x / 100.f);
```

La **zone morte** n'est pas une option : un stick au repos ne rend jamais zéro.

Note:
Les axes vont de −100 à 100, en flottant. Sans seuil, le personnage dérive
tout seul, et les étudiants cherchent le bug dans leur physique. La valeur de
20 est un point de départ, pas une vérité.

---

## Les boutons, par événement

```cpp
if (const auto* bouton = event->getIf<sf::Event::JoystickButtonPressed>())
    if (bouton->button == 0)
        heros.Sauter();
```

Même règle qu'au clavier : le saut est un **événement**, le déplacement un
**état**. Le support de la manette ne change que la source.

---

# Le son, en passant
<!-- .slide: class="title" -->

---

## Un bruit court, une musique

```cpp
sf::SoundBuffer tampon;                       // tout le fichier en mémoire
if (!tampon.loadFromFile("data/sounds/saut.wav")) return -1;
sf::Sound saut(tampon);                       // le tampon est obligatoire

sf::Music musique;                            // lue depuis le disque, en continu
if (!musique.openFromFile("data/sounds/level.ogg")) return -1;
musique.setLooping(true);
musique.play();
```

`loadFromFile` **charge**, `openFromFile` **ouvre** : tout est là.

Note:
C'est le code de la cible
[`Audio`](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/blob/main/Audio/src/main.cpp)
du dépôt d'exemples, qui est déjà en SFML 3.
Un buffer de musique de trois minutes, c'est une trentaine de mégaoctets en
mémoire — d'où `sf::Music`, qui ne garde qu'une fenêtre de lecture.

---

## Le même piège qu'au sprite

| Ce qui pointe | Ce qui doit survivre |
|---|---|
| `sf::Sprite` | sa `sf::Texture` |
| `sf::Sound` | son `sf::SoundBuffer` |

Un `SoundBuffer` local qui meurt à la fin de la fonction, et **le son ne sort
pas** — sans erreur, sans plantage.

Vous connaissez déjà ce bug : c'est le carré blanc de SBD-01.

---

## Atelier — 1 h

**Étape 2 du platformer.** La fenêtre écoute, le héros obéit.

1. `Closed` et `Resized` : la vue suit, le décor ne se déforme pas
2. le clavier, d'abord en `KeyPressed`, puis en `isKeyPressed` — et dire pourquoi
3. la manette : axes, bouton de saut, et un repli propre si elle est absente
4. un bruit de saut et une musique de fond, chacun dans **sa** classe — puis les
   inverser volontairement et mesurer la mémoire dans les deux cas

**On vérifie** : clavier et manette donnent le même déplacement, redimensionner
ne déforme rien, et le saut fait du bruit.

Note:
Démonstration, les événements :
[`Events-a`](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/blob/main/Events-a/Events-a.cpp) ·
[`Events-b`](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/blob/main/Events-b/Events-b.cpp) ·
[`Events-c`](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/blob/main/Events-c/Events-c.cpp) ·
[`Events-d`](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/blob/main/Events-d/Events-d.cpp).
Le son :
[`Audio`](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/blob/main/Audio/src/main.cpp)
et [`Sound`](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/blob/main/Sound/src/main.cpp).

`Events-a` est la plus parlante — elle change la couleur de fond quand la fenêtre
perd le focus, donc l'effet se voit sans rien lire.

---

## À retenir

- **un seul** `pollEvent` par image, tout en haut de la boucle
- événement pour ce qui **arrive**, état pour ce qui **dure**
- une manette absente est le cas **normal** : prévoyez le repli et la zone morte
- `Sound` pointe vers son `SoundBuffer`, comme `Sprite` vers sa `Texture`

---

# Questions ?
<!-- .slide: class="title" -->
