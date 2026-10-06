---
status: Ready
manual_order: 2
slides:
  - "[[01 courses/slides/Theory/TC-FT-GVM-05 - Interpolation et courbes|Slides GVM-05]]"
exercices:
  - "[[01 courses/exercises/Theory/TC-FT-GVM-05 - Interpolation et courbes|Exos GVM-05]]"
url_test: http://localhost:60720/theory/tc-ft-gvm-05/
---
- [x] Slide Smoot start/stop, step proposer schema pour visualiser
- [x] Ajouter Projet Unity comme companion , ajouter fiche de ressources

- [x] Widget
	- [x] Visualisation au fil du temps de différentes fonctions
		- [x] y  = a x + b (non-clamped)
		- [x] sin
		- [x] fonction scie
	- [x] Présenter une fonction cyclique
		- [x] wt + phi (pouvoir modifier les paramétres)
	- [x] fonction Lerp
- [x] Un widget specifique permettant de démontrer l'ambiguité des rotations en 3D : Le Quaternion
- [x] Compléter le contenu

## Traité le 06.10 — à vérifier (séance du 08.10)

**Widget 1 — `fonctions_temps_widget.html`**, quatre onglets, une seule horloge pour les
quatre. Un graphe `valeur = f(t)` avec une tête de lecture, et **une bille sur une piste
A → B** pilotée par la valeur : quand la fonction sort de [0, 1], la bille quitte la piste
et le dit.

| Onglet | Ce qu'il montre | Paramètres |
|---|---|---|
| `#droite` | `y = a·t + b`, **non bornée** — rien ne la retient | a, b |
| `#cyclique` | `y = A·sin(ω·t + φ)`, bornée toute seule | A, ω, φ, + période affichée |
| `#scie` | `y = t/T − ⌊t/T⌋`, la partie décimale du temps | période |
| `#lerp` | `Lerp(A, B, t)` avec le paramètre fabriqué depuis le temps | clamp on/off |

Le fil rouge est celui que tu avais posé dans le plan : la droite **non clampée** d'abord,
le choix « borner l'entrée ou borner la sortie » ensuite, et le Lerp qui n'est que le cas
où l'on a clampé.

**Widget 2 — `quaternion_widget.html`**, l'ambiguïté des rotations 3D en trois démonstrations
(cubes en 3D fil de fer et faces triées, trièdre coloré, tout en SVG sans dépendance) :

- `#ordre` — **deux cubes, les mêmes trois angles, deux ordres d'application**. Le panneau
  affiche où part l'axe `z` dans chaque cas et mesure l'écart. À 90°/90°, les deux poses
  n'ont plus rien à voir.
- `#gimbal` — un **cardan à trois anneaux** monté comme le vrai. Le blocage n'est pas
  affirmé, il est **mesuré** : on ajoute 20° de lacet et on cherche le roulis qui annule.
  À tangage 90°, +20° de roulis donne un écart de **0,000** — le degré de liberté est
  perdu. À 0°, rien ne rattrape.
- `#slerp` — **angles interpolés contre slerp** : mêmes extrémités, chemins différents, et
  la norme du quaternion reste à 1,000 tout du long. Le code gère `q` et `−q` en prenant
  l'arc court.

**Deck** — 16 slides de plan → **33**, `publish: true`, construit sur ton ossature
(*Animer…*, *Aller de A à B*, *Clamp vs clamp*, *le clip d'animation*, *la fonction
cyclique*). Sections : *Une valeur qui change* / *Boucler* / *Interpoler* / *Tourner* /
*Les courbes*. Les sept slides de widget sont placées juste après la notion qu'elles
démontrent. La slide *Cas de la fonction cyclique*, restée vide, est développée.

**Images** : `Pasted image 20261006105059.png` et la capture de la courbe Unity étaient à
la **racine du vault**, donc invisibles pour le site. Elles sont dans `00 images/` sous
`gvm05_cycle_marche.png` et `gvm05_courbe_unity.png`.

> [!question] À trancher de ton côté
> - **La feuille d'exercices n'est pas touchée** : elle est encore à l'état d'overview. Ta
>   note ne demandait que les widgets et le contenu du deck — dis-moi si tu veux les
>   exercices rédigés pour jeudi.
> - **Le widget `easing_widget.html`** promis par le plan n'est pas construit : les quatre
>   courbes d'easing sont présentées en formules. Avec trois widgets déjà dans l'heure,
>   un quatrième m'a semblé de trop — à confirmer.
> - **33 slides pour 1 h**, dont 7 de widget. C'est dense ; si c'est trop, la section
>   *Les courbes* se déplace vers une séance suivante sans rien casser.

## Traité le 06.10 — le schéma des courbes

**`gvm05_easing.svg`** (`tools/schemas/gvm05_easing.py`), sur une nouvelle slide
*Quatre courbes, quatre sensations*, placée juste avant *Smooth start, smooth stop*.

La figure dit la même chose deux fois, et c'est le but :

- **à gauche** — les quatre courbes dans le carré unité : linéaire en pointillé gris,
  `t²` en rouge, `1 − (1 − t)²` en bleu, `t²(3 − 2t)` en vert ;
- **à droite** — quatre bandes A → B, onze instants **réguliers** sur chacune, et où la
  bille se trouve à chaque instant. Les points se serrent au départ pour *smooth start*,
  à l'arrivée pour *smooth stop*, aux deux bouts pour *smoother step*, et restent
  réguliers pour la droite.

C'est la bande de droite qui porte la leçon : **points serrés = lent, points écartés =
rapide**. La courbe de gauche n'est que la règle qui produit cet espacement. La note de
présentation propose de faire deviner à la classe quelle bande va avec quelle courbe avant
d'afficher les couleurs.

*Smooth arch* garde sa slide de formule : elle n'est pas monotone et aurait brouillé la
comparaison.
