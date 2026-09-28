# Exercices — GPR-CF-EDC-01 — Chaîne d'outils et prérequis

> Cours associé : [[01 courses/slides/C++/GPR-CF-EDC-01 - Chaîne d'outils et prérequis|GPR-CF-EDC-01 - Chaîne d'outils et prérequis]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. La séance étant déjà publiée, cette
> fiche attend dans `_overviews/` et ne partira en ligne qu'une fois les énoncés écrits.

Séance d'outillage : les exercices se rendent en captures et en fichiers de journal, pas en code.

## Courts — valider la compréhension

### 1 — L'inventaire de la machine
Vérifier en ligne de commande la présence et la version du compilateur, de Git et de CMake, et rendre les quatre lignes de sortie obtenues.

### 2 — Du source à l'exécutable
Compiler un fichier unique à la main, en une commande, sans IDE. Nommer chaque étape traversée et dire ce que chacune produit.

### 3 — Casser volontairement
Provoquer trois erreurs distinctes — faute de syntaxe, fonction déclarée mais absente, en-tête introuvable — et dire pour chacune qui se plaint : le préprocesseur, le compilateur ou l'éditeur de liens.

### 4 — Le PATH
Renommer temporairement le dossier de CMake, constater l'échec, lire le message, et expliquer ce que le système cherchait et où.

## Complet — reprendre toute la séance

### 5 — La fiche d'installation de l'année
Écrire la procédure d'installation complète du poste de travail, testée sur une machine vierge ou une machine virtuelle : outils, versions, options d'installation qui comptent, vérifications à chaque étape, et les trois erreurs les plus probables avec leur solution. Le rendu doit permettre à un camarade de tout installer sans poser de question.

## Difficile — se projeter

### 6 — Le même projet sur trois machines
Faire compiler le même petit projet sur trois configurations différentes — deux systèmes, deux compilateurs au minimum — et relever tout ce qui diffère : chemins, options, avertissements, comportement de l'exécutable. Écrire ensuite ce qui, dans le projet, dépendait de la machine sans qu'on l'ait voulu. Prolongement : dire ce que CMake va régler de ces problèmes, et ce qu'il ne réglera pas.
