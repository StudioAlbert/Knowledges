# Partie 1 : Principes

## un arbre de décisions

Toutes les branches sont possibles a tout moment
3 statuts
- Success
- Running
- Failure
Typologie des noeuds
- action (feuille)
- décorateur (1 seul enfant) : Inverseur, etc.
- composite (plein d'enfants) : Sélecteur, Séquence, etc.
# Partie X : Flyweight pattern

Objectif save memory
Intrinstic state vs extrinstic state
Immutability : How to ensure this.
#### Flyweight and immutability

Since the same flyweight object can be used in different contexts, you have to make sure that its state can’t be modified. 
A flyweight should initialize its state just once, via constructor parameters. 
It shouldn’t expose any setters or public fields to other objects.
*What other means in c++ to ensure immutability ?*

Flyweight factory : Storage choice

Contraintes :
- stocker les states sans doublons
- restituer un state existant

Instead, I’d recommend you use an `std::set` for the following reasons:

- its semantic implies an ordering relationship, without duplication
- it has an (asymptotically) efficient insertion.
- it has stable iterators/pointers on insertion: a flyweight can just refer to a pointer to the object contained inside the `std::set`.

Exercice 1 : Refactoriser

Refactoriser un programme gourmand en mémoire consommée : Bcp d'entités, texture, assets gourmands.
*Programme SFML :* 
- *space shooter , asteroides*
- *city builder : tilemap, maisons*

1 Trouver les elements a extraire
2 mesurer l'impact sur la RAM consommée

Quels économies sont possibles sur les NPC ? Faire une projection sur 100, 200. 5000 entités ?
# Ressources

https://refactoring.guru/design-patterns/flyweight
https://en.wikipedia.org/wiki/Flyweight_pattern
https://belanyi.fr/2020/07/16/generic-flyweight-in-c-/

