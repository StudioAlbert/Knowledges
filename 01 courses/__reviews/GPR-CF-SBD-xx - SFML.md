---
slides:
exercices:
---
- [ ] Porter le companion Box2D
	- [x] importer comme submodule https://github.com/StudioAlbert/GPR-CF-SBD-XX---Box2D-Examples.git
	- [x] Verifier veracité des slides
- [x] Citer les exemples des differents companion (lien github du fichier concerné) dans les sildes
	- [x] Pas de texte cité de facon implicite dans le slide, mais un lien ecrit en petit en bas des slides (cf annotation)
- [x] intégrer (Embdede) les images de référence de l'énoncé Unity 
- [x] Pour les 6 seances SBD, proposer résumé du contenu au format Aurora (Plateforme de planning GSDA)
	- [x] Ex d'intitulé : Monde graphique contre monde physique, ce qu'est un moteur de jeu, sous-systèmes de SFML et ce qu'ils valent, `sf::RenderWindow`, boucle de jeu, événements, limitation du framerate
- [x] Ne plus citer la prochaine seance dans les slides de fin (**Review de tout le vault**)
- [x] Le widget est buggé, bouton Rejouer
	- [x] , sur ce widget eviter les interactions, privilégiez les indications graphiques, stop and go dans l'animation pour prouver le point, etc....
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
- [x] Reprendre enoncé Summative
	- [x] Reprendre depuis la fiche Unity
		- [x] Genre Content
		- [x] Screenshots de references
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

Enoncé Unity : [[2D Platformer]]


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

## Deuxième passe du 26.10 — tes points rouverts

### La summative, depuis la fiche Unity

`01 courses/projects/Unity/_archives_to_cut/2D Platformer` trouvée. Son cahier des
charges est **déjà couvert point par point** par la summative : déplacement, corps
physique, saut, plateformes, obstacles, level design, checkpoints, score, et les
options — power-ups, ennemis, saut maintenu, coyote time, jump buffer, wall jump,
glissade murale. Rien à reprendre de ce côté.

Ce qui manquait, c'était sa section **Screenshots / References**. Elle devient le
chapitre *À quoi ça ressemble* :

| | |
|---|---|
| Super Mario Bros, du début à la fin | le genre dans sa forme la plus pure |
| Les cartes des niveaux de Mario | la montée en difficulté qui se **voit** |
| Celeste | la référence actuelle du saut bien réglé |
| *Building a Better Jump* (GDC) | d'où viennent la gravité asymétrique et la hauteur variable |
| *5 Tips for Better Platformers* | en Unity, mais les idées se transposent |

J'ai vérifié chaque titre YouTube plutôt que de les deviner d'après l'identifiant.

> [!info] Des liens, pas des images
> La fiche Unity encadre des captures de Celeste et de Mario, hébergées chez
> Micromania et JustForGames. Cette summative-là est **publiée** : y recopier les
> images reviendrait à les servir depuis notre site. Donc des liens.

Les packs **Kenney** (CC0) rejoignent l'encadré des images, à côté du
`_Resources/sprites/` du companion.

### Le widget du saut

Deux vrais bugs, dont un que j'avais introduit :

> [!bug] Deux boucles d'animation en parallèle
> `montrer(location.hash.slice(1))` était écrit **deux fois** à la fin du fichier.
> Deux boucles avançaient la même simulation, d'où le mouvement saccadé. Le bouton
> *Rejouer* pouvait en démarrer une troisième.

Comme tu le demandes, **plus rien à cliquer** : le bouton est supprimé et la
démonstration tourne seule, en **stop and go**.

| Moment | Ce qui se passe |
|---|---|
| l'appui | **gel 1,4 s** — un trait vertical relie les deux coureurs, une étiquette dit ce qui part |
| le résultat | **gel 2,6 s** — qui est passé, qui est tombé |
| puis | la démonstration recommence, en boucle |

`buffer` fige deux fois, un gel par appui. Les trois autres une fois. Le trait
vertical est le cœur du propos : les deux coureurs sont à la même abscisse, donc au
même instant.

> [!check] Vérifié en pompant la boucle à la main
> Le panneau tourne en arrière-plan et y gèle `requestAnimationFrame` ; j'ai donc
> appelé la boucle image par image. **Trois cycles complets observés**, période
> 8,5 s, boucle toujours vivante. Un second bug trouvé là : `!etat.gel` est faux
> quand `gel` vaut `−0,003`, donc la simulation restait figée après le premier gel.

### Plus de « prochaine séance » dans les slides de fin

**Dix-neuf decks** nettoyés, deux formes :

- **14** avec `### Prochaine séance` et son lien sur la slide `# Questions ?` — retirés en entier ;
- **5** avec une puce `- Séance suivante :` en tête de *Pour aller plus loin* — la puce seule est retirée, les autres liens restent.

Les fins en *Fin du bloc* et *Fin de la série* ne citent pas de séance suivante :
elles sont gardées.

### Les exemples sont cités avec leur lien

**Vingt liens** vers le fichier exact, dans les notes de présentation et dans deux
slides. SBD-04 n'en a aucun : il n'a toujours pas de cible.

Attention à un piège évité : en SBD-02, `Sound` désigne tantôt la cible, tantôt
`sf::Sound`. Les liens ne sont posés que là où il s'agit de la cible.

> [!danger] Ces liens renvoient 404, et ce n'est pas la faute des liens
> **Le dépôt d'exemples n'a jamais été poussé.** Son `main` distant en est encore à
> l'ancien dossier `923-4FSC0PF001-SFML`. Deux commits attendent en local :
> `9735d1e` — ton portage CMake et SFML 3 — et `ee44c51`, le passage à vcpkg.
>
> Conséquence plus grave que les liens : **le vault poussé référence `9735d1e`**,
> un commit qui n'existe pas sur GitHub. Un `git clone --recurse-submodules` du
> vault **échoue déjà aujourd'hui**, et pas à cause de cette session.
>
> Un `git push` dans le companion répare les deux d'un coup.

### La slide de SBD-01 que tu as barrée

« C'est la seule concession de SFML à la simplicité, et elle est assumée » est
retirée. La slide s'arrête sur *Trois rôles dans un seul objet.*

## Troisième passe du 26.10 — le code des decks compile enfin

### La véracité des slides, prouvée par le compilateur

J'ai recopié **chaque extrait de code** de SBD-04, SBD-05 et SBD-06 dans un seul
fichier, et je l'ai compilé contre Box2D 3.2.0 et SFML 3.1.0. Il compile.

> [!bug] Ce que la compilation a attrapé
> `b2World_SetPreSolveCallback` prend **quatre** arguments, pas trois :
>
> ```cpp
> b2World_SetPreSolveCallback(monde, Traversable, nullptr, nullptr);
> ```
>
> Le troisième est le rappel *pre-continuous* — c'est précisément là qu'il vit.
> La slide est corrigée.

Ce qui est désormais vérifié, et non plus lu dans la doc : le monde et son pas
fixe, le corps et ses trois types, `b2MakeBox` avec `material.friction`, `b2Pos`
et `b2Body_GetPosition`, `sf::radians(b2Rot_GetAngle(b2Body_GetRotation(...)))`,
les trois gestes de déplacement, `b2World_GetContactEvents` avec
`b2Shape_GetUserData`, le capteur de sol et son compteur, le coyote time, le jump
buffer, et la plateforme à sens unique avec `pointCount = 0`.

### Le dépôt Box2D, premier étage

Importé en sous-module, et `01-Gravity` est porté : **il compile et il tourne**.
C'est la démonstration qui manquait à SBD-04 — une bille dynamique qui tombe, que
le clic téléporte sous la souris.

| Avant | Après |
|---|---|
| projets `.vcxproj` | `CMakeLists.txt` racine + une cible par dossier, par vcpkg |
| `b2World monde(gravite)` | `b2DefaultWorldDef` puis `b2CreateWorld` |
| `b2Body*`, `CreateFixture` | `b2BodyId`, `b2CreateCircleShape` |
| `bodyDef.fixedRotation` | `bodyDef.motionLocks.angularZ` |
| `world_.Step(dt, 6, 2)` | `b2World_Step(monde, dt, 4)` |
| `sf::Event event; pollEvent(event)` | `while (const std::optional event = ...)` |

Son facteur de conversion était déjà **100 px/m** — ce qui confirme le chiffre
retenu pour les decks.

> [!warning] Neuf cibles restent en Box2D 2 et SFML 2
> `00-Starter`, `02-Bouncing`, `02-BouncingAndCollsions`, `03-BouncingAdvanced`,
> `04-ZeroGravity`, `05-SpriteMovement` et les deux formatives. Seul `01-Gravity`
> est dans le `CMakeLists.txt` racine ; les autres y entreront au fur et à mesure.
>
> La prochaine utile est **`02-Bouncing`** : elle démontre les contacts, donc
> SBD-05. Puis `04-ZeroGravity`, qui a un capteur — SBD-06.

### Ton vcpkg est passé à box2d 3.2.0

Il était à **3.1.1**, et la base de versions ne connaissait pas la 3.2.0 : le
`builtin-baseline` ne suffisait pas, il fallait le `git pull`. Fait, 56 commits.

J'ai vérifié avant : **SFML et gtest ne sont pas touchés** par cette mise à jour,
donc `cpp-exam-925` ne bouge pas.

> [!question] Et chez les étudiants ?
> Un étudiant dont le vcpkg date d'avant le 22.10 aura exactement la même erreur,
> sans le message qui explique pourquoi. Deux façons de l'éviter : leur dire de
> faire `git pull` dans vcpkg avant SBD-04, ou récupérer box2d par `FetchContent`
> au tag `v3.2.0` dans leur projet. Dis-moi laquelle tu préfères et je l'écris
> dans la fiche *Mon premier projet SFML*.

### Les exemples cités en petit, en bas de slide

Comme ton annotation le demande. Plus de citation fondue dans la prose : la phrase
s'arrête, et le lien vient dessous.

> Six lignes, et une fenêtre noire qui ne répond pas encore.
> <small>Exemple : HelloWorld.cpp</small>

Neuf slides portent maintenant leur ligne d'exemples : les six ateliers, plus les
slides du son, de la planche de sprites et du programme minimal. Les notes de
présentation gardent le commentaire, plus les liens.

### Les images de référence sont embarquées

Deux des trois URL de la fiche Unity sont vivantes :

| | |
|---|---|
| `ref_mario_platformer.jpg` | *New Super Mario Bros. U* — 800 × 450 |
| `ref_celeste_platformer.jpg` | *Celeste* — 1920 × 1080 |

La troisième, chez Micromania, **ne renvoie pas une image** mais une page HTML de
952 octets. Elle est abandonnée.

Les fichiers sont copiés dans `00 images/` plutôt que pointés chez leur hébergeur :
un lien direct vers le serveur d'un tiers casse le jour où il déplace son fichier,
et consomme sa bande passante à chaque visite.

### Les résumés Aurora

Les six `À couvrir` étaient périmés — SBD-02 annonçait des sprites alors que le
deck fait les événements, SBD-03 annonçait le son alors qu'il fait le temps, et
SBD-04 comme SBD-05 citaient `b2Fixture` et `ContactListener`, disparus en Box2D 3.

Chaque note porte maintenant un **Résumé proposé pour Aurora**, tiré de ce que son
deck enseigne vraiment, dans le même format d'une ligne. L'`À couvrir` d'origine
est gardé au-dessus : c'est ce qu'Aurora contient aujourd'hui, jusqu'à ce que tu
colles le nouveau.
