---
title: TC-FT-PCL-03 - Taxonomie des patterns
type: slides
subject: Theory
duration_h: 1
bloc_gsda: Principes de Conception Logicielle
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

# Taxonomie des patterns
<!-- .slide: class="title" -->

### Une carte, pas un catalogue à appliquer

<small>TC-FT-PCL-03 · Principes de Conception Logicielle</small>

Note:
PCL-01 a donné les deux mots — couplage, cohésion. Cette séance donne les noms
des réponses déjà écrites. Le danger de la séance est connu : repartir avec
l'envie de tout appliquer. La dernière partie est là pour ça.

---

## Objectifs

À la fin de la séance, vous savez :

- ranger un pattern dans sa **famille**
- nommer les **six** qu'on croise vraiment dans un jeu
- dire, pour chacun, **quel problème** il résout
- reconnaître quand **s'en passer**

**Prérequis :** [[01 courses/slides/Theory/TC-FT-PCL-01 - Couplage et cohésion|TC-FT-PCL-01]].

---

# Ce qu'est un pattern
<!-- .slide: class="title" -->

---

## Ce n'est pas une recette

Une **recette** donne des étapes qui mènent au résultat — c'est un algorithme.
Un **plan** montre ce qu'on obtient, et laisse la construction à qui le lit.

- un pattern est un plan : il se reconnaît, puis s'adapte
- deux programmes qui l'appliquent n'ont **pas le même code**
- sa vraie valeur est le **vocabulaire** : « c'est un Observer », en trois mots

Un pattern mal nommé reste un bon code.

Un pattern appliqué sans **problème à résoudre** est une dette.

Note:
La distinction patron / algorithme vient de `refactoring.guru`, et c'est la plus
utile de la séance : ils chercheront tous un bout de code à coller. Leur dire
qu'une description de patron tient en quatre sections — intention, motivation,
structure, exemple de code — et que seule la dernière ressemble à du code.

---

## D'où ça vient

Vingt-trois patrons publiés en **1994** par le *Gang of Four*, pour le C++ et
Smalltalk de l'époque.

Peter Norvig en a compté **16 sur 23** « invisibles ou plus simples » dans un
langage plus expressif. Ce qui demandait une classe est souvent devenu un mot-clé.

---

## Ceux que le langage a avalés

| Patron de 1994 | Ce qui l'a remplacé |
|---|---|
| **Iterator** | `for (auto& x : v)`, `foreach`, les générateurs |
| **Strategy** | une lambda, `std::function`, un `delegate` |
| **Command** | une lambda qu'on stocke dans une liste |
| **Observer** | `event` en C#, `UnityEvent`, les signaux |
| **Prototype** | `clone()`, `ICloneable`, les copies de valeur |

Qui dit quoi, et où lire la suite :
[[01 courses/resources/Theory/TC-FT-PCL-03 - Ressources|la fiche de ressources]].

Note:
C'est la critique que `refactoring.guru` documente, et elle a deux auteurs
distincts qu'il ne faut pas confondre. Le compte de 16 sur 23 est de **Peter
Norvig** (1996). La phrase sur l'abstraction trop faible est de **Paul Graham**,
dans *Revenge of the Nerds* (2002) : voir la fiche de ressources. Elle est juste,
et elle ne disqualifie pas le reste — State, Component et Object Pool n'ont aucun
équivalent en mot-clé, et c'est pour ça qu'ils sont dans la liste des six.

---

# Trois familles
<!-- .slide: class="title" -->

---

## La carte
<!-- .slide: class="schema" -->

Créer des objets, les assembler, les faire se parler : toute la taxonomie tient là.

![[pcl03_trois_familles.svg]]

---

## Les trois questions

- **Création** — qui décide quel objet naît, et où ce choix est-il écrit ?
- **Structure** — comment des objets s'emboîtent pour n'en présenter qu'un ?
- **Comportement** — comment se répartir une décision sans se connaître ?

Ranger un pattern, c'est répondre à une de ces trois questions. Rien de plus.

---

# Les six du quotidien
<!-- .slide: class="title" -->

---

## Observer

- **le problème** — un émetteur, un nombre d'intéressés inconnu à l'écriture
- **comment** — l'émetteur tient une liste d'abonnés et les prévient, sans savoir qui ils sont
- **la métaphore** — une liste de diffusion : on écrit une fois, chacun reçoit

Les points de vie baissent : la barre, le son, l'animation et le succès réagissent.

---

## Un sujet, quatre abonnés
<!-- .slide: class="schema" -->

L'émetteur ne connaît aucun des quatre, et le cinquième ne lui coûtera rien.

![[pcl03_observer.svg]]

---

## State

- **le problème** — un comportement à phases, où chaque phase change les règles
- **comment** — une classe par état, un seul état courant, des transitions nommées
- **la métaphore** — un feu tricolore : jamais vert et rouge à la fois

Il remplace le tas de booléens qui finissent par décrire un état impossible.

---

## Un état courant, des transitions nommées
<!-- .slide: class="schema" -->

À gauche l'automate du héros, à droite les booléens qu'il remplace.

![[pcl03_state.svg]]

---

## Strategy

- **le problème** — plusieurs façons de faire la même chose, à choisir **pendant** le jeu
- **comment** — l'algorithme sort dans un objet derrière une interface, qu'on échange
- **la métaphore** — un GPS : même trajet, « le plus rapide » ou « sans péage »

Trois IA d'ennemi interchangeables selon les points de vie.

---

## Trois comportements, une seule signature
<!-- .slide: class="schema" -->

L'ennemi tient un objet derrière une interface — et son code ne change jamais.

![[pcl03_strategy.svg]]

---

## Command

- **le problème** — une action qu'il faut garder, rejouer, défaire ou réassigner
- **comment** — l'action devient un objet, avec `Execute` et `Undo`
- **la métaphore** — un ticket de restaurant : il existe sans le client ni le cuisinier

C'est ce qui rend possibles l'annulation et la reconfiguration des touches.

---

## La pile d'annulation
<!-- .slide: class="schema" -->

Une fois que l'action est un objet, on peut l'empiler, la rejouer et la défaire.

![[pcl03_command.svg]]

---

## Object Pool

- **le problème** — beaucoup d'objets courts, dont la création coûte plus que l'usage
- **comment** — une réserve allouée une fois, et des objets recyclés au lieu d'être détruits
- **la métaphore** — la vaisselle d'un restaurant : on la lave, on ne la jette pas

Trois cents projectiles par seconde, et le framerate qui tient.

---

## Seize cases, allouées une fois
<!-- .slide: class="schema" -->

Pendant la partie, on prend une case libre et on la rend : rien n'est créé ni détruit.

![[pcl03_object_pool.svg]]

---

## Component

- **le problème** — des capacités qui se **combinent**, et un arbre d'héritage qui explose
- **comment** — chaque capacité devient une pièce ajoutée à une entité neutre
- **la métaphore** — des briques : on assemble, on ne fabrique pas la brique parfaite

C'est le sujet entier de [[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage|PCL-04]].

---

## Deux entités, les mêmes pièces
<!-- .slide: class="schema" -->

« Vie » et « Rendu » sont écrits une fois et servent aux deux ; la caisse n'hérite de rien.

![[pcl03_component.svg]]

---

# Savoir s'en passer
<!-- .slide: class="title" -->

---

## Le pattern de trop

Deux ennemis à instancier, toujours les mêmes, connus à l'écriture.

- une fabrique abstraite : une interface, deux fabriques, trois fichiers
- le problème qu'elle résout — « et si on changeait de famille d'ennemis ? » — **n'existe pas**
- le coût, lui, existe : un niveau d'indirection, et un vocabulaire à expliquer

> Si tout ce que vous avez est un marteau, tout ressemble à un clou.

---

## Le principe YAGNI

*You Aren't Gonna Need It* — n'écrire que ce que le projet demande **aujourd'hui**.
Une fonctionnalité anticipée se paie **quatre fois** :

- **construction** — le temps passé à la penser, l'écrire et la tester
- **retard** — ce qui n'est pas livré pendant qu'on l'écrit
- **portage** — tout le reste devient plus lent à modifier
- **réparation** — la dette : on corrige longtemps une décision prise trop tôt

YAGNI retarde l'implémentation ; il n'interdit pas de **bien concevoir**.

Note:
Les quatre coûts sont ceux de la page GeeksforGeeks citée dans la fiche de
ressources, remis en français et en quatre mots. La dernière ligne est la nuance
que la même page insiste à poser, et c'est elle qu'il faut dire à voix haute :
retirer une abstraction qui sert **déjà** n'est pas du YAGNI, c'est un
appauvrissement. YAGNI est le cousin de KISS.

---

## Comment choisir

1. **nommer le problème** — en une phrase, sans nom de pattern dedans
2. écrire la version **simple**, et la faire marcher
3. attendre que le problème se **répète** — deux fois, pas une
4. **alors** chercher le pattern, et vérifier qu'il répond à la phrase du 1

Le pattern est une réponse. Sans question écrite, il n'y a rien à répondre.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/patterns_quizz_widget.html" data-background-interactive -->

Note:
Sept situations, à faire ensemble en fin de séance. Laisser proposer à voix haute
avant de cliquer. La septième est celle qui compte : la bonne réponse est
« aucun », et la moitié de la salle choisira une fabrique.

---

## Atelier — 20 min

**Concevoir un platformer**, deuxième passe : reprendre le schéma dessiné en
PCL-01, et y chercher des patterns.

1. une boîte à la fois : **peut-on en reconnaître un ?** Les six, et pas d'autres
2. pour chacun trouvé, écrire les **trois entrées** — le problème, le comment, la métaphore
3. trouver au moins **un endroit où la réponse est non**, et dire lequel vous tentait
4. si vous n'en voyez aucun, dire **ce qui devrait changer** dans le jeu pour qu'il en faille un

Énoncé : [[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer|Concevoir un platformer]].

---

## À retenir

- trois familles, trois questions : **qui crée**, **comment s'emboîter**, **comment se parler**
- six patterns couvrent l'essentiel d'un jeu ; les autres sont sur la carte, pas au programme
- beaucoup des patrons de 1994 sont devenus des **mots-clés**
- le problème se nomme **avant** la solution — toujours

---

# Questions ?
<!-- .slide: class="title" -->
