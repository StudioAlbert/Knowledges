# Exercices — 03 — Data Structures : array

> Source : [Google Docs](https://docs.google.com/document/d/1SNpTmnhk3ddfPftynXBgH4290_XavQNB_aQ0X-_3ykw/edit)
> Cours associé : [[03 - Data Structures (array, vector, map, etc.)]] · Suite : [[Exercices - 03 - Data Structures]]

1. Déclarer un tableau de 10 entiers.
2. Écrire une boucle qui remplit le tableau de nombres aléatoires.
3. Écrire une autre boucle qui affiche tous les éléments du tableau dans la console.
4. Fonction de remplissage :
    1. Déclarer dans un fichier **`array_functions.h`** et écrire le code de la fonction de remplissage
       `std::array<int, 10> FillRandom()`
    2. Remplir le tableau `numbers` avec la fonction.
5. Fonction d'affichage :
    1. Déclarer la fonction d'affichage
       `void Display(std::array<int, 10> array)`
    2. Utiliser cette fonction dans le `main` pour afficher le tableau.
6. Renverser un tableau :
    1. Déclarer une fonction qui prend un tableau en paramètre et qui retourne ce tableau « à l'envers » (le premier élément devient le dernier)
       `std::array<int, 10> Reverse(std::array<int, 10>)`
    2. Utiliser cette fonction dans le `main`.
    3. Afficher le nouveau tableau.
