# Exercices — GPR-CF-BDP-06 — Chaînes de caractères

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-06 - Chaînes de caractères|GPR-CF-BDP-06 - Chaînes de caractères]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

Un seul fichier `main.cpp` par exercice, sortie avec `std::println`. Pas de `std::vector` : il arrive plus tard.

## Courts — valider la compréhension

### 1 — La bannière du héros

> [!abstract] Objectifs
> `getline`, `size()`, concaténation

Demander le nom du héros et sa classe, puis afficher une bannière encadrée dont la largeur s'adapte à la longueur du texte.

![[bdp06_ex1_banniere.png]]

> [!tip] Évitez les accents dans vos essais
> `size()` compte des **octets** : `é` en occupe 2, et le cadre se décale d'une case.

### 2 — Barre de vie en texte

> [!abstract] Objectifs
> boucle, `to_string`, construction incrémentale

Afficher les PV sous forme de barre de 10 cases, `[####------] 40/100`, en construisant la chaîne caractère par caractère.

![[bdp06_ex2_barre_de_vie.png]]

### 3 — Pseudo valide ?

> [!abstract] Objectifs
> `empty()`, `size()`, `find`, comparaison à `std::string::npos`

Lire un pseudo avec `getline`, puis tester les règles **dans cet ordre**. On s'arrête à la première règle non respectée.

| # | Règle | Message affiché |
|:-:|---|---|
| 1 | le pseudo n'est pas vide | `Refusé : le pseudo est vide.` |
| 2 | au moins **3** caractères | `Refusé : trop court, 3 caractères minimum.` |
| 3 | au plus **16** caractères | `Refusé : trop long, 16 caractères maximum.` |
| 4 | aucun espace | `Refusé : pas d'espace dans un pseudo.` |
| — | toutes les règles passent | `Bienvenue, Morgane !` |

Tester avec : *(ligne vide)*, `Zo`, `LeChevalierDuNordEst`, `Dark Sasuke`, `Morgane`. Chaque essai doit afficher un message différent.

### 4 — Le tag de joueur

> [!abstract] Objectifs
> `find`, `substr`, `stoi`, index calculés et non devinés

Un tag de joueur s'écrit `[CLAN] Pseudo#numéro`, le clan est facultatif. Extraire le clan, le pseudo et le numéro (en `int`).

| Tag | Clan | Pseudo | Numéro |
|---|---|---|--:|
| `[SAE] Morgane#0427` | `SAE` | `Morgane` | 427 |
| `Aldric#12` | aucun | `Aldric` | 12 |
| `[GENEVE] Zo#9` | `GENEVE` | `Zo` | 9 |

Le même code doit marcher pour les trois : aucune position écrite en dur, tout part de `find('[')`, `find(']')` et `find('#')`.

## Complet — reprendre toute la séance

### 5 — La console de triche

> [!abstract] Objectifs
> tout le vocabulaire de la séance dans un seul programme

Lire une ligne au format `give potion 3`, reconnaître la commande parmi quatre connues, extraire l'objet et la quantité, convertir la quantité, et répondre soit par l'effet appliqué soit par un message d'erreur précis. La boucle tourne jusqu'à `quit`.

## Difficile — se projeter

### 6 — Le formateur de dialogues

> [!abstract] Objectifs
> découper une chaîne avec `find` et `substr`, gérer les cas limites

Un dialogue de PNJ doit tenir dans une boîte de 38 caractères de large : couper le texte entre les mots et jamais au milieu, gérer un mot plus long que la boîte, et paginer par groupes de trois lignes en attendant une touche entre deux pages. Bonus : garder les balises de couleur du type `[rouge]` hors du compte des caractères visibles.
