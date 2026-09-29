# Exercices — TC-FT-RNLB-03 — Flottants IEEE 754

> Cours associé : [[01 courses/slides/Theory/TC-FT-RNLB-03 - Flottants IEEE 754]]

Les exercices 1 à 3 se font sur papier. Pour vérifier : `std::bit_cast`, ou le [Float Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html).

## Exercice 1 — Fractions binaires

1. Écrire en binaire : 0,5 ; 0,25 ; 0,625 ; 5,75.
2. Écrire 0,2 en binaire, avec 8 chiffres après la virgule. Que remarque-t-on ?

## Exercice 2 — Lire un `float` donné en hexadécimal

Pour chaque motif : donner le signe, l'exposant stocké, l'exposant réel et la mantisse, puis la valeur.

1. `0x40000000`
2. `0xBF000000`
3. `0x42C80000`
4. `0x41A40000`
5. `0x80000000`
6. `0x7F800000`

## Exercice 3 — Coder un `float`

Donner le motif hexadécimal de : 3,0 ; −2,5 ; 0,15625 ; 1000,0.

## Exercice 4 — Prévoir le résultat

Sans exécuter le programme, prévoir chaque ligne affichée. Vérifier ensuite.

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::boolalpha;
    float grand = 16777216.0f;
    std::cout << (grand + 1.0f == grand) << '\n';
    std::cout << (0.1 + 0.2 == 0.3) << '\n';
    float z = 0.0f;
    float inf = 1.0f / z;
    std::cout << inf << ' ' << std::isnan(inf - inf) << '\n';
    float nan = std::sqrt(-1.0f);
    std::cout << (nan == nan) << ' ' << std::isnan(nan) << '\n';
    std::cout << static_cast<int>(-7.9f) << ' ' << std::lround(-7.5f) << '\n';
    std::cout << (0.0f == -0.0f) << '\n';
}
```

## Exercice 5 — La boucle qui ne finit pas

```cpp
for (float x = 0.0f; x != 2.0f; x += 0.2f)
    std::cout << x << '\n';
```

1. Ce programme s'arrête-t-il ? Pourquoi ?
2. Le réécrire avec un compteur entier, pour afficher les mêmes valeurs de 0 à 2.

## Exercice 6 — `presque_egaux`

Écrire `bool presque_egaux(float a, float b)`, qui combine une tolérance absolue de `1e-6f` et une tolérance relative de `1e-5f`.

> [!info] Deux façons de dire « assez proche »
> - **Tolérance absolue** : un écart **fixe**. `a` et `b` sont égaux si `|a − b| ≤ 1e-6`, quelle que soit leur taille.
> - **Tolérance relative** : un écart **proportionnel**. `a` et `b` sont égaux si `|a − b| ≤ 1e-5 × max(|a|, |b|)`, soit 0,001 % du plus grand des deux.
>
> | Ordre de grandeur de `a` et `b` | Écart accepté — absolu | Écart accepté — relatif |
> |--:|--:|--:|
> | 0 | 0,000 001 | 0 |
> | 1 | 0,000 001 | 0,000 01 |
> | 1 000 | 0,000 001 | 0,01 |
> | 100 000 | 0,000 001 | 1 |
>
> - L'absolue seule est **trop sévère pour les grands nombres** : à 100 000, deux `float` voisins sont déjà séparés de 0,0078.
> - La relative seule est **trop sévère près de zéro** : 1e-5 × 0 = 0, il faudrait l'égalité exacte.
> - D'où la combinaison : égaux si **l'une ou l'autre** est satisfaite.

Étapes : calculer l'écart `|a − b|` avec `std::abs` ; s'il passe la tolérance absolue, renvoyer `true` ; sinon, renvoyer le résultat du test relatif (`std::max` dans `<algorithm>`).

Tester avec : `(0.1f + 0.2f, 0.3f)`, `(1e-8f, 0.0f)`, `(100000.0f, 100000.01f)`, `(1.0f, 1.1f)`, puis avec deux NaN. Pour chaque paire, dire **quelle tolérance** l'accepte, ou pourquoi aucune ne l'accepte.

## Exercice 7 — Loin de l'origine

Un jeu range la position du joueur dans un `float`, en mètres.

1. À partir de quelle distance de l'origine l'écart entre deux positions voisines est-il d'au moins 1 cm ?
2. Et d'au moins 1 m ?
3. Proposer deux solutions pour un monde ouvert de 200 km de côté.
