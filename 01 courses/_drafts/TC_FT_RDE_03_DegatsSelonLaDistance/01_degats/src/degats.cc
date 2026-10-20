#include "degats.h"

namespace rde03 {

// Etape 1 — a ecrire.
//
// 1.1  Les bornes seules : kDegatsMax sous kDistanceMin, 0 a partir de
//      kDistanceMax, et la moitie entre les deux. C'est faux au milieu, et
//      c'est normal a ce stade.
// 1.2  La proportionnalite : normaliser, borner entre 0 et 1, descendre.
//      Les deux if de 1.1 disparaissent alors d'eux-memes.
float DegatsProportionnels(float distance) {
  return 0.f;
}

// Etape 2 — a ecrire.
//
// Memes bornes exactes, mais la courbe tient plus longtemps avant de
// s'effondrer. La moitie des degats tombe a 3,8 m, pas au milieu.
// Une seule operation de plus qu'en 1.2, et elle porte sur (1 - t).
float DegatsAmortis(float distance) {
  return 0.f;
}

}  // namespace rde03
