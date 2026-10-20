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
- [ ] Feuille d'exercices, tes annotations du 20.10 :
	- [x] Supprimer l'encadré **SFML 3, et rien d'autre** — SFML 3 arrive, le tableau de migration n'intéresse pas les élèves
	- [x] Supprimer les six encadrés **Le piège**, un par étape
	- [x] Supprimer l'**étape 6** : pas d'exercice pour les ficelles
	- [x] Réparer la **grille d'auto-évaluation** : elle casse au milieu et finit en texte brut
- [ ] Reprendre le companion pour intégrer SFML via vcpkg
- [ ] Faire une fiche de ressources "My first SFML project" qui les guide pour creer le premier projet SFML
	- [ ] Creation depuis Clion
	- [ ] ajout du Cmake, recopie depuis le companion
	- [ ] ajout de vcpkg
	- [ ] code "hello world" = afficher une fenetre
- [ ] Reprendre enoncé Summative
	- [ ] Reprendre depuis la fiche Unity
		- [ ] Genre Content
		- [ ] Screenshots de references
		- [ ] Chapitre des reglages : 
			- [ ] Simplifier par une simple mention que les reglages du jeu (saut, vitesse, gravité) doivent etre disponilbe dans un seul et mm fichier
			- [ ] Tenir compte des ratures
			- [ ] Garder encart de test
	

-------------------------------
### Sources complémentaires

- https://www.sfml-dev.org/tutorials/3.1/
- https://www.sfml-dev.org/documentation/3.1.0/
- https://github.com/jayjay1509/platformer
- https://github.com/StudioAlbert/GPR922_GPR4-1_SFML
  
  https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples

## Traité le 20.10 — les ateliers rentrent dans les decks

Le companion est effectivement prêt : `CMakeLists.txt` racine, SFML **3.1.0** par
`FetchContent` en statique, `/utf-8` pour MSVC, un `copy_data` qui pose le `data/` de chaque
cible à côté de son exécutable, et **dix-neuf cibles**. Nouvel audit : **plus aucun marqueur
SFML 2** dans les sources. Les quatorze cibles que je signalais le matin sont portées.

### Chaque deck porte son atelier, et nomme sa cible

| Deck | Atelier | Cibles citées en note |
|---|---|---|
| SBD-01 | fenêtre, décor, héros, carré blanc provoqué | `HelloWorld`, `Graphics` |
| SBD-02 | `Closed` / `Resized`, clavier puis manette, le son | `Events-a` à `-d`, `Audio`, `Sound` |
| SBD-03 | le `dt`, le carré trop rapide, la planche découpée | `TimeClock`, `Animation`, `AnimationClass`, `MoveAndJump` |
| SBD-04 | le monde, le pas fixe, les trois types de corps | **aucune** — voir plus bas |
| SBD-05 | la classe de conversion, la copie, `UserData` | `Views`, `Motor` |
| SBD-06 | **pas d'atelier**, une heure de finition | `MoveAndJump`, `LevelEditor` |

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
