---
title: GPR-CF-SBD-05 - Relier physique et graphique
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

# Relier physique et graphique
<!-- .slide: class="title" -->

### Étape 5 du platformer

<small>GPR-CF-SBD-05 · SFML et Box2D</small>

Note:
Les deux mondes existent depuis SBD-04 et ne se parlent pas. Cette séance pose
le pont — dans **un seul sens** — et apprend à écouter les contacts. C'est la
séance la plus courte à écrire et la plus facile à rater.

---

## Objectifs

À la fin de la séance, vous savez :

- écrire **une** classe de conversion, et ne convertir nulle part ailleurs
- recopier une position physique vers un sprite, **dans le bon sens**
- écouter les contacts et savoir **qui** a touché quoi
- dire pourquoi « au sol » n'est pas un contact

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-04 - Le monde Box2D|GPR-CF-SBD-04]].

---

## Le pont

Box2D sait où sont les choses. SFML sait les dessiner. **Rien** ne les relie
tant que vous n'écrivez pas le pont.

Ce pont tient en trois gestes : convertir l'unité, convertir l'axe, recopier.
Les trois se trompent facilement, et aucun ne produit d'erreur.

---

## Une seule classe sait convertir

```cpp
// conversion.h — le seul endroit du projet qui connaît le facteur
namespace monde {

inline constexpr float kPixelsParMetre = 32.f;

constexpr float Metres(float pixels) { return pixels / kPixelsParMetre; }
constexpr float Pixels(float metres) { return metres * kPixelsParMetre; }

}  // namespace monde
```

Si `32` apparaît ailleurs dans votre code, vous avez déjà le bug : le jour où
il devient `48`, il n'en changera qu'un sur deux.

---

## Les deux axes Y s'opposent

```cpp
// Box2D : Y monte.  SFML : Y descend.
sf::Vector2f VersEcran(b2Vec2 p, float hauteurEcran)
{
    return { Pixels(p.x), hauteurEcran - Pixels(p.y) };
}
```

Un héros qui tombe **vers le haut** de l'écran, c'est ce signe-là. Rangez la
conversion d'axe avec celle d'unité : même fichier, même geste.

---

## Dans le bon sens, et un seul

```cpp
const b2Vec2 p = corps_->GetPosition();
sprite_.setPosition(monde::VersEcran(p, kHauteurEcran));
```

La copie va **du physique vers le graphique**. Jamais l'inverse.

Déplacer un sprite à la main pendant que Box2D simule donne deux vérités qui
divergent, et un personnage qui tremble.

---

## Les angles

```cpp
sprite_.setRotation(sf::radians(corps_->GetAngle()));
```

Box2D compte en **radians**, SFML en **degrés** — et dans le sens opposé, pour
la même raison que l'axe Y.

Note:
`sf::radians` et `sf::degrees` existent depuis SFML 3 : `sf::Angle` est un type,
plus un `float` ambigu. C'est un des rares endroits où SFML 3 rend le code plus
sûr, pas seulement différent.

---

## Trois façons de faire bouger un corps

| Geste | Ce qu'il fait | Quand |
|---|---|---|
| `SetTransform` | **téléporte**, sans physique | respawn, téléporteur |
| `ApplyForce` | pousse progressivement | vent, aimant, tapis roulant |
| `SetLinearVelocity` | impose la vitesse **tout de suite** | marcher, sauter |

Un platformer utilise surtout le troisième : on veut un contrôle **immédiat**,
pas une voiture qui glisse.

---

# Les contacts
<!-- .slide: class="title" -->

---

## Écouter

```cpp
class Ecouteur : public b2ContactListener
{
public:
    void BeginContact(b2Contact* contact) override { /* ils se touchent */ }
    void EndContact(b2Contact* contact) override   { /* ils se séparent */ }
};

Ecouteur ecouteur;
monde.SetContactListener(&ecouteur);
```

Box2D vous **appelle** pendant `Step`. Ne créez et ne détruisez rien dedans :
le monde est en train de travailler.

---

## Qui a touché qui

```cpp
void BeginContact(b2Contact* contact) override
{
    auto* a = reinterpret_cast<Objet*>(
        contact->GetFixtureA()->GetBody()->GetUserData().pointer);
    auto* b = reinterpret_cast<Objet*>(
        contact->GetFixtureB()->GetBody()->GetUserData().pointer);

    if (a && b) a->Touche(*b), b->Touche(*a);
}
```

`UserData` est le fil qui ramène du corps physique à **votre** objet de jeu.
Sans lui, vous savez que ça s'est touché, pas ce qui s'est touché.

---

## « Au sol » n'est pas un contact

Un contact dit « ces deux formes se touchent ». Il ne dit pas **où**.

- toucher un mur par le côté, ce n'est **pas** être au sol
- un seul pied sur l'arête, c'est quand même être au sol
- `EndContact` arrive aussi quand l'objet touché est détruit

D'où un **capteur** sous les pieds, en SBD-06 — pas un simple booléen de contact.

Note:
C'est la slide qui prépare toute la séance suivante. Faire le test en direct :
coller le héros contre un mur, constater que `BeginContact` part, et qu'avec un
booléen naïf il peut sauter en l'air indéfiniment.

---

## Atelier — 1 h

**Étape 5 du platformer.** Les deux mondes se rejoignent.

1. la **classe de conversion**, et la seule constante du projet
2. recopier position et angle vers le sprite, à chaque image, dans un seul sens
3. brancher le `ContactListener`, puis `UserData` pour savoir **qui** a touché quoi
4. en déduire un booléen `au sol`, et reprendre votre schéma de conception pour
   dire ce que la physique a imposé

**On vérifie** : le sprite suit exactement le corps, et `au sol` est vrai posé,
faux en l'air.

Note:
Démonstration : `Views` pour la caméra et le passage écran / monde, `Motor` pour
un projet complet où chaque entité tient son propre couple données / sprite.
`Motor` est le seul du dépôt à ressembler à un vrai jeu — le lire pour voir où
la conversion est rangée.

---

## À retenir

- **une** classe sait convertir, et le facteur n'existe nulle part ailleurs
- Y monte chez Box2D, descend chez SFML — rangez les deux conversions ensemble
- la copie va du physique vers le graphique, **jamais** l'inverse
- un contact n'est pas une position : « au sol » demande un capteur

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/C++/GPR-CF-SBD-06 - Les ficelles d'un platformer|GPR-CF-SBD-06]] — tout ce qui rend un saut agréable, et qui ne se déduit d'aucune équation.</small>
