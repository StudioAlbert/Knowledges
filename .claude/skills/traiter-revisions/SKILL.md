---
name: traiter-revisions
description: Traiter les séances en attente dans le kanban __course base — choisir la prochaine note de 01 courses/lectures/, appliquer les corrections de sa fiche review aux slides et exercices liés, cocher la checklist, faire avancer le status et rebuilder le serveur de test. À utiliser quand on demande de traiter les révisions, de reprendre le kanban, ou de s'occuper d'une séance à préparer.
---

# Traiter les révisions

Le kanban `01 courses/__reviews/__course base.base` porte les **notes de séance** de
`01 courses/lectures/` (colonnes : Backlog, To prepare, To check, Ready, Post-mortem,
Post-mortem-done). C'est le seul kanban du vault, et son `status` **pilote aussi la
publication du site** — voir `site-build/CLAUDE.md`. Faire avancer une carte, c'est décider
de ce que voient les étudiants.

Les fiches de `01 courses/__reviews/` ne sont plus des cartes : ce sont les **checklists**
du travail à faire, atteintes depuis la séance par sa clé `review:`.

## Choisir la note

Deux files d'entrée, **dans cet ordre** :

1. **To prepare** — séances à venir, à préparer. On vide la colonne entière.
2. **Post-mortem** — séances déjà données dont la révision prépare l'an prochain.

Une séance à venir passe avant la préparation de l'année suivante. Dans chaque file,
**l'ordre du kanban** — `manual_order` croissant, et rien d'autre. L'auteur place ses cartes
et les ordonne : la colonne est déjà priorisée. La réordonner sur les dates de séance, ou sur
ce qui paraît urgent, lui retire ce contrôle.

Dérouler **toute** la colonne, pas la première note seulement. Et **relire le kanban après
chaque note** : l'auteur en ajoute, et en rouvre, pendant qu'on travaille.

Une séance sans `review:` n'a pas de checklist : demander à l'auteur ce qu'il attend plutôt
que de deviner.

## Traiter

La fiche pointée par `review:` est la checklist ; ses notes `slides:` et `exercices:` en
frontmatter sont les fichiers à modifier.

Rien à basculer avant d'éditer : le deck ne porte plus ni `publish` ni `status`, et c'est le
statut de la séance, inchangé pendant le travail, qui décide de sa visibilité. Une séance en
`To prepare` n'est pas publiée ; une séance en `Post-mortem` **reste en ligne pendant sa
révision**, donc une correction visible par les étudiants arrive dès le prochain
déploiement — le dire à l'auteur quand la correction est lourde.

- Appliquer les corrections dans les notes liées, en respectant les règles d'écriture de
  `01 courses/slides/CLAUDE.md` (4 bullets max, un schéma ou un exemple de code seul sur sa
  slide).
- **Poser les questions nécessaires avant de trancher à la place de l'auteur** — c'est du
  matériel pédagogique, un arbitrage silencieux coûte plus cher qu'une question.
- Cocher dans la fiche review les cases traitées, au fur et à mesure.

## Clôturer

1. Faire avancer le `status` de la **note de séance**, selon la file d'où elle vient :

   | File | Statut en fin de traitement | Effet sur le site |
   |---|---|---|
   | `To prepare` | **To check** | la séance passe en brouillon, visible du seul serveur de test |
   | `Post-mortem` | **Post-mortem-done** | la page reste en ligne, du début à la fin |

2. Rebuilder et lancer le serveur de test, qui inclut les brouillons :
   `preview_start {name: "knowledges-site-draft"}` (voir `site-build/CLAUDE.md`).
3. Renseigner `url_test` dans le frontmatter de la **note de séance** (le port change à
   chaque lancement).
4. **Ne pas passer la séance en `Ready` soi-même.** C'est la relecture de l'auteur qui
   tranche : depuis `To check`, il renvoie en `To prepare` pour un nouveau tour ou passe en
   `Ready` ; depuis `Post-mortem-done`, il rouvre en `Post-mortem` si de nouveaux points
   apparaissent. Le signaler dans le compte rendu plutôt que de le faire.
5. Commiter — message en français non accentué, sans mention d'outil ni `Co-Authored-By`.

`Ready` et `Post-mortem-done` publient en ligne **au prochain push** : il n'y a plus d'étape
de mise en ligne séparée, le statut suffit.
