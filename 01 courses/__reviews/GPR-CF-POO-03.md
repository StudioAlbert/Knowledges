---
status: Ready
manual_order: 2.75
slides:
  - "[[01 courses/slides/C++/GPR-CF-POO-03 - Découpage en fichiers|Slides POO-03]]"
exercices:
  - "[[01 courses/exercises/C++/GPR-CF-POO-03 - Découpage en fichiers|Exos POO-03]]"
url_test: http://localhost:61638/cpp/gpr-cf-poo-03/
---
- [x] Mettre en page ![[{16BFE2EF-DA84-4EFD-99D5-FF95AFF94350}.png]]
## Traité le 05.10 — à vérifier (séance du 14.10)

> [!warning] La note était vide
> Aucune case à cocher : rien ne disait ce que tu attendais. J'ai fait **ce que valaient les
> cinq autres révisions de la journée** — développer le plan de 14 slides, écrire la feuille
> d'exercices, et fournir ce dont elle a besoin. Tout est à reprendre si l'intention était
> autre ; rien n'est détruit, le plan d'origine est dans l'historique git.

**Slides** (22, `publish: true`) — sections *Pourquoi découper* / *Ce que fait vraiment
`#include`* / *Ce qui va où* / *Le projet suit*.

- *Un seul fichier, jusqu'au jour où* donne les trois raisons, dont « deux personnes ne
  peuvent plus y travailler en même temps » — qui renvoie directement à GTE-02.
- **`## Forward declaration` était une slide vide** dans le plan : elle est écrite, avec le
  `class Arme;` et la raison (un pointeur n'a pas besoin du type complet).
- **Deux slides ajoutées** : *Deux façons d'inclure* (`<>` contre `""`, et l'ordre
  conseillé) et *Deux familles d'erreurs* — un tableau compilateur / éditeur de liens, qui
  est ce qui fait réellement perdre du temps aux élèves.
- **Snippets vérifiés au compilateur** (MSVC, C++23) : le duo `Joueur.h` / `Joueur.cpp`
  compile et tourne ; la double inclusion sans garde donne bien `C2011: redéfinition du
  type 'struct'` ; une méthode déclarée et jamais définie donne `LNK2019`, cité tel quel.

**Schéma** `poo03_unite_compilation.svg` (`tools/schemas/poo03_unite_compilation.py`) —
celui que le plan décrivait : `main.cpp`, `Joueur.h` et `Vector2.h` à gauche, l'unique
fichier fabriqué par le préprocesseur à droite, chaque bloc gardant la couleur de son
fichier d'origine, avec les pastilles 1-2-3 qui donnent l'ordre de recopie.

**Companion** `01 courses/companion projects/C++/GPR-CF-POO-03 - Découpage en fichiers/`

- `Exercice_5/main.cpp` : le donjon en **293 lignes**, un seul fichier, quatre concepts
  séparés par des bandeaux de commentaires — `Vector2`, `Journal`, `Entite`, `Salle`.
- **Compile sans aucun avertissement** (`/W4`) et se joue : déplacement `z s q d`, combat
  `a`, journal `j`. Partie vérifiée de bout en bout — le gobelin bloque le passage, tombe au
  troisième coup, le journal compte ses 12 événements.
- Les dépendances sont choisies pour que l'ordre de découpage soit évident :
  `Vector2` et `Journal` ne dépendent de personne, `Entite` de `Vector2`, `Salle` des deux.
- `README.md` donne le tableau des concepts et ce qui sera vérifié.

**Exercices** — les six sont rédigés, tous assis sur le companion.

- **1** sort `Vector2` ; l'encadré explique pourquoi `<string>` monte dans l'en-tête alors
  que `std::to_string` reste dans le source.
- **2** fait retirer la garde et recopier l'erreur réelle.
- **3** donne un `Journal.h` volontairement fautif — `<iostream>` inutile,
  `using namespace std`, un corps dans l'en-tête — et demande *ce que ça provoque chez celui
  qui inclut*, pas « c'est interdit ».
- **4** sépare compilateur et éditeur de liens, avec le piège : déclarer sans définir ne
  produit **rien** tant que personne n'appelle.
- **5** est le bilan : les quatre duos, la grille d'auto-évaluation, et le rendu = le projet
  **plus** le schéma des inclusions dessiné à la main.
- **6** ajoute `Arme` et la dépendance circulaire, avec une mesure de temps de compilation.

> [!question] À trancher de ton côté
> - **Le widget `inclusion_widget` du plan n'est pas construit.** Sur une note vide, je n'ai
>   pas voulu investir une journée de widget sans savoir si tu le voulais — d'autant que tu
>   as demandé « pas de widget » pour POO-02. Le schéma couvre le même point ; dis-moi si tu
>   veux le widget en plus (graphe d'inclusions avec interrupteur de gardes).
> - **Le companion n'est pas un sous-module**, comme celui de POO-02 : créer le dépôt public
>   est une action vers l'extérieur que je n'ai pas faite.
> - Le deck est passé en `publish: true`.

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
