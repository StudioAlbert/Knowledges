# Formative — Poker Card Game

> Source : [Google Docs](https://docs.google.com/document/d/1dBvLn3y-ITNwEClbM7gpKqP7K6pjDtXdH44QR7VcMj0/edit)
> Schémas : [[Formative - Poker Card Game - Sequence]] · [[Formative - Poker - Hand Evaluation]]

## Poker Game

Propose, as a console program, a poker game between a player and a bot. It follows the same rules as Texas Hold'em; you will simplify the bet sequences with a bot which only bets the same as the player, or any dumb behaviour of your choice.

### Programming architecture proposal

- Define two enums to express **Suit** (Club, Hearts, Spades, Squares) and **Value** (from 2 to Ace).
- Define a `struct Card` which can contain two properties representing a Suit and a Value.
- Find out which data structure could be useful to represent a hand, a deck or the common hand of cards.
- Define every algorithm needed to know which player is winning.
    - Value of a poker hand : [Texas hold 'em (Wikipedia)](https://en.wikipedia.org/wiki/Texas_hold_%27em)

### Development steps

1. Find out a `struct Card` and functions to evaluate a card versus another. Store these functions in a specific header.
2. Find out the data structures required to store any number of cards, and functions to "give" cards (e.g. move a card from one vector to another). Can a **queue** be useful in that specific use case? Can you print the content of the player's hand in the console?
3. Finally, find the conditions required for each [**Hand Value**](https://en.wikipedia.org/wiki/Texas_hold_%27em#Hand_values). Can you print which hand value applies to your player in the console?
