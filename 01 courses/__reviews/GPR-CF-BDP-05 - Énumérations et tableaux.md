---
status: Ready
manual_order: 2.625
slides:
  - "[[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|Slides BDP-05]]"
exercices:
  - "[[01 courses/exercises/C++/GPR-CF-BDP-05 - Énumérations|Exos BDP-05 — Énumérations]]"
  - "[[01 courses/exercises/C++/GPR-CF-BDP-05 - Tableaux|Exos BDP-05 — Tableaux]]"
  - "[[01 courses/exercises/C++/GPR-CF-BDP-05 - Bilan formatif, le morpion|Exos BDP-05 — Bilan formatif]]"
url_test: http://localhost:61638/cpp/gpr-cf-bdp-05/
---
- [x] Mettre en page ![[{51DA48AF-01DE-4896-8004-EF54222085F8}.png]]
- [x] `enum` simple ou `enum class` ? => proposer snippet avec problemes, pousser a 2 slides si besoin
- [x] Exercices
	- [x] abandonner cris d'animaux
	- [x] creer 2 fichiers d'exercice (enums/tableaux) pour une meilleure compréhension pour les eleves + 1 fichier formative
	- [x] abandonner table de multiplication
- [x] separer exercices enum / exercices tableaux
- [x] Clean slides from old css style to new css style
- [x] Reformuler exercices
- [x] Renumeroter
- [x] Proposer un exercice sur l'enum **Restaurant** des slides
- [x] Rediger exercice Formative/Bilan de la seance TicTacToe

Partie Array 
- [x] Compléter ## Multiple declarations styles
- [x] Completer Multiple reading loop
	- [x] Avertir sur les erreurs de depassement d'index
- [x] Ajouter slides, pas d'ajout, pas de suppression
	- [x] ajouter slide pour savoir si une valeur existe
- [x] Ajouter slides sur les tableaux multidimensionnels, declaration, parcours
	- [x] ajouter slide "anecdote" sur une comparaison tableau multi (2D) et tableau 1D avec calcul d'indice permettant de parcourir. Prendre exemple d'une grille de morpion
- [x] Proposer exercice sur le theme du gaming pour les tableaux multi dimensionnels

## Traité le 05.10 — à vérifier (séance du 07.10, 11:10)

**Slides** (29, `publish: false`)

- **Ancien style retiré** : plus de `data-background="00 images/01_slide_fond_…jpg"` ; sections en `class="title"`, slides schéma en `class="schema"`. Textes passés en français, slides doublons fusionnées (*What is an enum?* ×2).
- **Déclarations** : `a[N]` (indéterminé), `= {…}`, taille déduite, `{}` (zéros), initialisation partielle.
- **Parcours** : avec index, `for` sans index ; à l'envers en note.
- **Dépassement** : schéma `bdp05_index.svg` (*L'index commence à zéro*) + slide *Attention au dépassement* avec la sortie réelle d'un `<=` de trop (`vies[3] = 344280576`), `-fsanitize=address` en note.
- **Ajoutées** : *Taille fixe : pas d'ajout, pas de suppression*, *Savoir si une valeur existe*, *Deux dimensions : déclarer*, *Deux dimensions : parcourir*.
- **Anecdote 2D / 1D** : schéma `bdp05_grille_1d.svg` (le morpion en `grille[3][3]` et en `grille[9]`, `index = ligne × 3 + colonne`) + *Le morpion en une dimension* en code.
- Snippets ajoutés aussi sur les slides du plan restées sans code (*Indexer par une énumération*, *Passer un tableau à une fonction*, `std::array` / `at()`) ; la phrase « `degats[Arme::Epee]` se lit tout seul » était fausse avec une `enum class` (le `static_cast` est obligatoire) : corrigée.
- Les deux widgets proposés dans le plan (`tableau_index_widget`, `grille_memoire_widget`) sont remplacés par ces deux schémas.

**Exercices** (8, renumérotés)

- **Séparés** : *Énumérations* (1 – 3), *Tableaux* (4 – 6), *Complet — 2D* (7), *Bilan formatif* (8). Tous reformulés en français, étapes numérotées, cadre *Objectifs*.
- **3 — Au restaurant** : l'`enum class Aliment` des slides, prix par `switch`, menu en boucle, `static_cast`, addition.
- **7 — La carte du donjon** (2D, jeu) : `Tuile carte[6][10]`, affichage, trésors, pièges, déplacement `zqsd`.
- **8 — Morpion** (bilan formatif) : étapes, sortie attendue, bonus 1D, grille d'auto-évaluation par notion.
- Corrigés écrits et exécutés pour 3, 7 et 8 (sorties citées dans l'énoncé = sorties réelles). Le cadre *Overview à valider* est retiré.
- Le fichier `Exercices - 01b - …` n'est pas modifié ; sa partie *Strings* reste la source de BDP-06.

## Traité le 05.10 — complément

**Slides** — `## `enum` simple ou `enum class` ?` passe de quatre puces à **deux slides de code**,
comme proposé :

- *`enum` simple : ce qui se passe mal* — un snippet qui tient les trois problèmes : la
  collision `ROUGE` entre `Couleur` et `Feu`, l'affectation `int degats = EPEE;`, et la
  comparaison `EPEE == MORT` entre deux énumérations étrangères.
- *`enum class` : le compilateur reprend la main* — le même code corrigé, ce qui devient
  refusé, et le prix à payer (`static_cast<int>` explicite).
- **Vérifié au compilateur** : la collision est une erreur dure, la comparaison entre
  énumérations ne déclenche qu'un *avertissement*, et les deux autres lignes passent en
  **silence** — c'est l'argument de la slide, et il est exact.

**Exercices** — la feuille unique devient **trois fichiers**, tous rattachés par
`seances: [GPR-CF-BDP-05]` et par leur nom :

| Fichier | Contenu |
| --- | --- |
| `GPR-CF-BDP-05 - Énumérations.md` | 1 Les états du garde, ~~2 Cris d'animaux~~, 3 Au restaurant |
| `GPR-CF-BDP-05 - Tableaux.md` | 4 Le meilleur score, 5 La valeur est-elle là ?, ~~6 Table de multiplication~~, 7 La carte du donjon |
| `GPR-CF-BDP-05 - Bilan formatif, le morpion.md` | 8 Morpion, bonus et grille d'auto-évaluation |

- Chaque feuille renvoie au cours et aux deux autres ; le préambule est repris dans les trois.
- Les deux exercices abandonnés (*cris d'animaux*, *table de multiplication*) restent
  **barrés** dans leur feuille, comme les autres abandons du vault.
- Contenu reporté mot pour mot : seuls les trois titres de section ont disparu, devenus les
  titres des fichiers.
- L'ancienne feuille combinée est supprimée ; ses trois liens entrants (note de séance, deck,
  cette note) pointent maintenant vers les trois feuilles.

> [!question] À trancher de ton côté
> - La séance n'a plus de feuille d'exercices portant **exactement** le nom du deck. C'est
>   voulu, mais ça déroge à la convention « même nom dans `lectures/`, `slides/`,
>   `exercises/` » : le rattachement tient désormais au champ `seances`.
> - Les messages d'erreur cités en note sont ceux de **MSVC** : aucun GCC n'est installé sur
>   cette machine, alors que le reste du deck cite GCC 14. À harmoniser quand tu auras GCC
>   sous la main.

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
