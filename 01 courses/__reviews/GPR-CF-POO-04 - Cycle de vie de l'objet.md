---
status: Ready
manual_order: 1
url_test: http://localhost:56689/cpp/gpr-cf-poo-04/
slides: "[[01 courses/slides/C++/GPR-CF-POO-04 - Cycle de vie de l'objet]]"
---
- [x] C'est le private de POO-02 pris par l'autre bout — on ferme la porte, puis on installe la seule entrée. => Supprimer
- [x] Slide "Ce qui se passe vraiment", rappeller snippet de code en une ligne
- [ ] 
- [x] Créer companion : mini projet faisant démonstration du sujet
	- [x] une classe **Entity**  avec constructeur et destructeur et affichage console pour montrer par ou passe le programme
		- [x] Création d'une entité, destruction d'une entité dans le main
		- [x] Création d'une entité, destruction d'une entité dans un appel à une fonction (cette fonction a son propre )
		- [x] Création de deux entités a la suite dans le main
- [x] Détailler le contenu
- [ ] Publier — **en attente de toi** : le deck est en `draft`, un mot à changer

## Deuxième passe, le 12.10

- **Phrase supprimée.** La slide *Ce qu'il garantit* s'arrête sur ses trois puces.
- **Le schéma rappelle son code.** La ligne de contexte de *Ce qui se passe vraiment* est
  devenue le constructeur lui-même :
  `Monstre(int max) : pointsDeVieMax_(max), pointsDeVie_(pointsDeVieMax_)`. On lit la liste
  et le schéma sans revenir en arrière. La phrase qui y était est passée en note de
  présentation, où elle sert de commentaire oral.
- **Le companion a son dépôt** : `StudioAlbert/GPR_CF_POO_04_CycleDeVieDeLObjet`, poussé, et
  ajouté ici en sous-module. La fiche ressources affiche donc sa vraie fiche GitHub.
- **Publier** reste ouvert : la séance est le **14.10** et le deck est en `draft`. Il part en
  ligne quand tu passes cette note en *Ready*.

## Traité le 12.10 — à vérifier

**Companion construit.** `companion projects/C++/GPR-CF-POO-04 - Cycle de vie de l'objet/`,
structure conforme : une target par répertoire, la classe partagée dans `entity/` pour
qu'une ligne changée se voie dans les trois traces.

| Cible | Ce qu'elle montre | Trace |
|---|---|---|
| `01_dans_le_main` | la mort à l'accolade fermante | `- Gobelin` sort **après** `main : apres` |
| `02_dans_une_fonction` | la portée de la fonction | `- Squelette` sort **entre** deux lignes du `main` |
| `03_deux_entites` | l'ordre inverse | Troll meurt avant Gobelin |

Configuré et compilé au MSVC, les trois exécutables lancés : **les traces du deck sont
celles qui sortent vraiment**, pas des traces écrites à la main.

> [!warning] Le dépôt public n'existe pas encore
> Le companion est un dépôt git **local**, avec un commit, pas encore un sous-module : créer
> `StudioAlbert/GPR_CF_POO_04_CycleDeVieDeLObjet` et pousser est une action sur ton compte,
> je ne l'ai pas faite. Tant qu'il manque, la fiche ressources affiche une fiche GitHub
> réduite. Dis-moi et je l'enchaîne.

**Deck rédigé** : 23 slides, de 15 titres sans contenu. Découpage en trois temps — *Naître*,
*L'ordre*, *Mourir* — et l'atelier de fin pointe les trois étapes du companion.

**Schéma** `poo04_ordre_initialisation.svg` : la liste telle qu'on l'écrit en haut, l'ordre
de déclaration en bas, les deux liaisons qui se croisent, et le membre lu avant d'exister.
Mesuré à 978 x 323 dans le cadre.

**Un point vérifié au compilateur** plutôt qu'affirmé : MSVC ne dit **rien** sur l'ordre des
membres en `/W4`. Il faut `/w15038` pour sortir le C5038. La slide *La règle* montre les
deux lignes de commande et le message exact.

## Hors périmètre, à décider

- **La feuille d'exercices reste un overview** — six pistes de deux lignes, rien de rédigé.
  Le companion couvre le terrain des exercices 1 à 3. POO-03 a choisi de supprimer sa
  feuille au profit du companion ; ici je n'ai rien touché, la question n'était pas posée.
- **Le widget `cycle_de_vie_widget.html`** reste proposé et non construit. Le schéma et les
  traces du companion couvrent le sujet ; le widget apporterait le pas-à-pas.
- Le deck est en **`publish: draft`** : la séance est le **14.10**, donc le passage en
  `online` est à faire avant, après ta relecture.
