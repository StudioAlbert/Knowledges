---
title: Enemy Design
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
source_slides: https://docs.google.com/presentation/d/1A7l6WDBqciNgMD7fQu1YGGjrBMJTJvXNcN5DjXSixrw/edit
---

# Enemy Design
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

<small>The design brief the AI programmer is implementing</small>

Note:
The only lecture of the module that contains no algorithm. It is here on
purpose: an FSM is a means, and this is the end. A student who can write a
perfect behaviour tree and cannot answer "why does the player fight this thing"
has learned half the subject.

---

## Who are the enemies?
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

Entities that **mimic living characters** — plants, insects, mammals, humans —
that can **hurt the player** and could be **killable**.

As opposed to a **hazard**, which cannot be killed but still hurts.

<small>A spike pit is not an enemy. A spike pit that moves towards you is a
design decision.</small>

---

## Four principles
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

- **Form follows attributes** — the silhouette must announce the behaviour
- **Fighting an enemy should be fun**
- **Enemies should be fought, not avoided**
- **Novelty over time**

Note:
"Fought, not avoided" is the one to interrogate. If the optimal play is to run
past, the encounter cost art, animation and AI time for nothing.

---

### The attributes

| | |
| --- | --- |
| Size | Behaviour |
| Speed | Movement |
| Attacks | Aggression |
| Health | |

<small>Form follows these. If two enemies share every attribute, they are one
enemy wearing two skins.</small>

---

### Size

| Class | Definition |
| --- | --- |
| **Short** | no taller than the character's waist |
| **Average** | roughly the player's height |
| **Large** | several heads taller than the player |
| **Huge** | at least twice the player's size |
| **Gigantic** | only fully visible from a distance |

Note:
Size is read before anything else, from further away than anything else. It is
the first promise the enemy makes to the player, and it must be honest.

---

### Speed

- **Non-mobile** (static)
- **Slow**
- **Medium** — matches the player's speed
- **Fast** — faster than the player

<small>Faster than the player removes the option to disengage. That is a
statement about the whole encounter, not just about one enemy.</small>

---

## Why fight them at all?
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

- they have the **loot**
- they **block the path**
- they have the **key**
- you need to take their **power**
- they are **making fun of you**
- …

Note:
Every enemy needs an answer on this slide. "Because it is in the room" is not
one. The last item is not a joke — taunting is a real and cheap motivator.

---

# A taxonomy
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
Eleven archetypes. For each one, ask the class which decision structure from
the module implements it — most are an FSM, a couple need a behaviour tree.

---

### Patroller

Moves back and forth, or up and down, in a **mechanical fashion**. The path can
be more involved than that, but the movement is always **predictable**.

<small>Predictability is the feature: it is what the player learns.</small>

---

### Chaser

**Pursues the player** when approached, or when some other condition is met.

In many games, patrollers **turn into** chasers when they see the player, or
when the player attacks them.

<small>That transition is a two-state FSM — the first one students write.</small>

---

### Shooter

Fires a **projectile**. Shooting patrollers and chasers open fire once the
player is spotted.

Because of the nature of the attack, this enemy tries to **keep its distance**
rather than engage.

---

### Guard

Its AI priority is to **guard an item or a location** — a doorway — rather than
actively pursue the player.

Guarding combines easily with chasing or shooting, once the player steals the
item or gets past.

---

### Flyer

An **aerial patroller** — but the extra dimension earns it its own class.

Flyers can **swoop down**, or fire from a safe distance. They are advanced
enemies: their movement and attack patterns are harder to predict, and players
usually have to **stop to target** them, or commit to a jump attack.

Note:
"The player must stop moving to deal with it" is the real cost of a flyer, and
it is why a room full of them feels oppressive.

---

### Bomber

A flyer that attacks **from above** rather than from the side.

Common in 2D, where the player often cannot use the camera to look up.

---

### Burrower

Has an **invulnerable state** that lets it reach an advantageous position.

The player must **wait for it to emerge** before attacking.

---

### Teleporter

Changes position around the playfield **instantly**. The player must attack
quickly, before it teleports out of harm's way.

Unlike the burrower, there is **no window** — so give the player a way to
disrupt it: a stun, or another disruptive attack.

Note:
The design note is the important half. An enemy that can always escape and that
the player cannot pin is not a challenge, it is a chore.

---

### Blocker

Defends itself with a **shield** or another defensive device. The player can:

- **go around it** — attack from another direction or elevation
- **disarm** it with a specific move
- **break** the shield, or wait out the invulnerable state

---

### Doppelganger

Looks like the player, and has moves, attacks and an AI that **mimic the
player's own**.

It forces the player to use their moves or weapons in an **unusual way** to
defeat "themselves".

---

### Combination

Enemies usually come in **groups**. The combination space of different enemy
types creates **combat puzzles**, forcing the player to think about
**prioritisation** and **positioning**.

Note:
This is where the taxonomy pays off: a shooter alone is boring, a blocker alone
is boring, a blocker in front of a shooter is a puzzle. The encounter is the
unit of design, not the enemy.

---

# Attacks
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

| Family | Examples |
| --- | --- |
| **Melee** | bare hands, fist |
| **Weapon combat** | sword, knife |
| **Projectile** | arc, grenade |
| **Persistent damage** | poison, fire |

**Not every attack needs to deal damage:**

<small>block / parry · knockback · stun · freeze, paralyse, capture ·
repair, heal · buff · thief · leech</small>

Note:
The second list is where enemy variety actually comes from. A healer changes the
whole encounter without doing a single point of damage.

---

# What good design looks like
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

Good enemy design makes behaviours **distinct**, **consistent** and
**discernible** — which makes them **learnable**.

Each new enemy should be tackled in a **different way**.

---

### Don'ts

- **Do not** ship a different look — or just a palette swap — with the same
  function. To the player, they are the same enemy.
- **Do not** ship small changes in HP, damage or speed. To the player, they are
  still the same enemy.

Note:
Both of these are how enemy rosters get padded under deadline, and players see
through both instantly.

---

### Orthogonal unit differentiation

Coined by **Harvey Smith**: each enemy has **unique, statistically independent
attributes**, rather than being a more or less powerful version of another.

It means the player plays **intentionally**, making meaningful tactical
decisions — instead of randomly reacting to what is going on.

<small>Which attributes are the axes of differentiation depends on your game.</small>

Note:
This is the theoretical statement of the two "don'ts". Orthogonal means: knowing
how to fight A tells you nothing about how to fight B.

---

### The decisions you are designing for

| Decision | Question the player asks |
| --- | --- |
| **Prioritisation** | which enemy do I take first? |
| **Positioning** | what sequence of movement do I make? |
| **Resources** | which weapon against which enemy? |

<small>If an encounter produces none of these three questions, it is not an
encounter.</small>

---

### Do's

- It is easy to design **"deal with me first"** enemies — also explore
  **"deal with me last"**: enemies that get more aggressive each time you hit
  them, high HP, low damage
- **Timing** — give enemies vulnerable and stronger windows
- **Range** — mix close- and long-range enemies
- **Enemy counters player** — design enemies that counter player actions

---

### Do's — continued

- **Player counters enemy** — give a power that lets the player defeat an enemy
  they previously could not
- **Player attention** — **telegraphed** strong attacks that demand the player's
  focus

<small>The telegraph is a contract: the attack is unblockable *and* announced.</small>

Note:
Sekiro's perilous attack symbol is the canonical example — a full-screen glyph
that says "this one is different, react now". The AI side of it is trivial; the
readability work is everything.

---

### The perilous attack symbol

<!-- TODO: figure d'origine, deck 04, slide ~24 (symbole d'attaque périlleuse) -->

<small>One glyph, and the player has all the information they need.</small>

---

# Conclusion
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

As in the level design course, **enemies are architectural elements** in your
game. Placing them matters as much as placing platforms and walls.

**Variety is key** when designing level progression — and the same rule applies
to enemies.

Note:
Close by pointing forward: everything the designer decided here becomes an FSM,
a behaviour tree or a steering behaviour in the lectures that follow. The
implementation is downstream of this slide.

---

# Resources
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- **Game Maker's Toolkit** — `youtube.com/channel/UCqJ-Xo29CKyLTjn6z2XwYAw`
- *Rules of the Game: Five techniques from quite inventive designers* —
  `youtube.com/watch?v=d8QAVGeEj-U`
- Scott Rogers, **Level Up! The Guide to Great Video Game Design**

<small>Implementation lectures: [[ai_decision_algorithms]] ·
[[ai_steering_behavior]]</small>
