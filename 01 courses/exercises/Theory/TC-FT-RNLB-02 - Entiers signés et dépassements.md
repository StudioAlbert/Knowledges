# Exercices — TC-FT-RNLB-02 — Entiers signés et dépassements

> Cours associé : [[01 courses/slides/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements]]

Les exercices 1 à 4 se font sur papier ; les exercices 5 et 6 sont des programmes C++.

## Exercice 1 — Plages

1. Combien de valeurs différentes peut-on écrire sur 12 bits ? Quelle est la plage d'un entier signé de 12 bits ?
2. Quel est le plus petit type de `<cstdint>` capable de stocker :
    - l'âge d'un joueur
    - un score qui peut atteindre 3 millions
    - une température relevée entre −40 °C et 50 °C
    - le nombre de millisecondes écoulées depuis le 1ᵉʳ janvier 1970

## Exercice 2 — Complément à deux sur 8 bits

1. Coder en complément à deux sur 8 bits : 100, −100, −1, −128.
2. Décoder : `1000 0001`, `1110 0000`, `0111 1111`, `1010 1010`.
3. Pourquoi −128 existe-t-il sur 8 bits, mais pas +128 ?

## Exercice 3 — Prévoir un dépassement

Pour chaque ligne, donner la valeur obtenue, ou écrire « comportement indéfini ».

```cpp
std::uint8_t a = 250;    a += 10;     // a = ?
std::uint8_t b = 10;     b -= 20;     // b = ?
std::int16_t c = 30000;  c += 10000;  // c = ? (attention au piège)
int d = 2'147'483'647;   d += 1;      // d = ?
unsigned int e = 0;      e -= 1;      // e = ?
std::uint8_t f = 200, g = 100;
auto h = f + g;                       // h = ? de quel type ?
```

## Exercice 4 — Trouver le bug

```cpp
#include <iostream>
#include <vector>

void afficher_a_l_envers(const std::vector<int>& v)
{
    for (unsigned int i = v.size() - 1; i >= 0; --i)
        std::cout << v[i] << '\n';
}
```

1. Que se passe-t-il avec un vecteur vide ? Et avec `{1, 2, 3}` ?
2. Corriger la fonction.

### Bonus

Même chose pour la multiplication.
