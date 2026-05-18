// 09 — std::ranges::to  (C++23)
// Materialise a lazy view back into a real container.
#include <iostream>
#include <ranges>
#include <set>
#include <vector>

int main() {
    auto squares = std::views::iota(1, 11)
        | std::views::filter([](int x) { return x % 2 == 0; })
        | std::views::transform([](int x) { return x * x; })
        | std::ranges::to<std::vector<int>>();

    std::cout << "vector:";
    for (int x : squares) std::cout << ' ' << x;   // 4 16 36 64 100
    std::cout << '\n';

    // Works with any container.
    auto s = squares | std::ranges::to<std::set<int>>();
    std::cout << "set size: " << s.size() << '\n';
}
