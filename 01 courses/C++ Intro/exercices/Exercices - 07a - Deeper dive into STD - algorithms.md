# Exercices — 07a — Deeper dive into STD : algorithms

> Source : [Google Docs](https://docs.google.com/document/d/10IMXgerYgoMGtaJRYFj9VVa86FfwyakZVYDkHWU-kAc/edit)
> Cours associé : [[07 - Deeper dive into STD 2-2 - Algorithms]]

**Échéance de rendu (telle qu'indiquée dans le document d'origine) : mardi 1er octobre, 23h59.**

## Exercice 1 — Bubble sort

*Rendu Drive.*

Voici une liste de nombres : `[84, 17, 11, 9, 21, 52, 25, 3, 13, 22]`.

Créer un programme qui trie cette liste avec l'algorithme **bubble sort**.

## Exercice 2 — Insertion sort

*Rendu Drive.*

Voici une liste de nombres : `[84, 17, 11, 9, 21, 52, 25, 3, 13, 22]`.

Créer un programme qui trie cette liste avec l'algorithme **insertion sort**.

## Exercice 3 — Quick sort

*Rendu Drive.*

Voici une liste de nombres : `[84, 17, 11, 9, 21, 52, 25, 3, 13, 22]`.

Créer un programme qui trie cette liste avec l'algorithme **quick sort**.

## Exercice 4 — Menu de tri

*Rendu Git.*

En reprenant les 3 premiers exercices, créer un programme qui demande à l'utilisateur de choisir le type de tri qu'il veut et le nombre d'éléments qu'il veut trier. Il faut ensuite remplir un tableau avec *n* caractères aléatoires.

## Exercice 5 — Tic tac toe

*Rendu Git. Par groupe de 2.*

- Écrire une fonction `void GenerateMap()` qui remplit une fois la map avec un `char` représentant les cases vides.
- Créer une fonction `ShowMap()` qui affiche la carte dans son état actuel.
- Créer une fonction `SetNewPosition()` : elle demande au joueur une position et met à jour la map.
- Créer une fonction `void CheckWin()` qui vérifie s'il y a un pattern gagnant sur la map.
- Créer une fonction `void PlayGame()` (appelle `ShowMap()` et `SetNewPosition()`).
- Appeler `GenerateMap()` et `PlayGame()` dans `Main()`.
