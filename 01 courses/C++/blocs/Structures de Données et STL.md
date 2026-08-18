---
type: bloc
specialisation: "[[C++]]"
mineur: Games Programming
prerequis:
  - "[[Bases de la Programmation]]"
projet:
  - "[[City Builder]]"
cours: 6
---

# Structures de Données et STL

Choisir le bon conteneur plutôt que le premier connu, puis exploiter la bibliothèque standard : entrées-sorties, flux de chaînes et algorithmes.

## Objectifs

- Choisir entre `array`, `vector`, `list`, `map` et `set` selon l'accès attendu
- Lire et écrire des fichiers, et parser via `stringstream`
- Remplacer une boucle écrite à la main par un algorithme de `<algorithm>`
- Raisonner sur le coût d'une opération avant de l'écrire

## Cours

> `Deeper dive into STD 2/2` est une réimpression à l'identique de la seconde
> moitié de `1/2` : elle porte `duration_h: 0` et ne pèse aucune heure dans le
> total. Projeter `1/2` en entier rend `2/2` redondant.

<!-- cours:auto -->

| # | Cours | Heures | Lien |
| --- | --- | --- | --- |
| 1 | Data Structures | 3 | [[03 - Data Structures (array, vector, map, etc.)]] |
| 2 | Deeper dive into STD 1/2 — file I/O, stringstream | 3 | [[07 - Deeper dive into STD 1-2 - iofile, stringstream, algorithms]] |
| 3 | Deeper dive into STD 2/2 — Algorithms | 0 | [[07 - Deeper dive into STD 2-2 - Algorithms]] |

**Total : 3 cours, 6 h.**

<!-- /cours:auto -->

## Validation

Programme qui charge un fichier de données, l'indexe dans le bon conteneur et l'interroge.

## Liens

- Spécialisation : [[C++]]
- Prérequis : [[Bases de la Programmation]]
- Bloc suivant : [[Structure de Programme et Bonnes Pratiques]]
- Index des cours : [[index_cours.base|Index]]
