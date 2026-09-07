---
title: Procedural Content Generation — Applications
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
source_slides: https://docs.google.com/presentation/d/1tg8BEbLVmRAQFxHpUXM8Ci6_dbmZi9qnUPUwWU0IHVQ/edit
manual_order: 32
---

# Procedural Generation
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Applications

<small>Rooms · mazes · Dijkstra maps · distributions · geometry</small>

Note:
The toolbox lecture. Everything here is something a student can implement in an
afternoon and drop into a project. The recurring question across all of it is
the same: what does this algorithm guarantee, and what does it merely make
likely?

---

## Agenda
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

1. **Simple room placement** — the cheapest dungeon that works
2. **Mazes** — what a maze must contain to be a level
3. **Dijkstra maps** — the single most useful tool in the lecture
4. **Carving** — drunkard's walk, diffusion limited aggregation
5. **Distributions** — Voronoi, Gaussian, Poisson disk, noise
6. **From algorithm to geometry** — the part that actually ships

---

# Simple room placement
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

The whole algorithm:

1. Add a **random rectangle** of random size to the scene
2. Check it does **not overlap** an existing rectangle
3. Connect the **closest** rooms together
4. **Ensure total connectivity**

```text
   +-----+        +--+          +-----+--------+--+
   |     |   +----+  |    ->    |     |        |  |
   +-----+   |       |          +-----+--------+  |
        +----+-------+               +-----+------+
```

Note:
Step 4 is not a detail bolted on the end — it is the requirement, and steps 1 to
3 are a heuristic that usually satisfies it. Connect the room centres by
Delaunay, then MST, exactly as in the previous lecture.

---

# Mazes
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

A maze is not a level. A maze becomes a level once it has:

- an **entrance** and an **exit**
- **branches** — a branch is a *choice*
- **rooms and special places** — treasure, enemies
- **dead ends** — the cost of a wrong choice
- **loops** — shortcuts, backtracking made bearable

Note:
Go through them in this order and stop on "a branch is a choice". A maze with no
branch is a corridor; a maze with branches but no reward at the end of them is a
tax on the player. Every one of these five items is a design decision the
generator must be told about.

---

### Implementation

1. Take **one square**
2. **Divide it into a grid**
3. Designate **one starting cell**
4. **Visit every cell** to carve the maze — the last cell visited is the exit

<small>Or pick the exit first, and carve towards it.</small>

```text
   +---+---+---+---+       +---+---+---+---+
   |   |   |   |   |       | S         |   |
   +---+---+---+---+       +---+---+   +   +
   |   |   |   |   |  ->   |   |       |   |
   +---+---+---+---+       +   +---+---+   +
   |   |   |   |   |       |           | E |
   +---+---+---+---+       +---+---+---+---+
```

Note:
"Last cell visited is the exit" is the free trick of the lecture: it guarantees
the exit is as far from the start as the traversal could reach, without
measuring anything.

---

### Four carvers, four textures

| Algorithm | Result |
| --- | --- |
| **BFS** | short, fat, regular branches |
| **BFS, random neighbour order** | the same, less obviously gridded |
| **DFS** | long winding corridors, few branches |
| **DFS, random neighbour order** | long corridors, unpredictable turns |

<small>Randomising the neighbour order is one line of code and the single
biggest visual improvement available.</small>

Note:
Have them run all four on the same grid, same seed. DFS gives the "cave crawl"
feel, BFS gives the "hedge maze" feel. Neither is better; they answer different
design intents.

---

# Dijkstra maps
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Generate a map of the **distance from a starting point** — typically with BFS.

```text
   4 3 2 3 4 5
   3 2 1 2 3 4
   2 1 S 1 2 3        every cell knows how far it is from S
   3 2 1 2 # #
   4 3 2 3 # #
```

Note:
This is the most reusable idea in the whole module. One BFS pass, and the grid
answers a dozen different design questions. Spend the most time here.

---

### Use 1 — remove the unreachable

Any cell the flood never reached is **unreachable**. Delete it, or refuse to use
it.

Run this *before* choosing a starting point, so you never place the player in a
sealed pocket.

Note:
Same job as the flood fill from the cellular automaton lecture, obtained as a
by-product. If you already need a Dijkstra map, you no longer need a separate
connectivity pass.

---

### Use 2 — find an endpoint

The endpoint is a query over the distance field.

<small>Example: start on the left edge (`pos.x == 0`), exit on the right
(`pos.x == width`) — and among the candidates, take the one with the greatest
distance.</small>

---

### Use 3 — the hot path

Regenerate a second Dijkstra map giving each tile its **distance to the critical
path**.

You can then:

- **cull** every tile too far from the hot path — a more linear level
- **spawn interesting loot** exactly at the far end of a branch

```text
   2 1 0 0 0 1 2       0 = on the critical path
   3 2 1 1 1 2 3       3 = deep in a side branch -> good treasure spot
```

Note:
This is how you buy "handcrafted pacing" from a random generator. The reward
value can literally be a function of the distance-to-hot-path number.

---

### Use 4 — room based dungeons

The same map, computed over **rooms** instead of tiles:

- mark the rooms on the hot path
- hide treasure in the off-path rooms — or cull them for a linear dungeon

---

### Use 5 — ordering the story

Give each room an **order number**. Now the generator can tell a story:

> Put a lock on room 5, and the key in a room between 1 and 4 —
> ideally in an off-path room, to push exploration.

Note:
The lock-and-key example is the punchline of the lecture. Nothing here is
authored, and yet the result reads as designed. This is what "procedural" means
when it is done well.

---

# Carving
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

### Drunkard's walk

> Put Hulk somewhere on the map. Give him beer. Let him run randomly.

He stops when he leaves the map, or passes out after *n* steps.

The result looks like **caverns carved by water**.

```text
   . . # # # . .
   . # # . # # .        one wandering agent,
   # # . . . # #        everything it touched is floor
   . # # # . . .
```

Note:
Trivially connected — the walker cannot teleport, so every carved cell is
reachable from the start. That guarantee for free is why the algorithm survives
despite being absurd.

---

### Diffusion limited aggregation

1. Set a **target seed**
2. From a random position on the map, **shoot a particle**
3. **Dig out** the last edge the particle hit

A **central attractor** gives an open central area — good for a boss room.

<small>Typically produces **open areas**, in contrast with cellular automata.</small>

Note:
The mental image is frost growing on a window. Compare the output side by side
with the cave automaton: DLA gives branching open space, the automaton gives
blobby rooms. Different games.

---

# Distributions
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

---

### Voronoi diagram

1. Throw random points
2. Build regions from the **closest point**
3. Done

```text
    .  |     |   .
   ----+  .  +------      each region = everything nearer
    .  |     |   .        to this point than to any other
```

- Apply **Lloyd relaxation** for something more regular
- Swap the **distance heuristic** — Manhattan, Chebyshev — for a different look
- Used for **city generation**: edges become roads, regions become districts

Note:
Manhattan distance gives blocky, city-like cells; Euclidean gives organic ones.
One line of code, completely different city.

---

### Gaussian random

The normal distribution: **more probability near the centre**, like the sum of
several dice.

```text
   1 die:    flat        ▁▁▁▁▁▁
   3 dice:   bell        ▁▂▅█▅▂▁
```

Use it for enemy shot spread, and for object spawn density.

Note:
The "sum of several dice" trick is how you get an approximate Gaussian without
touching a maths library — and it is how tabletop games have done it forever.

---

### Poisson disk sampling

Guarantees that points are **separated by at least a radius**.

Useful for object spawn: forests, asteroid fields, anything that must look
scattered but never clumped.

**Implementation:** start from a sample point; add points by checking the
surrounding area through a simple grid; stop when there is no space left.

Note:
This is the fix for the "random position clumps" failure mode from the
introduction lecture. Show uniform scatter next to Poisson disk — students see
immediately which one looks *designed*.

---

### White noise

Random distribution between black and white, uncorrelated.

<small>Almost never what you want on its own — but it is the input the cellular
automaton smooths, and the input Poisson disk replaces.</small>

---

### Perlin noise

A procedural texture, used as a visual effect: **random values in waves**.

- typically **layered in octaves** for a richer result
- built into Unity as `Mathf.PerlinNoise`

Note:
Layering is the whole craft: one big slow octave for the continents, a medium
one for the hills, a fast one for the surface detail. Amplitude halves as
frequency doubles.

---

# From algorithm to geometry
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

All of this is nice to *watch*. A game needs **geometry** out of those abstract
tiles and points.

- **2D** — instantiate tiles as sprites, add box colliders to the wall tiles
- **3D** — generate a mesh, add a mesh collider

> Only give a collider to wall tiles that have a **non-wall neighbour**.
> Otherwise your framerate collapses.

Note:
End on this slide, because it is where student projects die. A 200x200 grid is
40 000 colliders if you are naive, and about 2 000 if you check neighbours
first. Same level, twenty times the cost.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Terrain and meshes**

- `youtube.com/playlist?list=PLFt_AvWsXl0cONs3T0By4puYy6GM22ko8` — 3D planet generation
- `youtube.com/playlist?list=PLFt_AvWsXl0eBW2EiBtl_sxmDtSgZBxB3` — 3D terrain generation
- `shamusyoung.com/twentysidedtale/?p=9644` — 3D world generation
- `youtube.com/watch?v=bG0uEXV6aHQ` — Perlin noise in Unity
- `youtube.com/watch?v=64NblGkAabk` — mesh generation
- `youtube.com/watch?v=O9J_Cfl6HzE` — Islanders island generation post mortem

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

**Dungeons and mazes**

- `youtube.com/watch?v=TlLIOgWYVpI` — roguelike algorithms
- `youtube.com/watch?v=ucWX34Vrel8` — maze generation with an MST
- `youtube.com/watch?v=2ExLEY32RgM` — using Dijkstra maps
- `youtube.com/watch?v=Uqk5Zf0tw3o` — Spelunky generation, in depth
- `astrolog.org/labyrnth/algrithm.htm` — a catalogue of maze algorithms
- `thingonitsown.blogspot.com/2018/11/dungeon-generator.html`
- `ctrl500.com/tech/handcrafted-feel-dungeon-generation-unexplored-explores-cyclic-dungeon-generation/`
- `devforum.roblox.com/t/dungeon-generation-a-procedural-generation-guide/342413`

<small>Further reading and annexes: [[pcg_annexes]]</small>
