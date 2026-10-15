//
// Created by sebas on 14.10.2026.
//

#include "../include/wizard.hpp"

#include <print>

void Wizard::Spell() {
    std::print("Shazam");
}

void Wizard::TakeDamage(int damage) {
    Hero::TakeDamage(damage + 2);
}
