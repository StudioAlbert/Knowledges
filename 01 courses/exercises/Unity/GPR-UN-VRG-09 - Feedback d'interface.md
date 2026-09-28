# Exercices — GPR-UN-VRG-09 — Feedback d'interface

> Cours associé : [[01 courses/slides/Unity/GPR-UN-VRG-09 - Feedback d'interface|GPR-UN-VRG-09 - Feedback d'interface]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le prototype de
> départ et les corrigés viendront après validation de ces pistes.

Prototype fourni avec une interface fonctionnelle et parfaitement inerte : score, barre de vie, munitions, menu.

## Courts — valider la compréhension

### 1 — Le score qui monte
Faire monter le score jusqu'à la valeur atteinte au lieu de l'afficher d'un coup, avec une durée qui ne dépend pas du montant gagné, puis avec une durée qui en dépend. Choisir et justifier.

### 2 — La barre retardée
Ajouter la barre de dégât retardée, régler délai et rattrapage, et traiter la série de cinq coups rapides.

### 3 — Les quatre états du bouton
Donner au bouton du menu ses quatre états, puis mesurer le temps entre l'appui et le premier retour visible. Le ramener sous un vingtième de seconde.

### 4 — La transition
Passer du menu au jeu par une transition qui masque le chargement, puis en retirer la moitié de la durée et dire si le joueur s'en plaint.

## Complet — reprendre toute la séance

### 5 — La passe interface du prototype
Animer l'ensemble : score, munitions, barre de vie avec dégât retardé, apparition en cascade du menu, quatre états sur tous les boutons, transitions entre les trois écrans, et retour immédiat sur chaque appui. Le rendu est une vidéo du parcours complet et le tableau des durées retenues.

## Difficile — se projeter

### 6 — Jamais bloquant, toujours réductible
Mettre les animations d'interface dans une file qui n'empêche jamais d'agir, avec priorité et interruption propre quand une nouvelle information arrive. Ajouter une option qui réduit toutes les durées à zéro pour les joueurs qui la demandent, sans casser la logique. Mesurer au profileur le coût de l'interface pendant un combat dense, et le ramener sous un budget fixé.
