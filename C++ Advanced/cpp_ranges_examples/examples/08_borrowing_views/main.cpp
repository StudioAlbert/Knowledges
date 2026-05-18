// 08 — Borrowing Views
// A borrowed range's iterators stay valid even after the range
// expression is gone. find() on a temporary returns std::ranges::dangling.
#include <iostream>
#include <ranges>
#include <span>
#include <string>
#include <string_view>
#include <type_traits>
#include <vector>

int main() {
    static_assert( std::ranges::borrowed_range<std::string_view>);
    static_assert( std::ranges::borrowed_range<std::span<int>>);
    static_assert(!std::ranges::borrowed_range<std::string>);

    // Temporary (rvalue) vector -> result is std::ranges::dangling.
    auto bad = std::ranges::find(std::vector{1, 2, 3}, 2);
    static_assert(std::is_same_v<decltype(bad), std::ranges::dangling>);

    // lvalue container outlives the call -> a real iterator.
    std::vector<int> v{1, 2, 3};
    auto ok = std::ranges::find(v, 2);
    std::cout << "found in lvalue: " << *ok << '\n';
    std::cout << "find() on a temporary yielded std::ranges::dangling "
                 "(checked at compile time).\n";
}
