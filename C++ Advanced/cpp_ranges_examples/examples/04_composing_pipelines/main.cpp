// 04 — Composing Pipelines with |
// Pipe stages together; the whole pipeline is a single fused pass.
#include <iostream>
#include <ranges>
#include <vector>

struct Order { int quantity; double unit_price; bool cancelled; };

int main() {
    std::vector<Order> orders{
        {2, 10.0, false}, {1, 5.0, true}, {3, 7.5, false}, {4, 2.0, false}};

    auto revenue = [](const Order& o) { return o.quantity * o.unit_price; };

    auto top = orders
        | std::views::filter([](const Order& o) { return !o.cancelled; })
        | std::views::transform(revenue);

    double total = 0;
    for (double r : top) {
        std::cout << "revenue: " << r << '\n';
        total += r;
    }
    std::cout << "total (non-cancelled): " << total << '\n';
}
