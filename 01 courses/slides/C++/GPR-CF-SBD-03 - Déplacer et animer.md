---
title: GPR-CF-SBD-03 - Déplacer et animer
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

# Déplacer et animer
<!-- .slide: class="title" -->

### Étape 3 du platformer

<small>GPR-CF-SBD-03 · SFML et Box2D</small>

Note:
Une seule question, et elle commande tout le reste de la série : **comment on
gère le temps**. Le déplacement et l'animation en sont les deux usages, et le
`dt` qu'on mesure ici nourrira la physique de SBD-04.

---

## Objectifs

À la fin de la séance, vous savez :

- mesurer le temps écoulé entre deux images, **une seule fois**
- dire pourquoi une vitesse s'exprime par **seconde**, jamais par image
- choisir entre limiter le framerate et se synchroniser à l'écran
- découper une planche et faire défiler les poses à **cadence fixe**

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-02 - Gameplay et événements|GPR-CF-SBD-02]].

---

# Le temps
<!-- .slide: class="title" -->

---

## Mesurer, une fois par image

```cpp
sf::Clock horloge;

while (window.isOpen())
{
    const float dt = horloge.restart().asSeconds();   // une seule fois

    TraiterEvenements(window);
    joueur.Update(dt);

    window.clear();
    window.draw(joueur);
    window.display();
}
```

`restart()` rend le temps écoulé **et** remet le compteur à zéro.

Note:
Un seul `restart()` par tour. Deux appels dans deux fonctions différentes, et la
seconde reçoit un `dt` presque nul — le personnage avance par à-coups et
personne ne comprend pourquoi. `getElapsedTime()` lit sans remettre à zéro :
c'est ce qu'il faut pour un chrono, pas pour une boucle.

---

## Le piège du déplacement par image

```cpp
position.x += 2.f;          // deux pixels par image
position.x += 120.f * dt;   // cent vingt pixels par seconde
```

La première ligne donne un jeu **deux fois plus rapide** sur une machine deux
fois plus rapide. La seconde donne le même jeu partout.

C'est la seule règle de la série qui ne se discute jamais.

Note:
Le faire mesurer, pas l'affirmer : le carré traverse l'écran, on note le temps à
30 images par seconde, puis à 144. C'est l'exercice 2, et le widget de la slide
suivante le montre côte à côte.

---

## Limiter, ou se synchroniser

- `setFramerateLimit(60)` — SFML attend pour vous
- `setVerticalSyncEnabled(true)` — l'écran décide
- **jamais les deux** : elles se battent, et le résultat saccade

Sans limite, la boucle tourne aussi vite qu'elle peut et fait chauffer la
machine pour rien.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/boucle_de_jeu_widget.html#course" data-background-interactive -->

Note:
Onglet *course* : deux carrés, l'un déplacé par image, l'autre par seconde, à
30, 60 ou 144 fps. **C'est la démonstration de la séance** — à 144 fps le rouge
est à l'arrivée quand le vert est au tiers. Passer ensuite à l'onglet *frise* :
monter le temps de calcul jusqu'à dépasser le budget, et montrer que la limite
ne sert plus à rien.

---

# Animer
<!-- .slide: class="title" -->

---

## Une planche, des cases

```cpp
sf::Texture planche("data/sprites/hero-run.png");
sf::Sprite hero(planche);

constexpr sf::Vector2i kCase{64, 64};
hero.setTextureRect(sf::IntRect({0, 0}, kCase));        // la pose 0
hero.setTextureRect(sf::IntRect({64, 0}, kCase));       // la pose 1
```

Une **sprite sheet** est une seule texture qui contient toutes les poses. On
n'en montre qu'un rectangle à la fois.

Note:
Une seule texture pour seize poses, c'est un seul chargement et un seul envoi à
la carte graphique. L'alternative — un PNG par pose, comme la cible
`AnimationClass` du dépôt d'exemples — est plus simple à écrire et plus lente à
tout : seize fichiers, seize textures, seize allers-retours.

---

## Faire défiler, à cadence fixe

```cpp
constexpr float kPeriode = 1.f / 12.f;    // douze poses par seconde

temps_ += dt;
while (temps_ >= kPeriode)
{
    temps_ -= kPeriode;
    pose_ = (pose_ + 1) % kNbPoses;
}
hero.setTextureRect(sf::IntRect({pose_ * kCase.x, 0}, kCase));
```

Un `while`, pas un `if` : si une image a duré longtemps, on rattrape **toutes**
les poses sautées.

Note:
Le `if` marche tant que le jeu tourne bien, et casse exactement quand il rame —
donc au pire moment. Le `while` est la même ligne, et il est juste dans les deux
cas. C'est le même raisonnement que le pas fixe de la physique, en SBD-04.

---

## Ce que l'animation ne doit pas faire

- dépendre du **framerate** : douze poses par seconde, à 30 comme à 144
- se recalculer **deux fois** par image
- repartir de la pose 0 à chaque changement d'état

Une animation qui redémarre à chaque image reste bloquée sur sa première pose —
et ça se voit comme un personnage figé.

---

## Changer d'animation

```cpp
if (!auSol)            jeu_.Jouer(Anim::Saut);
else if (vitesse != 0) jeu_.Jouer(Anim::Course);
else                   jeu_.Jouer(Anim::Repos);
```

`Jouer` ne fait **rien** si l'animation demandée est déjà en cours. C'est cette
ligne qui évite le personnage figé.

Note:
Trois états, trois animations, et la décision prise à un seul endroit. Ceux qui
ont fait le pattern `State` en PCL-03 reconnaîtront : ici un `if` suffit, parce
qu'il y a trois cas et qu'ils ne se combinent pas.

---

## Mise en œuvre — 1 h

**Étape 3 du platformer.** Le héros bouge, et il bouge pareil partout.

1. mesurer le `dt` **une fois** par tour de boucle
2. le carré trop rapide, mesuré à 30 puis à 144 images par seconde, puis corrigé
3. plafonner, se synchroniser, et afficher le framerate réel dans le titre
4. découper la planche et faire défiler les poses à cadence fixe

Énoncé : [[01 courses/exercises/C++/GPR-CF-SBD - Le platformer, etape par etape|Le platformer, étape par étape]].

---

## À retenir

- un seul `restart()` par image — le temps se mesure **une fois**
- toute vitesse s'exprime **par seconde**, jamais par image
- limiter **ou** se synchroniser, jamais les deux
- une animation avance avec le `dt`, et un `while` rattrape ce qui a été sauté

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/C++/GPR-CF-SBD-04 - Le monde Box2D|GPR-CF-SBD-04]] — une heure sans rien afficher, et c'est voulu.</small>
