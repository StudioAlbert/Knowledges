---
title: TC-FT-RDE-03 - Fonctions et repères
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

# Fonctions et repères
<!-- .slide: class="title" -->

### Une courbe, et ce qu'elle règle

<small>TC-FT-RDE-03 · Résolution d'Équation</small>

Note:
Dernière séance du bloc. RDE-02 cherchait **la** valeur qui annule ; ici on
regarde la courbe entière, parce que c'est elle qu'on règle quand on équilibre un
jeu. Séance volontairement visuelle : on reconnaît avant de calculer.

---

## Objectifs

À la fin de la séance, vous savez :

- dire le **domaine** et l'**image** d'une fonction, et pourquoi ça compte
- **reconnaître** une famille de courbe à son allure
- lire **monotonie**, **extremum**, **racines** et **signe** sur un graphe
- **composer** deux fonctions, et borner le résultat

**Prérequis :** [[01 courses/slides/Theory/TC-FT-RDE-02 - Équations et inéquations|TC-FT-RDE-02]].

---

# Ce qu'est une fonction
<!-- .slide: class="title" -->

---

## Une entrée, une sortie

$$f : x \longmapsto f(x)$$

Une fonction associe à chaque entrée **une seule** sortie. 
Deux sorties pour la même entrée, et ce n'est plus une fonction.

En code c'est la même exigence : les même conditions doivent toujours donner les résultats, sinon le jeu n'est pas reproductible, le joueur est faché.

---

## Domaine et image

- le **domaine** : ce qu'on a le droit de donner
- l'**image** : ce qu'on peut obtenir en retour

$$\sqrt{x} \text{ refuse le négatif} \qquad \frac{1}{x} \text{ refuse } 0 \qquad \log x \text{ exige } x > 0$$

Un domaine mal gardé, c'est un `NaN` qui remonte jusqu'à l'affichage.

Note:
Le réflexe à installer : avant d'appeler, se demander ce que la fonction refuse.
`sqrt` d'un discriminant négatif, `log` d'un volume nul, une division par une
distance nulle quand deux objets se superposent — les trois arrivent vraiment.

---

# Reconnaître une famille
<!-- .slide: class="title" -->

---

## Six formes à reconnaître
<!-- .slide: class="schema" -->

L'allure suffit pour choisir : le calcul vient après.

![[rde03_catalogue.svg]]

---

## Le premier degré, c'est une sensibilité

$$f(x) = ax + b$$

- **a** est la pente : de combien la sortie bouge quand l'entrée bouge d'un cran
- **b** est la valeur au repos, en `x = 0`
- doubler `a`, c'est doubler la sensibilité de la souris

C'est la seule famille où la réponse est **proportionnelle** à la demande.

---

## Le second degré, c'est un sommet

$$f(x) = ax^2 + bx + c \qquad \text{sommet en } x = \frac{-b}{2a}$$

La hauteur d'un saut est une parabole, et son sommet est le point le plus haut
atteint — l'instant où la vitesse verticale s'annule.

RDE-02 cherchait où elle coupe l'axe ; ici on cherche **où elle culmine**.

---

## Exponentielle et logarithme

- l'**exponentielle** s'envole : chaque palier coûte le double du précédent
- le **logarithme** s'essouffle : il faut doubler l'entrée pour gagner un cran
- elles sont **réciproques** : l'une défait ce que l'autre fait

C'est pour ça qu'une courbe d'XP est exponentielle et qu'un volume est en décibels.

---

# Lire une courbe
<!-- .slide: class="title" -->

---

## Monter, descendre, culminer

- **monotone** : la courbe ne change jamais d'avis, elle monte ou elle descend
- **extremum** : l'endroit exact où elle en change
- une fonction monotone est **inversible** — à une sortie correspond une entrée

Une courbe de réglage non monotone est presque toujours un bug de conception.

Note:
L'argument du dernier point : si deux réglages différents donnent la même
sensation, le joueur ne peut plus régler. C'est la définition pratique de
« inversible », et elle vaut pour tous les curseurs d'un menu d'options.

---

## Lire un graphe

| On cherche | On regarde |
|---|---|
| les **racines** | où la courbe traverse l'axe horizontal |
| le **signe** | au-dessus de l'axe : positif ; en dessous : négatif |
| l'**extremum** | le sommet ou le creux |
| le **domaine** | jusqu'où la courbe est tracée |

Tout ce que RDE-02 calculait, le graphe le montre.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/fonctions_widget.html#degats" data-background-interactive -->

Note:
Six fonctions de jeu, et le panneau de droite lit tout : domaine, image,
monotonie, racines, extremum. Commencer par les dégâts — faire bouger la portée
et regarder la racine se déplacer. Puis la courbe d'XP, pour voir l'image
exploser quand on réduit le palier.

---

# Combiner
<!-- .slide: class="title" -->

---

## Composer

$$(g \circ f)(x) = g\big(f(x)\big)$$

Appliquer une fonction au **résultat** d'une autre.

C'est exactement ce que fait un easing : on normalise le temps entre 0 et 1,
puis on applique une courbe à ce temps.

---

## Composer, en trois graphes
<!-- .slide: class="schema" -->

Une distance entre à gauche, des dégâts sortent à droite — et rien n'est calculé deux fois.

![[rde03_composition.svg]]

Note:
C'est **l'exemple du formatif**, montré en entier avant qu'ils l'écrivent. Faire
lire les trois graphes dans l'ordre : `f` ne connaît que des distances et rend un
nombre entre 0 et 1 ; `g` ne connaît que ce nombre et rend des dégâts. Aucune des
deux ne connaît l'autre — c'est ce qui permet de changer la courbe du milieu sans
retoucher les bornes.

---

## Ce qu'il faut vérifier pour composer

- le **domaine** : l'image de `f` doit tenir dans le domaine de `g`
- la **monotonie** se transmet : deux croissantes donnent une croissante, une décroissante inverse le sens
- la **normalisation** entre 0 et 1 rend les courbes interchangeables
- le **bornage** garantit la première ligne — c'est exactement le rôle de `clamp`

Composer sans vérifier le domaine, c'est une racine de négatif ou une division par zéro.

---

## Les deux outils du formatif

```text
|x − c|              l'écart à une cible, sans le signe
clamp(x, 0, 1)       la valeur ramenée dans l'intervalle
```

Le premier mesure, le second **protège**. Sans le `clamp`, une distance de
−2 mètres donnerait des dégâts supérieurs au maximum.

Note:
À partir d'ici, tout ce qu'on montre sert au formatif. Le `clamp` n'est pas une
précaution de style : c'est lui qui garantit que l'image de `f` reste dans
`[0 ; 1]`, donc dans le domaine de `g`. C'est la slide précédente, appliquée.

---

## Fonction par morceaux

```text
             plein          décroissant        nul
        ├──────────────┼──────────────────┼──────────
        0             10 m              30 m

dégâts(d) = 1                si d ≤ 10
          = (30 − d) / 20    si 10 < d ≤ 30
          = 0                si d > 30
```

La forme la plus courante dans un jeu — et celle du formatif, aux valeurs près.

Note:
Faire remarquer la continuité aux raccords : en `d = 10`, les deux morceaux
donnent 1 ; en `d = 30`, les deux donnent 0. Un raccord qui ne colle pas se voit
en jeu comme un saut de dégâts, et c'est le bug qu'on cherche des heures.

---

## La courbe à retrouver
<!-- .slide: class="schema" -->

Mêmes règles, deux formes : la proportionnelle perd régulièrement, l'amortie tient puis s'effondre.

![[rde03_degats_amortis.svg]]

Note:
Les deux bornes sont imposées par le game design — 25 à bout portant, 0 à cinq
mètres — et c'est **tout** ce qui est imposé. La forme entre les deux est un
choix, et c'est le choix qu'on leur demande de faire. Ne **pas** donner la
formule de l'amortie : les cinq points du tableau suffisent à la retrouver, et
c'est l'exercice.

---

## Formatif — les dégâts selon la distance

Le game designer pose trois règles, et rien d'autre :

- **25 dégâts** à bout portant, soit à moins de 0,25 m
- **0 dégât** à partir de 5 m
- entre les deux, ça **descend**

Deux fonctions à écrire : `DegatsProportionnels`, puis `DegatsAmortis`.

Énoncé : [[01 courses/exercises/Theory/TC-FT-RDE-03 - Formatif, les degats selon la distance|les dégâts selon la distance]].

---

## À retenir

- le **domaine** d'abord : ce que la fonction refuse est ce qui fera planter
- la **famille** ensuite : l'allure dit le comportement avant tout calcul
- **composer** pour régler, **borner** pour protéger
- le **graphe** montre ce que le calcul démontre

---

# Questions ?
<!-- .slide: class="title" -->

### Fin du bloc

<small>Nombres et logarithmes, équations et inéquations, fonctions et repères : trois séances pour lire ce qu'un jeu calcule.</small>
