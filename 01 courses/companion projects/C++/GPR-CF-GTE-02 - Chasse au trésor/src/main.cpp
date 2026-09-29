#include <cstdlib>
#include <ctime>

#include "Game.hpp"

int main()
{
    // Nouveau tirage à chaque lancement
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    playGame();

    return 0;
}
