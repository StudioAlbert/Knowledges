---
type: bloc
specialisation: "[[Theory]]"
mineur: Games Programming
prerequis: []
projet: []
cours: 4
---

# Représentation des Nombres et Logique Binaire

Ce que la machine manipule réellement sous les `int` et les `float` : bases, encodages, et l'algèbre qui gouverne les opérateurs bit à bit.

## Objectifs

- Convertir entre binaire, octal, hexadécimal et décimal, et savoir pourquoi
- Expliquer le complément à deux et prévoir un dépassement d'entier
- Décrire la structure d'un flottant IEEE 754 et les pièges de comparaison qui en découlent
- Poser un masque et un décalage à partir d'une table de vérité

## Cours

| # | Cours (1h) | Contenu | Source |
| --- | --- | --- | --- |
| 1 | Bases et changements de base | Poids des chiffres, binaire, octal, hexadécimal, conversions dans les deux sens, notation en C++ | [[02 - Introduction to logic - non decimal arithmetic]] |
| 2 | Entiers signés et dépassements | Complément à deux, plages représentables, dépassement signé et non signé, types de taille fixe | [[02 - Introduction to logic - non decimal arithmetic]] |
| 3 | Flottants IEEE 754 | Signe, exposant, mantisse, précision et epsilon, valeurs spéciales, pourquoi `==` ment sur les flottants | — |
| 4 | Algèbre de Boole et opérations bit à bit | Tables de vérité, ET/OU/NON/XOR, masques, décalages, drapeaux compactés | [[Truth table]] |

## Validation

Exercice écrit : conversions, prévision d'un dépassement, et lecture d'un flottant donné en hexadécimal.

## Liens

- Spécialisation : [[Theory]]
- Index des blocs : [[index_blocs.base|Index]]
