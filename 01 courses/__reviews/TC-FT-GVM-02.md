---
status: Ready
manual_order: 3
slides:
  - "[[01 courses/slides/Theory/TC-FT-GVM-02 - Produits scalaire et vectoriel|Slides GVM-02]]"
exercices:
  - "[[01 courses/exercises/Theory/TC-FT-GVM-02 - Produits scalaire et vectoriel|Exos GVM-02]]"
url_test: http://localhost:60720/theory/tc-ft-gvm-02/
---
- [x] Mise en page widget dans la formule ![[Pasted image 20261006133612.png]]

- [x] Slide La normale d'une surface : propose schema en 3D
- [x] Slide Le produit mixte : expliciter w

- [x] Slide "Definition" mettre en indice le y
- [x] terme impropre en francais Rejet : mauvaise traduction ? que représente ce terme ? est il utilisé en géométrie ?
- [x] Widget "De quel coté" : 
	- [x] permettre au snapping de manipuler des vecteurs colineaires
	- [x] cos phi : comment est calculé phi ?
	- [x] Aller a la ligne entre regard et cible ![[{3D516141-F530-424C-8837-B17DB9EA33C6}.png]]
- [x] c'est quoi le produit mixte ? produire slide
- [x] proposer développement du contenu
- [x] Exercices
	- [x] Préambule : ajouter un exercice d'implémentation d'un vecteur + exercice compémentaire, l'ennemi est il dans la range de distance ?
	- [x] ajouter un exercice (comprendre la session)
		- [x] Implémenter une fonction d'addition
		- [x] une fonction de multiplcation scalaire
		- [x] une fonction de calcul du produit vectoriel
		- [x] fournir les protoypes 
	- [x] ajouter un formative qui demande au eleve de determiner si une cible est dans une range de distance Et d'angle. Guider l'exercice.

## Traité le 05.10 — à vérifier (séance du 08.10, 11:10)

**Slides** (28, `publish: true`) — l'ossature que tu avais posée à la main est gardée telle
quelle et développée autour :

- *AB × BC ?* ouvre sur la vraie question, avec le piège du produit composante par
  composante qui « ne veut rien dire ».
- *Deux produits, deux réponses* : un tableau qui pose scalaire → un **nombre**, vectoriel →
  un **vecteur**. Toute la séance tient dedans.
- *Définition et méthode de calcul*, puis *La seconde écriture* (`‖u‖‖v‖cos θ`) : l'une se
  calcule, l'autre s'interprète.
- *Cas particulier : perpendiculaires* (`u · v = 0`, avec l'epsilon) et *Cas particulier :
  colinéaires* — cette dernière amène le produit vectoriel comme **test symétrique**
  (`u × v = 0`), ce qui est l'enchaînement que tu avais noté.
- Sections *Projeter et réfléchir* (projection, rejet, formule du rebond) et *Le produit
  vectoriel* (calcul 3D et 2D, côté, normale, aire / volume / base).
- **Snippets** (3) : `Dot` avec le test « devant », `Cross` avec les trois cas, et le cône
  de vision par comparaison de cosinus.

**Widget** `00 widgets/_widgets/produit_scalaire_widget.html`, trois onglets — il **remplace
les deux widgets** promis par le plan, qui n'existaient pas :

- `#scalaire` : u et v attrapables, le calcul détaillé, l'arc d'angle, le verdict
  *d'accord / perpendiculaires / opposés*, et l'équerre qui apparaît à 90°.
- `#projection` : l'ombre de u sur v en rouge, le rejet en pointillé vert avec son angle
  droit, et `proj · rejet = 0` affiché en permanence.
- `#orientation` : le garde, son regard, la cible, le demi-plan coloré, plus un cône réglable
  (±angle, portée) qui montre que « voir » demande les **deux** produits.

**Exercices** — trois ajouts, les deux courts rédigés, les ex. 3 à 6 toujours barrés.

- **Préambule A** — *Reconstruire `Vector2`* : les cinq fonctions de GVM-01 dans un
  `vecteur.h` que les suivants incluent, avec le test `NaN` (`v.x == v.x` est faux).
- **Préambule B** — *L'ennemi est-il à portée ?* : la portée avec `sqrt`, puis **sans**, en
  comparant les carrés, et pourquoi les deux réponses sont identiques.
- **1 et 2** rédigés avec leurs tableaux et leurs corrigés : le signe seul, puis le cône par
  comparaison de cosinus (avec le sens du `≥`, qui surprend toujours).
- **7 — Les trois opérations à la main** : prototypes fournis, `Dot` et `Cross` à écrire,
  puis cinq vérifications qui font *démontrer* commutativité, anticommutativité, linéarité,
  et les deux droites `Dot = 0` / `Cross = 0`.
- **8 — Le garde voit-il le joueur ?** (bilan formatif, guidé) : six cibles, les trois tests
  dans l'ordre distance → angle → côté, grille d'auto-évaluation. Corrigé **exécuté** (MSVC,
  `/std:c++latest`) : la sortie citée est la sortie réelle.
- Heureux hasard du jeu de données : **(2, −2)** tombe à 45,0° pile, cosinus 0,71 contre une
  limite de 0,707. La question 7 s'appuie dessus pour parler de la comparaison en flottants.

> [!question] À trancher de ton côté
> - Le préambule est numéroté **A** et **B** pour ne pas bousculer les numéros 1 à 6, dont
>   quatre sont barrés. Si tu préfères une renumérotation complète, c'est une passe à faire.
> - `Dot` ne figurait pas dans ta liste de prototypes (addition, multiplication scalaire,
>   produit vectoriel), mais les exercices 1, 2 et 8 ne tiennent pas sans. Je l'ai ajouté.
> - Le deck est passé en `publish: true`. À confirmer, comme pour GVM-01.

## Traité le 06.10 — à vérifier (28 → 31 slides)

**1. Les indices.** L'unicode n'a pas d'indice `y` — d'où le `u_y` à côté du `uₓ`. Une
règle CSS `p.formule` est posée dans `sae_styles.css` : elle donne à un paragraphe
l'allure d'un bloc de code tout en rendant le HTML, donc de **vrais** indices. Les slides
*Définition et méthode de calcul* et *Le calcul, en 3D et en 2D* l'utilisent.

**2. « Rejet » — réponse aux trois questions.**

- **Mauvaise traduction ?** Oui, c'est un calque de l'anglais *vector rejection*.
- **Que représente le terme ?** La part de `u` qui reste une fois retirée sa projection sur
  `v` — donc sa composante perpendiculaire à `v`.
- **Est-il utilisé en géométrie ?** Non. La géométrie française dit **composante
  orthogonale** (ou normale), et note la décomposition `u = u∥ + u⊥`.

La slide s'appelle désormais *La composante orthogonale* et emploie `u∥` / `u⊥`. Une note
garde le mot « rejet » comme vocabulaire **à reconnaître dans la doc des moteurs, pas à
employer**. Le widget, la feuille d'exercices et la note de séance suivent.

**3. Le widget « De quel côté »**, les trois points :

- **Colinéaires atteignables** : une **aimantation** a été ajoutée. À moins de 5,7° d'une
  direction remarquable de l'autre vecteur — même sens, opposé, ou perpendiculaire — le
  point s'y pose exactement. Vérifié : on obtient `regard × cible = 0`, verdict
  « alignée », cos θ = 1. Elle vaut aussi pour l'onglet *Signe et angle*, où elle permet
  d'atteindre le produit scalaire exactement nul.
- **Comment est calculé φ** : le panneau le déroule maintenant en trois lignes —
  `direction = cible / ‖cible‖`, puis `cos θ = regard · direction`, puis `θ` en degrés et
  la limite `cos(demi-angle)`. On voit d'où vient chaque nombre.
- **Retour à la ligne** : `regard` et `cible` sont sur deux lignes séparées, plus de
  coupure au milieu d'une coordonnée.

**4. Le produit mixte** a ses slides, là où il n'était qu'une ligne :

- ***Aire*** — `‖u × v‖` et ce qu'elle sert (triangle, pondération des normales) ;
- ***Le produit mixte*** — `(u × v) · w` déroulé en trois temps : aire de la base, hauteur
  par projection, volume. Et d'où vient le nom : il *mélange* les deux produits ;
- ***Ce que le produit mixte répond*** — nul = coplanaires = pas de base, et le signe qui
  donne l'orientation du trièdre (le test de la main de GVM-01, devenu calcul).

## Traité le 06.10 — les trois points

**1. Mise en page du widget.** Le panneau fait 310 px de large : une formule et son
résultat sur la même ligne cassaient au milieu d'une coordonnée (`= (0.5,` / `0.87)`).
Chaque calcul tient désormais sur **deux lignes** — la formule, puis le résultat — dans
les trois onglets. Vérifié ligne par ligne à 1280 px : **aucune ne passe à la ligne**.

**2. La normale d'une surface, en 3D.** Schéma **`gvm02_normale_3d.svg`**
(`tools/schemas/gvm02_normale_3d.py`) : le même triangle vu deux fois en perspective, les
sommets lus `A → B → C` à gauche et `A → C → B` à droite. Les deux arêtes du calcul sont
dessinées, la face est remplie, et **la normale se retourne** d'un panneau à l'autre — la
face de droite est éliminée par le backface culling. La slide devient une slide `schema` ;
la formule et ses conséquences passent sur une slide suivante, *Ce que l'ordre des sommets
décide*, avec le modèle « troué » en note.

> Au passage, `schema_lib.line()` accepte maintenant un `fill` : c'est ce qui permet de
> remplir une face. Utile pour toutes les figures 3D à venir.

**3. Expliciter `w`.** La slide posait `(u × v) · w` sans jamais dire ce qu'est `w`. Elle
l'annonce maintenant d'entrée : **trois** vecteurs partant du même point, `u` et `v`
définissent la base, **`w` est la troisième arête, celle qui donne l'épaisseur**. Les trois
étapes nomment son rôle à chaque ligne (aire de la base, projection de `w` = hauteur,
volume), et la note insiste : si `w` reste dans le plan de `u` et `v`, la boîte est plate.
