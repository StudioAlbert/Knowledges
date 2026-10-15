//
// Created by sebas on 14.10.2026.
//

#ifndef INHERITANCE_RANGER_HPP
#define INHERITANCE_RANGER_HPP
#include "archer.hpp"
#include "wizard.hpp"

class Ranger : public Archer, public Wizard {

public:
    void TalkToAnimals();

    Ranger(int pv, int arrow) : Archer(pv, arrow) {}

};


#endif //INHERITANCE_RANGER_HPP
