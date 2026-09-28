---
title: GPR-UN-APU-09 - Observer, State et composition
type: slides
status: Backlog
subject: Unity
duration_h: 1
bloc_gsda: Architecture et Patterns Unity
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

# Observer, State et composition
<!-- .slide: class="title" -->
## GPR-UN-APU-09

<small>Trois outils pour découpler un gameplay</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase par slide ; widgets et schémas
décrits seulement. Séance de clôture du bloc : elle rejoue SOLID sur des cas concrets.

---

## Objectifs

Savoir prévenir sans connaître son destinataire, découper un comportement en états, et assembler un personnage au lieu de l'hériter.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-APU-01 - SOLID en Unity|GPR-UN-APU-01]] et le Strategy pattern de `GPR-UN-APU-08`.

---

## Le problème : qui prévenir quand le joueur perd un PV

Si `PlayerHealth` appelle lui-même le HUD, le son et la caméra, il dépend de tout le jeu.

> [!tip] Schéma
> À gauche, `PlayerHealth` avec quatre flèches sortantes vers HUD, audio, caméra, succès.
> À droite, la même scène avec un seul événement au centre. Le nombre de flèches qui
> traversent le schéma est l'argument.

---

## Observer : publier, s'abonner

Celui qui sait qu'un événement a eu lieu l'annonce ; ceux que ça intéresse s'inscrivent.

---

## Trois façons de le faire en Unity

`event Action` en C# pur, `UnityEvent` exposé dans l'inspecteur, ou un ScriptableObject qui sert de canal partagé.

> [!tip] Widget — `observer_bus_widget.html`
> Un bus d'événements dessiné au centre, quatre abonnés autour. Le bouton « le joueur
> prend un coup » propage l'événement et allume les abonnés dans l'ordre d'inscription ;
> on peut désabonner un objet et voir ce qui cesse de réagir.

---

## Le piège : l'abonné qui survit

Un abonnement jamais retiré garde en vie un objet détruit — `OnDisable` est l'endroit où on se désabonne.

---

## State : un comportement par état

Plutôt qu'un `if` qui grossit à chaque cas, chaque état devient une classe qui sait entrer, agir et sortir.

---

## La machine à états d'un garde

Patrouille, Alerte, Poursuite, Retour : quatre états, et des transitions nommées.

> [!tip] Widget — `state_machine_widget.html`
> La machine du garde en graphe. Les boutons *bruit entendu*, *joueur vu*, *joueur perdu*,
> *timer écoulé* déclenchent les transitions ; l'état courant s'illumine et le widget
> refuse les transitions impossibles en expliquant pourquoi.

---

## Composition plutôt qu'héritage

Un ennemi n'hérite pas de ses capacités : il les porte, un composant à la fois.

> [!tip] Schéma
> Une hiérarchie `Enemy → FlyingEnemy → FlyingShootingEnemy` barrée, et en face le même
> ennemi comme une liste de composants cochables : *vol*, *tir*, *bouclier*, *butin*.

---

## Le catalogue minimal d'un projet Unity

Observer pour les annonces, State pour les comportements, Strategy pour les variantes, composition pour tout le reste.

---

## Atelier — 20 min

Sur le Dungeon Crawler : remplacer un `if / else if` de garde par deux états, et brancher le HUD sur un événement au lieu d'un `FindObjectOfType`.

---

## À retenir

Un objet qui annonce ne doit pas savoir qui écoute, un comportement qui change d'état ne doit pas grossir, et une capacité s'ajoute sans toucher au reste.

---

## Questions ?
