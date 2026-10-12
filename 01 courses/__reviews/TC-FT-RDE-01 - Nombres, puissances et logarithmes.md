---
status: To check
manual_order: 5
url_test: http://localhost:56689/theory/tc-ft-rde-01/
slides: "[[01 courses/slides/Theory/TC-FT-RDE-01 - Nombres, puissances et logarithmes]]"
---
La note était vide : les consignes étaient écrites **dans le deck**, en italique. Je les ai
reprises ici pour qu'elles restent lisibles une fois le deck rédigé.

- [x] Citer les différents ensembles de nombres, avec définitions et notations
- [x] Trouver un titre à la slide sur les puissances négatives et les racines
- [x] Exponentielle : définition mathématique, ce qu'elle résout, schéma de la courbe
- [x] Logarithme : définition mathématique, ce qu'il résout, schéma de la courbe
- [x] Rédiger le reste du deck

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
