---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Event Bus & Signals
### A 3-Hour Lecture

**2h de cours · 1h d'exercices**

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Agenda

1. **Part 1** - Coupling, the silent killer *(20 min)*
2. **Part 2** - Observer, signals, and the event bus *(25 min)*
3. **Part 3** - Designing a typed signal in C++23 *(35 min)*
4. **Part 4** - Event bus: many publishers, many subscribers *(25 min)*
5. **Part 5** - Pitfalls *(15 min)*
6. **Part 6** - Signals in the City Builder *(20 min)*
7. **Part 7** - Exercises *(1h)*

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 1
## Coupling, the Silent Killer

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.1 - Direct Calls

`tilemap_ptr_->SetTile(...)` from a BT action - who depends on whom?

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.2 - The Dependency Graph Today

Who knows about whom in `game.cc` - drawn out.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.3 - What "Loose Coupling" Buys

Testability, reuse, parallel work - three concrete wins.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.4 - When *Not* to Decouple

Flow is hard to trace through events - the honest disclaimer.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 2
## Observer, Signals, and the Event Bus

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.1 - Observer Pattern

Subject and observers - the GoF version.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.2 - Signal / Slot

Qt and Boost.Signals2 in one slide each.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.3 - Event Bus

A global (or scoped) broker - one channel, many topics.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.4 - Comparing the Three

Coupling, performance, traceability - the trade-off table.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 3
## Designing a Typed Signal in C++23

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.1 - The Shape

`Signal<Args...>` with `Connect`, `Disconnect`, `Emit` - the public surface.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.2 - Storage of Slots

`std::vector` of callables - why not `std::function`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.3 - Concepts-Based Slots

`std::invocable<Args...>` - echo of the templates lecture.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.4 - Connection Handles

RAII tokens that disconnect on destruction.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.5 - Re-Entrancy

Emitting from inside a slot - the deferred-removal trick.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.6 - Move-Only Slots and Lifetime Tracking

Weak references for objects that may die before the signal does.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 4
## Event Bus: Many Publishers, Many Subscribers

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.1 - One Bus, Many Event Types

`std::variant` vs type-keyed map - two designs.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.2 - Synchronous vs Queued Dispatch

The frame boundary as a natural flush point.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.3 - Scoped Buses vs Global

Why the `[SMEL]` guideline matters here - no singletons.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.4 - The Namespace-Based Service Approach

Bus as a module, not a singleton - free functions over hidden state.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 5
## Pitfalls

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.1 - Debugging

The stack trace stops at `Emit` - tools and conventions to compensate.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.2 - Order of Delivery

Never rely on it - the painful lesson.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.3 - Cycles

A emits → B emits → A again - how to detect and break it.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.4 - Lifetime

Dangling slots after the subscriber dies.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.5 - Performance

When a direct call is just better - the honest answer.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 6
## Signals in the City Builder

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 6.1 - `ChopEvent` Today

A function pointer captured in `ResourceManager` - the one-subscriber limit.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 6.2 - Target

`Signal<int, float> on_resource_depleted` on `Resource` - multi-subscriber, typed.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 6.3 - `Clickable::OnReleasedLeft`

Already half a signal - what's missing for multi-subscriber.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 6.4 - Module-Level Bus in `namespace game::events`

No singleton, just free functions over a hidden vector.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 7
## Exercises - 1 Hour

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Exercise 1
## Build a Typed `Signal<Args...>`
### 30 minutes

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## Exercise 1 - Context

Implement `core::Signal<Args...>` with `Connect` returning an RAII `Connection` handle, `Emit(Args...)`, and safe re-entrant emission. Constrain slot types with `std::invocable<Args...>`. Unit test: connect two slots, emit, disconnect one via handle destruction, emit again.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Exercise 2
## Replace `ChopEvent` with a Signal
### 30 minutes

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## Exercise 2 - Context

Remove the function-pointer `ChopEvent` parameter from `ResourceManager::LoadResources`. Add a `Signal<int, float> on_depleted` on `Resource` (or on `ResourceManager`). Have `game.cc` connect a slot that calls `tilemap_ptr_->SetTile(index, kBg)`. Bonus: a second slot that logs the event for debugging - show that multiple subscribers work.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Summary

---

## What We Covered

| Thème | À retenir |
|---|---|
| Couplage | Direct = simple ; signal = découplé mais traçable plus difficilement |
| Observer / signal / bus | Trois échelles du même concept |
| `Signal<Args...>` | Concepts + RAII pour des slots sûrs |
| Event bus | Module avec état caché, pas singleton |
| Pièges | Cycles, ordre, lifetime, debug |
| Application projet | `ChopEvent`, `Clickable`, bus `game::events` |

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Questions?
