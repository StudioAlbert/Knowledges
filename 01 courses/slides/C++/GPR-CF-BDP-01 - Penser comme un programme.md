---
title: Penser comme un programme
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Bases de la Programmation
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
manual_order: 9
---

# Penser comme un programme
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

### C'est quoi programmer ?

<small>Module 4FSC0PF001 · Introduction to Games Programming</small>

Note:
Première séance du module. On commence par le cadre — règles, méthode de
travail, outils — puis on entre dans le langage : types, opérations,
fonctions, et enfin les structures de contrôle. À la fin de la séance,
vous avez de quoi écrire un petit jeu en console.

---
## Vous allez apprendre à…
<!-- .slide" -->

- les bases de la programmation C++
- les maths : algèbre, booléenne
- la programmation orientée objet
- faire un jeu : **space shooter**

---

## Rôle au sein d'une équipe
<!-- .slide" -->

- Responsable du bon fonctionnement du jeu
- Responsable de la structure du projet de jeu
- Imposer certaines contraintes aux artistes
- Coder en pensant que les autres membres, qui ne savent pas coder, puissent modifier le jeu
- Documenter

Note:
Le point sur les artistes est le plus mal compris : imposer des
contraintes n'est pas un caprice de programmeur, c'est ce qui rend le jeu
tenable techniquement. Et coder pour les non-codeurs, c'est ce qui décide
si l'équipe peut itérer sans vous.

---

## La documentation
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Documenter avec les sections :

- Scénario / GDD
- Analyse
- Conception
- Réalisation

Faites des schémas **avant** d'implémenter. Cela aide pour discuter avec nous, et pour votre documentation.

---

## Pipeline de développement
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

1. Bière
2. Idée de base
3. **Pré-production** — mise en place des documents, prototype, vertical slice
4. **Production** — mise en place des assets, ajouter toutes les features
5. **Feature freeze** — finition, plus de nouvelle feature
6. Bière

---

## Les sauvegardes de projet
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- Utiliser des outils de versioning comme **git**
- Les projets sont à rendre sur GitHub, donc vous allez devoir vous y faire !
- Ne surtout pas utiliser Dropbox ou système du genre. Ni ZIP, ni RIEN !
- Sauvegarder à distance

On n'accepte pas les excuses « j'ai oublié mon projet à la maison » ou « mon chien a mangé mon disque dur ».

---

## Faites des jeux hors cursus
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Faites des mini-jeux / prototypes régulièrement hors de l'école.

Faites des **Game Jams** !

- [itch.io/jams](https://itch.io/jams)
- Global Game Jam (mondial, en localisation)
- Ludum Dare (mondial, online)
- SAE gamejam (Genève)
- Lvlupgamejam (Fribourg)

---

## Veille technologique
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Raisons de faire de la veille :

- la technologie est en permanente évolution
- marché compétitif
- nouveaux outils permettant la productivité
- dépréciation des outils
- vous êtes toujours un ignorant ⇒ connaissez vos faiblesses

Regarder les nouveautés au moins une fois par semaine.

---

## Veille créative
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Analyser la création des autres. Découvrir des idées qu'on n'aurait pas eues soi-même :

- par inspiration
- par mélange
- par opposition

Faire de la veille sur les jeux — mais **pas que** sur les jeux : cinéma, BD, exposition, actualités, nature, industrie.

---

# Penser comme un programme
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

---

## C'est quoi la programmation ?
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Contrôle sur un ordinateur.

Mais un ordinateur, c'est bête…

---
## Recette de cuisine
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```
400 g de sucre
Mixer dans le bol
???
Manger
```

Note:
La blague du « ??? » est le cœur de la diapo : une recette incomplète ne
se laisse pas exécuter. Un ordinateur ne comble aucun trou tout seul.

---

## La programmation, c'est comme les Legos
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- Tout ce que vous apprenez en cours est utile
- Chaque exercice vous fait avancer
- Tous les jeux (réussis ou ratés) sont des expériences
- Il suffit de tout mettre ensemble

---

## Pseudocode
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```
Import GameDevTools
Using GameDevTool create Minecraft
```

… ou, plus raisonnablement :

```
Demander à l'utilisateur un nombre
Mettre le nombre au carré
Afficher le nouveau nombre sur la console
```

---

## Division des problèmes
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Créature A vs Créature B.

- Chaque créature a une **initiative** qui détermine qui commence
- Chaque créature a une valeur de **défense** et une valeur d'**attaque**

---

## Division des problèmes — pseudocode
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```
If Creature A has a greater initiative than Creature B, then
    We calculate the hit probability from Creature A offense
        against Creature B Defense
    We throw the dices.
    If the result of the dice is higher than the probability, then
        Creature B avoids the attack
    Else, if the result of the dices is lower than the probability, then
        Creature B receives damages
Else, if Creature B has a greater initiative than Creature A, then
    ....
```
