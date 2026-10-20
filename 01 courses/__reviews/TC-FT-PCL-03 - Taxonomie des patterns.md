---
slides: "[[01 courses/slides/Theory/TC-FT-PCL-03 - Taxonomie des patterns]]"
exercices: "[[01 courses/exercises/Theory/TC-FT-PCL-03 - Taxonomie des patterns]]"
atelier: "[[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer]]"
ressources: "[[01 courses/resources/Theory/TC-FT-PCL-03 - Ressources]]"
---
- [x] Expliciter
	- [x]  dont la moitié se sont fondus dans les langages depuis.
- [x] ## Ceux qu'on croise vraiment en jeu
	- [x] Faire un slide par pattern avec le dètail pour chacun
		- [x] Quel probleme resout il ?
		- [x] comment ?
		- [x] Trouver une metaphore
- [x] Citer les sources dans une page ressources dédiée
	- [x] Ajouter la pages de Paul Graham
- [x] Slide **Ce n'est pas une recette** = Résumer la page https://refactoring.guru/fr/design-patterns/what-is-pattern
- [x] Pour chacune des 6 pages des patterns *de base* ajouter un schema pour chacun dans un slide qui fait suite a la definition ecrite
- [x] Faire suite au slide **le pattern de trop** par **le principe Yagni** (Traduire le passage Importance of following the YAGNI principle de la page geeks for geeks)
- [x] Intégrer une question "Peut on reconnaitre des patterns parmi la conception du platformer ?" dans l'atelier "Concevoir un platformer" cf autres seances du groupe
-------------------
Sources complementaires
https://refactoring.guru/fr/design-patterns/what-is-pattern
https://refactoring.guru/fr/design-patterns/what-i
https://refactoring.guru/fr/design-patterns/history
https://refactoring.guru/fr/design-patterns/why-learn-patterns
https://refactoring.guru/fr/design-patterns/criticism
https://refactoring.guru/fr/design-patterns/classification
https://unity.com/fr/resources/level-up-your-code-with-game-programming-patterns
https://www.geeksforgeeks.org/software-engineering/what-is-yagni-principle-you-arent-gonna-need-it/

## Traité le 20.10 — à vérifier

**Deck**, 22 slides, de 14 titres sans contenu. Aucune slide hors cadre.

### « Fondus dans les langages », explicité

Une slide le dit maintenant nommément, en tableau :

| Patron de 1994 | Ce qui l'a remplacé |
|---|---|
| Iterator | `for (auto& x : v)`, `foreach`, les générateurs |
| Strategy | une lambda, `std::function`, un `delegate` |
| Command | une lambda stockée dans une liste |
| Observer | `event` en C#, `UnityEvent`, les signaux |
| Prototype | `clone()`, `ICloneable`, les copies de valeur |

### Une slide par pattern, avec les trois entrées

Six slides, toutes bâties pareil — **le problème**, **comment**, **la métaphore** :

| Pattern | Métaphore retenue |
|---|---|
| Observer | une liste de diffusion |
| State | un feu tricolore : jamais vert et rouge à la fois |
| Strategy | un GPS : « le plus rapide » ou « sans péage » |
| Command | un ticket de restaurant, qui existe sans le client ni le cuisinier |
| Object Pool | la vaisselle d'un restaurant : on la lave, on ne la jette pas |
| Component | des briques : on assemble, on ne fabrique pas la brique parfaite |

**Schéma** `pcl03_trois_familles.svg` : les trois colonnes, la question de chacune, et les
six en rouge parmi les dix-huit.

### Le quizz

`patterns_quizz_widget.html` : sept situations, sept réponses possibles — les six patterns
plus **« aucun — du code simple suffit »**. La septième situation est justement celle-là,
une fabrique abstraite pour deux ennemis connus à l'écriture.

## Deuxième passe, le 20.10 — à vérifier

Le deck passe de 22 à **30 slides** : six schémas, la slide YAGNI, et la slide d'atelier.
**Aucune slide hors cadre**, aucune image cassée.

### Un schéma par pattern, juste après sa définition

Six générateurs neufs dans `tools/schemas/`, un par figure, tous relus sur le serveur de
test :

| Figure | Ce qu'elle montre |
|---|---|
| `pcl03_observer` | un sujet, quatre abonnés, et la phrase « le cinquième n'ouvre pas la boîte de gauche » |
| `pcl03_state` | l'automate du héros à gauche, les trois booléens et leur combinaison impossible à droite |
| `pcl03_strategy` | l'ennemi, l'interface, trois mises en œuvre — et « son code ne change jamais » |
| `pcl03_command` | la pile d'annulation : quatre actions, et le Ctrl+Z qui remonte en appelant `Undo` |
| `pcl03_object_pool` | seize cases allouées au chargement, six en vol, et le cycle prendre / rendre |
| `pcl03_component` | deux entités très différentes faites des mêmes pièces, dont aucune n'hérite |

### La slide *Ce n'est pas une recette*, refaite sur la source

C'est la distinction que
[what-is-pattern](https://refactoring.guru/fr/design-patterns/what-is-pattern) pose et que la
slide ne posait pas : **une recette, ce sont des étapes — c'est un algorithme ; un patron est
un plan**, qui montre le résultat et laisse la construction à qui le lit. La conséquence est
sur la slide : deux programmes qui appliquent le même patron n'ont pas le même code.

> [!warning] Deux auteurs, et je les avais mélangés
> La première passe attribuait à **Paul Graham** l'idée que la moitié des patrons ont été
> avalés par les langages. En lisant les sources, ce sont deux choses distinctes :
>
> - le **compte** est de **Peter Norvig** — *Design Patterns in Dynamic Languages*, présenté
>   en 1996 : **16 des 23** patrons sont « invisibles ou plus simples » dans un langage plus
>   expressif ;
> - l'argument de **Paul Graham**, dans *Revenge of the Nerds* (2002), est plus radical :
>   voir un patron se répéter dans son **propre** code est le signe d'une abstraction trop
>   faible. C'est lui qui cite Norvig, en note de bas de page.
>
> Les deux slides et la note de présentation disent maintenant qui dit quoi. La fiche de
> ressources aussi.

### La slide YAGNI

Elle suit *Le pattern de trop*, et reprend les quatre coûts de la page GeeksforGeeks —
**construction, retard, portage, réparation** — en français et en quatre mots, pas en
traduction mot à mot : une slide tient quatre puces, et le texte source est sous droits.
La dernière ligne porte la nuance que la même page insiste à poser : *YAGNI retarde
l'implémentation, il n'interdit pas de bien concevoir.*

### La page de ressources

[[01 courses/resources/Theory/TC-FT-PCL-03 - Ressources|Ressources — les patterns]] gagne
trois sections : **À la source** (Norvig et Graham, avec la mise au point ci-dessus),
**Ne pas en mettre partout** (GeeksforGeeks), et **Côté moteur** (l'e-book Unity en
français). Les trois liens ont été ouverts et répondent.

### L'atelier

La question que tu demandais est l'**étape 2** de
[[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer|Concevoir un platformer]] :
on reprend le schéma dessiné en PCL-01 et on cherche les patterns dedans, **avec obligation
d'assumer un « non »**. Une slide d'atelier a été ajoutée au deck pour y renvoyer.

## Deux points à trancher

**1. Trente slides pour une heure.** Six sont des schémas sans texte et passent vite, mais le
deck est devenu le plus long du bloc. Si l'heure déborde, le candidat au retrait est le
tableau *Ceux que le langage a avalés* — son argument tient déjà dans la slide *D'où ça vient*.

**2. `patterns_map_widget.html` n'est toujours pas construit.** Le squelette proposait une
carte cliquable de quinze patterns. Avec six schémas de plus, le besoin a encore baissé — mais
c'est ton appel.
