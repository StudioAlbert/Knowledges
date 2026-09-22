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

The Unity and C++ companion projects are git submodules
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
| `00 widgets` | Interactive HTML widgets, embedded in the decks and published by the site under `/widgets/` |
| `01 courses` | The teaching material, organised by category — see below |
| `02 Notes` | Personal notes (bio, work-time logs) — not teaching material |
| `Excalidraw` | Editable sources of the hand-drawn schemas whose SVG lives in `00 images` |
| `site-build` | The static site generator — see [Building the site](#building-the-site) |
| `tools` | Scripts run by hand, outside any build — see [Schema generators](#schema-generators) |

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

## Building the site

Part of the vault is published as a static site (reveal.js decks + exercise pages) at
knowledges.studio-albert.com. **One script does everything:**
[`site-build/build.mjs`](site-build/build.mjs) — plain Node, no framework, no
intermediate step. Its header comment is the reference; the short version:

| | |
| --- | --- |
| **Reads** | `01 courses/slides/`, `exercises/`, `resources/`, plus `00 images`, `00 templates/css`, `00 widgets` (copied verbatim to `/widgets/`) and reveal.js from `node_modules` |
| **Writes** | `site-build/dist/` — gitignored, deployed as is |
| **Publishes** | one page per teaching session; a session appears **only** if its deck frontmatter carries `publish: true`. An exercise or resource attaches to it through `seances: [CODE, …]` or a filename starting with the session code. Any folder whose name starts with `_` is skipped, except under `00 widgets` |

```bash
cd site-build
npm ci          # Node >= 24, first time only
npm run build   # → site-build/dist/
npm run serve   # local preview of dist/
```

A deck references a widget by its vault path (`00 widgets/_widgets/x.html#tab`), which is
what Obsidian serves too; the build rewrites it to `/widgets/…`. An exercise can embed a
GitHub repository header and README through a fenced `github` block, fetched at build time
(`GITHUB_TOKEN` optional — 60 requests/h without it).

**Deployment** is [`.github/workflows/deploy-knowledges.yml`](.github/workflows/deploy-knowledges.yml):
every push to `main` touching the slides, exercises, images, widgets, deck CSS or
`site-build/` rebuilds the site and rsyncs `dist/` to the VPS, mirror-style (`--delete`,
so anything dropped into `/var/www/knowledges` by hand is wiped on the next deploy). It can
also be run from the Actions tab. Host and SSH key come from the `VPS_*` repository secrets.

## Schema generators

The figures drawn for the decks are **generated**, not drawn by hand, so that the SVG shown
in the slide and the Excalidraw file kept for later edits cannot drift apart. One script per
schema, under `tools/schemas/`, run by hand with Python 3:

```bash
python "tools/schemas/trg02_rapports_trigo.py"
```

Each script holds a single description of the figure and emits both outputs: the SVG into
`00 images/`, embedded by the slide as `![[name.svg]]` under
`<!-- .slide: class="schema" -->`, and the `.excalidraw.md` into `Excalidraw/`, which opens
in the Excalidraw plugin. Editing the Excalidraw copy does **not** update the SVG, and
re-running the script overwrites both — treat the script as the source.

Only the TRG-02 generator is kept so far; the `trg01_cas_*.svg` schemas were produced the
same way, but their script was not saved.
