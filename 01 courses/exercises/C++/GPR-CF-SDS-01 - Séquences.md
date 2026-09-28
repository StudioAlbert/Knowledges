# Exercices — GPR-CF-SDS-01 — Séquences

> Cours associé : [[01 courses/slides/C++/GPR-CF-SDS-01 - Séquences|GPR-CF-SDS-01 - Séquences]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

## Courts — valider la compréhension

### 1 — Fixe ou variable
Le même inventaire écrit avec un tableau de taille fixe puis avec un vecteur. Dire ce que chaque version permet que l'autre interdit, et laquelle convient à un inventaire de jeu.

### 2 — Espionner la capacité
Ajouter cent ennemis un par un en affichant taille, capacité et adresse du premier élément à chaque changement. Compter les déménagements, puis refaire avec une réservation préalable.

### 3 — Insérer au début
Mesurer le temps d'ajout de cinquante mille éléments en tête puis en queue d'un vecteur, et donner le rapport entre les deux.

### 4 — La référence qui ne vaut plus rien
Garder une référence vers un élément d'un vecteur, provoquer un déménagement, et montrer ce qu'on lit ensuite. Énoncer la règle qui en découle.

## Complet — reprendre toute la séance

### 5 — La file des ennemis
La vague d'ennemis d'un tower defense : ajout à la fin, retrait de ceux qui meurent, parcours à chaque image, et compactage en fin de vague. Réserver la capacité au bon endroit, supprimer sans casser le parcours en cours, et afficher à chaque étape le nombre d'éléments et la capacité. Le rendu commente chaque choix de conteneur.

## Difficile — se projeter

### 6 — Le million d'éléments
Parcourir et sommer un million d'entiers dans un vecteur puis dans une liste, mesurer, et expliquer un écart qui n'a rien à voir avec le nombre d'instructions. Refaire l'expérience avec des objets plus gros, puis avec une insertion au milieu toutes les cent itérations, et dire à quelle condition exacte la liste reprend l'avantage. C'est l'entrée en matière du bloc de performance.
