---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Command Pattern for UI Actions
### A 3-Hour Lecture

**1h30 de cours · 1h d'exercices · 30 min de bilan**

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Agenda

1. **Part 1** - What is an action, really? *(15 min)*
2. **Part 2** - The Command pattern *(25 min)*
3. **Part 3** - Modern C++ alternatives *(25 min)*
4. **Part 4** - Undo, redo, replay, networking *(20 min)*
5. **Part 5** - Commands in the City Builder *(25 min)*
6. **Part 6** - Exercises *(1h)*

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 1
## What is an Action, Really?

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.1 - The Lambda Trap

`OnReleasedLeft = []{ ... }` in `game.cc` - convenient, then painful.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.2 - What Lambdas Can't Do

Name, serialize, undo, queue, log - five missing verbs.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.3 - The "Verb as Object" Idea

Turning a method call into a value you can store.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.4 - Where This Matters

UI, input remapping, save/replay, networking - the same pattern everywhere.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 2
## The Command Pattern

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.1 - Definition and Intent

Encapsulate a request as an object.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.2 - The GoF Roles

Command, ConcreteCommand, Invoker, Receiver, Client - five characters.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.3 - The Minimal Interface

`Execute()`, optional `Undo()` - that's the whole contract.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.4 - Ownership

Who keeps the command alive, who deletes it, who never should.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 3
## Modern C++ Alternatives

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.1 - Virtual `Command` Base

The classic - still valid, still readable.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.2 - `std::function`

Flexible but allocating - watch the `[STD]` guidelines on hot paths.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.3 - `std::variant` + `std::visit`

Closed-set, zero alloc - the modern default.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.4 - Template-Based Static Dispatch

Concepts + duck-typed `Execute()` when types are known at compile time.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.5 - Trade-Offs Table

Flexibility vs cost vs guideline compliance - one table to choose.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 4
## What Commands Enable

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.1 - Undo / Redo

The history stack - one push per `Execute`, one pop per `Undo`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.2 - Macro Commands

Composite actions - one click, many effects.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.3 - Queueing and Deferred Execution

Running on the next tick instead of mid-frame.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.4 - Replay and Determinism

Recording a session - the same commands give the same game.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.5 - Networking

Commands as the wire format - a tiny protocol.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 5
## Commands in the City Builder

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.1 - The Current UI

Buttons holding lambdas in `game.cc` - what we have today.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.2 - Target Design

`ICommand` (or `variant`) with `Execute()` - where we're going.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.3 - Three Concrete Commands

`PlaceNpcCommand`, `SelectNpcTypeCommand`, `ExitCommand`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.4 - `ChopEvent` Revisited

A `RemoveTileCommand` queued by the BT, drained by the main loop.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.5 - Wiring the Invoker

A `CommandQueue` ticked once per frame - one drain point.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.6 - Where Undo Helps in a City Builder

Placement mistakes, accidental selections - the obvious wins.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 6
## Exercises - 1 Hour

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Exercise 1
## Convert the UI to Commands
### 30 minutes

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## Exercise 1 - Context

Define a `Command` concept (or `variant`) covering the four buttons in `game.cc`. Replace the four `OnReleasedLeft` lambdas with concrete command types stored in the buttons. Wire them through a `CommandQueue` that the main loop drains each frame. No behaviour change - same screen, cleaner code.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Exercise 2
## Undoable NPC Placement
### 30 minutes

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## Exercise 2 - Context

Extend `PlaceNpcCommand` with an `Undo()` method that removes the last placed NPC. Add a history stack in `NpcManager`. Bind Ctrl+Z to pop and undo. Bonus: cap history at N entries with a ring buffer.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Summary

---

## What We Covered

| Thème | À retenir |
|---|---|
| L'action comme objet | Une lambda ne sait pas se nommer ni s'annuler |
| Command pattern | `Execute()` + `Undo()` - contrat minimal |
| Alternatives modernes | `variant` zéro-alloc > `function` |
| Undo / redo | Une pile, une convention |
| Queue de commandes | Un drain par frame, exécution déterministe |
| Application projet | UI, `ChopEvent`, placements annulables |

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Questions?
