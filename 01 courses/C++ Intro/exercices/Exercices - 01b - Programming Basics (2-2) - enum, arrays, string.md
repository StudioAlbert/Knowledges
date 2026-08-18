# Exercices — 01b — Programming Basics (2/2) : enum, arrays, string

> Source : [Google Docs](https://docs.google.com/document/d/1LLXS8JqyXoErKJaNVk3eYqoNXP-wtlbVmG6qMrKbG54/edit) — le document Drive est intitulé « 01 - Programming Basics (2 / 2) enum, arrays, string » mais son contenu est une feuille d'exercices.
> Cours associé : [[01.02 - Programming Basics 2-2 - enum, string]]

## Enums

### Exercise — cris d'animaux

Create a program that lists different animals and allows the user to read how each animal screams.

Steps :

- declare the enum
- create a function : you pass an animal as parameter and it outputs a string as the scream of that animal
- create a program allowing the user to pick an animal in the list and see the scream printed out

## Arrays

### Exercise — find the best score

Create a program that finds the best score in this score array :

```cpp
int scores[]{ 84, 92, 76, 81, 56 };
```

### Exercise — find the value

Write a program that asks the user to input an integer `V` between 0 and 20.

The program creates an array of 10 random integers between 0 and 20, writes out the content of the array, and a message « V is / is not in the array ».

### Exercise — display multiplication table

Using a multidimensional array, create a program displaying the multiplication table.

## Strings

Pour tous ces exercices :

- l'utilisateur doit entrer la chaîne de caractères et les autres paramètres ;
- quitter le programme avec la touche `[ESC]`.

Source d'origine des énoncés : [w3resource — C++ string exercises](https://www.w3resource.com/cpp-exercises/string/index.php)

### Exercise 1

After asking the user their name, first name and age, display a full sentence welcoming them to the program.

Ex. : `John` + `Doe` + `45` ⇒ « Welcome John Doe, are you really 45 years old? You don't seem to be. »

### Exercise 2

Write a program to count all the vowels (a e i o u y) in a given string.

### Exercise 3

Write a C++ program to reverse a given string.

- Input : `w3resource`
- Output : `ecruoser3w`

### Exercise 4

Write a C++ program to change every letter in a given string with the letter following it in the alphabet (a becomes b, p becomes q, z becomes a).

- Input : `w3resource`
- Output : `x3sftpvsdf`

### Exercise 5

Write a C++ program to capitalize the first letter of each word of a given string. Words are separated by only one space.

- Input : `cpp string exercises`
- Output : `Cpp String Exercises`

### Exercise 6

Write a C++ program to find the largest word in a given string.

- Input : `C++ is a general-purpose programming language.`
- Output : `programming`

### Exercise 7

Write a C++ program to sort the characters of a string (numbers and punctuation symbols are not included).

- Input : `python`
- Output : `hnopty`

### Exercise 9

Write a C++ program to count all the words in a given string.

- Input : `Python`
- Output : `number of words -> 1`

### Exercise 10

Write a C++ program to check whether two characters are present equally often in a given string.

- Input : `aabcdeef`
- Output : `True`

### Exercise 11

Write a C++ program to check if a given string is a palindrome or not.

A palindrome is a word, number, phrase or other sequence of characters which reads the same backward as forward, such as *madam* or *racecar*.

- Input : `madam`
- Output : `True`

### Exercise 12

Write a C++ program to find the word in a given string which has the highest number of repeated letters.

- Input : `Print a welcome text in a separate line.`
- Output : `separate`

### Exercise 13

Write a C++ program to insert a dash character (`-`) between two odd numbers in a given string of numbers.

- Input : `1345789`
- Output : `1-345-789`

### Exercise 14

Write a C++ program to change the case (lower to upper and upper to lower) of each character of a given string.

- Input : `Python`
- Output : `pYTHON`

### Exercise 15

Write a C++ program to find the numbers in a given string and calculate the sum of all numbers.

- Input : `w3resource from 2008`
- Output : `Sum of the numbers: 2011`

### Exercise 16

Find a way to replace a whole substring inside another string (use `find`, `substr`, `replace`).

- Input : `Hi, [Title] [Name] ! How do you do ?`
- Output : `Hi Mr Albert ! How do you do ?`

## Enum + String

### Combat menu

Créer 2 menus pour simuler un jeu de combat.

**Menu principal :**

```
Choisir le type de créature [Orc, Troll, Elf, Warrior, Pokemon, Batman, etc.]
Quel est le nom de votre créature ?
```

**Menu de combat :**

```
La créature [nom_de_la_creature] doit agir...
+ Attaquer
+ Se protéger
+ Se soigner
+ Attaque spéciale
+ Quitter [ESC]
```

**Pistes d'implémentation :**

```cpp
enum Monster {};
enum Attack {};

// Variables globales
Monster my_monster;
std::string name;

DisplayMainMenu();

// game loop
do {
    DisplayAttackMenu();
} while (fin_du_jeu);

// Fonctions utilitaires
std::string MonsterToString(Monster monster) {};
```
