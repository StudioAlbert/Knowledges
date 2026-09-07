---
title: Decision Algorithms
type: course
status: Backlog
subject: AI
duration_h: 3
bloc_gsda:
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
source_slides: https://docs.google.com/presentation/d/1LQFu96jekKiG9GIxXDrrT3RJNj-czFsDJtPaGZSCkFM/edit
tags:
  - courses
  - AI
manual_order: 1
---

# AI Fundamentals
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Decisions making

<small>State pattern · behaviour trees · GOAP</small>

Note:
This deck overlaps almost entirely with
[[ai_decision_making_lecture]] in *Game programming - Généralités* — same title,
same three sections. See the import report in `02 Notes/Historique` before
teaching either one.

---

## Agenda
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

1. **The AI engine** — where decision making sits
2. **State pattern** — finite state machines
3. **Behaviour trees** — graphs of actions
4. **GOAP** — goal oriented action planning

<small>Each step solves a limitation of the previous one.</small>

---

# AI Engine
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

```text
   +---------+     +----------------+     +---------+
   |  SENSE  | --> |     DECIDE     | --> |   ACT   |
   +---------+     +----------------+     +---------+
        ^                                      |
        `--------------------------------------'
```

<small>This lecture is entirely about the **DECIDE** box.</small>

---

# State pattern
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

### Definition

A **finite state machine**, borrowed from automata theory.

---

### Finite state machine — the rules

- You have a **fixed set of states** the machine can be in
- The machine can only be in **one state at a time**
- A **sequence of inputs or events** is sent to the machine
- Each state has a set of **transitions**, each associated with an input and
  pointing to a state

```text
             user input
                 |
                 v
   [Idle] --see--> [Chase] --caught--> [Attack]  <- final state
      ^                                    |
      `-------------- lost ----------------'
```

Note:
Four bullets, and they are the definition. The one students break first is "one
state at a time" — as soon as they want an enemy that walks *and* shoots, the
FSM has to gain a state for the combination, and that is the combinatorial
explosion that behaviour trees exist to solve.

---

### The Unity Animator is a state machine

Same object, different vocabulary: states are animation clips, transitions carry
conditions, parameters are the inputs.

<small>Students have been authoring FSMs for months without calling them that.</small>

---

### Coding it — the if/switch way

```csharp
switch (state) {
    case State.Idle:   /* ... */ break;
    case State.Chase:  /* ... */ break;
    case State.Attack: /* ... */ break;
}
```

<small>Fine up to about five states. Past that, the transitions get lost inside
the bodies and nobody can see the machine any more.</small>

---

### Coding it — the object oriented way

**Each state is a class.**

```text
   interface IState { Enter(); Update(); Exit(); }

   IdleState : IState
   ChaseState : IState
   AttackState : IState

   StateMachine holds one IState, swaps it on transition
```

<small>`Enter` and `Exit` are what the switch version cannot express, and they
are where half the bugs live.</small>

Note:
The payoff is testability: a state is now a class you can instantiate alone.
The cost is ceremony. Both versions are correct; the choice is a function of how
many states you expect.

---

### Sources — state pattern

- `en.wikipedia.org/wiki/Automata_theory`
- `gameprogrammingpatterns.com/state.html`
- `raywenderlich.com/6034380-state-pattern-using-unity`
- `learn.unity.com/project/finite-state-machines-1`
- `youtube.com/watch?v=V75hgcsCGOM`

---

# Behaviour trees
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

### A graph that determines the actor's actions

```text
                 root
                  |
              decorator
                  |
               selector
              /    |    \
           leaf  leaf  sequence
                        /  |  \
                    leaf leaf leaf
```

Note:
Introduce the shape before the vocabulary. Students should see that it is a
tree, evaluated from the root every tick, before they learn what each node type
means.

---

### Root

**No parent.** This is the tree.

```text
   root
    |
   ...
```

---

### Leaf

- **no child**
- the end of a branch
- the actor **performs the leaf's action**

<small>Leaves are the only nodes that do anything. Everything else is control
flow.</small>

---

### Decorator

**Only one child.**

<small>Repeater, repeat-until-fails, inverter, succeeder — a decorator wraps a
single child and modifies its result or its repetition.</small>

---

### Sequence

Each leaf is performed **one by one**.

```text
   sequence
    |-- 1. leaf
    |-- 2. leaf
    `-- 3. leaf
```

---

### Selector

**Only one leaf is performed** — the first one that does not fail.

```text
   selector
    |-- leaf   <- try this
    |-- leaf   <- if it failed, this
    `-- leaf   <- if that failed too, this
```

---

### An example — dinner

```text
   Selector: Have dinner
    |-- order pizza
    |-- do some pastas
    `-- eat ice cream
```

<small>Try to order a pizza. If that fails, cook pasta. If that fails, ice
cream.</small>

---

### An example — nesting

```text
   Selector: Have dinner
    |-- Sequence: order pizza
    |    |-- pick the phone
    |    |-- Selector: Pick a restaurant
    |    |    |-- call local restaurant
    |    |    |-- order to Deliveroo
    |    |    `-- order to Uber Eats
    |    |-- go downstairs
    |    `-- give a tip
    |-- do some pastas
    `-- eat ice cream
```

Note:
The dinner example is worth all the abstract diagrams put together. Ask what
happens if the phone is dead: the sequence fails at step 1, the top selector
falls through to pasta. That is a fallback plan nobody had to write.

---

### Navigation — every node returns a status

```text
   RUNNING   still working on it
   FAILURE   could not do it
   SUCCESS   done
```

Each node returns one of the three to its parent, every tick.

---

### Sequence, precisely

```text
   Dinner (sequence)
    |-- buy some food
    |-- cook the ingredients
    |-- eat the dish
    `-- put in the dishwasher
```

If a leaf succeeds, the sequence moves to the next one, as long as they succeed.

| Status | When |
| --- | --- |
| **RUNNING** | one leaf is running |
| **FAILURE** | **one** leaf failed |
| **SUCCESS** | the last leaf succeeded |

<small>A sequence is a logical **AND**.</small>

---

### Selector, precisely

```text
   Dinner (selector)
    |-- order pizza
    |-- do some pastas
    `-- eat ice cream
```

The selector picks the first leaf that does **not** fail.

| Status | When |
| --- | --- |
| **RUNNING** | one leaf is running |
| **FAILURE** | **all** leaves failed |
| **SUCCESS** | the chosen leaf succeeded |

<small>A selector is a logical **OR**.</small>

Note:
Put the AND/OR framing side by side on the board. Once students see sequence =
AND and selector = OR, they can read any behaviour tree in the wild.

---

# Workshop
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Build a robber AI, step by step:

1. Make a **node** class
2. Make a **graph** and print all nodes
3. Make some **leaves** that move the robber to different destinations
4. Make a **sequence** node to execute leaves step by step
5. Make a **selector** that picks one door
6. **Open** the door

---

### Workshop — the target tree

```text
   _robberTree
    `-- _stealOperation (Sequence)
         |-- go to diamond
         |-- select a door (Selector)
         |    |-- go to front door
         |    `-- go to back door
         `-- go to van
```

Note:
Steps 1 and 2 are deliberately boring — printing the tree is what lets students
debug steps 3 to 6. Do not let them skip step 2.

---

# Goal Oriented Action Planner
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Instead of authoring *what to do*, author **what each action requires and what it
produces**, then let the agent **plan** a sequence that reaches its goal.

```text
   goal:    player is dead
   actions: [attack]  needs: weapon, in range
            [pick up gun]  needs: gun nearby   -> gives: weapon
            [move to player]                   -> gives: in range

   plan found: pick up gun -> move to player -> attack
```

Note:
The selling point over a behaviour tree: add a new action and every existing
goal can use it, with no tree to re-author. The cost is that the plan is a
search, and searches are hard to debug and hard to bound. Famously used in
F.E.A.R., 2005.

---

# References
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- *Three States and a Plan: The A.I. of F.E.A.R.* — the founding GOAP paper
- *An Introduction to GOAP* — Unity Learn
- *Goal-Oriented Action Planning: Ten Years of AI Programming*
- *Intro to Goal Oriented Action Planning*
- *Unity AI Tutorial: Goal Oriented Action Planning*
- *Goal Oriented Action Planning for a Smarter AI*
- *Building the AI of F.E.A.R. with Goal Oriented Action Planning*

<small>Counterparts already in the vault: [[ai_decision_making_lecture]] ·
[[finite_state_machine]] · [[behavior_tree]] · [[goal_driven_behaviour]] ·
[[cpp_behaviour_tree_lecture]]</small>
