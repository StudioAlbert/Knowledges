---
title: GPR-CF-SBD-01 - Boucle de jeu et fenêtre
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

# Boucle de jeu et fenêtre
<!-- .slide: class="title" -->

### Étape 1 du platformer

<small>GPR-CF-SBD-01 · SFML et Box2D</small>

Note:
Première séance d'une série de six, et toutes construisent **le même projet**. Deck
court, parce que l'heure qui suit sert à l'écrire. Tout est en SFML 3 : les
exemples SFML 2 du web ne compilent pas.

---

## Objectifs

À la fin de la séance, vous savez :

- écrire une boucle de jeu **dans le bon ordre**
- traiter les événements SFML 3
- mesurer le temps entre deux images, et **s'en servir**
- dire pourquoi une vitesse s'exprime par seconde, jamais par image

---

## Un jeu est une boucle

```text
tant que la fenêtre est ouverte :
    lire les événements
    mettre à jour le monde      ← avec le temps écoulé
    effacer
    dessiner
    afficher
```

Inverser deux de ces lignes se voit tout de suite à l'écran.

---

## Deux mondes

- le **monde graphique** montre : des sprites, des pixels, une caméra
- le **monde physique** décide : des corps, des forces, des contacts

Ce sont **deux jeux de données** qu'il faudra relier — c'est le sujet de SBD-05.
Pour l'instant, on n'a que le premier.

---

## Ce qu'un moteur fait pour vous

Fenêtre, images, sons, entrées, temps : ce que personne n'a envie de réécrire.

- **SFML** fait tout ça, et s'arrête là
- il ne fait **pas** de physique, pas de scène, pas d'éditeur
- c'est ce qui le rend lisible : on voit encore sa propre boucle

Un moteur comme Unity fait la même chose, en cachant la boucle.

---

## SFML, module par module

| Module | Ce qu'il apporte |
|---|---|
| `System` | temps, vecteurs, threads — la base, toujours là |
| `Window` | la fenêtre et les entrées, sans rien dessiner |
| `Graphics` | sprites, textes, formes, vues |
| `Audio` | sons courts et musiques |
| `Network` | sockets — hors programme |

On n'en prend que ce dont on a besoin.

---

## Ouvrir une fenêtre

```cpp
#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode({800u, 600u}), "Platformer");
    window.setFramerateLimit(60);

    while (window.isOpen())
    {
        // ...
    }
}
```

En SFML 3, `sf::VideoMode` prend un **vecteur**, pas deux entiers.

---

## Les événements

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

`pollEvent` rend un `std::optional` : plus de `sf::Event e` déclaré à l'avance.

Note:
C'est **le** changement SFML 3 qui casse tous les exemples du web. `is<T>()` teste
le type, `getIf<T>()` rend un pointeur ou `nullptr`. Sans cette boucle, la fenêtre
ne se ferme pas — c'est l'exercice 1 de l'étape 1.

---

## La boucle, en entier

```cpp
sf::Clock clock;
while (window.isOpen())
{
    const float dt = clock.restart().asSeconds();

    while (const std::optional event = window.pollEvent())
        if (event->is<sf::Event::Closed>()) window.close();

    joueur.Update(dt);

    window.clear(sf::Color(30, 30, 40));
    window.draw(joueur);
    window.display();
}
```

Un seul `restart()` par image : le temps se mesure **une fois**.

---

## Limiter le framerate

- `setFramerateLimit(60)` — SFML attend pour vous
- `setVerticalSyncEnabled(true)` — l'écran décide
- **jamais les deux** : elles se battent, et le résultat saccade

Sans limite, la boucle tourne aussi vite qu'elle peut et fait chauffer la machine
pour rien.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/boucle_de_jeu_widget.html#frise" data-background-interactive -->

Note:
Premier onglet : monter le temps de calcul jusqu'à dépasser le budget, et montrer
que la limite ne sert plus à rien. Deuxième onglet, c'est la démonstration de la
séance — la lancer à 30 fps, puis à 144, sans rien changer d'autre.

---

## Le piège du déplacement par image

```cpp
position.x += 2.f;          // deux pixels par image
position.x += 120.f * dt;   // cent vingt pixels par seconde
```

La première ligne donne un jeu **deux fois plus rapide** sur une machine deux
fois plus rapide. La seconde donne le même jeu partout.

C'est la seule règle de la séance qui ne se discute jamais.

---

## Mise en œuvre — 1 h

**Étape 1 du platformer.** Une fenêtre, une boucle, un carré pilotable.

1. la fenêtre qui ne se ferme pas, puis la boucle d'événements
2. la couleur de fond qui varie, et ce qui arrive sans `clear`
3. le carré trop rapide, mesuré à 30 puis 144 images par seconde
4. plafonner, se synchroniser, afficher le framerate réel dans le titre

Énoncé : [[01 courses/exercises/C++/GPR-CF-SBD - Le platformer, etape par etape|Le platformer, étape par étape]].

---

## À retenir

- une boucle **dans le bon ordre** : événements, mise à jour, effacer, dessiner, afficher
- les événements se traitent, sinon la fenêtre ne répond pas
- le temps se mesure **une fois** par image
- toute vitesse s'exprime **par seconde** — jamais par image

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/C++/GPR-CF-SBD-02 - Afficher|GPR-CF-SBD-02]] — le héros à l'écran, étape 2 du même projet.</small>
