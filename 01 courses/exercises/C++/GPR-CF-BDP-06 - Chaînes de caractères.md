# Exercices — GPR-CF-BDP-06 — Chaînes de caractères

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-06 - Chaînes de caractères|GPR-CF-BDP-06 - Chaînes de caractères]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

Un seul fichier `main.cpp` par exercice, sortie avec `std::println`. Pas de `std::vector` : il arrive plus tard.

## Courts — valider la compréhension

### 1 — La bannière du héros
Demander le nom du héros et sa classe, puis afficher une bannière encadrée dont la largeur s'adapte à la longueur du nom. Objectif : `getline`, `size()`, concaténation.

### 2 — Barre de vie en texte
Afficher les PV sous forme `[####------] 40/100` en construisant la chaîne caractère par caractère. Objectif : boucle, `to_string`, construction incrémentale.

### 3 — Pseudo valide ?
Refuser un pseudo vide, trop court, trop long ou contenant un espace, et dire lequel de ces quatre cas a échoué. Objectif : `empty()`, `size()`, `find`, comparaison de `npos`.

### 4 — Le nom du fichier de sauvegarde
De `saves/partie_03_donjon.sav`, extraire le dossier, le numéro de partie et l'extension. Objectif : `find`, `rfind`, `substr`, index calculés et non devinés.

## Complet — reprendre toute la séance

### 5 — La console de triche
Lire une ligne au format `give potion 3`, reconnaître la commande parmi quatre connues, extraire l'objet et la quantité, convertir la quantité, et répondre soit par l'effet appliqué soit par un message d'erreur précis. La boucle tourne jusqu'à `quit`. Objectif : tout le vocabulaire de la séance dans un seul programme.

## Difficile — se projeter

### 6 — Le formateur de dialogues
Un dialogue de PNJ doit tenir dans une boîte de 38 caractères de large : couper le texte entre les mots et jamais au milieu, gérer un mot plus long que la boîte, et paginer par groupes de trois lignes en attendant une touche entre deux pages. Bonus : garder les balises de couleur du type `[rouge]` hors du compte des caractères visibles.
