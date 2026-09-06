---
title: AI World Representation
type: course
status: Backlog
subject: AI
duration_h: 3
bloc: "[[AI Fundamentals]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
source_slides: https://docs.google.com/presentation/d/10jwfKqraYPJMlk_7OoQ4xGrVbG-Co8L_c7SIbJSlo0I/edit
---

# AI Fundamentals
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Artificial space representations

<small>Waypoint graphs · navmesh · point query systems</small>

Note:
An agent does not navigate the level. It navigates a *model* of the level that
we built for it. This lecture is about choosing that model — and it comes before
the pathfinding lecture on purpose, because the representation constrains which
algorithm is even possible.

---

## Agenda
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

1. **Waypoint graph** — a set of points
2. **NavMesh** — a set of convex shapes
3. **Point query system** — the hybrid that ships

<small>The same three questions each time: who authors it, how direct are the
paths, and what does a query cost?</small>

---

# Waypoint graph
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

A **set of points**, linked to one another.

```text
      (o)-------(o)
       |  \       |
       |   \      |
      (o)---(o)--(o)
```

- placed **by hand**, **generated** by an algorithm, or a mix of both
- individual points can carry **specific behaviours** — a cover spot, a sniper
  perch, a patrol pause
- you choose the **level of detail**

Note:
The behaviour-carrying point is the design payoff. A navmesh knows where the
agent *can* stand; a waypoint knows where it *should* stand and why. That is
level-design data, and it is the reason waypoints refuse to die.

---

### Level of detail

Fewer points means cheaper searches and coarser movement; more points means
smoother paths and a slower search.

```text
   coarse                     fine
   (o)-----------(o)          (o)-(o)-(o)-(o)
    |             |            |   |   |   |
   (o)-----------(o)          (o)-(o)-(o)-(o)
   fast, robotic              smooth, expensive
```

<small>The density is a design decision, not a technical one.</small>

---

# NavMesh
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

A set of **convex shapes** covering the walkable surface.

```text
   +--------+-------+
   |   A    |   B   |     inside one convex shape,
   +----+---+-------+     any two points are joined
   | C  |     D     |     by a straight line
   +----+-----------+
```

- allows **more direct paths** than a waypoint graph
- once generated, it is **faster** to find a path

Note:
Convexity is the whole trick and it is worth one minute: inside a convex
polygon, the straight segment between any two points stays inside the polygon.
So movement within a cell needs no pathfinding at all.

---

### Three scenarios for two points

| Situation | What to do |
| --- | --- |
| both points on the **same** triangle | straight line, no search |
| one point **outside** every triangle | no path — reject the query |
| points on **different** triangles | run pathfinding over the mesh |

Note:
Case two is the one students forget, and it is the one that produces the classic
bug: the enemy walks into a wall forever because the destination was off-mesh.
Always snap the target to the navmesh, or fail loudly.

---

# Point query system
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

The mix of the two previous solutions — and what shipped games actually use:

- **NavMesh** for the open areas
- **Points** for the important or interesting places
- the points can be **generated at runtime**
- each point carries a **weight**

<small>`youtube.com/watch?v=B0Su8cxipBQ`</small>

Note:
Runtime generation is what makes this a *query* system rather than a data
structure: "give me the three best cover positions that see the player and are
behind me" is answered by generating candidate points now, scoring them, and
sorting. Unreal's EQS is exactly this.

---

### Weights are the design surface

```text
   candidate points around the agent
        (o) score 0.2   -- exposed
        (o) score 0.9   -- in cover, sees the player
        (o) score 0.6   -- in cover, blind
```

The agent does not need to be clever. It needs a **good scoring function**, and
that function is written by a designer.

Note:
This is the bridge to the utility AI lecture on the Unity side of the vault
([[unity_ai_utility_ai|Unity AI - Utility AI]]). Same idea: score the options,
pick the best, and put the intelligence in the scoring.

---

# Choosing
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

| | Waypoint graph | NavMesh | Point query |
| --- | --- | --- | --- |
| Authoring | manual, or generated | generated from geometry | both |
| Path quality | as good as the points | direct | direct + meaningful stops |
| Query cost | cheap | cheap after bake | scales with candidates |
| Carries design intent | **yes** | no | **yes** |
| Dynamic worlds | rebuild by hand | re-bake | runtime candidates |

Note:
The honest summary: navmesh for locomotion, points for intent, and almost every
shipped game uses both. If a student must pick one for a school project, navmesh
— because Unity gives it for free.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `gameaipro.com` — the reference collection of expert articles, free online
- `theory.stanford.edu/~amitp/GameProgramming/MapRepresentations.html` — the hierarchy of representations
- `youtube.com/watch?v=CHV1ymlw-P8` — Unity NavMesh tutorial
- `medium.com/@mscansian/a-with-navigation-meshes-246fd9e72424` — implementing A* on a navmesh
- `journals.sagepub.com/doi/full/10.1155/2015/238727` — waypoint graph implementation
- `factorio.com/blog/post/fff-317` — hierarchical pathfinding, in production
- `cs.au.dk/~gerth/advising/thesis/anders-strand-holm-vinther_magnus-strand-holm-vinther.pdf` — 2D pathfinding thesis
- `learn.unity.com/project/waypoints-graphs` — Unity Learn, waypoint graphs

<small>Unity-side counterpart already in the vault: [[ai_pathfinding_nav_mesh]]</small>
