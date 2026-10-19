---
slides: "[[01 courses/slides/Theory/TC-FT-PCL-03 - Taxonomie des patterns]]"
exercices: "[[01 courses/exercises/Theory/TC-FT-PCL-03 - Taxonomie des patterns]]"
---
- [x] Expliciter
	- [x]  dont la moitié se sont fondus dans les langages depuis.
- [x] ## Ceux qu'on croise vraiment en jeu
	- [x] Faire un slide par pattern avec le dètail pour chacun
		- [x] Quel probleme resout il ?
		- [x] comment ?
		- [x] Trouver une metaphore
-------------------
Sources complementaires

https://refactoring.guru/fr/design-patterns/what-is-pattern
https://refactoring.guru/fr/design-patterns/history
https://refactoring.guru/fr/design-patterns/why-learn-patterns
https://refactoring.guru/fr/design-patterns/criticism
https://refactoring.guru/fr/design-patterns/classification

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

L'argument est attribué à **Paul Graham**, comme le fait ta source
[Critiques](https://refactoring.guru/fr/design-patterns/criticism) — j'ai lu la page pour ne
pas le déformer. La note de présentation ajoute ce que la slide ne peut pas dire : la
critique est juste, et elle ne disqualifie pas les six retenus, parce que `State`,
`Component` et `Object Pool` n'ont **aucun** équivalent en mot-clé.

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
six en rouge parmi les dix-huit. Les douze autres sont là pour que la carte soit complète,
et la légende le dit — *sur la carte, pas au programme*.

### L'atelier est le quizz que tu décrivais

`patterns_quizz_widget.html` : sept situations, sept réponses possibles — les six patterns
plus **« aucun — du code simple suffit »**. La septième situation est justement celle-là,
une fabrique abstraite pour deux ennemis connus à l'écriture. La correction donne le
problème, le comment, la métaphore. Vérifié : les sept bonnes réponses valident.

**Fiche de ressources publiée** :
[[01 courses/resources/Theory/TC-FT-PCL-03 - Ressources|Ressources — les patterns]], avec tes
cinq liens refactoring.guru remis **dans un ordre de lecture**, et la page *Critiques*
signalée comme à lire avec les autres, pas après.

## Deux arbitrages

**1. `patterns_map_widget.html` n'est pas construit.** Le squelette proposait une carte
cliquable de quinze patterns. J'ai fait le **schéma** à la place : une carte de patterns est
une image statique, et ce que le widget ajoutait — une phrase par case — tient dans les six
slides de détail. Le budget est passé dans le quizz, que la fiche demandait et que le
squelette écrivait déjà dans l'atelier.

**2. Le tableau « ce que le langage a avalé » cite cinq patrons, pas « la moitié ».** La
phrase d'origine disait la moitié des vingt-trois. Je n'ai pas cherché à en lister douze :
cinq exemples que les étudiants reconnaissent valent mieux qu'une liste exhaustive dont ils
ne connaissent pas les deux tiers. La slide dit « la moitié », le tableau en montre cinq.

## Hors périmètre

La feuille d'exercices reste un **overview**. Le quizz couvre le terrain de l'atelier.
