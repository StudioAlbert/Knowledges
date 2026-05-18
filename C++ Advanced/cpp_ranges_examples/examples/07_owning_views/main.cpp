// 07 — Owning Views
// Piping an rvalue moves the container into a std::ranges::owning_view,
// which keeps it alive as long as the pipeline — safe to return.
#include <iostream>
#include <ranges>
#include <vector>

std::vector<int> make_data() { return {1, 2, 3, 4, 5}; }

// Returns a view over the moved-in temporary; no dangling.
auto good() {
    return make_data()
         | std::views::transform([](int x) { return x * 2; });
}

int main() {
    std::cout << "good():";
    for (int x : good()) std::cout << ' ' << x;   // 2 4 6 8 10
    std::cout << '\n';
}
