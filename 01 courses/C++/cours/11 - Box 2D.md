---
title: Box2D
type: course
duration_h: 3
bloc: "[[Game Prog 101]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Box2D
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Le monde physique — corps, fixtures, contacts, platformer

<small>Sébastien Albert · Module 4FSC0PF001</small>

Note:
Dernière séance du module. On branche une simulation physique derrière
l'affichage SFML, et on va jusqu'aux cas concrets d'un platformer :
sauter uniquement au sol, wall jump, plateformes traversables par le bas.

---

## Source
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine (contient les extraits de code non transposés) :

- 🔗 [Google Slides — 11 Box 2D](https://docs.google.com/presentation/d/1WjpVxwYO2RImfP0aQ01sj5HMEUIAEMwjGJP-Slcmj-g/edit)

Séance précédente : [[10 - SFML]]

</div>

---

## Physical world
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Le monde physique ne fonctionne pas comme le monde graphique.

Et la physique n'a pas besoin de fonctionner comme la physique du monde réel : c'est une **simulation**, une frame physique après l'autre, de ce qui se passe.

- 📖 [Documentation Box2D](https://box2d.org/documentation/index.html)
- 📖 [Tutoriels (Drive)](https://drive.google.com/open?id=17zXbUKJhApoayzjVZ3du0TLsglVHP_I0)

---

# Les briques de Box2D
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## b2World
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Dans Box2D, vous avez littéralement un `b2World`, qui a besoin d'une **gravité** pour démarrer. Notez que l'on utilise `b2Vec2`, et non `sf::Vector2`.

Ce `b2World` est notre interface vers le monde physique :

- pour simuler une nouvelle frame physique, on appelle la méthode **`Step`**
- pour créer un nouveau corps physique, on demande au **world** d'en créer un

---

## b2Body + b2BodyDef
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Dans Box2D, un `b2Body` est un **rigidbody**. Voyez-le comme un point dans l'espace, représentant un objet physique qui peut bouger, et auquel on peut appliquer une `linearVelocity` et des forces.

Pour créer un `b2Body`, on demande au `b2World` d'en créer un, en lui donnant un `b2BodyDef` en argument.

---

## b2BodyDef
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Plusieurs membres intéressants dans `b2BodyDef` :

- **Damping** — réduit la vélocité ou l'angle d'une valeur constante par seconde
- **Type** — static, dynamic ou kinematic
- **UserData** — peut être renseigné par l'utilisateur de la bibliothèque (vous) et contenir n'importe quel pointeur

---

## b2Body — les types
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

| Type | Réagit à | Exemple typique |
|---|---|---|
| **Static** | rien — ni `linearVelocity`, ni forces, ni collisions | l'environnement |
| **Kinematic** | uniquement la `linearVelocity` — pas les forces ni les collisions | balles, ennemi de fond indestructible |
| **Dynamic** | tout : collisions, forces, etc. | le personnage joueur |

---

## b2Shape
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Un point dans l'espace, c'est bien, mais on veut des **formes** physiques. Celles supportées par Box2D :

- **b2PolygonShape** — les boîtes sont des polygones, on peut utiliser la méthode `.SetAsBox`
- **b2CircleShape**
- **b2EdgeShape** — un segment de droite

Pour un corps **static**, vous pouvez créer une fixture directement avec une shape.

---

## b2Fixture (le Collider d'Unity)
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Une shape, c'est bien, mais il nous faut plus d'infos pour gérer les contacts et les collisions :

- **Restitution** — la valeur utilisée pour le rebond (*bounciness*)
- **Density** — indispensable pour un corps dynamique !
- **isSensor** — quand on veut juste déclencher un contact, sans gérer une vraie collision physique
- **userData** — comme dans le `BodyDef` ; va être **très** important pour le résultat des contacts

---

## Créer un vrai corps dynamique
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Définir **un** `b2BodyDef`, **une** shape (ici un `b2PolygonShape` en boîte) et **une** `b2Fixture`.

---

# Relier physique et graphique
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Copier les valeurs du monde physique vers le monde graphique
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

On ne voit pas le monde physique tant qu'on n'a pas copié les positions et les rotations vers le monde graphique.

Comme on n'utilise pas les mêmes unités de mesure, il nous faut une façon de **convertir les mètres en pixels**.

---

## Déplacer notre personnage
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

On modifie la logique précédente : `input -> graphics` devient **`input -> physics -> graphics`**.

On peut déplacer le personnage :

- en réglant la `linearVelocity`
- ou en appliquant une force (`ApplyForceToCenter()`) à chaque frame

Typiquement, on met la **friction à 0.0** et **fixedRotation à true** sur le corps du personnage joueur.

---

## Contact Listener
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Pour pouvoir réagir aux contacts et collisions, il faut créer notre propre **contact listener**, qui sera appelé par le `b2World` s'il y a un contact — méthodes `BeginContact` / `EndContact`.

Un `b2Contact` contient les **deux fixtures** en contact (ou en collision). Depuis la fixture, on peut récupérer le `userData`.

---

## User Data
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

`void*` est un pointeur vers quelque chose. Le problème, en C++, c'est qu'on n'a aucun moyen de savoir ce qu'il y a derrière un `void*`.

Mais si on y met **notre propre type unique**, on sait avec certitude que ce sera soit `nullptr`, soit notre struct / classe.

Avec ce type unique, on peut savoir quel objet entre en collision avec quel autre — par exemple en ajoutant une `enum`.

---

# Un platformer, concrètement
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Platformer goals
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

On ne veut sauter **que** lorsqu'on est au sol. Il faut donc récupérer le contact avec le sol.

Plusieurs cas à résoudre :

1. ne pas sauter en l'air
2. toucher le sol par le côté
3. passer d'une plateforme à une autre
4. wall jump
5. traverser une plateforme par en dessous, mais pas par le dessus

---

## 1 — Ne pas sauter en l'air
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Utilisez une **fixture séparée pour le pied**, et incrémentez un compteur de contacts à chaque contact.

⚠ Si vous détruisez un corps alors qu'il est en contact, **`EndContact` ne sera pas appelé !**

---

## 2 — Toucher le sol par le côté
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Utiliser une fixture de pied séparée (`isSensor = true`) permet de distinguer le corps du personnage de son pied.

⚠ Si vous allez contre un mur avec de la friction, vous resterez **collé** contre lui tant que vous poussez dessus.

---

## 3 — Passer d'une plateforme à une autre
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Utiliser une fixture de pied séparée (`isSensor = true`) avec une valeur **entière** permet de passer d'une plateforme à l'autre tout en restant considéré comme au sol :

```
1 -> 2 -> 1     au lieu de     true -> true -> false
```

Note:
C'est tout l'intérêt du compteur plutôt que du booléen : pendant
l'enjambement, le pied touche brièvement les deux plateformes. Avec un
booléen, le `EndContact` de la première fait perdre le sol alors qu'on
est encore posé sur la seconde.

---

## 4 — Wall jump
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Comme pour la fixture de pied, vous pouvez ajouter des **fixtures latérales** pour savoir où vous touchez le mur.

Ajoutez une force vers le haut — un peu plus faible que la gravité, pour glisser lentement vers le bas — tant que vous êtes contre le mur.

Vous pouvez alors donner la possibilité de sauter, mais du **côté opposé** au mur.

---

## 5 — One way platform
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Celle-ci est particulièrement délicate.

Il faut **désactiver le contact** — pas le corps — entre le corps du personnage et la plateforme *one way*, mais **uniquement quand la vélocité du personnage est dirigée vers le haut** !

---

## Physical conclusion
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Vous avez maintenant une simulation physique complète ! Vous pouvez évidemment ajouter des comportements physiques plus complexes — on en verra certains sur Unity.

---

## Conclusion
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

On peut maintenant développer des jeux avec C++.

La 3D sera plus difficile à la main, et vous en apprendrez bien plus sur la création de jeux dans les semaines et modules qui viennent.

Et c'est BEAUCOUP plus facile dans un moteur de jeu :D

Mais il faut quand même apprendre à le faire *from scratch* :F
