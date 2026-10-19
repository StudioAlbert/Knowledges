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
s'arrête — et ce n'est pas une question de goût : c'est une question de compte.

---

## Objectifs

À la fin de la séance, vous savez :

- reconnaître une **hiérarchie qui ne tient plus**
- la remplacer par des **composants**
- dire ce que la séparation **données / traitements** permet
- nommer le principe de l'**ECS**

**Prérequis :** [[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme|GPR-CF-POO-06]].

---

# L'arbre qui ne pousse plus
<!-- .slide: class="title" -->

---

## Au début, ça marche

```
Ennemi
├── EnnemiTerrestre
│   ├── Gobelin
│   └── Golem
└── EnnemiVolant
    ├── Chauve-souris
    └── Dragon
```

Une hiérarchie décrit très bien le monde qu'on imaginait au départ.

---

## Le cas qui ne rentre pas

Le game designer demande un **gobelin volant qui tire**.

- il n'est ni `EnnemiTerrestre`, ni tout à fait `EnnemiVolant`
- « tirer » n'existe nulle part dans l'arbre
- chaque réponse — dupliquer, remonter la méthode, hériter deux fois — coûte

L'arbre a été dessiné avant de connaître le jeu. Le jeu a changé.

Note:
Les trois réponses, à faire proposer : dupliquer le code de vol dans Gobelin ;
remonter `Voler()` dans `Ennemi`, et tous les ennemis savent voler ; héritage
multiple, et on retombe sur le diamant de POO-06. Aucune n'est bonne.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/composition_widget.html" data-background-interactive -->

Note:
Partir à deux capacités : trois classes, ça passe. Ajouter la troisième, puis la
quatrième — 15 classes — et laisser la salle réagir. Le chiffre de droite,
lui, ne bouge que de un. C'est tout l'argument de la séance, et il est
arithmétique, pas esthétique.

---

## Le compte

Pour couvrir **toutes** les combinaisons de `n` capacités :

<p class="formule">héritage : 2<sup>n</sup> − 1 classes &nbsp;&nbsp;·&nbsp;&nbsp; composition : n composants</p>

- 3 capacités → **7** classes, ou 3 composants
- 6 capacités → **63** classes, ou 6 composants
- une capacité de plus **double** la première colonne

---

# Assembler
<!-- .slide: class="title" -->

---

## Une capacité devient une pièce

```csharp
// au lieu d'une classe par combinaison
var gobelinVolantTireur = new Entite();
gobelinVolantTireur.Ajouter(new Vol());
gobelinVolantTireur.Ajouter(new Tir());
gobelinVolantTireur.Ajouter(new Vie(30));
```

On n'écrit plus un **rang dans un arbre**, on écrit une **liste**.

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
composants. La troisième mène à l'ECS.

---

# Les données d'un côté
<!-- .slide: class="title" -->

---

## Orientation données

Séparer ce que l'objet **est** de ce qu'on lui **fait** :

- les **données** : des champs, sans méthode, rangés ensemble
- les **traitements** : des fonctions qui prennent ces données en lot
- le même traitement vaut pour **mille** objets, pas pour un

On arrête de demander à chaque objet de se mettre à jour lui-même.

---

## Le principe de l'ECS
<!-- .slide: class="schema" -->

Des entités sans comportement, des composants sans logique, des systèmes qui balaient.

![[pcl04_ecs.svg]]

Note:
Insister sur le tableau sans trou : une entité qui n'a pas le composant n'occupe
pas de case. Le système ne teste donc jamais « est-ce que celui-là bouge ? » — il
parcourt une suite de données toutes utiles. C'est l'exercice 6.

---

## Ce que l'ECS achète, et à quel prix

- **achète** : des parcours rapides, et des lots qu'on peut paralléliser
- **coûte** : du code moins direct, et un débogage moins évident
- il devient rentable à **beaucoup d'entités**, pas à douze

Unity DOTS, Bevy, Overwatch : le même principe, à des échelles différentes.

---

# Où placer le curseur
<!-- .slide: class="title" -->

---

## Quand l'héritage reste juste

- une relation **« est un »** vraie, stable, et peu profonde
- un parent **abstrait** qui fixe un contrat — l'`Arme` de POO-06
- deux ou trois classes filles qu'on ne combinera jamais

L'héritage n'est pas une faute. C'est un outil à **un seul axe**.

---

## Le test, en une question

> Est-ce que mes catégories se **combinent** ?

- **non** → l'héritage classe très bien
- **oui** → chaque combinaison deviendra une classe, et il y en a 2<sup>n</sup>

« Volant » et « tireur » se combinent. « Chien » et « chat », non.

---

## Ce que coûte la composition

- plus de petits objets, et plus d'indirections
- un **ordre d'exécution** à décider explicitement
- un bug se cherche dans l'assemblage, pas dans une classe

Ce n'est pas gratuit : c'est seulement moins cher que 63 classes.

---

## Atelier — 20 min

Reprendre la hiérarchie d'ennemis de votre projet.

1. compter les classes qu'exigerait **une capacité de plus**
2. lister les capacités qui se **combinent** vraiment
3. refaire l'arbre en composants, sur papier
4. dire qui **coordonne**, maintenant que personne ne le fait d'office

---

## À retenir

- l'héritage **classe**, la composition **assemble**
- dès que les capacités se combinent, le compte tranche : 2<sup>n</sup> contre n
- l'orientation données sépare ce que l'objet **est** de ce qu'on lui **fait**
- l'ECS pousse le principe jusqu'à la **disposition mémoire**

---

# Questions ?
<!-- .slide: class="title" -->

### Fin du bloc

<small>Couplage et cohésion, SOLID, taxonomie des patterns, et ce dernier arbitrage : les quatre séances se répondent.</small>
