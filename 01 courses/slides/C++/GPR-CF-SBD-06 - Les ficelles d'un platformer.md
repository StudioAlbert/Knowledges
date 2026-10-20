---
title: GPR-CF-SBD-06 - Les ficelles d'un platformer
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

# Les ficelles d'un platformer
<!-- .slide: class="title" -->

### Étape 6 du platformer

<small>GPR-CF-SBD-06 · SFML et Box2D</small>

Note:
Mini-séance, et la seule de la série qui ne parle pas d'API : un répertoire de
ficelles techniques et de game design. Aucune ne se déduit d'une équation, et
c'est précisément ce qu'il faut qu'ils retiennent.

---

## Objectifs

À la fin de la séance, vous savez :

- détecter « au sol » avec un **capteur**, pas avec un contact
- nommer et régler **coyote time** et **jump buffer**
- dire ce qui rend un saut **agréable**, et pas seulement correct
- citer trois décisions d'**accessibilité** qui ne coûtent presque rien

**Prérequis :** [[01 courses/slides/C++/GPR-CF-SBD-05 - Relier physique et graphique|GPR-CF-SBD-05]].

---

## Ce qu'on attend d'un contrôleur

Un corps physique **tombe correctement**. Ça ne suffit pas :

- il saute quand on appuie, pas trois images plus tard
- il ne saute pas en l'air
- il ne reste pas accroché à l'arête d'une plateforme

---

# Le sol
<!-- .slide: class="title" -->

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

## Toucher par le côté

Un contact avec un mur n'est **pas** un contact avec le sol.

- le capteur sous les pieds l'exclut d'office — c'est pour ça qu'on en met un
- un capteur latéral, lui, sert au **wall jump**
- un capteur au-dessus sert à ne pas coller au plafond en montant

Trois capteurs, trois questions. Aucun n'arrête le personnage.

---

# Le saut
<!-- .slide: class="title" -->

---

## Le coyote time

```cpp
if (AuSol()) coyote_ = kCoyote;        // kCoyote ≈ 0,08 s
else         coyote_ -= dt;

if (sautDemande_ && coyote_ > 0.f)
{
    corps_->SetLinearVelocity({v.x, kImpulsionSaut});
    coyote_ = 0.f;
}
```

Le saut reste possible **quelques centièmes de seconde** après avoir quitté le
sol. Le joueur ne le remarque jamais ; il remarque son absence.

Note:
Le nom vient du coyote de Tex Avery, qui court dans le vide avant de tomber.
Entre 0,05 et 0,15 s selon les jeux. Au-delà, on saute visiblement dans le
vide ; en dessous de 0,05, personne ne sent la différence.

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
b2World_SetPreSolveCallback(monde, Traversable, nullptr);

// dans le rappel : false annule le contact, cette fois seulement
bool Traversable(b2ShapeId a, b2ShapeId b, b2Manifold* m, void*)
{
    return !(EstPlateforme(a, b) && MonteVersElle(m));
}
```

C'est le seul endroit où l'on peut annuler un contact au cas par cas — et le
seul rappel qui reste dans Box2D 3.

Note:
Le rappel tourne **pendant** la simulation, et Box2D est multithread : on ne
crée, ne détruit et ne modifie rien dedans. On lit, on répond `true` ou `false`.

---

## Le wall jump

- un capteur latéral dit qu'un mur est là
- le saut applique une vitesse **vers le haut et vers l'opposé**
- pendant quelques dixièmes, on ignore l'entrée du joueur, sinon il recolle au mur

Ce troisième point est la ficelle : sans elle, le wall jump ne marche pas, et
rien dans la physique ne l'indique.

---

# Le fun, et tout le monde
<!-- .slide: class="title" -->

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

## L'accessibilité, à trois décisions

- **touches reconfigurables** — une table, pas des `if` codés en dur
- **aucune combinaison à trois doigts** — ni maintien long obligatoire
- **le niveau pardonne** — points de reprise fréquents, pas de chute punitive

Ça ne coûte presque rien si on y pense **maintenant**, et ça coûte une refonte
si on y pense à la fin.

Note:
Lier au point précédent : coyote time et jump buffer **sont** des mesures
d'accessibilité avant d'être des astuces de game feel. Un joueur précis ne les
sent pas ; un joueur moins précis ne joue pas sans.

---

## Régler, c'est tester

1. changer **une** valeur à la fois
2. rejouer **le même** passage, celui qui vous embête
3. demander à quelqu'un d'autre de jouer, sans rien lui expliquer
4. noter la valeur retenue et **pourquoi**

Toutes les valeurs vivent dans un seul fichier de réglages — doublez-en une,
recompilez, et vous saurez si elles en sont vraiment sorties.

---

## Pas d'atelier, une finition

Cette séance n'a **pas** d'exercice à elle : les ficelles se posent dans le jeu
que vous avez déjà, et elles se jugent en jouant.

L'heure sert à les essayer une par une, à régler, et à faire jouer le voisin.

Le rendu de la série :
[[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]].

Note:
Démonstration : `MoveAndJump` pour le saut, `LevelEditor` pour les tuiles et les
plateformes. Garder vingt minutes pour faire jouer les projets entre eux — c'est
le seul test qui dise si le saut est bon.

---

## À retenir

- « au sol » se mesure avec un **capteur** et un **compteur**, jamais un booléen de contact
- coyote time et jump buffer : la même idée, dans les deux sens du temps
- ce qui rend un saut agréable n'est **pas** dans le moteur physique
- l'accessibilité se décide au début, ou elle coûte une refonte

---

# Questions ?
<!-- .slide: class="title" -->

### Fin de la série

<small>Le rendu : [[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]].</small>
