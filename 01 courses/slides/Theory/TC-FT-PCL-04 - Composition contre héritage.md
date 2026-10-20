---
title: TC-FT-PCL-04 - Composition contre héritage
type: slides
subject: Theory
duration_h: 1
bloc_gsda: Principes de Conception Logicielle
specialisation: Fondamentaux Théoriques
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
---

# Composition contre héritage
<!-- .slide: class="title" -->

### Assembler plutôt que classer

<small>TC-FT-PCL-04 · Principes de Conception Logicielle</small>

Note:
POO-06 a donné l'héritage et montré ce qu'il règle. Cette séance montre où il
s'arrête — et pas sur un cas d'école : sur des demandes que le game designer
pose vraiment, une par une.

---

## Objectifs

À la fin de la séance, vous savez :

- reconnaître une **hiérarchie qui ne tient plus**
- composer, d'abord **dans la classe**, puis par composants
- dire ce que la séparation **données / traitements** permet
- nommer le principe de l'**ECS**

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme|GPR-CF-POO-06]].

---

# L'arbre qui ne pousse plus
<!-- .slide: class="title" -->

---

## Au début, ça marche

```text
Personnage
├── Guerrier     arme au contact
├── Magicien     sorts arcaniques
├── Roublard     furtivité, tir à distance
└── Clerc        sorts divins, soin
```

Quatre classes, quatre rôles nets. L'arbre décrit très bien le jeu qu'on
imaginait au départ.

---

## Le cas qui ne rentre pas

Le designer demande un **Paladin** : il se bat au contact **et** lance des sorts divins.

- il hérite de `Guerrier`, mais les sorts divins sont chez `Clerc`
- hériter des deux, c'est le **diamant** de POO-06
- recopier les sorts divins, c'est le **même code à deux endroits**

Et il ne s'arrêtera pas là : rôdeur, barde, moine, druide.

Note:
Faire proposer les trois réponses avant de les montrer. Aucune n'est bonne, et
c'est **la troisième qu'on choisit en vrai** — on recopie, parce que c'est la
seule qui compile tout de suite. Le coût arrive six demandes plus tard.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/composition_widget.html" data-background-interactive -->

Note:
Partir du Paladin seul : une classe de plus, une copie, personne ne s'inquiète.
Ajouter les demandes une par une et laisser la salle regarder l'arbre se
remplir de rouge. Finir sur le Druide : c'est **la seule** des huit qui coûte
quelque chose à droite, parce que la métamorphose n'existait pas encore. Toutes
les autres ne demandent qu'un nouveau mélange.

---

## Ce que coûte chaque demande
<!-- .slide: class="schema" -->

Huit demandes réelles, posées l'une après l'autre sur les quatre classes de départ.

![[pcl04_croissance_classes.svg]]

Note:
La courbe noire part **au-dessus** de la rouge : à zéro demande, la composition
coûte plus cher. C'est honnête, et c'est important — elle se paie d'avance. Le
croisement a lieu dès la première demande.

---

# Assembler
<!-- .slide: class="title" -->

---

## Ça commence dans la classe

```cpp
class Personnage
{
    Sante sante_;              // « a une » santé
    Inventaire sac_;           // « a un » sac
    Deplacement pas_;          // « a un » déplacement
};
```

Composer, c'est d'abord **ajouter un membre**. Ni framework, ni moteur : une
classe qui contient ses pièces.

Note:
Point à ne pas sauter : la composition ne commence pas à Unity. `Sante`,
`Inventaire` et `Deplacement` sont trois classes écrites **une fois** et
réutilisées partout — c'est ce qu'ils font déjà depuis POO-01 sans le nommer.
Ajouter une capacité au personnage, ici, c'est ajouter une ligne, et aucune
hiérarchie n'est touchée.

---

## Une capacité devient une pièce

```cpp
// au lieu d'une classe par croisement demandé
Entite paladin;
paladin.Ajouter<ArmeAuContact>();
paladin.Ajouter<SortsDivins>();
paladin.Ajouter<Sante>(30);
```

Quand les pièces doivent changer **en cours de partie**, le membre fixe devient
une **liste**.

---

## Le modèle composant

Unity est construit là-dessus : un `GameObject` n'est rien d'autre qu'un nom, une
transformée, et une **liste de composants**.

- `AddComponent` à l'exécution, pas à la compilation
- aucun composant ne connaît les autres
- l'inspecteur **est** la liste

C'est pour ça qu'on peut fabriquer un ennemi sans écrire une ligne.

---

## Ce que ça change à l'écriture

- un composant fait **une** chose, et ignore qui l'entoure
- ajouter une capacité n'ouvre **aucun** fichier existant
- l'objet n'est plus décrit par son type mais par ses **données**

Le prix : il faut décider **qui coordonne**, puisque plus personne ne le fait
d'office.

Note:
C'est la question que l'exercice 3 pose. Trois réponses tenables : un composant
chef d'orchestre, des événements, ou un système extérieur qui lit les deux
composants. La troisième mène à l'ECS, qu'on voit en fin d'heure.

---

# Où placer le curseur
<!-- .slide: class="title" -->

---

## Quand l'héritage reste juste

- une relation **« est un »** vraie, stable, et peu profonde
- un parent **abstrait** qui fixe un contrat — l'`Arme` de POO-06
- deux ou trois classes filles qu'on ne croisera jamais

L'héritage n'est pas une faute. C'est un outil à **un seul axe**.

---

## Le test, en une question

> Est-ce que mes catégories se **croisent** ?

- **non** → l'héritage les classe très bien
- **oui** → chaque croisement demandé deviendra une classe de plus

« Guerrier » et « magicien » se croisent : D&D en vit. « Chien » et « chat », non.

---

## Ce que coûte la composition

- plus de petits objets, et plus d'indirections
- un **ordre d'exécution** à décider explicitement
- un bug se cherche dans l'assemblage, pas dans une classe

Elle se paie d'avance : six composants avant la première demande. Et c'est moins
cher que treize classes et huit copies.

---

## Le même principe, à l'échelle du moteur

Unity l'a poussé jusqu'au bout : un personnage n'est pas une classe `Personnage`.

<p class="formule">Personnage = Physique + Rendu + Animation + Gameplay</p>

- quatre morceaux écrits par quatre équipes qui ne se parlent pas
- aucun ne connaît les trois autres
- on en retire un, le reste tourne encore

---

## Le principe de l'ECS
<!-- .slide: class="schema" -->

Des entités sans comportement, des composants sans logique, des systèmes qui balaient.

![[pcl04_ecs.svg]]

Note:
Insister sur le tableau sans trou : une entité qui n'a pas le composant n'occupe
pas de case. Le système ne teste donc jamais « est-ce que celui-là bouge ? » — il
parcourt une suite de données toutes utiles.

---

## Le gain : la donnée suivante est déjà là

- les composants d'un même type sont **côte à côte** en mémoire
- un système lit une suite **continue**, pas un objet par-ci par-là
- le processeur charge une ligne de cache et s'en sert **entièrement**
- rentable à **beaucoup** d'entités, pas à douze

Unity DOTS, Bevy, Overwatch : le même principe, à des échelles différentes.

---

## Atelier — 20 min

**Concevoir un platformer** — celui-là même que vous écrirez ensuite en SFML.

1. lister les **fonctionnalités** du jeu, sans prononcer le mot « classe »
2. en déduire les **classes**, et ce que chacune sait faire
3. tracer les **relations** : qui contient quoi, qui hérite de quoi
4. rendre **un schéma**, où chaque flèche d'héritage est justifiée par un « est un »

Énoncé : [[01 courses/exercises/Theory/TC-FT-PCL - Concevoir un platformer|Concevoir un platformer]].

---

## À retenir

- l'héritage **classe**, la composition **assemble**
- composer commence par **un membre de plus** dans une classe
- chaque croisement demandé coûte une classe à l'héritage, **rien** à la composition
- l'ECS pousse le principe jusqu'à la **disposition mémoire**

---

# Questions ?
<!-- .slide: class="title" -->

### Fin du bloc

<small>Couplage et cohésion, SOLID, taxonomie des patterns, et ce dernier arbitrage : les quatre séances se répondent.</small>
