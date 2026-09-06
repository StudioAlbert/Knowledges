---
title: SFML
type: course
status: Backlog
subject: C++
duration_h: 3
bloc: "[[Game Prog 101]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# SFML
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Sortir de la console — fenêtre, sprites, sons

<small>Module 4FSC0PF001 · Introduction to Games Programming</small>

Note:
Première séance où le jeu quitte le terminal. On ouvre une fenêtre, on
met en place une game loop, on affiche et on déplace un sprite, puis on
ajoute du son. La physique arrive à la séance suivante avec Box2D.

---

## Source
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine (contient les extraits de code et captures non transposés) :

- 🔗 [Google Slides — 10 SFML](https://docs.google.com/presentation/d/1IFFIopIjzAz-iy2_iQp-1pxJNNpdivqmUn3hlo5bm1M/edit)

Exercices : [[Exercices - 10 - SFML]] · Suite : [[11 - Box 2D]]

</div>

---

## Games Programming
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

L'interface console, c'est bien, mais un jeu c'est beaucoup plus :

- graphics
- audio
- basic AI
- scripting
- tool
- gameplay
- physics
- network

---

## Graphical world vs physical world
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Les deux mondes sont clairement séparés dans un jeu !

| Monde | Distance | Temps |
|---|---|---|
| **Graphique** | pixel | frame |
| **Physique** | mètre | seconde |

Exemple avec Super Mario 64 : [vidéo](https://youtu.be/kpk2tdsPh0A?t=626)

---

## Game Engine
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Si vous voulez créer un jeu, le faire *from scratch* est un travail difficile. La plupart des débutants commencent dans un moteur (Unity, Unreal, Godot, Game Maker, …).

Mais vous n'êtes pas n'importe quels débutants, et vous aurez tout le temps de jouer avec Unreal et Unity. Alors commençons **presque** de zéro !

---

## SFML — les sous-systèmes
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

API open source gratuite, divisée en plusieurs sous-systèmes :

- **SFML Graphics** — drawing sprites and shapes
- **SFML Window** — opening a window and managing inputs
- **SFML System** — working with the OS, threads, time, clock and files (utile avant C++11)
- **SFML Audio** — playing sound and music
- **SFML Network** — sending packets over the Internet

<small>Tutoriels : [sfml-dev.org/tutorials/2.5](https://www.sfml-dev.org/tutorials/2.5/index-fr.php)</small>

---

## SFML — ce que ça vaut
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- API facile à comprendre, très orientée objet
- utilise l'**ancien OpenGL** pour le rendu ; peu utilisée dans les « vrais » jeux (on utilise plutôt SDL, une autre API, plus bas niveau) et pas utilisée sur console
- excellent outil pour apprendre l'abstraction ; pas le meilleur outil pour faire un vrai jeu, mais bon pour des petits jeux simples

---

# La boucle de jeu
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Game Loop
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Pour que nos jeux tournent en continu, il nous faut une **game loop** qui tourne jusqu'à ce qu'on quitte le jeu.

Mais d'abord, il nous faut une fenêtre dans laquelle boucler.

<small>[Vidéo de référence](https://www.youtube.com/watch?v=H4N8xYue_3Q)</small>

---

## sf::RenderWindow
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Cette fenêtre nous permet de gérer les inputs, les événements, et de dessiner dedans.

Pour créer une fenêtre, il faut la résolution et un nom de fenêtre (d'autres flags existent : fullscreen, resizable…).

```cpp
sf::RenderWindow window(sf::VideoMode(800, 600), "My Game");

while (window.isOpen())
{
    sf::Event event;
    while (window.pollEvent(event))
    {
        if (event.type == sf::Event::Closed)
            window.close();
    }

    window.clear();
    // toutes les draw calls vont ici
    window.display();
}
```

**Toutes les draw calls doivent être entre `clear` et `display` !**

---

## Events
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Liste non exhaustive des événements SFML :

- `Closed` — quand quelqu'un fait alt-F4 ou ferme la fenêtre
- `Resized` — quand la fenêtre est redimensionnée
- `LostFocus` / `GainFocus`
- `KeyPressed` / `KeyReleased`
- `MouseWheelScrolled`
- `MouseButtonPressed` / `MouseButtonReleased`
- `MouseMoved`

---

## Limiting framerate
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- vous pouvez faire tourner votre jeu à 1200 fps, mais vous restez graphiquement limité par la fréquence de rafraîchissement de l'écran (60 Hz, 120 Hz, 144 Hz…)
- limiter le framerate laisse respirer l'OS, et sur mobile ou portable, ça ne vide pas la batterie
- **FRAPS** est un logiciel connu pour mesurer les FPS de votre programme
- dans SFML, vous pouvez vous synchroniser à la **Vertical Sync**, ou limiter le framerate comme vous voulez

---

# Afficher
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## sf::Texture
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

On charge une Texture depuis le disque (formats supportés typiques : PNG, JPG, BMP, etc.).

Pour faciliter le chargement des données, le `CMakeLists` de Platformer920 copie les assets dans le dossier `Build/`, de sorte que vous pouvez simplement utiliser `"data/"` au lieu de `"../data/"`.

Charger une Texture est **lent**, mais pratique. Comment la met-on dans la fenêtre ?

---

## Draw a Sprite
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

SFML utilise la classe `sf::Sprite` pour définir le dessin d'une `sf::Texture` dans la fenêtre.

- n'oubliez pas de dessiner **entre** l'appel `clear` et l'appel `display`
- vous obtiendrez un **rectangle blanc** si vous détruisez la Texture avant de dessiner !
- ne chargez pas deux fois la même Texture si deux `sf::Sprite` l'utilisent !

Note:
Le rectangle blanc est l'erreur numéro un des étudiants sur cette
séance : le sprite ne possède pas sa texture, il la référence. Si la
texture est locale et sort de scope, le sprite pointe dans le vide.

---

## Positioning
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- la position `(0, 0)` de la fenêtre SFML est en **haut à gauche** ; `(width, height)` est en bas à droite. **Y plus grand = plus bas** ;)
- par défaut, toutes les positions sont en **pixels**
- l'origine d'un sprite est par défaut en haut à gauche : il faudra mettre à jour l'origine du sprite pour l'avoir au centre de l'image

---

## Moving a sprite with keyboard
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

D'abord récupérer les inputs clavier, puis changer la position du Sprite.

Deux façons de récupérer le clavier :

1. écouter les **événements**, et basculer un booléen sur *key down* / *key up*
2. lire directement la valeur à chaque update, et l'utiliser

---

## Camera
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

`sf::View` (centre + taille) représente un rectangle que l'on donne à la caméra, pour pouvoir se déplacer **sans déplacer tous les sprites** ! Déplacer la caméra revient à déplacer le centre de la `sf::View`.

Par défaut, la fenêtre a la `sf::View` de sa résolution d'origine, mais on peut la changer avec `.setView(myView)`.

On verra ce qu'il y a réellement dans une `sf::View` en GPR5300 (spoiler : c'est une matrice !).

---

## Managing resize like a boss
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Quand on redimensionne une fenêtre, la vue va comprimer ou étirer les sprites à l'écran.

Correctif simple : mettre à jour la vue de la fenêtre avec la nouvelle taille.

---

## Framebuffer
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Parfois, on veut d'abord rendre dans une Texture séparée avant de la dessiner à l'écran — pensez à la **minimap** d'un RPG.

C'est là qu'un **framebuffer** est utile ; dans SFML, on l'appelle `sf::RenderTexture`.

Au redimensionnement de l'écran, vous voudrez sans doute redimensionner les framebuffers également.

---

## Animation
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Il y a une classe `sf::Animation` dans SFML… en fait non, il n'y a **pas** d'animation dans SFML. Mais qu'est-ce qu'une animation ? Plusieurs images échangées à une fréquence donnée !

Par exemple : vous créez un fichier JSON décrivant une animation avec les keyframes où les textures changent. Vous chargez toutes les textures dans l'`Init`, puis vous utilisez un timer pour savoir quand basculer sur la nouvelle texture du sprite — et voilà !

---

# Le son
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Playing a sound
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

SFML supporte la musique et les sons en **WAV, FLAC et OGG** — pas le MP3 !

SFML utilise en interne un thread séparé pour jouer l'audio : vous n'avez qu'à dire à SFML quand jouer ou arrêter un son, il s'occupe du reste automatiquement.

---

## sf::Sound
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Comme Texture + Sprite : il faut charger un `sf::SoundBuffer` (le contenu du son), le donner à un `sf::Sound`, pour enfin pouvoir appeler `play()`.

---

## sf::Music
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

La musique peut être un gros fichier : au lieu de la charger d'un coup à l'`Init`, `sf::Music` **stream** le fichier depuis le disque pendant la lecture — pas besoin de SoundBuffer.

---

## Graphical world — conclusion
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

C'est à peu près tout pour SFML ! Vous pouvez maintenant afficher votre jeu à l'écran et le faire bouger un peu.

Évidemment, pour un platformer, il manque encore des parties importantes…

---

## Pause
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Question time !

Vous pouvez aussi jouer avec VS2019 — ou faire une pause, au cas où votre cerveau serait en train de fondre…
