---
status: To check
manual_order: 4
url_test: http://localhost:56689/cpp/gpr-cf-poo-06/
slides: "[[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme]]"
---
- [x] Extraire contenu de 01 courses/lectures/C++/04 - OOP Advanced et l'inclure dans le deck final 
- [x] Proposer nouvel atelier de création d'une hierarchie, l'inclure comme formative
	- [ ] https://mermaid.ai/app/projects/cf787ab8-6815-4645-90a0-22f5b42df581/diagrams/c74b9e74-9c5f-474e-9c74-40517add3281/share/invite/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkb2N1bWVudElEIjoiYzc0YjllNzQtOWM1Zi00NzRlLTljNzQtNDA1MTdhZGQzMjgxIiwiYWNjZXNzIjoiRWRpdCIsInB1cnBvc2UiOiJzaGFyZS1pbnZpdGUiLCJpYXQiOjE3OTE3OTY0MjcsImV4cCI6MTc5NDM4ODQyN30.aNtRXTvQPKYZTBeAZwJZcdY_dgN5tbLCOTiNZRSkjfA?entryPoint=share-modal
	- [x] éléments d'énoncé
		- [x] un menu : 1/2/3/4/5 pour tirer avec une arme de chaque type 
		- [x] l'élève doit créer la hiérarchie, chaque entrée de menu utilise une arme différente de type différent

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

**Formative proposée** : [[01 courses/projects/C++/Formative - OOP - L'armurerie|L'armurerie]],
dans `projects/C++/` comme les autres formatives. Un stand de tir, cinq armes de cinq types,
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
