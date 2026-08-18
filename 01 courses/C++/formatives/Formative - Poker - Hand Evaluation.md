# Formative — Poker — Hand Evaluation

> Source : [Google Drawing](https://docs.google.com/drawings/d/1_ZwzCnnDBBgAAII89OUl75hRCPiDIv3vnz2daxIsDXM/edit)
> Énoncé : [[Formative - Poker Card Game]]

![[formative_poker_hand_evaluation.png]]

## Lecture du schéma

Le schéma illustre **la constitution de la main à évaluer** :

- à gauche de la barre, les **2 cartes privées** du joueur ;
- à droite, les **5 cartes communes** (le paquet de 3 du flop, puis les 2 cartes suivantes) ;
- les deux flèches convergent vers une rangée de **6 cartes** : c'est l'ensemble des cartes candidates parmi lesquelles l'algorithme doit chercher la meilleure combinaison.

La rangée du bas donne un exemple concret de valeurs à évaluer : `K  8  K  2  6  A  D`.

L'exercice consiste à écrire l'algorithme qui, à partir de cet ensemble, détermine la [hand value](https://en.wikipedia.org/wiki/Texas_hold_%27em#Hand_values) la plus forte.
