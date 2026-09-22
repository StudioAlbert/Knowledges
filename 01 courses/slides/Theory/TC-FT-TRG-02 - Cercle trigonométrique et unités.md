---
title: Cercle trigonométrique et unités
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

# Cercle trigonométrique et unités
<!-- .slide: class="title" -->

### Sinus, cosinus, tangente : d'un triangle à un point qui tourne

<small>TC-FT-TRG-02 · Trigonométrie</small>

Note:
Deuxième séance du bloc. TRG-01 a posé le vocabulaire du triangle rectangle
(hypoténuse, cathètes) et la similitude : on s'en sert dès la première
section. Fil rouge : tout ce qui tourne, oscille ou vise dans un jeu passe
par sin et cos — et presque tous les bugs viennent des unités.

---

## Objectifs

À la fin de la séance, vous savez :

- définir sinus, cosinus et tangente dans un triangle rectangle
- convertir un angle entre **degrés**, **radians** et **tours** sans hésiter
- placer un angle sur le **cercle unité** et y lire cos, sin et leurs signes
- retrouver les **valeurs remarquables** sans les apprendre par cœur
- exploiter les symétries du cercle et le **déphasage** entre sin et cos
- utiliser **cos² + sin² = 1**

**Prérequis :** [[01 courses/slides/Theory/TC-FT-TRG-01 - Géométrie du triangle|TC-FT-TRG-01]] (Pythagore, triangles semblables).

---

# Du triangle aux rapports
<!-- .slide: class="title" -->

---

## Le triangle rectangle, vu depuis un angle

On se place au sommet d'un angle aigu **α** :

- l'**hypoténuse** ne change pas : c'est le côté opposé à l'angle droit
- le côté **opposé** est celui qui ne touche pas α
- le côté **adjacent** est la cathète qui touche α

Changer d'angle aigu échange opposé et adjacent — l'hypoténuse reste la même.

Note:
Faire le dessin au tableau avec les deux angles aigus, et nommer les côtés
depuis l'un puis depuis l'autre. C'est la confusion numéro un en exercice.

---

## Sinus, cosinus, tangente

```
sin α = opposé   / hypoténuse
cos α = adjacent / hypoténuse
tan α = opposé   / adjacent  = sin α / cos α
```

Moyen mnémotechnique : **SOH CAH TOA**.

- sin et cos sont compris entre **0 et 1** dans un triangle : on divise par le plus long côté
- la tangente, elle, n'est pas bornée

---

## Pourquoi ça ne dépend que de l'angle

Deux triangles rectangles avec le même angle α sont **semblables** (TRG-01) :

- leurs côtés sont proportionnels, de rapport *k*
- donc les **rapports** entre côtés sont identiques, quelle que soit la taille

sin α, cos α et tan α sont des propriétés **de l'angle**, pas du triangle.

Note:
C'est le lien direct avec la séance précédente : la trigonométrie, c'est la
similitude mise en tableau. Une fois qu'on a les rapports pour un triangle
d'hypoténuse 1, on les a pour tous.

---

<!-- .slide: class="schema" -->

![[trg02_rapports_trigo.svg]]

Note:
Le schéma résume les trois slides précédentes. Le lire de gauche à droite :
1. depuis α, l'opposé est en face, l'adjacent touche l'angle ;
2. depuis β, les deux s'échangent — l'hypoténuse, elle, ne bouge jamais,
   et β = 90° − α puisque la somme des angles vaut 180° ;
3. deux triangles de tailles différentes avec le même α : le rapport a/c
   est identique, d'où « sin α ne dépend que de l'angle ».

Source éditable : `Excalidraw/TRG-02 - Rapports trigonométriques.excalidraw.md`.

---

## Exemple : la rampe

Une rampe de 5 m monte avec une pente de 30°.

```
hauteur  = 5 × sin 30° = 5 × 0,5   = 2,5 m
longueur = 5 × cos 30° ≈ 5 × 0,866 ≈ 4,33 m
```

- hypoténuse connue → **multiplier** par sin ou cos
- côté connu, hypoténuse cherchée → **diviser**

Note:
Faire vérifier avec Pythagore : 2,5² + 4,33² ≈ 6,25 + 18,75 = 25 = 5².
Les deux séances se valident l'une l'autre.

---

# Unités d'angle
<!-- .slide: class="title" -->

---

## Trois façons de mesurer un tour

| Unité | Un tour | Angle droit | Où on la croise |
|---|---|---|---|
| **degré** | 360° | 90° | éditeurs, Inspector Unity, level design |
| **radian** | 2π ≈ 6,283 | π/2 | `std::sin`, `Mathf.Sin`, GLSL, HLSL |
| **tour** | 1 | 1/4 | shaders, animations, rotations normalisées |



---

## Le radian

> Un radian est l'angle qui intercepte, sur un cercle, un arc de **même longueur que le rayon**.

- longueur d'arc = rayon × angle en radians : **s = r · θ**
- le périmètre vaut 2πr, donc un tour vaut **2π** radians
- c'est l'unité « naturelle » : elle relie directement l'angle à une distance parcourue

Note:
L'argument décisif pour des programmeurs : une roue de rayon r qui tourne de
θ radians avance de r·θ. Pas de facteur 360 à trimballer. C'est aussi pour
ça que les bibliothèques mathématiques ont toutes fait ce choix.

---

## Conversions

```
radians = degrés × π / 180
degrés  = radians × 180 / π
tours   = degrés / 360      = radians / 2π
```

| degrés | 0 | 30 | 45 | 60 | 90 | 180 | 270 | 360 |
|---|---|---|---|---|---|---|---|---|
| radians | 0 | π/6 | π/4 | π/3 | π/2 | π | 3π/2 | 2π |
| tours | 0 | 1/12 | 1/8 | 1/6 | 1/4 | 1/2 | 3/4 | 1 |

---

## Le piège des unités en code

```cpp
std::sin(90);                     // ≈ 0.894 : 90 RADIANS, pas 90°
std::sin(90 * std::numbers::pi / 180);   // 1
```

```csharp
Mathf.Sin(90 * Mathf.Deg2Rad);          // 1
transform.eulerAngles = new Vector3(0, 90, 0);   // degrés !
```

Règle : **radians partout dans le code**, conversion uniquement à la frontière (UI, Inspector, fichiers de données).

Note:
Unity mélange les deux : Mathf.Sin en radians, eulerAngles et
Quaternion.Euler en degrés. Le symptôme typique : un objet qui tourne
« n'importe comment » ou à peine. Premier réflexe : vérifier l'unité.

---

# Le cercle unité
<!-- .slide: class="title" -->

---

## De l'angle aigu à n'importe quel angle

Cercle de centre O et de **rayon 1**. On part de (1, 0) et on tourne de θ dans le sens **anti-horaire**.

Le point atteint M a pour coordonnées :

```
M = (cos θ, sin θ)
```

- pour θ entre 0 et 90°, c'est exactement SOH CAH TOA avec une hypoténuse de 1
- au-delà, c'est la **définition** : cos et sin deviennent négatifs, et θ peut dépasser 360°

Note:
C'est le saut conceptuel de la séance. Dans le triangle, un angle ne peut pas
valoir 120° ; sur le cercle, si. On garde la même définition — abscisse et
ordonnée de M — et elle s'étend toute seule.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/cercle_trigo_widget.html#cercle" data-background-interactive -->

Note:
Onglet « Le cercle unité ». Faire glisser M : cos est le segment gris sur
(Ox), sin le segment rouge. Basculer les graduations degrés / radians /
tours sur le même dessin — c'est la slide « unités » rendue visible.
Activer la tangente et montrer qu'elle explose en approchant 90°.
Passer par les valeurs remarquables (aimantation activée) : le panneau
donne la valeur exacte, √2/2 et non 0,707.

Repli : ouvrir 00 widgets/_widgets/cercle_trigo_widget.html.

---

## Signes selon le quadrant

| Quadrant | θ entre | cos | sin | tan |
|---|---|---|---|---|
| I | 0 et 90° | + | + | + |
| II | 90° et 180° | − | + | − |
| III | 180° et 270° | − | − | + |
| IV | 270° et 360° | + | − | − |

- cos = abscisse (gauche / droite), sin = ordonnée (haut / bas)
- −1 ≤ cos θ ≤ 1 et −1 ≤ sin θ ≤ 1, toujours

---

## La tangente sur le cercle

- tan θ = sin θ / cos θ : c'est la **pente** de la droite (OM)
- on la lit sur la droite verticale x = 1, là où (OM) la coupe
- elle n'existe pas quand cos θ = 0 : à **90°** et **270°**, (OM) est verticale

```cpp
float slope = std::tan(angle);   // proche de 90° : valeur énorme, précision perdue
```

Note:
Conséquence pratique : ne jamais calculer une direction avec tan quand on
peut utiliser (cos, sin). C'est l'amorce d'atan2, vu à TRG-03.

---

## Valeurs remarquables

| θ | 0 | 30° · π/6 | 45° · π/4 | 60° · π/3 | 90° · π/2 |
|---|---|---|---|---|---|
| **sin** | 0 | 1/2 | √2/2 | √3/2 | 1 |
| **cos** | 1 | √3/2 | √2/2 | 1/2 | 0 |
| **tan** | 0 | √3/3 | 1 | √3 | — |

Astuce : sin vaut **√0/2, √1/2, √2/2, √3/2, √4/2** — et cos parcourt la même suite à l'envers.

---

## D'où viennent-elles

- **45°** : demi-carré de côté 1 → deux cathètes égales, hypoténuse √2 (Pythagore) → cos = sin = 1/√2 = **√2/2**
- **30° et 60°** : moitié d'un équilatéral de côté 1 → base 1/2, hauteur **√3/2** (TRG-01)
- les autres angles remarquables (120°, 135°, 210°…) s'en déduisent par symétrie

Note:
Refaire les deux dessins au tableau : c'est plus rapide que de réviser le
tableau, et ça ne s'oublie pas. La hauteur √3/2 de l'équilatéral a été
calculée à la séance précédente.

---

# Symétries et déphasages
<!-- .slide: class="title" -->

---

## Les symétries du cercle

| Transformation | Symétrie | cos | sin |
|---|---|---|---|
| θ → **−θ** | axe (Ox) | cos θ | −sin θ |
| θ → **π − θ** | axe (Oy) | −cos θ | sin θ |
| θ → **π + θ** | centre O | −cos θ | −sin θ |
| θ → **π/2 − θ** | droite y = x | sin θ | cos θ |

On ne les apprend pas : on **dessine le cercle** et on lit.

Note:
cos est **paire** (cos(−θ) = cos θ), sin est **impaire**. C'est la
première ligne, et la plus utilisée : retourner un sprite ou un angle de
visée horizontalement ne change que le signe de sin.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/cercle_trigo_widget.html#symetries" data-background-interactive -->

Note:
Onglet « Symétries ». Prendre θ = 30°, afficher −θ seul : les projections
dessinées montrent que l'abscisse est commune (cos identique) et que
l'ordonnée est retournée (sin opposé). Ajouter π−θ, puis π+θ, puis
π/2−θ — à chaque fois, faire énoncer la relation par les étudiants avant
de la lire dans le panneau de droite.
Le point à faire passer : aucune de ces quatre lignes ne s'apprend, elles
se lisent sur le dessin.

Repli : ouvrir 00 widgets/_widgets/cercle_trigo_widget.html#symetries.

---

## Périodicité et déphasage

- un tour complet ramène au même point : sin(θ + 2π) = sin θ — **période 2π**
- cos est un sin **en avance d'un quart de tour** :

```
cos θ = sin(θ + π/2)
```

- une onde générale : **y = A · sin(ω t + φ)** — amplitude A, pulsation ω, déphasage φ

Note:
Le déphasage est l'outil le plus rentable en game feel : dix pièces qui
flottent avec le même A et ω mais un φ différent ne bougent pas à l'unisson.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/cercle_trigo_widget.html#onde" data-background-interactive -->

Note:
Onglet « Du cercle à l'onde ». Animer : la sinusoïde est la hauteur du
point qui tourne, tracée au fil du temps. Superposer cos — même courbe,
décalée d'un quart de tour. Puis les trois curseurs : A change la hauteur,
ω la vitesse (période 2π/ω affichée), φ décale la courbe au départ.
Finir sur le code du panneau : c'est littéralement un bonus qui flotte.

Repli : ouvrir 00 widgets/_widgets/cercle_trigo_widget.html#onde.

---

## Tourner en rond, en code

Un point sur un cercle de rayon r, de centre C, à l'angle θ :

```cpp
x = C.x + r * std::cos(theta);
y = C.y + r * std::sin(theta);
```

- faire varier θ avec le temps : **orbite** (ω = vitesse angulaire en rad/s)
- ne garder que y : **flottement**, respiration, bobbing de caméra
- r différents en x et en y : **ellipse**

Note:
Attention au sens : anti-horaire en maths, mais dans un repère écran où y
descend, le même code tourne en sens horaire. Faire le test en live si le
temps le permet.

---

# Identités pythagoriciennes
<!-- .slide: class="title" -->

---

## cos² + sin² = 1

M(cos θ, sin θ) est sur le cercle de rayon 1 : Pythagore dans le triangle O, M, projeté de M.

```
cos² θ + sin² θ = 1
```

En divisant par cos² θ, puis par sin² θ :

```
1 + tan² θ = 1 / cos² θ
1 + 1 / tan² θ = 1 / sin² θ
```

Note:
La première est la seule à retenir absolument ; les deux autres se
retrouvent en une ligne. Notation : cos² θ signifie (cos θ)², pas cos(cos θ).

---

## À quoi ça sert

- retrouver l'un à partir de l'autre, au signe près : cos θ = ±√(1 − sin² θ)
- (cos θ, sin θ) est **toujours** de longueur 1 : c'est un vecteur direction tout fait
- contrôle en debug : si cos² + sin² s'éloigne de 1, une rotation a dérivé

```cpp
Vec2 dir{ std::cos(angle), std::sin(angle) };   // déjà normalisé
```

Note:
Le signe se lit sur le cercle, pas dans la formule : c'est la seule
difficulté. Transition vers le bloc Géométrie vectorielle : (cos θ, sin θ)
est le vecteur unitaire d'angle θ, qu'on retrouvera à GVM-01.

---

## À vous

1. Convertir 150° en radians, et 5π/4 en degrés.
2. Donner cos et sin de 210° sans calculatrice.
3. Un objet flotte avec y = 0,5 · sin(2t). Quelle hauteur maximale, et combien de secondes pour un aller-retour ?
4. sin θ = 0,6 avec θ dans le quadrant II : que vaut cos θ ?

Note:
Corrigé : (1) 150 × π/180 = 5π/6 ; 5π/4 × 180/π = 225°. (2) 210° = π + 30° :
cos = −√3/2, sin = −1/2. (3) amplitude 0,5 ; période 2π/2 = π ≈ 3,14 s.
(4) cos² = 1 − 0,36 = 0,64, quadrant II donc cos < 0 : cos θ = −0,8
(triangle 3-4-5 de TRG-01).


---

## À retenir

- **SOH CAH TOA** — et ces rapports ne dépendent que de l'angle (similitude)
- tour = 360° = **2π rad** = 1 ; le code travaille en **radians**
- sur le cercle unité, **M = (cos θ, sin θ)** : les signes se lisent par quadrant
- valeurs remarquables : √0/2 … √4/2, retrouvées par le demi-carré et le demi-équilatéral
- symétries : cos pair, sin impair ; **cos θ = sin(θ + π/2)**
- **cos² θ + sin² θ = 1** : Pythagore sur le cercle

---

## Pour aller plus loin

- Séance précédente : [[01 courses/slides/Theory/TC-FT-TRG-01 - Géométrie du triangle|TC-FT-TRG-01 - Géométrie du triangle]]
- Séance suivante : [[01 courses/lectures/Theory/TC-FT-TRG-03 - Résolution de triangles et applications|TC-FT-TRG-03 - Résolution de triangles et applications]]
- Widget : [Cercle trigonométrique](https://studioalbert.github.io/widgets/_widgets/cercle_trigo_widget.html)
- Lengyel, *Mathematics for 3D Game Programming*, annexe B §B.1–B.3
- [Cercle trigonométrique — Wikipédia](https://fr.wikipedia.org/wiki/Cercle_trigonom%C3%A9trique)
