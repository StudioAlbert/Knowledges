---
status: Ready
manual_order: -1.5
slides:
  - "[[01 courses/slides/Theory/TC-FT-GVM-01 - Vecteurs et repères|Slides GVM-01]]"
exercices:
  - "[[01 courses/exercises/Theory/TC-FT-GVM-01 - Vecteurs et repères|Exos GVM-01]]"
url_test: http://localhost:61638/theory/tc-ft-gvm-01/
---
 - [x] Slide Soustraire => doit parler de la soustraction de VECTEURS (editer la comclusion)
 - [x] Intégrer le widget aprés chaque notion importante
- [x] Développer les slides
- [x] Widget
	- [x] presenter un vecteur
		- [x] , composantes
		- [x] , norme
		- [x] coordonnées A origine, B destination ?
		- [x] Interaction
			- [x] Deplacer l'origine (les compo)
			- [x] bouton pour afficher / cacher vecteur normalisé correspondant, le vrai vecteur passe en pointillé
	- [x] présenter une addition / soustraction de vecteur / multiplication scalaire
		- [x] ajouter slide avec onglet pointant sur le widget
- [x] Completer slide ## A quoi sert un vecteur ? avec d'autres cas d'usage
- [x] Reformuler exercice ### 3 — Somme de déplacements pour proposer une resolution de deplacement
- [x] iterer ensemble pour trouver des exercices 5 et6 plus parlants

## Traité le 05.10 — à vérifier (séance du 07.10, 13:30)

**Slides** (27, `publish: true`) — le plan de 16 slides est développé, sections *D'abord
pourquoi* / *Mesurer* / *Combiner* / *En mémoire, et dans le moteur*.

- **`## À quoi sert un vecteur ?`** devient un tableau à quatre cas : vitesse de la voiture,
  poussée du vent, position du trésor, pente du sol. Chaque ligne oppose ce que donne **un
  seul nombre** et ce que donne **le vecteur** ; la dernière (la normale) annonce GVM-02.
- **Slide ajoutée** *Point ou vecteur ?* — `transform.position` contre `velocity`, la
  confusion numéro un de l'année — et *Le piège du vecteur nul* (le `NaN` qui se propage).
- **Snippets** (4) : `Norme`, `Normaliser`, le déplacement `direction × vitesse × dt`, et
  `Vector2` avec le calcul `cible − joueur`. Tous sous 13 lignes.
- **Formules en unicode** (`‖v‖ = √(x² + y²)`), pas en LaTeX : aucun deck du vault n'utilise
  `$$`, et le style maison est celui de TRG-01.

**Widget** `00 widgets/_widgets/vecteur_widget.html`, deux onglets, deux slides sans titre.

- `#vecteur` : A et B attrapables à la souris, composantes de **AB = B − A**, norme détaillée
  et direction normalisée. Case *vecteur normalisé* → le vrai vecteur passe en pointillé et
  la direction unitaire s'affiche en rouge ; case *même vecteur depuis l'origine* → le même
  AB redessiné en O, pour montrer qu'une flèche n'a pas de point de départ imposé.
- `#operations` : u et v attrapables, boutons `u + v` (avec le parallélogramme en pointillé),
  `u − v` (la flèche va bien de v vers u, sa norme est la distance) et `k · u` avec un
  curseur de −2 à 3. Le panneau compare ‖u + v‖ à ‖u‖ + ‖v‖.
- Conventions du dossier respectées : palette SAE, mode `embed`, onglets par ancre, flèches
  renvoyées à reveal.js. Inventaire de `00 widgets/README.md` mis à jour.

**Schéma** `gvm01_reperes.svg` (`tools/schemas/gvm01_reperes.py`) : Unity, Unreal et le repère
mathématique côte à côte. La même lettre garde la même couleur dans les trois panneaux — ce
qui change, c'est le rôle qu'elle joue. Pastille *main gauche* / *main droite*, unité du
moteur, et la règle du pouce / index / majeur en pied de figure. Il remplace le trièdre
décrit dans le plan.

**Exercices** — les trois courts sont rédigés avec leurs valeurs et leurs corrigés.

- **3 — Résoudre un déplacement** (reformulé) : la somme poussée + courant devient une
  résolution complète — vitesse résultante, vitesse **réelle** comparée au moteur seul,
  position après 2 s, et le courant qui annule la poussée. Encadré sur ‖u + v‖ ≠ ‖u‖ + ‖v‖.
- **4 — Le vaisseau, la poussée et le courant** (nouveau, remplace le radar) : la boucle de
  simulation qui enchaîne les cinq opérations de la séance, puis trois questions — courant
  plus fort que le moteur, oubli de la normalisation, départ sur la cible.
- Corrigé écrit et **exécuté** (MSVC, `/std:c++latest`) : la sortie citée est la sortie
  réelle, et la variante « courant (−5 ; 0) » a été vérifiée — la distance passe de 22,36 à
  plus de 40 en vingt secondes.
- Les ex. 5 et 6 restent **barrés** : pas de remplacement pour le difficile, comme convenu.
  Le nouvel exercice complet prend le numéro 4, qui manquait.

> [!question] À trancher de ton côté
> - L'exercice 4 suppose que les élèves savent écrire une boucle et une fonction qui rend
>   une `struct`. POO-01 passe le même jour à 09:30 : l'ordre est bon, mais c'est frais.
> - Le deck est passé en `publish: true` pour être relisible sur le site. À confirmer.

## Traité le 06.10 — à vérifier (27 → 33 slides)

**La soustraction parle enfin de vecteurs.** La slide *Soustraire* définissait l'opération
par son usage (`cible − joueur`), c'est-à-dire par une soustraction de **points**. Elle est
coupée en deux :

- ***Soustraire*** — l'opération, composante par composante, `u − v = (uₓ − vₓ, u_y − v_y)`,
  présentée comme l'addition de l'opposé, avec le résultat qui va de v vers u ;
- ***Et sur deux positions*** — l'application : `AB = B − A`, la direction et la distance.

La **conclusion est éditée** dans la même logique : « soustraire deux vecteurs en soustrait
les composantes — et sur deux positions, `cible − joueur` donne la direction ».

**Le widget suit chaque notion.** Il y en avait deux ; il y en a sept, un après chaque point
du cours :

| Après la slide | Ancre | Ce qui est préréglé |
|---|---|---|
| Composantes | `#vecteur` | A et B attrapables, composantes en direct |
| Point ou vecteur ? | `#origine` | case « même vecteur depuis l'origine » déjà cochée |
| La norme en C++ | `#norme` | le détail √(x² + y²) sur les valeurs courantes |
| Normaliser en C++ | `#normalise` | case « vecteur normalisé » déjà cochée |
| Multiplier par un scalaire | `#scalaire` | onglet Opérations, curseur k |
| Additionner | `#somme` | onglet Opérations, `u + v` et son parallélogramme |
| Soustraire | `#difference` | onglet Opérations, `u − v` |

Pour ça, **le widget comprend désormais une ancre par notion** et plus seulement une par
onglet : l'ancre ouvre l'onglet **et** le préréglage. Les sept sont vérifiées une à une
(bon onglet, bonne opération, bonnes cases). Inventaire de `00 widgets/README.md` à jour.

**Mise en page** : le deck passe l'audit des 713 slides sans débordement.
