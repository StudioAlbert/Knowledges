---
status: Ready
manual_order: 3
slides:
  - "[[01 courses/slides/C++/GPR-CF-POO-01 - Structures|Slides POO-01]]"
exercices:
  - "[[01 courses/exercises/C++/GPR-CF-POO-01 - Structures|Exos POO-01]]"
url_test: http://localhost:61638/cpp/gpr-cf-poo-01/
---
- [x] Mettre en page ![[{51FD8CFD-4056-4472-BBD2-B1160830090E}.png]]![[{2FC6DF67-646D-4C24-A6D6-668684A9828E}.png]]
- 
 - [x] ne pas spécifier le nom de la "variable" , gobelin : Ennemi => Ennemi 
![[{2D3717A4-60AC-43D1-A43F-33B08C77A8A3}.png]]
- [x] Ajouter ou compléter contenu de  01 courses/slides/C++/GPR-CF-POO-01 - Structures avec les éléments de 01 courses/lectures/C++/01.03 - Basics OOP
	- [x] 01 courses/slides/C++/GPR-CF-POO-01 - Structures est le deck final
	- [x] Recopier snippets dans les slides appropriés
	- [x] Ajouter slides eventuels pour les concepts manquants
	- [x] ne pas dépasser le contenu de la compariason entre classes et structs

## Traité le 05.10 — à vérifier (séance du 07.10, 09:30)

- **Deck complété** à partir de `01.03 - Basics OOP` : 20 slides, du besoin (six variables pour un ennemi) jusqu'à la comparaison `struct` / `class`, rien au-delà (ni méthodes, ni `.h` / `.cpp`, ni constructeurs : POO-02 à 04).
- **Snippets repris** de 01.03 et traduits (`Enemy` → `Ennemi`, `std::println`) : déclaration, initialisation (liste, champ par champ), échange de coups joueur / alien, `struct` vs `class`, accès privé refusé.
- **Slides ajoutées** pour les concepts du plan sans contenu : *Trois façons d'initialiser*, *Une structure dans une structure* (`Vector2` / `Transform`), *Passer à une fonction* (copie, `&`, `const &`), *Un tableau de structures*, *Visibilité*, *Le compilateur vérifie*.
- **Schémas** : `poo01_regrouper.svg` (six variables → une boîte `Ennemi`) et `poo01_declaration_instances.svg` (le plan et deux gobelins) — ce dernier remplace le widget `struct_memoire_widget` proposé dans le plan, non construit.
- **Corrigé au passage** : 01.03 annonçait l'initialisation `.champ = valeur` en C++17 ; c'est du **C++20**.
- Tout le code compile et tourne (GCC 14, `-Wall -Wextra`) ; les messages d'erreur cités sont ceux de GCC 14.
- Le deck reste en `publish: false`.

> [!note] Thème : blocs de code limités à ~13 lignes
> `sae_styles.css` plafonne `pre code` à 200 px : au-delà, le bloc défile et la fin est cachée. Tous les blocs de POO-01 et BDP-05 ont été ramenés à 13 lignes au plus.

## Traité le 05.10 — complément

- **`poo01_regrouper.svg`** : le bandeau de la boîte annonçait `gobelin : Ennemi`, il
  n'annonce plus que **`Ennemi`** — le schéma montre le *type*, pas une variable. La légende
  suit : « un seul type, six champs qui voyagent ensemble » au lieu de « un nom, une
  variable, six valeurs ».
- `poo01_declaration_instances.svg` garde `Ennemi gobelinA` / `Ennemi gobelinB` : c'est le
  panneau des **instances**, où nommer la variable est justement le propos.

## Traité le 06.10 — la règle de mise en page

Le titre qui mordait le cadre n'était pas propre à cette slide : **reveal centre chaque
section verticalement** en lui posant un `top` calculé sur sa hauteur. Dès que le contenu
dépasse la hauteur du cadre, tout remonte et le titre finit sur la bande noire du fond.

**La règle est posée dans `00 templates/css/sae_styles.css`** :

- le padding vertical des sections matérialise désormais le cadre — **104 px** en haut
  (97 + 7 de garde), **98 px** en bas (720 − 622) ;
- la section est figée sur toute la slide (`top: 0`, `height: 720px`) et son contenu est
  centré **à l'intérieur** de ce padding : un contenu court reste centré comme avant, un
  contenu haut s'arrête net au bord du cadre au lieu de le franchir ;
- sur une slide `schema`, l'image est le seul enfant qui se **réduit** : elle prend ce qui
  reste sous le titre et son chapeau, et pas un pixel de plus.

**Les 713 slides des 29 decks ont été passées en revue**, automatiquement, en mesurant
chaque élément de chaque slide contre le cadre. 11 slides débordaient encore après la
règle, toutes par excès de contenu — elles sont corrigées (voir le compte rendu de la
session). Le compte est maintenant de **0 slide hors cadre**.
