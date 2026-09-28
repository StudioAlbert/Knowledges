---
title: GPR-CF-BDP-06 - Chaînes de caractères
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Bases de la Programmation
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: false
---

# Chaînes de caractères
<!-- .slide: class="title" -->
## GPR-CF-BDP-06

<small>Du texte, et ce qu'on peut en faire</small>

Note:
**Plan de séance — à développer.** Un titre et une phrase par slide ; widgets et schémas
décrits seulement. Dernière séance du bloc *Bases de la Programmation*.

---

## Objectifs

Savoir construire, mesurer, comparer et découper une `std::string`, et lire proprement ce que tape le joueur.

**Prérequis :** types, tableaux et boucles — [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05]].

---

## Une chaîne n'est pas un nombre

`"42"` occupe deux caractères et ne s'additionne pas ; `42` est une valeur.

---

## Déclarer et concaténer

`std::string` s'écrit comme un type ordinaire, et `operator +` colle deux chaînes bout à bout.

---

## Passer d'un nombre à du texte

`std::to_string(pv)` fabrique la chaîne, `std::stoi(saisie)` tente le retour — et peut échouer.

> [!tip] Schéma
> Un aller-retour en deux flèches entre la case mémoire `int pv = 42` et la chaîne `"42"`,
> avec `to_string` dessus et `stoi` dessous ; sous la flèche du retour, les trois entrées
> qui la font échouer.

---

## Longueur

`size()` compte les caractères, et une chaîne vide se teste avec `empty()`.

---

## Accès : `[]` ou `at()`

`[]` ne vérifie rien et vous laisse lire à côté ; `at()` vérifie et lève une exception.

> [!tip] Widget — `string_index_widget.html`
> La chaîne `"Dungeon Crawler"` affichée case par case avec ses index sous chaque
> caractère. Deux curseurs *début* et *longueur* montrent en direct ce que renvoie
> `substr`, et un champ index compare `[]` et `at()` quand on sort des bornes.

---

## Lire ce que tape le joueur

`std::cin >> pseudo` s'arrête au premier espace ; `std::getline` prend la ligne entière.

---

## Comparer

`==` répond oui ou non ; `compare()` répond avant, après ou identique — utile pour trier.

---

## Chercher : `find` et `npos`

`find` renvoie la position trouvée, ou `std::string::npos` — qui n'est pas `-1`, et qui se teste explicitement.

---

## Découper : `substr`

`substr(debut, longueur)` extrait une tranche ; combiné à `find`, il découpe une ligne en morceaux.

---

## Atelier — 20 min

Écrire la console de triche du jeu : lire une ligne, reconnaître la commande, en extraire l'objet et la quantité.

---

## À retenir

Une chaîne se mesure, se compare, se cherche et se découpe — et tout index vient d'un `find` vérifié, jamais d'un nombre écrit à la main.

---

## Questions ?
