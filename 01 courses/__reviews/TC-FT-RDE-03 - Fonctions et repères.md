---
slides: "[[01 courses/slides/Theory/TC-FT-RDE-03 - Fonctions et repères]]"
exercices: "[[01 courses/exercises/Theory/TC-FT-RDE-03 - Fonctions et repères]]"
---
- [x] Compléter slides essentiellement avec exemples visuels

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
