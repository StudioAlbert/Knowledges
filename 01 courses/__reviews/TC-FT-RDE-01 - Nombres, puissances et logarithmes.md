---
status: Ready
manual_order: -1
url_test: http://localhost:54573/theory/tc-ft-rde-01/
slides: "[[01 courses/slides/Theory/TC-FT-RDE-01 - Nombres, puissances et logarithmes]]"
---
- [x]  Slide Nombre premiers, decomposer la multiplication des nombres 1, 2, 3, 4, 5, 8, 13, 18, 19
- [x] Puissances, il y a t'il un plugin pour ecrire les formules de maniere plus exacte et plus precise ?
- [x] Exponentielle, Logarithme, trouver sources pédagogiques pour préciser
La note était vide : les consignes étaient écrites **dans le deck**, en italique. Je les ai
reprises ici pour qu'elles restent lisibles une fois le deck rédigé.

- [x] Citer les différents ensembles de nombres, avec définitions et notations
- [x] Trouver un titre à la slide sur les puissances négatives et les racines
- [x] Exponentielle : définition mathématique, ce qu'elle résout, schéma de la courbe
- [x] Logarithme : définition mathématique, ce qu'il résout, schéma de la courbe
- [x] Rédiger le reste du deck

## Deuxième passe, le 12.10 — à vérifier

### La décomposition

Nouvelle slide *Décomposer*, juste après *Nombres premiers*, avec tes neuf nombres :

```text
 1  =  (rien)            ni premier, ni composé : le produit vide
 2  =  2                 premier
 4  =  2 × 2             =  2²
 8  =  2 × 2 × 2         =  2³
18  =  2 × 3 × 3         =  2 × 3²
```

Le cas de **1** est celui qui paye : il n'est ni premier ni composé, c'est le produit de zéro
facteur. La note de présentation dit pourquoi en faire un premier casserait tout — on
pourrait écrire `18 = 1 × 2 × 3²` autant de fois qu'on veut, et l'unicité tombe.

### Les formules : oui, il y a un plugin — et il est maintenant actif

reveal en livre un, `plugin/math`, qui était déjà sur le disque sans être chargé. Il est
branché sur **KaTeX**, et KaTeX est **servi depuis le site**, pas depuis un CDN : j'ai ajouté
le paquet aux dépendances et le build recopie `node_modules/katex/dist` vers
`/assets/katex`. Le site reste autonome, comme avant.

Les délimiteurs sont ceux d'Obsidian — `$…$` et `$$…$$` — donc **une formule écrite dans le
vault s'affiche pareil des deux côtés**, sans double écriture.

Les six formules de RDE-01 sont passées de `<p class="formule">` à du LaTeX :

```latex
$$\log_a(x) = y \iff a^{y} = x$$
```

> [!check] Le risque était les `$` déjà présents dans les decks
> Trois decks en contiennent — un `'$'` dans un tableau C++ de BDP-05, des `${PROJECT_SOURCE_DIR}`
> dans EDC-03. Tous sont **dans des blocs de code**, et KaTeX ignore `pre` et `code` par
> défaut. Vérifié : rien n'a bougé ailleurs. `<p class="formule">` reste en place et sert
> toujours pour le reste.

### Les sources

Nouvelle fiche publiée : [[01 courses/resources/Theory/TC-FT-RDE-01 - Ressources|Ressources — exponentielle et logarithme]],
quatre entrées dans l'ordre où elles servent.

| | Pour quoi |
|---|---|
| **BetterExplained** — *An Intuitive Guide To Exponential Functions & e* | `e` comme taux de croissance continue, pas comme 2,718… |
| **3Blue1Brown** — *Essence of calculus*, chapitre sur `e` | dix minutes en images : la seule exponentielle égale à sa dérivée |
| **maths-et-tiques.fr** (Yvan Monka) | le cours terminale propre, en français, à donner aux étudiants qui révisent |
| **EPFL, Analyse I** | la construction par série entière, pour le jour où on la demande |

Toutes définissent le logarithme comme la **réciproque** de l'exponentielle, pas comme une
table de règles — c'est l'angle qu'avait déjà la séance, et ça la confirme.

**24 slides**, aucune hors cadre.

## Traité le 12.10 — à vérifier

**Deck rédigé**, 23 slides, de 15 titres sans contenu. Créé de zéro, comme l'annonçait la
note de séance : aucun support n'existait.

**Les ensembles de nombres** tiennent dans un tableau — nom, notation, ce qu'il contient, un
exemple — suivi de la chaîne d'inclusions `ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ`. J'ai ajouté **ℚ** à ta liste :
sans lui, le saut qui compte ne se voit pas — `1/3` n'a pas d'écriture décimale finie, et
c'est ce qui prépare RNLB-03. Une seconde slide fait le lien avec le code : quelle grandeur
va dans quel ensemble, et ce que `ℝ⁺` garantit.

**Le titre manquant** : *Négatif, fractionnaire : les mêmes règles*. La slide montre
`2^-3`, `8^(1/3)`, `8^(2/3)` et `a^(-1/2)`, et dit pourquoi on écrit tout en exposant —
un seul jeu de règles couvre les fractions et les racines.

**Exponentielle et logarithme** ont chacun leur slide de définition puis leur schéma :

| | Définition | Ce qu'elle résout |
|---|---|---|
| exponentielle | `f(x) = a^x`, `a > 0` | toute grandeur dont la croissance est proportionnelle à elle-même |
| logarithme | `log_a(x) = y ⟺ a^y = x` | les équations où l'inconnue est **en exposant** ; c'est la réciproque |

**Les deux schémas sont jumeaux** : même repère, mêmes six points (1, 2, 4, 8, 16, 32), axes
échangés. Posés l'un après l'autre dans le deck, la symétrie se voit toute seule. Mesurés à
978 x 323 dans le cadre. Pas de widget, comme demandé.

## À vérifier côté contenu

- **Les notations ℕ ℤ 𝔻 ℚ ℝ ℝ⁺** passent dans la police du deck, vérifié à l'écran. Le `𝔻`
  est le glyphe le plus rare du lot : si ton projecteur le rend en carré, dis-le et je passe
  la colonne en `D`.
- **L'atelier** demande quatre estimations sans calculatrice (atlas de textures, mipmaps,
  courbe d'XP, dichotomie). Les réponses ne sont nulle part : à toi de voir si tu veux un
  corrigé dans la note de séance.
- Le deck est en **`publish: draft`** et la séance est le **14.10** : le passage en `online`
  est à faire avant.
