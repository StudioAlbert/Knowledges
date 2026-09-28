# Exercices — GPR-UN-APU-04 — ScriptableObjects, les données hors du code

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|GPR-UN-APU-04 - ScriptableObjects — les données hors du code]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, la scène de
> départ et les corrigés viendront après validation de ces pistes.

Terrain de jeu : le **Dungeon Crawler** du bloc, dont les statistiques d'ennemis sont écrites en dur dans trois scripts.

## Courts — valider la compréhension

### 1 — Sortir les chiffres du code
Créer un asset de configuration d'ennemi, y déplacer points de vie, vitesse et dégâts, et faire lire le prefab dedans. Le script ne doit plus contenir aucune valeur numérique.

### 2 — Cinq variantes sans code
Produire cinq ennemis sensiblement différents à partir du même prefab et du même script, uniquement par des assets. Montrer les cinq en jeu dans la même scène.

### 3 — Le piège de l'exécution
Modifier une valeur de l'asset pendant le jeu, arrêter, et constater qu'elle est restée. Expliquer ce qui s'est passé, puis proposer deux façons de s'en protéger.

### 4 — Un asset pour plusieurs prefabs
Faire pointer trois prefabs différents vers le même asset de réglages communs, changer une valeur, et vérifier que les trois suivent.

## Complet — reprendre toute la séance

### 5 — Le catalogue d'ennemis
Un catalogue complet en assets : familles d'ennemis, statistiques, butin, sons, préfab visuel associé. Le générateur de vagues lit le catalogue et ne connaît aucun type d'ennemi en particulier. Ajouter une sixième famille en fin d'exercice sans écrire de code, et livrer la scène plus la liste des assets.

## Difficile — se projeter

### 6 — L'équilibrage comme donnée
Reprendre le catalogue et y ajouter des tables d'équilibrage par niveau de difficulté, une validation qui refuse un asset incohérent — vitesse négative, butin inexistant, référence manquante — et un outil d'éditeur qui liste les assets fautifs avec la raison. Puis faire relire l'équilibrage par quelqu'un qui ne programme pas, et corriger ce qui l'a bloqué. Le rendu inclut son retour.
