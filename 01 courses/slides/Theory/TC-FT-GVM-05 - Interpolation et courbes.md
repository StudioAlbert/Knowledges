---
title: TC-FT-GVM-05 - Interpolation et courbes
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Géométrie Vectorielle et Matricielle
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: online
---

# Interpolation et courbes
<!-- .slide: class="title" -->

### Entre A et B, tout se joue dans la courbe

<small>TC-FT-GVM-05 · Géométrie Vectorielle et Matricielle</small>

Note:
Tout ce qui bouge sans être piloté à la main est une valeur qui passe d'un point
à un autre en un certain temps. On regarde d'abord la fonction brute, puis ce
qu'il faut lui ajouter pour qu'elle serve.

---

## Objectifs

À la fin de la séance, vous savez :

- écrire un **Lerp** et lui fabriquer son paramètre
- **normaliser** un temps, et dire pourquoi on le clampe
- choisir entre une fonction **bornée**, **cyclique** ou **en dents de scie**
- dire pourquoi on n'interpole **pas** des angles d'Euler

**Prérequis :** [[01 courses/slides/Theory/TC-FT-GVM-01 - Vecteurs et repères|TC-FT-GVM-01]].

---

# Une valeur qui change
<!-- .slide: class="title" -->

---

## Animer, c'est faire varier une valeur
<!-- .slide: class="schema" -->

![[117-lovely-barley-1-brawl-stars-acegif.gif]]

---

## L'animateur le fait à la main
<!-- .slide: class="schema" -->

Un cycle de marche : des poses clés, et le temps qui passe entre elles.

![[gvm05_cycle_marche.png]]

Note:
Contact, down, passing position, up — puis on recommence. L'animateur pose les
extrêmes et laisse le logiciel remplir entre les deux. C'est *exactement* ce
qu'on va écrire en code.

---

## Aller de A à B

La fonction la plus simple qui monte avec le temps :

```
y = a · t + b
```

Elle marche — et elle ne s'arrête **jamais**. Rien, dans la formule, ne la
retient entre A et B.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/fonctions_temps_widget.html#droite" data-background-interactive -->

Note:
Monter `a` et laisser tourner : la bille quitte la piste avant la fin du temps.
C'est le défaut de la fonction brute, et toute la séance consiste à y répondre.

---

## Clamp ou cycle : il faut choisir

Une fonction du temps qui sert dans un jeu est **toujours** bornée. Deux façons :

- **borner l'entrée** — on clampe `t` entre 0 et 1, la valeur s'arrête à B
- **borner la sortie** — on prend une fonction qui revient toute seule

Le choix n'est pas technique : *l'animation doit-elle finir, ou tourner ?*

---

## Cas du clip d'animation
<!-- .slide: class="schema" -->

Une courbe d'animation dans Unity : des clés, et une interpolation entre elles.

![[gvm05_courbe_unity.png]]

Note:
Les tangentes aux clés décident de la forme entre deux poses. C'est le même
sujet que les courbes d'easing de la fin de séance, posé dans l'éditeur au lieu
du code.

---

# Boucler
<!-- .slide: class="title" -->

---

## La fonction cyclique

```
y = A · sin(ω · t + φ)
```

- **A** l'amplitude — jusqu'où ça monte
- **ω** la vitesse — période `T = 2π / ω`
- **φ** la phase — le décalage au démarrage

Elle reste bornée **toute seule**, pour toujours : flottement, pulsation, respiration.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/fonctions_temps_widget.html#cyclique" data-background-interactive -->

Note:
Changer φ sans toucher à ω : la courbe glisse, sa forme ne bouge pas. C'est
comme ça qu'on décale deux objets identiques pour casser l'effet « tout le
monde en rythme ».

---

## La fonction scie

```
y = t/T − ⌊t/T⌋              std::fmod(t, T) / T
```

Elle monte de 0 à 1, puis **retombe d'un coup** : c'est la partie décimale du temps.

- une barre qui se remplit en boucle, un défilement de texture, un cycle de jour
- le saut est **voulu** — mais interdit pour une position

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/fonctions_temps_widget.html#scie" data-background-interactive -->

Note:
Réduire la période : la bille repart plus souvent au point A. Montrer le bond
au raccord, et demander où ce bond serait inacceptable.

---

# Interpoler
<!-- .slide: class="title" -->

---

## Interpolation linéaire

```
Lerp(A, B, t) = A + (B − A) · t
```

- `t = 0` → on est en **A** &nbsp;·&nbsp; `t = 1` → on est en **B**
- entre les deux, on avance **proportionnellement**
- `Lerp` ne connaît pas le temps : il attend un `t` **déjà normalisé**

---

## Normaliser le temps

Tout le travail est de **fabriquer ce paramètre** :

```
t = temps écoulé / durée voulue        puis clamp(t, 0, 1)
```

Sans le clamp, `t` dépasse 1 et la valeur dépasse B — exactement le problème de
la droite du début.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/fonctions_temps_widget.html#lerp" data-background-interactive -->

Note:
Décocher le clamp et laisser tourner : la bille continue au-delà de B. Remettre
le clamp : elle s'arrête et reste. C'est la différence entre `Lerp` et
`LerpUnclamped`.

---

## Lerp en C++

```cpp
float Lerp(float a, float b, float t)
{
    return a + (b - a) * t;
}

// une porte qui s'ouvre en 1,5 seconde
ecoule += dt;
const float t = std::clamp(ecoule / 1.5f, 0.0f, 1.0f);
porte.angle = Lerp(0.0f, 90.0f, t);
```

Note:
Trois lignes, dont une seule de maths. Tout le reste de la séance consiste à
remplacer le `t` de la dernière ligne par une **courbe** de `t`.

---

## Interpoler quoi

Tout ce qui **s'additionne et se multiplie** :

- des **positions**, des échelles
- des **couleurs**, canal par canal
- des **volumes** sonores, des opacités

Les **angles**, eux, méritent une précaution — et c'est la suite.

---

# Tourner
<!-- .slide: class="title" -->

---

## Tourner en 2D

Un seul angle, et deux lignes :

<p class="formule">x' = x·cos θ − y·sin θ &nbsp;&nbsp;&nbsp; y' = x·sin θ + y·cos θ</p>

Un angle s'interpole **sans problème** : il n'y a qu'un nombre, et un seul
chemin de l'un à l'autre — à la question du sens près.

---

## Tourner en 3D

En 3D, il faut **trois** angles : lacet (`y`), tangage (`x`), roulis (`z`).

Mais trois nombres ne suffisent pas à décrire une orientation : il faut aussi
dire **dans quel ordre** on les applique.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/quaternion_widget.html#ordre" data-background-interactive -->

Note:
Mêmes angles, deux ordres d'application, deux orientations. Unity applique Z,
puis X, puis Y ; d'autres moteurs font autrement. Un triplet copié d'un moteur
à l'autre ne donne pas la même pose.

---

## Le gimbal lock

À **90°** de tangage, l'axe du lacet et celui du roulis se retrouvent dans le
même plan.

- les deux commandes tournent alors **autour du même axe**
- il ne reste que **deux** libertés sur trois
- ce n'est pas un bug : c'est une limite des angles d'Euler eux-mêmes

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/quaternion_widget.html#gimbal" data-background-interactive -->

Note:
Bouton « Mettre le tangage à 90° », puis bouger lacet et roulis : le panneau
mesure que l'un annule exactement l'autre. Le degré de liberté perdu se voit
sur les anneaux, devenus coplanaires.

---

## Le quaternion

Quatre nombres qui portent **un axe et un angle**, et rien d'autre.

<p class="formule">q = (x, y, z, w) &nbsp;&nbsp; avec ‖q‖ = 1</p>

- pas d'ordre à choisir : une orientation, une valeur
- pas de gimbal lock : aucun axe ne peut en manger un autre
- `q` et `−q` décrivent la **même** rotation — par les deux sens du tour

---

## Interpoler deux orientations

`Slerp` suit le **plus court arc** sur la sphère des rotations, à vitesse constante.

- interpoler des **angles** fait passer par des poses que personne n'a demandées
- `Quaternion.Slerp` en Unity, `FQuat::Slerp` en Unreal
- en pratique : on **stocke** des quaternions, on **affiche** des angles d'Euler

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/quaternion_widget.html#slerp" data-background-interactive -->

Note:
Animer : les deux cubes partent du même endroit et arrivent au même endroit,
mais le chemin n'a rien à voir. Celui de gauche part en vrille, celui de droite
tourne droit.

---

# Les courbes
<!-- .slide: class="title" -->

---

## Le mouvement linéaire ne trompe personne

Une vitesse constante du début à la fin donne cette sensation de **tiroir
mécanique** : rien, dans la nature, ne démarre et ne s'arrête d'un coup.

La réponse tient en une ligne : on remplace `t` par **une courbe de `t`**.

```
Lerp(A, B, courbe(t))
```

---

## Quatre courbes, quatre sensations
<!-- .slide: class="schema" -->

Les instants sont réguliers ; c'est l'espacement des points qui se voit à l'écran.

![[gvm05_easing.svg]]

Note:
Lire la figure de droite d'abord : on y voit directement la sensation. La courbe
de gauche n'est que la règle qui produit cet espacement. Faire deviner à la
classe quelle bande va avec quelle courbe avant d'afficher les couleurs.

---

## Smooth start, smooth stop

```
smoothStart(t) = t²            smoothStop(t) = 1 − (1 − t)²
```

- **smooth start** : part lentement, finit vite — une chute, une accélération
- **smooth stop** : part vite, finit lentement — un arrêt, un amorti
- la puissance règle la force de l'effet : `t³` démarre encore plus mou

---

## Smoother step

```
smootherStep(t) = t² · (3 − 2t)
```

Une courbe en **S** : elle démarre au repos **et** finit au repos.

C'est le passe-partout des interfaces — un panneau qui s'ouvre, une caméra qui
se recale, une valeur qui se corrige.

---

## Smooth arch

```
smoothArch(t) = 4 · t · (1 − t)
```

Elle monte puis **redescend** : à `t = 0` et `t = 1` elle vaut 0, au milieu 1.

Un saut, un pop d'icône, un flash de dégât — tout ce qui doit revenir d'où il
vient.

---
## À retenir

- un paramètre **normalisé**, une valeur de départ, une d'arrivée, et une courbe
- **clamper** l'entrée ou **boucler** la sortie : il faut choisir, toujours
- on interpole ce qui s'additionne — **pas** des angles d'Euler
- en 3D : on **stocke** des quaternions, on **affiche** des angles

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/Theory/TC-FT-GVM-03 - Matrices et transformations|TC-FT-GVM-03]] — ranger une rotation, une translation et une échelle dans un seul objet.</small>
