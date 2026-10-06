---
name: traiter-revisions
description: Traiter les notes de révision en attente dans 01 courses/__reviews/ — choisir la prochaine note, passer le deck en publish draft, appliquer les corrections aux slides et exercices liés, cocher la checklist, passer le status et rebuilder le serveur de test. À utiliser quand on demande de traiter les révisions, de reprendre le kanban Reviews, ou de s'occuper d'une séance à préparer.
---

# Traiter les révisions

La base `01 courses/__reviews/Reviews.base` liste les révisions à apporter (colonnes Kanban :
Backlog, To do, To check, Ready).

## Choisir la note

Traiter les notes en statut **To do**, par ordre d'urgence :

1. les séances à venir d'abord — `date_scheduled` de la séance correspondante dans
   `01 courses/lectures/<matière>/` ;
2. à égalité, l'ordre dans le Kanban (`manual_order`).

## Traiter

La note de révision est une checklist ; ses notes `slides:` et `exercices:` en frontmatter
sont les fichiers à modifier.

**Avant d'éditer, passer le deck en brouillon** : dans le deck de `01 courses/slides/`,
mettre `publish: draft`. Tant qu'il est en `draft`, le deck n'est rendu que par le serveur de
test (bandeau « brouillon », `noindex`) et le build de production l'ignore — une révision en
cours ne peut donc pas atteindre le site des étudiants.

Si le deck était `online`, le passer en `draft` **le retire du site en ligne au prochain
déploiement** : c'est voulu pour une refonte, mais pour une correction mineure sur une séance
déjà donnée, demander à l'auteur s'il préfère la laisser `online` pendant la révision.

- Appliquer les corrections dans les notes liées, en respectant les règles d'écriture de
  `01 courses/slides/CLAUDE.md` (4 bullets max, un schéma ou un exemple de code seul sur sa
  slide).
- **Poser les questions nécessaires avant de trancher à la place de l'auteur** — c'est du
  matériel pédagogique, un arbitrage silencieux coûte plus cher qu'une question.
- Cocher dans la note de révision les cases traitées, au fur et à mesure.

## Clôturer

1. Passer le `status` de la note de révision à **To check**.
2. Rebuilder et lancer le serveur de test, qui inclut les brouillons :
   `preview_start {name: "knowledges-site-draft"}` (voir `site-build/CLAUDE.md`).
3. Renseigner l'URL de test dans le frontmatter de la note de révision.
4. **Laisser le deck en `publish: draft`.** Le passage en `online` n'est pas l'affaire de la
   révision : il appartient à l'auteur, après relecture du statut *To check*. Le signaler
   dans le compte rendu plutôt que de le faire.
5. Commiter — message en français non accentué, sans mention d'outil ni `Co-Authored-By`.

## Mettre en ligne (étape séparée, sur demande explicite)

Quand l'auteur valide une révision : passer le deck de `draft` à `online`, rebuilder en
production (`npm run build`, sans `--drafts`) pour vérifier que la séance apparaît bien, puis
commiter. Ne jamais enchaîner cette étape sur la précédente sans accord.
