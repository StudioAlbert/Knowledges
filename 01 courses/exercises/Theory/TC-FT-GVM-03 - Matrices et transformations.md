# Exercices — TC-FT-GVM-03 — Matrices et transformations

> Cours associé : [[01 courses/slides/Theory/TC-FT-GVM-03 - Matrices et transformations|TC-FT-GVM-03 - Matrices et transformations]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les valeurs
> numériques et les corrigés viendront après validation de ces pistes.

Exercices 1 à 4 sur papier, vérifiés ensuite au clavier avec une structure de matrice maison.

## Courts — valider la compréhension

### 1 — Lire une matrice
Six matrices deux par deux : dire pour chacune ce qu'elle fait au carré unité, sans calcul, en regardant ses colonnes.

### 2 — L'ordre qui change tout
Une rotation et une translation : calculer les deux produits possibles, appliquer les deux au même sprite, et dessiner les deux résultats.

### 3 — Le déterminant
Quatre matrices : donner le déterminant, l'aire du carré transformé, et dire laquelle retourne l'orientation. Relier au cas du miroir dans un jeu 2D.

### 4 — La translation impossible
Montrer qu'aucune matrice deux par deux ne peut déplacer l'origine, puis écrire la version homogène qui le fait.

## Complet — reprendre toute la séance

### 5 — Placer un sprite
Écrire de quoi construire la matrice complète d'un objet — échelle, rotation, translation, dans l'ordre du moteur — l'appliquer aux quatre coins d'un sprite, et afficher le résultat en caractères. Vérifier sur trois cas connus, dont un objet retourné et un objet à échelle non uniforme, et comparer avec ce que donne Unity sur la même configuration.

## Difficile — se projeter

### 6 — La chaîne d'une tourelle
Une tourelle montée sur un char : le canon tourne dans le repère de la tourelle, la tourelle dans celui du châssis, le châssis dans le monde. Composer les matrices pour obtenir la position mondiale du bout du canon, vérifier avec trois orientations, puis introduire une échelle non uniforme sur le châssis et expliquer le cisaillement qui apparaît. C'est l'entrée en matière de `TC-FT-GVM-04`.
