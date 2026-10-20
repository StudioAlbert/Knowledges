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

## Deux points à trancher

**1. La feuille d'étapes n'a plus de lecteur.** Les six decks portent leur atelier et
**aucun ne la cite plus**. Ce qu'il en reste — cinq étapes sans leurs pièges — fait doublon
avec les slides, et reste publié dans l'onglet *Exercices* des six séances. Je ne l'ai pas
supprimée : dis-moi si elle part, et la summative devient le seul exercice de la série.

**2. SBD-04 n'a aucune cible de démonstration.** Le dépôt d'exemples ne contient pas de
Box2D — c'est la seule séance de la série sans code à montrer. Sa note de présentation le
dit, et l'heure se fait au tableau. Une cible `Box2D-a` dans le companion réglerait ça.
