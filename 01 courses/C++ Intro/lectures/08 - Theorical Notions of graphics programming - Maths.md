---
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Introduction to maths
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Notions théoriques pour la programmation graphique

<small>Sébastien Albert · Module 4FSC0PF001</small>

Note:
Le plus long deck du module, en quatre temps : géométrie et vecteurs,
fonctions et courbes d'easing, représentation des nombres en machine, et
enfin probabilités et statistiques. Chaque partie peut se traiter
séparément.

---

## Source
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine, marquée « (Temp) » (contient les graphes et schémas non transposés) :

- 🔗 [Google Slides — 08 Theorical Notions of graphics programming / Maths](https://docs.google.com/presentation/d/1MyyUSkqldoEikta8TUQdn0hG3AnSXnd81yfQcC0hGMc/edit)

Exercices : [[Exercices - 08 - Introduction to Maths]]

</div>

---

# Géométrie et vecteurs
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Number sets
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

| Ensemble | Contenu |
|:-:|---|
| **ℕ** Natural | unsigned positive integers (0, 1, …) |
| **ℤ** Integer | signed integers (…, −1, 0, 1, …) |
| **ℚ** Rational | ½, −⅔ |
| **ℝ** Real | π, e, √2 |

---

## Basic geometry
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Let's look at basic geometric facts that might be useful later on.

---

## Pythagore
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Given a right triangle :

- **a** and **b** : sides
- **c** : hypotenuse

```
a² + b² = c²
```

---

## Trigonometry
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Given a right triangle with angle **α** at vertex A :

- hypotenuse : `c`
- adjacent : `b`
- opposite : `a`

```
sin(α) = opp / hyp
cos(α) = adj / hyp
tan(α) = opp / adj
```

Angle at vertex B : **β = 90 − α**

---

## Angle unit
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- **Degree** — 0° à 360°, dans le sens antihoraire
- **Radian** — 0 à 2π

Les fonctions de trigonométrie de la STL C++ **et** d'Unity utilisent les **radians** !

Dans Neko Engine, vous pouvez utiliser des fonctions `Sin` et `Cos` spécifiques qui prennent des degrés ou des radians.

---

## Vectors !
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Vectors are defined by :

- a **magnitude** (a length)
- a **direction**
- a **position**

Différence entre *speed* et *velocity*.

⚠ Pas de multiplication ni de division entre vecteurs — uniquement avec des floats !

---

## Magnitude
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Using Pythagoras' formula, we can find the length of a vector.

Vector2 example :

```
(3, 4) => sqrt(3² + 4²) = sqrt(9 + 16) = sqrt(25) = 5
```

---

## Lerp
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

I want to go from point A to point B with `t = 0..1` :

```
Result = Lerp(A, B, t)
```

→ hint : vous pouvez utiliser les **easing functions** pour changer la linéarité de `t` ;)

---

## Projection
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Exemple : dans un jeu de course, comment savoir qui est premier et qui est dernier ? On **projette** la position sur le tracé et on compare les valeurs.

<small>[Unity — Vector3.Project](https://docs.unity3d.com/ScriptReference/Vector3.Project.html)</small>

---

## Reflection
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Étant donnée une **normale**, on calcule facilement la réflexion d'un vecteur d'entrée — ce n'est pas toujours un vecteur perpendiculaire.

<small>[Unity — Vector3.Reflect](https://docs.unity3d.com/ScriptReference/Vector3.Reflect.html)</small>

---

## Rotation in 2D space
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

En 2D, l'axe de rotation est l'axe **z**. Pour un angle α :

```
x2 = cos(α) * x1 − sin(α) * y1
y2 = sin(α) * x1 + cos(α) * y1
```

---

## Rotation in 3D space
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

En 3D, on utilise les **quaternions** — des objets mathématiques complets et bizarres. On peut générer un quaternion depuis des angles d'Euler, ou depuis un axe et un angle.

<small>[Quaternion.AngleAxis](https://docs.unity3d.com/ScriptReference/Quaternion.AngleAxis.html) · [Quaternion.Euler](https://docs.unity3d.com/ScriptReference/Quaternion.Euler.html)</small>

---

## Vector 2 — perpendicular
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Il y a **2** vecteurs perpendiculaires à tout vecteur non nul.

```
V   = ( x,  y)
V'  = ( y, -x)
V'' = (-y,  x)
```

---

## Vector 3 — perpendicular
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

En 3D, il y a une **infinité** de vecteurs perpendiculaires à un vecteur donné.

Étant donnés **deux** vecteurs non colinéaires, il y en a deux — obtenus par le **produit vectoriel** (cross product).

---

# Fonctions et courbes
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Let's talk about math functions
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
f(x) = 3x² + 4x − 7
```

- on a `x` en entrée, et la sortie `f(x)` ou `y` ; en traçant la courbe, on voit les valeurs
- plusieurs `x` peuvent donner le même `y`, mais il n'y a **qu'un seul** `y` pour chaque `x`
- on les implémente facilement en C++ : [godbolt.org/z/WK1j6f](https://godbolt.org/z/WK1j6f)

---

## First degree function
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Ces fonctions sont des **droites**.

```
f(x) = 3x
f(x) = -4x + 1
f(x) = -4
```

Ou simplement : `f(x) = ax + b`, où **a** est la pente et **b** la valeur de `y` en `x = 0`.

Autre nom : **polynôme linéaire**.

---

## Second degree function
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Ces fonctions sont des **paraboles**.

```
f(x) = 3x²
f(x) = -4x² + 1
f(x) = x² + 2x - 4
```

Ou simplement : `f(x) = ax² + bx + c`, où **a** définit si la parabole s'ouvre vers le haut ou vers le bas, et **c** est la valeur de `y` en `x = 0`.

---

## Square root
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
f(x) = √x = x^0.5
```

C'est l'inverse de la fonction quadratique.

---

## Sinus et cosinus
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

On les a découverts avec la trigonométrie, mais ils ont aussi des caractéristiques d'**onde**.

Vous connaissez sûrement des ennemis qui se déplacent en sinusoïde !

---

## Parametric function
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Given `t = [0..2π]` :

```
X = r * sin(t)
Y = r * cos(t)
```

Ou :

```
X² + Y² = r²
```

---

## Absolute value
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Peut servir à faire rebondir une balle, en combinaison avec une sinusoïde.

---

## Clamp
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
function clamp(x, min, max):
    if (x < min) then
        x = min
    else if (x > max) then
        x = max
    return x
```

Vous pouvez utiliser cette fonction quand vous ne voulez pas que votre personnage sorte du niveau.

---

## (Inbe)tweening ou easing functions
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Le *tweening* est un terme d'animation, mais on peut utiliser des fonctions pour adoucir un mouvement ou un comportement — **parce que le linéaire, c'est moche !**

<small>[Vidéo de référence](https://www.youtube.com/watch?v=mr5xkf6zSzk)</small>

---

## Normalizing
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Les fonctions 1D qui nous intéressent ont `x = [0..1]` et `y = [0..1]`.

Il est alors facile de simplement multiplier par la valeur que l'on veut.

---

## SmoothStart
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

On ne veut pas démarrer d'un coup : on veut une accélération douce au début — c'est-à-dire une tangente **horizontale** au départ, au lieu d'être directement diagonale.

---

## SmoothStop
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Même chose, mais on veut finir doucement.

---

## Smooth(er)Step
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```
Smoothstep   : f(x) = 3x² − 2x³              x = [0, 1]
Smootherstep : f(x) = 6x⁵ − 15x⁴ + 10x³      x = [0, 1]
```

Ou en mélangeant **smoothstart** et **smoothstop**.

---

## SmoothArch
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Smooth start **et** smooth stop, mais en faisant un aller-retour.

---

## Other curves
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Vous voudrez peut-être implémenter d'autres types de courbes spécifiques :

- Bézier curves
- Catmull-Rom curves
- Hermite splines
- …

---

# Les nombres en machine
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Number notations
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Le système Hindou-Arabe compte en **base 10** — probablement parce que nous avons 10 doigts.

```
196 = 1*10² + 9*10¹ + 6*10⁰
```

Cependant :

- les Chepang, au Népal, utilisent un système en **base 12** (plus facile à diviser par 2, 3, 4, 6)
- la numération **maya** est en base 20
- les Babyloniens utilisaient une numération en base 60

---

## Comment un nombre est implémenté dans l'ordinateur
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

À cause de l'électronique, les ordinateurs stockent beaucoup de valeurs en 0 et 1.

`196`, en integer 32 bits :

```
Big-Endian    : 00000000 00000000 00000000 11000100
Little-Endian : 11000100 00000000 00000000 00000000
                (probablement votre ordinateur)
```

| Déc | Bin | Déc | Bin |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 8 | 1000 |
| 1 | 1 | 9 | 1001 |
| 2 | 10 | 10 | 1010 |
| 3 | 11 | 11 | 1011 |
| 4 | 100 | 12 | 1100 |
| 5 | 101 | 13 | 1101 |
| 6 | 110 | 14 | 1110 |
| 7 | 111 | 15 | 1111 |

---

## Hexadecimal
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Le binaire est souvent encombrant, donc en informatique on aime bien l'**hexadécimal** :

```
196 = 0xC4 = 12*16¹ + 4*1
```

Le passage de l'hexadécimal au binaire est immédiat :

```
0xC4 :  C = 1100 , 4 = 0100  ->  1100'0100
```

**Un chiffre hexadécimal représente exactement 4 chiffres binaires !**

---

# Probabilités et combinatoire
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Probability and combinatorics basics
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**The first rule of probability is that your intuition is wrong !**

---

## Combinatorics
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Calculer le nombre de possibilités.

Combien de possibilités pour un dé, pour deux dés, … ?

---

## Permutations sans répétition
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Le nombre de possibilités de mettre 6 balles de couleurs différentes dans 6 boîtes ordonnées :

```
6 × 5 × 4 × 3 × 2 × 1 = 720

soit 6! = 720
```

---

## Permutations avec répétition
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Un mot de passe alphanumérique : `a-z0-9`, soit 26 lettres + 10 chiffres = **36**.

Mot de passe de 5 caractères (exemple : `a4fz1`) :

```
36⁵ = 60 466 176 possibilités
```

---

## Combinaison sans répétition
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Étant donnés 40 étudiants en game art, les répartir en 2 classes — ou choisir 20 étudiants parmi 40 :

```
C(40, 20) = 40! / (20! × (40−20)!)
```

---

## Combinaison avec répétition
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Combien de pièces de domino existe-t-il ?

On a 7 éléments `{blanc, 1, 2, 3, 4, 5, 6}`, pris 2 par 2 : **28**.

---

## Probability basics — la pièce
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Quelle est la probabilité d'obtenir pile sur une pièce suisse ?

2 possibilités : *heads*, *tails* ⇒ **une possibilité sur deux**.

---

## Probability basics — le dé
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Quelle est la probabilité d'obtenir un « 6 » sur un dé ?

6 possibilités : 1, 2, 3, 4, 5, 6 ⇒ **une possibilité sur six**.

---

## Probability basics — deux piles d'affilée
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Quelle est la probabilité d'avoir deux fois pile d'affilée ?

4 possibilités :

```
heads, heads
tails, tails
heads, tails
tails, heads
```

⇒ **une possibilité sur quatre**.

---

## Probability basics — la même classe
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Deux amis A et B rejoignent SAE Institute en Game Art, avec 38 autres étudiants répartis en deux classes. Quelle est la probabilité qu'ils finissent dans la même classe ?

- nombre total de possibilités : choisir 20 étudiants parmi 40
- ils sont ensemble dans une classe : choisir 18 parmi 38
- il y a l'autre classe : doubler le résultat précédent

```
2 × C(38,18) / C(40,20) = 19/39     ... et NON 1/2
```

Note:
C'est l'illustration de la première règle : l'intuition dit 1/2, la
combinatoire dit 19/39. L'écart est petit, mais il est réel, et il vient
du fait que A occupe déjà une des 20 places de sa classe.

---

## Probability basics — les anniversaires
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Quelle est la probabilité que deux personnes de cette classe aient le même anniversaire (jour et mois) ?

---

## Probability basics — probabilité conditionnelle
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Quelle est la probabilité d'avoir deux piles d'affilée, **sachant qu'on a déjà fait pile** ?

2 possibilités :

```
tails, tails
tails, heads
```

⇒ **une possibilité sur deux**.

---

## Théorème de Bayes
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

La probabilité de A sachant B est la probabilité de B sachant A, multipliée par la probabilité de A, divisée par la probabilité de B.

```
P(A|B) = P(B|A) × P(A) / P(B)
```

---

# Statistiques
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Statistics
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Les ingénieurs utilisent les données pour prendre des décisions, et il vous faut des outils pour analyser ces données.

Vous en aurez besoin pour votre travail de bachelor, et si vous décidez de développer votre jeu en vous appuyant sur des analytics.

---

## Expected value
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Ou *average*, ou *expectation*, ou *mean*.

On somme les valeurs, on divise par la taille de l'échantillon.

L'*expected value* est la valeur que l'on peut en moyenne attendre.

---

## Variance
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Mesure à quel point un ensemble de nombres est dispersé autour de sa valeur moyenne.

C'est le **carré** de l'écart-type (*standard deviation*).

---

## Median
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Une valeur séparant la moitié haute de la moitié basse d'un échantillon.

C'est une valeur utile, parce que les moyennes sont très sensibles aux extrêmes, contrairement à la médiane.

Parfois, médiane et *expected value* coïncident.

---

## Statistics test
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Le problème des petits échantillons, c'est que les moyennes partent dans tous les sens.

Les statistiques, c'est essentiellement : étant donné un échantillon, que peut-on dire ?

<small>[Vidéo de référence](https://www.youtube.com/watch?v=fl9V0U2SGeI)</small>

---

## Student's t-test
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Prenons un exemple : le temps de build de votre projet sur SSD versus sur HDD. Est-ce **statistiquement** plus rapide de builder sur SSD ?

Comme on fait la même chose (builder le même projet dans deux configurations), ça ressemblera à une distribution normale — mêmes moyennes, avec des variations. On peut donc utiliser le t-test de Student contre l'hypothèse nulle : « le build sur SSD n'est pas plus rapide ».

---

## Student's t-test — en pratique
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

1. On définit **p**, la probabilité que l'hypothèse nulle soit vraie (par exemple 5 %).
2. Dans Excel, on fait un « t-Test: Two-Sample Assuming Unequal Variances » (en français : *Test d'égalité des espérances : deux observations de variances différentes*).
3. Cela sort beaucoup de nombres ; celui qui nous intéresse est **`P(T<=t) two-tail`** (*P(T<=t) bilatéral*).
4. S'il est inférieur à notre **p**, nous avons raison !

---

## Difference of means
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

On a montré que les populations sont différentes, mais pas **à quel point**.

Ce qui nous intéresse, c'est la différence des moyennes — mais elle a une marge d'erreur. Il nous faut l'**intervalle de confiance** (macro personnalisée).

On peut alors utiliser ces nombres pour savoir si la différence est **pratiquement** significative, et pas simplement **statistiquement** significative.

Si l'intervalle chevauche 0 (5 ± 10, par exemple), c'est que la différence n'est pas significative.

---

## Un exemple plus concret côté jeu
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Vous travaillez sur votre jeu mobile, avec un mode de jeu spécifique. On veut tester si les joueurs jouent davantage quand on baisse la difficulté. Problème : le temps de jeu part dans tous les sens (1 h par semaine pour certains, 10 h pour d'autres).

On peut faire de l'**A/B testing** : le groupe A teste la version facile puis la difficile, le groupe B teste la difficile puis la facile.

On calcule ensuite les différences pour chaque joueur, et on obtient une belle distribution normale de différences.

---

## Comment utiliser le t-test correctement
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- si **des personnes différentes** sont assignées à la version A et à la version B → test *two-sample*, non apparié
- si **les mêmes personnes** jouent la version A, puis la B → test **apparié** (*paired test*)

---

## Binary outcomes
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- **Relative risk** (*risk ratio*) : « les fumeurs ont 4× plus de risques de prendre feu que les non-fumeurs ». Tend à magnifier de petites différences absolues.
- **Two-sample z-test** (*difference of proportions*) : « la part de marché a monté de 5 %, de 20 % à 25 % ».

---

## Mann-Whitney test
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Deux versions différentes d'un puzzle, chronométrées avec des testeurs différents (cette fois, pas les mêmes testeurs).

La distribution est **non normale** : il faut alors utiliser le test de Mann-Whitney.

---

## Conclusion
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Les maths sont votre **outil**. Comme tout outil, vous n'avez pas toujours besoin de savoir comment il est fabriqué, mais vous devez savoir…

Note:
La diapo de conclusion est tronquée dans l'export Drive — la phrase
s'arrête au milieu. Se référer à la présentation d'origine pour la fin.
