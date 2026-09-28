# Exercices — GPR-UN-VRG-10 — Feedback audio

> Cours associé : [[01 courses/slides/Unity/GPR-UN-VRG-10 - Feedback audio|GPR-UN-VRG-10 - Feedback audio]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, la banque de sons
> et les corrigés viendront après validation de ces pistes.

On reprend le prototype d'arène, désormais muet, et une banque de sons libres de droits.

## Courts — valider la compréhension

### 1 — Le son qui confirme
Ajouter un son à trois actions — tir, impact, ramassage — et faire jouer quelqu'un sans le son puis avec. Relever ce qu'il comprend en plus.

### 2 — La latence
Retarder volontairement le son d'impact de 0, 50, 100 et 200 millisecondes, faire deviner à l'aveugle, et donner le seuil à partir duquel le décalage se sent.

### 3 — Vingt tirs
Tirer vingt fois en une seconde avec le même échantillon, écouter, puis ajouter variation de hauteur et limite d'instances simultanées. Comparer les deux enregistrements.

### 4 — Les priorités
Saturer les voix pendant un combat, puis décider quels sons doivent passer devant et le mettre en place. Vérifier que le son de mort du joueur n'est jamais coupé.

## Complet — reprendre toute la séance

### 5 — La passe audio du prototype
Sonoriser toutes les actions du jeu avec variation, limites d'instances, priorités, catégories de mixage réglables par le joueur, atténuation spatiale, et un silence travaillé avant l'arrivée du boss. Le rendu est une capture vidéo de trente secondes de combat et le tableau des sons avec leur catégorie, leur priorité et leur limite.

## Difficile — se projeter

### 6 — Le mixage qui s'adapte
Faire baisser automatiquement les catégories secondaires quand une information importante est annoncée, remonter progressivement ensuite, et ajuster le mixage global selon un mode de sortie choisi — casque, télévision, petits haut-parleurs. Tester réellement sur trois sorties différentes, relever ce qui devient inaudible sur chacune, et corriger. Conclure sur ce qui, dans le mixage, doit rester entre les mains du sound designer plutôt que du programmeur.
