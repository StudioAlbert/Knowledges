# Exercices — GPR-CF-POO-02 — Classes et visibilité

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-02 - Classes et visibilité|GPR-CF-POO-02 - Classes et visibilité]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

On repart de la structure `Monstre` de `GPR-CF-POO-01`.

## Courts — valider la compréhension

### 1 — Fermer la structure
Transformer `Monstre` en classe, passer les données au privé, et faire compiler le programme existant en ajoutant le strict minimum de méthodes publiques.

### 2 — Des points de vie toujours valides
Écrire `subirDegats` et `soigner` qui bornent la vie entre 0 et le maximum, puis montrer par un appel de 9999 dégâts que la règle tient. Le compteur ne doit être accessible qu'en lecture.

### 3 — Le même code, deux mots-clés
Écrire la même chose en `struct` puis en `class` sans autre modification, et dire précisément quelle ligne cesse de compiler et pourquoi.

### 4 — De la fonction libre à la méthode
La fonction `afficherFiche(const Monstre&)` devient une méthode. Dire ce que le code gagne, ce qu'il perd, et quels paramètres disparaissent de la signature.

## Complet — reprendre toute la séance

### 5 — La classe `Joueur`
Un joueur avec vie, endurance, or et un compteur de clés. Chaque règle du jeu est tenue par une méthode : courir consomme de l'endurance et refuse si elle est vide, ouvrir une porte consomme une clé, acheter refuse si l'or manque, se reposer régénère jusqu'au maximum. Aucun champ public. Le rendu est une petite boucle de commandes au clavier qui exerce les cinq règles.

## Difficile — se projeter

### 6 — L'inventaire qui ne peut pas mentir
Une classe d'inventaire à huit emplacements et un poids maximum, qui garantit en toutes circonstances : pas de quantité négative, pas d'emplacement fantôme, pas de dépassement de poids, et objets identiques empilés. Ajouter, retirer, déplacer et échanger deux emplacements. L'énoncé demandera d'écrire une liste de tests qui tentent de violer chaque garantie, et d'expliquer pourquoi aucun code extérieur ne peut y parvenir.
