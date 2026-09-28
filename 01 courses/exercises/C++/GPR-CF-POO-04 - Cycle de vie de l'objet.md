# Exercices — GPR-CF-POO-04 — Cycle de vie de l'objet

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-04 - Cycle de vie de l'objet|GPR-CF-POO-04 - Cycle de vie de l'objet]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

Les exercices 1 à 4 affichent un message à chaque construction et destruction : la sortie du programme est la réponse.

## Courts — valider la compréhension

### 1 — Trois façons de naître
Donner à `Monstre` un constructeur par défaut, un constructeur complet, et un constructeur à paramètres par défaut. Montrer par trois déclarations que les trois chemins mènent à un objet valide.

### 2 — L'ordre qui surprend
Une classe dont la liste d'initialisation est écrite dans l'ordre inverse de la déclaration des membres, et dont un membre se calcule à partir d'un autre. Prédire la sortie, la vérifier, puis corriger.

### 3 — Le destructeur bavard
Trois objets dans des portées imbriquées, un quatrième dans un tableau. Prédire l'ordre des messages de destruction avant de lancer le programme, puis expliquer les écarts.

### 4 — `this` au secours
Une méthode dont le paramètre porte le même nom que le membre. Faire la version qui échoue, la version avec `this`, et dire laquelle on préfère lire.

## Complet — reprendre toute la séance

### 5 — La vie d'un projectile
Une classe `Projectile` qui s'initialise avec une position, une direction et une durée de vie, se déplace à chaque image, et annonce sa disparition dans son destructeur. Une boucle de jeu en tire douze, les fait vivre, et les retire quand leur durée est écoulée. Le rendu est la trace complète des naissances et des morts, commentée : qui a détruit quoi, et quand.

## Difficile — se projeter

### 6 — La texture qui se libère toute seule
Une classe qui simule le chargement d'une ressource lourde : le constructeur l'acquiert et l'annonce, le destructeur la rend. La faire vivre dans un conteneur, la passer à des fonctions, et compter les acquisitions et libérations — elles doivent s'équilibrer exactement. Le comptage va se déséquilibrer dès la première copie : l'énoncé demandera de trouver pourquoi, ce qui ouvre la question du constructeur de copie et du déplacement.
