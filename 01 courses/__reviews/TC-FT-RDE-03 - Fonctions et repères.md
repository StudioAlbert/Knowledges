---
slides: "[[01 courses/slides/Theory/TC-FT-RDE-03 - Fonctions et repères]]"
exercices: "[[01 courses/exercises/Theory/TC-FT-RDE-03 - Fonctions et repères]]"
formatif: "[[01 courses/exercises/Theory/TC-FT-RDE-03 - Formatif, les degats selon la distance]]"
---
- [x] Compléter slides essentiellement avec exemples visuels
- [x] pour la partie ** Combiner**
	- [x] Montrer le graphe d'une combinaison f .g 
	- [x] Citer les notions mathematiques qui permettent de composer
	- [x] Basculer les slides Valeur absolue et bornage comme elements d'introduction du formative
	- [x] Le formative propose l'implementation du calcul des degats selon la distance
		- [x] Poser les regles de gameplay : 25 degats a bout portant (< 0.25 m), 0 degats a 5 m de distance, proportionelle entre les 2
		- [x] proposer aux eleves de completer les fonctions dédiées
			- [x] la premiere DegatsProportionelles repond a la regle de gameplay posée
			- [x] donner aux eleves les etapes d'implementation (Reformuler le brouillon ci-dessous)
				- [x] Degats proportionnelles
					- [x] la fonction repond max degats, 1/2 degats ou 0 degats selon les regles invoquées, mettre en place les bornes evoquees
					- [x] mettre en place la proportionnalité
				- [x] Degats amortis
					- [x] Montrer une courbe d'amorti des degats (log inverse ??), le graphe courbe montre des points et valeurs particulieres a respecter
					- [x] Demander aux eleves de trouver
						- [x] le calcul le plus approprié
						- [x] une methode permettant de verifier que le code matche le graphe
		- [ ] Proposer un projet companion avec une pré-implémentation
			- [ ] on entre la distance, le programme log le resulat du calcul dans la console
			- [ ] créer deux fonctions vides DegatsProportionelles, DegatsAmortis. En commentant l'une ou l'autre appel de fonction, on passe d'un mode a l'autre
## Traité le 20.10 — à vérifier

**Deck**, 21 slides, de 15 titres sans contenu. Comme demandé, le visuel porte la séance :
un schéma catalogue, un widget plein écran, un tableau de lecture de graphe, et une fonction
par morceaux dessinée en chasse fixe. Aucune slide hors cadre, 5 formules KaTeX sans erreur.

**Schéma** `rde03_catalogue.svg` : six tracés côte à côte — droite, parabole, racine,
exponentielle, logarithme, valeur absolue — chacun avec sa formule et ce qu'il règle dans un
jeu. Le but assumé n'est pas d'étudier ces courbes, c'est de les **reconnaître**.

**Widget** `fonctions_widget.html`, celui que le squelette décrivait : six fonctions de jeu —
dégâts par distance, sensibilité souris, courbe d'XP, volume en dB, racine, écart — avec
leurs curseurs. Le panneau lit **domaine, image, monotonie, racines, extremum**, et le
sélecteur « puis » compose avec `clamp`, `1 − y` ou `y²`.

Vérifié sur les six fonctions : la composition inverse bien la monotonie, et un palier à zéro
ne compte plus qu'**une** racine au lieu d'une par échantillon.

## Un signalement, pas un arbitrage

> [!bug] Le widget que le squelette proposait de réutiliser ne va pas
> La slide *Le premier degré et sa pente* disait : « réutiliser `droites_remarquables_widget.html`,
> le widget existant du bloc suffit pour la pente et l'ordonnée à l'origine ».
>
> Ce widget traite les **médianes, hauteurs, médiatrices et bissectrices d'un triangle** et
> leurs points de concours (TC-FT-TRG-01). Il n'a ni pente, ni ordonnée à l'origine, ni
> `y = ax + b`. La réutilisation n'était pas possible.
>
> La pente est donc traitée en slide, et la lecture « sensibilité » est passée dans
> `fonctions_widget` où elle a sa propre courbe — `f(x) = x^k`, avec l'exposant au curseur.
> C'est le même point pédagogique, mieux placé.

## Deux arbitrages

**1. L'atelier est réécrit autour du traceur.** Le squelette disait « régler la courbe
d'atténuation d'un fusil à pompe, puis celle de la sensibilité de visée ». J'en ai fait
quatre questions qui s'appuient sur le widget, dont une sur la composition avec `clamp` et
une sur l'écriture en fonction par morceaux avec vérification des raccords. **Les réponses ne
sont nulle part** — à décider si tu veux un corrigé.

**2. Le découpage du support d'origine n'a rien donné.** `08 - Theorical Notions of graphics
programming - Maths` ne porte sur ce lot que deux slides — la droite et la parabole, en trois
lignes chacune. Tout le reste du deck est neuf. Même constat qu'en RDE-02 : ce support
annonce huit heures mais n'en contient pas la matière.

## Hors périmètre

La feuille d'exercices reste un **overview** de six pistes.

## Deuxième passe, le 20.10 — à vérifier

24 slides, **aucune hors cadre**, aucune image cassée. La partie *Combiner* est refaite et
elle mène maintenant droit au formatif.

### Le graphe d'une composition

`rde03_composition.svg` — **trois** repères côte à côte, et c'est volontairement l'exemple du
formatif plutôt qu'un exemple abstrait :

| | |
|---|---|
| `f` | la distance, ramenée entre 0 et 1 par `clamp((d − 0,25) / 4,75 ; 0 ; 1)` |
| `g` | ce nombre, transformé en dégâts : `25 (1 − t)` |
| `g ∘ f` | la courbe qu'on branche dans le jeu : plateau, descente, zéro |

Ce que le dessin fait voir et qu'une formule ne fait pas : **aucune des deux ne connaît
l'autre**. On peut changer la courbe du milieu sans retoucher les bornes — c'est exactement
ce que l'étape 2 du formatif demande.

### Les notions qui permettent de composer

Une slide, quatre lignes, et chacune est opératoire :

- le **domaine** : l'image de `f` doit tenir dans le domaine de `g` ;
- la **monotonie** se transmet — deux croissantes donnent une croissante, une décroissante
  inverse le sens ;
- la **normalisation** entre 0 et 1 rend les courbes interchangeables ;
- le **bornage** garantit la première ligne, et c'est tout le rôle du `clamp`.

La phrase de fin dit la sanction : composer sans vérifier le domaine, c'est une racine de
négatif ou une division par zéro.

### Valeur absolue et bornage, devenus l'introduction du formatif

La slide est renommée **Les deux outils du formatif** et sa note de présentation l'annonce :
à partir de là, tout ce qui est montré sert à l'exercice. *Fonction par morceaux* la suit et
porte la même mention — « la forme du formatif, aux valeurs près ».

### Le formatif

[[01 courses/exercises/Theory/TC-FT-RDE-03 - Formatif, les degats selon la distance|Les dégâts selon la distance]],
rattaché à la séance. Les règles de gameplay sont celles que tu as posées, et rien d'autre :
**25 dégâts sous 0,25 m, 0 dégât à partir de 5 m, ça descend entre les deux.**

**Étape 1 — `DegatsProportionnels`**, en deux temps comme demandé :

1. *les bornes seules* — la fonction ne sait répondre que 25, 12,5 ou 0. C'est faux au
   milieu, et c'est dit : les deux règles de bord sont posées et ne bougeront plus ;
2. *la proportionnalité* — normaliser, borner, descendre. Le point que la feuille insiste à
   faire voir : une fois le `clamp` en place, **les deux `if` de l'étape 1 disparaissent**.

**Étape 2 — `DegatsAmortis`.** La formule n'est **pas** donnée. Ils reçoivent
`rde03_degats_amortis.svg` : la courbe, et cinq points à respecter.

| d (m) | 0,25 | 1,40 | 2,60 | 3,80 | 5,00 |
|---|---|---|---|---|---|
| dégâts | 25,0 | 21,8 | 17,8 | 12,6 | 0,0 |

La feuille donne trois indices sans donner la réponse — les bornes restent exactes, la moitié
des dégâts tombe à **3,8 m** et non au milieu, et on travaille sur `1 − t` et non sur `t`. Et
elle demande la **méthode de vérification** : faire afficher la table par le programme, la
comparer aux cinq points à ± 0,5, ajouter les deux bornes et un point hors domaine, conclure
en une phrase. C'est la méthode qui est évaluée.

> [!note] La courbe choisie, et pourquoi
> `25 × √(1 − t)`. Elle respecte les deux bornes **exactement**, ce qu'une exponentielle ou
> un logarithme inverse ne font pas sans un `clamp` de plus — et elle « tient puis
> s'effondre », ce qui est le sens d'amorti. Si tu préférais une autre forme, c'est le
> générateur `tools/schemas/rde03_degats_amortis.py` qu'il faut changer : il produit la
> figure **et** la table, donc les deux resteront d'accord.

## Le projet companion reste à décider

Le **contenu** est écrit : le programme de départ est dans la feuille — il lit une distance,
affiche les dégâts, et porte les deux fonctions vides avec l'appel de l'une commenté, comme
tu le demandais. Ce qui manque, c'est le **dépôt** : la convention de ce vault veut un dépôt
public `<CODE>_<Nom>` plus un sous-module ici, et je ne crée pas de dépôt public sans que tu
le dises. Les trois cases correspondantes restent donc ouvertes.
