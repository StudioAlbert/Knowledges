---
title: GPR-CF-SBD-06 - Le game feel d'un platformer
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

# Le game feel d'un platformer
<!-- .slide: class="title" -->

### Étape 6 du platformer

<small>GPR-CF-SBD-06 · SFML et Box2D</small>

Note:
Mini-séance, et la seule de la série qui ne parle pas d'API : un répertoire de
techniques, moitié code moitié game design. Aucune ne se déduit d'une équation,
et c'est précisément ce qu'il faut qu'ils retiennent.

Le deck va dans cet ordre : **on sent d'abord, on code ensuite**. La première
moitié ne montre aucune ligne de C++ — c'est voulu. Tant qu'ils n'ont pas vu les
deux coureurs du widget, le code n'a rien à expliquer.

---

## Objectifs

À la fin de la séance, vous savez :

- dire ce qui rend un saut **agréable**, et pas seulement correct
- nommer et régler **coyote time** et **jump buffer**
- détecter « au sol » avec un **capteur**, pas avec un contact
- citer trois décisions d'**accessibilité** qui ne coûtent presque rien

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-05 - Relier physique et graphique|GPR-CF-SBD-05]].

---

## Ce qu'on attend d'un contrôleur

Un corps physique **tombe correctement**. Ça ne suffit pas :

- il saute quand on appuie, pas trois images plus tard
- il ne saute pas en l'air
- il ne reste pas accroché à l'arête d'une plateforme

---

# Ce que le joueur sent
<!-- .slide: class="title" -->

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/saut_fun_widget.html#coyote" data-background-interactive -->

Note:
**La slide qui ouvre la séance.** Les quatre onglets, dans l'ordre. Les deux
premiers décident qui passe et qui tombe — c'est la démonstration. Les deux
derniers ne font tomber personne : *hauteur variable* montre 61 px contre 31 px
pour **le même appui**, et *gravité asymétrique* montre la même hauteur mais deux
courbes différentes.

Faire remarquer que les deux coureurs reçoivent **la même touche au même
instant** : la seule variable est la technique. Aucun code à l'écran pour
l'instant — on nomme ce qu'on voit, on l'écrira tout à l'heure.

---

## Ce qui rend un saut agréable

| Réglage | Ce que le joueur ressent |
|---|---|
| gravité plus forte **en descente** | le saut est nerveux, pas flottant |
| hauteur variable selon l'appui | il contrôle, au lieu de subir |
| coyote time + jump buffer | « le jeu a compris ce que je voulais » |
| une courte accélération au sol | le personnage a du poids |

Aucune de ces lignes n'est dans Box2D. Toutes sont dans votre contrôleur.

---

## Le wall jump

- un capteur latéral dit qu'un mur est là
- le saut applique une vitesse **vers le haut et vers l'opposé**
- pendant quelques dixièmes, on ignore l'entrée du joueur, sinon il recolle au mur

Ce troisième point est la technique : sans elle, le wall jump ne marche pas, et
rien dans la physique ne l'indique.

---

## L'accessibilité, à trois décisions

- **touches reconfigurables** — une table, pas des `if` codés en dur
- **aucune combinaison à trois doigts** — ni maintien long obligatoire
- **le niveau pardonne** — points de reprise fréquents, pas de chute punitive

Ça ne coûte presque rien si on y pense **maintenant**, et ça coûte une refonte
si on y pense à la fin.

Note:
Lier au widget : coyote time et jump buffer **sont** des mesures d'accessibilité
avant d'être des astuces de game feel. Un joueur précis ne les sent pas ; un
joueur moins précis ne joue pas sans.

---

# Et dans le code
<!-- .slide: class="title" -->

---

## « Au sol » n'est pas un contact

Un contact dit « ces deux formes se touchent ». Il ne dit pas **où**.

- toucher un mur par le côté, ce n'est **pas** être au sol
- un capteur latéral, lui, sert au wall jump qu'on vient de voir
- un capteur au-dessus sert à ne pas coller au plafond en montant

Trois capteurs, trois questions. Aucun n'arrête le personnage.

---

## Le capteur de sol

```cpp
const b2Polygon pieds =
    b2MakeOffsetBox(0.35f, 0.08f, {0.f, -0.9f}, b2Rot_identity);

b2ShapeDef def = b2DefaultShapeDef();
def.isSensor = true;              // il détecte, il n'arrête rien
def.enableSensorEvents = true;    // sans ça : aucun événement
def.userData = &capteurSol_;

b2CreatePolygonShape(heros, &def, &pieds);
```

Un **capteur** traverse tout et signale ce qu'il traverse. C'est la bonne
réponse à « est-ce que je touche le sol ».

<small>Exemple : [04-ZeroGravity](https://github.com/StudioAlbert/GPR-CF-SBD-XX---Box2D-Examples/tree/master/04-ZeroGravity)</small>

---

## Compter, ne pas basculer

```cpp
const b2SensorEvents capteurs = b2World_GetSensorEvents(monde);

for (int i = 0; i < capteurs.beginCount; ++i) ++contactsSol_;
for (int i = 0; i < capteurs.endCount;   ++i) --contactsSol_;

bool AuSol() const { return contactsSol_ > 0; }
```

Un booléen casse dès qu'on touche **deux** plateformes à la fois : la première
qu'on quitte met `false` alors qu'on est toujours posé.

Note:
Le bug est garanti sur toute arête entre deux tuiles de sol : le héros marche,
et il perd le droit de sauter une image sur deux. Un compteur règle le cas sans
rien comprendre de plus.

---

## Le coyote time

```cpp
if (AuSol()) coyote_ = kCoyote;        // kCoyote ≈ 0,08 s
else         coyote_ -= dt;

if (sautDemande_ && coyote_ > 0.f)
{
    const b2Vec2 v = b2Body_GetLinearVelocity(corps_);
    b2Body_SetLinearVelocity(corps_, {v.x, kImpulsionSaut});
    coyote_ = 0.f;
}
```

C'est l'onglet `#coyote` du widget, en six lignes.

Note:
Le nom vient du coyote de Tex Avery, qui court dans le vide avant de tomber.
Entre 0,05 et 0,15 s selon les jeux. Au-delà, on saute visiblement dans le
vide ; en dessous de 0,05, personne ne sent la différence.

On garde `v.x` : le saut change la vitesse verticale et **ne touche pas** à la
course en cours. Y monte chez Box2D, donc `kImpulsionSaut` est positif.

---

## Le saut mis en mémoire

```cpp
if (toucheSaut_) tampon_ = kTampon;    // kTampon ≈ 0,1 s
else             tampon_ -= dt;

if (tampon_ > 0.f && AuSol()) { Sauter(); tampon_ = 0.f; }
```

Une touche pressée **juste avant** l'atterrissage déclenche le saut dès le
contact, au lieu d'être perdue.

Coyote time et jump buffer sont la même idée, dans les deux sens du temps.

---

## Passer d'une plateforme à l'autre

Un personnage qui accroche l'arête d'une tuile, c'est **la forme** qui est en
cause, pas la physique :

- une boîte à angles vifs accroche les jointures du sol
- un bas arrondi, ou un capteur un peu plus étroit que le corps, n'accroche plus
- des tuiles de sol fusionnées en **une** forme suppriment les jointures

Aucune de ces trois réponses n'est un réglage de gravité.

---

## La plateforme à sens unique

```cpp
forme.enablePreSolveEvents = true;
b2World_SetPreSolveCallback(monde, Traversable, nullptr, nullptr);

// zéro point de contact = pas de collision, cette image seulement
void Traversable(b2ShapeId a, b2ShapeId b, b2Manifold* m, void*)
{
    if (EstPlateforme(a, b) && MonteVersElle(m)) m->pointCount = 0;
}
```

C'est le seul endroit où l'on peut **annuler** un contact au cas par cas.

Note:
Attention, le rappel a changé en Box2D **3.2** : il renvoie `void`, et on annule
la collision en mettant `pointCount` à zéro. Les versions 3.0 et 3.1 renvoyaient
un `bool` — un exemple trouvé en ligne ne compilera pas ici.

Le rappel tourne pendant la simulation, et Box2D est multithread : on ne crée,
ne détruit et ne modifie rien dedans. On lit le manifold, on le neutralise ou
non.

Box2D 3 garde quatre rappels au niveau du monde — filtrage personnalisé,
pre-solve, friction, restitution. Ce qui a disparu, c'est le `b2ContactListener`
de la version 2 : les contacts se **lisent** après le pas, ils ne se reçoivent
plus.

---

## Régler, c'est tester

1. changer **une** valeur à la fois
2. rejouer **le même** passage, celui qui vous embête
3. demander à quelqu'un d'autre de jouer, sans rien lui expliquer
4. noter la valeur retenue et **pourquoi**

Toutes les valeurs vivent dans un seul fichier de réglages — doublez-en une,
recompilez, et vous saurez si elles en sont vraiment sorties.

---

## Une technique, et un playtest

Pas d'atelier en salle : les techniques se posent dans le jeu que vous avez
déjà, et elles se jugent en jouant.

**La formative** : une seule technique, bien réglée, avec un interrupteur pour
l'éteindre. La semaine prochaine, tout le monde joue à tout le monde.

[[01 courses/exercises/C++/GPR-CF-SBD-06 - Formative, un saut qui fait envie|Un saut qui fait envie]]
· [[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]]

<small>Exemples : [MoveAndJump.cpp](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/blob/main/MoveAndJump/MoveAndJump.cpp) · [LevelEditor](https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples/tree/main/LevelEditor)</small>

Note:
Garder vingt minutes pour faire jouer les projets entre eux — c'est le seul test
qui dise si le saut est bon.

L'interrupteur est le point à insister : une technique qu'on ne peut pas
éteindre ne se démontre pas au playtest.

---

## À retenir

- ce qui rend un saut agréable n'est **pas** dans le moteur physique
- coyote time et jump buffer : la même idée, dans les deux sens du temps
- « au sol » se mesure avec un **capteur** et un **compteur**, jamais un booléen
- l'accessibilité se décide au début, ou elle coûte une refonte

---

# Questions ?
<!-- .slide: class="title" -->

### Fin de la série

<small>Le rendu : [[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]].</small>
