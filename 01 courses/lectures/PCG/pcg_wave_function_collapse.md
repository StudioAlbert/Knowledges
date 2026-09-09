---
title: WaveFunctionCollapse
type: course
status: Backlog
subject: PCG
duration_h: 3
bloc_gsda:
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
source_slides: https://docs.google.com/presentation/d/1jMvp_3UypMXalr1Gdh5A-8Z5Z-_GjS-imo5ayihwJy0/edit
manual_order: 35
---

# Procedural Content Generation
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

### WaveFunctionCollapse

<small>Constraint solving disguised as a level generator</small>

Note:
Third lecture. Everything so far generated content by *building* it — carving,
smoothing, connecting. WFC does the opposite: it starts from "everything is
possible everywhere" and removes possibilities until one world remains. That
inversion is the whole lesson.

---

### Where it comes from

Developed by **Maxim Gumin**. Used in production by:

- **Oskar Stålberg** — Townscaper, Bad North
- **Caves of Qud**

It generates textures, landscapes, spaces and images **from a model** — that is,
from an example of what the result should look like.

<small>Playable demo: `oskarstalberg.com/game/wave/wave.html`</small>

Note:
The name is borrowed from quantum mechanics and is, strictly speaking, a
marketing accident: the algorithm is a constraint propagation solver. Say so
once, then use the borrowed vocabulary anyway, because the whole literature does.

---

# How it works
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

Two ingredients, and nothing else:

| | |
| --- | --- |
| **The modules** | the model — *what is possible* |
| **The slots** | the result — *what is still undecided* |

Plus the rules that bind them:

- **adjacency rules** — which module may sit next to which
- **min / max rules** — at least one exit, at most three towers
- **weighted repartition** — grass is common, a shrine is rare

Note:
Adjacency is the mandatory half; min/max and weights are what turn a tiling
demo into a level generator. Students always implement adjacency and stop there,
and their output is uniform mush.

---

### The slots hold every possibility

Each slot is initialised with the **full set of modules**: at the start,
anything can be anywhere.

```text
   +--------+--------+--------+
   | 12 mod | 12 mod | 12 mod |
   +--------+--------+--------+
   | 12 mod | 12 mod | 12 mod |     nothing decided yet
   +--------+--------+--------+
```

---

### Entropy

A slot has an **entropy**: how undecided it still is.

| Entropy | Meaning |
| --- | --- |
| max | every module is still possible |
| 3 | three modules remain |
| 0 | solved — one module left |

The goal is to bring every slot from max to 0, **without breaking a rule**.

<small>With `pi` the probability of each element of the domain, entropy is the
size of the domain when the `pi` are equal.</small>

Note:
Equiprobable entropy is just "how many options are left", which is all students
need to implement it. The weighted Shannon form matters only once you add
weighted repartition — mention it, do not derive it.

---

### Think of it as sudoku

| WFC | Sudoku |
| --- | --- |
| modules | the numbers 1 to 9 |
| slots | the 81 cells |
| adjacency rules | one number per row, per column, per box |
| collapse | writing a number in a cell |
| propagation | crossing that number out of the row, column and box |

<small>`sudoku-solutions.com`</small>

Note:
This analogy does more work than any diagram. Every student has solved a sudoku
by "this cell has only one candidate left" — that *is* the minimum-entropy
heuristic, discovered by hand.

---

# The algorithm
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

---

### Step 1 — define the rules, by hand

- Set up a structure holding your modules
- Write the adjacency rules yourself

<small>Total control, and unusable past about twenty modules: the rule table
grows as the square of the module count.</small>

---

### Step 1 — define the rules, automatically

- **Analyse the model** — a sample image, or a hand-built reference chunk
- Fill the structure from what the sample actually contains
- Derive the rules from observed adjacencies

<small>The generator now imitates an example instead of obeying a spec. This is
what makes WFC feel like magic in demos.</small>

Note:
Worth naming the trap: the generator can only produce what the sample allowed.
A sample with no dead end will never generate a dead end, and students spend
hours debugging a generator that is behaving exactly as instructed.

---

### Step 1 — socket based

The practical middle ground:

- each **border** of a module defines a **socket** (by pixel sampling, or by hand)
- two tiles may be adjacent on a side if their **sockets fit together**
- generate a module for each **rotation and symmetry**

```text
        Socket A              Socket A
     +-----------+         +-----------+
   A |           | A     A |           | B
     |           |         |           |
     +-----------+         +-----------+
        Socket A              Socket C

   these two fit on the left/right side only if A matches A
```

Note:
Sockets turn an O(n²) rule table into an O(n) labelling job, which is why every
practical implementation uses them. Rotations are the part students forget:
one authored tile usually becomes four modules.

---

### Step 2 — fill the grid

Every slot starts with every module. Everything is possible.

---

### Step 3 — observation

Make a guess:

1. Find the slot with the **least entropy** — the most constrained one
2. Pick one of its remaining modules **at random**, respecting the weights
3. That slot **collapses**: it now holds exactly one module

Note:
Least entropy first is not an optimisation, it is what keeps the algorithm from
painting itself into a corner. Picking a wide-open slot first almost guarantees
a contradiction later.

---

### Step 3 — propagation

Push the consequences outwards:

- eliminate, from **adjacent slots**, every module the guess has made impossible
- if a neighbour's possibilities changed, propagate to *its* neighbours in turn
- stop when nothing changes any more

```text
   collapse here
        |
        v
      [ X ]--> neighbour loses 4 modules
               |
               `--> its neighbour loses 1 module
                    |
                    `--> nothing changes, stop
```

Note:
Propagation is a work queue, and it is where all the runtime goes. It is also
where the contradiction shows up: a slot with zero remaining modules means the
guess was wrong.

---

### Step x — repeat

Observe, propagate, observe, propagate — until every slot has entropy 0.

**And when a slot reaches zero possibilities?** That is a *contradiction*. Three
strategies:

| Strategy | Cost | Used when |
| --- | --- | --- |
| restart from scratch | cheap to code | small grids |
| backtrack the last guesses | expensive | strict rule sets |
| relax a rule locally | design decision | shipping games |

<small>Live demo: `oskarstalberg.com/game/wave/wave.html`</small>

Note:
Original Gumin implementation simply restarts. Students should implement restart
first, measure the failure rate, and only then decide whether backtracking is
worth it. Usually it is not — loosening the rule set is.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- `github.com/mxgmn/WaveFunctionCollapse` — the original implementation
- `boristhebrave.com/2020/04/13/wave-function-collapse-explained/`
- `boristhebrave.com/2021/10/31/constraint-based-tile-generators/`
- `oskarstalberg.com/game/wave/wave.html` — the demo to play with in class
- YouTube, **DV Gen** — `watch?v=20KHNA9jTsE` and `watch?v=zIRTOgfsjl0`
- `selfsame.itch.io/unitywfc` — a Unity implementation to read

<small>Boris the Brave's "explained" post is the one to read before implementing.</small>
