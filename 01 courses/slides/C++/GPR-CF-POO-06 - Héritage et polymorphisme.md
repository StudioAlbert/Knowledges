---
title: GPR-CF-POO-06 - Héritage et polymorphisme
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

# Héritage et polymorphisme
<!-- .slide: class="title" -->
## GPR-CF-POO-06

<small>Un seul appel, plusieurs comportements</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Dernière séance du bloc POO.

---

## Objectifs

Savoir factoriser par héritage, comprendre ce que `virtual` change à l'appel, et écrire une classe abstraite.

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-05 - Static et surcharge d'opérateur|GPR-CF-POO-05]].

---

## Trois ennemis, 80 % de code identique

Gobelin, archer et golem se déplacent et perdent des points de vie de la même façon.

---

## Hériter

L'enfant reçoit tout ce que le parent possède, et ajoute ce qui lui est propre.

---

## Les deux points à retenir

Un gobelin **est un** ennemi, et le constructeur du parent s'exécute avant celui de l'enfant.

---

## Mode d'héritage

En public, la relation « est un » est visible de tous ; autrement, elle reste une affaire interne.

---

## Héritage multiple

Hériter de deux parents qui partagent un aïeul amène le diamant, et les questions qui vont avec.

> [!tip] Schéma
> Le diamant classique en quatre classes, avec la donnée de l'aïeul dessinée en double, puis
> la même hiérarchie remplacée par une seule base et une interface.

---

## `virtual`

Sans `virtual`, c'est le type écrit dans le code qui décide ; avec, c'est le type réel de l'objet.

---

## Le dispatch en action

Un tableau de pointeurs vers la base, un seul appel, et chaque objet fait ce qu'il sait faire.

> [!tip] Widget — `dispatch_widget.html`
> Une liste de cinq ennemis de types différents derrière des pointeurs de base. Le bouton
> « attaquer » montre quelle implémentation s'exécute pour chacun, et un interrupteur
> `virtual` fait basculer tout le monde sur la version de la base pour montrer la différence.

---

## Méthode virtuelle pure

Une base qui déclare sans implémenter devient abstraite : on ne peut plus l'instancier, et c'est voulu.

---

## Le destructeur virtuel

Détruire un enfant par un pointeur de base sans destructeur virtuel laisse la moitié du travail en plan.

---

## Atelier — 20 min

Factoriser gobelin, archer et golem sous une base abstraite `Ennemi`, puis les faire attaquer depuis un seul tableau.

---

## À retenir

L'héritage factorise ce qui est commun, `virtual` laisse l'objet décider, la classe abstraite fixe le contrat — et le destructeur est virtuel.

---

## Questions ?
