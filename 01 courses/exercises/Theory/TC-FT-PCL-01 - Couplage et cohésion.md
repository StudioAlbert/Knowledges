# Exercices — TC-FT-PCL-01 — Couplage et cohésion

> Cours associé : [[01 courses/slides/Theory/TC-FT-PCL-01 - Couplage et cohésion|TC-FT-PCL-01 - Couplage et cohésion]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le projet
> d'étude et les corrigés viendront après validation de ces pistes.

Support commun : un projet Unity fourni, volontairement mal découpé, avec un `GameManager` de 900 lignes.

## Courts — valider la compréhension

### 1 — Dessiner les flèches
Relever les dépendances des huit scripts du projet et en dessiner le graphe sur une page. Une flèche par « a besoin de », rien d'autre.

### 2 — Le rayon d'impact
Choisir trois classes et dire, pour chacune, ce qu'il faudrait relire et retester si on changeait le nom d'une de ses méthodes publiques. Classer les trois par coût.

### 3 — Combien de raisons de changer
Lister les responsabilités du `GameManager` fourni, une ligne par responsabilité, et conclure en nombre de raisons distinctes de le rouvrir.

### 4 — Inverser une flèche
Une dépendance va du gameplay vers l'interface. L'inverser par une interface ou un événement, et redessiner la portion de graphe concernée.

## Complet — reprendre toute la séance

### 5 — Le diagnostic du projet
Produire un diagnostic d'une page : le graphe des dépendances, les trois classes les plus coûteuses à modifier, les responsabilités mélangées, les symptômes repérés nommément, et un plan de découpe en quatre étapes ordonnées par rapport bénéfice sur risque. Aucune ligne de code à écrire : c'est un rendu d'analyse.

## Difficile — se projeter

### 6 — Payer la dette, une étape à la fois
Exécuter les deux premières étapes du plan précédent sur le projet réel, sans casser le jeu à aucun moment : chaque commit doit laisser le projet jouable. Mesurer avant et après — nombre de dépendances, taille du plus gros fichier, nombre de fichiers touchés par un changement type. Conclure sur ce qui a vraiment baissé, et sur ce qui a seulement été déplacé.
