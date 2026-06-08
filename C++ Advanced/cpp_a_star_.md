
Same two terms — here's the short version:
---
**`std::expected<Value, Error>`** (C++23): a return type that holds *either* a success value *or* an error — no exceptions needed.
```cpp
std::expected<Path, PathError> r = FindPath(...);
if (r)  use(*r);            // success → the Path
else    handle(r.error());  // failure → why it failed (enum)
```
The good A* uses it to report *why* a path failed (`kStartOutOfBounds`, `kNoPathFound`…). The leaky version just returns an empty path, so you can't tell why. Think Rust's `Result`, or an `optional` that also carries a reason.

---

**`pq`** = `std::priority_queue` — the A* **open set** (frontier). It always pops the node with the smallest `f = g + h` next, which is exactly what A* needs. It's a binary heap → push/pop are **O(log n)**. The good core puts tiny `{f, pos}` items in it; the leaky version copies whole node structs in *and* does an O(n) linear search to check membership — that's the slow part.

---

I'll include both as short "vocab boxes" in the lecture since `std::expected` is new (C++23). Ready to re-present the plan and proceed whenever you are.