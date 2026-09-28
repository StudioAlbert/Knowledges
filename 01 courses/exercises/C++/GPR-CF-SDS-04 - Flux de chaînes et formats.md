# Exercices — GPR-CF-SDS-04 — Flux de chaînes et formats

> Cours associé : [[01 courses/slides/C++/GPR-CF-SDS-04 - Flux de chaînes et formats|GPR-CF-SDS-04 - Flux de chaînes et formats]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les fichiers de
> données et les corrigés viendront après validation de ces pistes.

Une bibliothèque JSON est fournie et intégrée au projet ; les fichiers de données aussi.

## Courts — valider la compréhension

### 1 — Découper une ligne de journal
Une ligne de log de jeu au format `temps acteur action cible` : la découper avec un flux de chaînes, la retranscrire en phrase lisible, et traiter la ligne mal formée.

### 2 — Fabriquer le message
Construire la ligne de journal inverse, à partir de valeurs typées, avec deux décimales pour le temps. Comparer avec la version par concaténation.

### 3 — Lire une fiche d'arme
Charger un JSON d'arme, en extraire nom, dégâts, cadence et liste d'effets, et afficher la fiche. Le fichier est valide.

### 4 — Le champ qui manque
Le même chargement sur trois fichiers abîmés : champ absent, type faux, valeur négative. Produire pour chacun un message qu'un designer pourrait comprendre et corriger seul.

## Complet — reprendre toute la séance

### 5 — Charger un niveau
Un niveau décrit en JSON : dimensions, grille de tuiles, points d'apparition, liste d'ennemis avec leur type et leur position, réglages de partie. Écrire le chargeur, le valider entièrement avant de construire quoi que ce soit, et afficher le niveau en caractères. Un fichier invalide ne doit jamais produire un niveau à moitié construit.

## Difficile — se projeter

### 6 — Le format qui vieillit bien
Faire évoluer le format du niveau trois fois — champ renommé, champ devenu optionnel avec valeur par défaut, structure imbriquée déplacée — en gardant la capacité de charger les anciens fichiers. Écrire les messages d'erreur du point de vue du designer, avec le numéro de ligne fautif. Conclure en comparant avec la façon dont Unity gère les mêmes situations dans ses assets, ce qui prépare `GPR-UN-APU-04`.
