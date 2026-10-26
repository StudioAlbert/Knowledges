---
slides:
exercices:
---
- [x] Le repo companion est pret, reprendre citations de code des decks depuis celui-ci
- [x] Les exercices retournent en tant qu'ateliers de chaque Deck
	- [x] Ceux ci sont amendés depuis la session Claude
- [x] Chaque atelier pointe vers une target du companion
	- [x] qui fera demonstration de l'atelier
	- [x] c'est du code de travail pour moi et parler de ce qui se passe
	- [x] les eleves doivent le recopier / reprendre dans leur propre projet
- [x] Feuille d'exercices, tes annotations du 20.10 :
	- [x] Supprimer l'encadré **SFML 3, et rien d'autre** — SFML 3 arrive, le tableau de migration n'intéresse pas les élèves
	- [x] Supprimer les six encadrés **Le piège**, un par étape
	- [x] Supprimer l'**étape 6** : pas d'exercice pour les ficelles
	- [x] Réparer la **grille d'auto-évaluation** : elle casse au milieu et finit en texte brut
- [x] Reprendre le companion pour intégrer SFML via vcpkg
- [x] Faire une fiche de ressources "My first SFML project" qui les guide pour creer le premier projet SFML
	- [x] Creation depuis Clion
	- [x] ajout du Cmake, recopie depuis le companion
	- [x] ajout de vcpkg
	- [x] code "hello world" = afficher une fenetre
- [ ] Reprendre enoncé Summative
	- [ ] Reprendre depuis la fiche Unity
		- [x] Genre Content
		- [ ] Screenshots de references
		- [x] Chapitre des reglages : 
			- [x] Simplifier par une simple mention que les reglages du jeu (saut, vitesse, gravité) doivent etre disponilbe dans un seul et mm fichier
			- [x] Tenir compte des ratures
			- [x] Garder encart de test
- [x] Check companion Box2D (voir sources)
	

-------------------------------
### Sources complémentaires

- https://www.sfml-dev.org/tutorials/3.1/
- https://www.sfml-dev.org/documentation/3.1.0/
- https://github.com/jayjay1509/platformer
- https://github.com/StudioAlbert/GPR922_GPR4-1_SFML
  
  https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples
  https://github.com/StudioAlbert/GPR-CF-SBD-XX---Box2D-Examples

## Traité le 20.10 — les ateliers rentrent dans les decks

Le companion est effectivement prêt : `CMakeLists.txt` racine, SFML **3.1.0** par
`FetchContent` en statique, `/utf-8` pour MSVC, un `copy_data` qui pose le `data/` de chaque
cible à côté de son exécutable, et **dix-neuf cibles**. Nouvel audit : **plus aucun marqueur
SFML 2** dans les sources. Les quatorze cibles que je signalais le matin sont portées.

### Chaque deck porte son atelier, et nomme sa cible

| Deck   | Atelier                                            | Cibles citées en note                                     |
| ------ | -------------------------------------------------- | --------------------------------------------------------- |
| SBD-01 | fenêtre, décor, héros, carré blanc provoqué        | `HelloWorld`, `Graphics`                                  |
| SBD-02 | `Closed` / `Resized`, clavier puis manette, le son | `Events-a` à `-d`, `Audio`, `Sound`                       |
| SBD-03 | le `dt`, le carré trop rapide, la planche découpée | `TimeClock`, `Animation`, `AnimationClass`, `MoveAndJump` |
| SBD-04 | le monde, le pas fixe, les trois types de corps    | **aucune** — voir plus bas                                |
| SBD-05 | la classe de conversion, la copie, `UserData`      | `Views`, `Motor`                                          |
| SBD-06 | **pas d'atelier**, une heure de finition           | `MoveAndJump`, `LevelEditor`                              |

Chaque note de présentation dit ce que tu demandais : la cible est une **démonstration**, du
code de travail qu'on lit et qu'on commente ensemble — pas un corrigé. Les étudiants
réécrivent dans **leur** projet.

**SBD-06 n'a plus d'atelier**, comme demandé. Sa slide dit pourquoi : les ficelles se posent
dans le jeu qu'ils ont déjà, et se jugent en jouant. L'heure sert à régler et à faire jouer
le voisin.

### Tes quatre annotations sur la feuille

- l'encadré **SFML 3, et rien d'autre** est supprimé — avec le companion en 3.1, le tableau
  de migration n'a plus de public ;
- les **six encadrés *Le piège*** sont supprimés ; leur contenu est déjà dans les decks, en
  slide ou en note de présentation ;
- l'**étape 6** est supprimée de la feuille ;
- la **grille d'auto-évaluation** est réparée et déplacée dans
  [[01 courses/exercises/C++/GPR-CF-SBD - Summative, le platformer|Summative — le platformer]],
  sous *Avant de rendre, cochez*. Vérifié rendu : sept lignes, dans l'encadré.

> [!bug] D'où venait la grille cassée
> De moi, ce matin. En ajoutant la ligne *choisir sa classe audio* par script, j'ai oublié
> le `>` de la citation. Une seule ligne sans préfixe ferme le bloc **et** le tableau — d'où
> la moitié de la grille en texte brut. C'est corrigé à la source.

## Un point à trancher

**SBD-04 n'a aucune cible de démonstration.** Le dépôt d'exemples ne contient pas de
Box2D — c'est la seule séance de la série sans code à montrer. Sa note de présentation le
dit, et l'heure se fait au tableau. Une cible `Box2D-a` dans le companion réglerait ça.

## Deuxième passe du 20.10 — tes annotations sur SBD-06 et la summative

**La feuille d'étapes est supprimée**, comme tu l'as confirmé. La summative est désormais le
**seul** exercice de la série : chaque séance n'a plus qu'un document dans son onglet, donc
il s'affiche directement — la règle de publication posée ce matin s'applique d'elle-même.

### SBD-06

La phrase de fin de *Ce qu'on attend d'un contrôleur* — « entre les deux, il n'y a que des
ficelles, et elles s'écrivent en dur » — est retirée. La slide s'arrête sur les trois
exigences, sans préjuger de la façon de les tenir.

### La summative

| Ce que tu as barré ou annoté | Ce qu'elle dit maintenant |
|---|---|
| *Et deux options, à choisir* + « deux, pas une, pas quatre » | **Et de quoi rendre le jeu fun** — on pioche dans la liste, **pas de quota** : deux ficelles bien réglées valent mieux que six à moitié faites |
| `reglages.h` dans *Ce qu'on rend* | **un fichier de réglages** — le nom leur appartient |
| *l'écrit — une page* | supprimé |
| *L'écrit dit quelque chose* (évaluation) | supprimé |
| *Les réglages sont sortis* (évaluation) | **Les ficelles sont là** — les options marchent et se sentent en jouant |

La section **Les réglages ne se cherchent pas dans le code** (celle que tu as entourée) perd
ce qu'elle avait de prescriptif : plus de nom de fichier imposé, et l'encadré *Le test*
devient un test que **l'étudiant** se fait à lui-même, au lieu d'un critère de correction —
puisque la ligne d'évaluation correspondante est partie. Le principe, lui, reste : aucune
valeur de gameplay écrite en dur ailleurs.

> [!question] Si l'intention était autre
> Un cercle, dans tes annotations précédentes, signalait un problème à régler — la grille
> cassée. Ici la section n'avait pas de défaut de rendu : je l'ai donc lue à la lumière des
> deux autres annotations, qui dé-prescrivent le fichier et retirent le critère. Si tu
> voulais au contraire la renforcer, ou la supprimer, dis-le.

### Les images

Le dossier `_Resources/sprites/` du companion est signalé dans la summative : planches
Cuphead, Zelda dans les quatre directions, une planche de personnages, un village, un mur.
Les étudiants ne perdront pas une soirée à chercher des PNG.

## Traité le 26.10 — vcpkg, la fiche du premier projet, et l'état du dépôt Box2D

### Le companion passe à vcpkg

`FetchContent` recompilait SFML dans chaque dossier de build. Le dépôt prend
maintenant **vcpkg**, comme les projets des étudiants.

```cmake
find_package(SFML 3 COMPONENTS Graphics Audio System REQUIRED)
```

Un `vcpkg.json` déclare `sfml` avec `graphics`, `window` et `audio` — pas `network`,
aucune cible ne s'en sert. Les DLL sont recopiées à côté des exécutables par vcpkg
lui-même : il n'y a plus de raison de compiler en statique.

> [!check] Vérifié, pas supposé
> `cmake --build` sur la totalité : **les dix-neuf cibles compilent**, zéro erreur.
> Commit `ee44c51` dans le dépôt d'exemples, **pas encore poussé**.

Le `README.md` du dépôt dit la nouvelle ligne de commande, et mentionne le panneau
Vcpkg de CLion qui rend la toolchain implicite.

### La fiche du premier projet

[[01 courses/resources/C++/GPR-CF-SBD-01 - Mon premier projet SFML|Mon premier projet SFML]],
rattachée à SBD-01. Quatre étapes, dans ton ordre : CLion, vcpkg, le CMake, la fenêtre.

La recette n'est pas écrite de mémoire : **j'ai monté le projet et je l'ai compilé**
avant de la rédiger. Ce qui en sort :

- vcpkg livre **SFML 3.1.0**, la même version que le companion ;
- en mode manifeste, `vcpkg.json` suffit — pas de `vcpkg install` à taper ;
- `find_package(SFML 3 COMPONENTS Graphics REQUIRED)` trouve la bibliothèque, et
  les DLL arrivent à côté de l'exécutable sans rien demander.

La fiche finit sur l'encadré qui leur fera gagner le plus de temps : le signe qui
trahit un exemple SFML 2 trouvé en ligne, `sf::Event event; while (pollEvent(event))`.

### Le dépôt Box2D : il existe, et il est en Box2D 2

Tu l'as poussé le 26.10 à 09h29. Je l'ai cloné et audité.

| | |
|---|---|
| Cibles | **10 répertoires**, 5 669 lignes de `.h` et `.cpp` |
| Box2D | **2.x partout** — `b2ContactListener`, `b2FixtureDef`, `CreateFixture`, `b2Body*` |
| Marqueurs Box2D 3 | **aucun** |
| SFML | **2.x partout** — 29 fichiers, aucun marqueur SFML 3 |
| Build | projets Visual Studio `.vcxproj` + un `.sln` ; **deux** `CMakeLists.txt` sur dix |
| Son README | « Warning, there's some obsolete files » |

C'est donc un **double portage** — Box2D 2 → 3.2 *et* SFML 2 → 3.1 — plus un système
de build à écrire. `05-SpriteMovement` pèse à lui seul 1 908 lignes et ressemble à un
petit jeu complet.

Tu as choisi de le porter. Je propose de le faire **par étages**, dans l'ordre où les
decks en ont besoin, en compilant à chaque étage :

| Étage | Contenu | Pour |
|---|---|---|
| 0 | racine CMake, vcpkg (SFML 3.1 + Box2D 3.2), `_Utilities`, `copy_data` | — |
| 1 | `01-Gravity` | SBD-04, la physique seule |
| 2 | `02-Bouncing`, `04-ZeroGravity` | SBD-05 les contacts, SBD-06 les capteurs |
| 3 | `03-BouncingAdvanced`, `05-SpriteMovement`, les deux formatives | en plus |

L'étage 1 suffit déjà à donner à SBD-04 la démonstration qui lui manque, et surtout
à **compiler enfin** le code Box2D 3.2 des trois decks.

### Deux cases que je ne peux pas cocher

> [!question] La fiche Unity n'est pas dans le vault
> *Reprendre enoncé Summative → Reprendre depuis la fiche Unity* : il n'existe aucune
> summative Unity ici, et « Genre Content » n'apparaît que dans cette fiche. Soit elle
> vit ailleurs — `_GSDA_Tech_Vault` ? un Google Doc ? — soit tu l'as en tête. Dis-moi
> où la lire.

> [!question] Les screenshots de référence
> Je ne peux pas les inventer. Trois façons de les avoir :
> - des captures des cibles du companion qui tournent — `Motor`, `LevelEditor` ;
> - des captures de platformers du commerce, mais alors **hors du site public** ;
> - les tiennes, déposées dans `00 images/`.
>
> Dis laquelle, et je les intègre.

### Ce qui est fait sur la summative

Le chapitre des réglages passe de dix-huit lignes — dont un bloc de code qui imposait
des noms de constantes — à **deux lignes** :

> Les réglages du jeu — saut, vitesse, gravité — vivent dans **un seul et même
> fichier**. Le nom de ce fichier vous appartient.

L'encadré *Le test que vous pouvez faire vous-même* est gardé tel quel, comme demandé.
Les ratures de tes annotations du 20.10 étaient déjà reportées.

### Au passage : huit liens morts

La feuille d'étapes supprimée restait citée **huit fois** : dans les six notes de
séance, dans le frontmatter `exercices:` de la fiche SBD-01, et dans la summative
elle-même. Tous réparés — ils pointent la summative, qui est bien le seul exercice de
la série.

Les six notes de séance portaient aussi un bloc `[!todo] Produit les 27 et 28
septembre, en attente de validation` devenu entièrement faux : « 15 slides,
`publish: false` », « Rien n'est rédigé », un widget `plateforme_widget.html` qui
n'a jamais existé. Remplacé par l'état réel — deck, nombre de slides, cible de
démonstration, rendu. Ce bloc n'est pas publié : il ne te gênait que dans Obsidian.
