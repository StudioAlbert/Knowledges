# Exercices — GPR-CF-SDS-05 — Itérateurs et algorithmes

> Cours associé : [[01 courses/slides/C++/GPR-CF-SDS-05 - Itérateurs et algorithmes|GPR-CF-SDS-05 - Itérateurs et algorithmes]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

Contrainte de toute la fiche à partir de l'exercice 2 : aucune boucle écrite à la main.

## Courts — valider la compréhension

### 1 — Parcourir sans index
Le même parcours d'un vecteur d'ennemis écrit avec un index, avec un itérateur, puis avec une boucle par intervalle. Dire ce que chaque version suppose du conteneur.

### 2 — Compter ce qui compte
Compter les ennemis blessés, ceux hors de portée, et ceux d'un type donné, avec un prédicat par question.

### 3 — Transformer
Appliquer un poison à toute la vague, puis produire la liste des noms à afficher dans le journal, sans modifier la vague.

### 4 — Supprimer pendant le parcours
Retirer les ennemis morts en modifiant le vecteur pendant qu'on le parcourt, constater le dégât, puis le faire correctement.

## Complet — reprendre toute la séance

### 5 — Le tableau de bord de la vague
À partir d'une vague de cinquante ennemis : le nombre de survivants, le plus proche du joueur, les trois plus dangereux, la vague triée par distance, la séparation entre ceux à portée et les autres, les dégâts totaux infligés, et la liste des types présents sans doublon. Chaque réponse est un appel d'algorithme, et le rendu nomme celui choisi et pourquoi.

## Difficile — se projeter

### 6 — Le même code sur trois conteneurs
Écrire une fonction de filtrage et d'agrégation qui fonctionne à l'identique sur un tableau fixe, un vecteur et une liste, sans surcharge ni duplication. Puis mesurer la version séquentielle et la version parallèle sur un million d'éléments, sur les trois conteneurs, et expliquer les résultats — y compris le cas où le parallèle est plus lent. Prolongement : dire quelles hypothèses la fonction fait sur l'itérateur qu'elle reçoit.
