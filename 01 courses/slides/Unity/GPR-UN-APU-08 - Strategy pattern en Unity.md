---
title: GPR-UN-APU-08 - Strategy pattern en Unity
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

# Strategy pattern en Unity
<!-- .slide: class="title" -->
## GPR-UN-APU-08

<small>Changer de comportement sans changer de code</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir sortir un comportement d'une classe pour le rendre interchangeable, et le confier au designer via un asset.

**Prérequis :** interfaces et injection — [[01 courses/slides/Unity/GPR-UN-APU-01 - SOLID en Unity|GPR-UN-APU-01]].

---

## Le `switch` qui grossit à chaque arme

Ajouter le lance-roquettes demande de rouvrir la classe du joueur, qui ne devrait rien savoir des armes.

---

## Le comportement devient un objet

Tirer n'est plus une branche du `switch` mais une chose qu'on peut tenir, ranger, échanger.

---

## L'interface de stratégie

Une seule méthode, un contrat minimal : le tireur ne connaît que ça.

---

## Brancher la stratégie

Le joueur reçoit sa stratégie de l'extérieur et ne la crée jamais lui-même.

---

## La stratégie en `ScriptableObject`

Chaque arme devient un asset réglable dans l'inspecteur, sans recompiler.

> [!tip] Widget — `strategy_widget.html`
> Un tireur au centre et trois assets d'armes à gauche — pistolet, fusil à pompe, laser. On
> glisse un asset dans l'emplacement et le motif de tir change immédiatement, sans que le
> code du tireur, affiché à droite, ne bouge d'une ligne.

---

## Changer à l'exécution

Ramasser une arme, c'est remplacer une référence — rien de plus.

---

## Le même moteur pour l'IA

Agressif, peureux, soutien : trois stratégies de décision derrière la même interface.

---

## Strategy ou State

Strategy remplace un comportement de l'extérieur, State enchaîne des comportements de l'intérieur.

> [!tip] Schéma
> Deux petits diagrammes côte à côte : à gauche, un objet avec trois stratégies
> interchangeables et une flèche venant de l'extérieur ; à droite, trois états reliés par
> des transitions internes.

---

## Ce que ça coûte

Un fichier de plus par comportement, une indirection à l'appel, et un projet qui se lit mieux.

---

## Atelier — 20 min

Sortir les trois armes du `switch` du Dungeon Crawler vers trois assets de stratégie, et les échanger au ramassage.

---

## À retenir

Une interface courte, des stratégies en assets, une référence injectée — et le comportement se choisit sans toucher au code.

---

## Questions ?
