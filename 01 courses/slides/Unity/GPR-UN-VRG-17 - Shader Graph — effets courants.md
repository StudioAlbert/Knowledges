---
title: GPR-UN-VRG-17 - Shader Graph — effets courants
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

# Shader Graph — effets courants
<!-- .slide: class="title" -->
## GPR-UN-VRG-17

<small>Cinq recettes qui servent partout</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir composer les cinq effets de shader les plus utilisés en jeu, et connaître leur prix.

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-VRG-16 - Shader Graph — composer un matériau|GPR-UN-VRG-16]].

---

## Cinq recettes couvrent l'essentiel

Défilement, dissolution, fresnel, distorsion, flash : avec ça, on habille un jeu entier.

---

## Le défilement d'UV

Ajouter le temps aux coordonnées de texture : l'eau coule, la lave avance, le tapis roule.

---

## La dissolution

Un bruit, un seuil qui monte, et l'objet disparaît en se rongeant.

> [!tip] Widget — `effets_shader_widget.html`
> Cinq onglets, un par effet, avec le graphe minimal et l'aperçu côte à côte. Pour la
> dissolution, un curseur de seuil et un choix de bruit ; pour le fresnel, un curseur de
> puissance ; pour la distorsion, l'amplitude. Chaque onglet affiche le nombre
> d'échantillonnages et d'opérations du graphe.

---

## Le bord qui s'allume

Le fresnel mesure l'angle avec la caméra : c'est le contour lumineux des boucliers et des fantômes.

---

## La distorsion

Perturber les coordonnées avant l'échantillonnage : chaleur, vitre déformante, onde de choc.

---

## Le flash de dégât

Le même retour visuel que dans le bloc juice, mais fait dans le shader et donc gratuit côté code.

---

## Combiner sans exploser

Chaque effet ajouté multiplie les branches : on compose deux ou trois, pas six.

---

## Ce que coûte un nœud

Les bruits procéduraux et les échantillonnages répétés coûtent ; les additions ne coûtent rien.

---

## Variantes et compilation

Chaque mot-clé double le nombre de shaders compilés, et allonge le temps de build.

---

## Atelier — 20 min

Composer la dissolution d'un ennemi vaincu, puis y ajouter un bord lumineux au moment de la disparition.

---

## À retenir

Cinq recettes, deux ou trois combinées au plus, un œil sur les échantillonnages, et les variantes comptées.

---

## Questions ?
