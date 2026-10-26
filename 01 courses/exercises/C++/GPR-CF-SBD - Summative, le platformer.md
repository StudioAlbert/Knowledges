---
seances: [GPR-CF-SBD-01, GPR-CF-SBD-02, GPR-CF-SBD-03, GPR-CF-SBD-04, GPR-CF-SBD-05, GPR-CF-SBD-06]
---
# Summative — le platformer

**Le rendu de la série**, à remettre à la fin du module.

---

> [!tip] Les images sont fournies
> Le dépôt d'exemples porte un dossier `_Resources/sprites/` : planches Cuphead, sprites de
> Zelda dans les quatre directions, une planche de personnages, un décor de village et un
> mur. De quoi monter un niveau sans passer une soirée à chercher des PNG.
>
> S'il vous en faut d'autres, Kenney les donne en CC0 — aucune condition, pas même la
> mention : [Platformer Pack Redux](https://kenney.nl/assets/platformer-pack-redux) et
> [Pixel Platformer](https://www.kenney.nl/assets/pixel-platformer).

## Le genre, en deux phrases

Un platformer 2D se joue de profil. On y dirige un personnage de gauche à droite, on saute
d'une plateforme à l'autre, on évite ce qui blesse, et on atteint une sortie.

Tout le plaisir tient dans **le saut** : sa hauteur, sa durée, ce qui arrive quand on le
rate de deux pixels. C'est ce réglage-là qui est évalué, pas la quantité de contenu.

---

## À quoi ça ressemble

Avant d'écrire une ligne, regardez ce que vous visez.

![[ref_mario_platformer.jpg]]

***New Super Mario Bros. U*** — tout le vocabulaire du genre sur une seule image : un sol,
des plateformes à atteindre, un trou entre les deux, des ennemis qui traversent, des pièces
à ramasser, un compteur en haut.

![[ref_celeste_platformer.jpg]]

***Celeste*** — la même grammaire, trente ans plus tard : des pointes qui tuent, des blocs
qui portent, et un saut réglé au centième. C'est la référence du game feel **et** de
l'accessibilité.

| | |
|---|---|
| [Super Mario Bros, du début à la fin](https://www.youtube.com/watch?v=cWOkHQXw0JQ) | le genre dans sa forme la plus pure — un bouton, un saut, et quarante ans de descendance |
| [Les cartes des niveaux de Mario](http://nintendoforever.free.fr/Nes/SuperMarioBros1/SuperMarioBros1_Dossier/SuperMarioBros1_Cartes.php) | chaque niveau à plat : la montée en difficulté se **voit** |
| [Celeste](https://www.celestegame.com/) | la référence actuelle du saut bien réglé, et de l'accessibilité |

Deux vidéos qui valent une heure de cours :

- [**Building a Better Jump**](https://www.youtube.com/watch?v=hG9SzQxaCm8) — GDC. D'où viennent la gravité asymétrique et le saut à hauteur variable, démontrés au tableau.
- [**5 Tips for Better Platformers**](https://www.youtube.com/watch?v=8QPmhDYn6rk) — en Unity, mais les idées se transposent telles quelles.

> [!tip] Regardez les cartes avant de dessiner votre niveau
> Un niveau de Mario introduit **une** idée, la donne à tester et comprendre au joueur avant
> d'en faire une réelle difficulté.

---

## Ce qui est attendu de tous

|                    | Attendu                                                                                           | Vu en          |
| ------------------ | ------------------------------------------------------------------------------------------------- | -------------- |
| **Déplacement**    | le personnage se déplace horizontalement, au clavier **et** à la manette                          | SBD-02         |
| **Temps**          | vitesses et animations identiques à 30 et à 144 images par seconde                                | SBD-03         |
| **Corps physique** | le personnage est un corps **dynamique** Box2D ; le décor est **statique**                        | SBD-04         |
| **Saut**           | une touche, une impulsion, et **jamais** de double saut                                           | SBD-04, SBD-06 |
| **Plateformes**    | au minimum : des plateformes fixes<br>si possible : mobile, et traversable par en dessous         | SBD-05, SBD-06 |
| **Obstacles**      | un danger qui fait perdre;<br>au minimum : tomber dans le vide<br>si possible : pointes, ennemies | SBD-05         |
| **Niveau**         | un niveau lisible, qui monte en difficult                                                         | —              |
| **Reprise**        | mettre des checkpoints                                                                            | —              |
| **Score**          | un compteur visible : pièces, temps, ou les deux                                                  | —              |

---

## Et de quoi rendre le jeu **fun**

Piochez dans cette liste ce qui rendra votre jeu agréable à jouer. Il n'y a pas de quota :
mieux vaut deux techniques bien réglées que six à moitié faites.

- **Saut maintenu** — la hauteur dépend du temps pendant lequel la touche reste enfoncée.
- **Coyote time** — le saut reste possible quelques centièmes de seconde après avoir quitté
  le sol. Vu en SBD-06.
- **Jump buffer** — une touche pressée juste avant l'atterrissage déclenche le saut dès le
  contact. Vu en SBD-06.
- **Wall jump** — un saut au contact d'un mur, qui repousse à l'opposé.
- **Glissade murale** — le personnage descend lentement le long d'un mur.
- **Bonus** — un objet ramassable qui change une capacité : vitesse, hauteur de saut, vie.
- **Ennemis** — au moins un ennemi qui patrouille, qu'on évite ou qu'on neutralise.

---

## Les réglages ne se cherchent pas dans le code

Les réglages du jeu — saut, vitesse, gravité — vivent dans **un seul et même fichier**. Le
nom de ce fichier vous appartient.

> [!tip] Le test que vous pouvez faire vous-même
> Doublez la valeur du saut dans votre fichier de réglages, et recompilez. Si le personnage
> saute deux fois plus haut et que rien d'autre ne casse, c'est gagné. Si vous devez chercher
> un `9.f` dans trois fichiers, il reste du travail.

---

## Ce qu'on rend

Un seul dépôt git, avec :

| | Ce qui est attendu |
|---|---|
| **le jeu** | il compile en une commande (`cmake -S . -B build`, `cmake --build build`) et se lance sans réglage manuel |
| **le code** | **six commits au moins**, un par étape, qui racontent la construction |
| **un fichier de réglages** | toutes les valeurs de gameplay, nommées et commentées avec leur unité |
| **`README.md`** | les touches, les techniques que vous avez ajoutées, et comment lancer le jeu |

---

## Comment c'est évalué

|                               | Ce qu'on regarde                                                                        |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| **Ça marche**                 | le jeu compile, se lance, se termine. Un jeu qui ne compile pas ne s'évalue pas.        |
| **Le saut est bon**           | quelqu'un d'autre que vous y joue cinq minutes sans s'énerver.                          |
| **Le code se lit**            | une classe par responsabilité, le schéma de conception de PCL-01 encore reconnaissable. |
| **Le game feel est là** | les options choisies marchent, et elles se sentent en jouant. |

## Avant de rendre, cochez

> [!check] Grille d'auto-évaluation
>
> | Je sais… | Vérification |
> |---|---|
> | ouvrir une fenêtre et afficher | le héros s'affiche, et je sais dire pourquoi un sprite devient blanc |
> | traiter les entrées | clavier et manette donnent le même déplacement, la fenêtre se redimensionne proprement |
> | choisir sa classe audio | je sais dire pourquoi une musique n'est pas un `sf::Sound` |
> | gérer le temps | la vitesse et l'animation ne dépendent pas du framerate |
> | faire vivre un monde physique | le héros tombe et s'arrête sans sprite |
> | relier les deux mondes | la conversion passe par une seule classe, et `au sol` est fiable |
> | rendre le jeu agréable | coyote time et jump buffer réglés, et je sais dire ce qu'ils changent |

> [!tip] Le conseil qui compte
> Un niveau court et un saut parfaitement réglé valent beaucoup mieux qu'un grand niveau et
> un personnage qui glisse. Si vous devez couper, coupez du **contenu**, jamais du réglage.
