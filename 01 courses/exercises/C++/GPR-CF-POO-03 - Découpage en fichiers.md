# Exercices — GPR-CF-POO-03 — Découpage en fichiers

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-03 - Découpage en fichiers|GPR-CF-POO-03 - Découpage en fichiers]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les projets de
> départ et les corrigés viendront après validation de ces pistes.

Tous les exercices partent du même `main.cpp` fourni — un mini jeu de donjon d'environ 300 lignes — et le découpent.

## Courts — valider la compréhension

### 1 — Sortir une classe
Déplacer `Vector2` vers son duo de fichiers, l'ajouter au `CMakeLists.txt`, et recompiler sans rien changer au comportement du jeu.

### 2 — Provoquer la double inclusion
Retirer la garde de `Vector2.h`, l'inclure depuis deux en-têtes, recopier l'erreur du compilateur dans le rendu et l'expliquer en une phrase, puis remettre la garde.

### 3 — Ce qui n'a rien à faire dans un en-tête
Un `Joueur.h` fourni contient le corps de trois méthodes, un `using namespace std` et une inclusion inutile. Dire pour chacun pourquoi c'est un problème, puis corriger.

### 4 — L'en-tête qui mentait
Une méthode déclarée dans l'en-tête n'est implémentée nulle part. Dire si l'erreur vient du compilateur ou de l'éditeur de liens, et à quel moment elle apparaît.

## Complet — reprendre toute la séance

### 5 — Découper le donjon
Le fichier de départ contient quatre concepts : `Vector2`, `Entite`, `Salle`, `Journal`. Le découper en quatre duos de fichiers, avec gardes, inclusions minimales et `CMakeLists.txt` à jour. Le rendu est le projet qui compile plus le schéma des inclusions obtenues, dessiné à la main.

## Difficile — se projeter

### 6 — La dépendance circulaire
`Joueur` doit connaître son `Arme`, et `Arme` son porteur : les deux en-têtes s'incluent mutuellement et rien ne compile. Résoudre par déclaration anticipée et pointeur, dire ce que l'en-tête peut encore promettre dans ce cas, puis mesurer le temps de compilation avant et après pour chiffrer ce que coûte une inclusion inutile.
