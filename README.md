# Knowledges

Teaching vault for the **C++** and **Unity** Games Programming modules at
[SAE Institute Geneva](https://www.sae.edu/), maintained by Sébastien Albert.

It holds the lectures, exercises, project briefs and the pedagogical blocks that group
them. Everything is plain Markdown with YAML frontmatter — the frontmatter *is* the source
of truth, so the vault stays readable and scriptable outside Obsidian.

Prose in this README is English; folder names, note titles and frontmatter values are kept
verbatim in French, because they are identifiers used by links and scripts.

Released under the [MIT License](LICENSE).

## Requirements

- **[Obsidian](https://obsidian.md/)** with the community plugins listed in
  [`.obsidian/community-plugins.json`](.obsidian/community-plugins.json):
  - `slides-extended` — **required**, lectures are reveal.js decks. It succeeds
    `obsidian-advanced-slides`, whose files are still in `.obsidian/plugins/` but which
    is no longer enabled; both read the same deck syntax
  - `obsidian-excalidraw-plugin`, `code-files`, `card-board`, `obsidian-git`
- **Python 3** for `tools/sync_blocs.py` (standard library only, no install step)

## Clone

`00 widgets` and the two C++ companion projects are git submodules
(see [`.gitmodules`](.gitmodules)), so clone recursively:

```bash
git clone --recurse-submodules https://github.com/StudioAlbert/Knowledges.git
```

The exam repositories under `01 courses/C++/exams/` are **not** submodules — they are
gitignored working clones of separate SAE-Geneve repositories, and are cloned by hand
when needed.

## Layout

| Folder | Contents |
| --- | --- |
| `00 images` | Slide backgrounds and screenshots referenced by the decks |
| `00 templates/css` | `sae_styles.css` (the deck theme), `temps_travail_perso.css` |
| `00 widgets` | Submodule → [StudioAlbert/widgets](https://github.com/StudioAlbert/widgets) — interactive HTML widgets published on GitHub Pages |
| `01 courses` | The curricula: `C++`, `Unity`, `Theory`, `AI`, `PCG`, `Game programming - Généralités` |
| `02 Notes` | Personal notes (bio, work-time logs) — not teaching material |
| `tools` | `sync_blocs.py` |

## How a course is organised

Each course under `01 courses/` follows the same shape:

| Path | Role |
| --- | --- |
| `intro.md` | Entry point — explains the curriculum and embeds the index views |
| `blocs/` | Pedagogical blocks, one note per block |
| `cours/` | Lectures, one note per lecture |
| `exercices/` | Exercise sheets, attached to a lecture, no hours |
| `projets/` | Project and formative briefs |
| `ressources/` | Support material (Git, coroutines, …), no hours |
| `drafts/` | Unfinished lectures — outside the curriculum until promoted to `cours/` |
| `index_cours.base`, `index_blocs.base` | Obsidian table views over the two note types |

### Two note types

**`type: course`** — one lecture, rendered as a Slides Extended deck. See
[`cours/cpp_builder_lecture.md`](01%20courses/C%2B%2B/cours/cpp_builder_lecture.md):

```yaml
---
title: C++ Builder
type: course
duration_h: 2
bloc: "[[Patterns]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
---
```

**`type: bloc`** — a block grouping several lectures. See
[`blocs/Patterns.md`](01%20courses/C%2B%2B/blocs/Patterns.md):

```yaml
---
type: bloc
specialisation: "[[C++]]"
mineur: Games Programming
prerequis:
  - "[[Generique, prog fonctionnelle]]"
projet:
  - "[[City Builder]]"
cours: 9
---
```

Its body always has the same four sections: `## Objectifs`, `## Cours` (generated — see
below), `## Validation`, `## Liens`.

### Sizing rule

**One lecture is worth 3 h**, unless the deck states its own duration (Builder 2 h,
Serialisation 1 h, Behaviour Tree 4 h). Exercises, formatives and resources belong to the
curriculum but carry no hours. The `cours:` field of a block is the sum of the `duration_h`
of the lectures pointing at it.

## Keeping blocks in sync

`tools/sync_blocs.py` reads `bloc` and `duration_h` from the lectures and, for each note in
`blocs/`, recomputes the `cours:` total and regenerates the table in the `## Cours` section.

```bash
python tools/sync_blocs.py
```

| Command | Effect |
| --- | --- |
| `python tools/sync_blocs.py` | Sync every tracked course |
| `python tools/sync_blocs.py "C++"` | Sync one course only |
| `python tools/sync_blocs.py --check` | Write nothing; report divergences and exit 1 if any (usable as a pre-commit gate) |

> **Do not hand-edit the table between `<!-- cours:auto -->` and `<!-- /cours:auto -->`** —
> it is overwritten on the next run. Fix the lecture frontmatter instead.

The script walks `Unity`, `C++`, `PCG` and `AI` (its `COURS_SUIVIS` constant); `Theory`
blocks are maintained by hand.

## Index views

Each course ships two `.base` views, embedded in its `intro.md`:

- **`index_cours.base`** — all lectures. Views: *Progression* and *Par bloc* (grouped by
  block, hours summed), *Tout*.
- **`index_blocs.base`** — the blocks themselves, plus *Heures par bloc*, which recomputes
  the hour totals live to cross-check the script.

Two views act as gap-finders: **Sans bloc** lists lectures with no `bloc`, and
**À compléter** lists lectures with no `duration_h`.
