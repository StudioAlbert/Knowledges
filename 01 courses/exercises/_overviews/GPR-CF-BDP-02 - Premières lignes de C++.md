# Exercices — GPR-CF-BDP-02 — Premières lignes de C++

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-02 - Premières lignes de C++|GPR-CF-BDP-02 - Premières lignes de C++]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. La séance étant déjà publiée, cette
> fiche attend dans `_overviews/` et ne partira en ligne qu'une fois les énoncés écrits.

Un seul fichier `main.cpp` par exercice, sortie avec `std::println`.

## Courts — valider la compréhension

### 1 — La fiche du personnage
Déclarer les caractéristiques d'un héros avec le type qui convient à chacune, les afficher proprement alignées, et commenter chaque choix de type en fin de fichier.

### 2 — Ce que pèse un type
Afficher la taille en mémoire des types de base, comparer avec les plages de valeurs annoncées, et relever celui dont la taille surprend sur Windows.

### 3 — Le calcul de dégâts
Une formule de dégâts donnée en français, à traduire en une expression. Écrire d'abord la version sans parenthèses, montrer qu'elle donne un résultat faux, puis corriger.

### 4 — La division entière
Calculer un pourcentage de vie avec des entiers, obtenir zéro, comprendre pourquoi, et donner deux façons de s'en sortir.

## Complet — reprendre toute la séance

### 5 — La fiche de combat
Un programme qui déclare deux combattants, calcule les dégâts échangés en un tour selon une formule à plusieurs opérateurs, applique les résultats, et affiche un compte rendu formaté avec titres, séparateurs et alignements. Chaque type est choisi et justifié, chaque constante est nommée, et le fichier est commenté pour un lecteur qui découvre le projet.

## Difficile — se projeter

### 6 — Le débordement silencieux
Faire dépasser volontairement la capacité d'un entier avec un score qui grimpe, observer la valeur obtenue, puis chercher à quel moment exactement le calcul a basculé. Refaire avec un type plus large et avec un type non signé, comparer les trois comportements, et écrire la règle de choix de type pour un compteur de score. C'est la question que reprendra `TC-FT-RNLB-02`.
