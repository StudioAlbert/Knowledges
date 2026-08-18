---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Flyweight Pattern
### A 3-Hour Lecture

**1h30 de cours · 1h d'exercices · 30 min de discussion**

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Agenda

1. **Part 1** - Memory in games: the cost of duplication *(20 min)*
2. **Part 2** - The Flyweight pattern *(25 min)*
3. **Part 3** - Intrinsic vs extrinsic state *(20 min)*
4. **Part 4** - Variants and neighbours *(25 min)*
5. **Part 5** - Flyweight in the City Builder *(20 min)*
6. **Part 6** - Exercises *(1h)*

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 1
## Memory in Games: The Cost of Duplication

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.1 - Why Duplication Hurts

Cache lines, allocator pressure, RAM budget - the three enemies.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.2 - A Concrete Count

200 NPCs × N owned objects each - the arithmetic gets ugly fast.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.3 - The Current State of `Npc`

`unique_ptr` to texture, motor, path, BT - five allocations per NPC.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.4 - The `FIXME` in `npc.h`

The problem the pattern solves, in the author's own words.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 2
## The Flyweight Pattern

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.1 - Definition

Share invariant data across many fine-grained objects.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.2 - The GoF Diagram

Flyweight, FlyweightFactory, Client, Context - the four roles.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.3 - Identity vs Equality

When two NPCs "share" a BT - what that actually means in memory.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.4 - Lifetime and Ownership

Who keeps the shared pieces alive, who never deletes them.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 3
## Intrinsic vs Extrinsic State

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.1 - Intrinsic State

Shared, immutable, lives in the flyweight.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.2 - Extrinsic State

Per-instance, passed in at call time.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.3 - Splitting `NpcBehaviourTree`

Structure (intrinsic) vs hunger/path/resources (extrinsic).

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.4 - The Blackboard Companion Pattern

Where extrinsic state lives in a behaviour tree.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 4
## Variants and Neighbours

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.1 - The Factory

Interning, caching, lookup by key.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.2 - `shared_ptr<const T>` vs Static Pool

Two storage strategies with different trade-offs.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.3 - Comparison with Singleton

Why a registry is not a singleton - and why that matters for `[API] 1`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.4 - Thread-Safety Considerations

Immutable flyweights are easy - the mutable bits are the trap.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.5 - Cousins

Object Pool, Prototype, Interning - what flyweight is *not*.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 5
## Flyweight in the City Builder

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.1 - The Target

Four shared BT structures, one per `NpcType` - no more per-NPC trees.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.2 - The New Shape

`NpcBehaviourTreeStructure` + `NpcBlackboard` - the split.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.3 - Refactoring `Npc`

Replace `unique_ptr<NpcBehaviourTree>` with a pointer to a flyweight + an owned blackboard.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.4 - The Factory

Registered at startup, owned by `NpcManager`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.5 - Measured Impact

`sizeof(Npc)` before/after, allocation count - the numbers that justify the work.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 6
## Exercises - 1 Hour

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Exercise 1
## Share Textures Across NPCs
### 30 minutes

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## Exercise 1 - Context

NPCs currently each own a `unique_ptr<sf::Texture>` even though textures are keyed by `NpcType`. Build a `NpcTextureRegistry` (flyweight factory) returning `const sf::Texture&` per type. Refactor `Npc` to hold only the reference. Verify only 3 textures are loaded regardless of NPC count.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Exercise 2
## Shared Behaviour Trees
### 30 minutes

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## Exercise 2 - Context

Extract the BT *structure* (selector / sequences / actions) from `NpcBehaviourTree` into an immutable `BehaviourTreeStructure` indexed by `NpcType`. Move the mutable state (`hunger_`, `current_ressource_`, `path_`) into a per-NPC `Blackboard` passed to each `Action`. Show that ticking 100 NPCs only walks 4 tree structures.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Summary

---

## What We Covered

| Thème | À retenir |
|---|---|
| Coût de la duplication | Cache, allocator, RAM - mesurer avant d'optimiser |
| Flyweight | Partager l'invariant, isoler le variable |
| Intrinsic / extrinsic | Découper l'état selon ce qui change par instance |
| Blackboard | Compagnon naturel du BT partagé |
| Factory de flyweights | Registre, pas singleton |
| Application projet | 4 BT au lieu de N, textures partagées par type |

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Questions?
