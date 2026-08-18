# Exercices — 04 — OOP

> Source : [Google Docs](https://docs.google.com/document/d/1cex2WzfjOfhlf99RmHsrJGj5uR22dm_gy48aoEJWG24/edit)
> Cours associé : [[04 - OOP Advanced]]

## OOP

### Exercice 1 — Car

Créer une classe `Car` avec les membres suivants :

- marque
- modèle
- année

Créer un programme :

- déclarant une Ford Mustang de 1966 et une Fiat Panda de 1982
- affichant dans la console les informations des voitures

Remplacer les attributs publics par des attributs privés.

Créer les accesseurs donnant accès en lecture et en écriture aux attributs.

### Exercice 2 — Point dans un plan

Réaliser une classe `point` permettant de manipuler un point d'un plan. On prévoira :

- un point défini par ses coordonnées `x` et `y` (des membres privés)
- un constructeur (vous pouvez également implémenter deux types de constructeur : par défaut, avec paramètres)
- une méthode **déplace** effectuant une translation définie par ses deux arguments `dx` et `dy` (`double`)
- une méthode **affiche** se contentant d'afficher dans la console les coordonnées cartésiennes du point
- une fonction membre **saisir** se contentant de saisir depuis la console les coordonnées cartésiennes du point
- une méthode **distance** calculant la distance entre deux points ([Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance))
- une fonction membre **milieu** donnant le milieu d'un segment ([milieu d'un segment](https://fr.wikipedia.org/wiki/Milieu_d%27un_segment))

On écrira séparément :

- un fichier d'en-tête pour la définition de la classe
- un fichier source constituant l'implémentation de la classe
- un petit programme d'essai (`main`) gérant la classe `point`

### Exercice 3 — Collection d'objets

En utilisant une classe comportant un membre de type entier :

- grâce aux boucles `for`, créer une collection d'objets et stocker dans un attribut de la classe un nombre aléatoire entier
- créer une fonction permettant d'afficher la liste complète des nombres stockés dans les objets
- supprimer tous les objets dont la valeur stockée est multiple de 3

### Exercice 4 — Le magasin de bonbons

**Partie 1**

Créer un programme permettant de gérer un magasin de bonbons.

- Écrire une classe magasin de bonbons avec les membres suivants :
    - type de bonbons avec une `enum` : Boule de mammouth, Tagada, LolliPops
    - quantité de bonbons à travers une `std::map` (clé : type de bonbons, valeur : entier permettant de compter le stock)
- Le constructeur de la classe initiera la quantité pour chaque type de bonbons.
- Écrire les méthodes permettant de :
    - refaire ou initier les stocks
    - « acheter des bonbons » : demande au joueur quel type il veut et combien. Celle-ci doit vérifier la quantité disponible et la somme restante au joueur.

**Partie 2**

Créer une classe `wallet` permettant de gérer l'argent de l'acheteur.

### Exercice 5 — Machine à café

Créer un programme simulant la machine à café de l'école.

La machine sert 3 produits : Expresso, Café long, Cappuccino. Elle dispose d'un stock de 10 g de grains de café. Chaque produit consomme une certaine quantité de ces grains : Expresso 1 g, Café long 2 g, Cappuccino 1,5 g.

**Partie 1**

- Créer une classe permettant d'utiliser cette machine.
    - Créer un menu demandant avec les touches du clavier quel produit servir.
    - La classe affiche :
        - un message disant que le service s'est correctement passé
        - ou bien un message proposant de remplir la machine avec une touche (ex. `[R]`) si celle-ci est vide
- Comment est constituée la classe (méthodes, membres) ?

**Partie 2**

- Ajouter un produit : l'eau chaude, ne consommant aucun grain.
- Ajouter une classe `Wallet` pour faire payer au consommateur le prix des produits, fixer les prix.
- Ajouter un message d'attente et une barre de progression : chaque produit n'est pas instantané et doit maintenant prendre un certain temps.

## OOP : surcharge d'opérateur

### Exercice 6 — Point et opérateurs

Créer une classe `Point` :

- 2 membres `float` `X` et `Y` pour les coordonnées du point
- une méthode pour afficher dans la console les coordonnées du point

En utilisant la classe `Point`, créer des surcharges d'opérateurs :

- opérateur `+` : `pointA + pointB` donne le milieu du segment AB ([milieu d'un segment](https://fr.wikipedia.org/wiki/Milieu_d%27un_segment))
- opérateurs `>` et `<` : les points sont comparés selon leur distance à l'origine `(0,0)`. `pointA` est supérieur à `pointB` si la distance de `pointA` par rapport à l'origine est supérieure à celle de `pointB` ([Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)).

## OOP : inheritance

### Exercice 7 — Hiérarchie de classes

Représenter à l'aide d'une hiérarchie de classes le schéma suivant.

Où placeriez-vous les attributs suivants ?

- nombre de Roues
- puissance du Moteur
- numéro de Plaque d'immatriculation
- nom du Pilote
- couleur du Casque

### Exercice 8 — Multiple inheritance

Créer la classe `Race` et ses membres.

Créer 2 classes héritant de `Race` : `Human` et `Orc`, avec leurs méthodes et membres spécifiques.

Créer dans le `main` 2 héros : un héros `Human`, un héros `Orc`.

Créer la classe `CombatClass` et ses membres.

Créer 2 classes héritant de `CombatClass` : `Archer` et `Warrior`. Implémenter leurs spécificités.

Créer une classe `BlackOrc`, à la fois `Orc` et `Warrior`. Déclarer un héros Grimgor, un `BlackOrc`.

Créer une classe `HumanArcher`, à la fois `Human` et `Archer`. Déclarer RobinHood, un `HumanArcher`.

Comment étendre pour créer une classe `ElfMagicien` ?

### Exercice 9 — Solar system

**Partie 1**

Créer une classe `AstroObject`, représentant un corps céleste du système solaire :

- celui-ci possède plusieurs caractéristiques :
    - nom (chaîne)
    - diamètre, masse (numériques, expliciter les unités en commentaires), distance au soleil
    - composition de l'atmosphère. Créer une `enum` listant les éléments possibles (collection d'`enum`s).
- créer une méthode permettant d'afficher dans la console une présentation de ses caractéristiques ; celle-ci doit tenir compte du fait que certaines planètes n'ont pas d'atmosphère
- utiliser les capacités du constructeur pour créer depuis la fonction `main` une collection de planètes
- les caractéristiques ne doivent pas être accessibles depuis le `main`

Pour vous aider : [Système solaire (Wikipédia)](https://fr.wikipedia.org/wiki/Syst%C3%A8me_solaire)

**Partie 2 (facultative)**

En utilisant le travail de l'exercice précédent, créer deux classes `Planet` et `Moon`.

- La classe `Planet` hérite de `AstroObject` et ajoute une collection `moons` de `AstroObject` pour lister les différentes lunes (les plus connues) de chacune des planètes.
- La classe `Moon` hérite de `AstroObject`.

**Partie 3**

En utilisant le travail précédent, créer une classe `Ship` permettant de voyager dans le système solaire en tenant compte des distances entre les planètes.

Cette classe permettra, avec les touches du clavier, d'afficher les différents corps célestes et leurs caractéristiques, et s'appuiera sur les classes créées dans le reste de l'exercice.
