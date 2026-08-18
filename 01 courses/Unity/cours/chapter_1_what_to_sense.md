---
title: Chapter 1 — What to sense
type: course
chapter: "1"
duration_h: 0.75
module: "🐰 - Medium"
section:
  - SAE 2A
topic:
  - Programming
created: 2026-03-17T10:31
source: notion
---
# Chapter 1 — What to sense

# The Perception–Decision–Action loop

The whole chapter lives in the **Sense** box. The NPC's quality of perception directly caps how smart it can appear — a great decision system fed bad percepts produces dumb behavior.

> 💡 **Opening question:** *"What's the difference between a game AI that cheats and one that feels fair?"* The answer is almost always perception — a cheating AI reads global state directly; a fair one only knows what its sensors allow.
> 

![[chapter_1_what_to_sense_01.png]]

Sensing is the **input stage** of this loop. Decisions and actions come later — this chapter only asks: *what can the NPC know?*

---

## a — Physics world

The raw spatial layer. The NPC queries the engine's physics system directly — no game logic, no meaning yet, just geometry.

| Tool | Answers | Unity API |
| --- | --- | --- |
| **Raycast** | Is this point visible from here? | `Physics.Raycast` |
| **Overlap / sphere cast** | What is within range of me? | `Physics.OverlapSphere` |
| **FOV cone** | What is in my field of view? | Sphere cast + `Vector3.Angle` |
| **NavMesh query** | Can I walk there, and how far? | `NavMesh.SamplePosition`, `NavMeshPath` |

> ⚠️ Physics queries return **geometry**, not meaning. Interpretation is the next level's job.
> 

## b — Entities

Once the physics layer says "something is there and visible", the entity layer asks: *what is it, and what state is it in?*

## Identity & state

- **Tags and layers** — coarse identity: enemy, ally, hazard. Also controls which overlap casts return the object.
- **Public component state** — rich context: health ratio, current action, faction. The NPC **reads only**, never writes to another entity's state.
- **Velocity and current action** — enable anticipation. A player charging toward you reads very differently from one retreating. Expose a `currentAction` enum on a `PublicAgentState` component.

## Detection vs Memory

This is the key conceptual split for believable NPC behavior.

|  | Detection | Memory |
| --- | --- | --- |
| **Condition** | Entity currently in FOV | Entity left FOV |
| **Data** | Live position, live state | Last known position + timestamp |
| **NPC behavior** | Track and react in real time | Move to last known pos, investigate |
| **Ends when** | Entity leaves FOV | Timestamp expires → forgotten |

**Why it matters:** without this distinction, the NPC has two broken options — it either always knows where you are (cheat, feels unfair), or it instantly forgets you the moment you leave its FOV (stupid). Memory is the middle ground: the NPC *commits* to investigating where it last saw you, not where you actually are.

The **timestamp** drives decay — after a threshold, the memory expires and the NPC returns to patrol. This produces three distinct behaviors from a single struct field: *react → investigate → give up*.

## c — Strategic level

The highest level — not about individual entities, but about the **state of the battlefield as a whole**.

## World state

Game-level flags held in manager components or scriptable objects: is the objective taken? Is the zone controlled? Read via public interface, never by reaching into unrelated systems.

## Influence maps

A grid overlaid on the level where each cell holds a numerical score (threat, opportunity, danger). The NPC consults the map to pick safe positions or approach routes **without needing to know where every enemy is**. This is what enables flanking, retreat decisions, and safe positioning at a tactical level.

## Team awareness

Ally positions, alive count, known chokepoints — collective context. Even a single NPC benefits from knowing *"I'm the last one alive"* vs *"I have three allies nearby"*.

> 📈 **Progression to share with students:**
> 

> - *"Is something there?"* → Physics
> 

> - *"What is it doing?"* → Entities
> 

> - *"What is the state of the battlefield?"* → Strategic
> 

> Each level requires a wider view and produces richer decisions.
> 

---

# Key references

- *Game AI Pro* vol. 1 — "Perception Systems" (Dave Mark)
- *AI Game Programming Wisdom* — "The Basics of Sensation and Perception" (Steve Rabin)
- GDC 2011 — *Halo: Reach AI Systems* (influence maps, perception pipeline in production)
- GDC 2014 — *The Last of Us AI* (Naughty Dog) — full perception pipeline, decoupled architecture
