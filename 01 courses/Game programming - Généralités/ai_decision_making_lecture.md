---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# AI Fundamentals
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Decision Making

<small>State machines · Behaviour trees · GOAP</small>

Note:
This lecture is about how a game agent *decides what to do next*. We
move from the simplest mental model (a finite state machine) to a more
scalable one (behaviour trees), and finish on a glimpse of planning
(GOAP). Each step solves a limitation of the previous one.

---

## Agenda
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

1. **The AI Engine** — where decision making sits
2. **State Pattern** — finite state machines
3. **Behaviour Trees** — graphs of actions
4. **GOAP** — goal-oriented action planning

---

# The AI Engine
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
Game AI is usually split into three layers: *decision making* (what
should I do?), *steering / movement* (how do I get there?), and
*sensing* (what do I know about the world?). Today we stay almost
entirely in the first layer.

---

### The Decision Loop

Every AI agent runs the same loop, every frame:

```text
   ┌─────────┐     ┌────────────────┐     ┌─────────┐
   │  SENSE  │ ──▶ │ DECIDE         │ ──▶ │   ACT   │
   │ world   │     │ (state machine │     │ move,   │
   │ inputs  │     │  / tree / plan)│     │ animate │
   └─────────┘     └────────────────┘     └─────────┘
        ▲                                      │
        └──────────────────────────────────────┘
```

<small>This lecture is entirely about the **DECIDE** box.</small>

Note:
The architectures we cover — FSM, behaviour trees, GOAP — are all
interchangeable implementations of that middle box. Picking one is a
trade-off between simplicity, scalability and how "smart" the agent
needs to look.

---

# State Pattern
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

### Finite State Machines

---

## State Pattern — Définition
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

A **state machine** describes behaviour as a set of distinct
*states*, and the *transitions* that move the agent between them.

The agent is always in **exactly one** state, and that state fully
determines how it behaves *right now*.

Note:
The State pattern is one of the classic Gang of Four patterns. In games
it is by far the most common decision-making structure — patrol /
chase / attack enemies, menu screens, animation graphs, all of it.

---

### Finite State Machine — from Automata Theory

**You have a fixed set of states the machine can be in.**

```text
   ( Idle )      ( Patrol )      ( Chase )      ( Attack )
```

<small>Source: en.wikipedia.org/wiki/Automata_theory</small>

Note:
This idea comes straight out of automata theory in computer science.
The set of states is decided up front, at design time — the machine
cannot invent a new state at runtime.

---

### Finite State Machine — from Automata Theory

**The machine can only be in one state at a time.**

```text
   ( Idle )    [ Patrol ]    ( Chase )    ( Attack )
                  ▲
              current state
```

Note:
This is the defining constraint — and also the main limitation. One
state at a time keeps things simple to reason about, but means the
agent cannot, say, "patrol *and* reload" at once without modelling a
combined state.

---

### Finite State Machine — from Automata Theory

**A sequence of inputs or events is sent to the machine.**

```text
   user inputs / events
   ───────────────────▶  [ State Machine ]
   "enemy spotted"
   "lost sight"
   "in range"
```

Note:
Inputs can be player commands, but in game AI they are usually *events*
the agent senses: a target entering range, taking damage, a timer
firing. Each event is a chance to transition.

---

### Finite State Machine — from Automata Theory

**Each state has a set of transitions** — each tied to an input and
pointing to a target state.

```text
            enemy spotted              in range
   ( Patrol ) ──────────▶ ( Chase ) ──────────▶ ( Attack )
        ▲                     │                      │
        └─────────────────────┘                      │
              lost sight                              │
        ▲                                             │
        └─────────────────────────────────────────────┘
                       target dead  →  final state
```

<small>input → state. Some states may be **final states**.</small>

Note:
A transition is the triple *(from-state, input, to-state)*. Drawn out,
the whole machine is a directed graph. A "final state" is one with no
outgoing transitions — for an enemy, that is often "dead".

---

### Unity's Animator is a State Machine

The Unity **Animator** window *is* a finite state machine you author
visually:

- each **box** is an animation state
- each **arrow** is a transition
- transitions fire on **parameters** (`bool`, `float`, `trigger`)

```text
   [Idle] ──Speed>0.1──▶ [Run] ──jumpTrigger──▶ [Jump]
      ▲                    │                       │
      └────Speed<0.1───────┘◀──────grounded─────────┘
```

Note:
This is the everyday proof that you already use state machines. The
Animator Controller is a designer-facing FSM editor. The same mental
model — states, parameters, transitions — applies to gameplay logic,
not just animation.

---

### Coding It — the `if` / `switch` way

The naive implementation: one `enum`, one big `switch`.

```csharp
enum State { Idle, Patrol, Chase, Attack }
State _state = State.Idle;

void Update() {
    switch (_state) {
        case State.Idle:   /* ... */ break;
        case State.Patrol: if (SeesEnemy()) _state = State.Chase;  break;
        case State.Chase:  if (InRange())   _state = State.Attack; break;
        case State.Attack: /* ... */ break;
    }
}
```

<small>Fine for **2–3 states**. Grows ugly fast.</small>

Note:
This works and is perfectly acceptable for a small agent. The problem
is scaling: per-state enter/exit logic gets scattered, the switch
becomes hundreds of lines, and two people cannot edit two states
without merge conflicts. It does not scale, but do not over-engineer
a three-state enemy either.

---

### Coding It — the Object-Oriented way

**Each state is a class.** The agent holds a reference to its current
state object and delegates to it.

```csharp
interface IState {
    void Enter();
    IState Update();   // returns the next state (or itself)
    void Exit();
}

class PatrolState : IState {
    public IState Update() =>
        SeesEnemy() ? new ChaseState() : this;
    // Enter / Exit ...
}
```

<small>Each state owns its own logic, its `Enter` / `Exit`, and its
transitions.</small>

Note:
This is the actual *State design pattern*. Benefits: each state is an
isolated, testable unit; enter/exit logic has an obvious home; adding a
state means adding a file, not editing a giant switch. Cost: more
boilerplate. The OO way pays off once you pass roughly four states.

---

### State Pattern — Sources
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- [Automata theory — Wikipedia](https://en.wikipedia.org/wiki/Automata_theory)
- [Game Programming Patterns — State](https://gameprogrammingpatterns.com/state.html)
- [State Pattern using Unity — Ray Wenderlich](https://www.raywenderlich.com/6034380-state-pattern-using-unity)
- [Finite State Machines — Unity Learn](https://learn.unity.com/project/finite-state-machines-1)
- [State machines in Unity — YouTube](https://www.youtube.com/watch?v=V75hgcsCGOM)

---

# Behaviour Trees
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

### A graph that determines an actor's actions

Note:
State machines break down when the number of states — and especially
the number of *transitions* — explodes. Behaviour trees scale better:
behaviour is composed hierarchically, and reused sub-trees are shared
instead of re-wired.

---

### A graph that determines an actor's actions

A behaviour tree is a **tree of nodes**, evaluated from the top down.

```text
                    ( node )
                   /        \
            ( node )        ( node )
            /     \             |
       (node)   (node)       ( node )
                              /     \
                         (node)   (node)
```

<small>Every frame the agent **traverses** the tree to choose its
action.</small>

Note:
Where an FSM is a flat graph of states, a behaviour tree is a
*hierarchy*. Composition is the key idea — small behaviours snap
together into bigger ones, and a whole sub-tree can be reused.

---

### Node taxonomy

```text
                    [ root ]
                       │
                  [ decorator ]
                       │
                  [ composite ]
                  /     │      \
            [ leaf ] [ leaf ] [ composite ]
                              /    │     \
                        [leaf]  [leaf]  [leaf]
```

Four kinds of node: **root**, **decorator**, **composite**
(selector / sequence), and **leaf**.

Note:
Earlier slides ask "root (node?)" / "decorator (node?)" — the answer is
yes, everything is a node; these are just *roles*. The next slides
define each role precisely.

---

### Node — `root`

```text
        ▶ [ ROOT ]
             │
        [ decorator ]
             │
           ...
```

**The root has no parent.** It *is* the tree.

Tree traversal starts here every tick.

Note:
There is exactly one root per tree. It is the entry point of every
evaluation. Often it is little more than a handle to the first real
node beneath it.

---

### Node — `leaf`

```text
        [ composite ]
        /     │     \
   [LEAF]  [LEAF]  [LEAF]
```

A **leaf has no children**. It is the **end of a branch**.

The leaf is where the actor **performs an actual action** — move,
attack, play an animation, check a condition.

Note:
Leaves are the only nodes that *do* anything observable. Two flavours:
*action* leaves (move to door) and *condition* leaves (is the door
locked?). Everything above the leaves only decides *which* leaves run.

---

### Node — `decorator`

```text
        [ DECORATOR ]
             │
          [ node ]   ← exactly one
```

A **decorator has exactly one child.**

It *wraps* that child to modify it — invert its result, repeat it,
add a cooldown, succeed-anyway, etc.

Note:
Think of decorators as modifiers. Common ones: Inverter, Repeater,
Succeeder, Cooldown. They never contain *behaviour* themselves; they
adjust the behaviour of the single node below them.

---

### Composite — `sequence`

```text
        [ SEQUENCE ]
        /     │     \
   [leaf] [leaf] [leaf]
      1      2      3
```

A **sequence runs its children one by one, in order**.

It is the **"AND"** of behaviour trees — *do this, then this, then
this*.

Note:
A sequence is a to-do list executed left to right. We will see the
exact success/failure rules in a couple of slides — but the intuition
is: keep going only while each step succeeds.

---

### Composite — `selector`

```text
        [ SELECTOR ]
        /     │     \
   [leaf] [leaf] [leaf]
```

A **selector runs children until one succeeds** — then stops.

It is the **"OR"** of behaviour trees — *try this, or else this, or
else this*.

Note:
A selector is a priority list of fallbacks. Only one child ultimately
"counts". It is how you express "do the best option that is currently
possible".

---

### Worked example — "Have dinner"

A **selector**: pick the *first option that works*.

```text
        [ SELECTOR: Have dinner ]
        /          │           \
  [order pizza] [cook pasta] [eat ice cream]
```

Note:
Read it as: try to order pizza; if that fails, cook pasta; if that
fails, fall back to ice cream. The selector stops at the first option
that succeeds.

---

### Worked example — nesting trees

Children of a composite can themselves be composites:

```text
[ SELECTOR: Have dinner ]
├─ [ SEQUENCE: order pizza ]
│     ├─ pick up the phone
│     ├─ [ SELECTOR: pick a restaurant ]
│     ├─ go downstairs
│     └─ give a tip
├─ cook some pasta
└─ eat ice cream
```

Note:
This is the power of behaviour trees: a node does not care whether its
child is a leaf or another whole sub-tree. "Order pizza" is itself a
sequence of sub-steps, and one of those steps is another selector.

---

### Worked example — fully expanded

```text
[ SELECTOR: Have dinner ]
├─ [ SEQUENCE: order pizza ]
│     ├─ pick up the phone
│     ├─ [ SELECTOR: pick a restaurant ]
│     │     ├─ call local restaurant
│     │     ├─ order on Deliveroo
│     │     └─ order on Uber Eats
│     ├─ go downstairs
│     └─ give a tip
├─ cook some pasta
└─ eat ice cream
```

<small>Composition all the way down — selectors inside sequences
inside selectors.</small>

Note:
Notice the two composite types alternate naturally: a sequence of
*required* steps, where one of the steps is a selector of
*interchangeable* options. That selector / sequence alternation is the
everyday rhythm of authoring behaviour trees.

---

### Navigation — every node returns a status

When traversed, **each node returns one of three statuses** to its
parent:

| Status | Meaning |
|---|---|
| **`RUNNING`** | still working — ask me again next tick |
| **`SUCCESS`** | finished, it worked |
| **`FAILURE`** | finished, it did not work |

<small>Parents read these statuses to decide what to do next.</small>

Note:
This three-valued return is the whole protocol of a behaviour tree.
`RUNNING` is what makes trees handle multi-frame actions gracefully —
a node can say "not done yet" and be resumed next frame, no extra
state machine required.

---

### Sequence — the status rules

```text
        [ SEQUENCE: Dinner ]
        ├─ buy some food          ✔
        ├─ cook the ingredients   ✔
        ├─ eat the dish           ▶ running
        └─ load the dishwasher    · pending
```

A sequence runs the **next** child only while every previous child
**succeeds**:

- **`RUNNING`** — if a child is running
- **`FAILURE`** — if **one** child fails (stop immediately)
- **`SUCCESS`** — when the **last** child succeeds

Note:
Sequence = logical AND. The first failure short-circuits the whole
sequence — there is no point cooking if buying food failed. Success
requires every child to succeed.

---

### Selector — the status rules

```text
        [ SELECTOR: Dinner ]
        ├─ order pizza      ✘ failed
        ├─ cook some pasta  ▶ picked
        └─ eat ice cream    · not reached
```

A selector picks the **first child that does not fail**:

- **`RUNNING`** — if a child is running
- **`FAILURE`** — if **all** children fail
- **`SUCCESS`** — as soon as a picked child succeeds

Note:
Selector = logical OR. It is the mirror image of sequence: the first
*success* short-circuits, and only an all-children failure makes the
selector itself fail. Sequence and selector together give you AND / OR
over behaviour.

---

# Workshop — The Robber
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

Build a behaviour tree that steals a diamond.

---

### Workshop steps
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

1. **Make a `Node` class**
2. **Make a graph** and print all nodes
3. **Make leaves** that move the robber to different destinations
4. **Make a `Sequence` node** to execute leaves step by step
5. **Make a `Selector`** that picks one door
6. **Open the door**

Note:
The workshop builds the tree bottom-up: first the data structure
(node + graph), then the leaves that act, then the two composites that
orchestrate. Each step is independently testable before moving on.

---

### Workshop — the target tree

```text
[ _robberTree ]
└─ [ SEQUENCE: _stealOperation ]
      ├─ go to van
      ├─ [ SELECTOR: select a door ]
      │     ├─ go to front door
      │     └─ go to back door
      └─ go to diamond
```

<small>A sequence of must-do steps; one step is a selector choosing
*how* to get in.</small>

Note:
This is the same selector-inside-sequence pattern as the dinner
example. `_stealOperation` is the ordered plan; the door selector is
the interchangeable choice. If neither door works, the selector fails,
which fails the whole sequence — the heist aborts.

---

# Goal-Oriented Action Planner
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

### GOAP

---

### From scripted to *planned* behaviour

| Approach | The agent... |
|---|---|
| **FSM** | follows hand-wired transitions |
| **Behaviour tree** | follows a hand-authored tree |
| **GOAP** | is given a **goal** and **plans** the actions itself |

With GOAP you author **actions** (with preconditions & effects) and
**goals** — the planner searches for an action sequence that reaches
the goal.

<small>Famously used in <em>F.E.A.R.</em> for its strikingly smart
soldiers.</small>

Note:
GOAP flips the authoring effort. Instead of wiring *when* each action
runs, you describe *what each action needs and produces*, plus the
goal. A planner (an A*-style search over world states) assembles the
sequence at runtime. The pay-off is emergent, adaptive behaviour —
the F.E.A.R. soldiers flanking and taking cover were not scripted, the
planner found those sequences.

---

### References
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- *Three States and a Plan: The A.I. of F.E.A.R.* — Jeff Orkin
- [An Introduction to GOAP — Unity Learn](https://learn.unity.com/)
- *Goal-Oriented Action Planning: Ten Years of AI Programming*
- *Intro to Goal Oriented Action Planning*
- *Unity AI Tutorial: Goal Oriented Action Planning*
- *Goal-Oriented Action Planning for a Smarter AI*
- *Building the AI of F.E.A.R. with Goal-Oriented Action Planning*

---

# Recap
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- **FSM** — one state at a time; simple, but transitions explode
- **Behaviour Tree** — composable selectors & sequences; `RUNNING` /
  `SUCCESS` / `FAILURE`
- **GOAP** — author actions + goals; the planner finds the sequence

<small>Pick the simplest one that makes your agent look smart enough.</small>

Note:
The progression is one of moving authoring effort away from *when* and
toward *what*. Start with an FSM; reach for a behaviour tree when
transitions get unmanageable; reach for GOAP only when you genuinely
need adaptive, emergent planning.
