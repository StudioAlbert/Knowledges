---
title: GPR-UN-VRG-18 - Particle Systems
type: slides
status: Backlog
subject: Unity
duration_h: 1
bloc_gsda: VFX, Rendu et Game Feel
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

# Particle Systems
<!-- .slide: class="title" -->
## GPR-UN-VRG-18

<small>Beaucoup de petites choses, et un budget</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement. Dernière séance du bloc.

---

## Objectifs

Savoir construire un effet de particules par modules, le régler en courbes, et connaître ce qui le rend cher.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-VRG-14 - Shaders, matériaux, textures, UV|GPR-UN-VRG-14]].

---

## Beaucoup de petites choses

Fumée, étincelles, poussière, sang, magie : le même outil pour tout ce qui n'a pas de forme fixe.

---

## Les modules

Chaque module ajoute une couche de comportement, et l'ordre dans lequel ils s'appliquent compte.

---

## L'émission

Un débit continu, des rafales, ou les deux : c'est le premier réglage qui décide de l'allure.

---

## La forme d'émission

D'où sortent les particules : un point, un cône, une sphère, le bord d'un maillage.

---

## Tout se règle en courbes

Taille, couleur, vitesse, rotation : chacune évolue sur la durée de vie, et c'est là que se joue la crédibilité.

> [!tip] Widget — `particules_widget.html`
> Un système minimal avec aperçu en direct : débit, rafale, forme, et trois courbes de durée
> de vie éditables. Un compteur affiche le nombre de particules vivantes et la surface
> d'écran couverte, avec un avertissement quand le remplissage explose.

---

## Le rendu

Face caméra, maillage, ou traînée : trois façons de dessiner la même particule.

---

## Tri et transparence

Les particules transparentes se dessinent dans un ordre, et cet ordre se voit quand il est faux.

---

## Ce que ça coûte

Pas le nombre de particules, mais la surface d'écran qu'elles recouvrent — et combien de fois.

---

## L'intégration au pipeline

Le matériau des particules dépend du pipeline choisi, et les outils modernes vivent à côté du système historique.

---

## Quand une particule n'est pas la réponse

Pour une traînée nette ou une onde régulière, un shader coûte moins et se contrôle mieux.

---

## Atelier — 20 min

Construire l'impact d'un coup : une rafale d'étincelles, un nuage de poussière, une traînée — sous budget de remplissage.

---

## À retenir

Des modules empilés, des courbes de durée de vie, un tri correct, et un budget qui se compte en pixels recouverts.

---

## Questions ?
