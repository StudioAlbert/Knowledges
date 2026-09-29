#include "Messages.hpp"

#include <iostream>
#include <limits>
#include <print>

#include "GameConfig.hpp"

// Lit un nombre entier ; redemande tant que la saisie n'en est pas un.
static int readNumber()
{
    int value = 0;
    while (!(std::cin >> value))
    {
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::print("Un nombre, s'il vous plait : ");
    }
    return value;
}

void printWelcome()
{
    std::println("=====================================");
    std::println("        CHASSE AU TRESOR");
    std::println("=====================================");
    std::println("Un tresor est enterre sous la plage.");
    std::println("Creusez une case : le detecteur dira si vous chauffez.");
    std::println("");

    // Dessin de la plage : une ligne d'en-tete, puis GRID_SIZE lignes de sable.
    std::print("    ");
    for (int column = 1; column <= GRID_SIZE; column++)
    {
        std::print("{} ", column);
    }
    std::println("");
    for (int row = 1; row <= GRID_SIZE; row++)
    {
        std::print("{}   ", row);
        for (int column = 1; column <= GRID_SIZE; column++)
        {
            std::print(". ");
        }
        std::println("");
    }
    std::println("");
}

int askColumn()
{
    std::print("Colonne (1-{}, 0 pour abandonner) : ", GRID_SIZE);
    return readNumber();
}

int askRow()
{
    std::print("Ligne   (1-{}) : ", GRID_SIZE);
    return readNumber();
}

void printHint(int distance)
{
    if (distance == 1)
    {
        std::println("  >> BRULANT !");
    }
    else if (distance == 2)
    {
        std::println("  >> Chaud");
    }
    else if (distance <= 4)
    {
        std::println("  >> Tiede");
    }
    else
    {
        std::println("  >> Froid");
    }
}

void printVictory(int attempts)
{
    std::println("");
    std::println("*** TRESOR TROUVE en {} essai(s) ! ***", attempts);
}

void printGiveUp(int treasureColumn, int treasureRow)
{
    std::println("");
    std::println("Abandon. Le tresor etait en colonne {}, ligne {}.", treasureColumn, treasureRow);
}

void printDefeat(int treasureColumn, int treasureRow)
{
    std::println("");
    std::println("La maree monte : plus d'essais !");
    std::println("Le tresor etait en colonne {}, ligne {}.", treasureColumn, treasureRow);
}
