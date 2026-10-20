---
seances: [GPR-CF-SBD-01, GPR-CF-SBD-02, GPR-CF-SBD-03, GPR-CF-SBD-04, GPR-CF-SBD-05, GPR-CF-SBD-06]
---
# Summative — le platformer

**Le rendu de la série**, à remettre à la fin de la sixième séance. Vous ne partez pas de
zéro : c'est le projet que vous construisez depuis la première heure, étape par étape, dans
[[01 courses/exercises/C++/GPR-CF-SBD - Le platformer, etape par etape|Le platformer, étape par étape]].

---

> [!tip] Les images sont fournies
> Le dépôt d'exemples porte un dossier `_Resources/sprites/` : planches Cuphead, sprites de
> Zelda dans les quatre directions, une planche de personnages, un décor de village et un
> mur. De quoi monter un niveau sans passer une soirée à chercher des PNG.

## Le genre, en deux phrases

Un platformer 2D se joue de profil. On y dirige un personnage de gauche à droite, on saute
d'une plateforme à l'autre, on évite ce qui blesse, et on atteint une sortie.

Tout le plaisir tient dans **le saut** : sa hauteur, sa durée, ce qui arrive quand on le
rate de deux pixels. C'est ce réglage-là qui est évalué, pas la quantité de contenu.

> [!info] Ce que vous écrivez vous-même
> En moteur, le personnage, la gravité et les collisions existent déjà. Ici, **vous écrivez
> la boucle, le temps, la liaison entre la physique et l'image, et le contrôleur**. C'est
> plus long, et c'est le but : vous saurez ce qu'un moteur fait à votre place.

---

## Ce qui est attendu de tous

| | Attendu | Vu en |
|---|---|---|
| **Déplacement** | le personnage se déplace horizontalement, au clavier **et** à la manette | SBD-02 |
| **Temps** | vitesses et animations identiques à 30 et à 144 images par seconde | SBD-03 |
| **Corps physique** | le personnage est un corps **dynamique** Box2D ; le décor est **statique** | SBD-04 |
| **Saut** | une touche, une impulsion, et **jamais** de saut en l'air | SBD-04, SBD-06 |
| **Plateformes** | au moins trois sortes : fixe, mobile, et traversable par en dessous | SBD-05, SBD-06 |
| **Obstacles** | au moins un danger qui fait perdre — pointes, vide, ou ennemi | SBD-05 |
| **Niveau** | un niveau lisible, qui monte en difficulté, et qui contient tout ce qui précède | — |
| **Reprise** | au moins un point de reprise : on ne recommence pas tout | — |
| **Score** | un compteur visible : pièces, temps, ou les deux | — |

---

## Et de quoi rendre le jeu **fun**

Piochez dans cette liste ce qui rendra votre jeu agréable à jouer. Il n'y a pas de quota :
mieux vaut deux ficelles bien réglées que six à moitié faites.

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

C'est l'exigence qui vient du cahier des charges d'origine, et c'est celle qui coûte le plus
cher si on l'ignore.

**Toutes** les valeurs de gameplay — vitesse, hauteur de saut, gravité, coyote time, facteur
mètre/pixel — vivent **à un seul endroit**, et nulle part ailleurs.

```cpp
// un fichier de réglages — le seul qu'on ouvre pour régler le jeu
namespace reglages {

inline constexpr float kPixelsParMetre = 32.f;
inline constexpr float kVitesseMarche = 6.f;      // m/s
inline constexpr float kImpulsionSaut = 9.f;      // m/s
inline constexpr float kGravite = 24.f;           // m/s²
inline constexpr float kCoyoteTime = 0.08f;       // s

}  // namespace reglages
```

Le nom du fichier vous appartient, et un fichier de configuration lu au démarrage vaut mieux
encore — on règle sans recompiler. Ce qui compte, c'est qu'**aucune valeur de gameplay ne
soit écrite en dur ailleurs**.

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
| **`README.md`** | les touches, les ficelles que vous avez ajoutées, et comment lancer le jeu |

---

## Comment c'est évalué

|                               | Ce qu'on regarde                                                                        |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| **Ça marche**                 | le jeu compile, se lance, se termine. Un jeu qui ne compile pas ne s'évalue pas.        |
| **Le saut est bon**           | quelqu'un d'autre que vous y joue cinq minutes sans s'énerver.                          |
| **Le code se lit**            | une classe par responsabilité, le schéma de conception de PCL-01 encore reconnaissable. |
| **Les ficelles sont là** | les options choisies marchent, et elles se sentent en jouant. |

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
