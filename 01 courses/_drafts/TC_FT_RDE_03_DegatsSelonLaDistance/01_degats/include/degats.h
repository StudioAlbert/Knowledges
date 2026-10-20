#pragma once

namespace rde03 {

// Les trois regles du game designer. Elles sont imposees, elles ne bougent pas.
inline constexpr float kDegatsMax = 25.f;
inline constexpr float kDistanceMin = 0.25f;  // en deca : degats maximum
inline constexpr float kDistanceMax = 5.f;    // a partir de la : aucun degat

// Etape 1 : d'abord les bornes seules, puis la proportionnalite.
float DegatsProportionnels(float distance);

// Etape 2 : memes bornes, une autre forme entre les deux.
float DegatsAmortis(float distance);

}  // namespace rde03
