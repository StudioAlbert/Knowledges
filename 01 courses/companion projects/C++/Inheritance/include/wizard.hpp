//
// Created by sebas on 14.10.2026.
//

#ifndef INHERITANCE_WIZARD_HPP
#define INHERITANCE_WIZARD_HPP
#include "hero.hpp"


class Wizard : public Hero {

public:
    // Wizard(int pv_) : Hero(pv_) {}
    using Hero::Hero;
    void Spell();

    void TakeDamage(int damage) override;

};


#endif //INHERITANCE_WIZARD_HPP
