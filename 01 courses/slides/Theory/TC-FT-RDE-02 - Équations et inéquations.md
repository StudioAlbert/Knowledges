---
title: TC-FT-RDE-02 - Équations et inéquations
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

# Équations et inéquations
<!-- .slide: class="title" -->

### Trouver la valeur qui fait que ça marche

<small>TC-FT-RDE-02 · Résolution d'Équation</small>

Note:
RDE-01 a donné les outils de calcul. Ici on s'en sert pour répondre à une
question précise : quelle valeur de `x` rend l'égalité vraie ? C'est la question
que pose tout code de collision, de trajectoire et de seuil.

---

## Objectifs

À la fin de la séance, vous savez :

- résoudre une équation du **premier degré**, et dire par quelle méthode
- **factoriser** pour faire apparaître les solutions
- lire un **discriminant**, et vérifier par somme et produit
- manier une **inéquation** sans vous tromper de sens

**Prérequis :** [[01 courses/slides/Theory/TC-FT-RDE-01 - Nombres, puissances et logarithmes|TC-FT-RDE-01]].

---

# Le premier degré
<!-- .slide: class="title" -->

---

## Résoudre, c'est isoler

```text
7x − 4 = 2x + 11

7x − 2x = 11 + 4        rassembler : les x d'un côté
     5x = 15            réduire
      x = 3             diviser par 5
```

Chaque opération se défait par son **inverse**, appliquée des **deux** côtés.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/premier_degre_widget.html#resoudre" data-background-interactive -->

Note:
**Le même calcul, en image.** La droite `y = ax + b` croise l'axe en un point, et
son abscisse est la solution. Bouger `a` et `b` : le point se déplace, mais il y
en a toujours **exactement un** — c'est l'unicité, vue au lieu d'être démontrée.

Enchaîner sur l'onglet `ax + b = cx + d` : résoudre une équation à deux membres,
c'est chercher où deux droites se croisent. Beaucoup comprennent le « rassembler
les x d'un côté » seulement ici.

Garder le dernier onglet pour la fin de la slide suivante : quand `a = 0`, la
droite devient horizontale et il n'y a plus rien à croiser.

---

## Ce qu'on a le droit de faire

- **ajouter** ou **retirer** la même chose des deux côtés — toujours
- **multiplier** ou **diviser** par un nombre **non nul** — toujours
- diviser par une **expression** — seulement si on sait qu'elle n'est pas nulle
- élever au carré — attention, ça peut **inventer** des solutions

---

## Élever au carré invente des solutions

```text
√(2x + 3) = x            on élève les deux côtés au carré

2x + 3 = x²
x² − 2x − 3 = 0          x = 3   ou   x = −1

x = 3  :  √9 = 3         vrai
x = −1 :  √1 = 1 ≠ −1    faux
```

Le carré **perd le signe** : il rend vraie une égalité qui ne l'était pas. Toute
solution obtenue en élevant au carré se vérifie dans l'équation **de départ**.

Note:
C'est la seule ligne de la slide précédente qui ne se devine pas, d'où cette
slide à elle seule. Faire remarquer que `−1` n'est pas une erreur de calcul :
le calcul est juste, c'est l'opération qui a ajouté une solution. Le même piège
revient avec la valeur absolue, et c'est la raison pour laquelle on vérifie
toujours.

Note:
Le troisième point est celui qui coûte cher. Diviser par `x` fait disparaître la
solution `x = 0` sans prévenir. D'où le réflexe de la séance : on ne divise pas
par une expression, on **factorise**.

---

# Factoriser
<!-- .slide: class="title" -->

---

## Le produit nul

<p class="formule">A × B = 0 &nbsp;&nbsp;⟺&nbsp;&nbsp; A = 0 &nbsp;ou&nbsp; B = 0</p>

C'est la seule règle qui transforme une équation en **liste de solutions**.

Tout l'art consiste donc à ramener l'équation à un **produit égal à zéro**.

---

## Les identités remarquables

$$a^2 - b^2 = (a-b)(a+b)$$
$$a^2 + 2ab + b^2 = (a+b)^2$$
$$a^2 - 2ab + b^2 = (a-b)^2$$

Trois formes à reconnaître d'un coup d'œil : elles évitent la méthode du discriminant.

Note:
Le repère pour les deux dernières : le terme constant est un carré, et le terme
du milieu vaut deux fois le produit des racines. `x² + 6x + 9` : 9 = 3², et
6 = 2 × 3. C'est `(x + 3)²`.

---

## Factoriser pour annuler

```text
x² − 9 = 0

(x − 3)(x + 3) = 0      identité a² − b²
x − 3 = 0  ou  x + 3 = 0
x = 3      ou  x = −3
```

Ne **jamais** développer un produit déjà factorisé : il est au bon format.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/equations_quizz_widget.html#cours" data-background-interactive -->

Note:
Cinq équations, à faire ensemble. Laisser chercher trente secondes, prendre une
réponse à voix haute, puis valider. La correction donne les étapes, mais c'est
la ligne du bas qu'il faut lire : **la méthode à reconnaître**. La série
« à la maison » en a dix, et sert de devoir.

---

# Le second degré
<!-- .slide: class="title" -->

---

## La forme générale

$$ax^2 + bx + c = 0 \qquad a \neq 0$$

- **a** décide si la parabole s'ouvre vers le haut ou vers le bas
- **c** est la valeur en `x = 0`, donc où elle coupe l'axe vertical
- les **solutions** sont les points où elle coupe l'axe horizontal

Quand la factorisation ne saute pas aux yeux, on passe au discriminant.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/discriminant_widget.html#parabole" data-background-interactive -->

Note:
Bouger `a` d'abord, seul : la parabole s'ouvre, se referme, se retourne. Puis
`c`, qui la fait monter et descendre — et faire remarquer que les racines
apparaissent et disparaissent à ce moment-là. `b` en dernier, c'est le moins
intuitif : il décale le sommet en diagonale.

---

## Le discriminant

$$\Delta = b^2 - 4ac$$

| signe de Δ | racines | la parabole |
|---|---|---|
| **Δ > 0** | deux, $x = \dfrac{-b \pm \sqrt{\Delta}}{2a}$ | coupe l'axe en deux points |
| **Δ = 0** | une seule, $x = \dfrac{-b}{2a}$ | l'effleure au sommet |
| **Δ < 0** | aucune réelle | ne le touche jamais |

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/discriminant_widget.html#aucune" data-background-interactive -->

Note:
Les trois onglets donnent les trois cas. Insister sur le dernier : en code,
`Δ < 0` n'est pas une erreur, c'est une **réponse** — le rayon manque la sphère.
Oublier de tester le signe avant la racine carrée donne un `NaN` qui se propage
silencieusement jusqu'à l'affichage.

---

## Somme et produit des racines

$$S = x_1 + x_2 = \frac{-b}{a} \qquad P = x_1 x_2 = \frac{c}{a}$$

- se lisent **directement** sur les coefficients, sans résoudre
- vérifient un résultat sans le recalculer
- `x² − 5x + 6` : S = 5, P = 6 → **2 et 3**, trouvées de tête

Valable dès que **Δ ≥ 0**. Et réciproquement, $x^2 - Sx + P = 0$ reconstruit l'équation.

Note:
C'est la méthode la plus rapide sur les petits trinômes à coefficients entiers,
et elle sert surtout de **contrôle** : deux racines sorties du discriminant dont
la somme ne fait pas `−b/a`, c'est une erreur de calcul, et on le voit en deux
secondes.

---

## À quoi ça sert dans un jeu
<!-- .slide: class="schema" -->

Un saut de platformer, c'est **deux** paraboles : on monte doucement, on retombe vite.

![[rde02_saut_parabole.svg]]

Note:
Un seul exemple, et il porte toute la séance. La montée et la chute n'ont pas la
même gravité — c'est ce qui rend un saut agréable, et c'est la raison pour
laquelle les deux instants ne sont **pas** symétriques autour du sommet.
Résoudre l'équation donne l'instant où il passe à 8 m ; le discriminant dit
qu'à 11 m il n'y passe jamais, sans qu'on ait à tracer quoi que ce soit.
Faire remarquer que la fenêtre de 0,76 s est exactement ce qu'un game designer
règle à la main.

---

# Les inéquations
<!-- .slide: class="title" -->

---

## Résoudre une inéquation

```text
3x − 2 < 7

3x < 9
 x < 3            la réponse est un intervalle : ]−∞ ; 3[
```

On résout **exactement** comme une équation. 
Seule la réponse change de nature : ce n'est plus une valeur, c'est un **ensemble**.

---

## Le piège du signe

```text
-2x < 6

 x > -3           on divise par -2 : l'inégalité se retourne
```

Multiplier ou diviser par un nombre **négatif retourne le sens**. 
C'est l'erreur la plus fréquente, et elle ne se voit pas.

Note:
Le contrôle qui sauve : prendre une valeur de l'intervalle trouvé et la remettre
dans l'inéquation de départ. Avec `x = 0` : `0 < 6`, vrai, donc 0 doit être dans
la réponse. `x > −3` le contient. Si on avait gardé `x < −3`, non.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/premier_degre_widget.html#inequation" data-background-interactive -->

Note:
**Le piège du signe, rendu visible.** La bande verte est l'ensemble des `x` qui
conviennent : ceux où la droite passe au-dessus de l'axe. Faire passer `a` du
négatif au positif et laisser la bande basculer de l'autre côté — c'est ça, le
sens qui se retourne.

Demander l'intervalle **avant** de le montrer, puis vérifier. La réponse d'une
inéquation est un intervalle, pas un nombre : c'est la deuxième chose qu'ils
oublient après le signe.

---

## Tableau de signes

Un produit change de signe **en ses racines**, et nulle part ailleurs.

```text
                 -∞        -2         3        +∞
   x + 2             -      0    +         +
   x - 3             -           -    0    +
   (x+2)(x-3)        +      0    -    0    +
```

Chaque ligne est un facteur, la dernière est leur **produit des signes**.

---

## Lire le tableau

Pour `(x + 2)(x − 3) > 0`, on prend les colonnes où la dernière ligne est **+** :

<p class="formule">x ∈ ]−∞ ; −2[ ∪ ]3 ; +∞[</p>

- **une ligne par facteur**, chacune change de signe à sa racine
- la dernière ligne multiplie les signes, colonne par colonne
- un **quotient** se traite pareil — mais la racine du dénominateur est **exclue**

Note:
C'est ce que le tableau évite : tâtonner avec des valeurs au hasard. Trois
facteurs, et le tâtonnement devient impraticable, alors que le tableau ne change
pas de méthode — une ligne de plus.

---

## Atelier — 20 min

Un projectile part à 20 m/s vers le haut, depuis 1,5 m, avec `g = 10` :

<p class="formule">h(t) = −5t² + 20t + 1,5</p>

1. à quel instant atteint-il **12 m** ? les deux réponses ont-elles un sens ?
2. pour quel **intervalle de temps** est-il au-dessus de 12 m ?
3. quelle **vitesse de départ** le ferait manquer 12 m ? (indice : Δ)
4. et s'il partait du sol, la réponse à la question 1 changerait-elle **beaucoup** ?

Énoncé et quizz : [[01 courses/exercises/Theory/TC-FT-RDE-02 - Quizz des dix équations|dix équations à la maison]].

---

## À retenir

- **isoler** pour le premier degré, **factoriser** pour faire apparaître les racines
- un produit nul donne la **liste** des solutions ; ne jamais développer un produit déjà factorisé
- Δ dit **combien** de racines ; S et P les **vérifient** sans recalcul
- un négatif **retourne** l'inégalité, et un tableau de signes évite de tâtonner

---

# Questions ?
<!-- .slide: class="title" -->
