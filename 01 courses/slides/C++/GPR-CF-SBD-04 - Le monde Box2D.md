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
b2Vec2 gravite(0.f, -9.81f);     // vers le bas, en mètres par seconde carrée
b2World monde(gravite);
```

Une gravité, une liste de corps, et une méthode qui fait avancer le temps.
C'est tout ce qu'un moteur physique est.

---

## Le pas de simulation

```cpp
constexpr float kPas = 1.f / 60.f;

accumulateur_ += dt;
while (accumulateur_ >= kPas)
{
    monde.Step(kPas, 8, 3);      // vélocité, position
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
b2BodyDef def;                      // on décrit ce qu'on veut
def.type = b2_dynamicBody;
def.position.Set(4.f, 10.f);        // en mètres

b2Body* heros = monde.CreateBody(&def);   // le monde le fabrique
```

On décrit d'abord, le monde fabrique ensuite — et **c'est lui qui possède** le
corps. On ne fait jamais `delete` sur un `b2Body*`.

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
b2PolygonShape boite;
boite.SetAsBox(0.4f, 0.9f);        // demi-largeur, demi-hauteur, en mètres

b2FixtureDef matiere;
matiere.shape = &boite;
matiere.density = 1.f;             // la masse en découle
matiere.friction = 0.3f;
matiere.restitution = 0.f;         // 0 : aucun rebond

heros->CreateFixture(&matiere);
```

`SetAsBox` prend des **demi**-dimensions : un héros de 1,8 m, c'est `0.9f`.

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

Note:
**Aucune cible du dépôt d'exemples ne fait de Box2D** : c'est la seule séance de
la série sans démonstration prête. On écrit donc le monde ensemble, au tableau
puis à l'écran, et la console sert de preuve.

---

## À retenir

- un pas **fixe**, rattrapé par un `while` — jamais `Step(dt, …)`
- statique pour le décor, **cinématique** pour ce qu'on pilote, dynamique pour le reste
- `SetAsBox` prend des **demi**-dimensions, en mètres
- le monde possède ses corps : aucun `delete` de votre côté

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/C++/GPR-CF-SBD-05 - Relier physique et graphique|GPR-CF-SBD-05]] — on rebranche l'image sur la physique.</small>
