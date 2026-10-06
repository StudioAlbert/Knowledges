# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this
repository.

## What this repository is

An Obsidian vault of teaching material (C++ and Unity games programming, SAE Institute
Geneva), plus the small Node build that publishes part of it as a static site. There is no
application code to compile — the deliverables are Markdown notes, HTML widgets, and
generated SVG schemas. `README.md` is the long-form reference; read it before any
structural change.

**Language:** note titles, frontmatter values, headings and prose are **French**, and the
titles double as wikilink identifiers — never translate or "normalise" them. Commit
messages in the log are French and unaccented.

## Where the rules live

Each area carries its own `CLAUDE.md`, loaded when you touch a file there:

| Fichier | Couvre |
|---|---|
| `site-build/CLAUDE.md` | build et serve, contrat de publication, déploiement |
| `01 courses/slides/CLAUDE.md` | écriture des decks, classes de slide, limites de cadre |
| `00 widgets/CLAUDE.md` | widgets autonomes, inventaire, chemins |
| `tools/schemas/CLAUDE.md` | générateurs Python des figures SVG |
| `01 courses/__reviews/CLAUDE.md` | checklists de révision, kanban, métadonnées GSDA |

Procédure récurrente : la skill **`traiter-revisions`** (traiter le kanban Reviews de bout
en bout).

## Commands

Site statique (détail dans `site-build/CLAUDE.md`) :

```bash
cd site-build && npm ci && npm run build
```

Figures (une par script, détail dans `tools/schemas/CLAUDE.md`) :

```bash
python "tools/schemas/bdp06_std_string.py"
```

Companion projects are git submodules — clone with `--recurse-submodules`, and remember a
change inside one needs a commit there *and* a pointer bump here.

## Architecture — the session note is the hub

A teaching session is split across one file per kind of support, and the **session note in
`lectures/` is the centre**: it points to its slides, exercises and resources and says what
to prepare.

- **`01 courses/lectures/<subject>/`** — the 69 one-hour **session** notes
  (`type: seance`, carrying `code:`, `date_scheduled`, `classes`, `tache`), which
  centralise slides + exercises + resources for that hour, *plus* the legacy
  `type: course` decks not yet split into `slides/`. Sessions carry no `duration_h`: an
  hour is not a lecture and must not enter hour totals.
- **`01 courses/slides/<subject>/`** — the reveal.js decks themselves (`type: slides`).
  **This is what the site build reads**, so `publish: true` goes here, not on the session
  note.

A session, its deck and its exercise sheet share the **same filename**
(`<CODE> - <Titre>.md`) across `lectures/`, `slides/` and `exercises/` — that convention,
not a field, is what ties them together for a reader. Other categories under
`01 courses/`: `resources/`, `projects/`, `exams/` (gitignored working clones, not
submodules), `companion projects/` (submodules), `_drafts/`, `_source/`, `_archive/`,
`__reviews/`.

Titles are unique vault-wide, so wikilinks are historically bare (`[[C++ Builder]]`);
newer notes use the full path form (`[[01 courses/slides/C++/… |Slides BDP-06]]`). Match
whichever the file you are editing already uses.

## Specific instructions

Privilégiez les phrases concises et les explications par schéma. Proposez des **widgets** et
des **schémas** dès qu'un point s'explique mieux en image.

### Format d'une séance

1 h de cours + 20 min d'exercices ou d'atelier, terminés à la maison.

### Commits

Ne pas mentionner Claude comme co-auteur : pas de ligne `Co-Authored-By` ni de mention
d'outil dans les messages de commit.
