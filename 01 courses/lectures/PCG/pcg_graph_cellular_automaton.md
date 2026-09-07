---
title: Graphs & Cellular Automata
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
source_slides: https://docs.google.com/presentation/d/1TAX40hGOnn0-FI2mRCERd3orFMpOboCmTDomdBB6rm0/edit
manual_order: 33
---

# Procedural Generation
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Graphs and cellular automata

<small>Two structures, two generators: rooms connected by a graph, caves grown by
a rule</small>

Note:
Second lecture of the module. The previous one named the tools; this one derives
two of them completely. By the end, students should be able to generate a
connected dungeon layout and a connected cave system — the word *connected* is
the whole difficulty in both halves.

---

## Agenda
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

1. **Graphs** — nodes, links, direction, weight
2. **Minimum spanning tree** — Kruskal, and rooms connected by corridors
3. **Delaunay** — from a cloud of points to a graph
4. **Trees** — root, leaves, and how BSP produces one
5. **Traversal** — BFS and DFS
6. **Cellular automata** — Game of Life, caves, flood fill

---

# Graphs
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

<small>Discrete mathematics</small>

A structure of objects, some of which form pairs that are *in relation*.

- The objects are the **nodes** (or points)
- The relations are the **links** (or edges)

```text
        (1)-------(5)
         |  \       |
         |   \      |
        (3)---(8)--(7)
```

Note:
Keep the vocabulary bilingual on the board — students will meet *node/vertex* and
*link/edge* interchangeably in the literature.

---

### Undirected graph

The relation between two objects carries **no direction**: if 1 relates to 5,
then 5 relates to 1.

```text
        (1)-------(5)
```

<small>This is the default for "these two rooms are connected by a corridor".</small>

---

### Directed graph

The relation carries a **direction**. Two consequences:

- a relation can be **one-way** — 1 → 5, but not 5 → 1
- a relation can exist **both ways** — 1 → 5 *and* 5 → 1, as two distinct links

```text
        (1)------>(5)
        (1)<------(5)      both directions = two links
        (3)------>(8)      one-way only
```

Note:
One-way links are the level designer's drop-ledge: you can fall into the room,
you cannot climb back. Modelling it as a directed link is what lets the
generator reason about it.

---

### Weighted graph

Each link can carry a **weight**, defined by whatever criterion matters:
distance, cost, travel time, danger.

```text
        (1)---2---(5)
         |  \       |
         3   1      2
         |    \     |
        (3)-1-(8)-3-(7)
```

Note:
The weight is a design decision, not a fact. Weighting corridors by *danger*
rather than by *length* changes the generated dungeon completely.

---

# Minimum spanning tree
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

The set of links of an undirected spanning tree that:

- **connects every node** together
- contains **no cycle**
- has the **smallest possible total weight**

Note:
Three conditions, and students must be able to recite them. Drop any one and the
result is no longer an MST — dropping "no cycle" is the mistake they will make.

---

### Kruskal's algorithm

To find the graph with the fewest links that still connects everything:

1. Sort the links by weight, ascending
2. Take the **lightest** link and add it to the MST
3. **Skip** any link that would close a loop
4. Continue until every node is connected

```text
   links sorted:  1, 1, 2, 2, 3, 3, ...
                  ^  ^  ^  x     -> x closes a loop, discarded
```

Note:
It is a greedy algorithm and it is provably optimal, which is rare enough to be
worth saying out loud. The loop check is a union-find in practice — mention it,
do not derive it here.

---

### MST for room connection

A complete worked use case:

1. Generate the rooms, take their **centres**
2. **Triangulate** those centres — you now have every plausible corridor
3. Build the **MST**, weighting each link by the distance between rooms
4. Add a few **loops back in**, deliberately

<small>Step 4 is the design step: shortcuts, secret passages, and the escape
route that makes a dungeon readable.</small>

Note:
Step 3 alone gives a dungeon where every room has exactly one route in — safe,
connected, and tedious. The reinjected loops are typically 10-15% of the
discarded links. This is the canonical PCG dungeon recipe; students will
implement it.

---

### Delaunay triangulation

In PCG we often have a cloud of points and **no graph**. Triangulation builds
the graph of all plausible connections.

The **Bowyer-Watson** algorithm produces a Delaunay triangulation: no point
falls inside the circumcircle of any triangle, which is what keeps the triangles
fat and the connections local.

<small>Reference implementation:
`github.com/EliasFarhan/GPR4400_920` → `Assets/Scripts/GPR4400/TriangulationUtils.cs`</small>

Note:
"No long thin slivers" is the property that matters for us: a Delaunay edge
connects rooms that are actually near each other, so the MST built on top of it
produces corridors that make spatial sense.

---

# Trees
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

The graph produced by the MST is a special one:

- every node is reachable by **exactly one path** — no loops
- it is **undirected**

That is a **tree**.

- Pick one node as the parent of all: it is the **root** — the choice is arbitrary
- The end-of-branch nodes with a single neighbour are the **leaves**

Note:
Emphasise that "root" is a choice, not a property of the structure. The same tree
rooted at a different node describes a different traversal order and a different
level progression.

---

### BSP produces a tree

Binary space partitioning and trees are the same object seen twice:

```text
   +-------+-------+          (space)
   |       |   B   |          /      \
   |   A   +-------+       (A)      (split)
   |       |   C   |                /     \
   +-------+-------+             (B)      (C)

   each cut = a node        each final area = a leaf
```

Note:
This is the slide that makes the previous lecture click. Rooms go in the leaves;
corridors are carved by walking back up the tree and connecting siblings.
Connecting siblings, and only siblings, is what guarantees the result is
connected without any extra check.

---

### Walking a tree

Several reasons to traverse:

- finding a path
- finding the largest or smallest object
- deciding whether two nodes are **connected at all**

<small>Two strategies: breadth first, and depth first.</small>

---

### Breadth First Search

Traverse **horizontally**, then descend one layer at a time.

1. Start at the root
2. Go down one layer — left-to-right or right-to-left, arbitrarily
3. Continue until the whole tree has been visited

```text
             (1)
            /   \
         (2)     (3)
         / \     / \
      (4) (5) (6) (7)
      / \
   (8) (9)  (10) (11)      visit order = 1 2 3 4 5 6 7 8 9 10 11
```

Note:
BFS uses a queue. On an unweighted graph it also gives the shortest path in
number of steps, for free — which is why it comes back in the AI pathfinding
lecture.

---

### Depth First Search

Traverse **vertically**: go as deep as possible, back up only when stuck.

1. Start at the root
2. Pick one child
3. Continue until you reach a leaf
4. Back up to the nearest node with an unvisited child, and continue

```text
             (1)
            /   \
         (2)     (8)
         / \     / \
      (3) (5) (9) (10)
      / \
   (4) ...  (6) (7)         visit order = 1 2 3 4 5 6 7 8 9 10 11
```

Note:
DFS uses a stack, or recursion — which is the same stack, borrowed from the
runtime. Its randomised form is exactly the maze carver from the previous
lecture.

---

### BFS vs DFS

| | BFS | DFS |
| --- | --- | --- |
| Structure | queue | stack / recursion |
| Explores | layer by layer | branch to the end |
| Finds | the shortest path first | *a* path, fast |
| Memory | wide frontier | deep stack |

With **early exit** — stop as soon as a path is found — the choice becomes a
real trade-off: DFS reaches *a* target sooner, BFS reaches the *nearest* one.

Note:
Give them the case where DFS is catastrophic: a deep tree where the target is
the second child of the root. And the case where BFS is: a broad shallow tree
where any answer will do.

---

# Cellular automata
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
Second half. The structure changes completely: no more explicit graph, only a
grid and a local rule applied everywhere at once.

---

### Game of Life

Black cells are **alive**, white cells are **dead**. At each step, every cell is
evaluated and its living neighbours counted:

| Cell | Living neighbours | Becomes |
| --- | --- | --- |
| alive | 2 or 3 | alive |
| dead | exactly 3 | alive |
| any other case | — | dead |

<small>`playgameoflife.com`</small>

Note:
Insist that all cells are evaluated **from the same snapshot**. Updating in
place, reading half-new half-old neighbours, is the classic first bug and it
produces plausible-looking garbage.

---

### Counting neighbours

Step 0: for every cell, count the occupied neighbours.

```text
   grid            neighbour counts
   . # # .            1 2 2 1
   # # . .            2 3 3 1
   . # # #            2 3 3 2
   . . # .            1 2 2 2
```

Then apply the rule everywhere at once, and you have step 1.

<!-- TODO: figure d'origine, deck 02, slides ~44-47 (grilles step 0 à step 3) -->

---

### Neighbourhoods in 2D

```text
   Moore neighbourhood        Von Neumann neighbourhood

   (-1, 1)( 0, 1)( 1, 1)              ( 0, 1)
   (-1, 0)  cell ( 1, 0)       (-1, 0)  cell ( 1, 0)
   (-1,-1)( 0,-1)( 1,-1)              ( 0,-1)

        8 neighbours                4 neighbours
```

Note:
The choice is not cosmetic. Moore includes diagonals; Von Neumann does not. Which
one you pick decides whether a diagonal gap counts as a passage — and that
question comes back two slides later, as a bug.

---

### Growing a cave

Same machinery, different rule. Start from a noisy grid and apply:

| Cell | Living neighbours | Becomes |
| --- | --- | --- |
| alive | 1, 4, 5, 6, 7 or 8 | alive |
| dead | 5, 6, 7 or 8 | alive |
| any other case | — | dead |

After about **five iterations** the noise has smoothed into cave-like blobs.

Note:
Have them play with the thresholds live. Raising the birth threshold thins the
caves; lowering it floods the map. There is no correct value — there is a value
that fits the movement speed of your character.

---

### The connectivity problem

A smoothed cave is not a *playable* cave: it comes out as several **disconnected
pockets**, some far too small to be worth anything.

<small>The generator has produced a beautiful map the player cannot traverse.</small>

Note:
This is the moment to link back to the MST half of the lecture: there, we
guaranteed connectivity by construction. Here we have to go and measure it after
the fact. Two opposite strategies for the same requirement.

---

### Flood fill

Count the cells that are actually connected to one another:

1. Find a cell that has not been checked yet
2. Assign it an index, and give **all its neighbours** the same index
3. Count the cells carrying that index as you go
4. At the end, delete the regions that are too small

```text
   1 1 . 2 2      three regions found
   1 1 . 2 2      region 3 = 1 cell  -> deleted
   . . . 2 .
   3 . . . .
```

Note:
Deleting small regions is the cheap fix. The expensive fix is carving a corridor
between the two largest ones — which is, again, an MST over region centres. The
two halves of the lecture meet here.

---

### The flood fill trap

Use the **Von Neumann** neighbourhood when flooding.

With Moore, two cells touching only by a corner are counted as connected — but
the player cannot walk through a diagonal pinch. The generator would certify a
map as connected when it is not.

Note:
The best kind of bug to show students: the code is correct, the algorithm is
correct, and the answer is wrong because the neighbourhood does not match the
character controller. Always ask what *the player* can traverse.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `tutorialspoint.com/discrete_mathematics/graph_and_graph_models.htm` — graph primer
- `geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/` — Kruskal
- `youtube.com/watch?v=ucWX34Vrel8` — using an MST to generate a maze
- `raywenderlich.com/2425-procedural-level-generation-in-games-using-a-cellular-automaton-part-1` — cave implementation
- `rejbrand.se/rejbrand/article.asp?ItemIndex=425` — cellular automaton rule patterns
- `youtube.com/watch?v=R9Plq-D1gEk` — John Conway on the Game of Life

<small>Related theory block: Théorie des Graphes et Recherche de Chemin</small>
