---
title: GPR-CF-GTE-02 - Branches et intégration
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Git et Travail en Équipe
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: true
---

# Branches et intégration
<!-- .slide: class="title" -->
## GPR-CF-GTE-02

<small>Travailler à côté, puis revenir</small>

Note:
**Plan de séance — à développer.** Chaque slide porte son titre et sa phrase directrice ;
les widgets et schémas sont décrits, pas encore écrits. `publish: false` tant que le deck
n'est pas rédigé.

---

## Objectifs

- Ouvrir une branche
- Changer de branche
- La ramener dans `main` par merge ou par rebase, 
- Résoudre un conflit sans casser le travail des autres.

**Prérequis :** dépôt, commit, remote — [[01 courses/slides/C++/GPR-CF-GTE-01 - Principes et premier dépôt|GPR-CF-GTE-01]].

---

## Pourquoi on ne travaille pas dans `main`

Une branche isole un travail en cours du reste du projet

- pouvoir travailler de facon isolée
	- on ne casse pas le projet
	- ce qui se passe dans les autres branches
- On conserve la possibilité de commit
---
## Bonnes pratiques

- une branche par fonctionnalité :
	- Nouveau niveau
	- Nouveau systèmes : economie, armes, sauvegard
- une branche par version :
	- alpha, beta, V1, V2
- une branche par departement
	- prog, graphique, level design


---

## Où pointe `HEAD`

Une branche n'est qu'une étiquette sur un commit ; `HEAD` dit sur laquelle vous êtes.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/git_graph_widget.html#libre" data-background-interactive -->

Note:
Widget — onglet « Bac à sable ». `switch -c saut-double`, deux « ajouter un commit » (les
libellés proposés suivent la branche), `switch main`, un commit : seule l'étiquette de la
branche courante avance. Créer une branche ne copie rien — c'est une étiquette de plus.
Le même bac à sable sert à montrer `merge` (fast-forward ou commit de fusion) et
`rebase` pendant les deux slides suivantes. Repli : ouvrir
00 widgets/_widgets/git_graph_widget.html localement.

---

## Merge : garder les deux histoires

Le merge fabrique un commit de plus qui joint les deux lignes, et ne touche à rien de ce qui existait.

Note:
Démonstration dans le bac à sable (slide widget précédente) : fusionner une branche dont
`main` n'a pas bougé → fast-forward ; puis une branche dont `main` a bougé → commit de
fusion à deux parents. C'est ce que les élèves verront à l'étape 4 de l'atelier.

---

## Rebase : réécrire la sienne

Le rebase rejoue vos commits au-dessus de `main` : l'histoire devient linéaire, mais ce sont de nouveaux commits.

Note:
Démonstration dans le bac à sable : lire les hash de la branche, « rebase main », relire —
même message, nouveaux hash ; les anciens commits restent en pointillés (case « commits
abandonnés »). C'est l'argument de la slide suivante. Comparaison statique, commandes à
l'appui : onglet « Merge ou rebase ».

---

## La règle qui évite les drames

On ne rebase jamais une branche que quelqu'un d'autre a déjà récupérée.

Note:
Question naturelle de la salle : « comment je sais qu'elle a été
récupérée ? » — réponse sur les deux slides suivantes. En bref : Git ne
peut pas le savoir, alors on raisonne sur ce qui a été **poussé**.

---

## Savoir si une branche a pu être récupérée

- Git ne sait pas qui a fait un `fetch` : on raisonne sur ce qui est **poussé**
- `git branch -r` : la branche existe sur `origin` → elle est partagée
- `git branch -vv` : `ahead 2` → ces 2 commits-là ne sont **que chez vous**
- sur GitHub : une pull request ouverte, un fork, un collaborateur → partagée

Note:
Règle pratique à donner : ce qui est poussé est public. On peut rebaser
librement les commits « ahead » (pas encore poussés) ; tout ce qui est
déjà sur `origin` ne se réécrit qu'après accord de l'équipe.
Sur GitHub : onglet *Branches* (qui l'a poussée, quand), *Insights →
Network* (qui a des forks et des branches qui en partent).

---

## Les vérifier, en commandes

Avant de réécrire, on regarde ce qui n'existe que chez soi.

```bash
git branch -vv
# * feature/mines  0b627ce [origin/feature/mines: ahead 2] Son de l'explosion

git log --oneline origin/feature/mines..feature/mines
# 0b627ce Son de l'explosion      ← pas encore poussés : rebase sans risque
# 95c348e Explosion

git push --force-with-lease       # refuse si quelqu'un a poussé entre-temps
```

Note:
Sorties vérifiées sur un dépôt de test. `A..B` = les commits de B qui ne
sont pas dans A. `--force-with-lease` plutôt que `--force` : si la branche
distante a bougé depuis votre dernier `fetch`, le push est refusé au lieu
d'écraser le travail de l'autre.

---

## Merge vs Rebase

Mêmes commits, même contenu final : seule la forme de l'histoire change.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/git_graph_widget.html#compare" data-background-interactive -->

Note:
Widget — onglet « Merge ou rebase », statique : même départ à gauche et à droite, avec
sous chaque graphe les commandes qui l'ont produit. À gauche la bifurcation reste visible
avec son commit de fusion ; à droite l'histoire est une ligne, main a avancé en
fast-forward, et les anciens commits réécrits restent en pointillés.

---
## Un conflit n'est pas une erreur

Git s'arrête quand deux branches ont modifié les mêmes lignes : il demande un arbitrage humain.

---

## Résoudre un conflit

On garde ce qui doit vivre, on supprime les marqueurs, on teste, puis on commit la résolution.

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/git_conflict_widget.html#choisir" data-background-interactive -->

Note:
Widget — quiz en 7 situations, à faire avec la salle. Pour chaque onglet : faire voter
(HEAD / la branche / les deux / réécrire) **avant** de toucher au fichier, révéler, puis
résoudre et tenter le commit — il est refusé tant que la résolution ne compile pas.
1 Équilibrage (`MAX_ATTEMPTS`, l'étape 5 de l'atelier) → un seul côté ;
2 Deux ajouts → les deux ; 3 Même bug, deux fix → un seul, peu importe ;
4 Deux includes → les deux ; 5 Deux conditions → réécrire ;
6 Renommer + modifier → réécrire ; 7 Un texte → un seul, décision de design.
Message : un conflit n'a pas de bouton « bonne réponse », il faut comprendre ce que
chaque côté voulait faire.

---

## Pull request et revue

- une PR **demande** de fusionner une branche dans `main` — sur GitHub, pas en local
- elle montre le **diff**, garde la **discussion**, et peut lancer des vérifications
- un relecteur commente, demande des changements, ou **approuve**
- on ne fusionne qu'après approbation, avec le bouton *Merge pull request*

Note:
La PR transforme l'intégration en conversation : on propose, on relit, puis on fusionne.
Personne ne pousse directement sur `main` — dans beaucoup d'équipes, GitHub l'interdit
même (branche protégée).

---

## Le cycle d'une pull request
<!-- .slide: class="schema" -->

On boucle entre revue et correction jusqu'à l'approbation, puis GitHub fusionne.

![[gte02_pull_request.svg]]

Note:
Chaque nouveau `git push` sur la branche met la PR à jour : pas besoin d'en rouvrir une.
Après la fusion, GitHub propose *Delete branch* — le faire, la branche a servi.

---

## Ouvrir une PR, en commandes

Tout se prépare en local ; GitHub propose la PR dès que la branche est poussée.

```bash
git switch -c feature/mines
git commit -am "Pose des mines sur la plage"
git push -u origin feature/mines
# GitHub affiche « Compare & pull request » : titre, description, relecteur

# après une remarque du relecteur :
git commit -am "Renomme placeMine en buryMine"
git push                    # la PR se met à jour toute seule
```

Note:
Variante en ligne de commande avec la CLI GitHub (`gh`, à installer) :
`gh pr create --base main --title "Pose des mines" --body "…"`.
Dans un fork (l'atelier), la PR peut viser `main` du fork ou le dépôt d'origine : bien
vérifier la base en haut du formulaire.

---

## Relire une PR

- onglet ***Files changed*** : tout le diff, fichier par fichier
- le **+** dans la marge : commenter une ligne précise
- ***Review changes*** : *Comment*, *Approve* ou *Request changes*
- on relit le **code**, pas la personne : une question vaut mieux qu'un ordre

Note:
Exemples de bons commentaires : « Que se passe-t-il si la plage fait 1 × 1 ? »,
« Ce 8 pourrait venir de GameConfig ? ». Le relecteur n'est pas là pour réécrire, mais
pour qu'une deuxième paire d'yeux ait vu chaque ligne avant `main`.

---

## Une bonne PR

- **une** intention : une fonctionnalité ou un correctif, pas les deux
- **petite** : quelques centaines de lignes au plus, sinon personne ne relit vraiment
- un titre et une description qui disent **quoi** et **pourquoi**
- à jour avec `main` (rebase avant de demander la relecture), et elle compile

Note:
Le bouton de fusion propose trois modes : *Create a merge commit* (le merge du cours),
*Squash and merge* (tous les commits en un seul), *Rebase and merge* (le rebase du
cours). Lien direct avec « Merge ou rebase ».

---

## Atelier — 20 min

Par binôme sur **Chasse au trésor** : un fork partagé, un fix et une fonctionnalité sur deux branches, un merge propre — puis un conflit à résoudre.

Note:
Énoncé complet : [[01 courses/exercises/C++/GPR-CF-GTE-02 - Branches et intégration|GPR-CF-GTE-02 — Atelier]].
Dépôt : StudioAlbert/GPR_CF_GTE_02_ChasseAuTresor. En classe, viser l'étape 4 ; l'étape 5
(conflit) se termine à la maison.

---

## À retenir

Une branche par intention, un rebase avant de proposer, un merge pour intégrer — et jamais de réécriture sur ce qui est partagé.

---

## Questions ?
