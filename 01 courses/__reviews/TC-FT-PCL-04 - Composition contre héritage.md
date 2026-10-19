---
slides: "[[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage]]"
exercices: "[[01 courses/exercises/Theory/TC-FT-PCL-04 - Composition contre héritage]]"
---
- [x] Rédiger le deck — 22 slides, de 14 titres sans contenu
- [x] Schéma de l'ECS
- [x] Widget du décompte des combinaisons
- [ ] Rédiger la feuille d'exercices — toujours à l'état d'overview

## Traité le 19.10 — à vérifier

La fiche était **vide** : le template l'avait créée, sans checklist. J'ai pris le brief dans
la note de séance — « hiérarchie profonde et ses impasses, modèle composant, orientation
données, principe de l'ECS » — et rédigé le deck sur son squelette. **Si ce n'était pas la
demande, c'est ici qu'il faut le dire.**

**Deck**, 22 slides, en quatre temps : l'arbre qui ne pousse plus, assembler, les données
d'un côté, où placer le curseur. Aucune slide hors cadre.

**Widget** `composition_widget.html` : on coche les capacités du jeu, et deux compteurs se
répondent — les classes qu'exigerait l'héritage, les composants qu'exige la composition.
À six capacités : **63 contre 6**. Une capacité de plus double la colonne de gauche et
ajoute un à celle de droite.

**Schéma** `pcl04_ecs.svg` : entités réduites à un numéro, tableaux de composants sans trou,
et sous chaque tableau la flèche du système qui le balaie. Le tableau dense est l'argument —
la donnée suivante est déjà dans la ligne de cache.

## Quatre arbitrages, à confirmer ou à casser

**1. Le compte est `2^n − 1`, toutes combinaisons confondues.** C'est le pire cas : il
suppose qu'on veut *tous* les mélanges. Un jeu réel n'en veut qu'une poignée, et l'écart se
réduit. J'ai gardé le pire cas parce que c'est lui qui rend l'argument lisible en trente
secondes, et parce que c'est le chiffre que l'exercice 1 demande déjà. La slide *Le test, en
une question* nuance : le problème n'arrive que si les catégories **se combinent**.

**2. La source ECS n'existe pas.** `Entity Component System` est un squelette de 160 octets,
et il est dans `_archive/`. Rien à en extraire : la partie ECS est écrite de zéro. Les trois
slides concernées sont donc à relire comme du contenu neuf, pas comme une reprise.

**3. `solid_principles_in_unity` n'a pas été rouvert.** La note de séance dit que ses quatre
heures partent à PCL-01, APU-01 et APU-09 — et PCL-04 n'y est pas nommée pour autre chose
que le thème. J'ai écrit depuis le squelette. **À vérifier** : s'il y avait des schémas de ce
support à transposer ici, ils manquent.

**4. L'exemple de code est en C#, pas en C++.** Le bloc *Une capacité devient une pièce*
utilise `new Entite()` et `Ajouter(...)`, et la slide suivante parle de `GameObject` et
d'`AddComponent`. La séance est dans le bloc *Fondamentaux Théoriques*, donc sans langage
imposé, mais elle suit POO-06 qui est en C++. J'ai choisi C# parce que le modèle composant
**est** Unity, et que c'est là que les étudiants le rencontreront. À basculer en C++ si tu
préfères la continuité du bloc.

## Hors périmètre

La feuille d'exercices reste un **overview** : six pistes de deux lignes, rien de rédigé.
Elle n'était pas dans le brief de la séance, et le deck y renvoie déjà par son atelier.
