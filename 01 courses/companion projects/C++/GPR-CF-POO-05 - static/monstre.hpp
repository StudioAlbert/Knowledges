//
// Created by sebas on 15.10.2026.
//

#ifndef GPR_CF_POO_05___STATIC_MONSTRE_HPP
#define GPR_CF_POO_05___STATIC_MONSTRE_HPP
#include <print>

class Monstre {
   //int lifePoints = 100;


public:
    Monstre() { ++count_; }
    ~Monstre() { --count_; }
    
    static int count() { return count_; }

    static void HowMany() {
        std::println("How many monsters ? {}", count_);
    }

private:
    static int count_; // une seule case, pour toute la classe
};


#endif //GPR_CF_POO_05___STATIC_MONSTRE_HPP
