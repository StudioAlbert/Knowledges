---
slides: "[[01 courses/slides/Theory/TC-FT-RDE-02 - Équations et inéquations]]"
exercices: "[[01 courses/exercises/Theory/TC-FT-RDE-02 - Équations et inéquations]]"
---
- [x] Compléter slides selon slides originels et sources complémentaires
- [x] Proposer exercices de resolution
	- [x] sujets : equations du premier degre et les diverses methodes de résolution
		- [x] factorisation
		- [x] identites remarquables
	- [x] un quizz a faire pendant le cours + un quizz plus complet a faire a la maison
	- [x] La correction propose une solution +un tip sur la methode a utiliser
- [x] Somme et produit des racines : Trouver sources pedagogiques
- [x] Tableau de signes : Un produit ou un quotient change de signe en ses racines, et le tableau évite de tâtonner. => Expliciter


### Sources en complément
https://classroom.khanacademy.org/teacher/library/fr/math/all/algebra/one-variable-linear-equations/alg1-intro-equations/a/introduction-to-equations

https://classroom.khanacademy.org/teacher/library/fr/math/all/algebra/one-variable-linear-equations/alg1-one-step-add-sub-equations/a/solving-one-step-addition-and-subtraction-equations

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
