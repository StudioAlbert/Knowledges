---
status: Ready
manual_order: 2.5
slides:
  - "[[01 courses/slides/C++/GPR-CF-POO-02 - Classes et visibilité|Slides POO-02]]"
exercices:
  - "[[01 courses/exercises/C++/GPR-CF-POO-02 - Classes et visibilité|Exos POO-02]]"
url_test: http://localhost:61638/cpp/gpr-cf-poo-02/
---
- [x] Mettre en page![[{9FF7F33E-3D0C-4994-BED5-76417C5EC791}.png]]
	- (Poser regles css)
		- image reduite
		- Titre en position absolue pour ne JAMAIS mordre le cadre
- [x] pas de widget 
- [x] développer contenu
- [x] Exercices
	- [x] exercice 5 : proposer companion avec le menu, l'éléve complete seulement la classe joueur

## Traité le 05.10 — à vérifier (séance du 08.10)

**Slides** (23, `publish: true`) — sections *Le problème* / *Les méthodes* / *Encapsuler* /
*Classe et instance*.

- **Bornes de la séance tenues** : pas de constructeur (POO-04), pas de `.h` / `.cpp`
  (POO-03). Les attributs sont initialisés à leur déclaration, ce qui évite les deux.
- **Pas de redite avec POO-01** : `public:` / `private:` et la différence `class` / `struct`
  y sont déjà traitées. Ici, une seule slide de rappel, puis la vraie question — *à quoi ça
  sert*.
- *La règle n'existe nulle part* pose le problème : une borne répétée dans le combat, les
  pièges, les soins et le poison est une borne qu'on oubliera.
- *Le membre et le paramètre* fixe la convention `_` final, qui n'est pas une règle du
  langage.
- *Accesseurs, et quand s'en passer* : un `pointsDeVie()` qui rend le champ rouvre ce que
  `class` venait de fermer ; l'appelant veut souvent un verdict (`estVivant`).
- **Snippets vérifiés au compilateur** : la classe `Joueur`, les appels bornés
  (`100 → 70 → 0`, puis `0 → 100`), le tableau de trois instances, et l'erreur d'accès privé
  (MSVC C2248, citée telle quelle).

**Pas de widget**, comme demandé. Le `encapsulation_widget` du plan est remplacé par le
schéma **`poo02_encapsulation.svg`** (`tools/schemas/poo02_encapsulation.py`) : l'objet en
deux zones, l'appel qui passe par l'interface publique, et l'accès direct au champ privé
barré d'une croix — avec l'invariant `0 ≤ pointsDeVie_ ≤ pointsDeVieMax_` écrit dedans.

**Exercices** — la feuille est rédigée (1, 2, 4, 5, 6 ; la 3 reste barrée).

- **1 — Fermer la structure** : remplacer `struct` par `class` et compter ce qui casse.
  Vérifié : une seule ligne, **trois** erreurs C2248. La question 4 (« auriez-vous pu n'en
  écrire qu'une ? ») amène `afficherFiche()` plutôt que trois accesseurs.
- **2** : les deux bornes, avec la sortie attendue.
- **4** : la fonction libre devient méthode — et le cas où la fonction libre reste le bon
  choix (`memeEspece(a, b)`).
- **6** : réécrit autour du mot **invariant**, et le rendu demandé est la *liste de tests
  qui échouent*, pas le jeu.

**Companion de l'exercice 5** —
`01 courses/companion projects/C++/GPR-CF-POO-02 - Classes et visibilité/`

- `Exercice_5/main.cpp` **fourni et complet** : le menu lit une commande et appelle une
  méthode. Il ne connaît aucun compteur, aucune borne, aucun coût.
- `Exercice_5/joueur.h` **à compléter** : six `// TODO`, un par règle, avec le comportement
  attendu écrit au-dessus de chacun.
- **Le squelette compile et tourne tel quel** : le menu s'affiche et toutes les actions sont
  refusées. Vérifié (MSVC, C++23).
- **Corrigé écrit et exercé** : `c c c c c c` vide l'endurance puis refuse, `r` remonte à 50
  et pas à 60, trois `o` pour deux clés, deux `a` pour 30 d'or, et la vie descend
  70 → 40 → 10 → 0 sans passer négative. Le corrigé n'est **pas** dans le companion.
- `README.md` reprend le tableau des règles et le test de recette.

> [!question] À trancher de ton côté
> - **Le companion n'est pas encore un sous-module.** Créer le dépôt public
>   `GPR_CF_POO_02_ClassesEtVisibilite` sous `StudioAlbert` est une action vers l'extérieur :
>   je ne l'ai pas faite. Tant qu'il n'existe pas, l'exercice pointe le **dossier**, pas un
>   bloc ```` ```github ```` — qui produirait un avertissement au build et une fiche réduite.
>   Même situation que le companion BDP-06, ajouté en fichiers simples.
> - `joueur.h` est un **header rempli en ligne**, alors que POO-03 n'a pas encore eu lieu.
>   C'est assumé (l'élève n'y touche pas comme à un header, il remplit des méthodes), mais
>   dis-moi si tu préfères tout ramener dans `main.cpp`.
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

> [!note] Les deux règles que tu demandais
> - **« image réduite »** : c'est le `flex` sur l'image d'une slide `schema`. Elle se
>   réduit d'elle-même si le dessin est trop haut, au lieu de pousser le titre dehors.
> - **« titre en position absolue »** : le padding de 104 px joue ce rôle sans sortir le
>   titre du flux — il ne peut plus commencer au-dessus de 104, quelle que soit la
>   hauteur du contenu. Un vrai `position: absolute` aurait figé aussi la hauteur du
>   titre, et cassé les titres sur deux lignes.
>
> Au passage, `poo02_encapsulation.svg` : l'invariant `0 ≤ pointsDeVie_ ≤ pointsDeVieMax_`
> chevauchait le bord de la zone privée, il est remonté dedans.
