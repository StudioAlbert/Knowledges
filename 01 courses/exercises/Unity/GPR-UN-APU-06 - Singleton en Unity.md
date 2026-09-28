# Exercices — GPR-UN-APU-06 — Singleton en Unity

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-06 - Singleton en Unity|GPR-UN-APU-06 - Singleton en Unity]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le projet de
> départ et les corrigés viendront après validation de ces pistes.

Projet fourni : un petit jeu avec quatre gestionnaires en singleton, dont un qui plante au changement de scène.

## Courts — valider la compréhension

### 1 — Le singleton naïf
Écrire un gestionnaire d'audio en singleton, l'appeler depuis trois scripts, puis lister toutes les dépendances créées — celles que l'inspecteur ne montre pas.

### 2 — Le doublon
Poser le gestionnaire dans deux scènes chargées ensemble, observer ce qui se passe, et écrire les deux politiques possibles : le premier gagne, ou le dernier gagne.

### 3 — L'ordre du réveil
Faire s'appeler deux singletons pendant leur initialisation, provoquer l'erreur, et montrer qu'elle dépend de l'ordre de chargement des objets.

### 4 — Remplacer par une injection
Prendre l'un des quatre gestionnaires et le passer par référence au lieu d'y accéder statiquement. Compter les fichiers modifiés et dire ce que le projet a gagné.

## Complet — reprendre toute la séance

### 5 — L'audit des singletons
Sur le projet fourni : recenser tous les accès statiques, dessiner le graphe des dépendances qu'ils créent, classer les quatre gestionnaires selon qu'ils sont légitimes ou non, et justifier chaque verdict en deux lignes. Puis supprimer le moins légitime, sans casser le jeu, et remesurer le graphe.

## Difficile — se projeter

### 6 — Le jeu qui se teste
Rendre le projet testable : aucun accès statique dans le code de gameplay, les dépendances fournies au démarrage depuis un seul endroit, et la possibilité de remplacer le gestionnaire d'audio par un faux qui n'émet rien. Écrire trois tests automatisés qui ne pourraient pas exister avec les singletons d'origine. Conclure sur le prix payé : nombre de fichiers touchés, lignes de câblage ajoutées, et ce que cela vaut sur un projet de six mois.
