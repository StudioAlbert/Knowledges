---
title: GPR-CF-SBD-01 - Afficher la fenêtre et les sprites
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

# Afficher la fenêtre et les sprites
<!-- .slide: class="title" -->

### Étape 1 du platformer

<small>GPR-CF-SBD-01 · SFML et Box2D</small>

Note:
Première séance d'une série de six, et toutes construisent **le même projet**.
Deck court, parce que l'heure qui suit sert à l'écrire. Tout est en SFML 3 : les
exemples SFML 2 du web ne compilent pas, et la moitié de notre propre dépôt
d'exemples non plus.

---

## Objectifs

À la fin de la séance, vous savez :

- ouvrir une **fenêtre** et la fermer proprement
- écrire la boucle `effacer / dessiner / afficher` **dans cet ordre**
- charger une **texture** et en montrer un **sprite**
- dire pourquoi un sprite devient blanc

---

# Une fenêtre
<!-- .slide: class="title" -->

---

## Le programme minimal

```cpp
#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode({800, 600}), "The Game");
    window.setFramerateLimit(60);

    while (window.isOpen())
    {
        window.clear(sf::Color::Black);
        window.display();
    }
}
```

Six lignes, et une fenêtre noire qui ne répond pas encore. C'est
`HelloWorld` du dépôt d'exemples.

Note:
Le lancer tel quel, et laisser quelqu'un essayer de la fermer. Elle ne se ferme
pas : c'est la slide suivante. En SFML 3, `sf::VideoMode` prend **un vecteur**,
pas deux entiers — c'est la première ligne qui casse quand on copie un exemple
du web.

---

## Ce que `RenderWindow` est vraiment

- une **fenêtre** du système, avec sa barre de titre et sa croix
- une **cible de dessin** : tout ce qu'on affiche passe par elle
- une **source d'événements** : clavier, souris, redimensionnement

Trois rôles dans un seul objet. C'est la seule concession de SFML à la
simplicité, et elle est assumée.

---

## La boucle, dans le bon ordre

```cpp
while (window.isOpen())
{
    // 1. lire les événements
    // 2. mettre à jour le monde
    window.clear(sf::Color(30, 30, 40));   // 3. effacer
    window.draw(heros);                    // 4. dessiner
    window.display();                      // 5. afficher
}
```

Inverser deux de ces lignes se voit **tout de suite** à l'écran.

Note:
Retirer `clear` et montrer la traînée : c'est l'exercice 2. Mettre `display`
avant `draw` et montrer l'écran vide. L'ordre n'est pas une convention de style,
c'est la seule séquence qui produit une image juste.

---

## Les événements, en SFML 3

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

`pollEvent` rend un `std::optional` : plus de `sf::Event` déclaré à l'avance.

Note:
**Le** changement SFML 3 qui casse tous les exemples du web, et quatorze des
dix-huit cibles de notre dépôt. `is<T>()` teste le type, `getIf<T>()` rend un
pointeur ou `nullptr`. Sans cette boucle, la fenêtre ne se ferme pas.

---

# Dessiner
<!-- .slide: class="title" -->

---

## Une forme, pour commencer

```cpp
sf::RectangleShape sol({800.f, 40.f});
sol.setFillColor(sf::Color(90, 90, 110));
sol.setPosition({0.f, 560.f});

window.draw(sol);
```

Avant le premier sprite, les formes suffisent : un sol, une plateforme, une
boîte de collision qu'on veut voir.

Note:
En SFML 3, `setPosition` prend **un vecteur**. C'est le deuxième piège de
migration, après `VideoMode`. Les formes servent longtemps : tout le travail de
Box2D en SBD-04 se débogue avec des rectangles.

---

## Texture et sprite

```cpp
sf::Texture texture;
if (!texture.loadFromFile("data/sprites/hero.png"))
    return -1;                       // le fichier n'est pas là : on le dit

sf::Sprite hero(texture);            // la texture est obligatoire
hero.setPosition({100.f, 420.f});

window.draw(hero);
```

La **texture** est l'image en mémoire, le **sprite** est ce qu'on en montre.

Note:
En SFML 3, `sf::Sprite` n'a plus de constructeur sans texture : `sf::Sprite s;
s.setTexture(t);` ne compile pas. C'est le troisième piège de migration, et il
touche cinq cibles du dépôt d'exemples.

---

## Le piège : la texture morte

```cpp
sf::Sprite ChargerHero()          // NE FAITES PAS ÇA
{
    sf::Texture texture;          // elle meurt à la fin de la fonction
    texture.loadFromFile("hero.png");
    return sf::Sprite(texture);   // le sprite pointe vers du vide
}
```

Un sprite **ne copie pas** sa texture, il garde un pointeur dessus. Une texture
qui meurt avant lui donne un **carré blanc**.

Note:
C'est le bug numéro un de la séance, et il ne produit ni erreur de compilation
ni plantage — juste un rectangle blanc. La règle à retenir : les textures vivent
aussi longtemps que le jeu, et se chargent une fois.

---

## Un morceau de planche

```cpp
sf::Sprite hero(planche);
hero.setTextureRect(sf::IntRect({0, 0}, {64, 64}));   // la première case
```

Une **sprite sheet** est une seule texture qui contient toutes les poses. On
n'en montre qu'un rectangle à la fois.

Faire défiler ces rectangles, c'est l'animation — et c'est
[[01 courses/slides/C++/GPR-CF-SBD-03 - Déplacer et animer|SBD-03]].

---

## Mise en œuvre — 1 h

**Étape 1 du platformer.** Une fenêtre, un décor, un héros immobile.

1. la fenêtre qui ne se ferme pas, puis la boucle d'événements
2. la couleur de fond qui varie, et ce qui arrive **sans** `clear`
3. un sol et deux plateformes en `RectangleShape`
4. le héros chargé depuis un PNG, posé sur le sol — et le carré blanc provoqué
   **exprès**, puis corrigé

Énoncé : [[01 courses/exercises/C++/GPR-CF-SBD - Le platformer, etape par etape|Le platformer, étape par étape]].

---

## À retenir

- `sf::VideoMode({w, h})`, `setPosition({x, y})` : en SFML 3, **des vecteurs**
- la boucle : événements, mise à jour, **effacer**, dessiner, afficher
- une texture se charge **une fois** et survit à ses sprites
- un sprite blanc, c'est une texture morte — jamais autre chose

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/C++/GPR-CF-SBD-02 - Gameplay et événements|GPR-CF-SBD-02]] — le clavier, la manette, et la fenêtre qu'on redimensionne.</small>
