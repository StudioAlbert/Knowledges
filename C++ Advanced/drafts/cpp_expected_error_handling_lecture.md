---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# `std::expected` & Error-Handling Discipline
### A 3-Hour Lecture

**2h de cours · 1h d'exercices**

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Agenda

1. **Part 1** - Error categories & the C++ landscape *(20 min)*
2. **Part 2** - Exceptions: when and when not *(20 min)*
3. **Part 3** - `std::optional` vs `std::expected` *(25 min)*
4. **Part 4** - `std::expected` in depth *(35 min)*
5. **Part 5** - Project rules & migration *(20 min)*
6. **Part 6** - Exercises *(1h)*

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 1
## Error Categories & the C++ Landscape

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.1 - Bugs vs Exceptional vs Expected

Three different problems that demand three different answers.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.2 - The Four Classic Strategies

Error codes, output parameters, exceptions, sum types - history in one slide.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.3 - Cost Models

What each strategy costs at runtime and in code clarity.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 1.4 - What "Exception-Safe" Means

Basic, strong, nothrow guarantees - the vocabulary.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 2
## Exceptions: When and When Not

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.1 - Throw / Catch Mechanics

Stack unwinding in one slide.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.2 - `noexcept` and Move Constructors

Why move constructors care about `noexcept`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.3 - When Exceptions Are the Right Answer

The `[ERR] 1` rule explained - things that should not happen.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 2.4 - The Hidden Costs

Code size, latency tails, banned-in-games reality.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 3
## `std::optional` vs `std::expected`

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.1 - `std::optional<T>`

"Maybe a value" - no reason attached.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.2 - `std::expected<T, E>`

"Value or reason why not" - the error gets a name.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.3 - The `[ERR] 3` Rule

Do not abuse `optional` for errors - the project guideline.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 3.4 - Choosing Between Them

A decision tree.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 4
## `std::expected` in Depth

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.1 - Construction and Accessors

`value()`, `error()`, `value_or()`, `has_value()`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.2 - `std::unexpected<E>`

Building the error branch explicitly.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.3 - Monadic Operations

`and_then`, `transform`, `or_else`, `transform_error`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.4 - Designing the Error Type

Enum, struct, hierarchy - what carries information without leaking concerns.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.5 - Chaining Without Nested Ifs

Pipelines of fallible calls read top to bottom.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 4.6 - `[[nodiscard]]` and Forgetting to Check

The compiler as a safety net.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 5
## Project Rules & Migration

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.1 - Recap of the `[ERR]` Guidelines

What this project mandates, in one slide.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.2 - Case Study: `texture_->loadFromFile` in `npc.cc`

The `bool texture_is_fine` pattern rewritten with `expected`.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.3 - Case Study: `AssetManager::Load`

Returning `expected` instead of throwing on missing files.

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## 5.4 - Interop at API Boundaries

Exceptions at boundaries, `expected` internally.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Part 6
## Exercises - 1 Hour

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Exercise 1
## Refactor `Npc::Setup` Texture Loading
### 30 minutes

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## Exercise 1 - Context

Replace the `bool texture_is_fine` pattern in `api/src/ai/npc.cc` with a function returning `std::expected<sf::Texture, TextureError>`. Define a small error enum, chain the fallback to `empty.png` via `or_else`, and log on `transform_error`.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Exercise 2
## Fallible `AssetManager::Load`
### 30 minutes

---
<!-- slide bg="[[01_slide_GP_GA_22_08_22.jpg]]" -->
## Exercise 2 - Context

Modify `core::experimental::AssetManager::Load` so it returns `std::expected<void, LoadError>` where `LoadError` reports which path failed. Update the `ButtonFactory` constructor to handle the result without exceptions. Bonus: a constexpr table mapping `LoadError` codes to human messages.

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Summary

---

## What We Covered

| Thème | À retenir |
|---|---|
| Catégories d'erreurs | Bugs, exceptionnel, attendu - trois traitements distincts |
| Exceptions | Pour l'inattendu uniquement ; coûteuses en jeu vidéo |
| `optional` vs `expected` | `optional` = absence ; `expected` = raison |
| Opérations monadiques | `and_then`, `transform`, `or_else` - pipelines lisibles |
| Type d'erreur | Enum + contexte > exception générique |
| `[[nodiscard]]` | Le compilateur force la vérification |
| Règles projet | `expected` partout en interne, exceptions aux frontières |

---
<!-- slide bg="[[01_slide_fond_GP_22_08_22.jpg]]" -->
# Questions?
