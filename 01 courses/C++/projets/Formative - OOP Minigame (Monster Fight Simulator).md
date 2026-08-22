# Formative — OOP Minigame (Monster Fight Simulator)

> Source : [Google Docs](https://docs.google.com/document/d/1Le8QEltCbEsUHOYXPOs4JDj9gAPdR5UkjqgAboswwgA/edit)
> Cours associé : [[04 - OOP Advanced]] · [[Exercices - 04 - OOP]]

## Énoncé

Write a program that simulates a fight between two monsters. Both monsters are to be created with the help of object-oriented programming.

A monster must have at least the following attributes: **Health Points (HP)**, **Attack Damage (AD)**, **Defense Points (DP)**, **Speed (S)** and **Race**. Possible races are orc, troll and goblin. The player can select premade monster profiles.

At the beginning, the program shall ask for an input to determine which two monsters shall fight against each other. The program must not allow a fight between monsters of the same race.

Monsters can perform:

- **Attack** — the formula is `Damage = Attack Damage - Defense Points`. If the damage is negative, it is set to 0. The damage is subtracted from the life points of the respective monster. If the monster still has life points left after an attack, it now performs an attack. This is repeated until a monster dies.

Optional features:

- **Parry** — add a certain amount of points to the Defense stat, for up to two rounds.
- **Heal** — add a certain amount of points to the HP.

The monster with the higher speed value performs its actions first.

After a monster is defeated, the program displays who won and how many rounds the fight lasted. Each action counts as a round.

## Tips

- Have a fellow student test your code to find possible bugs.
- Catch improper user input (e.g. range of input data values, input of non-numeric values, data validation).
- Think about extreme conditions (infinite combat, attribute value conflicts).
- Pay attention to data encapsulation.
- Avoid `goto` and magic numbers.

## Learning objectives

- **K1.** Describe the principles of object-oriented programming.
- **S1.** Produce stable code using object-oriented programming.
- **S4.** Plan and manage the allocated time to successfully meet given milestones and deadlines.

## Feedback elements

Pay attention to the following elements and note feedback on them from your subject supervisor.

**Proficiency**

- Does the program run stably and without errors?
- Is the user input designed in an understandable way?
- Is the battle between the monsters simulated correctly?

**Process**

- Was a consistent coding convention used?
- Was class inheritance used sensibly?
- Is the game logic coherent?

**Person**

- How understandable and readable is the code created?
- How creatively was the task handled?
