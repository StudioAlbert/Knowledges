---
title: Géométrie du triangle
type: slides
status: Backlog
subject: C++
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
publish: false
---

# Géométrie du triangle
<!-- .slide: class="title" -->

### Pythagore, Thalès, similitude : mesurer sans mesurer

<small>TC-FT-TRG-01 · Trigonométrie</small>

Note:
Séance d'entrée du bloc Trigonométrie, sans prérequis au-delà du collège.
Tout ce qui suit sert de socle à TRG-02 (cercle trigonométrique) et au bloc
Géométrie vectorielle. Fil rouge : le triangle est la seule primitive que
connaisse une carte graphique, et la distance entre deux points est le
calcul le plus exécuté d'un moteur de jeu.

---

## Objectifs

À la fin de la séance, vous savez :

- nommer les éléments d'un triangle et ses droites remarquables
- calculer une aire et un périmètre, y compris à partir de trois sommets
- appliquer Pythagore **et sa réciproque** pour tester un angle droit
- calculer la distance entre deux points d'un repère, et dire quand éviter la racine carrée
- reconnaître deux triangles semblables et exploiter le rapport de similitude
- prévoir l'effet d'une mise à l'échelle sur les longueurs, les aires et les volumes

**Prérequis :** aucun.

---

# Le triangle, brique de base
<!-- .slide: class="title" -->

---

## Pourquoi le triangle ?

- c'est le **polygone minimal** : trois points non alignés définissent toujours un plan
- il est **toujours plan et toujours convexe** — un quadrilatère, non
- le GPU ne sait rasteriser **que** des triangles : tout maillage est triangulé avant affichage
- collisions, navmesh, terrains, UV : tout repose dessus

Note:
Insister sur « toujours plan » : c'est la raison technique du monopole du
triangle en 3D temps réel. Quatre points peuvent être non coplanaires,
donc une normale de face n'aurait plus de sens.

---

## Vocabulaire

- **sommets** A, B, C — **côtés** [AB], [BC], [CA] — **angles** Â, B̂, Ĉ
- convention : le côté *a* est **opposé** au sommet A
- la somme des angles d'un triangle vaut toujours **180°** (π rad)
- **inégalité triangulaire** : chaque côté est plus court que la somme des deux autres

```
a < b + c      b < a + c      c < a + b
```

Note:
La convention côté opposé / sommet servira à TRG-03 pour les lois des sinus
et des cosinus. L'inégalité triangulaire est le premier test à faire quand
un triangle « ne se dessine pas ».

---

## Vocabulaire

[[Schema Excalidraw]]

---
## Définitions — triangle quelconque

Aucun côté égal, aucun angle égal. C'est le cas général.

Un triangle porte **6 mesures** : 3 longueurs (*a*, *b*, *c*) et 3 angles (Â, B̂, Ĉ).

- elles ne sont **pas indépendantes** : Â + B̂ + Ĉ = 180°, deux angles donnent le troisième
- **3 mesures bien choisies** suffisent à construire le triangle — les 3 autres s'en déduisent
- parmi ces 3, il faut **au moins un côté** : les angles seuls fixent la *forme*, jamais la *taille*

Note:
On pose ici sans le nommer le vocabulaire de TRG-03 : « résoudre un
triangle », c'est retrouver les six mesures à partir de trois d'entre elles.
Faire deviner pourquoi trois angles ne suffisent pas : un triangle 60-60-60
de 1 cm et un de 1 km ont les mêmes angles.

---

## Les trois cas de construction

| Cas | On connaît | Exemple (triangle 3-4-5) |
|---|---|---|
| **CCC** | les 3 côtés | a = 3, b = 4, c = 5 |
| **CAC** | 2 côtés et l'angle **compris** entre eux | a = 3, Ĉ = 90°, b = 4 |
| **ACA** | 1 côté et les 2 angles **à ses extrémités** | Â ≈ 37°, c = 5, B̂ ≈ 53° |

- deux triangles qui partagent l'un de ces trios sont **égaux** (isométriques)
- **AAA** ne suffit pas : mêmes angles, tailles différentes → triangles **semblables** (fin de séance)
- piège : 2 côtés et un angle **non compris** entre eux peuvent donner deux triangles différents

Note:
CCC est exactement ce que fait le widget « Réciproque » de Pythagore :
trois longueurs, deux coups de compas, un seul triangle possible (ou aucun
si l'inégalité triangulaire est violée).
---

## Cas CCC — les trois côtés
<!-- .slide: class="schema" -->

![[trg01_cas_ccc.svg]]

Note:
Deux coups de compas suffisent : A est à la distance b de C et à la
distance c de B. Les deux arcs ne se coupent qu'en un point — le triangle
est unique.
C'est exactement la construction du widget « La réciproque » : trois longueurs,
deux arcs, un seul triangle. Rappeler l'inégalité triangulaire : si un côté
dépasse la somme des deux autres, les arcs ne se coupent pas.

---

## Cas CAC — deux côtés et l'angle entre eux
<!-- .slide: class="schema" -->

![[trg01_cas_cac.svg]]

Note:
L'angle est compris entre les deux côtés donnés : on trace l'angle, on
reporte les deux longueurs, il ne reste qu'à refermer. Le troisième côté c
n'est pas donné, il se déduit — ici par Pythagore.
Insister sur « compris entre ». Avec deux côtés et un angle qui n'est pas
entre eux (cas CCA), deux triangles différents peuvent convenir : c'est le
cas ambigu, à montrer au tableau si la question vient.

---

## Cas ACA — un côté et les deux angles
<!-- .slide: class="schema" -->

![[trg01_cas_aca.svg]]

Note:
Le côté donné fixe l'échelle ; les deux angles à ses extrémités fixent la
forme. Les deux demi-droites ne se coupent qu'une fois : C est déterminé,
donc a et b aussi.
Le troisième angle se déduit de la somme à 180°, il n'apporte rien de plus :
c'est pourquoi AAA ne détermine pas le triangle, mais seulement sa forme.

---

# Angles et droites remarquables
<!-- .slide: class="title" -->

---

## Angles — rappels utiles

- **complémentaires** : somme = 90° · **supplémentaires** : somme = 180°
- **opposés par le sommet** : égaux
- **alternes-internes** (deux parallèles coupées par une sécante) : égaux
- **correspondants** : égaux

Note:
Ces égalités d'angles sont l'outil de démonstration de Thalès et de la
similitude, plus loin dans la séance. Les poser maintenant évite de
s'arrêter au milieu de la preuve.

---

## Les quatre droites remarquables

| Droite | Définition | Point de concours |
|---|---|---|
| **Médiane** | sommet → milieu du côté opposé | centre de gravité **G** |
| **Hauteur** | sommet ⊥ côté opposé | orthocentre **H** |
| **Médiatrice** | ⊥ au milieu d'un côté | centre du cercle circonscrit **O** |
| **Bissectrice** | coupe un angle en deux | centre du cercle inscrit **I** |

Dans chaque cas, les trois droites sont **concourantes**.

---
<!-- .slide: data-background-iframe="00 widgets/_widgets/droites_remarquables_widget.html" data-background-interactive -->

Note:
Widget interactif. Afficher une famille à la fois, en commençant par les
médianes : montrer que les trois se coupent, puis déplacer un sommet — le
point de concours suit. Ajouter les hauteurs, les médiatrices (cercle
circonscrit), les bissectrices (cercle inscrit).
Préréglages qui portent le cours : isocèle (les quatre droites confondues
depuis le sommet principal), équilatéral (G = H = O = I), rectangle
(H sur l'angle droit, O au milieu de l'hypoténuse), obtusangle (H et O
sortent du triangle). Le barycentre est calculé en clair dans le panneau.

Repli : ouvrir 00 widgets/_widgets/droites_remarquables_widget.html.

---

## Le centre de gravité

G est situé aux **2/3** de chaque médiane depuis le sommet.

```
G = ( (x₁ + x₂ + x₃) / 3 ,  (y₁ + y₂ + y₃) / 3 )
```

C'est la moyenne des sommets — le **barycentre**.

Note:
Traduction directe en jeu : pivot d'un objet, centre de masse d'un ragdoll,
point de visée d'une IA sur une hitbox. La formule se généralise à n points
et à la 3D sans changement.

---

# Triangles remarquables
<!-- .slide: class="title" -->

---

## Définitions — isocèle et équilatéral

| Triangle | Côtés | Angles | Symétrie |
|---|---|---|---|
| **isocèle** | 2 côtés égaux | 2 angles égaux | 1 axe |
| **équilatéral** | 3 côtés égaux | 3 × 60° | 3 axes |

L'équilatéral est un cas particulier d'isocèle — pas l'inverse.

---

## Propriétés du triangle isocèle

Triangle isocèle en A (AB = AC) :

- les **angles à la base** sont égaux : B̂ = Ĉ
- la médiane, la hauteur, la médiatrice et la bissectrice issues de **A** sont **confondues** : c'est l'axe de symétrie
- réciproque vraie : deux angles égaux ⇒ triangle isocèle

Note:
Le « quatre droites en une » est le résultat le plus rentable de la slide :
il évite la moitié des constructions dans les exercices.

---
<!-- .slide: data-background-iframe="00 widgets/_widgets/droites_remarquables_widget.html#isocele" data-background-interactive -->

Note:
Widget ouvert sur le préréglage isocèle, les quatre familles affichées :
depuis le sommet principal A, médiane, hauteur, médiatrice et bissectrice
sont une seule et même droite — l'axe de symétrie. Décocher les familles
une à une pour le faire constater.
Puis glisser A : tant que AB = AC, les quatre droites restent confondues ;
dès qu'on casse la symétrie, elles se séparent. Passer ensuite au
préréglage équilatéral : les trois axes, et G = H = O = I.

Repli : ouvrir 00 widgets/_widgets/droites_remarquables_widget.html#isocele.

---

## Propriétés du triangle équilatéral

Côté *c* :

- tous les angles valent **60°**
- hauteur : *h* = (√3 / 2) · *c* ≈ 0,866 · *c*
- aire : *A* = (√3 / 4) · *c*²
- centre de gravité, orthocentre, centre du cercle inscrit et circonscrit : **un seul point**

Note:
√3/2 ≈ 0,866 revient partout en grilles hexagonales — l'espacement vertical
d'une grille hex pointy-top vaut exactement cette hauteur.

---

## Définitions — triangle rectangle

Un angle vaut 90°.

- le côté opposé à l'angle droit est l'**hypoténuse** — c'est toujours le **plus long**
- les deux autres sont les **cathètes** (ou côtés de l'angle droit)
- les deux angles aigus sont **complémentaires** : leur somme vaut 90°

Note:
Vocabulaire à fixer maintenant : « hypoténuse » et « cathète » seront
utilisés sans rappel à TRG-02 pour définir sinus, cosinus et tangente.

---

## Propriétés du triangle rectangle

- **Pythagore** : hypoténuse² = somme des carrés des cathètes *(section suivante)*
- l'aire se calcule directement avec les deux cathètes : *A* = (a · b) / 2
- le **cercle circonscrit** a pour diamètre l'hypoténuse — son centre est le milieu de celle-ci
- conséquence : tout triangle inscrit dans un demi-cercle est rectangle *(théorème de Thalès, version cercle)*

Note:
Le coup du demi-cercle est le test visuel le plus rapide pour vérifier un
angle droit sur une figure, et il sert en level design pour placer un point
qui « voit » un segment sous un angle droit.

---
<!-- .slide: data-background-iframe="00 widgets/_widgets/droites_remarquables_widget.html#rectangle" data-background-interactive -->

Note:
Widget ouvert sur le préréglage rectangle, hauteurs et médiatrices affichées :
l'orthocentre H tombe **sur** le sommet de l'angle droit (deux des trois
hauteurs sont les cathètes elles-mêmes), et O est au **milieu de
l'hypoténuse** — le cercle circonscrit a donc l'hypoténuse pour diamètre.
Glisser le sommet de l'angle droit le long du cercle : tant qu'il y reste,
l'angle reste droit et O ne bouge pas. Dès qu'on sort du cercle, O se
déplace et l'angle n'est plus droit — c'est la version « demi-cercle » de
la slide précédente.

Repli : ouvrir 00 widgets/_widgets/droites_remarquables_widget.html#rectangle.

---

## Aires et périmètres

| Forme | Périmètre | Aire |
|---|---|---|
| Triangle quelconque | a + b + c | (base × hauteur) / 2 |
| Triangle rectangle | a + b + c | (a × b) / 2 |
| Équilatéral de côté c | 3c | (√3 / 4) c² |

**Formule de Héron** — trois côtés, aucune hauteur :

```
s = (a + b + c) / 2
A = √( s(s−a)(s−b)(s−c) )
```

---

## Aire à partir de trois sommets

Dans un repère, avec A(x₁,y₁), B(x₂,y₂), C(x₃,y₃) :

```
A = |x₁(y₂−y₃) + x₂(y₃−y₁) + x₃(y₁−y₂)| / 2
```

- sans la valeur absolue, le **signe** donne le sens de parcours : positif = anti-horaire
- c'est ce signe qui sert au **back-face culling** et aux tests « point dans triangle »

Note:
C'est la moitié du produit vectoriel de AB et AC, qu'on démontrera à
GVM-02. Ici on le donne comme recette : le but est qu'ils reconnaissent la
formule quand ils la croiseront dans du code de rasterisation.

---

# Théorème de Pythagore
<!-- .slide: class="title" -->

---

## Théorème de Pythagore : énoncé

> Dans un triangle **rectangle**, le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés.

Triangle rectangle en C, hypoténuse *c* :

```
a² + b² = c²
```

- « carré » au sens littéral : l'**aire** du carré construit sur chaque côté
- connu des Babyloniens ~1000 ans avant Pythagore

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/pythagore_widget.html#carres" data-background-interactive -->

Note:
Widget interactif, quatre onglets (les suivants reviennent plus loin) :
1. « Les trois carrés » : glisser un sommet, lire a², b², c² et l'angle Ĉ.
   Montrer un cas non rectangle → l'égalité casse.
2. « Preuve par réarrangement » : le curseur fait glisser les quatre
   triangles entre les deux pavages du même carré (a+b)². Les côtés a, b, c
   sont cotés sur chaque triangle. Laisser les étudiants énoncer la conclusion.

Repli : ouvrir 00 widgets/_widgets/pythagore_widget.html dans un navigateur.

---

## La preuve en une phrase

Un carré de côté (a + b), pavé de deux façons avec les **mêmes** quatre triangles rectangles :

| Pavage | Reste au centre |
|---|---|
| quatre triangles en moulin | un carré incliné de côté **c** |
| quatre triangles en coin | deux carrés de côtés **a** et **b** |

Même carré, mêmes triangles retirés ⇒ **c² = a² + b²**

Note:
C'est la preuve par réarrangement (attribuée à Bhāskara). Elle ne demande
aucune algèbre : deux découpages du même carré total. La version algébrique
— (a+b)² = c² + 4·(ab/2) — se déroule en deux lignes si un étudiant la
demande.

---

## La réciproque

> Si a² + b² = c² alors le triangle est rectangle en C.

- **théorème** : on *sait* que l'angle est droit → on calcule une longueur
- **réciproque** : on ne connaît *que* les trois longueurs → on conclut sur l'angle, sans rapporteur

Le test **classe** même les triangles, *c* étant le plus grand côté :

| Comparaison | Angle en C |
|---|---|
| a² + b² **=** c² | droit |
| a² + b² **>** c² | aigu |
| a² + b² **<** c² | obtus |

Note:
La réciproque est ce qui rend Pythagore utile en code : on ne mesure pas un
angle, on compare deux sommes. Aucun appel trigonométrique, aucune racine.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/pythagore_widget.html#reciproque" data-background-interactive -->

Note:
Onglet « La réciproque » : on ne donne que trois longueurs, le triangle
est construit au compas (cas CCC). Dérouler les quatre étapes du panneau :
données → carrés → comparaison → conclusion. Presets : 9-12-15 (exercice 1),
4-5-6 (aigu), 4-5-8 (obtus), 3-4-9 (impossible : inégalité triangulaire).
Insister sur la différence théorème / réciproque / contraposée.

---

## Triplets pythagoriciens

Trois entiers qui vérifient a² + b² = c² :

```
3, 4, 5      5, 12, 13      8, 15, 17      7, 24, 25
```

- leurs multiples marchent aussi : 6-8-10, 9-12-15…
- la « corde à treize nœuds » des bâtisseurs : 12 intervalles → un angle droit sans équerre

---

## Pythagore dans un repère

Distance entre A(x₁, y₁) et B(x₂, y₂) — le triangle rectangle est fabriqué par les axes :

```
dx = x₂ − x₁
dy = y₂ − y₁
distance = √(dx² + dy²)
```

En 3D, un terme de plus, même formule :

```
distance = √(dx² + dy² + dz²)
```

Note:
Faire tracer dx et dy au tableau : la formule n'est rien d'autre que
Pythagore appliqué au triangle rectangle formé par le segment et les deux
axes. C'est la norme d'un vecteur, qu'on nommera ainsi à GVM-01.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/pythagore_widget.html#distance" data-background-interactive -->

Note:
Onglet « Distance dans un repère » : glisser le PNJ (A) et le joueur (B).
Le triangle rectangle est fabriqué par les axes. Le cercle de détection
montre qu'on compare d² à r², sans racine — transition vers la slide suivante.

---

## La racine carrée coûte cher

Pour **comparer** deux distances, la racine est inutile : elle est croissante.

```cpp
// mauvais : deux racines par test
if (std::sqrt(dx*dx + dy*dy) < range) { /* ... */ }

// bon : on compare les carrés
if (dx*dx + dy*dy < range * range) { /* ... */ }
```

C#/Unity : `Vector3.sqrMagnitude` plutôt que `Vector3.Distance`.

Note:
Règle pratique : la racine ne sert que si on a besoin de la valeur — barre
de vie, affichage, normalisation. Pour un test de portée, un tri par
proximité ou un rayon de détection, on reste au carré. Sur un millier
d'agents et par frame, la différence se mesure.

---

## À vous

1. Un triangle a pour côtés 9, 12 et 15. Est-il rectangle ?
2. Un PNJ est en (3, 7), le joueur en (8, 19). Le PNJ détecte à 15 m : voit-il le joueur ?
3. Quelle est la diagonale d'un écran 16:9 de 1600 px de large ?

Note:
Corrigé : (1) 81 + 144 = 225 = 15² → oui, rectangle. (2) dx=5, dy=12 →
25 + 144 = 169 ; 15² = 225 > 169 → il le voit (distance 13). (3) hauteur
900, diagonale = √(1600² + 900²) = √3 610 000 ≈ 1836 px.

---

# Thalès et similitude
<!-- .slide: class="title" -->

---

## Triangles semblables

Deux triangles sont **semblables** si leurs angles sont égaux deux à deux.

- leurs côtés sont alors **proportionnels** : un seul rapport *k* pour les trois
- critère suffisant : **deux** angles égaux (le troisième suit, somme = 180°)
- semblable ≠ égal : même forme, taille libre

```
a' / a = b' / b = c' / c = k
```

---

## Théorème de Thalès

Une droite parallèle à un côté coupe les deux autres en segments proportionnels.

Dans le triangle ABC, avec M sur [AB], N sur [AC] et (MN) ∥ (BC) :

```
AM / AB = AN / AC = MN / BC
```

- c'est la version « triangle emboîté » de la similitude
- la **réciproque** sert à prouver un parallélisme à partir des rapports

Note:
Thalès et similitude sont le même fait vu sous deux angles : un
agrandissement de centre A et de rapport k. Le dire explicitement évite de
les ranger dans deux cases séparées.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/thales_widget.html#thales" data-background-interactive -->

Note:
Widget interactif, trois onglets :
1. « Le théorème » : glisser A, B, C, puis M le long de (AB) ; N suit et
   (MN) reste parallèle à (BC). Les trois rapports restent égaux à k.
   Pousser M au-delà de A → configuration papillon ; au-delà de B → agrandissement.
   Le rapport des aires vaut k² : prépare la slide « Mise à l'échelle ».
2. « La réciproque » : M et N indépendants ; (MN) ∥ (BC) seulement quand
   AM/AB = AN/AC. Le point N′ montre où placer N.
3. « Mesurer sans mesurer » : l'exemple de l'ombre, slide suivante.

---

## Rapports de proportionnalité — exemple

Un bâtiment projette une ombre de 24 m ; un jalon de 1,80 m en projette une de 2,40 m au même instant.

```
h / 24 = 1,80 / 2,40 = 0,75
h = 24 × 0,75 = 18 m
```

Deux triangles semblables — mêmes rayons solaires, donc mêmes angles.

---

<!-- .slide: data-background-iframe="00 widgets/_widgets/thales_widget.html#ombre" data-background-interactive -->

Note:
Onglet « Mesurer sans mesurer » : mêmes valeurs que l'exemple (jalon 1,8 m,
ombre 2,4 m, ombre du bâtiment 24 m → 18 m). Faire varier la taille du
jalon ou l'heure (longueur de son ombre) : H change, le rapport reste le bon.

---

## Mise à l'échelle : ce qui change, et comment

Agrandissement de rapport *k* :

| Grandeur | Facteur |
|---|---|
| longueurs, périmètres | **k** |
| aires, surfaces | **k²** |
| volumes, masses | **k³** |

Les **angles**, eux, ne changent pas — la forme est conservée.

Note:
Le piège classique : « je double la taille de la texture » multiplie la
mémoire par 4, pas par 2. Idem pour une hitbox doublée : son aire
quadruple, son volume octuple — d'où les collisions qui « collent » après
un scale naïf.

---

## À retenir

- somme des angles = 180° ; inégalité triangulaire ; l'hypoténuse est le plus long côté
- **a² + b² = c²** dans un triangle rectangle — et la **réciproque** teste l'angle droit sans le mesurer
- distance dans un repère = Pythagore : √(dx² + dy²) ; pour **comparer**, rester au carré
- semblables = mêmes angles ⇒ côtés proportionnels de rapport *k*
- mise à l'échelle : longueurs ×k, aires ×**k²**, volumes ×**k³**

---

## Exercices

- classer des triangles avec la réciproque de Pythagore
- calculer des distances et des portées dans un repère
- résoudre deux configurations de Thalès
- convertir des rapports d'échelle en facteurs d'aire et de volume

Énoncés : [[01 courses/exercises/C++/TC-FT-TRG-01 - Géométrie du triangle]]

---

## Pour aller plus loin

- Séance suivante : [[01 courses/slides/Theory/TC-FT-TRG-02 - Cercle trigonométrique et unités|TC-FT-TRG-02 - Cercle trigonométrique et unités]]
- Widgets : [Droites remarquables](<00 widgets/_widgets/droites_remarquables_widget.html>) · [Pythagore — démonstration graphique](<00 widgets/_widgets/pythagore_widget.html>) · [Thalès — proportionnalité](<00 widgets/_widgets/thales_widget.html>)
- [Théorème de Pythagore — Wikipédia](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Pythagore)
- [Théorème de Thalès — Wikipédia](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Thal%C3%A8s)
