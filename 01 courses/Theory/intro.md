---
title: Theory
type: index
---
# Blocs théoriques

Les notions théoriques qui sous-tendent les cours [[01 courses/Unity/intro|Unity]]
et [[01 courses/C++/intro|C++]] : ce qu'un étudiant doit comprendre indépendamment
d'un moteur ou d'un langage. 8 blocs, 30 cours d'1 h.

Ce cours suit une convention différente des deux autres, volontairement.

| | Unity et C++ | **Theory** |
|---|---|---|
| Un cours est… | une note de `cours/` | une **ligne du tableau** `## Cours` du bloc |
| `cours:` compte… | la somme des `duration_h` | le nombre de lignes d'1 h |
| Le tableau est… | régénéré par `tools/sync_blocs.py` | **tenu à la main** |

C'est le schéma du vault GSDA, où le contenu d'un bloc se décrit dans le bloc
lui-même. Les notes de bloc sont donc copiables telles quelles dans
`_GSDA_Tech_Vault/Bloc/`.

> `tools/sync_blocs.py` **ignore** les blocs dépourvus des marqueurs
> `<!-- cours:auto -->`, donc il ne touche ni aux tableaux ni aux compteurs de
> Theory. Ne pas ajouter ces marqueurs ici.

![[index_blocs.base]]

# Colonne Source

Chaque ligne de cours renvoie, quand il existe, vers le support Unity ou C++ qui
traite déjà la notion. Un `—` signale une notion **sans support écrit** : c'est le
travail de rédaction qui reste à faire, et la raison d'être de ce dossier.

# Dossier cours

`cours/` est vide et le restera tant que les notions vivront comme lignes de
tableau. Il est prévu pour le jour où une notion mérite sa propre note : elle
prendra alors `type: course`, `duration_h` et `bloc`, et remontera dans
[[index_cours.base|l'index des cours]].
