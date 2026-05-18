// 05 — Projections & Constraints
// A projection adapts each element before the algorithm compares/tests it.
#include <algorithm>
#include <cmath>
#include <iostream>
#include <memory>
#include <ranges>
#include <string>
#include <vector>

struct Person { int id; std::string name; };

int main() {
    // 1 - by a field
    std::vector<Person> people{{3, "Cara"}, {1, "Ada"}, {2, "Bob"}};
    std::ranges::sort(people, {}, &Person::name);
    auto p = std::ranges::find(people, 2, &Person::id);
    std::cout << "first by name: " << people.front().name
              << " | id 2 = " << (p != people.end() ? p->name : "?") << '\n';

    // 2 - by a derived key
    std::vector<int> xs{4, -2, 7, -1, 3};
    auto z = std::ranges::min(xs, {}, [](int x) { return std::abs(x); });
    std::cout << "nearest to zero: " << z << '\n';

    // 3 - through indirection
    std::vector<std::unique_ptr<Person>> ptrs;
    ptrs.push_back(std::make_unique<Person>(9, "Zoe"));
    ptrs.push_back(std::make_unique<Person>(4, "Max"));
    std::ranges::sort(ptrs, {}, [](const auto& up) { return up->id; });
    std::cout << "smallest pointee id: " << ptrs.front()->name << '\n';
}
