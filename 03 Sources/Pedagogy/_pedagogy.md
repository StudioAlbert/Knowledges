# Pedagogy reference

## Backward Design (Wiggins & McTighe, *Understanding by Design*, 1998/2005)

1. Identify desired results → 2. Determine acceptable evidence → 3. Plan learning experiences.
Two failure modes it prevents: "activity-oriented" teaching (fun, aimless) and "coverage"
teaching (march through content, no goal). Related: Biggs' constructive alignment (1996).

## Revised Bloom's taxonomy (Anderson & Krathwohl, 2001)

| Level | Outcome verbs | Programming-flavoured tasks |
|---|---|---|
| Remember | list, name, identify, recall | List the steps of A*; name the RAII principle |
| Understand | explain, describe, trace, summarize, classify | Trace an FSM by hand; explain why a move is cheaper than a copy |
| Apply | implement, use, execute, compute | Implement a state from a template; use `std::priority_queue` for the open set |
| Analyze | debug, compare, differentiate, profile, decompose | Find why an agent oscillates; compare two heuristics on the same map |
| Evaluate | justify, critique, choose, assess, defend | Choose FSM vs behavior tree for a boss and defend it; code-review a peer |
| Create | design, architect, compose, build (from scratch), generate | Design an original enemy AI; architect a PCG pipeline |

Tagging pitfalls:
- "Implement" from a given skeleton is **Apply**; designing the structure yourself is **Create**.
- Multiple-choice questions rarely exceed Analyze; Evaluate/Create need open answers or projects.
- Debugging an unfamiliar bug is Analyze; fixing a bug you were told about is Apply.

## Cognitive Load Theory (Sweller 1988; Sweller, van Merriënboer & Paas 1998, 2019)

Working memory holds few new elements; schemas in long-term memory count as one.

- **Intrinsic load**: element interactivity of the content. Manage by sequencing
  (isolated elements first, then integrate).
- **Extraneous load**: caused by poor design. Eliminate.
- **Germane load**: effort spent building schemas; maximize the share of working memory
  devoted to intrinsic load.

Techniques to apply:
- **Worked example effect**: novices learn more from studying solved examples than from
  solving equivalent problems.
- **Completion problems / fading**: full example → partial code with gaps → blank file.
- **Split-attention**: integrate explanation and code physically.
- **Redundancy**: remove information that repeats or isn't needed.
- **Expertise reversal** (Kalyuga et al., 2003): heavy guidance hurts experts; make
  scaffolding optional for advanced students.
- **Isolated–interacting elements**: for very complex topics, teach parts alone first.

Further reading: van Merriënboer & Kirschner, *Ten Steps to Complex Learning* (2018),
a full design model for project-based courses built on CLT.
