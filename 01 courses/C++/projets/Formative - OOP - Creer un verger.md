# Formative — OOP — Créer un verger

> Source : [Google Docs](https://docs.google.com/document/d/1PW9ijKRXD6ksaGkIqJ2eHyzips79RamCeWESa6mgskw/edit)
> Cours associé : [[04 - OOP Advanced]]

## Énoncé

Créer un programme permettant de gérer votre verger.

Il y a dans ce verger 3 types d'arbre : Pommier, Poirier, Cerisier.

| | Nb fruits | Poids des fruits (g) | Hiver | Floraison (printemps) | Pousse / Récolte (été) | Descente (automne) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Cerisier | 45 000 – 60 000 | 5 | Janvier → Mars | Avril | Mai, Juin | Juillet, Décembre |
| Pommier | 600 – 850 | 150 | Janvier → Mars | Avril → Août | Septembre → Novembre | Décembre |
| Poirier | 250 – 350 | 90 | Janvier → Mars | Avril → Septembre | Octobre → Novembre | Décembre |

Chaque arbre passe par différentes phases :

- **La floraison** — aucun fruit n'est disponible, il y a 5 % de chances de perdre la récolte.
- **La pousse** — les fruits poussent progressivement et mûrissent ; chaque mois, entre 3 % et 10 % des fruits disparaissent, dus aux oiseaux et autres parasites.
- **La « descente »** — les fruits pourrissent petit à petit s'ils ne sont pas récoltés. À la fin de cette période, toute la récolte est perdue.
- **L'hiver** (janvier → mars) — l'arbre est en sommeil, rien ne pousse, mais rien de problématique n'arrive.

Lors de la récolte pour sa coopérative, le paysan s'est engagé à fournir 2000 kg de fruits à chaque récolte. Malheureusement, il ne peut se permettre qu'une seule période de récolte, pour laquelle il dispose des moyens d'embaucher des saisonniers.

## Travail demandé

1. Les données fournies sont-elles équilibrées ?
    1. Faites les calculs nécessaires pour déterminer le nombre d'arbres à implanter pour que le verger fonctionne correctement.
    2. Déterminez si une période optimale est possible — **= décision joueur**.
2. Créer un programme permettant les récoltes à l'aide :
    1. d'une hiérarchie de classes permettant la distinction des différents arbres ;
    2. de classes implémentant une méthode permettant :
        1. « la pousse des fruits » (= initier la quantité ; on ignorera les problématiques de saison en estimant les fruits immédiatement disponibles) ;
        2. la récolte, en vérifiant la quantité disponible sur chaque arbre ;
    3. d'un programme principal indiquant au paysan le contenu de chaque récolte.
3. Progressez par étapes :
    1. un type d'arbre sur une année ;
    2. implémenter les 3 types d'arbres ;
    3. implémenter les aléas.

## Données de correction

Variante Poirier :

| | Nb fruits | Poids des fruits (g) | Récolte |
|:-:|:-:|:-:|:-:|
| Poirier | 1600 – 2500 | 90 | Octobre – Novembre |

Quotas par parcelle :

| | Min / Max récolte (kg) | Nb arbres max sur la parcelle | Quota max (monoculture) |
|:-:|:-:|:-:|:-:|
| Cerisier | 225 / 300 | 8 | 8 × 300 − 10 % = 2260 kg |
| Poirier | 144 / 225 | 10 | 10 × 225 − 10 % = 2025 kg |
| Pommier | 90 / 127,5 | 18 | 18 × 127 − 10 % = 2057 kg |
