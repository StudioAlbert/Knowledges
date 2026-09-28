# Exercices — GPR-CF-SDS-06 — Les algorithmes, un par un

> Cours associé : [[01 courses/slides/C++/GPR-CF-SDS-06 - Les algorithmes, un par un|GPR-CF-SDS-06 - Les algorithmes, un par un]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

Aucune boucle écrite à la main dans toute la fiche.

## Courts — valider la compréhension

### 1 — Trouvé, ou pas
Chercher un ennemi par son identifiant dans une vague, traiter le cas trouvé et le cas absent, et montrer ce que donne une comparaison à zéro au lieu de la comparaison à la fin.

### 2 — Le piège de la suppression
Supprimer les ennemis morts en oubliant la seconde étape : afficher la taille et le contenu obtenus, expliquer la traîne, puis corriger des deux façons vues en cours.

### 3 — Trier selon sa propre règle
Trier le butin par rareté décroissante puis par nom, avec un seul comparateur, et vérifier la stabilité du résultat sur des égalités.

### 4 — Tous, au moins un, aucun
Trois questions sur la vague — tous à portée, au moins un boss, aucun invisible — chacune répondue par un seul appel.

## Complet — reprendre toute la séance

### 5 — L'inventaire tenu par la bibliothèque
Sur un inventaire de quarante objets : dédoublonner en empilant les identiques, trier par catégorie puis par poids, extraire la liste des objets utilisables, séparer ce qui est équipé du reste, calculer le poids total, fusionner avec le butin d'un coffre, et retirer tout ce qui est cassé. Chaque opération est un appel nommé dans le rendu, avec la raison du choix.

## Difficile — se projeter

### 6 — Le plateau, le butin et le coût de la copie
Faire tourner un plateau de jeu de seize cases d'un cran sans conteneur temporaire, fusionner deux listes de succès déjà triées sans tout retrier, et énumérer les ordres de passage possibles de quatre personnages. Puis mesurer la même série d'opérations sur des objets lourds, en copie puis en déplacement, et conclure sur le gain réel. Prolongement : dire lesquelles de ces opérations changent si le conteneur devient une liste.
