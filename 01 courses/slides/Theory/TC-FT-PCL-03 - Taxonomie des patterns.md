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

C'est le **nom** donné à une solution qui revient.

- il ne se copie pas : il se reconnaît, puis s'adapte
- sa vraie valeur est le **vocabulaire** : dire « c'est un Observer » en trois mots
- deux personnes qui le connaissent s'épargnent une demi-heure de dessin

Un pattern mal nommé reste un bon code. Un pattern appliqué sans problème est une dette.

---

## D'où ça vient

Vingt-trois patrons publiés en **1994** par le *Gang of Four*, pour le C++ et
Smalltalk de l'époque.

Depuis, **la moitié se sont fondus dans les langages** : ce qui demandait une
classe est devenu un mot-clé.

---

## Ceux que le langage a avalés

| Patron de 1994 | Ce qui l'a remplacé |
|---|---|
| **Iterator** | `for (auto& x : v)`, `foreach`, les générateurs |
| **Strategy** | une lambda, `std::function`, un `delegate` |
| **Command** | une lambda qu'on stocke dans une liste |
| **Observer** | `event` en C#, `UnityEvent`, les signaux |
| **Prototype** | `clone()`, `ICloneable`, les copies de valeur |

L'argument est de Paul Graham : un patron signale souvent ce qui **manque** au langage.

Note:
C'est la critique que `refactoring.guru` documente. Elle est juste, et elle ne
disqualifie pas le reste : State, Component et Object Pool n'ont aucun équivalent
en mot-clé, et c'est pour ça qu'ils sont dans la liste des six.

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

## State

- **le problème** — un comportement à phases, où chaque phase change les règles
- **comment** — une classe par état, un seul état courant, des transitions nommées
- **la métaphore** — un feu tricolore : jamais vert et rouge à la fois

Il remplace le tas de booléens qui finissent par décrire un état impossible.

---

## Strategy

- **le problème** — plusieurs façons de faire la même chose, à choisir **pendant** le jeu
- **comment** — l'algorithme sort dans un objet derrière une interface, qu'on échange
- **la métaphore** — un GPS : même trajet, « le plus rapide » ou « sans péage »

Trois IA d'ennemi interchangeables selon les points de vie.

---

## Command

- **le problème** — une action qu'il faut garder, rejouer, défaire ou réassigner
- **comment** — l'action devient un objet, avec `Execute` et `Undo`
- **la métaphore** — un ticket de restaurant : il existe sans le client ni le cuisinier

C'est ce qui rend possibles l'annulation et la reconfiguration des touches.

---

## Object Pool

- **le problème** — beaucoup d'objets courts, dont la création coûte plus que l'usage
- **comment** — une réserve allouée une fois, et des objets recyclés au lieu d'être détruits
- **la métaphore** — la vaisselle d'un restaurant : on la lave, on ne la jette pas

Trois cents projectiles par seconde, et le framerate qui tient.

---

## Component

- **le problème** — des capacités qui se **combinent**, et un arbre d'héritage qui explose
- **comment** — chaque capacité devient une pièce ajoutée à une entité neutre
- **la métaphore** — des briques : on assemble, on ne fabrique pas la brique parfaite

C'est le sujet entier de [[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage|PCL-04]].

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

## À retenir

- trois familles, trois questions : **qui crée**, **comment s'emboîter**, **comment se parler**
- six patterns couvrent l'essentiel d'un jeu ; les autres sont sur la carte, pas au programme
- la moitié des patrons de 1994 sont devenus des **mots-clés**
- le problème se nomme **avant** la solution — toujours

---

# Questions ?
<!-- .slide: class="title" -->

### Prochaine séance

<small>[[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage|TC-FT-PCL-04]] — le pattern Component, en entier.</small>
