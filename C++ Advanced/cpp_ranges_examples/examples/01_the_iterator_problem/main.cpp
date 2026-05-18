// 01 — The Iterator Problem
// Ranges collapse begin()/end() ceremony and make the cross-container
// iterator bug impossible.
#include <algorithm>
#include <iostream>
#include <ranges>
#include <string>
#include <vector>

struct Person { std::string name; int age; };

int main() {
    std::vector<Person> people{
        {"Ada", 36}, {"Linus", 54}, {"Grace", 25}, {"Bjarne", 73}};

    std::ranges::sort(people, {}, &Person::age);

    auto names = people | std::views::transform(&Person::name)
                        | std::ranges::to<std::vector>();

    auto it = std::ranges::find(people, 25, &Person::age);

    std::cout << "by age:";
    for (const auto& n : names) std::cout << ' ' << n;
    std::cout << "\nage 25 -> "
              << (it != people.end() ? it->name : "none") << '\n';
}
