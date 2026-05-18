// Exercise 2 — Top-3 Followers Leaderboard (solution)
// filter (lazy) + materialise + sort (algorithm) + take + enumerate.
#include <algorithm>
#include <functional>
#include <iostream>
#include <ranges>
#include <string>
#include <vector>

struct Player { int id; std::string name; int score; bool is_follower; };

void leaderboard(const std::vector<Player>& players) {
    auto top = players | std::views::filter(&Player::is_follower)
                       | std::ranges::to<std::vector>();      // sortable

    std::ranges::sort(top, std::ranges::greater{}, &Player::score);

    for (auto [i, p] : top | std::views::take(3) | std::views::enumerate)
        std::cout << (i + 1) << ". " << p.name
                  << " - " << p.score << '\n';
}

int main() {
    std::vector<Player> players{
        {1, "Ada", 980, true},  {2, "Bob", 1200, false},
        {3, "Cara", 1500, true}, {4, "Dee", 1100, true},
        {5, "Eve", 1750, true},  {6, "Fox", 300, true}};

    leaderboard(players); // Eve 1750, Cara 1500, Dee 1100
}
