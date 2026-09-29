#include <iostream>
#include <print>

int main() {
    double my_float = 14.0;
    double my_float_10 = 140.0;
    my_float += 1;
    my_float *= -1;
    std::println("Hello, Float {} !", my_float);

    auto bits = std::bit_cast<std::uint32_t>(12.5f);
    std::cout << std::format("{:0b}\n", bits);                            // 41480000
    std::cout << std::bit_cast<float>(std::uint32_t{0xC0D00000}) << '\n';


    return 0;
}
