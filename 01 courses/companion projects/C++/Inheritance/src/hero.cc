//
// Created by sebas on 14.10.2026.
//

#include "../include/hero.hpp"

#include <print>

void Hero::Move() {
    std::println("moving hero");
}

void Hero::TakeDamage(int damage) {
    pv_ -= damage;
    std::println("Remaining PV {}", pv_);
}
