# Exercices — GPR-CF-SDS-02 — Adaptateurs et conteneurs associatifs

> Cours associé : [[01 courses/slides/C++/GPR-CF-SDS-02 - Adaptateurs et conteneurs associatifs|GPR-CF-SDS-02 - Adaptateurs et conteneurs associatifs]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

## Courts — valider la compréhension

### 1 — La file d'actions
Les commandes du joueur arrivent plus vite qu'elles ne s'exécutent : les mettre en file, en traiter deux par tour, et afficher l'état de la file à chaque tour.

### 2 — La pile d'annulation
Chaque pose de tourelle est empilée ; la touche d'annulation défait la dernière. Traiter le cas de la pile vide, puis dire pourquoi une file donnerait un comportement absurde.

### 3 — L'inventaire par nom
Ranger les objets sous leur nom, incrémenter la quantité d'un objet déjà présent, et parcourir l'inventaire dans l'ordre alphabétique sans le trier soi-même.

### 4 — Les succès obtenus
Un ensemble de succès déjà débloqués : refuser silencieusement un doublon, tester l'appartenance, et afficher le compte. Montrer ce qu'un vecteur aurait demandé de plus.

## Complet — reprendre toute la séance

### 5 — Le gestionnaire d'entités
Un petit jeu où chaque entité a un identifiant unique : retrouver une entité par son identifiant, faire apparaître les ennemis depuis une file d'événements datés, empiler les actions annulables, et tenir l'ensemble des identifiants déjà détruits pour refuser une double suppression. Chaque choix de conteneur est justifié en une ligne dans le rendu.

## Difficile — se projeter

### 6 — Le cache de textures
Un cache qui garde en mémoire les seize dernières textures utilisées et libère la plus anciennement employée quand il déborde. Il faut retrouver une texture par son nom en temps constant et connaître l'ordre d'utilisation : deux exigences qu'aucun conteneur seul ne satisfait. Mesurer le taux de succès du cache sur une séquence de chargements réaliste, et dire ce que changerait une politique différente.
