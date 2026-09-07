---
title: Steering Behaviours
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
source_slides: https://docs.google.com/presentation/d/1YGAQb00UQ4Vo6S7Dn9-Q6Z881JGWoxza36SAROk-xVg/edit
---

# AI Fundamentals
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Movements: Steering Behaviours

<small>Seek · flee · arrival · wander · pursuit · evade · avoidance · flocking</small>

Note:
Pathfinding gave us a list of points. This lecture is about *how* the agent
travels between them — and it is where an enemy stops looking like a moving
object and starts looking like a creature.

---

## Where we are
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

| Layer | Question | This lecture |
| --- | --- | --- |
| **Action / decision** | what should I do? | done |
| **Steering** | how do I get there? | **here** |
| **Locomotion** | how do my legs move? | out of scope |

<small>Steering is path *determination*; locomotion is animation.</small>

Note:
Drawing this three-layer split early prevents the usual confusion between
"the agent decides to flee" (decision), "the agent turns away" (steering) and
"the run cycle plays" (locomotion).

---

# Following a path
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

**Implementation:** the agent follows a single path — a list of points — and
edits its `transform` every frame.

**Drawbacks:**

- movement is **not organic**
- **no reaction** to the environment whatsoever

Note:
This is what every student writes first, and it is the correct starting point.
The rest of the lecture is a sequence of dissatisfactions with it.

---

### Attempt 1 — Rigidbody velocity

Set the rigidbody's `velocity` directly towards the next point.

**Result:** exactly the same as editing the transform. Suitable for
non-organic movement — a lift, a drone, a turret.

---

### Attempt 2 — Rigidbody force

Apply a force towards the next point.

```text
   red   = current velocity
   blue  = direction to the next point
```

<small>Better, but the agent overshoots and oscillates: nothing tells it what
velocity it *wants*.</small>

---

### Attempt 3 — simulate a force

The idea that makes everything else work:

```text
   desired velocity  -  current velocity  =  steering force

        (purple)            (red)              (green)
```

The agent computes the velocity it **wants**, subtracts the velocity it
**has**, and applies the difference as a force.

Note:
Write those three vectors on the board and leave them there. Every single
behaviour in the rest of the lecture is one formula for *desired velocity* —
the subtraction never changes.

---

# Steering behaviours
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
Go through them in order. Each one is one line of vector maths, and each one
adds a recognisable creature-like quality.

---

### Seek

Desired velocity points **at the target**, at max speed.

```text
     agent ----current velocity---->
        \
         `--desired-->  (Target)

     steering = desired - current
```

<small>Chained over a list of points, seek *is* path following — but with
momentum, so the agent cuts corners like a real thing.</small>

---

### Flee

The same, negated: desired velocity points **away from the target**.

```text
     (Target)   <--desired---- agent ----current---->
```

---

### Arrival

Seek, with the max velocity **decreasing** near the target.

```text
   seek:      ------------------>| overshoot, orbit, oscillate
   arrival:   -------->---->--> .| settles
                    slowdown radius
```

Note:
Without arrival, agents visibly vibrate around their destination. It is the
cheapest polish in the whole module: one clamp based on distance.

---

### Wander

A small random drift added to the current heading:

```text
   wanderAngle += Random(-angle, angle)
```

```text
   current velocity ---->
                     \ random angle
                      `--> steering
```

<small>Random *direction* per frame gives a seizure. Random *change* of
direction gives a wandering animal.</small>

Note:
This distinction is the whole slide. Integrating the randomness is what makes
the motion smooth, and it is the same reason Perlin noise beats white noise in
the PCG module.

---

### Pursuit

Seek, aimed at where the target **will be**:

```text
   position = target.position + target.velocity * T

   T = DistanceFromAgentToTarget / MaxVelocity
```

- if **T is too large**, the agent chases far too far ahead
- if **T is too small**, it degenerates into a plain seek

<small>Then use the seek behaviour towards that predicted point.</small>

Note:
Pursuit is the behaviour players read as *intelligence*. Nothing about it is
intelligent — it is one multiplication — and that gap is the lesson.

---

### Evade

Same principle as flee, but from the target's **predicted** position.

```text
   current velocity
   desired velocity  =  away from where the target is heading
   steering force
```

---

### Collision avoidance

**Look ahead.** Only obstacles inside the look-ahead volume matter; the rest
are "not important right now".

```text
              look-ahead
     agent ==============>  (o) obstacle
                             |
                             v avoidance force

     is D < R ?   ->   push sideways
```

<small>`D` = distance from the obstacle centre to the look-ahead segment,
`R` = the obstacle radius.</small>

Note:
The `D < R` test is the entire algorithm. Longer look-ahead means earlier,
smoother avoidance and more false positives; it is a tuning value, not a
constant.

---

### Separation

Every agent is pushed away from its close neighbours.

```text
   (1)   (2)          1 avoids 2 and 3
      (3)             2 avoids 1 and 3
                      3 avoids 1 and 2

   each pair -> a desired velocity -> a steering force
```

---

### Cohesion

The group has a target — its **centre** — and each agent tends towards it.

```text
   (1)      (2)
         x            x = group centre, everyone seeks it
      (3)
```

---

### Alignment

Each agent copies the **heading** of every agent within a given radius.

```text
   (1)-->  (2)-->
      (3)-->        headings converge
```

<small>Separation + cohesion + alignment = **flocking**. Three rules, and you
have a shoal.</small>

Note:
Reynolds' boids, 1986. Emphasise the payoff: no agent knows there is a flock.
The flock is an artefact of three local rules — the same emergence argument as
cellular automata in the PCG module.

---

### What a boid can see

```text
   (1)   (2)
      (3)    (4)      agent 4 is not seen by agent 3
```

Every rule above applies only to the neighbours **within the perception
radius** — and often within a **field of view**, not a full circle.

Note:
This is also the performance slide: naive flocking is O(n²). A spatial grid over
the perception radius is what makes a thousand boids affordable.

---

# Combining behaviours
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
The second half of the lecture, and the more interesting one. Every game needs
several behaviours at once, and there are five ways to reconcile them — each
with a real drawback.

---

### Solution 1 — force one behaviour

A state machine picks exactly one behaviour.

```text
   [Patrol] --sees an enemy--> [Flee]
```

- **Patrol** — a plain wanderer, roaming the map freely
- **Flee** — get a certain distance away from whatever is attacking

**Drawback:** one behaviour per state, and nothing else can contribute.

Note:
This is the honest default, and it ships. The obstacle avoidance you want *at
all times* is exactly what it cannot express.

---

### Solution 2 — priority arbitration

Each behaviour carries a priority, recomputed from the situation. The highest
wins.

| Behaviour | Nothing is happening | Agent is hungry | Hungry, enemy appears |
| --- | --- | --- | --- |
| Seek (food) | 1 | **6** | 6 |
| Flee (predator) | 2 | 2 | **8** |
| Wander | **5** | 5 | 5 |
| Seek (water) | 3 | 3 | 3 |

**Drawback:** the agent can react to a situation — an obstacle — **too late**,
and the motion becomes jerky or plainly unnatural.

Note:
The jerkiness has a specific cause: switching winners swaps the whole steering
force in one frame. There is no blending, so there is no transition.

---

### Solution 3 — weighted blending

Every behaviour contributes, scaled by a weight:

```text
   Steering = Seek(food)      * 0.2
            + Flee(predator)  * 0.4
            + Wander          * 0.1
            + Seek(water)     * 0.3
```

**Drawbacks:**

- a very Swiss solution, which may end up satisfying nobody
- two behaviours can **cancel each other out**
- **CPU heavy** — everything is recomputed every frame

Note:
The cancellation case is worth drawing: an obstacle dead ahead, flee-left and
flee-right of equal weight, sum zero, agent walks straight into the wall.

---

### Solution 4 — prioritised dithering

Each behaviour has a **priority** and a **probability**.

| Behaviour | Priority | Probability |
| --- | --- | --- |
| Seek (food) | 1 | 0.5 |
| Flee (predator) | 2 | 0.1 |
| Wander | 5 | 0.9 |
| Seek (water) | 3 | 0.2 |

Each frame, draw a random value in `[0, 1]` and test it against the
highest-priority behaviour:

- value **greater** than the probability **and** the behaviour produces a
  non-zero force → that behaviour runs
- otherwise → draw again and test the **next** priority

---

### Prioritised dithering — worked

```text
   1. random = 0.5  ->  smaller than Wander (0.9, highest priority)  ->  rejected
   2. random = 0.3  ->  greater than Seek(water) (0.2)  ->  Seek(water) runs
```

**Drawback:** finding good probability values is hard, and it can take a very
long time to reach a satisfying set.

Note:
Its virtue is cost: one behaviour is evaluated most frames, and the variety
comes from the dice rather than from the sum. Cheap on CPU, expensive on
designer time.

---

### Solution 5 — weighted prioritised truncated sum

The one most shipped games use:

| Behaviour | Priority | Weight |
| --- | --- | --- |
| Seek (food) | 1 | 0.5 |
| Flee (predator) | 2 | 0.1 |
| Wander | 5 | 0.3 |
| Seek (water) | 3 | 0.1 |

1. Evaluate the behaviours **in priority order**
2. **Add** each force, scaled by its weight
3. If the total exceeds `MAX_FORCE`, **stop** — later behaviours are never
   evaluated
4. The last force added is **truncated** so the total never exceeds `MAX_FORCE`

<small>Drawbacks: none obvious — which is why it wins.</small>

Note:
It gets blending's smoothness, priority's responsiveness, and dithering's early
exit for CPU. The truncation in step 4 is what keeps it stable; skip it and the
agent teleports.

---

# In use
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

- **RTS** — hundreds of units sharing a flow field, kept apart by separation and
  avoidance
- **Flocking** — birds, fish, insect swarms, and any crowd that must feel alive

<!-- TODO: figure d'origine, deck 08, slides ~47-48 (captures RTS et flocking) -->

Note:
Close the loop with the pathfinding lecture: the flow field says *where*, the
steering behaviours say *how*, and neither works alone in a crowd.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `red3d.com/cwr/steer/gdc99/` — Craig Reynolds, the founding paper
- `gamedevelopment.tutsplus.com/series/understanding-steering-behaviors--gamedev-12732` — behaviour by behaviour
- `alastaira.wordpress.com/2013/03/13/methods-for-combining-autonomous-steering-behaviours/` — the five combination methods
- `slsdo.github.io/steering-behaviors/` — interactive demos
- `software.intel.com` — fish flocking in Unity, 3D
- `youtube.com/watch?v=mhjuuHl6qHM`

<small>Unity-side counterpart already in the vault:
[[autonomous_behaviours|Autonomous behaviours]]</small>
