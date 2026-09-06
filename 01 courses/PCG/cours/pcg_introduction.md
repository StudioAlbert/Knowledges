---
title: Procedural Generation — Introduction
type: course
status: Backlog
subject: PCG
duration_h: 3
bloc: "[[Fondamentaux de la génération procédurale]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
source_slides: https://docs.google.com/presentation/d/13eUqW3xYpEjPs_vNyqM1hh2HEseGHztCnkEp4oYbTiY/edit
---

# Procedural Generation
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Making things that make things

<small>Modules · patterns · randomness · generators</small>

Note:
This is the opening lecture of the PCG module. The goal is not to write a
generator today — it is to be able to *say what a generator is for* before
writing one. We start from modularity (the raw material), move to patterns
(the design vocabulary), then to the four levels of PCG in production, and we
finish on the first concrete tools: seeds, noise, partitioning, Markov chains.

---

## Agenda
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

1. **Modularity** — modules, gestalts, gestalt space
2. **Patterns & scenes** — the design vocabulary
3. **Four levels of PCG** — integral, drafting, modal, segmented
4. **Why, and why not** — the honest cost/benefit
5. **Random ≠ procedural** — seeds, noise, coherence
6. **First generators** — BSP, mazes, chunks, Markov chains

---

# Modularity
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
Everything procedural starts here. If you cannot name your modules, you have
nothing to generate with.

---

### Modules and gestalts

**Modularity** is the use of discrete units — *modules* — to assemble larger
structures, which we call **gestalts**.

A **gestalt space** is the set of all gestalts you can assemble from a set of
modules, through a given assembly mechanism.

<small>Change the modules *or* the assembly mechanism, and you get a different
space. Both are design decisions.</small>

Note:
Insist on the word *space*. A generator does not produce "content", it explores
a space you defined in advance. If the space is boring, no amount of randomness
will save the output.

---

### Order matters, or it does not

| Assembly | Order matters | Repetition |
| --- | --- | --- |
| **Permutation** | yes | with or without |
| **Combination** | no | with or without |

<small>Which one your generator produces changes the size of the gestalt space
by orders of magnitude — and changes how you must test it.</small>

Note:
Three room modules assembled in sequence: 3! = 6 permutations without
repetition, but 27 with repetition. This is the moment to connect back to the
combinatorics seen in the theory block.

---

### Mechanics as shared substrate

If certain combinations of modules assemble into *desirable* gestalts, there is
a definable relationship between those modules.

We can relate modules **indirectly**, using the language of the game's own
mechanics.

> A lance dealing bonus damage equal to your movement speed,
> and a pair of boots granting +20% movement speed.

<small>Neither module mentions the other. The mechanic — movement speed — is the
substrate that makes the pair meaningful.</small>

Note:
This is the key trick for procedural items. You do not enumerate good
combinations; you give modules a shared currency, and good combinations emerge.
The Borderlands weapon generator is exactly this.

---

# Patterns
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
From architecture to level design. The reference is Christopher Alexander's
*A Pattern Language* — the same book that gave software its design patterns.

---

### Patterns solve experiences

In *A Pattern Language*, a pattern creates a specific **life experience** for
the occupant. Patterns are interchangeable spatial ideas that solve problems of
human experience.

In PCG design, we use them to fix a **negative player experience**.

```text
   problem:  "architecturally static levels become
              predictable and lose player interest"
                          |
                          v
   pattern:  "Temporally Available Space"
              |- moving / disappearing platforms
              `- a guard patrolling in a stealth game
```

Note:
The workflow is: name the bad experience first, then reach for a pattern that
addresses it. Not the reverse. A generator built without a named problem
produces variety nobody asked for.

---

### Scenes as patterns

A good **scene** is an easily understood space that feels complete and
self-contained.

Binding patterns to scenes makes them tractable: one screen, or one room-sized
chunk of gameplay.

| Level | What you control | How |
| --- | --- | --- |
| **Local** | the pattern inside the scene | tightly — it can even be handcrafted |
| **Global** | how scenes connect | loosely — maze-like structures are enough |

Note:
This split is the single most useful production decision in the whole module.
Handcraft the rooms, generate the graph between them. Spelunky, Rogue Legacy and
Dead Cells all sit here.

---

# Procedural content generation
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

### Making things that make things

Four levels of commitment:

1. **Integral**
2. **Drafting content**
3. **Modal**
4. **Segmented**

Note:
These four levels are the practical taxonomy of the lecture. Ask students to
place a game they know in one of the four before you give the examples.

---

### Integral

Holistic use of procedural content. PCG is **core** to both the production and
the gameplay experience.

<small>Rogue · Spelunky · The Binding of Isaac · Darkest Dungeon · Steredenn ·
Elite Dangerous</small>

Note:
Remove the generator and the game stops existing. Highest payoff, highest risk:
you cannot fall back to handcrafted content late in production.

---

### Drafting content

PCG produces a **large amount of raw content**, which is then polished by hand.

<small>Skyrim — terrain and dungeon layouts drafted procedurally, then passed to
level artists.</small>

Note:
The generator is a tool for the content team, not for the player. Its output is
judged on how little cleanup it needs, not on its variety.

---

### Modal

Added as a **special mode** — an infinite mode, a DLC, a side activity.

<small>Lufia II and its Ancient Cave · procedural maps in Rust</small>

Note:
Cheap to scope, easy to cut. A good first PCG project for a student team.

---

### Segmented

A **part** of the game that is not core to the experience — so it can be swapped
for handcrafted content if the generator disappoints.

<small>The procedural weapons of Borderlands.</small>

Note:
This is the risk-managed version of Integral. Note how it echoes the "mechanics
as shared substrate" slide: Borderlands weapon parts relate through damage,
accuracy and elemental effects.

---

### When PCG is a bad idea

- **Quality assurance** — you cannot test a space you cannot enumerate
- **Time restrictions** — a generator is slower to build than the content it makes
- **Authored experience** — a scripted beat cannot be generated
- **Multiplayer** — everyone must see the same world, deterministically
- **Just random** — variety without meaning reads as noise
- **Overreliance** — infinite content, zero memorable content

Note:
Spend real time here. Most student projects fail on the second and the fifth
line. Ask them to estimate how many hours their generator costs versus how many
rooms they could have drawn by hand in that time.

---

### Why use PCG? — utilitarian

- Time saving, expandable content
- Replayability
- Reusable code, rules enforcement
- Modeling reality
- Scales and details impossible by hand
- Overcoming technical limitations

<small>These reasons are about **production**. They are measurable.</small>

Note:
The Elite Dangerous galaxy is the extreme case of "scales impossible by hand":
400 billion star systems shipped on a disc.

---

### Why use PCG? — unique

- Individual experience, new interaction modes
- Player input as generator input <small>(Mushroom 11)</small>
- Unpredictability, living systems
- Inhuman creativity
- Reflections and refractions of humanity
- Inspiration of infinity — and fun

<small>These reasons are about **experience**. They are not measurable, and they
are the interesting ones.</small>

Note:
"Inhuman creativity" is worth dwelling on: a generator regularly produces
something no designer would have drawn, and occasionally that thing is better.

---

### Roguelike — the Berlin Interpretation

The 2008 consensus definition, and a checklist of PCG in service of design:

- Random dungeons to increase replayability
- Permadeath, turn-based, **non-modal** <small>(every action always available)</small>
- Complexity enough to reach a goal in several ways
- Resource management to survive; peaceful options do not exist
- The map must be explored

Note:
Note how many of these are *not* about generation. The dungeon is random so that
the resource management stays tense — the generator serves a mechanic.

---

# Beyond levels
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
Quick tour, one slide each. The point is that "procedural" is a method, not a
level-design department.

---

### Procedural music

Instead of one finished track, program a system — FMOD, Wwise — that recombines
per-instrument stems at runtime.

<small>*We Happy Few*: 192 distinct musical combinations out of 4 tracks.</small>

Note:
The gestalt-space vocabulary from the modularity slide applies directly:
4 modules, an assembly mechanism, 192 gestalts.

---

### Procedural narration

Story generation is a module of its own — we only glance at it here.

<small>Dwarf Fortress · Caves of Qud</small>

Note:
Dwarf Fortress generates centuries of history before the player arrives; the
narrative is a by-product of a simulation, not of a text generator.

---

### Procedural art

> I have no artists, but I have got maths!

More seriously: not everything can be an animation. This is typically the
technical artist's job.

- Particle FX
- Grass and vegetation spawning <small>(Horizon Zero Dawn)</small>
- Post-processing FX

<small>Reference: `simonschreibt.de/game-art-tricks/`</small>

---

### Procedural animation

Movement computed rather than keyframed: procedural walk cycles, IK-driven
limbs, ragdoll blending.

<!-- TODO: figure d'origine, deck 01, slide ~19 (exemple animé) -->

Note:
Link forward to the steering behaviours lecture in the AI module — the same idea
applied to locomotion rather than to a rig.

---

# Warning
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Beginners start building their content generator **before knowing what their
content is**.

> Content *creation* is not a replacement for content *design*.

**The way out:** build a level by hand first, then look at it and decide what
deserves to be generated. Design your generator **by constraint**.

Note:
This is the slide to repeat at every project review of the module. "Show me the
handmade level your generator is trying to reproduce."

---

# Random is not procedural
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

| | |
| --- | --- |
| **Random** | noise — an anti-pattern |
| **Procedural** | randomness *constrained by patterns*, to produce interesting combinations |

<small>Do not use the word "random" to describe your generation. Please.</small>

Note:
The French original is blunt about this and it is worth keeping blunt. A student
who says "my level is random" has told you their generator has no design.

---

### Random numbers

Two everyday uses, two very different quality bars:

| Use | Question it answers | Failure mode |
| --- | --- | --- |
| **Dice roll** | which outcome, at what odds? | streaks feel unfair |
| **Random position** | where, in this space? | clumping and empty regions |

<!-- TODO: figure d'origine, deck 01, slides ~21-22 (illustrations dés / semis de points) -->

Note:
Show a uniform point scatter next to a blue-noise one. Uniform *is* correct and
*looks* wrong — which is the whole reason the next slide exists.

---

### Noise: Perlin

Coherent noise: nearby inputs give nearby outputs. That continuity is what makes
it usable for terrain, clouds, and any field that must look natural.

```text
   white noise            Perlin noise
   # . # . . # .          . . o # # o .
   . # . # # . #          . o # @ # o .
   # . . . # # .          o # @ @ # o .
   uncorrelated           locally smooth
```

Note:
Octaves and persistence come back in the terrain lecture. Here it is enough that
students see *why* white noise cannot be a heightmap.

---

### Global homogeneity

*Clockwork Empires*: a set of rules enforcing **global** coherence, so that the
locally generated pieces still read as one believable world.

<small>Local randomness plus a global rule set — the same local/global split as
the scene patterns.</small>

---

# Node based generation
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
Three classic space-carving families. These are the first generators students
actually write.

---

### Binary space partitioning

Divide the space in two, then divide the subspaces.

```text
   +---------------+   +-------+-------+   +---+---+-------+
   |               |   |       |       |   |   |   |       |
   |               | > |       |       | > +---+---+       |
   |               |   |       |       |   |       |       |
   +---------------+   +-------+-------+   +-------+-------+
        space              split 1              split 2
```

The split position can be **random**, **controlled** (multiples of a value), or
**exactly halved**.

<small>Rogue Legacy (2013)</small>

Note:
Rooms go in the leaves, corridors along the cut lines. The constraint
"multiples of N" is what keeps the rooms tileable — connect it back to
"design by constraint".

---

### Maze generation

> Game design disclaimer: big mazes are not fun.

Every mathematical tool from the theory block pays off here:

- **DFS / BFS** — carve a perfect maze, one long winding solution
- **Inverse Prim** — grow a spanning tree, more even branching

Note:
"Perfect maze" means exactly one path between any two cells. That property is
what makes the maze testable, and also what makes it boring. Loops are added on
purpose afterwards.

---

### Chunk-based generation

Cut the level into chunks and ask design questions before code questions:

- Does the level progress **up**, **down**, or **linearly**?
- What are the different chunks?
- What enemies, platforms and items live in each?

<small>Reference: the Spelunky generator walkthrough,
`tinysubversions.com/spelunkyGen/`</small>

Note:
The Spelunky grid is 4x4 rooms with a guaranteed path from entrance to exit
carved first, then everything else filled in. Guaranteed-path-first is the
pattern to remember.

---

# Markov chains
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

A set of **states** and **transitions**, each transition carrying a probability.

| Today | Tomorrow | Chance |
| --- | --- | --- |
| sunny | sunny | 90% |
| sunny | rainy | 10% |
| rainy | rainy | 50% |
| rainy | sunny | 50% |

Note:
Deliberately the simplest possible example. The state is "today's weather"; the
chain has no memory beyond it. That memorylessness is the Markov property.

---

### Building one

1. Define the blocks — from scratch, or extracted from a corpus with separators
2. Define the rules to transition from one block to the next

```text
   The --2--> Lord ---> of ---> Silver ---> Forest ---> END
    `---1---> Prince --'  |----> Golden ---> Lagoon
                          |----> Blue   ---> Castle
                          `----> Vanished
```

Note:
Read a couple of names out loud: "The Prince of Silver Castle", "The Lord of
Vanished Lagoon". The generator is three dictionaries deep and already produces
usable content.

---

### Two flavours of the same dictionary

**Equal probabilities**

```text
{ The      -> {Lord, Prince},
  Lord     -> {of},   Prince -> {of},
  of       -> {Silver, Golden, Blue, Vanished},
  Silver   -> {Forest, Lagoon, Castle},
  Forest   -> {END} }
```

**Weighted**

```text
{ The      -> {Lord (1), Prince (2)},
  of       -> {Silver, Golden, Blue, Vanished},
  ... }
```

<small>Weights are where the *design* lives: they are how you make a rare name
feel rare.</small>

---

### Explore

- `setosa.io/ev/markov-chains/` — visual, interactive
- `projects.haykranen.nl/markov/demo/` — text generation demo
- `github.com/chriscore/MarkovSharp` — a C# implementation to read

---

### Exercise

1. Generate a **weather sequence**
2. Generate an **enemy pool** under a generative budget

<small>Detailed briefs: [[pcg_exercices]]</small>

Note:
The budget constraint in exercise 2 is the interesting half: the chain proposes,
the budget disposes. It is the first constrained generator the students write.

---

# Seed generation
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

A **linear congruential generator**:

```text
   X(n+1) = (a * X(n) + b) mod m
```

Same seed, same sequence, same world — on every machine, every run.

<small>Reference: `pcg.wikidot.com/pcg-algorithm:linear-congruential-generator`</small>

Note:
Reproducibility is not a detail: it is what makes a generated bug reportable, a
run shareable, and multiplayer possible at all. Insist that every generator
written in this module takes a seed.

---

# Cellular automaton
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

The Conway Game of Life, repurposed: start from noise, then **smooth it** —
about five iterations is usually enough — and you get caves.

<small>`playgameoflife.com` — full treatment in
[[pcg_graph_cellular_automaton|the next lecture]]</small>

Note:
Teaser only. The next lecture derives the rule set and the connectivity problem
that comes with it: a cave system split into unreachable pockets is useless.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `rejbrand.se/rejbrand/article.asp?ItemIndex=425`
- `tinybirdgames.com/2018/04/10/adventures-in-procedural-generation/`
- `accidentalnoise.sourceforge.net/minecraftworlds.html`
- `devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413`
- `selfsame.itch.io/unitywfc`
- `www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/`

<small>The Amit Patel polygon map generation article is the one to read first.</small>
