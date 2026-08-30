---
title: PCG — Exercices
type: exercice
bloc: "[[Fondamentaux de la génération procédurale]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
source_slides: https://docs.google.com/presentation/d/16PDth6PeUJceHoB_TrW-9kfZOTr6QehSmzn1F0_M1s8/edit
---

# Procedural Generation
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Exercices

<small>Quatre ateliers, à faire dans l'ordre, en accompagnement des cours
[[pcg_introduction|Introduction]] et [[pcg_graph_cellular_automaton|Graphs & Cellular Automata]]</small>

Note:
Ces exercices ne portent pas d'heures au curriculum : ils se font pendant et
entre les cours. Chacun tient en une séance de TP.

---

# Generative Map I
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

### Perlin noise map

1. Utiliser une fonction aléatoire pour générer une carte **noir et blanc**
2. Regénérer la même carte avec un **algorithme de bruit**
3. Peux-tu **équilibrer** la fonction pour obtenir davantage de cases blanches ?

<small>Cours de référence : [[pcg_introduction]], slides *Random numbers* et
*Noise: Perlin*</small>

Note:
La question 3 est la vraie : le seuil appliqué au bruit est un paramètre de
design, pas une constante. Faire varier le seuil en direct devant la classe.

---

# Generative Map II
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

### Cellular automaton

1. Remplir une grille de **10 x 10** cases avec l'automate cellulaire
2. Quelles sont les **limites** de cette méthode ?
3. Résoudre le problème avec un **flood fill**

<small>Cours de référence : [[pcg_graph_cellular_automaton]], seconde moitié</small>

Note:
La réponse attendue en 2 : cavernes déconnectées, poches trop petites, et une
grille de 10x10 trop petite pour que les règles convergent joliment. Le flood
fill règle les deux premiers points ; le troisième s'apprend en agrandissant la
grille.

---

# Markov chains
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Construire une chaîne de Markov capable de **générer des noms de lieux** selon
les règles ci-dessous :

```text
   The --> Lord ---> of ---> Golden   ---> Lagoon
       `-> Prince -'    |--> Silver   ---> Forest
                        |--> Blue     ---> Castle
                        `--> Vanished
```

Deux variantes à produire :

1. **probabilités égales**
2. **probabilités pondérées** — un nom rare doit se sentir rare

---

### Markov chains — suite

Les deux générateurs demandés en cours :

1. Générer une **météo** — la chaîne à deux états du cours
2. Générer un **pool d'ennemis** sous **budget génératif**

<small>Le budget est la partie intéressante : la chaîne propose, le budget
dispose.</small>

Note:
Pour le pool d'ennemis : chaque ennemi coûte des points, la vague dispose d'un
budget total, et la chaîne de Markov décide de l'enchaînement des types. C'est
le premier générateur *sous contrainte* que les étudiants écrivent.

---

# Parcours d'arbre
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

1. Constituer un **arbre de nœuds** — peux-tu le **visualiser dans Unity** ?
2. Comparer une recherche en **BFS** et en **DFS**
3. **Tilemap painting** : peindre la tilemap au rythme de chacun des deux parcours

<small>Cours de référence : [[pcg_graph_cellular_automaton]], slides *BFS* / *DFS*</small>

Note:
Le point 3 est le plus pédagogique : peindre les cases dans l'ordre de visite
rend la différence entre les deux parcours immédiatement lisible, là où deux
listes de nombres ne disent rien. Ralentir la peinture avec une coroutine.
