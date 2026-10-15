#include <iostream>

#include "include/archer.hpp"
#include "include/hero.hpp"
#include "include/ranger.hpp"

int main() {
    //
    // Hero hero(100);
    // hero.Move();
    // hero.TakeDamage(5);

    Archer archer(50, 2);
    archer.Move();
    //archer.TakeDamage(6);
    archer.Shoot();

    Wizard merlin(100);
    //merlin.TakeDamage(6);

    // Menu ---------------------------
    Hero player;
    player = archer;
    // player = merlin;
    player.TakeDamage(6);

    for (int i = 0; i < 3; i++) {

    }

    return 0;
}
