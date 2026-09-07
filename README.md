# Knowledges

Teaching vault for the **C++** and **Unity** Games Programming modules at
[SAE Institute Geneva](https://www.sae.edu/), maintained by Sébastien Albert.

It holds the lectures, exercises and project briefs of the curricula. Everything is plain
Markdown with YAML frontmatter — the frontmatter *is* the source of truth, so the vault
stays readable and scriptable outside Obsidian.

Prose in this README is English; note titles and frontmatter values are kept verbatim in
French, because they are identifiers used by links.

Released under the [MIT License](LICENSE).

## Requirements

- **[Obsidian](https://obsidian.md/)** with the community plugins listed in
  [`.obsidian/community-plugins.json`](.obsidian/community-plugins.json):
  - `slides-extended` — **required**, lectures are reveal.js decks. It succeeds
    `obsidian-advanced-slides`, whose files are still in `.obsidian/plugins/` but which
    is no longer enabled; both read the same deck syntax
  - `obsidian-excalidraw-plugin`, `code-files`, `card-board`, `obsidian-git`

## Clone

`00 widgets` and the two C++ companion projects are git submodules
(see [`.gitmodules`](.gitmodules)), so clone recursively:

```bash
git clone --recurse-submodules https://github.com/StudioAlbert/Knowledges.git
```

The exam repositories under `01 courses/exams/C++/` are **not** submodules — they are
gitignored working clones of separate SAE-Geneve repositories, and are cloned by hand
when needed.

## Layout

| Folder | Contents |
| --- | --- |
| `00 images` | Slide backgrounds and screenshots referenced by the decks |
| `00 templates/css` | `sae_styles.css` (the deck theme), `temps_travail_perso.css` |
| `00 widgets` | Submodule → [StudioAlbert/widgets](https://github.com/StudioAlbert/widgets) — interactive HTML widgets published on GitHub Pages |
| `01 courses` | The teaching material, organised by category — see below |
| `02 Notes` | Personal notes (bio, work-time logs) — not teaching material |

## How `01 courses` is organised

**Category first, subject second.** Each folder under `01 courses/` is a kind of
material; inside it, one folder per subject — `C++`, `Unity`, `Theory`, `AI`, `PCG`,
`Game programming - Généralités`.

| Path | Role |
| --- | --- |
| `lectures/<subject>/` | Lectures, one note per lecture, rendered as Slides Extended decks — and the 69 session notes, next to the deck they slice |
| `exercises/<subject>/` | Exercise sheets, attached to a lecture, no hours |
| `resources/<subject>/` | Support material (Git, coroutines, …), no hours |
| `projects/<subject>/` | Project and formative briefs |
| `_drafts/<subject>/` | Unfinished lectures — outside the curriculum until promoted to `lectures/` |
| `exams/<subject>/` | Exam material; the working clones themselves are gitignored |
| `companion projects/<subject>/` | Submodules — runnable code that goes with a lecture |
| `_source/<subject>/` | Raw material kept from an import |
| `_archive/` | Older content, frozen as it was |

Note titles are unique across the vault, so wikilinks are written bare — `[[C++ Builder]]`,
not a path. Moving a note between categories does not break them.

### The lecture note

**`type: course`** — one lecture, rendered as a Slides Extended deck. See
[`lectures/C++/10 - SFML.md`](01%20courses/lectures/C%2B%2B/10%20-%20SFML.md):

```yaml
---
title: SFML
type: course
status: Backlog
subject: C++
duration_h: 3
bloc_gsda: SFML et Box2D
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
---
```

**Sizing rule.** One lecture is worth **3 h**, unless the deck states its own duration
(Builder 2 h, Serialisation 1 h, Behaviour Tree 4 h). Exercises, formatives and resources
belong to the curriculum but carry no hours.

### `bloc_gsda`

The department vault `_GSDA_Tech_Vault` groups teaching into **blocks**. A note names the
block it belongs to in `bloc_gsda`, as plain text — never a wikilink, there is no block
note in this vault — and the kanban lays out its lanes from it.

It is deliberately **empty on 49 notes**. Those decks were filed under an older, home-made
block scheme whose names have no GSDA counterpart, and several of them duplicate GSDA
material. An empty `bloc_gsda` marks a note still to be placed; the duplicates get sorted
out by hand.

## Teaching sessions

The department vault (`_GSDA_Tech_Vault`, a sibling checkout) plans teaching in **1 h
sessions**; this vault holds **3 h decks**. 69 session notes bridge the two — one per hour
Sébastien Albert teaches in 2026-2027 (55 in module 1, 14 in module 2) — each saying what
to prepare, from which deck, and how far along it is.

They live in `lectures/<subject>/`, **next to the deck they slice**: 30 in `C++`, 20 in
`Theory`, 19 in `Unity`. The filename carries the department's hierarchical code,
`<MINOR>-<SPECIALISATION>-<BLOCK>-<NN> - <Title>.md`
(`GPR-CF-EDC-02 - Gestionnaires de paquets.md`), which is what tells a session apart from a
deck at a glance. Every segment is read from `_GSDA_Tech_Vault`; none is invented here.

A session carries `type: seance` and **no** `duration_h` — an hour is not a lecture and must
not enter the hour totals. They appear on the `01 courses/__course base.base` kanban, in
the *To prepare* column.

They were generated once from `_GSDA_Tech_Vault` and are now **maintained by hand**: there
is no script left to refresh them, so a change on the department side has to be carried
over manually.

See [`01 courses/Séances GSDA 2026-2027.md`](01%20courses/S%C3%A9ances%20GSDA%202026-2027.md).

## The kanban

[`01 courses/__course base.base`](01%20courses/__course%20base.base) is the one Obsidian
view of the vault. It picks up every note in `lectures/` except the `type: section` sub-notes, columns
them by `status` (*Backlog*, *To prepare*, *Ready*, *Done*), groups them by `projet` and
lays out lanes by `bloc_gsda`.
