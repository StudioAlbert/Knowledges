# Exercices — GPR-UN-APU-07 — Singleton générique et persistant

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-07 - Singleton générique et persistant|GPR-UN-APU-07 - Singleton générique et persistant]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le projet de
> départ et les corrigés viendront après validation de ces pistes.

On repart du projet de `GPR-UN-APU-06`, avec ses quatre gestionnaires et ses trois scènes.

## Courts — valider la compréhension

### 1 — La base générique
Écrire la classe de base paramétrée, y faire hériter deux gestionnaires, et compter les lignes supprimées.

### 2 — Traverser les scènes
Rendre le gestionnaire d'audio persistant, passer du menu au jeu puis au menu, et vérifier que la musique ne redémarre pas.

### 3 — L'objet qui traîne
Revenir au menu qui contient lui aussi le gestionnaire, obtenir deux instances persistantes, montrer le symptôme audible, puis le corriger.

### 4 — Trop tôt
Appeler un gestionnaire depuis le réveil d'un autre objet, obtenir l'erreur, puis mettre en place l'interdiction explicite avec un message qui dit quoi faire.

## Complet — reprendre toute la séance

### 5 — Le bootstrap
Une scène de démarrage unique qui crée et initialise les quatre gestionnaires dans un ordre écrit, puis charge le menu. Aucun gestionnaire ne se crée tout seul, aucun n'est présent dans les autres scènes, et chaque scène reste lançable seule en développement. Le rendu inclut la frise du démarrage et la liste des ordres de dépendance.

## Difficile — se projeter

### 6 — Le cycle de vie complet
Donner à chaque gestionnaire un cycle explicite — initialisation, remise à zéro entre deux parties, arrêt — et le faire respecter par le bootstrap. Vérifier que trois parties d'affilée repartent d'un état propre, que le retour au menu libère ce qui doit l'être, et que le rechargement du code en éditeur ne laisse pas d'état fantôme. Écrire enfin la page de règles d'équipe : ce qui a droit d'être un singleton dans ce projet, et ce qui n'y a pas droit.
