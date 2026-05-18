// 03 — Range Algorithms Basics
// Every classic <algorithm> has a std::ranges:: cousin taking a range.
#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>

int main() {
    std::vector<int> v{5, 2, 8, 1, 9, 3};

    std::ranges::sort(v);
    auto it       = std::ranges::find(v, 8);
    auto [lo, hi] = std::ranges::minmax_element(v);
    auto n        = std::ranges::count_if(v, [](int x) { return x > 5; });

    std::cout << "sorted:";
    for (int x : v) std::cout << ' ' << x;
    std::cout << "\nfound 8: " << (it != v.end())
              << "\nmin=" << *lo << " max=" << *hi
              << "\ncount(>5)=" << n << '\n';
}
