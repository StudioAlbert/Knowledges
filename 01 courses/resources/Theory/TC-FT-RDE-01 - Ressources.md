---
seances: [TC-FT-RDE-01]
---
# Ressources — exponentielle et logarithme

Quatre entrées, dans l'ordre où elles servent. Les deux premières construisent l'intuition,
la troisième donne le cours propre en français, la dernière le fond mathématique.

## 1 — L'intuition, par la croissance

[An Intuitive Guide To Exponential Functions & e](https://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/) — BetterExplained, Kalid Azad.

`e` n'y est pas « un nombre qui vaut 2,718… », mais **le taux de croissance d'un système qui
grandit en continu**. L'article part des intérêts composés et resserre les intervalles
jusqu'à la limite. C'est la meilleure réponse à « d'où sort ce nombre ».

Le même auteur sur les trois régimes :
[A Visual Guide to Simple, Compound and Continuous Interest Rates](https://betterexplained.com/articles/a-visual-guide-to-simple-compound-and-continuous-interest-rates/) —
utile pour montrer qu'un gain par palier et un gain continu ne donnent pas le même résultat.

Le hub du site sur le logarithme naturel : [BetterExplained — e, natural log](https://betterexplained.com/topics/e-natural-log/).

## 2 — L'intuition, en images

[What's so special about Euler's number e ?](https://www.3blue1brown.com/lessons/eulers-number) —
3Blue1Brown, série *Essence of calculus*.

Part d'une population qui double chaque jour et arrive à `e^x` comme **la seule exponentielle
égale à sa dérivée**. C'est le chapitre à montrer en classe si on a dix minutes.

## 3 — Le cours, en français

[maths-et-tiques.fr](https://www.maths-et-tiques.fr/) — Yvan Monka, académie de Strasbourg.

Le niveau terminale, écrit proprement, avec les vidéos qui vont avec. Le fichier
[Fonction logarithme népérien](https://www.maths-et-tiques.fr/telech/20LogTC.pdf) donne la
définition par réciprocité — `ln a` est l'unique solution de `e^x = a` — puis les propriétés
algébriques, la dérivée `1/x`, la concavité et les limites.

C'est la référence à donner aux étudiants qui ont besoin de revoir le programme du lycée.

> [!tip] Le point que ces sources partagent
> Toutes définissent le logarithme comme **la réciproque de l'exponentielle**, pas comme une
> table de règles. C'est l'angle de la séance : `log_a(x)` est l'exposant à mettre à `a` pour
> obtenir `x`, et les deux courbes sont symétriques par rapport à la première bissectrice.

## 4 — Le fond

[Analyse I — chapitre compléments](https://botafogo.epfl.ch/analyse-1/resources/pdfschapitres/chap-complements.pdf) — EPFL.

Définit l'exponentielle par sa série entière et en déduit le logarithme. **Trop formel pour
la séance**, mais c'est là qu'on va chercher une démonstration quand un étudiant la demande.

## Pour la séance elle-même

- les deux schémas du deck, `rde01_exponentielle.svg` et `rde01_logarithme.svg`, sont
  produits par `tools/schemas/` : mêmes six points, axes échangés ;
- une piste non suivie : un **jeu de société** sur les logarithmes, décrit dans une étude de
  l'[IREM de Grenoble](https://irem.univ-grenoble-alpes.fr/medias/fichier/123x1_1774606864373-pdf),
  où les élèves verbalisent le lien exposant / logarithme en jouant.
