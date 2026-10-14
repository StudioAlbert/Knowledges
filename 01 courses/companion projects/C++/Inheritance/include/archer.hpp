//
// Created by sebas on 14.10.2026.
//

#ifndef INHERITANCE_ARCHER_HPP
#define INHERITANCE_ARCHER_HPP
#include "../hero.hpp"


class Archer : public Hero {

    int nb_arrows_;

public:
    Archer(int pv_, int n) : nb_arrows_(n) , Hero(pv_) {
        std::println("Constructing Archer");
    };
    void Shoot();
};


#endif //INHERITANCE_ARCHER_HPP
