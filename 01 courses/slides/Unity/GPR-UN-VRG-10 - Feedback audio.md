---
title: GPR-UN-VRG-10 - Feedback audio
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

# Feedback audio
<!-- .slide: class="title" -->
## GPR-UN-VRG-10

<small>Le retour que le joueur n'oublie pas</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir faire confirmer une action par le son, éviter la bouillie sonore, et hiérarchiser les voix.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-VRG-09 - Feedback d'interface|GPR-UN-VRG-09]].

---

## Le son confirme

Un clic sans son laisse un doute ; le même clic sonore ne se questionne pas.

---

## La latence perçue

Le son est le retour le plus sensible au retard : quelques dizaines de millisecondes se sentent.

---

## Parfois avant l'image

Une amorce sonore juste avant l'impact fait paraître le coup plus net qu'il ne l'est.

---

## La superposition

Vingt tirs identiques dans la même seconde ne donnent pas vingt tirs mais du bruit.

> [!tip] Widget — `saturation_audio_widget.html`
> Un curseur de nombre de sons simultanés et un compteur de voix. Avec variation de hauteur
> et limitation du nombre d'instances, la rafale reste lisible ; sans, le vumètre sature et
> le son devient une masse. Un bouton compare les deux à l'oreille.

---

## La variation

Hauteur, volume, et deux ou trois échantillons alternatifs suffisent à effacer la répétition.

---

## Les priorités

Quand il n'y a plus de voix disponible, il faut savoir quel son doit passer devant.

---

## L'espace

Panoramique et atténuation disent où se passe l'action sans que le joueur regarde.

---

## Le silence

Couper le son avant un moment fort le rend plus fort que n'importe quel ajout.

---

## Le mixage

Des catégories, des volumes indépendants, et un abaissement automatique quand une voix parle.

---

## Atelier — 20 min

Donner au prototype ses sons d'action avec variation, une limite d'instances par son, et trois catégories de mixage.

---

## À retenir

Le son confirme immédiatement, la variation évite la répétition, la limitation évite la bouillie, et le silence reste un outil.

---

## Questions ?
