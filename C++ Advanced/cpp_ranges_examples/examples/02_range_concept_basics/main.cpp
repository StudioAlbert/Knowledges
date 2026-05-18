// 02 — Range Concept Basics
// A range is anything with begin()/end(). Containers and C arrays qualify;
// std::stack does not (a container adaptor — no iterators).
#include <array>
#include <iostream>
#include <map>
#include <ranges>
#include <stack>
#include <string>
#include <type_traits>
#include <vector>

template <std::ranges::range R>
void show(const R& r) {
    std::size_t n = 0;
    for (auto&& e : r) { (void)e; ++n; }
    std::cout << "  range ok, elements=" << n << '\n';
}

int main() {
    std::vector<int>   v{1, 2, 3};
    std::array<int, 3> a{1, 2, 3};
    std::string        s{"hi"};
    int                c[]{1, 2, 3};
    std::map<int, int> m{{1, 1}, {2, 2}};

    show(v); show(a); show(s); show(c); show(m);

    static_assert(std::ranges::contiguous_range<std::vector<int>>);
    static_assert(std::ranges::range<int[3]>);
    static_assert(!std::ranges::range<std::stack<int>>); // adaptor, not a range

    std::cout << "stack is NOT a range (no begin/end).\n";
}
