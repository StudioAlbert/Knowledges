---
title: Résolution de triangles et applications
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Trigonométrie
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: true
---

# Résolution de triangles et applications
<!-- .slide: class="title" -->

### Loi des sinus, loi des cosinus, atan2 : viser, mesurer, tirer

<small>TC-FT-TRG-03 · Trigonométrie</small>

Note:
Troisième et dernière séance du bloc. TRG-01 a posé le triangle et Pythagore,
TRG-02 le cercle unité et sin/cos/tan. Ici on assemble les deux pour
résoudre n'importe quel triangle, puis on branche ça sur trois briques de
programmation de jeu : viser une cible, mesurer un cap, tirer en cloche.

---

## Objectifs

À la fin de la séance, vous savez :

- utiliser les identités d'addition et de duplication de sin et cos
- distinguer `asin`, `acos`, `atan` et expliquer pourquoi `atan2` existe
- énoncer et appliquer la **loi des sinus**
- énoncer et appliquer la **loi des cosinus**, et la relier à Pythagore
- résoudre un triangle quelconque à partir de trois mesures (ACA, CAC, CCC)
- calculer l'angle entre deux directions avec `atan2`
- calculer l'angle de tir d'un projectile pour atteindre une cible donnée

**Prérequis :** [[01 courses/slides/Theory/TC-FT-TRG-01 - Géométrie du triangle|TRG-01]] (Pythagore, triangles, similitude), [[01 courses/slides/Theory/TC-FT-TRG-02 - Cercle trigonométrique et unités|TRG-02]] (sin, cos, tan, cercle unité, radians).

---

# Identités d'addition et de duplication
<!-- .slide: class="title" -->

---

## Composer deux rotations

Sur le cercle unité (TRG-02), tourner de α **puis** de β revient à tourner de α + β :

```
sin(α + β) = sin α · cos β + cos α · sin β
cos(α + β) = cos α · cos β − sin α · sin β
```

- pour une différence, seuls les signes du milieu changent :
  `sin(α − β) = sin α cos β − cos α sin β` · `cos(α − β) = cos α cos β + sin α sin β`
- se retrouvent en composant deux matrices de rotation 2D — sans les nommer encore

Note:
On admet ces identités : la démonstration géométrique complète (projection
d'un point tourné deux fois) prend plus de temps qu'elle n'en vaut ici. Ce
qui compte, c'est de savoir les appliquer et d'y reconnaître une composition
de rotations, revue formellement au bloc Géométrie vectorielle.

---

## Duplication

En posant β = α dans les formules précédentes :

```
sin(2α) = 2 · sin α · cos α
cos(2α) = cos²α − sin²α  =  2cos²α − 1  =  1 − 2sin²α
```

Trois écritures de cos(2α), équivalentes via cos² + sin² = 1 (TRG-02) — utile pour éliminer l'une ou l'autre selon ce qu'on connaît.

Note:
Piège classique : « doubler un angle double son sinus ». Faux — sin(2α)
dépend aussi de cos α, et n'est proche de 2·sin α que pour un petit angle
(sin α ≈ α). Passé 45°, doubler l'angle peut même faire **chuter** le
sinus : 80° → 160° fait passer sin de 0,985 à 0,342, une fois 2α au-delà de 90°.

---

## À quoi ça sert en code

Faire tourner un point d'un petit angle supplémentaire **sans** recalculer sin et cos depuis zéro :

```cpp
// on connaît déjà (cos θ, sin θ) ; on avance de δ à chaque frame
float cosD = std::cos(delta), sinD = std::sin(delta);
float newCos = cosTheta * cosD - sinTheta * sinD;   // cos(θ + δ)
float newSin = sinTheta * cosD + cosTheta * sinD;   // sin(θ + δ)
```

Une seule paire (cosD, sinD) calculée une fois, réutilisée à chaque frame : c'est la **matrice de rotation 2D**, qu'on formalise à GVM-03.

Note:
C'est exactement ce que fait un moteur de particules qui fait tourner des
centaines de points chaque frame : deux multiplications et deux additions
par point, contre deux appels à cos/sin — nettement plus coûteux en masse.

---

# Fonctions réciproques : retrouver l'angle
<!-- .slide: class="title" -->

---

## asin, acos, atan

sin, cos et tan prennent un angle et rendent un nombre. Pour l'opération inverse :

| Fonction | Domaine | Codomaine (valeur principale) |
|---|---|---|
| **asin** (arcsin) | [−1, 1] | [−90°, 90°] |
| **acos** (arccos) | [−1, 1] | [0°, 180°] |
| **atan** (arctan) | ℝ | (−90°, 90°) |

Un seul nombre en entrée ⇒ un seul angle en sortie : ces fonctions **choisissent** une réponse parmi une infinité d'angles possibles (périodicité, TRG-02).

Note:
Rappeler l'exercice de TRG-02 (sin θ = 0,6, quadrant II) : c'est exactement
la limite d'asin — elle renvoie toujours une valeur entre −90° et 90°, donc
jamais un angle de quadrant II ou III directement. Il faut recorriger à la main.

---

## Le problème de atan seul

Une direction (dx, dy) définit un angle, mais `atan(dy / dx)` perd de l'information :

- **division par zéro** si dx = 0 (direction verticale)
- **même résultat pour deux directions opposées** : (3, 2) et (−3, −2) ont le même rapport dy/dx, donc le même atan, alors qu'elles pointent à l'opposé l'une de l'autre

```cpp
std::atan(2.0 / 3.0);     // ≈ 33,7°
std::atan(-2.0 / -3.0);   // ≈ 33,7° — même résultat, mauvaise direction !
```

Note:
atan ne voit qu'un rapport, pas un point : il ne sait pas dans quel sens on
regarde. C'est le nœud du problème que atan2 résout à la slide suivante.

---

## atan2(dy, dx)

`atan2` prend **les deux coordonnées séparément**, pas leur rapport :

- couvre tout le cercle : **(−180°, 180°]**, aucune division par zéro
- signe de dx et de dy ⇒ quadrant correct, automatiquement

```cpp
std::atan2(dy, dx);              // C++
```
```csharp
Mathf.Atan2(dy, dx);             // Unity — attention à l'ordre (y, x)
```

Note:
Insister sur l'ordre des arguments : (y, x), pas (x, y) — l'erreur la plus
fréquente en TP. `Mathf.Atan2` en radians comme tout Mathf trigonométrique.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/resolution_triangles_widget.html#atan2" data-background-interactive -->

Note:
Widget interactif — onglet « atan2 — viser une cible » :
1. Glisser T dans chaque quadrant, observer la droite grise (résultat de
   atan seul) : elle coïncide avec la flèche rouge en quadrant I/IV (dx > 0)
   et pointe à l'opposé en quadrant II/III (dx < 0). Amener dx à 0 : atan
   plante, atan2 continue de répondre.
2. Cocher « Deuxième direction » : montre l'angle signé entre deux vecteurs
   via une différence de atan2 (le sens de rotation) contre acos du produit
   scalaire (toujours positif, sans le sens) — prépare le dot product de GVM-02.

Repli : ouvrir 00 widgets/_widgets/resolution_triangles_widget.html localement.

---

# Résoudre un triangle quelconque
<!-- .slide: class="title" -->

---

## Rappel : que veut dire « résoudre »

Un triangle porte 6 mesures (3 côtés, 3 angles, TRG-01). En connaître **3 bien choisies** donne les 3 autres.

| Cas | Connu | Outil |
|---|---|---|
| **ACA** | 1 côté, 2 angles à ses extrémités | loi des sinus |
| **CAC** | 2 côtés, l'angle compris | loi des cosinus |
| **CCC** | 3 côtés | loi des cosinus (à l'envers) |

Le triangle rectangle (TRG-02, SOH CAH TOA) est un cas particulier : dès qu'un angle vaut 90°, ces deux lois se simplifient.

Note:
Relier explicitement à TRG-01 : CCC et CAC sont les cas de construction déjà
vus. Ce qui change ici, c'est qu'on calcule les mesures manquantes au lieu
de les construire au compas.

---

## Loi des sinus : énoncé

> Dans tout triangle, chaque côté divisé par le sinus de l'angle opposé donne la **même valeur** — le diamètre du cercle circonscrit.

```
a / sin A = b / sin B = c / sin C = 2R
```

- utile dès qu'on a un côté **et** l'angle qui lui est opposé (ACA, ou 2 angles + 1 côté quelconque : le 3ᵉ angle se déduit)
- **piège de l'angle ambigu** : donner 2 côtés et un angle **non compris** entre eux (CCA) peut avoir 0, 1 ou 2 solutions — la loi des cosinus n'a pas ce problème

Note:
Le lien avec le cercle circonscrit n'est pas un détail : c'est la raison
géométrique de l'égalité (angle inscrit / arc intercepté, TRG-02). Le widget
le rend visible en superposant le cercle.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/resolution_triangles_widget.html#sinus" data-background-interactive -->

Note:
Onglet « Loi des sinus » : curseurs côté c, angle A, angle B (cas ACA, comme
à TRG-01). Le panneau calcule C par somme des angles, puis b et a par la loi
des sinus, et affiche les trois rapports égaux entre eux. Le cercle
circonscrit (case à cocher) matérialise le « = 2R » : son rayon ne bouge pas
quand on déplace les curseurs à C constant.

---

## Loi des cosinus : énoncé

> Généralise Pythagore à un triangle **quelconque**, en ajoutant le terme qui manque quand l'angle n'est pas droit.

```
c² = a² + b² − 2ab · cos C
```

- angle C = 90° ⇒ cos C = 0 ⇒ on retombe exactement sur Pythagore
- angle C aigu ⇒ le terme soustrait rend c **plus petit** que √(a² + b²) ; obtus ⇒ plus grand — cohérent avec la réciproque de Pythagore vue à TRG-01

Note:
Présenter la loi des cosinus comme « Pythagore + correction » plutôt que
comme une formule nouvelle et isolée : ça se retient mieux et ça relie
directement les trois séances du bloc.

---

## Cas CCC : retrouver un angle

En isolant cos C dans la formule précédente :

```
cos C = (a² + b² − c²) / (2ab)
C = acos( (a² + b² − c²) / (2ab) )
```

- fonctionne avec **seulement** les trois côtés — aucun rapporteur
- c'est la généralisation directe de la réciproque de Pythagore (TRG-01) : là on ne testait que « droit ou pas », ici on obtient la valeur exacte de l'angle

Note:
Faire le lien avec l'exercice de TRG-01 (9-12-15) : appliquer cette formule
donnerait directement C = 90°, cohérent avec ce qu'ils avaient trouvé par
comparaison de carrés.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/resolution_triangles_widget.html#cosinus" data-background-interactive -->

Note:
Onglet « Loi des cosinus » : curseurs côtés a, b, angle C (cas CAC). Deux
préréglages : 90°/3-4-5 (Pythagore, le terme croisé s'annule visiblement) et
60°/équilatéral (a = b, C = 60° ⇒ c = a = b, callback à TRG-01). La carte
« Vérification inverse » applique acos aux trois côtés obtenus et retrouve
exactement l'angle C du curseur — à faire remarquer explicitement.

---

## Exemple : viser à travers un obstacle

Deux relevés depuis un même point O : une tourelle à 8 m (angle 0° pris comme référence), une cible à 11 m, séparées d'un angle de 35° vues depuis O.

```
c² = 8² + 11² − 2 × 8 × 11 × cos 35°
c² = 185 − 144,2 ≈ 40,8
c = √40,8 ≈ 6,39 m
```

Distance tourelle → cible obtenue **sans jamais connaître leurs positions cartésiennes** — seulement deux distances et un angle mesuré.

Note:
C'est le scénario CAC le plus courant en jeu : deux capteurs, un angle
mesuré (souvent via atan2, slide précédente), et une distance à en déduire.
GPS, radar, portée d'un cône de vision : même calcul.

---

# Applications
<!-- .slide: class="title" -->

---

## Angle entre deux directions

Un PNJ regarde selon **d1**, le joueur est dans la direction **d2** (toutes deux depuis le PNJ). L'angle entre les deux, signé :

```cpp
float a1 = std::atan2(d1.y, d1.x);
float a2 = std::atan2(d2.y, d2.x);
float turn = a2 - a1;                 // ramener dans ]−180°, 180°]
if (turn > 180.f)  turn -= 360.f;
if (turn <= -180.f) turn += 360.f;
```

- **positif** = tourner vers la gauche, **négatif** = vers la droite (repère anti-horaire, TRG-02)
- alternative avec la loi des cosinus / le produit scalaire : `acos(dot / (‖d1‖·‖d2‖))` donne l'angle **non signé** — utile pour un champ de vision, pas pour décider du sens à tourner

Note:
Deux outils, deux usages : atan2-diff pour piloter une rotation (IA qui
recale son cap, tourelle qui vise), acos-du-produit-scalaire pour tester
« est-ce dans mon champ de vision ? » sans se soucier du sens. Le widget
atan2 montre les deux côte à côte.

---

## Tir en cloche

Un projectile de vitesse initiale *v*, lancé à l'angle θ **depuis le sol vers une cible au sol** (même hauteur), atteint une distance *d* (gravité *g*) quand :

```
d = (v² · sin(2θ)) / g
```

En isolant θ avec asin :

```
θ = ½ · asin(g · d / v²)
```

- deux solutions : θ (tir tendu) et 90° − θ (tir en cloche) — même portée, `sin(2θ) = sin(180° − 2θ)`
- **portée maximale** à θ = 45° ; si g·d/v² > 1, asin échoue : **aucun angle n'atteint la cible** à cette vitesse

Note:
Faire le lien avec la duplication vue en début de séance : sin(2θ) est
exactement l'identité de duplication appliquée à l'angle de tir. La formule
n'est donc pas un nouvel objet, mais une application directe de la première
section.

---

## Exemple chiffré

Catapulte : v = 20 m/s, g = 9,81 m/s², cible à d = 30 m.

```
sin(2θ) = g·d / v² = 9,81 × 30 / 400 ≈ 0,736
2θ = asin(0,736) ≈ 47,4°  ou  2θ = 180° − 47,4° = 132,6°
θ ≈ 23,7° (tendu)   ou   θ ≈ 66,3° (en cloche)
```

Les deux angles envoient le projectile à exactement 30 m ; seule la hauteur et le temps de vol diffèrent.

Note:
Bon exercice de vérification : demander quelle des deux options survole un
obstacle entre le lanceur et la cible — c'est le tir en cloche (66,3°), plus
lent horizontalement mais plus haut.

---

## À retenir

- sin(α+β), cos(α+β) et leurs versions dupliquées : composer des rotations sans refaire le calcul trigonométrique complet
- **atan2(dy, dx)**, pas atan(dy/dx) : tous les quadrants, jamais de division par zéro
- **loi des sinus** — a/sinA = b/sinB = c/sinC = 2R — cas ACA
- **loi des cosinus** — c² = a²+b²−2ab·cosC — généralise Pythagore, cas CAC et CCC
- angle entre deux directions : différence de atan2 (signée) ou acos du produit scalaire (non signée)
- tir en cloche : θ = ½asin(gd/v²), deux solutions, portée max à 45°

---

## Exercices

- appliquer la loi des sinus à un triangle ACA
- appliquer la loi des cosinus pour une distance (CAC) et pour un angle (CCC)
- corriger un calcul de direction qui utilise atan au lieu de atan2
- calculer un angle de tir pour une portée donnée, et discuter des deux solutions

---

## Pour aller plus loin

- Séance précédente : [[01 courses/slides/Theory/TC-FT-TRG-02 - Cercle trigonométrique et unités|TC-FT-TRG-02 - Cercle trigonométrique et unités]]
- Widget : [Résolution de triangles — sinus, cosinus, atan2](<00 widgets/_widgets/resolution_triangles_widget.html>)
- Lengyel, *Mathematics for 3D Game Programming*, annexe B §B.4–B.6
- [Loi des sinus — Wikipédia](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_sinus)
- [Loi des cosinus — Wikipédia](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_d%27Al-Kashi)
- [atan2 — Wikipédia](https://fr.wikipedia.org/wiki/Atan2)
