---
slides: "[[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage]]"
exercices: "[[01 courses/exercises/Theory/TC-FT-PCL-04 - Composition contre héritage]]"
atelier: "[[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer]]"
---
- [x] Revisiter exercice
- [x] Reformulation Etape 3 : voir bloc ci dessous
- [x] Slide **Une capacité devient une pièce** : dire *si* les composants changent en cours de jeu


- [x] Rédiger le deck — 22 slides, de 14 titres sans contenu
- [x] Schéma de l'ECS
- [x] Basculer les snippets en c++
- [x] Widget du décompte des combinaisons
	- [x] Afficher la hierarchie de classes
	- [x] Eviter le cas du "pire", les situations nouvelles ne sont pas l'ajout d'une feature et l'ouverture de toutes les possibilités mais des cas réels qui imposeraient malgré tout la multiplication des classes :
		- [x] Prendre des examples dans les classes Donjons et dragons :
			- [x] Paladin = Wizard + Guerrier
			- [x] etc...
- [x] Slide Le compte = résumé des problèmes de combinaisons sans informations chifrées => plutot un graphe montrant l'évolution du nombre de classes au fil des implementations
- [x] L'ECS doit reduit à la conclusion : 3 Slides
	- [x] La modularité : prendre un exemple dans Unity : Personnage = Physique + Rendu + Animation + GamePlay
	- [x] Le gain d'accés en mémoire
- [x] La partie Composition abordera l'ajout de nouveaux membres directement dans une classe
- [x] Integrer l'atelier "Concevoir un platformer" comme exercice

------------------------
Nouveau Bloc Etape 3 (REformuler a la marge) 
### Etape 3 - Identifier les relations 

**Ce qu'on produit** : le schéma final, où chaque flèche d'héritage est justifiée.

1. Il y a t'il des héritages possibles ? Des fonctionnalités partagés entre certains objets du jeu — sauter, tomber, être poussé, être dessiné, faire du bruit, blesse. 
   Une plateforme mobile est-elle un mur qui bouge, ou un objet qui a un déplacement ?
2. Pour chaque relation de votre schéma, imaginez la phrase « **X est un Y** » en entier. 
   Si cette affirmation sonne faux, remplacez la flèche par une composition (fleche `──◆`),
   Si cette affirmation sonne juste, alors cela peut-être un héritage.
3. Posez vous cette autre question, si je pose un héritage, celui-ci s'avere problématique, bloquant ou contraignant pour le reste du programme ?

-----

## Deuxième passe, le 20.10 — à vérifier

Le deck fait toujours 22 slides, et **aucune slide de contenu ne sort du cadre** (l'audit
signale les cinq slides `title`, qui montent volontairement au-dessus de y = 97 : c'est leur
mise en page, pas un débordement).

### Le pire cas est parti, remplacé par huit demandes réelles

C'était le point central de ta remarque, et il change le widget, le schéma, deux slides et un
exercice. Le modèle est maintenant :

| | Départ | Ce que le designer demande |
|---|---|---|
| **Héritage** | `Personnage` + Guerrier, Magicien, Roublard, Clerc | une classe de plus **à chaque demande**, et le comportement qu'elle ne peut pas hériter est **recopié** |
| **Composition** | six capacités | **rien**, sauf si la demande apporte une capacité qui n'existait pas |

Les huit demandes sont toutes des classes qui existent dans D&D : **Paladin**, Chevalier
occulte, Roublard arcane, Rôdeur, Barde, Moine, Prêtre de guerre, **Druide**. Aucune n'ouvre
« toutes les combinaisons » — chacune est un cas précis, et chacune coûte quand même.

Le compte final, vérifié dans le widget : **13 classes et 8 copies** contre **7 composants et
aucune copie**. Et la ligne qui tranche : *« sorts arcaniques » est écrit 4 fois dans l'arbre,
1 fois en composant.*

Le Druide est volontairement le dernier : c'est **la seule** des huit à coûter quelque chose à
droite, parce que la métamorphose n'existait pas encore. C'est ce qui sépare « une combinaison
nouvelle » de « une capacité nouvelle ».

### Le widget affiche la hiérarchie

`composition_widget.html` est réécrit. À gauche, l'arbre se dessine et se remplit : chaque
demande apparaît sous son parent le plus proche, avec en rouge ce qu'elle recopie. À droite,
la liste des composants et l'assemblage de chaque personnage. Les boutons se cochent un par
un — ou `tout demander` pour la démonstration d'un coup.

### La slide *Le compte* est devenue un graphe

`pcl04_croissance_classes.svg`, généré par `tools/schemas/pcl04_croissance_classes.py`. Trois
tracés : les classes de l'héritage, les copies qu'il accumule, et les composants. Plus aucun
chiffre dans le titre de la slide.

> [!note] La courbe noire part **au-dessus** de la rouge
> À zéro demande, la composition coûte plus cher : six composants écrits avant que quoi que
> ce soit ne soit demandé. C'est volontaire et c'est dit en note de présentation — l'argument
> perd toute force si on cache que la composition se paie d'avance. Le croisement a lieu dès
> la **première** demande.

### L'ECS, trois slides, en fin d'heure

La section *Les données d'un côté* est supprimée, et l'ECS arrive maintenant après *Où placer
le curseur* :

1. **Le même principe, à l'échelle du moteur** — `Personnage = Physique + Rendu + Animation +
   Gameplay`, quatre morceaux écrits par quatre équipes qui ne se parlent pas ;
2. **Le principe de l'ECS** — le schéma `pcl04_ecs.svg`, inchangé ;
3. **Le gain : la donnée suivante est déjà là** — composants contigus, suite continue, ligne
   de cache utilisée entièrement, et rentable seulement à beaucoup d'entités.

### Composition : ça commence par un membre

Nouvelle slide en tête de la section *Assembler*, avant tout composant :

```cpp
class Personnage
{
    Sante sante_;
    Inventaire sac_;
    Deplacement pas_;
};
```

La note de présentation insiste : c'est ce qu'ils font depuis POO-01 sans le nommer. La slide
suivante ne passe à la liste de composants que **parce que les pièces doivent changer en cours
de partie**.

### Snippets en C++

Les deux blocs sont en C++ (`class Personnage`, `paladin.Ajouter<SortsDivins>()`). La slide
*Le modèle composant* garde `GameObject` et `AddComponent` : ce sont des noms d'API Unity
cités, pas du code à compiler.

### L'atelier partagé

[[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer|Concevoir un platformer]]
est créé, rattaché aux trois séances par `seances:`, et la slide *Atelier* y renvoie. Le
détail est dans la fiche de PCL-01, qui le définit.

**L'exercice 1 de la feuille overview a été réécrit** : il demandait les 2^n combinaisons,
il demande maintenant le coût des huit demandes, une par une. Les cinq autres pistes sont
inchangées.

## Ce qui reste ouvert

**1. La source ECS n'existe toujours pas.** `Entity Component System` est un squelette de
160 octets dans `_archive/`. Les trois slides ECS sont du contenu neuf, à relire comme tel.

**2. `solid_principles_in_unity` n'a pas été rouvert.** La note de séance dit que ses quatre
heures partent à PCL-01, APU-01 et APU-09. S'il y avait des schémas de ce support à
transposer ici, ils manquent encore.

**3. La feuille overview et l'atelier coexistent.** Le site rattache maintenant **deux**
feuilles d'exercices à PCL-04 : l'atelier partagé et l'overview de six pistes. C'est ce que tu
as choisi — mais si l'overview n'est jamais rédigé, il faudra décider de le supprimer plutôt
que de le laisser visible aux étudiants.

## Troisième passe, le 20.10 — tes annotations

### Slide *Une capacité devient une pièce*

La phrase de fin affirmait. Elle conditionne maintenant, comme ton annotation le demande :
« **Si** les composants changent en cours de jeu, la suite de membres devient une **liste de
composants dynamiques**. Sinon, les membres de la slide précédente suffisent. »

### L'atelier, revisité

Six coupes et une réécriture dans
[[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer|Concevoir un platformer]] :

| Où | Ce qui change |
|---|---|
| étape 1, question 1 | « sans prononcer le mot classe » et « Visez la quinzaine » retirés |
| étape 1 | la question 4 sur la direction des flèches supprimée — l'étape en compte trois |
| étape 2, le piège | « deux types de plateformes **seulement** », au lieu de « connues à l'écriture » |
| **étape 3** | retitrée *Identifier les relations* et réécrite sur ton bloc |
| le rendu | « à la fin de la troisième séance » retiré |
| le rendu | « papier photographié » retiré des outils acceptés |
| la fin | l'encadré *Pour GP-926 — la suite* supprimé |

L'étape 3 suit ta formulation : on cherche d'abord **s'il y a des héritages possibles**, on
teste chaque relation par la phrase « X est un Y » — faux donne une composition, juste rend
l'héritage *envisageable* — et on pose alors la troisième question, celle qui tranche
vraiment : **cet héritage est-il problématique, bloquant ou contraignant pour la suite ?**
J'ai gardé la quatrième question, celle de la fonctionnalité imprévue : c'est elle qui fait
mesurer ce que l'héritage coûte, et ta reformulation ne la nommait pas.
