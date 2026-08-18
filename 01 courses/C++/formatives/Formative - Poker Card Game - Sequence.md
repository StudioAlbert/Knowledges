# Formative — Poker Card Game — Sequence

> Source : [Google Drawing](https://docs.google.com/drawings/d/1s4k141ma3NIai-6T0-SFa-xn6q8T4h2gZXRB1l-xTHI/edit)
> Énoncé : [[Formative - Poker Card Game]]

![[formative_poker_sequence.png]]

## Ordre de distribution des cartes

Entre chaque phase, on ouvre une phase de pari. On pourra opter pour un pari « simplifié » : parier ou quitter pour le joueur, le bot suit systématiquement.

| # | Phase | Distribution |
|:-:|---|---|
| 1 | Donne | On donne les cartes aux joueurs une à une (2 cartes par joueur) |
| 2 | Flop | 3 cartes au commun |
| 3 | River | 1 carte au commun |
| 4 | Turn | 1 carte au commun |

> Note : le schéma d'origine nomme la 3ᵉ phase « River » et la 4ᵉ « Turn ». Dans les règles officielles du Texas Hold'em, l'ordre est l'inverse — turn puis river. La séquence de distribution (3 + 1 + 1) reste correcte.
