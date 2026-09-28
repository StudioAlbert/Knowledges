---
title: GPR-UN-VRG-16 - Shader Graph — composer un matériau
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

# Shader Graph — composer un matériau
<!-- .slide: class="title" -->
## GPR-UN-VRG-16

<small>Écrire un shader en le branchant</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir se repérer dans Shader Graph, brancher les nœuds usuels, et exposer des réglages utilisables par un designer.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-VRG-14 - Shaders, matériaux, textures, UV|GPR-UN-VRG-14]].

---

## Un shader sans écrire de code

Les mêmes opérations qu'en HLSL, mais posées et reliées — et vérifiables à l'œil.

---

## L'interface

Quatre zones : le tableau des propriétés, le graphe, l'aperçu, et la pile de sortie.

---

## La pile de sortie

C'est elle qui décide ce que le shader produit vraiment : couleur, transparence, normale, émission.

---

## Les nœuds qu'on utilise tous les jours

Échantillonner une texture, multiplier, mélanger, lire le temps, lire les coordonnées.

---

## Brancher une couleur

Une texture multipliée par une teinte : le premier matériau utile tient en trois nœuds.

> [!tip] Widget — `shadergraph_widget.html`
> Un mini éditeur de nœuds : texture, couleur, multiplication, mélange, temps. L'étudiant
> relie les sorties aux entrées et un aperçu rend le résultat en direct sur un quad. Les
> branchements impossibles sont refusés avec la raison.

---

## Exposer une propriété

Une propriété exposée devient un réglage du matériau : le designer travaille sans rouvrir le graphe.

---

## L'aperçu, nœud par nœud

Chaque nœud montre ce qu'il produit : c'est le débogueur de Shader Graph.

---

## Matériau et shader

Un shader, mille matériaux : ce qui change d'un matériau à l'autre, ce sont les propriétés.

---

## Ce que ça coûte

Le prix se compte en échantillonnages de texture et en opérations par pixel, pas en nœuds à l'écran.

---

## Les variantes

Un mot-clé crée deux versions compilées du shader : pratique, et vite ruineux.

---

## Atelier — 20 min

Composer le matériau d'un bloc de glace : texture, teinte exposée, transparence réglable, et léger défilement.

---

## À retenir

La pile de sortie dit ce qu'on produit, les propriétés exposées servent le designer, et le coût se compte par pixel.

---

## Questions ?
