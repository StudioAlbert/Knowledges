---
theme: white
css:
- _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# C++ Ranges

### A modern STL, in 3 hours

<small>5 modules · 10 hands-on examples · C++20 / C++23</small>

<small>Repo: [REPO_URL](REPO_URL)</small>

Note:
Welcome. Each slide links to a runnable folder in the companion repo —
folder name = slide title.

---

## Module 1 — Why Ranges?

<small>Part 1/2 · the iterator problem</small>

---

### 01 — The Iterator Problem

The classic STL forces you to write `begin()` / `end()` everywhere,
and accepts iterator pairs from **different containers** without complaining.

```cpp
std::sort(numbers.begin(), numbers.end());

// Compiles. Crashes at runtime.
auto bad = std::find(numbers.begin(), other.end(), 8);
```

vs.

```cpp
std::ranges::sort(numbers);
auto it = std::ranges::find(numbers, 8);   // safe by construction
```

<small>📁 [`examples/01_the_iterator_problem`](REPO_URL/tree/main/examples/01_the_iterator_problem)</small>

Note:
Iterator pairs are stringly-typed glue. Ranges fix that with a single argument.

---

## Module 1 — Why Ranges?

<small>Part 2/2 · what IS a range?</small>

---

### 02 — Range Concept Basics

A **range** is anything you can call `begin()` / `end()` on.
The standard formalises a *hierarchy* of range concepts.

```cpp
template <std::ranges::range R>
void print_first(const R& r) { /* ... */ }

template <std::ranges::random_access_range R>
auto middle(const R& r) {
    return *(std::ranges::begin(r) + std::ranges::size(r) / 2);
}

middle(std::vector<int>{1,2,3}); // OK
middle(std::list<int>{1,2,3});   // compile error — not random access
```

<small>Concepts: `input_range` → `forward_range` → `bidirectional_range`
→ `random_access_range` → `contiguous_range` (+ `sized_range`).</small>

<small>📁 [`examples/02_range_concept_basics`](REPO_URL/tree/main/examples/02_range_concept_basics)</small>

Note:
The hierarchy mirrors what the iterator categories used to encode,
but in a type-checked, composable way.

---

## Module 2 — Range Algorithms

<small>Part 1/2 · drop-in replacements</small>

---

### 03 — Range Algorithms Basics

Every classic `<algorithm>` has a `std::ranges::` cousin.
They take a **range**, not an iterator pair.

```cpp
std::vector<int> v{5, 2, 8, 1, 9, 3};

std::ranges::sort(v);
auto it       = std::ranges::find(v, 7);
auto [lo, hi] = std::ranges::minmax_element(v);
auto n        = std::ranges::count_if(v, [](int x){ return x > 5; });
```

Bonus: result types are structs (`in`, `out`) — no more lost information
about where the algorithm stopped.

<small>📁 [`examples/03_range_algorithms_basics`](REPO_URL/tree/main/examples/03_range_algorithms_basics)</small>

Note:
The return types of e.g. `ranges::copy` return both the input end and
the output end — useful when chaining.

---

## Module 2 — Range Algorithms

<small>Part 2/2 · projections</small>

---

### 04 — Projections & Constraints

The killer feature: every range algorithm takes an optional **projection**.

```cpp
struct Person { std::string name; int age; };
std::vector<Person> people = /* ... */;

// Sort by age — no lambda.
std::ranges::sort(people, {}, &Person::age);

// Find a 25-year-old.
auto it = std::ranges::find(people, 25, &Person::age);

// Sort by name length — projection can be any callable.
std::ranges::sort(people, {},
                  [](const Person& p) { return p.name.size(); });
```

Compare to the equivalent classic-STL boilerplate.

<small>📁 [`examples/04_projections_and_constraints`](REPO_URL/tree/main/examples/04_projections_and_constraints)</small>

Note:
Projection = "the lens through which the algorithm sees each element".
Pointer-to-member is the most idiomatic projection.

---

## Module 3 — Views & Pipelines

<small>Part 1/2 · lazy evaluation</small>

---

### 05 — Views & Lazy Evaluation

A **view** is a non-owning, lazy range.
Building one is O(1). Work happens during iteration.

```cpp
// Unbounded — but only the first 5 are ever materialised.
for (int x : std::views::iota(0) | std::views::take(5))
    std::cout << x << ' ';

// filter / transform are lazy too — no temporary vector.
auto evens = std::views::iota(1, 20)
           | std::views::filter([](int x){ return x % 2 == 0; });
```

<small>Key views: `iota`, `filter`, `transform`, `take`, `drop`, `reverse`.</small>

<small>📁 [`examples/05_views_lazy_evaluation`](REPO_URL/tree/main/examples/05_views_lazy_evaluation)</small>

Note:
Mental model: a view is a *recipe*, not a result.
Infinite ranges only "work" because nothing is computed up-front.

---

## Module 3 — Views & Pipelines

<small>Part 2/2 · composition</small>

---

### 06 — Composing Pipelines with `|`

Pipe stages together; the whole pipeline becomes a single fused pass.

```cpp
auto revenue = [](const Order& o){ return o.quantity * o.unit_price; };

auto top =
      orders
    | std::views::filter([](const Order& o){ return !o.cancelled; })
    | std::views::transform(revenue);

// Read it aloud: "from orders, keep non-cancelled, compute revenue."
```

The intent is in the type signature — not buried in a hand-written loop.

<small>📁 [`examples/06_composing_pipelines`](REPO_URL/tree/main/examples/06_composing_pipelines)</small>

Note:
Pipelines are the headline feature. They also compose well with
projections from Module 2 — both fight the same enemy: imperative noise.

---

## Module 4 — Lifetimes & Patterns

<small>Part 1/2 · owning vs borrowing</small>

---

### 07 — Owning & Borrowing Views

Views are usually **non-owning**. Dangling is the #1 footgun.

```cpp
// ❌ Returns a view over a dead local.
auto bad() {
    std::vector<int> v{1,2,3};
    return v | std::views::transform([](int x){ return x*2; });
}

// ✅ Piping an rvalue creates an owning_view that adopts the data.
auto good = make_data()
          | std::views::transform([](int x){ return x*2; });
```

The `borrowed_range` concept tags ranges safe to outlive their owner.

```cpp
static_assert( std::ranges::borrowed_range<std::string_view>);
static_assert(!std::ranges::borrowed_range<std::string>);
```

<small>📁 [`examples/07_owning_and_borrowing_views`](REPO_URL/tree/main/examples/07_owning_and_borrowing_views)</small>

Note:
If a function returns a view by value, ask: who owns the data it
references? If the answer is "this stack frame", you have a bug.

---

## Module 4 — Lifetimes & Patterns

<small>Part 2/2 · refactoring</small>

---

### 08 — Refactoring Classic Loops

Side-by-side: same problem, two styles.

```cpp
// Classic — intent diluted in counters and ifs.
double avg(const std::vector<Student>& s) {
    int sum = 0, count = 0;
    for (const auto& st : s) {
        if (st.passed) { sum += st.grade; ++count; }
    }
    return count ? double(sum)/count : 0;
}
```

```cpp
// Ranges — the pipeline reads like a spec.
auto passing = s | std::views::filter(&Student::passed)
                 | std::views::transform(&Student::grade);
```

Same machine code (or better, in many cases). Clearer intent.

<small>📁 [`examples/08_refactoring_classic_loops`](REPO_URL/tree/main/examples/08_refactoring_classic_loops)</small>

Note:
This is where pushback usually appears: "but my loop is fine".
Show the diff on a real codebase — bug rates speak for themselves.

---

## Module 5 — C++23 & Beyond

<small>Part 1/2 · new adaptors</small>

---

### 09 — `enumerate`, `zip`, `chunk`, `slide`, `cartesian_product`

C++23 fills the gaps that C++20 left.

```cpp
for (auto [i, name] : std::views::enumerate(names))
    std::cout << i << ": " << name << '\n';

for (auto [name, age] : std::views::zip(names, ages))
    std::cout << name << " is " << age << '\n';

// Sliding window of 3.
for (auto w : std::views::iota(1,7) | std::views::slide(3)) { /* ... */ }

// Every (x, y) pair.
for (auto [x, y] : std::views::cartesian_product(xs, ys)) { /* ... */ }
```

<small>Requires MSVC 19.34+ / GCC 14+ / Clang 17+.</small>

<small>📁 [`examples/09_cpp23_enumerate_zip_chunk`](REPO_URL/tree/main/examples/09_cpp23_enumerate_zip_chunk)</small>

Note:
`enumerate` finally kills the manual `i++` counter pattern.
`zip` retires `std::transform` with two iterators.

---

## Module 5 — C++23 & Beyond

<small>Part 2/2 · materialising & future</small>

---

### 10 — `std::ranges::to` and What's Next

The missing piece: turn a view back into a container.

```cpp
auto squares = std::views::iota(1, 11)
             | std::views::filter([](int x){ return x % 2 == 0; })
             | std::views::transform([](int x){ return x*x; })
             | std::ranges::to<std::vector<int>>();
```

Works with **any** container — `vector`, `set`, `map`, your own.

**On the horizon:**

- `std::views::concat` — multi-range concatenation
- `std::ranges::fold_left` / `fold_right` — proper reductions
- More lazy adaptors, possibly parallel

<small>📁 [`examples/10_ranges_to_and_future`](REPO_URL/tree/main/examples/10_ranges_to_and_future)
(falls back automatically on older standard libraries)</small>

Note:
Before C++23, materialising a view meant `vector(v.begin(), v.end())`.
Ugly, and didn't work for associative containers without helpers.

---

## Wrap-up

### When to reach for ranges

- **Algorithm + container** → `std::ranges::xxx` (always)
- **Multi-step transform** → views + `|`
- **Index/pair walking** → `enumerate` / `zip`
- **Hot inner loop with non-trivial work** → measure; ranges usually win

### When to think twice

- Need to mutate elements through a complex view → may not compile, by design
- Lifetimes — never return a view over a local
- Older toolchains — check `__cpp_lib_ranges*` feature-test macros

---

## Resources

- 📘 [cppreference: Ranges library](https://en.cppreference.com/w/cpp/ranges)
- 📘 [Eric Niebler — range-v3](https://github.com/ericniebler/range-v3) (the prototype)
- 📺 Tristan Brindle — "An Overview of Standard Ranges" (CppCon)
- 📺 Hannes Hauswedell — "From Iterators to Ranges"
- 💻 This repo: [REPO_URL](REPO_URL)

---

# Questions?

<small>Code: [REPO_URL](REPO_URL)</small>
