---
title: TC-FT-GVM-02 - Produits scalaire et vectoriel
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

# Produits scalaire et vectoriel
<!-- .slide: class="title" -->

### Deux opérations, et la moitié des questions du gameplay

<small>TC-FT-GVM-02 · Géométrie Vectorielle et Matricielle</small>

Note:
Suite directe de GVM-01. On sait additionner, soustraire, normaliser. Reste la
question qu'on a laissée de côté : peut-on *multiplier* deux vecteurs ? Il y a
deux réponses, et chacune répond à une famille de questions du jeu.

---

## Objectifs

À la fin de la séance, vous savez répondre par un produit :

- **devant ou derrière ?** et **sous quel angle ?** — produit scalaire
- **à gauche ou à droite ?** — produit vectoriel
- **projeter** un vecteur sur un autre, et faire **rebondir**
- trouver la **normale** d'une surface

**Prérequis :** [[01 courses/slides/Theory/TC-FT-GVM-01 - Vecteurs et repères|TC-FT-GVM-01]].

---

# Multiplier deux vecteurs ?
<!-- .slide: class="title" -->

---

## AB × BC ?

On sait faire `AB + BC` et `3 × AB`. Mais `AB × BC` ?

```
(3, 1) × (1, 2) = ?
```

Multiplier composante par composante — `(3, 2)` — ne **veut rien dire** : le
résultat ne répond à aucune question de géométrie.

Note:
Laisser la classe proposer. Le produit composante par composante existe
(Unity l'appelle `Vector3.Scale`), mais il sert à mettre à l'échelle, pas à
mesurer une relation entre deux directions. La vraie question : qu'est-ce
qu'on *veut* savoir de deux vecteurs ?

---

## Deux produits, deux réponses

| Ce qu'on veut savoir | L'opération | Le résultat |
| --- | --- | --- |
| à quel point ils sont **d'accord** | produit **scalaire** `u · v` | un **nombre** |
| ce qui leur est **perpendiculaire** | produit **vectoriel** `u × v` | un **vecteur** |

Toute la séance tient dans ces deux lignes.

---

# Le produit scalaire
<!-- .slide: class="title" -->

---

## Définition et méthode de calcul

Composante par composante, puis on additionne **tout** :

<p class="formule">u · v = u<sub>x</sub>·v<sub>x</sub> + u<sub>y</sub>·v<sub>y</sub> &nbsp;&nbsp;&nbsp;(+ u<sub>z</sub>·v<sub>z</sub> en 3D)</p>

```
(3, 1) · (1, 2) = 3×1 + 1×2 = 5
```

Le résultat est **un seul nombre**. Il n'a pas de direction, pas d'unité de
longueur : c'est un **scalaire**, d'où son nom.

---

## La seconde écriture

La même valeur s'écrit aussi avec l'angle entre les deux vecteurs :

```
u · v = ‖u‖ · ‖v‖ · cos θ
```

- la première écriture **se calcule** (deux multiplications, une addition)
- la seconde **s'interprète** : elle dit ce que le nombre signifie
- les deux sont égales — c'est ce qui rend le produit scalaire utile

Note:
Ne pas démontrer l'égalité : la poser, et la vérifier sur un exemple au
tableau. C'est le pont entre « des nombres » et « un angle ».

---

## Le produit scalaire en C++

```cpp
float Dot(Vector2 a, Vector2 b)
{
    return a.x * b.x + a.y * b.y;
}

// l'ennemi est-il devant le garde ?
const Vector2 versEnnemi = Soustraire(ennemi, garde);

if (Dot(regard, versEnnemi) > 0.0f)
{
    std::println("Il est devant moi.");
}
```

---

## Le signe suffit souvent

`cos θ` change de signe à 90° — donc le produit scalaire aussi.

- **positif** → moins de 90° : la cible est **devant**
- **nul** → exactement 90° : elle est **sur le côté**
- **négatif** → plus de 90° : elle est **derrière**

Trois réponses pour deux multiplications et une addition, sans aucune racine
ni trigonométrie.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/produit_scalaire_widget.html#scalaire" data-background-interactive -->

Note:
Faire tourner v autour de u et regarder le signe basculer pile à 90°. Cocher
« les trois zones » pour colorer le demi-plan devant et le demi-plan derrière.

---

## Cas particulier : perpendiculaires

```
u · v = 0     ⟺     u ⊥ v
```

C'est **le** test d'orthogonalité, et il ne coûte rien.

- pas de norme à calculer, pas d'angle à extraire
- il marche en 2D comme en 3D, sans rien changer
- attention aux flottants : tester `|u · v| < epsilon`, jamais `== 0.0f`

Note:
Lien avec RNLB-03 : deux vecteurs calculés ne donneront presque jamais un
produit scalaire exactement nul. L'epsilon n'est pas une coquetterie.

---

## Cas particulier : colinéaires

Deux vecteurs **colinéaires** portent la même droite : l'un est un multiple de
l'autre, `v = k · u`.

```
θ = 0°   →  u · v = +‖u‖·‖v‖        (même sens)
θ = 180° →  u · v = −‖u‖·‖v‖        (sens opposé)
```

Le produit scalaire est alors **maximal en valeur absolue** — mais pour
*tester* la colinéarité, il faudrait comparer à deux normes. L'autre produit
le fait en une soustraction.

Note:
C'est la transition vers le produit vectoriel : `u × v = 0` teste la
colinéarité directement, comme `u · v = 0` teste la perpendicularité.
Deux produits, deux tests, symétriques.

---

## Retrouver l'angle — et pourquoi on l'évite

```
cos θ = (u · v) / (‖u‖ · ‖v‖)      θ = acos(…)
```

- deux racines carrées **et** un `acos` : cher, pour une information rarement utile
- un cône de vision se teste en **comparant des cosinus**, pas des angles
- `acos` hors de `[−1, 1]` à cause des flottants rend `NaN` : borner avant

Note:
Règle de métier : si la question est « est-ce que l'angle est inférieur à X »,
on compare `cos θ` à `cos X` calculé une fois. On ne convertit en degrés que
pour l'afficher à un humain.

---

# Projeter et réfléchir
<!-- .slide: class="title" -->

---

## Projeter : l'ombre de u sur v

La projection est l'**ombre** de `u` sur la droite portée par `v`.

```
proj = ( (u · v) / ‖v‖² ) · v
```

- le facteur est un nombre : **combien de v** il faut pour atteindre l'ombre
- négatif, l'ombre tombe **derrière** l'origine
- aucun angle, aucune trigonométrie : deux produits scalaires

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/produit_scalaire_widget.html#projection" data-background-interactive -->

Note:
Faire tourner u : l'ombre glisse le long de v, et la composante ⊥ reste
perpendiculaire. Montrer dans le panneau que `u∥ · u⊥` reste nul.

---

## La composante orthogonale

Tout vecteur se découpe en deux morceaux, et un seul découpage marche :

<p class="formule">u = u<sub>∥</sub> + u<sub>⊥</sub> &nbsp;&nbsp;&nbsp; u<sub>⊥</sub> = u − u<sub>∥</sub></p>

- **u<sub>∥</sub>** est la projection : la part **le long de** v
- **u<sub>⊥</sub>** est la composante orthogonale : la part **perpendiculaire** à v
- ensemble, elles redonnent exactement `u`

C'est ce découpage qui permet de glisser le long d'un mur, et de rebondir.

Note:
Vocabulaire : l'anglais appelle u<sub>⊥</sub> le *vector rejection*, et la doc des
moteurs traduit souvent par « rejet ». Ce n'est pas du français géométrique :
on dit **composante orthogonale** (ou normale) de u par rapport à v. Le mot
« rejet » est à connaître pour lire la doc, pas à employer.

---

## Réfléchir : le rebond

Une balle qui tape un mur **retourne sa part perpendiculaire**, et garde l'autre.

```
r = d − 2 · (d · n) · n           avec ‖n‖ = 1
```

- `d` la direction d'arrivée, `n` la **normale** du mur
- la part le long du mur ne change pas → la balle glisse
- la part contre le mur s'inverse → la balle repart

Note:
Si on oublie de normaliser `n`, le facteur 2 n'est plus le bon et la balle
accélère ou s'écrase à chaque rebond. Bug classique de moteur maison.

---

# Le produit vectoriel
<!-- .slide: class="title" -->

---

## Deux vecteurs, un vecteur

Le produit vectoriel rend une direction **perpendiculaire aux deux**.

- il n'existe vraiment qu'en **3D** : en 2D on en garde un seul nombre
- sa **longueur** mesure l'aire du parallélogramme formé par `u` et `v`
- il n'est **pas commutatif** : `u × v = −(v × u)`

Note:
Le sens du résultat dépend de la main du repère : c'est exactement la règle
vue en GVM-01. Dans un repère gaucher, le vecteur sort de l'autre côté.

---

## Le calcul, en 3D et en 2D

<p class="formule">
3D : u × v = ( u<sub>y</sub>·v<sub>z</sub> − u<sub>z</sub>·v<sub>y</sub> , &nbsp; u<sub>z</sub>·v<sub>x</sub> − u<sub>x</sub>·v<sub>z</sub> , &nbsp; u<sub>x</sub>·v<sub>y</sub> − u<sub>y</sub>·v<sub>x</sub> )<br>
2D : u × v = u<sub>x</sub>·v<sub>y</sub> − u<sub>y</sub>·v<sub>x</sub> &nbsp;&nbsp; — un seul nombre
</p>

En 2D, c'est la **troisième composante** du produit 3D — les deux autres sont
nulles. Son signe porte toute l'information.

---

## À gauche ou à droite

```cpp
float Cross(Vector2 a, Vector2 b)
{
    return a.x * b.y - a.y * b.x;
}

const float cote = Cross(regard, versCible);

if      (cote > 0.0f) { std::println("à gauche"); }
else if (cote < 0.0f) { std::println("à droite"); }
else                  { std::println("alignée");  }
```

Le signe dit **dans quel sens tourner**. Zéro teste la colinéarité.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/produit_scalaire_widget.html#orientation" data-background-interactive -->

Note:
Déplacer la cible autour du garde : le signe bascule exactement sur la ligne de
regard. Élargir le cône et la portée pour montrer que « voir » demande les deux
produits — le scalaire pour l'angle et la distance, le vectoriel pour le côté.

---

## La normale d'une surface
<!-- .slide: class="schema" -->

Deux arêtes, un produit vectoriel, et on sait de quel côté le triangle regarde.

![[gvm02_normale_3d.svg]]

---

## Ce que l'ordre des sommets décide

<p class="formule">n = (B − A) × (C − A) &nbsp;&nbsp;&nbsp; puis n / ‖n‖</p>

- lire les sommets **dans l'autre sens** retourne la normale : `u × v = −(v × u)`
- un triangle qui tourne le dos à la caméra est **éliminé** : c'est le *backface culling*
- la normale sert ensuite à l'éclairage, aux collisions et au rebond

Note:
C'est pour ça qu'un modèle importé apparaît parfois « troué » : ses faces sont
décrites dans le mauvais sens, le moteur les jette, et on voit à travers.

---

## Aire

La **longueur** du produit vectoriel mesure une surface :

<p class="formule">‖u × v‖ = aire du parallélogramme porté par u et v</p>

- deux vecteurs colinéaires → parallélogramme aplati → aire **nulle**
- la moitié donne l'aire du **triangle** — celle d'une face de maillage
- c'est ce qui sert à pondérer les normales d'un sommet par la taille des faces

---

## Le produit mixte

**Trois** vecteurs partant du même point : `u` et `v` définissent une base, **`w` est le
troisième arête, celle qui donne l'épaisseur**.

<p class="formule">(u × v) · w</p>

1. `u × v` : un **vecteur** perpendiculaire à la base — sa norme est l'**aire** de cette base
2. `· w` : la projection de **`w`** sur cette perpendiculaire — c'est la **hauteur**
3. aire × hauteur = le **volume** de la boîte portée par `u`, `v` et `w`

Note:
Insister sur le rôle de `w` : il ne participe pas à la base, il mesure de combien
on s'en éloigne. S'il reste dans le plan de `u` et `v`, la boîte est plate, et le
volume est nul — c'est la slide suivante.

Note:
Le nom vient de là : il *mélange* les deux produits de la séance. On l'appelle
aussi déterminant 3×3, et on le retrouvera sous ce nom en GVM-03.

---

## Ce que le produit mixte répond

<p class="formule">(u × v) · w = 0</p>

- volume nul → les trois vecteurs sont **coplanaires** : ils tiennent dans un plan
- coplanaires → ils **ne peuvent pas** servir de base à l'espace
- son **signe** dit l'orientation du trièdre : positif = direct, négatif = indirect

C'est le test de la main de GVM-01, devenu un calcul.

Note:
C'est la définition opératoire de l'indépendance linéaire : trois vecteurs
forment une base de l'espace si et seulement si leur produit mixte n'est pas
nul. On s'en resservira en GVM-03 avec les matrices.

---

## Atelier — 20 min

Le garde voit-il le joueur ? Trois tests, dans cet ordre :

1. **distance** — le joueur est-il à portée ?
2. **angle** — est-il dans le cône, en comparant des cosinus ?
3. **côté** — à gauche ou à droite, pour savoir dans quel sens tourner ?

Exercices 1 et 2 de la feuille ; le 3 est le bilan, à finir à la maison.

---

## À retenir

- `u · v` répond **« à quel point d'accord »** — un nombre, et son signe suffit
- `u · v = 0` → perpendiculaires &nbsp;·&nbsp; `u × v = 0` → colinéaires
- projeter découpe un vecteur en **le long de** et **perpendiculaire à**
- `u × v` répond **« perpendiculaire à quoi, et de quel côté »**

---

# Questions ?
<!-- .slide: class="title" -->

