---
theme: white
css:
- _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# C++ Ranges

### A modern STL, in 3 hours

<small>6 modules · 10 examples · 2 exercises · C++20 / C++23</small>

<small>Repo: [github.com/SAE-Geneve/CPlusPlus_Course_Ranges](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges)</small>

Note:
Welcome. Each slide links to a runnable folder in the companion repo —
folder name = slide title.

---

## Module 1 — Why Ranges?

<small>Part 1/4 · the STL tax · verbosity</small>

---

### The STL Tax

An everyday task with the classic STL: sort people, pull out their
names, find someone. Notice the *ceremony*.

```cpp
struct Person { std::string name; int age; };
std::vector<Person> people = /* ... */;

// begin()/end() on every call.
std::sort(people.begin(), people.end(),
          [](const Person& a, const Person& b){ return a.age < b.age; });

// Manual reserve + back_inserter just to move data between containers.
std::vector<std::string> names;
names.reserve(people.size());
std::transform(people.begin(), people.end(),
               std::back_inserter(names),
               [](const Person& p){ return p.name; });

// A lambda for the most trivial predicate imaginable.
auto it = std::find_if(people.begin(), people.end(),
                       [](const Person& p){ return p.age == 25; });
```

<small>Three operations, and not one of them fits on a single line.</small>

Note:
Every call repeats `begin()/end()`. Every projection or predicate becomes a
lambda. Moving data between containers needs `reserve` + an inserter by hand.
This is the baseline we are about to improve.

---

## Module 1 — Why Ranges?

<small>Part 2/4 · the STL tax · and it's unsafe</small>

---

### …And It Won't Even Keep You Safe

Same code as the last slide — but every snippet hides a bug the
compiler accepts without a word.

```cpp
// Iterator pair from two different containers — compiles, UB at runtime.
auto it = std::find_if(people.begin(), other.end(),
                       [](const Person& p){ return p.age == 25; });

// Wrote begin() instead of back_inserter — names is empty → OOB write.
std::transform(people.begin(), people.end(), names.begin(),
               [](const Person& p){ return p.name; });

// `it` dangles the moment the element it points at is erased.
people.erase(it);
std::cout << it->name;
```

<small>Every one of these compiles cleanly. The verbosity is where the
bugs hide.</small>

Note:
None of these are exotic. They are the exact mistakes the boilerplate on the
previous slide invites — and the type system never flags them.

---

## Module 1 — Why Ranges?

<small>Part 3/4 · ranges to the rescue</small>

---

### 01 — The Iterator Problem

The same three operations, with ranges. One argument each, projections
instead of lambdas, and the cross-container bug becomes impossible.

```cpp
std::ranges::sort(people, {}, &Person::age);

auto names = people | std::views::transform(&Person::name)
                    | std::ranges::to<std::vector>();

auto it = std::ranges::find(people, 25, &Person::age);
// Mixing containers no longer type-checks — the runtime bug is gone.
```

<small>📁 [`examples/01_the_iterator_problem`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/01_the_iterator_problem)</small>

Note:
Everything on the last two slides — the verbosity *and* the silent bugs —
collapses to this. Iterator pairs were stringly-typed glue; a range is a
single, type-checked argument.

---

## Module 1 — Why Ranges?

<small>Part 4/4 · what IS a range?</small>

---

### 02 — Range Concept Basics

A **range** is just *"something with iterators"* — anything you can
call `begin()` / `end()` on. Almost every standard container qualifies,
and so does a plain C array.

```cpp
template <std::ranges::range R>
void show(const R& r) { for (auto&& e : r) /* ... */ ; }

std::vector<int>   v {1, 2, 3};
std::array<int, 3> a {1, 2, 3};
std::string        s {"hi"};
int                c[] {1, 2, 3};      // even a raw C array
std::map<int,int>  m {{1, 1}};
show(v); show(a); show(s); show(c); show(m);   // all ranges

// ❌ NOT ranges: std::stack / std::queue / std::priority_queue
//    — container *adaptors*: they have no begin()/end().
```

<small>If it exposes `begin()`/`end()`, every ranges algorithm and view
accepts it directly — no iterator pairs.</small>

<small>📁 [`examples/02_range_concept_basics`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/02_range_concept_basics)</small>

Note:
"Range = iterator-able" is the whole mental model here. The deeper
question — *how powerful* are those iterators — gets its own module
later (The Range Hierarchy).

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

<small>📁 [`examples/03_range_algorithms_basics`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/03_range_algorithms_basics)</small>

Note:
The return types of e.g. `ranges::copy` return both the input end and
the output end — useful when chaining.

---

### 04 — Composing Pipelines with `|`

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

<small>📁 [`examples/04_composing_pipelines`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/04_composing_pipelines)</small>

Note:
Pipelines are the headline feature. They also compose well with
projections from Module 2 — both fight the same enemy: imperative noise.

---

### Why `auto`, Not the Type

A pipeline's type is a deeply nested, compiler-generated template —
practically unspellable, and **not** a stable API you should write down.

```cpp
// Actual type ≈
//   transform_view<filter_view<ref_view<vector<Order>>>, F>
auto pipe = orders
          | std::views::filter([](const Order& o){ return !o.cancelled; })
          | std::views::transform(revenue);

// Insert or reorder a stage → the type changes; these lines do NOT:
auto pipe2 = orders
           | std::views::filter([](const Order& o){ return !o.cancelled; })
           | std::views::take(10)              // new stage
           | std::views::transform(revenue);

for (auto value : pipe2) use(value);           // consumption unchanged
```

`auto` absorbs whatever the adaptors produce: you can grow or rewire the
pipeline freely — neither the variable's declaration nor the loop that
iterates it has to change.

<small>Pass pipelines around as `template <std::ranges::range R>` or
`auto&&` — never a spelled-out view type.</small>

Note:
The view type is an implementation detail of the adaptor chain. Spelling
it couples your code to the exact stages; `auto` (and the `range` concept
for parameters) keeps the call site stable as the pipeline evolves.

---

## Module 2 — Range Algorithms

<small>Part 2/2 · projections</small>

---

### 05 — Projections & Constraints

A **projection** is a unary callable the algorithm applies to each
element *before* it compares or tests it.

Typical use cases:

- **Sort / search by a field** — order `people` by `age`, find by `id`,
  with no hand-written comparator.
- **Compare by a derived key** — case-insensitive sort, nearest-to-zero,
  newest-first: project through `toupper` / `abs` / a timestamp.
- **Reach through indirection** — sort a `vector<unique_ptr<T>>` or
  `vector<T*>` by the pointee, not by the pointer value.

---

The signature is always `(range, value-or-comparator, projection)`.
`{}` means "use the default" (`std::less` / identity). A
pointer-to-member is the idiomatic projection.

```cpp
struct Person { int id; std::string name; };
std::vector<Person> people = /* ... */;

// 1 · By a field — pointer-to-member, no comparator.
std::ranges::sort(people, {}, &Person::name);
auto p = std::ranges::find(people, 42, &Person::id);

// 2 · By a derived key — projection is any callable.
std::ranges::sort(words, {}, [](auto& s){ return std::tolower(s[0]); });
auto z = std::ranges::min(xs, {}, [](int x){ return std::abs(x); });

// 3 · Through indirection — order by the pointee, not the pointer.
std::vector<std::unique_ptr<Person>> ptrs = /* ... */;
std::ranges::sort(ptrs, {}, [](auto& up){ return up->id; });
```

Compare to the equivalent classic-STL boilerplate.

<small>📁 [`examples/05_projections_and_constraints`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/05_projections_and_constraints)</small>

Note:
Without projections you'd hand-write a comparator lambda for every
"sort/find by field". The projection keeps the algorithm generic and
the call site declarative — one concept replaces a pile of lambdas.

---

## Module 3 — Views & Pipelines

<small>Part 1/2 · lazy evaluation</small>

---

### 06 — Views & Lazy Evaluation

A **view** is a non-owning, lazy range.
Building one is O(1). Work happens during iteration — and *only* for
the elements you actually consume.

```cpp
std::vector<int> big(1'000'000);   // a million elements

// EAGER: allocates a 1,000,000-element vector and runs 1,000,000
// multiplications — then throws away all but the first 3.
std::vector<int> sq;
std::transform(big.begin(), big.end(), std::back_inserter(sq),
               [](int x){ return x * x; });
auto first3 = std::vector(sq.begin(), sq.begin() + 3);

// LAZY: no allocation, no work, until the loop pulls 3 elements.
auto v = big | std::views::transform([](int x){ return x * x; })
             | std::views::take(3);
for (int x : v) use(x);            // exactly 3 multiplications, 0 temporaries
```
---
The lazy cost is proportional to what you **consume**, not to what you
**have** — which is also why an infinite range works at all:

```cpp
for (int x : std::views::iota(0) | std::views::take(5))  // never blocks
    std::cout << x << ' ';
```

<small>Key views: `iota`, `filter`, `transform`, `take`, `drop`, `reverse`.</small>

<small>📁 [`examples/06_views_lazy_evaluation`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/06_views_lazy_evaluation)</small>

Note:
The benefit is concrete: same result, but the eager version did ~1M
multiplications plus a heap allocation while the lazy one did 3 and none.
A view is a *recipe*, not a result — infinite ranges only "work"
because nothing is computed up-front.

---

### `transform`: View or Algorithm?

`transform` names **two different tools** — easy to call the wrong one.

```cpp
std::vector<int> v{1, 2, 3};

// views::transform — lazy VIEW. Does NOT touch v. Recomputed on access.
auto doubled = v | std::views::transform([](int x){ return x*2; });
//   reading doubled → 2 4 6        v is still {1, 2, 3}

// ranges::transform — eager ALGORITHM. Writes a destination, once.
std::ranges::transform(v, v.begin(), [](int x){ return x*2; }); // v → 2 4 6
```

| | `std::views::transform` | `std::ranges::transform` |
|---|---|---|
| Kind | lazy view adaptor | eager algorithm |
| Mutates input | no | only if dest **is** the input |
| Stored output | none — recomputed each pass | yes — into the dest you give |

<small>Need a real container out of a view? Materialise it:
`… | std::ranges::to<std::vector>()`.</small>

Note:
The view never modifies the source and caches nothing — a 3-pass loop
calls the function 3× per element. To change data, either materialise
the view or use the algorithm form.

---

## Module 4 — Lifetimes & Patterns

<small>Part 1/2 · owning views</small>

---

### 07 — Owning Views

Views are usually **non-owning** — they only borrow their elements.
Dangling is the #1 footgun.

```cpp
// make_data() constructs a vector and returns it BY VALUE (a temporary).
std::vector<int> make_data() {
    return {1, 2, 3, 4, 5};
}

// ❌ Bind to a NAMED LOCAL, then view it. The view is non-owning, so it dangles the instant `data` leaves scope.
auto bad() {
    std::vector<int> data = make_data();
    return data | std::views::transform([](int x){ return x*2; });
}                          // `data` destroyed → returned view dangles

// ✅ Pipe the RVALUE directly: it is MOVED into a std::ranges::owning_view that holds the vector for as long as
//    the pipeline object lives — safe to return.
auto good() {
    return make_data()
         | std::views::transform([](int x){ return x*2; });
}
```

Rule of thumb: pipe an **lvalue** → the view *refers* to it (you own
the lifetime); pipe an **rvalue** → an `owning_view` *adopts* it (safe).

<small>📁 [`examples/07_owning_views`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/07_owning_views)</small>

Note:
Both functions use the *same* `make_data()` — the only difference is
lvalue vs rvalue. A named local is merely referred to (dangles); the
temporary is adopted by `owning_view` (safe). That is the whole rule.

---

## Module 4 — Lifetimes & Patterns

<small>Part 2/2 · borrowing views</small>

---

### 08 — Borrowing Views

A **borrowed range** is one whose iterators stay valid *even after the
range expression itself is gone* — because it never owned the elements;
it only refers to storage owned somewhere else.

```cpp
static_assert( std::ranges::borrowed_range<std::string_view>); // refers
static_assert( std::ranges::borrowed_range<std::span<int>>);   // refers
static_assert(!std::ranges::borrowed_range<std::string>);      // owns
```

Why it matters — the algorithm protects you at **compile time**:

```cpp
auto it = std::ranges::find(std::vector{1,2,3}, 2);
// decltype(it) == std::ranges::dangling — dereferencing it won't compile.
```

<small>An lvalue container is borrowed (it outlives the call); a temporary
is not. Opt your own type in via `std::ranges::enable_borrowed_range`.</small>

<small>📁 [`examples/08_borrowing_views`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/08_borrowing_views)</small>

Note:
"Borrowed" = iterator validity is not tied to the range object's
lifetime. `find` on a temporary returns `dangling` instead of an
iterator — the previous slide's footgun, caught by the type system.

---

### 09 — `std::ranges::to`

The missing piece: turn a view back into a container.

```cpp
auto squares = std::views::iota(1, 11)
             | std::views::filter([](int x){ return x % 2 == 0; })
             | std::views::transform([](int x){ return x*x; })
             | std::ranges::to<std::vector<int>>();
```

Works with **any** container — `vector`, `set`, `map`, your own.

<small>📁 [`examples/09_ranges_to`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/09_ranges_to)</small>

---

## Module 5 — The Range Hierarchy

<small>how powerful is your range?</small>

---

### The Range Hierarchy

The standard grades ranges into **five tiers** by how powerful their
iterator is. Each tier *refines* the previous one — it is a strict
**superset**: it keeps every guarantee and adds one capability.

| Range / view | Weakest tier it satisfies |
|---|---|
| `istream` view, a generator | `input_range` |
| `forward_list`, `unordered_set` | `forward_range` |
| `list`, `set`, `map` | `bidirectional_range` |
| `deque` | `random_access_range` |
| `vector`, `array`, `string`, `span` | `contiguous_range` |

<small>`sized_range` is **orthogonal** — not a tier. It only promises
`std::ranges::size(r)` is O(1), and can be true (or not) at any tier.</small>

Note:
Same ladder the old iterator categories encoded, but lifted to the
range level and made a checkable concept instead of a tag you had to
know by heart. The next slides take one tier each.

---

### Tier 1 — `input_range`

Read each element **once**, moving forward only. Advancing consumes
position — there is no going back, no second pass.

```cpp
// Tokens off std::cin — you cannot rewind a keyboard.
auto in = std::views::istream<int>(std::cin);

for (int x : in) use(x);   // each value seen exactly once
// Iterating `in` again would NOT replay the same values.
```

<small>Models: `std::ranges::istream_view`, coroutine generators, any
lazily-produced stream.</small>

Note:
This is the weakest, most permissive tier — algorithms that only need
to touch each element once (e.g. `for_each`, `copy`) accept it.

---

### Tier 2 — `forward_range`

Adds **multi-pass**: save an iterator, traverse, then start over and
get the same elements again.

```cpp
std::forward_list<int> fl{1, 2, 3};

std::ranges::for_each(fl, pass1);   // first traversal
std::ranges::for_each(fl, pass2);   // again — identical elements
```

<small>Models: `std::forward_list`, `std::unordered_set` / `unordered_map`.
A singly-linked list: you may restart from the head, but only go forward.</small>

Note:
First tier where two-pass algorithms (count-then-process) are valid.

---

### Tier 3 — `bidirectional_range`

Everything forward gives you, **plus `--it`** — you can also walk
backwards.

```cpp
std::list<int> l{1, 2, 3};

for (int x : l | std::views::reverse)   // needs backward iteration
    std::cout << x;                     // 3 2 1
```

<small>Models: `std::list` (doubly-linked), `std::set`, `std::map` (trees).
You can step left or right — but reaching the Nth element is still N steps.</small>

Note:
`std::views::reverse` is the canonical thing that *requires* this tier.

---

### Tier 4 — `random_access_range`

Iterator arithmetic: `it + n`, `it - it2`, `it[n]`, ordering. Reaching
**any** element is O(1).

```cpp
auto r = std::views::iota(0, 10);      // 0,1,…,9 — no container needed

int x   = r[5];                        // 5 — O(1), no stepping
auto mid = r.begin() + r.size() / 2;   // iterator arithmetic
```

<small>`iota_view` is random-access but **not** contiguous (no backing
array). 
This is why `std::ranges::sort(std::list{...})` fails to compile.</small>

Note:
Binary search, `nth_element`, `sort` — all gated on this tier.

---

### Tier 5 — `contiguous_range`

The strongest: elements sit **consecutively in memory**, so
`&r[0] + n == &r[n]` and a raw `T*` is a valid iterator.

```cpp
std::vector<int> v{1, 2, 3, 4};

int* p = std::ranges::data(v);          // a real, valid pointer
std::fwrite(p, sizeof(int), v.size(), f); // hand straight to a C API
```

<small>Models: `std::vector`, `std::array`, `std::string`, `std::span`.
`std::deque` does **not** qualify — its storage is chunked, not one block.</small>

Note:
The tier that lets you interop with C, `memcpy`, and SIMD.

---

### Climbing the Tiers — One Example

A function constrains on the **weakest tier it actually needs**. That
constraint *is* the compile-time contract.

```cpp
template <std::ranges::random_access_range R>
auto middle(const R& r) {
    return *(std::ranges::begin(r) + std::ranges::size(r) / 2);
}

middle(std::vector{1,2,3,4});   // ✅ contiguous  ⊇ random_access
middle(std::deque{1,2,3,4});    // ✅ exactly random_access
middle(std::list{1,2,3,4});     // ❌ only bidirectional — won't compile
middle(std::views::istream<int>(std::cin)); // ❌ only input — won't compile
```

<small>Pass a **stronger** range where a weaker tier is asked → fine
(superset). Pass a **weaker** one → the concept rejects it, at compile
time, with the requirement named in the signature.</small>

Note:
Same principle behind `sort` needing `random_access_range`. The concept
in the signature both documents and enforces the requirement — the
unwritten "needs a random-access iterator" convention is now checked.

---

## Module 6 — C++23 & Beyond

<small>Part 1/2 · new adaptors</small>

---

### 10 — `enumerate`, `zip`, `chunk`, `slide`, `cartesian_product`

C++23 fills the gaps that C++20 left.

```cpp
// enumerate → [index, value]; full demo in Exercise 2 (leaderboard).
for (auto [i, x] : std::views::enumerate(r)) rank(i + 1, x);

for (auto [name, age] : std::views::zip(names, ages))
    std::cout << name << " is " << age << '\n';

// Sliding window of 3.
for (auto w : std::views::iota(1,7) | std::views::slide(3)) { /* ... */ }

// Every (x, y) pair.
for (auto [x, y] : std::views::cartesian_product(xs, ys)) { /* ... */ }
```

<small>Requires MSVC 19.34+ / GCC 14+ / Clang 17+.</small>

<small>📁 [`examples/10_cpp23_enumerate_zip_chunk`](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges/tree/main/examples/10_cpp23_enumerate_zip_chunk)</small>

Note:
`enumerate` finally kills the manual `i++` counter pattern.
`zip` retires `std::transform` with two iterators.

---

## Exercises

---

### Exercise 1 — Refactor a Classic Loop

Rewrite this imperative loop as a **ranges pipeline**.

```cpp
struct Student { std::string name; int grade; bool passed; };

// Average grade of the students who passed.
double avg(const std::vector<Student>& s) {
    int sum = 0, count = 0;
    for (const auto& st : s) {
        if (st.passed) { sum += st.grade; ++count; }
    }
    return count ? double(sum) / count : 0;
}
```

**Your task:**

1. Build a view that `filter`s the students who **passed**, then
   `transform`s each to its **grade**.
2. Use **pointer-to-member projections** (`&Student::passed`,
   `&Student::grade`) — no hand-written lambdas.
3. Compute the average from that range (C++23 `std::ranges::fold_left`,
   or materialise with `std::ranges::to<std::vector>()` and accumulate).
4. Keep the empty-input case correct — return `0`, never divide by zero.

<small>Goal: the body should read like its spec — *"average of passing
grades"* — with no manual counters or `if`.</small>

Note:
Reference solution:
`auto passing = s | std::views::filter(&Student::passed)
                  | std::views::transform(&Student::grade);`
C++23: `int n = std::ranges::distance(passing);` then
`return n ? double(std::ranges::fold_left(passing, 0, std::plus{})) / n : 0;`
Pre-C++23: materialise `passing` with `std::ranges::to<std::vector>()`,
then `std::accumulate`. Classic pushback: "but my loop is fine" — show
bug rates on a real codebase.

---

### Exercise 1 — Solution

The loop collapses to a **filter → transform** pipeline; the average is
a single fold over it.

```cpp
double avg(const std::vector<Student>& s) {
    auto passing = s | std::views::filter(&Student::passed)
                     | std::views::transform(&Student::grade);

    const auto n = std::ranges::distance(passing);
    if (n == 0) return 0;                       // empty-input guard

    return double(std::ranges::fold_left(passing, 0, std::plus{})) / n;
}
```

<small>Pre-C++23 — no `fold_left`: materialise, then `accumulate`.</small>

```cpp
auto v = passing | std::ranges::to<std::vector>();
return v.empty() ? 0
                 : double(std::accumulate(v.begin(), v.end(), 0)) / v.size();
```

Note:
The body now reads like its spec. `filter`/`transform` are lazy, so the
C++23 path materialises nothing — `fold_left` consumes the view directly.
Caveat: `distance` walks `passing` once and the fold walks it again (two
passes); fine here, but for a single pass fold while counting.

---

### Exercise 2 — Top-3 Followers Leaderboard

Print a ranked leaderboard of your **top 3 followers** by score.

```cpp
struct Player { int id; std::string name; int score; bool is_follower; };
std::vector<Player> players = /* ... */;

// Classic: copy followers out, sort by score desc, print 3 with a rank.
std::vector<Player> f;
for (const auto& p : players)
    if (p.is_follower) f.push_back(p);
std::sort(f.begin(), f.end(),
          [](const Player& a, const Player& b){ return a.score > b.score; });
for (std::size_t i = 0; i < f.size() && i < 3; ++i)
    std::cout << (i + 1) << ". " << f[i].name << " — " << f[i].score << '\n';
```

**Your task:**

1. `filter` players where `is_follower`, then **materialise**
   (`std::ranges::to<std::vector>()`) — sorting needs a real container.
2. `std::ranges::sort` by `score` **descending** via the `&Player::score`
   projection + `std::ranges::greater{}` — no comparator lambda.
3. Print the first 3 with their **rank**: `take(3)` piped into
   `std::views::enumerate`, so the index *is* the position.

<small>Why materialise? `sort` needs a `random_access_range` and mutates
in place — a lazy `filter` view cannot be sorted directly.</small>

Note:
Deliberately mixes a view (`filter`) with an algorithm (`sort`) — the
"view vs algorithm" / hierarchy teaching point. `enumerate` turns the
manual `i++` counter into the rank for free.

---

### Exercise 2 — Solution

```cpp
void leaderboard(const std::vector<Player>& players) {
    auto top = players | std::views::filter(&Player::is_follower)
                        | std::ranges::to<std::vector>();      // sortable

    std::ranges::sort(top, std::ranges::greater{}, &Player::score);

    for (auto [i, p] : top | std::views::take(3)
                           | std::views::enumerate)
        std::cout << (i + 1) << ". " << p.name
                  << " — " << p.score << '\n';
}
```

<small>`std::ranges::greater{}` + `&Player::score` = "by score, high to
low" with no comparator. `enumerate` yields `[index, value]`; `i + 1`
is the 1-based rank.</small>

Note:
`filter` is lazy; `ranges::to` materialises only the followers (not all
players) so `sort` gets a contiguous container. `take(3)` caps the
output; `enumerate` supplies the rank. Pre-C++23: drop `enumerate` and
`zip` with `std::views::iota(1)`, or keep a manual counter.

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
- 💻 This repo: [github.com/SAE-Geneve/CPlusPlus_Course_Ranges](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges)

---

# Questions?

<small>Code: [github.com/SAE-Geneve/CPlusPlus_Course_Ranges](https://github.com/SAE-Geneve/CPlusPlus_Course_Ranges)</small>
