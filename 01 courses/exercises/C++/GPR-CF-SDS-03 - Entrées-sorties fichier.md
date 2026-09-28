# Exercices — GPR-CF-SDS-03 — Entrées-sorties fichier

> Cours associé : [[01 courses/slides/C++/GPR-CF-SDS-03 - Entrées-sorties fichier|GPR-CF-SDS-03 - Entrées-sorties fichier]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les fichiers
> d'exemple et les corrigés viendront après validation de ces pistes.

## Courts — valider la compréhension

### 1 — Ouvrir ce qui n'existe pas
Tenter de lire un fichier absent sans vérifier l'ouverture, décrire le comportement obtenu, puis ajouter la vérification et un message utile.

### 2 — Le fichier de réglages
Lire un fichier de réglages ligne par ligne, découper chaque ligne en clé et valeur, ignorer les commentaires et les lignes vides, et afficher les réglages obtenus.

### 3 — Le meilleur score
Lire le meilleur score, le comparer au score de la partie, réécrire le fichier si besoin. Traiter le premier lancement, quand le fichier n'existe pas encore.

### 4 — Texte contre binaire
Écrire mille positions de joueur en texte puis en binaire, comparer la taille des deux fichiers et le temps d'écriture, et regarder les deux dans un éditeur.

## Complet — reprendre toute la séance

### 5 — La sauvegarde de partie
Sauvegarder et recharger l'état complet d'une partie : joueur, inventaire, position, ennemis vivants, temps écoulé. Le format est binaire, la relecture reconstruit exactement l'état, et une sauvegarde tronquée à la main doit être détectée plutôt que chargée à moitié. Le rendu montre une partie sauvegardée, fermée, rechargée et poursuivie.

## Difficile — se projeter

### 6 — La sauvegarde qui survit à la mise à jour
Ajouter au format un numéro de version et une somme de contrôle, puis faire évoluer le jeu deux fois — un champ ajouté, un champ supprimé — en gardant la capacité de relire les sauvegardes des versions précédentes. Corrompre volontairement un fichier et montrer que le jeu refuse proprement. Conclure sur ce que les formats sérialisés du monde réel font à la place, ce qui ouvre `GPR-CF-SDS-04`.
