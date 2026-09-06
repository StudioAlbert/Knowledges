---
title: AI Fundamentals
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
source_slides: https://docs.google.com/presentation/d/1tTkOE_PtAqnNdSRq2bRa4VxNZ11fw-wXRVQm0pl8NS4/edit
---

# AI Fundamentals
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### The map of the module

<small>Movement · Pathfinding · Decision</small>

Note:
Opening lecture of the AI module. Its job is to hand out the vocabulary and the
map: every later lecture is one branch of the tree shown on the next slide. Do
not go deep on anything here — go *wide*, and name what is coming.

---

## The three families
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

```text
   AI
   |
   |- Movement
   |   |- Steering behaviour
   |   |- Blending behaviour
   |   `- Flocking behaviour
   |
   |- Pathfinding
   |   |- BFS
   |   |- DFS
   |   |- Dijkstra
   |   `- A*
   |
   `- Decision
       |- Decision tree
       |- State machine
       `- Behaviour tree
```

Note:
Ask students where "the enemy noticed me" fits in this tree. It does not — and
that is the point of the next slide. Perception is the missing fourth family,
and it comes back in the world representation lecture.

---

# The AI engine
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Every agent runs the same loop, every frame:

```text
   +---------+     +----------------+     +---------+
   |  SENSE  | --> |     DECIDE     | --> |   ACT   |
   |  world  |     | tree / FSM /   |     |  move,  |
   |  inputs |     | behaviour tree |     | animate |
   +---------+     +----------------+     +---------+
        ^                                      |
        `--------------------------------------'
```

<small>The three families above map onto the last two boxes. **Sense** is covered
in [[ai_world_representation|World Representation]].</small>

Note:
This diagram is the spine of the whole module. Every lecture that follows should
open by pointing at which box it lives in.

---

# Movement
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Three levels of sophistication, in order:

| | What it does | Feels like |
| --- | --- | --- |
| **Lerp** | interpolate towards a point | a camera rail |
| **Seek and arrive** | accelerate towards, decelerate near | something with mass |
| **Pursue and evade** | aim at where the target *will be* | something with intent |

<small>Full treatment: [[ai_steering_behavior|Steering Behaviour]]</small>

Note:
The jump from Lerp to Seek is the jump from "moving an object" to "an agent
deciding to move". Pursue is the one that reads as intelligence to a player,
and it is three lines of vector maths.

---

# Decision — decision tree
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

The simplest decision structure. You have written hundreds.

```csharp
if (playerInView) {
    ChasePlayer();
} else if (isHungry) {
    LookForFood();
}
```

<small>Cheap, readable, and it stops scaling around the fifth condition.</small>

Note:
Do not sneer at it. A decision tree is the right answer for most enemies in
most games. The lecture on decision algorithms is about what to do when it stops
being the right answer.

---

# Decision — finite state machine
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

The most elementary form of game AI. Typically implemented with:

- an **enum** listing the states
- a **field** holding the current state
- a **switch-case** defining each behaviour

```text
   [Idle] --see player--> [Chase] --lost him--> [Search]
      ^                                            |
      `----------------- gave up ------------------'
```

<small>Full treatment: [[ai_decision_algorithms|Decision Algorithms]]</small>

Note:
The enum/switch version is where everyone starts and it is fine up to about five
states. The object-oriented version — one class per state — is what the decision
lecture derives, and it is the same pattern as the Unity Animator.

---

# Decision — behaviour tree
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

First used in **Halo 2**. Another way to write AI, much easier to **serialise**:

- **Composite** — Selector, Sequencer, …
- **Decorator** — Repeater, Repeat-until-fails, Inverter, Succeeder, …
- **Leaf** — the actual actions, succeeding or failing

<small>The same structure you already know from Unreal's Behavior Trees.</small>

Note:
"Easier to serialise" is the reason it won, and it is worth spelling out: a tree
of nodes is data, so a designer can edit it in a graph editor without a
recompile. An enum-and-switch FSM is code, and only a programmer can touch it.

---

# Pathfinding
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

More than for player characters, these algorithms exist for **AI agents**.

| | Finds | Cost |
| --- | --- | --- |
| **BFS** | the shortest path in steps | explores everywhere |
| **DFS** | *a* path, fast | often a terrible one |
| **Dijkstra** | the cheapest path, weights included | explores everywhere |
| **A\*** | the cheapest path, guided by a heuristic | explores towards the goal |

<small>Full treatment: [[ai_pathfinding|Pathfinding]]</small>

Note:
Frame A* as "Dijkstra that has been told which way the exit is". That one
sentence saves an hour of confusion later.

---

# It starts with a graph
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Before any algorithm, be clear about the **mathematical structure** underneath.

There are several ways to turn a map into a graph — grid, waypoints, navmesh,
visibility graph — and the choice constrains everything downstream.

<small>`redblobgames.com/pathfinding/a-star/introduction.html`</small>

Note:
Red Blob Games is the single best resource on this and students should read it
before the pathfinding lecture, not after. The interactive diagrams do in five
minutes what a whiteboard does in forty.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `gamedev.net/articles/programming/artificial-intelligence/the-total-beginners-guide-to-game-ai-r4942/` — covers decision, pathfinding and movement, exactly this module
- `youtube.com/user/tthompso` — AI and Games: case studies of real shipped AI
- `gamedevelopment.tutsplus.com/tutorials/finite-state-machines-theory-and-implementation--gamedev-11867` — FSM implementations
- `gameprogrammingpatterns.com/state.html` — the State pattern, properly explained

<small>Unity-side counterparts already in the vault:
[[chapter_1_what_to_sense]] · [[unity_ai_core_principles]]</small>
