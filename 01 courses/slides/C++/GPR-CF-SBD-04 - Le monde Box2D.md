---
title: GPR-CF-SBD-04 - Le monde Box2D
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

# Le monde Box2D
<!-- .slide: class="title" -->

### Étape 4 du platformer

<small>GPR-CF-SBD-04 · SFML et Box2D</small>

Note:
Tout le code de cette séance est en **Box2D 3** : les pointeurs ont disparu, la
fixture aussi. Les exemples Box2D 2.4 du web ne compilent pas.
Une heure sans rien afficher, et c'est **délibéré** : séparer les deux mondes
avant de les relier est tout le propos de SBD-05. On observe par la console, et
on apprend à faire confiance à des nombres qu'on ne voit pas.

---

## Objectifs

À la fin de la séance, vous savez :

- créer un **monde** et le faire avancer à **pas fixe**
- choisir entre corps **statique**, **cinématique** et **dynamique**
- décrire une forme et sa **matière**
- travailler en **mètres**, et convertir une seule fois

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-03 - Déplacer et animer|GPR-CF-SBD-03]].

---

## Un monde parallèle

La physique calcule des positions. **Personne ne les voit** tant qu'on ne les
recopie pas vers les sprites — et c'est la séance suivante.

Pendant cette heure, votre jeu n'affiche rien de neuf, et pourtant il est déjà
juste.

---

## Le monde

```cpp
b2WorldDef def = b2DefaultWorldDef();
def.gravity = {0.f, -9.81f};          // vers le bas, en m/s²

b2WorldId monde = b2CreateWorld(&def);
```

Une gravité, une liste de corps, et une fonction qui fait avancer le temps.
C'est tout ce qu'un moteur physique est.

Note:
Box2D 3 ne rend plus de pointeurs mais des **identifiants** — `b2WorldId`,
`b2BodyId`, `b2ShapeId`. On les copie librement, et on n'en libère aucun à la
main : `b2DestroyWorld` emporte tout.

---

## Le pas de simulation

```cpp
constexpr float kPas = 1.f / 60.f;
constexpr int kSousPas = 4;

accumulateur_ += dt;
while (accumulateur_ >= kPas)
{
    b2World_Step(monde, kPas, kSousPas);
    accumulateur_ -= kPas;
}
```

Un pas **fixe** donne des résultats reproductibles. Un pas variable donne des
bugs impossibles à rejouer.

Note:
C'est exactement le `while` de l'animation en SBD-03, et pour la même raison :
quand une image dure longtemps, on rattrape plusieurs pas au lieu d'en faire un
énorme. Passer `dt` directement à `Step` est le bug le plus courant — le jeu
marche sur votre machine et traverse les murs sur celle d'à côté.

---

## Un corps

```cpp
b2BodyDef def = b2DefaultBodyDef();   // on part des valeurs par défaut
def.type = b2_dynamicBody;
def.position = {4.f, 10.f};           // en mètres

b2BodyId heros = b2CreateBody(monde, &def);
```

On décrit d'abord, le monde fabrique ensuite — et il rend un **identifiant**,
pas un pointeur. Rien à libérer.

Note:
Toujours partir de `b2DefaultBodyDef()`. Une structure laissée à zéro donne un
corps sans masse qui traverse tout, et l'erreur ne se voit qu'à l'exécution.

---

## Trois types de corps

| Type | Il bouge | On le pousse | Pour |
|---|---|---|---|
| `b2_staticBody` | non | non | le sol, les murs |
| `b2_kinematicBody` | oui, **vous** le bougez | non | la plateforme mobile |
| `b2_dynamicBody` | oui, la **physique** le bouge | oui | le héros, les caisses |

Une plateforme mobile en dynamique tombe. En statique, elle ne bouge pas.
**Cinématique** est la seule réponse.

---

## Une forme, et sa matière

```cpp
b2Polygon boite = b2MakeBox(0.4f, 0.9f);   // demi-largeur, demi-hauteur

b2ShapeDef forme = b2DefaultShapeDef();
forme.density = 1.f;                       // la masse en découle
forme.material.friction = 0.3f;
forme.material.restitution = 0.f;          // 0 : aucun rebond

b2CreatePolygonShape(heros, &forme, &boite);
```

`b2MakeBox` prend des **demi**-dimensions : un héros de 1,8 m, c'est `0.9f`.

Note:
Box2D 3 a supprimé la fixture : la forme et sa matière sont une seule structure,
attachée directement au corps. `friction` et `restitution` sont passées dans
`material`, parce qu'elles décrivent la surface, pas l'intérieur.

---

## Les unités
<!-- .slide: class="schema" -->

Box2D travaille en mètres et en kilogrammes : un personnage fait 1,8, pas 180.

![[sbd04_metres_pixels.svg]]

Note:
C'est le piège qui coûte le plus d'heures de la série, et il ne produit aucune
erreur. Box2D est réglé pour des objets de 0,1 à 10 mètres ; à 180, les forces
internes saturent et tout devient mou. Le facteur se décide **maintenant** et
s'écrit **une fois** — la classe de conversion, c'est SBD-05.

---

## Ce que le monde fait tout seul

- **intégrer** : appliquer les forces, avancer les positions
- **détecter** : trouver les paires de formes qui se touchent
- **résoudre** : séparer ce qui se chevauche, sans tout faire exploser

Trois problèmes difficiles que vous n'écrirez pas. C'est pour ça qu'on prend une
bibliothèque.

---

## Atelier — 1 h

**Étape 4 du platformer.** Rien à l'écran, et pourtant tout marche.

1. créer le monde, sa gravité, et le faire avancer à **pas fixe**
2. un sol **statique**, un héros **dynamique**
3. afficher la position du héros à chaque image, et le voir tomber puis s'arrêter
4. essayer les trois types sur une plateforme mobile, et dire lequel convient

**On vérifie** : le héros tombe, touche le sol et s'arrête — sans qu'aucun sprite
n'existe encore.

<small>Exemple : [01-Gravity](https://github.com/StudioAlbert/GPR-CF-SBD-XX---Box2D-Examples/tree/master/01-Gravity)</small>

Note:
`01-Gravity` est dans le **second** dépôt d'exemples, celui de Box2D. Une bille
dynamique qui tombe, et le clic la téléporte sous la souris : c'est l'atelier,
en quarante lignes.

Elle affiche sa position en console à chaque image — montrer que la physique
tourne avant qu'il n'y ait quoi que ce soit à l'écran.

---

## À retenir

- un pas **fixe**, rattrapé par un `while` — jamais `b2World_Step(monde, dt, …)`
- statique pour le décor, **cinématique** pour ce qu'on pilote, dynamique pour le reste
- `b2MakeBox` prend des **demi**-dimensions, en mètres
- Box2D 3 rend des **identifiants**, pas des pointeurs : rien à libérer

---

# Questions ?
<!-- .slide: class="title" -->
