#include <iostream>

#include "vector_2.hpp"

int main() {

    Vector2 poussee{1,2};
    Vector2 gravite{3,3};

    Vector2 resultante;
    resultante.x = poussee.x + gravite.x;
    resultante.y = poussee.y + gravite.y;

    resultante = poussee + gravite;
    Vector2 res = Vector2::multiply(poussee, 3);
    resultante = gravite * 2;
    resultante = 2 * gravite;

    return 0;
}
