# Exercices — GPR-CF-EDC-02 — Gestionnaires de paquets

> Cours associé : [[01 courses/slides/C++/GPR-CF-EDC-02  - Gestionnaires de paquets|GPR-CF-EDC-02 - Gestionnaires de paquets]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets et les corrigés
> viendront après validation de ces pistes. La séance étant déjà publiée, cette fiche attend
> dans `_overviews/` et ne partira en ligne qu'une fois écrite.

Tout se passe en ligne de commande, sur le projet CMake de `GPR-CF-EDC-03`.

## Courts — valider la compréhension

### 1 — Copier les sources, et le regretter
Intégrer une bibliothèque en copiant ses sources dans le dépôt, la mettre à jour d'une version, et lister ce qu'il a fallu refaire à la main. Trois lignes de conclusion.

### 2 — La même avec un gestionnaire
Installer la même bibliothèque avec vcpkg, la lier au projet, et compter les lignes de `CMakeLists.txt` nécessaires.

### 3 — Le triplet qui ne colle pas
Installer une bibliothèque en 32 bits et la lier à un projet 64 bits. Recopier l'erreur de l'éditeur de liens, expliquer ce qu'est un triplet, puis corriger.

### 4 — Le quotidien
Lister les paquets installés, en chercher un par mot-clé, en mettre un à jour, en supprimer un, et retrouver où les fichiers vivent réellement sur le disque.

## Complet — reprendre toute la séance

### 5 — Le projet qui déclare ses dépendances
Un projet CMake qui consomme trois bibliothèques déclarées dans un manifeste versionné avec le code, sans aucune installation manuelle. Le rendu est le dépôt, plus la démonstration qu'un `git clone` suivi d'une seule commande de configuration suffit à compiler.

## Difficile — se projeter

### 6 — Reproductible ailleurs
Faire compiler le même projet sur une deuxième machine et dans une intégration continue, avec les versions exactement figées, sans rien installer à la main, et en mesurant le temps de la première compilation puis des suivantes grâce au cache binaire. Documenter ce qui casse la reproductibilité — version du compilateur, registre non figé, dépendance système — et comment chaque cas se ferme.
