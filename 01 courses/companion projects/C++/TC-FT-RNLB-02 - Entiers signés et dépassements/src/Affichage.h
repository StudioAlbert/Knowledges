#ifndef AFFICHAGE_H
#define AFFICHAGE_H

#include <bitset>
#include <iostream>
#include <print>
#include <string>

inline void titre(const std::string& slide)
{
    std::println("");
    std::println("==================================================");
    std::println(" {}", slide);
    std::println("==================================================");
}

inline std::string bits8(std::uint8_t octet)
{
    const std::string b = std::bitset<8>(octet).to_string();
    return b.substr(0, 4) + " " + b.substr(4, 4);
}

inline void pause()
{
    std::print("\n[Entrée pour continuer] ");
    std::string ligne;
    std::getline(std::cin, ligne);
}
#endif // AFFICHAGE_H
