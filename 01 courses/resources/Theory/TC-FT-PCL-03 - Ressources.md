---
seances: [TC-FT-PCL-03]
---
# Ressources — les patterns

## S'entraîner

[Quel pattern ?](00 widgets/_widgets/patterns_quizz_widget.html) — sept situations, sept
réponses, et l'une d'elles est qu'aucun pattern n'est nécessaire. La correction donne le
problème posé, la manière dont le pattern y répond, et une métaphore.

## La référence, en français

[refactoring.guru](https://refactoring.guru/fr/design-patterns/what-is-pattern) est la
meilleure entrée francophone. Cinq pages suffisent, dans cet ordre :

1. [Qu'est-ce qu'un patron de conception ?](https://refactoring.guru/fr/design-patterns/what-is-pattern) —
   la définition, et surtout ce qu'un patron **n'est pas** : ni un algorithme, ni du code à copier.
2. [Classification](https://refactoring.guru/fr/design-patterns/classification) — les trois
   familles, création, structure et comportement. C'est la carte de la séance.
3. [Histoire](https://refactoring.guru/fr/design-patterns/history) — d'où viennent les
   vingt-trois patrons de 1994, et pourquoi ils parlent de C++ et de Smalltalk.
4. [Pourquoi les apprendre ?](https://refactoring.guru/fr/design-patterns/why-learn-patterns) —
   l'argument du vocabulaire commun, qui est le vrai bénéfice.
5. [Critiques](https://refactoring.guru/fr/design-patterns/criticism) — à lire **avec** les
   quatre autres, pas après.

> [!warning] La critique à connaître
> Deux arguments y sont développés, et les deux sont justes.
>
> **Des rustines pour des langages limités** (l'argument de Paul Graham) : un patron signale
> souvent ce qui manque au langage. `Strategy` se réduit à une lambda dans la plupart des
> langages modernes, et `Iterator` est devenu une boucle `for`.
>
> **L'usage injustifié** : fraîchement appris, un patron se met partout. *Si tout ce que vous
> avez est un marteau, tout ressemble à un clou.*
>
> Ça ne disqualifie pas les six de la séance : `State`, `Component` et `Object Pool` n'ont
> aucun équivalent en mot-clé.

## À la source

Les deux textes derrière la page *Critiques*, à lire en anglais. Ce sont **deux auteurs
différents**, et on les confond souvent.

- [Peter Norvig — *Design Patterns in Dynamic Languages*](https://norvig.com/design-patterns/)
  (présenté en 1996, en ligne depuis 1998). C'est de lui que vient le compte : **16 des 23**
  patrons sont « invisibles ou plus simples » dans un langage plus expressif. Les planches
  sont courtes et se lisent d'un trait.
- [Paul Graham — *Revenge of the Nerds*](https://www.paulgraham.com/icad.html) (2002). Son
  argument est plus radical : voir un patron se répéter dans son **propre** code est le signe
  qu'on fait à la main ce qu'une abstraction plus forte ferait toute seule. C'est lui qui
  cite Norvig, en note de bas de page.

## Ne pas en mettre partout

- [GeeksforGeeks — *YAGNI Principle*](https://www.geeksforgeeks.org/software-engineering/what-is-yagni-principle-you-arent-gonna-need-it/) :
  les quatre coûts d'une fonctionnalité écrite trop tôt — construction, retard, portage,
  réparation — et la nuance qui compte : YAGNI **retarde** l'implémentation, il n'excuse pas
  une mauvaise conception.

## Côté moteur

- [Unity — *Améliorez votre programmation avec des modèles de programmation de jeu*](https://unity.com/fr/resources/level-up-your-code-with-game-programming-patterns) :
  l'e-book gratuit de Unity, en français, qui reprend les mêmes patrons avec du C# et des
  exemples de jeu. Le plus proche de ce qu'on fait en atelier.

## Les six, en détail

Chacun est traité dans une séance du cursus — les fiches de refactoring.guru servent de
rappel, pas de cours.

| Pattern | Où il est traité |
|---|---|
| Observer | [[01 courses/slides/Unity/GPR-UN-APU-05 - Observer, prévenir sans connaître\|APU-05]] |
| State | [[01 courses/slides/Unity/GPR-UN-APU-09 - Observer, State et composition\|APU-09]] |
| Strategy | [[01 courses/slides/Unity/GPR-UN-APU-08 - Strategy pattern en Unity\|APU-08]] |
| Component | [[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage\|PCL-04]] |
| Command, Object Pool | cités ici, pas de séance dédiée |
