---
slides: "[[01 courses/slides/Theory/TC-FT-RDE-02 - Équations et inéquations]]"
exercices: "[[01 courses/exercises/Theory/TC-FT-RDE-02 - Équations et inéquations]]"
quizz_maison: "[[01 courses/exercises/Theory/TC-FT-RDE-02 - Quizz des dix équations]]"
---
- [ ] Ajouter graphique pour démonstration graphique du premier degré
- [ ] Séparer les différents quizz des exerices posés en texte = différentes pages
- [x] Compléter slides selon slides originels et sources complémentaires
- [x] Proposer exercices de resolution
	- [x] sujets : equations du premier degre et les diverses methodes de résolution
		- [x] factorisation
		- [x] identites remarquables
	- [x] un quizz a faire pendant le cours + un quizz plus complet a faire a la maison
	- [x] La correction propose une solution +un tip sur la methode a utiliser
- [x] Somme et produit des racines : Trouver sources pedagogiques
- [x] Tableau de signes : Un produit ou un quotient change de signe en ses racines, et le tableau évite de tâtonner. => Expliciter
- [x] Slide **a quoi ca sert dans un jeu ?** citer un seul exemple parabole de saut voir 2 paraboles une montante, une descendante
- [x] Quizz : le séparer en deux — un widget pour le cours, une page de l'onglet exercices pour la série maison
- [x] Widget du discriminant : pouvoir dézoomer le graphe à la molette
- [x] Atelier : fournir l'équation de la hauteur en question 1, les questions suivantes s'appuyant toutes sur cette formule
- [x] Slide **Ce qu'on a le droit de faire** : expliciter « élever au carré peut inventer des solutions »
- [x] Schéma du saut : exagérer encore la deuxième parabole
- [x] Feuille d'exercices, 1 *Combien de potions* : finaliser l'exemple avec des valeurs chiffrées
- [x] Feuille d'exercices : supprimer 2 *Factoriser*, 3 *Le temps d'impact*, 6 *Rayon contre cercle*
- [x] Feuille d'exercices : 4 *L'inéquation qui se retourne* part dans un quizz Inéquations
- [x] Feuille d'exercices : 5 *Le tir qui touche* remplacé par l'énoncé de l'atelier
- [x] Page de ressources : les formules `$…$` s'affichaient en LaTeX brut sur le site


### Sources en complément
https://classroom.khanacademy.org/teacher/library/fr/math/all/algebra/one-variable-linear-equations/alg1-intro-equations/a/introduction-to-equations

https://classroom.khanacademy.org/teacher/library/fr/math/all/algebra/one-variable-linear-equations/alg1-one-step-add-sub-equations/a/solving-one-step-addition-and-subtraction-equations

https://youtu.be/hG9SzQxaCm8

## Traité le 20.10 — à vérifier

**Deck**, 25 slides, de 15 titres sans contenu. Quatre temps : le premier degré, factoriser,
le second degré, les inéquations. Aucune slide hors cadre, 9 formules en KaTeX, aucune
erreur de rendu.

### Le quizz, comme demandé

`equations_quizz_widget.html`, deux séries derrière deux onglets :

| Onglet | Contenu |
|---|---|
| `#cours` | 5 équations — isoler, rassembler, identité `a²−b²`, produit nul, racine double |
| `#maison` | 10 équations — les mêmes méthodes, plus les deux carrés parfaits, le discriminant et la somme-produit |

On **tape** la réponse, on ne choisit pas dans une liste. Les valeurs sont comparées comme un
ensemble : `3 -1` et `-1 3` valent pareil, et `aucune` est accepté. La correction donne les
étapes **et** la ligne de méthode, qui est le vrai contenu — « identité remarquable »,
« produit nul, ne pas développer », « somme et produit, plus rapide que le discriminant ».

Testé : les dix réponses de la série maison validées dans des ordres mélangés, une fausse
réponse déclenche bien la correction.

### Le tableau de signes, explicité

Il a maintenant **deux** slides au lieu d'une phrase. La première pose le tableau en chasse
fixe — une ligne par facteur, la dernière ligne multiplie les signes. La seconde apprend à le
lire : on prend les colonnes où le produit est positif, et on écrit l'union d'intervalles.
La règle du quotient — racine du dénominateur **exclue** — est sur cette seconde slide.

### Somme et produit : sources trouvées

Trois, vérifiées, rassemblées dans une fiche publiée
[[01 courses/resources/Theory/TC-FT-RDE-02 - Ressources|Ressources — équations et inéquations]] :
le cours de Première de Paul Milan (lycée d'adultes), le chapitre Première spécialité du
CNRS, et des exercices corrigés chez digiSchool. Les trois donnent `S = −b/a`, `P = c/a`
sous condition `Δ ≥ 0`, et la réciproque `x² − Sx + P = 0`.

**Tes deux liens Khan Academy pointent vers `classroom.khanacademy.org/teacher/library/`** —
la bibliothèque enseignant, qui demande une connexion. Je ne les ai donc pas mis dans la
fiche des étudiants : j'y ai mis les pages publiques équivalentes de `fr.khanacademy.org`.
Les tiens restent ci-dessus, pour toi.

### Le widget du discriminant

`discriminant_widget.html` : trois curseurs, la parabole, Δ, les racines, et S et P affichés
en vis-à-vis pour que la vérification se voie. Quatre onglets — libre, et un par signe de Δ.
Le deck l'utilise **deux fois** : une fois en découverte sur la forme générale, une fois sur
`#aucune` pour le cas Δ < 0.

## Deux arbitrages

**1. Le quizz ne contient aucune inéquation.** Ta liste de sujets dit « équations du premier
degré et les diverses méthodes de résolution », et une réponse d'inéquation est un intervalle
— impossible à corriger automatiquement sans un analyseur. Les inéquations sont donc
traitées dans le deck et dans l'atelier, pas dans le quizz. Si tu les veux dedans, il faudra
passer en choix multiple pour ces questions-là.

**2. L'atelier est entièrement nouveau.** Le squelette proposait « calculer à quel instant un
projectile atteint sa cible ». Je l'ai écrit en quatre questions qui montent — l'équation, les
deux racines et leur sens physique, l'intervalle, puis le Δ négatif. La dernière question est
celle qui relie la séance au code. **Les réponses ne sont nulle part** : à toi de voir si tu
veux un corrigé.

## Hors périmètre

La feuille d'exercices reste un **overview** de six pistes. Le quizz couvre maintenant le
terrain des exercices 1 à 3.

## Deuxième passe, le 20.10 — à vérifier

25 slides, **aucune hors cadre**, aucune image cassée. Les quatre points de ta relecture sont
faits, et vérifiés sur le serveur de test.

### Un seul exemple de jeu, et c'est le saut

La slide *À quoi ça sert dans un jeu* ne liste plus quatre usages : elle en montre **un**,
en schéma — `rde02_saut_parabole.svg`.

C'est bien **deux paraboles**, comme tu le demandais, et pour une raison qui tient debout :
un saut de platformer agréable monte avec une gravité et retombe avec une plus forte. Le
dessin prend `g = 20` à la montée et `g = 40` à la chute :

| | |
|---|---|
| montée | `h(t) = 20t − 10t²` |
| chute | `h(t) = 10 − 20(t − 1)²` |
| au-dessus de 8 m | de **0,55 s** à **1,32 s**, soit 0,76 s |
| à 11 m | `Δ = −0,4` : il n'y arrive jamais |

Deux choses se voient d'un coup : les instants ne sont **pas** symétriques autour du sommet —
parce que les deux moitiés n'ont pas la même gravité — et le discriminant répond « jamais »
sans qu'on trace quoi que ce soit.

### Le quizz, séparé en deux

Sans dupliquer le widget : **en iframe, les onglets disparaissent et l'ancre choisit la
série**. Une seule règle CSS, et chaque endroit n'affiche qu'un quizz.

| Où | Ce qu'on voit |
|---|---|
| slide du deck, `#cours` | *Équation 1 sur 5*, pas d'onglet |
| [[01 courses/exercises/Theory/TC-FT-RDE-02 - Quizz des dix équations\|page de l'onglet Exercices]] | *Équation 1 sur 10*, pas d'onglet |
| ouvert en double-clic | les deux onglets, comme avant |

La page d'exercices est une note neuve qui embarque le widget en `<iframe>` — le build
réécrit déjà le chemin vault, **rien à changer côté `build.mjs`**. Elle porte aussi le
tableau de ce que les dix couvrent, et le rappel somme-produit pour se vérifier.

### La molette

`discriminant_widget.html` : la molette dézoome et rezoome, le **double-clic** revient au
cadrage de départ. Le pas de la grille suit — 1, 2, 5, 10 — pour que les graduations restent
lisibles quand on s'éloigne. Une ligne sous le graphe le dit.

Testé : trois crans en arrière font passer les graduations de `−6…6` au pas de 1 à `−10…10`
au pas de 2, et le double-clic restaure `−7…6`.

### L'atelier part de l'équation

La question 1 ne demande plus d'écrire la formule, elle la **donne** :
`h(t) = −5t² + 20t + 1,5`. Les trois questions suivantes s'appuient toutes dessus, et j'en ai
ajouté une quatrième qui fait varier la hauteur de départ — elle teste si le 1,5 m a vraiment
été compris comme un paramètre, pas comme un décor.

## Ce qui reste ouvert

**1. L'atelier n'a toujours pas de corrigé.** Même signalement qu'à la première passe. Les
réponses, si tu les veux : `t = 0,62 s` et `t = 3,38 s` ; au-dessus de 12 m entre les deux ;
et `v₀ < 14,5 m/s` environ le ferait manquer. À toi de dire si ça va dans la feuille ou si
ça reste au tableau.

**2. Deux feuilles d'exercices pour RDE-02.** L'overview de six pistes et la page de quizz
cohabitent dans l'onglet *Exercices*. C'est volontaire — mais l'overview n'est toujours pas
rédigé.

## Troisième passe, le 20.10 — tes annotations du deck

26 slides, aucune hors cadre, aucune image cassée.

### Élever au carré, expliqué sur sa propre slide

La puce disait « attention, ça peut inventer des solutions » et s'arrêtait là. Une slide la
démontre maintenant, en entier :

```text
√(2x + 3) = x   →   x² − 2x − 3 = 0   →   x = 3  ou  x = −1
x = 3  : √9 = 3        vrai
x = −1 : √1 = 1 ≠ −1   faux
```

La leçon est écrite en toutes lettres : le carré **perd le signe**, et toute solution obtenue
en élevant au carré se vérifie dans l'équation **de départ**. La note de présentation ajoute
que `−1` n'est pas une faute de calcul — le calcul est juste, c'est l'opération qui a ajouté
une racine.

### La chute est trois fois plus raide

`g` passe de 40 à **60** à la descente, contre 20 à la montée. Le script calcule désormais
les deux instants et la fenêtre au lieu de les porter en dur, donc la figure et ses chiffres
ne peuvent plus diverger : la fenêtre au-dessus de 8 m passe de 0,76 s à **0,71 s**, et le
second point à 1,26 s au lieu de 1,32 s.

### La feuille d'exercices, réduite à deux

| Avant | Après |
|---|---|
| 1 Combien de potions | gardé, et **chiffré** : 12 pièces d'entrée, 7 par potion, 100 en bourse |
| 2 Factoriser | supprimé |
| 3 Le temps d'impact | supprimé |
| 4 L'inéquation qui se retourne | parti dans le quizz |
| 5 Le tir qui touche | remplacé par l'énoncé de l'atelier |
| 6 Rayon contre cercle | supprimé |

L'exercice 1 ne s'arrête plus à l'intervalle : il demande le **nombre entier** de potions et
ce qui reste dans la bourse, avec le piège nommé — `n ⩽ 12,57` n'est pas une réponse.

### Le quizz des inéquations

Une troisième série dans le même widget, `#inequations`, et une
[[01 courses/exercises/Theory/TC-FT-RDE-02 - Quizz des inéquations|page dans l'onglet Exercices]].

Une inéquation se répond par un intervalle, donc **on choisit au lieu de taper** : quatre
écritures proposées, et la bonne est tirée au sort à chaque affichage — sinon elle serait
toujours la première. Huit questions : trois retournements de sens, deux tableaux de signes,
un quotient dont la racine du dénominateur est exclue.

Vérifié : les huit bonnes réponses valident, une mauvaise déclenche la correction, et la
position de la bonne varie bien d'une question à l'autre.

### Les formules ne s'affichaient pas sur le site

C'était un vrai trou, et pas seulement sur RDE-02 : **KaTeX n'était branché que sur les
decks**. Toutes les notes — ressources, exercices, séances — rendaient leurs `$…$` en LaTeX
brut.

`pageShell` charge maintenant KaTeX et son `auto-render`, depuis `/assets/katex` comme les
decks, et **seulement si la page contient un `$`**. Les délimiteurs sont ceux d'Obsidian, et
`pre` / `code` sont ignorés : un `$VAR` de shell n'est pas une formule.

Vérifié sur la page de RDE-02 : **six formules rendues, aucune erreur**.
