---
title: TC-FT-PCL-01 - Couplage et cohésion
type: slides
subject: Theory
duration_h: 1
bloc_gsda: Principes de Conception Logicielle
specialisation: Fondamentaux Théoriques
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
---

# Couplage et cohésion
<!-- .slide: class="title" -->

### Deux mots pour dire pourquoi un projet devient lourd

<small>TC-FT-PCL-01 · Principes de Conception Logicielle</small>

Note:
Première séance du bloc. Tout ce qui suit — SOLID, les patterns, composition
contre héritage — n'est que l'application de ces deux mots. Les exemples
viennent de deux projets réels de l'école, pas d'un cas d'école.

---

## Objectifs

À la fin de la séance, vous savez :

- dire ce qu'est une **dépendance**, et dans quel sens elle doit aller
- mesurer le **couplage** d'une classe, et sa **cohésion**
- répondre à « qu'est-ce que je dois **retester** »
- reconnaître les **symptômes** d'une dette de conception

---

# Le script qui grossit
<!-- .slide: class="title" -->

---

## Le script de deux mille lignes

Tout le monde en a écrit un : il marche, et plus personne n'ose y toucher.

- il a commencé à cent lignes, et chaque ajout était « juste une de plus »
- aujourd'hui, trois personnes ne peuvent plus y travailler en même temps
- le modifier demande de relire **tout** le fichier

Il n'est pas devenu mauvais d'un coup. Il n'a jamais été découpé.

---

## Un cas réel

```cpp
// 925 - SpaceShooter / starship_player.hpp
class StarshipPlayer : public sf::Drawable
{
    sf::Texture ship_texture_;      sf::RectangleShape ship_rect_;
    sf::Texture shield_texture_;    bool shield_on_;
    int shield_texture_idx_;        float shield_counter_;
    Motor motor_;
    Weapons::ProjectileManager projectile_manager_;
    float shoot_counter_, shoot_rate_;

    void Load(...);  void Update(const sf::RenderWindow&, float);
    bool CheckCollisions(...);      void HandleEvent();
    void draw(...) const override;
};
```

Note:
Projet `SAE-Geneve/925-4FSC0PF001-SpaceShooter`. Ne pas en faire un procès : il
marche, il a été livré, et c'est exactement le code qu'on écrit tous. Le propos
est de le **lire** avec les deux mots de la séance.

---

## Compter ses raisons de changer

`StarshipPlayer` change si on modifie :

- l'apparence du vaisseau, ou **celle du bouclier**
- la durée du bouclier, ou sa **séquence d'animation**
- la cadence de tir, ou les **projectiles**
- les **collisions**, le **déplacement**, les **entrées clavier**, l'**affichage**

Huit raisons, un seul fichier. C'est la définition d'un problème de **cohésion**.

---

# Dépendance
<!-- .slide: class="title" -->

---

## La seule définition qui compte

> **A dépend de B** si changer B peut casser A.

Pas « A importe B ». Pas « A est dans le même dossier ». La question est
toujours : *qu'est-ce qui casse si je touche ça ?*

```cpp
void Update(const sf::RenderWindow&, float);
```

Le joueur a besoin de la **fenêtre** pour avancer d'une image. Il dépend donc de
tout le système d'affichage, pour connaître deux bords d'écran.

---

## La direction compte
<!-- .slide: class="schema" -->

Le même jeu, deux organisations : à plat, ou en couches qui ne remontent jamais.

![[pcl01_direction_dependances.svg]]

Note:
Projets `925-4FSC0PF001-SpaceShooter` et `CityBuilder_SFML`, tous deux dans
`SAE-Geneve`. À droite, `core/` tient les maths et les interfaces de l'IA, `api/`
les implémentations, `game/` l'assemblage. Un fichier de `core/` ne peut pas
inclure `api/` : la structure l'interdit, et c'est tout l'intérêt.

---

## L'interface dépend du gameplay

Que le bouton **dépende** de ce qu'il déclenche est normal. Que le gameplay
dépende du bouton est une **dette**.

```text
game/  → ui/button_factory.h, ui/clickable.h
api/   → core/ai/bt_node.h
core/  → rien
```

Le sens des flèches dit qui peut être remplacé sans toucher au reste.

---

# Mesurer
<!-- .slide: class="title" -->

---

## Couplage

Le **couplage** se mesure au nombre de choses qu'il faut connaître pour en
modifier une.

- `StarshipPlayer` : SFML, `Motor`, `ProjectileManager`, `AutoEntity`, `EntityManager`
- changer l'un d'eux, c'est rouvrir le joueur
- et le joueur n'est testable qu'avec **tous** les autres présents

Peu de couplage, ce n'est pas zéro dépendance : c'est des dépendances **choisies**.

---

## Cohésion

Une classe est **cohésive** quand tout ce qu'elle contient parle du même sujet.

- cohésive : `Motor` — une vitesse, une accélération, une direction
- pas cohésive : `StarshipPlayer` — textures, bouclier, armes, collisions, entrées
- test rapide : décrire la classe **sans dire « et »**

Le couplage lie les classes entre elles ; la cohésion regarde l'intérieur d'une seule.

---

## La portée d'un changement

La bonne question n'est pas « est-ce que ça marche », c'est :

> **Qu'est-ce que je dois retester ?**

- changer `Motor` : le joueur, les ennemis, les projectiles
- changer la taille d'un sprite de bouclier : le joueur entier se recompile
- changer `core/maths/vec2.h` : tout le CityBuilder

La réponse est la mesure du couplage, et elle se répond **avant** d'écrire.

---

## Responsabilité unique

Une classe ne doit avoir qu'une seule **raison de changer** — pas une seule
fonction.

- `EnemyManager` fait avancer les ennemis **et** décide quand en faire apparaître
- deux raisons : l'équilibrage du spawn, et la mise à jour
- les séparer, c'est pouvoir régler le spawn sans toucher à la boucle

Note:
`EnemyManager::Update` du SpaceShooter construit un `std::random_device` et un
`mt19937` **à chaque image**, parce que la décision de spawn est à l'intérieur de
la mise à jour. Le défaut de conception a ici un coût mesurable — c'est rare, et
c'est l'exemple à montrer.

---

## Les symptômes

- un fichier que **tout le monde** modifie, et qui part en conflit à chaque merge
- des noms en **`Manager`**, qui ne disent pas ce que la classe refuse de faire
- des **paramètres booléens** : `Update(dt, true)` — vrai quoi ?
- la **peur de renommer** quoi que ce soit

Aucun de ces symptômes n'est un bug. Tous coûtent du temps, chaque semaine.

---

## La dette de conception

Elle ne se voit **pas** dans le jeu. Elle se paie en temps, à chaque nouvelle
fonctionnalité.

- la première fonctionnalité coûte un jour
- la dixième en coûte trois, pour la même difficulté apparente
- personne ne peut montrer la dette à un producteur : elle n'a pas d'écran

C'est pour ça qu'il faut la nommer. Le reste du bloc donne les outils.

---

## Atelier — 20 min

**Concevoir un platformer.** Première des trois passes du bloc, et c'est celle
qui dessine.

1. lister les **fonctionnalités** du jeu, sans prononcer le mot « classe »
2. en déduire les **classes**, chacune décrite par **une phrase sans « et »**
3. tracer les **relations** — utilise, contient, est un — et désigner la classe
   dont la modification serait la plus coûteuse
4. rendre **un schéma**

Énoncé : [[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer|Concevoir un platformer]].

Note:
Le même schéma est repris en PCL-03 pour y chercher des patterns, et en PCL-04
pour trancher chaque flèche d'héritage. GP-926 l'écrira ensuite en SFML : c'est
le jeu de la série SBD. Insister sur l'ordre — fonctionnalités d'abord, classes
ensuite. Ceux qui commencent par les classes retrouvent toujours les mêmes
quatre boîtes qu'ils connaissent déjà.

---

## À retenir

- une dépendance, c'est « changer B peut casser A » — **rien d'autre**
- peu de dépendances, **dans le bon sens** : le gameplay ne dépend pas de l'interface
- une classe, **un sujet** : la décrire sans dire « et »
- la dette ne se voit pas à l'écran, elle se paie au temps de développement

---

# Questions ?
<!-- .slide: class="title" -->
