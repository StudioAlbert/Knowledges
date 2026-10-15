---
status: Ready
manual_order: -2
url_test: http://localhost:54573/cpp/gpr-cf-poo-06/
slides: "[[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme]]"
exercices:
  - "[[01 courses/exercises/C++/GPR-CF-POO-06 - Héritage et polymorphisme - Formative|Formative POO-06]]"
---
- [x] Pas d'exercices, pas d'atelier => un seul exercice Formative basé sur le contenu de l'atelier initial
- [x] se baser sur la hierarchie pour rédiger les étapes de l'exercice
- [x] ajouter companion pour lancer les étudiants sur l'exercice
	- [x] donner Menu avec une arme, classe non héritée
	      
> [!Tip] Dans la rédaction des consignes, rester concis (peu de mots, phrases courtes, mots précis et spécifiques)
> 

- [x] Extraire contenu de 01 courses/lectures/C++/04 - OOP Advanced et l'inclure dans le deck final 
- [x] Proposer nouvel atelier de création d'une hierarchie, l'inclure comme formative
	- [x] https://mermaid.ai/app/projects/cf787ab8-6815-4645-90a0-22f5b42df581/diagrams/c74b9e74-9c5f-474e-9c74-40517add3281/share/invite/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb2N1bWVudElEIjoiYzc0YjllNzQtOWM1Zi00NzRlLTljNzQtNDA1MTdhZGQzMjgxIiwiYWNjZXNzIjoiRWRpdCIsInB1cnBvc2UiOiJzaGFyZS1pbnZpdGUiLCJpYXQiOjE3OTE3OTY0MjcsImV4cCI6MTc5NDM4ODQyN30.aNtRXTvQPKYZTBeAZwJZcdY_dgN5tbLCOTiNZRSkjfA?entryPoint=share-modal
	- [x] éléments d'énoncé
		- [x] un menu : 1/2/3/4/5 pour tirer avec une arme de chaque type 
		- [x] l'élève doit créer la hiérarchie, chaque entrée de menu utilise une arme différente de type différent

## Deuxième passe, le 12.10 — à vérifier

**La hiérarchie est la tienne**, reprise du diagramme : `Weapon` → `Firearm` →
`SemiAutomatic` / `FullAuto`, et `Melee` à côté. Trois niveaux, pas deux — et la formative
dit **pourquoi** : `Melee` n'a pas de chargeur, donc `Reload()` ne peut pas monter sur
`Weapon`. `Firearm` existe pour porter ce que seules les armes à feu partagent. C'est le
point que ma première proposition, à plat, ratait complètement.

Une seule liberté prise : les attributs sont notés `+` sur ton diagramme, ils sont écrits
`protected` dans l'énoncé. Sinon POO-02 est contredit deux séances plus tard. C'est dit dans
la formative, en une phrase.

**Plus de feuille d'exercices, plus d'atelier.**
`exercises/C++/GPR-CF-POO-06 - Héritage et polymorphisme.md` est supprimée, et la slide
*Atelier — 20 min* devient *La formative* : quatre puces, le companion, la contrainte, le
test final. Le site ne rattache plus d'exercice à POO-06.

**Companion créé** : `StudioAlbert/GPR_CF_POO_06_HeritageEtPolymorphisme`, poussé, ajouté en
sous-module, avec sa fiche ressources. Une cible, `01_une_seule_arme` : une classe `Weapon`
sans parent, un menu qui l'appelle directement. Compilé et lancé au MSVC — tirer, recharger,
chargeur vide.

Le premier geste demandé est volontairement le mauvais : **ajouter une deuxième arme par
copier-coller**. C'est ce qui fait apparaître le problème avant qu'on en donne la solution.

**Consignes resserrées**, comme demandé : phrases courtes, sept étapes numérotées, un verbe
par étape, et le tableau d'auto-évaluation en cinq lignes.

**18 slides**, aucune hors cadre.

## Traité le 12.10 — à vérifier

**Deck rédigé**, 18 slides, de 14 titres sans contenu. Repris de `04 - OOP Advanced` : le
principe de l'héritage, `protected` et `using`, le mode d'héritage, l'héritage multiple, la
démonstration `virtual`, la virtuelle pure. `static` et la surcharge d'opérateur restent à
POO-05, comme le prévoyait la note de séance.

Ce qui a changé en route : le support d'origine montrait `A` / `B` et `Print` / `Show`, qui
ne disent rien. Le deck garde `Monstre` et `Dragon`, la famille des séances précédentes, et
chaque bout de code est **compilé** avant d'entrer dans une slide.

| Slide | Ce qui est montré | Vérifié |
|---|---|---|
| *L'enfant* | accès `protected` accepté, `private` refusé | `error C2248` au MSVC |
| *Ce que ça change* | `attaquer()` virtuel, `avancer()` non | sortie réelle du programme |
| *La classe abstraite* | `Monstre m;` refusé | `error C2259` au MSVC |
| *Le destructeur virtuel* | `~Dragon` jamais appelé sans `virtual` | sortie réelle, et **aucun avertissement** en `/W4` |

**Schéma** `poo06_diamant.svg` : le diamant à gauche, la base plus interface à droite.
Mesuré à 958 x 326 dans le cadre.

**Formative proposée** : [[01 courses/exercises/C++/GPR-CF-POO-06 - Héritage et polymorphisme - Formative|L'armurerie]],
dans `exercises/C++/`, publiée comme l'exercice de la séance. Un stand de tir, cinq armes de cinq types,
un menu `1`…`5`, et la contrainte qui porte tout : **aucun test sur le type** dans le menu.
Le test final est d'ajouter une sixième arme sans toucher au menu. La hiérarchie est dessinée
en `mermaid` dans la note, et l'atelier de fin de deck la reprend en quatre étapes.

> [!question] Ton diagramme Mermaid, je ne l'ai pas vu
> Le lien de partage demande une connexion à mermaid.ai, et je ne me connecte pas à ton
> compte. La hiérarchie que je propose — une base abstraite `Arme` et cinq filles — est donc
> la mienne. Si ton diagramme dit autre chose, envoie-le et je recale la formative dessus.
> C'est la seule case que je laisse ouverte.

## Hors périmètre, à décider

- **La feuille d'exercices reste un overview**, six pistes de deux lignes. La formative
  couvre le terrain de l'exercice complet.
- **Le widget `dispatch_widget.html`** reste proposé, pas construit : les deux sorties
  console du deck disent déjà ce qu'il montrerait, mais sans le pas-à-pas.
- Le deck est en **`publish: draft`** et la séance est le **14.10** : le passage en `online`
  est à faire avant, après ta relecture.
