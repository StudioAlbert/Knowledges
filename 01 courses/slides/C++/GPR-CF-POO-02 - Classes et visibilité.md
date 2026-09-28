---
title: GPR-CF-POO-02 - Classes et visibilité
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Programmation Orientée Objet
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

# Classes et visibilité
<!-- .slide: class="title" -->
## GPR-CF-POO-02

<small>Ce que l'objet montre, ce qu'il garde</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir écrire une classe, choisir ce qui est public, et faire tenir une règle du jeu par l'objet lui-même.

**Prérequis :** structures — [[01 courses/slides/C++/GPR-CF-POO-01 - Structures|GPR-CF-POO-01]].

---

## Une structure que n'importe qui peut casser

Si tout le code peut écrire `pv = -50`, la règle « on ne descend pas sous zéro » n'existe nulle part.

---

## Public et privé

Le privé n'est pas du secret : c'est la promesse que personne ne contournera la règle.

---

## `class` ou `struct`

Le seul écart est la visibilité par défaut ; le choix du mot dit l'intention.

---

## Méthodes

Une méthode est une fonction qui vit dans l'objet et connaît ses données.

---

## L'interface, c'est ce qui est public

L'extérieur demande `subirDegats(12)` et non l'accès direct au compteur.

> [!tip] Widget — `encapsulation_widget.html`
> Un `Joueur` dessiné en deux zones, publique et privée. On tente d'écrire directement dans
> le compteur de vie depuis l'extérieur : le widget affiche l'erreur de compilation. En
> passant par la méthode, la valeur est bornée et le widget montre la règle qui s'applique.

---

## Pourquoi cacher

Ce qui est caché peut changer demain sans casser le reste du jeu.

---

## Accesseurs, et quand s'en passer

Un accesseur qui ne fait que rendre le champ n'encapsule rien : c'est le comportement qu'il faut exposer.

---

## Classe et instance

La classe est le plan, l'instance est la maison — et il peut y en avoir mille.

---

## Le vocabulaire

Attribut, méthode, instance, interface, encapsulation : les mots qu'on emploiera jusqu'à la fin de l'année.

---

## Atelier — 20 min

Transformer la structure `Monstre` de la séance précédente en classe qui garantit des points de vie toujours valides.

---

## À retenir

Les données au privé, le comportement au public — et chaque règle du jeu tenue par l'objet qui la porte.

---

## Questions ?
