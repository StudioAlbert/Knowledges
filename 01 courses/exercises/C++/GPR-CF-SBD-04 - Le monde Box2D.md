# Exercices — GPR-CF-SBD-04 — Le monde Box2D

> Cours associé : [[01 courses/slides/C++/GPR-CF-SBD-04 - Le monde Box2D|GPR-CF-SBD-04 - Le monde Box2D]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, le projet CMake
> avec Box2D et les corrigés viendront après validation de ces pistes.

Rien n'est affiché dans cette fiche : tout se vérifie dans la console. L'affichage arrive en `GPR-CF-SBD-05`.

## Courts — valider la compréhension

### 1 — La chute libre
Un monde avec gravité, un seul corps dynamique, et la position affichée à chaque pas pendant une seconde. Comparer la chute obtenue à la formule vue en physique.

### 2 — La caisse et le sol
Ajouter un sol statique et montrer, par les valeurs affichées, que la caisse s'arrête dessus. Faire varier le rebond et commenter.

### 3 — Les trois types
Un corps de chaque type, une même poussée appliquée aux trois. Dire lequel bouge, lequel pousse sans être poussé, lequel ne bouge jamais, et à quel usage de jeu chacun correspond.

### 4 — Le facteur d'échelle
Créer un personnage de 180 unités de haut, observer le comportement absurde, puis introduire la conversion pixels vers mètres et refaire. Décrire les deux symptômes de l'oubli.

## Complet — reprendre toute la séance

### 5 — La scène physique
Un niveau complet en physique seule : sol et murs statiques, une plateforme cinématique qui va et vient, six caisses dynamiques empilées, une balle très rebondissante et une très amortie. Le programme affiche à intervalle régulier la position et la vitesse de chaque corps, et un résumé de la scène au repos. Le rendu commente ce que chaque réglage de matière a changé.

## Difficile — se projeter

### 6 — Le pont de planches
Une passerelle faite de dix planches reliées entre elles et ancrée aux deux bords, sur laquelle des caisses tombent. Régler les liaisons pour qu'elle ploie sans exploser, trouver le poids qui la fait céder, et mesurer le coût en temps de simulation quand on double le nombre de planches. Prolongement : dire ce qui se passe si le pas de simulation devient variable.
