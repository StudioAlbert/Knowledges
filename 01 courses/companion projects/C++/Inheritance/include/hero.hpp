//
// Created by sebas on 14.10.2026.
//

#ifndef INHERITANCE_HERO_HPP
#define INHERITANCE_HERO_HPP
#include <print>


class Hero{

protected:
    int pv_;

public :
    Hero(int pv = 10) : pv_(pv) {
        std::println("Constructing Hero");
    };

    void Move();

    virtual void TakeDamage(int damage);
    // virtual void TakeDamage(int damage){
    //     pv_ -= damage;
    //     std::println("Remaining PV {}", pv_);
    // }

};




#endif //INHERITANCE_HERO_HPP
