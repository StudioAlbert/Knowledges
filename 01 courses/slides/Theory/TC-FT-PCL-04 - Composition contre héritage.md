---
title: TC-FT-PCL-04 - Composition contre héritage
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Principes de Conception Logicielle
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

# Composition contre héritage
<!-- .slide: class="title" -->
## TC-FT-PCL-04

<small>Assembler plutôt que classer</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir reconnaître une hiérarchie qui ne tient plus, la remplacer par des composants, et nommer le principe de l'ECS.

**Prérequis :** héritage — [[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme|GPR-CF-POO-06]].

---

## L'arbre qui ne pousse plus

Une hiérarchie décrit bien le monde qu'on imaginait au début, et mal celui qu'on a maintenant.

---

## Le cas qui ne rentre pas

L'ennemi volant qui tire et se soigne : trois capacités, et déjà huit classes à écrire.

> [!tip] Widget — `composition_widget.html`
> À gauche, des cases à cocher de capacités — voler, tirer, se soigner, invisible. À droite,
> deux compteurs : le nombre de classes qu'exigerait l'héritage pour couvrir toutes les
> combinaisons, et le nombre de composants nécessaires. L'écart devient absurde à la
> quatrième capacité.

---

## Assembler au lieu d'hériter

Une capacité devient une pièce qu'on ajoute ou qu'on retire, pas un rang dans un arbre.

---

## Le modèle composant

Unity est construit là-dessus : un `GameObject` n'est rien d'autre qu'une liste de composants.

---

## Ce que ça change à l'écriture

Chaque composant ignore les autres, et l'objet n'est plus qu'un assemblage décrit par des données.

---

## Orientation données

Séparer ce que l'objet est de ce qu'on lui fait subit : les données d'un côté, les traitements de l'autre.

---

## Le principe de l'ECS

Des entités sans comportement, des composants sans logique, des systèmes qui traitent des lots homogènes.

> [!tip] Schéma
> Trois bandes horizontales — entités, composants rangés par type en tableaux contigus,
> systèmes qui balaient chaque tableau — avec la mémoire dessinée pour montrer pourquoi le
> parcours est rapide.

---

## Quand l'héritage reste juste

Une vraie relation « est un », stable et peu profonde, se laisse hériter sans regret.

---

## Ce que coûte la composition

Plus de petits objets, un ordre d'exécution à décider, et une indirection de plus à chaque appel.

---

## Atelier — 20 min

Reprendre la hiérarchie d'ennemis du groupe, compter les classes qu'exigerait une capacité de plus, puis la refaire en composants.

---

## À retenir

L'héritage classe, la composition assemble — et dès que les capacités se combinent, c'est la composition qui gagne.

---

## Questions ?
