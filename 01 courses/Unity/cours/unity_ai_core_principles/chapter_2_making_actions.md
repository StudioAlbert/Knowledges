---
title: Chapter 2 — Making actions
type: section
module: "🐰 - Medium"
section:
  - Game Sup 2A
  - SAE 1A
parent: "[[unity_ai_core_principles|Unity AI - Core principles]]"
source: notion
---
# Chapter 2 — Making actions

# Acting on the world

Once an NPC knows what is around it, it needs to decide **what to do** — and then do it. This chapter covers how to design, structure, and select actions so the AI behaves in a believable, responsive way.

> 💡 An action is not just an animation. It is a **contract**: it has preconditions that must be met before it can fire, a score that reflects how desirable it is right now, and an effect that changes the world state.
> 

---

# Action taxonomy

Actions can be grouped by their purpose. A well-designed NPC draws from all five categories depending on the situation.

| Category | Examples |
| --- | --- |
| **Movement** | Move to position, strafe, retreat, flank |
| **Combat** | Attack melee, shoot, throw grenade, block |
| **Tactical** | Take cover, peek, reload, call for backup |
| **World interaction** | Use health pack, open door, interact with objective |
| **Communication** | Signal ally, taunt, suppress |

---

# The three things every action needs

Every action is a contract between the AI and the game world. It must answer three questions:

**Preconditions** are boolean checks on world state — they gate which actions are even eligible this tick. **Score** is a 0–1 value computed from context (health ratio, distance, threat level, cooldown). The highest-scoring eligible action is selected. **Effect** declares what the action changes in world state when it completes, feeding back into the sensor layer so the next decision cycle is accurate.

[https://link.excalidraw.com/readonly/x8ZFy3ycF6HNPYyQOecm?darkMode=true](https://link.excalidraw.com/readonly/x8ZFy3ycF6HNPYyQOecm?darkMode=true)

> Scores can be shaped with **response curves** (exponential, logistic, step) to control how sharply an action reacts to context changes — this is what makes AI feel tunable rather than hardcoded.
> 

---

# How the NPC selects an action

The action list defined above is just raw material. A **decision algorithm** is needed to select which action to execute. Three main approaches exist:

[https://link.excalidraw.com/readonly/nS05DoenYMyd9eVA2jWX?darkMode=true](https://link.excalidraw.com/readonly/nS05DoenYMyd9eVA2jWX?darkMode=true)

| Algorithm | How it selects | Best for |
| --- | --- | --- |
| **Finite State Machine (FSM)** | Explicit transitions between states, each state maps to an action | Simple, predictable NPCs with few behaviors |
| **Behaviour Tree (BT)** | Hierarchical tree of conditions and tasks, traversed each tick | Complex NPCs with structured, readable logic |
| **Utility AI** | Scores all eligible actions, picks the highest each tick | Emergent, tunable behavior across many actions |

All three consume the same action contract (preconditions, score, effect) — the algorithm is the layer above that decides *which* action wins.

## Action interruption

Every running action must handle being interrupted cleanly. A new highest-scoring action can preempt an ongoing one at any tick. The interrupted action must leave the world in a consistent state.

Interruption is what makes the AI feel **reactive** rather than rigid. Without it, the NPC finishes a long animation before responding to a sudden threat.

---

# Design principles

- **Keep actions atomic** — one action does one thing. Compound behaviors (flank-then-shoot) are composed from smaller actions by the decision layer, not baked into a single action.
- **Expose score weights as data** — never hardcode a multiplier. Designers should be able to tune `retreatWeight`, `aggressionBias`, etc. without touching code.
- **Actions don't know about each other** — an action reads context and returns a score. It never checks what other actions are doing or bypasses the selector.
- **Cooldowns are scores, not locks** — rather than hard-blocking a recently used action, apply a decay curve to its score. This produces softer, more natural behavior.

---

# Key references

- [*Behavioral Mathematics for Game AI* — Dave Mark](https://www.amazon.com/Behavioral-Mathematics-Game-AI-Applied/dp/1584506849) — the scoring and response curve bible
- [GDC 2012 — "Embracing the Dark Art of Mathematical Modeling in AI" (Dave Mark & Kevin Dill) — GDC Vault](https://gdcvault.com/play/1015955/Embracing-the-Dark-Art-of) — canonical utility AI talk
- [Game AI Pro vol. 2 — "Architecture Tricks: Managing Behaviors in Time, Space, and Depth" — free PDF](http://www.gameaipro.com/GameAIPro2/GameAIPro2_Chapter03_Architecture_Tricks_Managing_Behaviors_in_Time_Space_and_Depth.pdf)
