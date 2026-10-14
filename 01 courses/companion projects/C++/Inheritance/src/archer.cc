//
// Created by sebas on 14.10.2026.
//

#include "../include/archer.hpp"

#include <print>

void Archer::Shoot() {
    if (nb_arrows_ > 0) {
        std::print("Pffffifiifififiioooooouuu");
    }
    nb_arrows_--;
}
