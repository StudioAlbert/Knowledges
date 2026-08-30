---
title: Pathfinding
type: course
duration_h: 3
bloc: "[[Movement & Pathfinding]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
source_slides: https://docs.google.com/presentation/d/1zGklq_vMz7AfOr9viyWYpBTRgu9w01JAuIMjv65Z26U/edit
---

# AI Fundamentals
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Pathfinding

<small>BFS · weights · Dijkstra · heuristics · A\* · flow fields</small>

Note:
The densest lecture of the module, and the one students most often think they
already know. The through-line: every algorithm here is the previous one plus
one idea. BFS + weights = Dijkstra. Dijkstra + heuristic = A*. A* run backwards
for everyone at once = flow field.

---

## Agenda
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

1. **The graph** — cities, crossroads, roads
2. **BFS** — and why it is not enough
3. **Weights** — movement cost as a design tool
4. **Dijkstra** — worked by hand
5. **Heuristics** — the definition, and what it buys
6. **A\*** — worked on a grid, step by step
7. **Flow fields** — when everyone shares one destination

---

# The waypoint graph
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Build the vocabulary on something concrete — a road map:

| Map | Graph |
| --- | --- |
| **Cities** | nodes |
| **Crossroads** | nodes |
| **Roads** | links |
| A route from **A to B** | the path we are looking for |

```text
       (A)---------(o)
        |            \
       (o)---(o)------(B)
```

Note:
Starting from a road map rather than from a grid is deliberate: it stops
students from assuming pathfinding means "tiles". Everything in this lecture
works on any graph.

---

# BFS
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Breadth first search finds a path from A to B by exploring layer by layer.

It works. Its two drawbacks:

- **slow** — it explores in *every* direction, including away from the goal
- **no priorities, no weights** — every step costs the same

```text
      . . 3 . .
      . 2 2 2 .          A expands equally in all directions,
      3 2 A 2 3          then finally reaches B
      . 2 2 2 .
      . . 3 . B
```

Note:
Both drawbacks have the same root cause: BFS knows nothing about the world
except adjacency. The next two slides fix them one at a time — weights fix the
second, heuristics fix the first.

---

# Weights
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Not every step costs the same. *Civilization VI*, 2016:

| Terrain | Movement |
| --- | --- |
| **Plains** | base cost |
| **Roads** | fast |
| **Forests, hills** | slow |

<small>The cost table *is* the strategy layer of the game. Change it and you
change how the map is played.</small>

Note:
Insist that weights are game design, not physics. Making forests expensive is
what makes roads valuable, which is what makes road-building a decision. The
pathfinder just obeys.

---

# Dijkstra
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

<small>Edsger Dijkstra, 1956 — reportedly designed in about twenty minutes, in a
café, without paper.</small>

BFS with weights: always expand the **cheapest known** node next.

Note:
The algorithm is one sentence long, and the whole difficulty is bookkeeping:
keeping a tentative distance per node, and remembering the parent so you can
rebuild the path at the end.

---

### Worked example — the graph

```text
              8
      (A)-----------(C)
       |            / \
       | 4       1 /   \ 7
       |          /     \
      (B)      (F)      (E)
       |         |      /
       | 8       | 2   / 2
       |         |    /
      (D)-------(I)  /
       |  \  14  |  /
     7 |   \     | 10
       |    \    |
      (H)   (E) (J)
```

<small>Reconstruction from the original slides; the edge set is the one
consistent with every distance shown on them.</small>

---

### Worked example — the run

Start at **A**, expand the cheapest node each time:

| Step | Settled | Tentative distances |
| --- | --- | --- |
| 1 | A = 0 | B = 4, C = 8 |
| 2 | B = 4 | C = 8, D = 12 |
| 3 | C = 8 | D = 12, F = 9, E = 15 |
| 4 | F = 9 | I = 11, E = 15, D = 12 |
| 5 | I = 11 | J = 21, H = **25**, D = 12 |
| 6 | D = 12 | E = **14**, H = **19** |

**Result: A → B → D → H, total 19.**

Note:
Two numbers get *improved* — E from 15 to 14, H from 25 to 19. That is the whole
point of the algorithm and the thing students must see happen: a node's distance
is provisional until it is settled.

---

### On a grid

The same thing, with the weight being the **distance travelled**:

```text
   orthogonal step = 1
   diagonal step   = 1.41

      A --1-- o --1.41-- o
      |                  |
     1.41                1
      |                  |
      o -----1---------- B
```

Same two drawbacks as BFS remain half-fixed: weights are handled now, but the
search still spreads **in every direction**.

---

# Heuristics
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

> A technique designed for solving a problem more quickly when classic methods
> are too slow, or for finding an approximate solution when classic methods fail
> to find any exact solution. This is achieved by trading optimality,
> completeness, accuracy or precision for speed.

<small>From the Greek *εὑρίσκω*, "I find, I discover" — Wikipedia. In a way, a
shortcut.</small>

Note:
Read the trade explicitly: we give up something to gain speed. In A*'s case, as
long as the heuristic never *overestimates*, we give up nothing at all — which
is why A* is the famous one.

---

# A\*
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

A\* sits **on top of Dijkstra**, adding a priority for the nodes that look
closest to the destination.

```text
   Dijkstra           A*
   1 2 3 4 5 6 7 8    8 7 6 5 4 3 2 1
   ^                              ^
   cost from the       estimated cost
   start (g)           remaining (h)

   priority f = g + h
```

Note:
Write `f = g + h` on the board and leave it there for the rest of the lecture.
`g` is a fact, `h` is a guess, `f` is what the priority queue sorts on. Every
A* bug is one of these three being wrong.

---

### Step 1 — the start cell

```text
    h = 11.3     g = 0     f = 11.3
```

- the **heuristic** is the crow-flies distance to B — here 11.3
- the **Dijkstra cost** is free: we are already standing on the cell
- the **priority** is the sum of the two

---

### Step 2 — expanding

Each neighbour gets its own crow-flies heuristic. Transition costs:

- in the **cross** (orthogonal) = **1**
- in **diagonal** = **1.4**

```text
   h / g / f

   12.7  1.4  14.1  |  11.4  1.4  12.8  |  12.0  1  13
   11.3   0   11.3  |     [ start ]     |  10.6   1  11.6
   11.4  1.4  12.8  |  10.6   1   11.6  |   9.8  1.4 11.2
```

<small>Lowest `f` wins — here 11.2, towards B.</small>

Note:
Have them compute one cell out loud. The mechanical part is easy; what they must
internalise is that `h` is recomputed fresh for each new cell, while `g`
accumulates from the parent.

---

### Step 3 — costs accumulate, heuristics do not

- the **heuristic is always optimal**: it depends only on the cell's position,
  never on the route taken to reach it
- the **cost may not be**: a cell reached the long way carries a `g` that is too
  high

**So:** whenever a cheaper route to an already-seen cell is found, **update its
cost and its parent**.

<small>This is why you must remember each cell's parent, every time you search.</small>

Note:
This is the slide that separates a working A* from a subtly broken one. Students
who skip the update produce paths that are *nearly* optimal and impossible to
debug by looking at the result.

---

### Step 4 — no change is also a result

Expanding a cell often changes nothing:

- no new heuristics to compute — the neighbours were already visited
- their costs stay put, because reaching them **through the current cell** would
  be more expensive than through their existing parent

<small>Correct behaviour, and the most common source of "my A* is stuck" panic.</small>

---

### Ties

Two cells frequently share the same priority. They are examined in an
**arbitrary order**.

<small>Consequence: two runs on the same map can return two different — equally
optimal — paths. If you need determinism, break ties explicitly.</small>

Note:
Tie-breaking is also the cheap trick for prettier paths: bias ties towards the
straight line to the goal and the output stops looking like a staircase.

---

### The full expansion

<!-- TODO: figure d'origine, deck 07, slides ~38-39 (grille complète des f/g/h) -->

Every explored cell ends up holding its own `h`, `g` and `f`.

```text
   ... 8.9  3.4 12.3 | 8.5  4.4 12.9 | ...
   ... 8.0   3   11  | 7.6   4  11.6 | ...
   ... 6.7  4.4 11.1 | 6.3  5.4 11.7 | ...
   ... 5.3  5.8 11.1 | 5.0  6.8 11.8 | ...
                              ...  0  11.4  11.4  <- B reached
```

**The path is rebuilt by walking the parents backwards from the last cell.**

Note:
End the walkthrough here. The path is never built forwards — it is reconstructed
by following parent pointers from the goal back to the start, then reversed.

---

### Heuristics on a waypoint graph

The same idea, with the game's own vocabulary:

```text
   Cities · Crossroads · Roads

   heuristic:  on a road   -> distance * 1
               otherwise   -> distance * 2
```

<small>The heuristic encodes what the AI *believes* about the world — here, that
roads are twice as good.</small>

Note:
Careful: a heuristic that overestimates breaks A*'s optimality guarantee. The
`* 2` above is only safe if off-road movement really is at least twice as
expensive. Worth stating; not worth proving here.

---

# Flow fields
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

When there is **only one destination**, do not run a search per agent. Point
every cell of the map at the destination, once.

```text
   > > v v <        every cell stores a direction
   > > v < <        any agent, anywhere, just follows it
   ^ > B < <
   ^ ^ ^ < ^
```

Note:
This is the RTS answer: 200 units clicking the same rally point cost one field,
not 200 searches. It is a Dijkstra map — the same structure as the PCG lecture's
Dijkstra maps, used for movement instead of level design.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `redblobgames.com/pathfinding/a-star/introduction.html` — the one to read first
- `theory.stanford.edu/~amitp/GameProgramming/` — A\* implementation details
- `theory.stanford.edu/~amitp/GameProgramming/MovementCosts.html` — movement costs
- `gabrielgambetta.com/generic-search.html` — A\* explained as generic search
- `leifnode.com/2013/12/flow-field-pathfinding/` — flow fields, technical
- `howtorts.github.io/2014/01/04/basic-flow-fields.html` — flow fields for an RTS
- `slideshare.net/mobius.cn/influence-map` — influence maps
- `gamedev.net/articles/programming/artificial-intelligence/the-core-mechanics-of-influence-mapping-r2799/`

<small>Implementations already in the vault: [[cpp_a_star_|A\* en C++ moderne]] ·
[[ai_pathfinding_nav_mesh|AI Pathfinding (Nav mesh)]]</small>
