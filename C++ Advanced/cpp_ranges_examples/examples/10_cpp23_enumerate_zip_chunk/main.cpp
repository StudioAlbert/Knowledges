// 10 — enumerate / zip / slide / cartesian_product  (C++23)
#include <iostream>
#include <ranges>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> names{"Ada", "Bob", "Cara"};
    std::vector<int> ages{36, 41, 29};

    for (auto [i, name] : std::views::enumerate(names))
        std::cout << i << ": " << name << '\n';

    for (auto [name, age] : std::views::zip(names, ages))
        std::cout << name << " is " << age << '\n';

    std::cout << "sliding windows of 3: ";
    for (auto w : std::views::iota(1, 7) | std::views::slide(3)) {
        std::cout << '[';
        for (int x : w) std::cout << x;
        std::cout << "] ";
    }
    std::cout << '\n';

    std::cout << "cartesian product: ";
    std::vector<int> xs{1, 2};
    std::vector<char> ys{'a', 'b'};
    for (auto [x, y] : std::views::cartesian_product(xs, ys))
        std::cout << x << y << ' ';
    std::cout << '\n';
}
