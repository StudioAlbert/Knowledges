#include <iostream>

#include "degats.h"

// On entre une distance par ligne, le programme affiche les degats.
// Pour passer d'un mode a l'autre : commenter une ligne, decommenter l'autre.
int main() {
  std::cout << "Distance en metres, une par ligne.\n"
            << "Ctrl+Z puis Entree pour terminer.\n\n";

  float distance = 0.f;
  while (std::cin >> distance) {
    const float degats = rde03::DegatsProportionnels(distance);
    // const float degats = rde03::DegatsAmortis(distance);

    std::cout << distance << " m  ->  " << degats << " degats\n";
  }
}
