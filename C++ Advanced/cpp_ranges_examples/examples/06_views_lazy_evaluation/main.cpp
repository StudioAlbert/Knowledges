// 06 — Views & Lazy Evaluation
// Work happens only for the elements you actually consume.
#include <iostream>
#include <ranges>
#include <vector>

int main() {
    std::vector<int> big(1'000'000);
    for (int i = 0; auto& x : big) x = i++;

    long calls = 0;
    auto v = big
        | std::views::transform([&](int x) { ++calls; return x * x; })
        | std::views::take(3);

    std::cout << "first 3 squares:";
    for (int x : v) std::cout << ' ' << x;
    std::cout << "\nmultiplications performed: " << calls << " (not 1e6)\n";

    std::cout << "first 5 of an infinite range:";
    for (int x : std::views::iota(0) | std::views::take(5))
        std::cout << ' ' << x;
    std::cout << '\n';
}
