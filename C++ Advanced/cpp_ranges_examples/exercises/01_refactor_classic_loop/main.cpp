// Exercise 1 — Refactor a Classic Loop (solution)
// Average grade of the students who passed, as a ranges pipeline.
//
// The deck's one-liner is `std::ranges::fold_left` (C++23). It needs a
// very recent stdlib (libstdc++ 13+/libc++ 17+); this runnable version
// uses the portable fallback: materialise the view, then accumulate.
#include <iostream>
#include <numeric>
#include <ranges>
#include <string>
#include <vector>

struct Student { std::string name; int grade; bool passed; };

double avg(const std::vector<Student>& s) {
    auto passing = s | std::views::filter(&Student::passed)
                     | std::views::transform(&Student::grade)
                     | std::ranges::to<std::vector<int>>();

    if (passing.empty()) return 0;
    return double(std::accumulate(passing.begin(), passing.end(), 0))
           / passing.size();
}

int main() {
    std::vector<Student> s{
        {"Ada", 90, true}, {"Bob", 40, false},
        {"Cara", 80, true}, {"Dee", 70, true}};

    std::cout << "average passing grade: " << avg(s) << '\n'; // 80
    std::cout << "empty input: " << avg({}) << '\n';          // 0
}
