---
title: TC-FT-RDE-01 - Nombres, puissances et logarithmes
type: slides
subject: Theory
duration_h: 1
bloc_gsda: Résolution d'Équation
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

# Nombres, puissances et logarithmes
<!-- .slide: class="title" -->

### De quoi mesurer un jeu

<small>TC-FT-RDE-01 · Résolution d'Équation</small>

Note:
Première séance du bloc. Rien de neuf pour personne : des outils vus au collège,
repris pour ce qu'ils servent ici — dire si ça tient en mémoire, si ça tient dans
l'image, et à quelle vitesse ça grossit.

---

## Objectifs

À la fin de la séance, vous savez :

- nommer les **ensembles de nombres** et leurs notations
- manipuler **puissances** et **racines** avec un seul jeu de règles
- dire ce que résolvent l'**exponentielle** et le **logarithme**
- estimer un **ordre de grandeur** sans calculatrice

---

# Les nombres
<!-- .slide: class="title" -->

---

## Quel ensemble pour quelles données

| Ensemble | Notation | Ce qu'il contient | Exemple |
|---|---|---|---|
| Entiers naturels | **ℕ** | les entiers à partir de 0 | `0, 1, 2, 3` |
| Entiers relatifs | **ℤ** | les naturels et leurs opposés | `−3, 0, 7` |
| Décimaux | **𝔻** | une virgule, un nombre **fini** de chiffres | `0,25` &nbsp; `3,5` |
| Rationnels | **ℚ** | tout ce qui s'écrit en fraction | `1/3 = 0,333…` |
| Réels | **ℝ** | les rationnels **et** le reste | `√2` &nbsp; `π` |
| Réels positifs | **ℝ⁺** | les réels à partir de 0 | une durée, une distance |

Chacun contient le précédent : **ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ**.

Note:
Le saut qui compte est 𝔻 → ℚ : `1/3` n'a pas d'écriture décimale finie, donc pas
de représentation exacte en machine non plus. Et `0,1` est décimal pour nous mais
pas en binaire — c'est tout le sujet de RNLB-03 sur les flottants.

---

## Choisir son ensemble

- un compteur de munitions, un numéro de niveau → **ℕ**
- une température, un solde, un décalage → **ℤ**
- une position, une vitesse, un temps → **ℝ**
- une durée, une distance, une masse → **ℝ⁺**, et c'est une **garantie**

Dire « cette grandeur est dans ℝ⁺ », c'est déjà écrire une règle du jeu.

---

## Nombres premiers

Divisibles par 1 et par eux-mêmes, et par rien d'autre : `2, 3, 5, 7, 11, 13…`

- **ℕ tout entier** se fabrique en les multipliant, d'une seule façon
- une table de hachage de taille **première** répartit mieux les clés
- deux cycles de longueurs premières entre elles ne se resynchronisent qu'au bout
  de leur **produit**

Note:
Le dernier point est visuel : deux ennemis qui clignotent toutes les 4 et 6
images retombent ensemble toutes les 12. En 5 et 7, toutes les 35 — on ne voit
plus le motif. C'est ainsi qu'on casse l'effet « tout le monde en rythme ».

---

## Décomposer

```text
 1  =  (rien)            ni premier, ni composé : le produit vide
 2  =  2                 premier
 3  =  3                 premier
 4  =  2 × 2             =  2²
 5  =  5                 premier
 8  =  2 × 2 × 2         =  2³
13  =  13                premier
18  =  2 × 3 × 3         =  2 × 3²
19  =  19                premier
```

Une seule décomposition par nombre, à l'ordre des facteurs près.

Note:
C'est le théorème fondamental de l'arithmétique. Les premiers sont les briques,
et il n'y a qu'une façon d'empiler les briques pour obtenir un nombre donné. Le
cas de 1 mérite l'arrêt : il n'est pas premier, et pas composé non plus — c'est
le produit de zéro facteur. En faire un premier casserait l'unicité, puisqu'on
pourrait écrire 18 = 1 × 2 × 3² autant de fois qu'on veut.

---

# Puissances et racines
<!-- .slide: class="title" -->

---

## Puissances

$$a^n = \underbrace{a \times a \times \cdots \times a}_{n \text{ facteurs}}$$

Trois règles, et tout le reste s'en déduit :

```
a^m · a^n = a^(m+n)        (a^m)^n = a^(m·n)        a^(-n) = 1 / a^n
```

On **additionne** les exposants pour multiplier, on les **multiplie** pour empiler.

---

## Racines

$$\sqrt{a} = a^{1/2} \qquad \sqrt[3]{a} = a^{1/3}$$

Une racine n'est pas une opération de plus : c'est une **puissance fractionnaire**.

Les trois règles d'avant s'y appliquent telles quelles, sans rien apprendre de neuf.

---

## Négatif, fractionnaire : les mêmes règles

```
2^-3  = 1 / 2^3 = 1/8          une puissance négative est une fraction
8^(1/3) = ∛8 = 2               une puissance fractionnaire est une racine
8^(2/3) = (∛8)^2 = 4           et les deux se combinent

a^(-1/2) = 1 / √a              l'inverse d'une racine, sans règle nouvelle
```

Un seul jeu de règles couvre les fractions **et** les racines : c'est tout
l'intérêt de les écrire en exposant.

Note:
Le réflexe à installer : devant `1 / √x`, ne pas chercher une règle des racines —
réécrire en `x^(-1/2)` et appliquer les trois règles. C'est aussi ce que fait la
machine, qui ne connaît que `pow`.

---

## Notation scientifique

$$a \times 10^{n} \qquad \text{avec } 1 \leqslant a < 10$$

Un niveau de jeu, c'est 10<sup>5</sup> triangles et 10<sup>7</sup> octets de textures.

L'ordre de grandeur suffit à décider : on ne compare pas `1 048 576` et `1 000 000`,
on compare `10⁶` et `10⁶`.

---

# Exponentielle et logarithme
<!-- .slide: class="title" -->

---

## Exponentielle

$$f(x) = a^{x} \qquad \text{avec } a > 0$$

- l'exposant devient la **variable** : on ne multiplie plus, on fait varier
- elle décrit toute grandeur dont la **croissance est proportionnelle à elle-même**
- intérêts composés, population, désintégration, propagation
- `exp(x) = e^x` est celle qui est **égale à sa propre dérivée**

---

## La courbe
<!-- .slide: class="schema" -->

À chaque pas sur `x`, la valeur est multipliée — pas augmentée.

![[rde01_exponentielle.svg]]

Note:
Faire lire les six points à voix haute : 1, 2, 4, 8, 16, 32. Puis demander la
valeur en 10 — 1024 — et faire remarquer qu'elle ne tiendrait pas sur l'écran.
C'est le problème que le logarithme vient résoudre.

---

## Logarithme

$$\log_a(x) = y \iff a^{y} = x$$

- c'est **l'exposant** qu'il faut mettre à `a` pour obtenir `x`
- donc la fonction **réciproque** de l'exponentielle
- elle résout les équations où l'inconnue est **en exposant**
- `log₂` en informatique, `log₁₀` pour les ordres de grandeur, `ln` en maths

---

## La courbe
<!-- .slide: class="schema" -->

Il faut doubler `x` pour gagner un pas sur `y`.

![[rde01_logarithme.svg]]

Note:
C'est la même courbe que la précédente, vue en échangeant les axes. Le faire
dire : deux fonctions réciproques sont symétriques par rapport à la première
bissectrice. Et noter que `log(0)` n'existe pas, parce qu'aucune puissance de 2
ne vaut 0.

---

## Cas d'usage

- **doubler à chaque palier** : la courbe d'expérience d'un jeu de rôle
- **combien de doublements** pour arriver là : l'autre question, le logarithme
- **diviser en deux** à chaque étape : dichotomie, arbres, coût en `log₂ n`
- le **décibel** et les **f-stops** sont des échelles logarithmiques

Un million d'éléments, c'est **20** étapes de dichotomie. C'est ça, la bonne nouvelle.

Note:
Le widget `croissance_widget.html` était proposé au plan — trois courbes sur le
même graphe et un axe basculable en échelle log. Il n'est pas construit : les
deux schémas de courbe disent l'essentiel.

---

# Mesurer juste
<!-- .slide: class="title" -->

---

## Arrondi

```
tronquer(2.7) = 2          on jette ce qui dépasse
arrondir(2.7) = 3          on prend le plus proche
arrondir(2.5) = ?          2 ou 3, selon la convention
```

Tronquer **biaise toujours vers le bas**. Sur un score affiché mille fois par
partie, le joueur voit la différence.

---

## Erreur relative

$$\varepsilon_{\text{rel}} = \frac{\lvert \text{mesure} - \text{valeur vraie} \rvert}{\lvert \text{valeur vraie} \rvert}$$

- se tromper d'un mètre sur un kilomètre : **0,1 %**
- se tromper d'un mètre sur un mètre : **100 %**

L'écart absolu ne dit rien tout seul. C'est la **proportion** qui décide, et c'est
pourquoi les flottants surprennent sur les grands nombres.

Note:
Transition vers RNLB-03 : un flottant garde un nombre fixe de chiffres
**significatifs**, donc une erreur relative constante — et une erreur absolue qui
grandit avec la valeur.

---

## Atelier — 20 min

Sans calculatrice, et en notation scientifique.

1. un atlas de 4096 × 4096 pixels, 4 octets par pixel : combien d'octets ?
2. avec les niveaux de mipmap, combien en plus — et pourquoi ce n'est pas le double ?
3. une courbe d'XP qui double à chaque niveau : quel palier atteint 20 heures de jeu ?
4. combien d'étapes de dichotomie pour trouver un nom dans une liste d'un million ?

---

## À retenir

- les puissances décrivent la **croissance**, le logarithme la **découpe**
- une racine est une puissance : **un seul** jeu de règles
- l'ordre de grandeur suffit à **décider** ; la valeur exacte vient après
- une erreur se mesure en **proportion**, jamais en absolu

---

# Questions ?
<!-- .slide: class="title" -->
