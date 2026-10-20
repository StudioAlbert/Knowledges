# Exercices — TC-FT-PCL-04 — Composition contre héritage

> Cours associé : [[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage|TC-FT-PCL-04 - Composition contre héritage]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le projet de
> départ et les corrigés viendront après validation de ces pistes.

## Courts — valider la compréhension

### 1 — Compter ce que coûte une demande
Les quatre classes de base du widget et ses huit demandes sont fournies. Pour chacune, dire quelle classe l'héritage ajoute, quel comportement il recopie, et ce que la composition ajoute. Donner les trois totaux, puis nommer la capacité qui finit écrite le plus de fois dans l'arbre.

### 2 — Convertir une hiérarchie
Une hiérarchie d'ennemis à trois niveaux est fournie. La remplacer par une entité neutre et des composants, en conservant exactement le comportement observable.

### 3 — Le composant qui ne sait rien
Un composant de déplacement qui cite trois autres composants par leur type. Le rendre ignorant de ses voisins, et dire ce qui doit alors porter la coordination.

### 4 — Données ou comportement
Un composant fourni mélange les deux. Séparer ce qui est réglage de ce qui est traitement, et dire ce que la séparation permet que le mélange interdisait.

## Complet — reprendre toute la séance

### 5 — Le bestiaire assemblé
Douze ennemis différents à produire à partir de six composants seulement, chacun décrit par ses données. Ajouter en fin d'exercice une treizième variante et une septième capacité sans modifier un composant existant. Le rendu montre les douze ennemis en jeu, la liste des composants, et les fichiers touchés par l'ajout final.

## Difficile — se projeter

### 6 — Un ECS de poche
Écrire le minimum viable : des entités numérotées, des composants rangés par type dans des tableaux contigus, et trois systèmes qui balaient ces tableaux. Faire tourner mille entités, mesurer le temps par image, puis comparer avec la version objet du même jeu. Expliquer l'écart par la disposition mémoire, et dire à partir de combien d'entités le détour devient rentable.
