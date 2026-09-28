---
title: TC-FT-RDE-03 - Fonctions et repères
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Résolution d'Équation
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

# Fonctions et repères
<!-- .slide: class="title" -->
## TC-FT-RDE-03

<small>Une courbe, c'est un réglage de jeu</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase directrice par slide ; widgets et
schémas décrits seulement.

---

## Objectifs

Savoir lire une fonction et sa courbe, reconnaître les familles usuelles, et les composer pour régler une sensation.

**Prérequis :** [[01 courses/slides/Theory/TC-FT-RDE-02 - Équations et inéquations|TC-FT-RDE-02]].

---

## Une entrée, une sortie

Une fonction associe à chaque valeur d'entrée une seule sortie — sinon ce n'en est pas une.

---

## Domaine et image

Ce qu'on a le droit de donner, et ce qu'on peut obtenir : une racine refuse le négatif, une division refuse zéro.

---

## Le premier degré et sa pente

La pente est la sensibilité : combien la sortie bouge quand l'entrée bouge d'un cran.

> [!tip] Widget — réutiliser `droites_remarquables_widget.html`
> Le widget existant du bloc suffit pour la pente et l'ordonnée à l'origine ; on l'emploie
> ici avec une lecture « sensibilité de la souris » plutôt que géométrique.

---

## Le second degré et sa parabole

Une parabole a un sommet, et ce sommet est la hauteur maximale du saut.

---

## Racine carrée

Une courbe qui monte vite puis s'aplatit : ce qu'on veut pour une récompense décroissante.

---

## Exponentielle et logarithme

L'une s'envole, l'autre s'essouffle, et elles se répondent.

---

## Monter, descendre, culminer

Une fonction monotone ne change jamais d'avis ; un extremum est l'endroit où elle le fait.

---

## Composer

Appliquer une fonction au résultat d'une autre : c'est exactement ce que fait un easing appliqué à un temps normalisé.

---

## Valeur absolue et bornage

L'écart sans le signe, et la valeur ramenée dans un intervalle : deux outils omniprésents.

---

## Fonction par morceaux

Les dégâts pleins jusqu'à dix mètres, décroissants ensuite, nuls au-delà de trente.

> [!tip] Widget — `fonctions_widget.html`
> Un traceur de courbes avec une bibliothèque de fonctions de jeu — atténuation des dégâts,
> sensibilité, expérience, volume sonore — et des curseurs de paramètres. Le widget marque
> domaine, image, extremum et racines, et permet de composer deux fonctions pour en voir le
> résultat.

---

## Lire un graphe

Les racines sont les passages par zéro, le signe se lit au-dessus ou en dessous de l'axe.

---

## Atelier — 20 min

Régler la courbe d'atténuation des dégâts d'un fusil à pompe, puis celle de la sensibilité de visée.

---

## À retenir

Domaine et image d'abord, la famille de la courbe ensuite, la composition pour régler — et le graphe pour vérifier.

---

## Questions ?
