# Exercices — TC-FT-RNLB-01 — Bases et changements de base

Sans calculatrice. Écrivez la méthode, pas seulement le résultat.

## Changements de base

17 en base 5
23 en base 8
31 en base 7
20 en base 16
35 en base 16

13(4) en base 10
21(3) en base 10
14(5) en base 10
## Exercice 1 — Vers le décimal

1. Quel nombre est `10011011` ?
2. Quel nombre est `0xFA` ?
3. Quel nombre est `755` en octal ?
4. Quel nombre est `345` en base 9 ?

## Exercice 2 — Depuis le décimal

1. Quelles sont les représentations binaire et hexadécimale du nombre 201 ?
2. Convertir 2026 en binaire par divisions successives, puis en hexadécimal par paquets de 4 bits.
3. Convertir 493 en octal. Retrouver le résultat depuis son écriture binaire, par paquets de 3 bits.

## Exercice 3 — Formative : le tableau des conversions

Compléter le tableau :

| Valeur décimale | Valeur hexadécimale | Valeur binaire |
|:-:|:-:|:-:|
|  | AF = 10 × 16 + 15 = 175 |  |
|  | ACD |  |
|  | AB2 |  |
|  | FF |  |
| 25 | 19 | 11001 |
| 147 |  |  |
| 39554 |  | 1001 1010 1000 0010 |
| 15637 |  |  |
| 2856 |  |  |

Décomposition de 39554, à titre d'exemple de méthode :

```
39554 = 32768 + 6786
39554 = 32768 + 4096 + 2690
39554 = 32768 + 4096 + 2048 + 642
39554 = 32768 + 4096 + 2048 + 512 + 130
39554 = 32768 + 4096 + 2048 + 512 + 128 + 2
39554 = 2^15 + 2^12 + 2^11 + 2^9 + 2^7 + 2^1
```

## Exercice 4 — Littéraux C++

1. Sans exécuter le programme, prévoir ce qu'il affiche. Vérifier ensuite.

```cpp
#include <bitset>
#include <format>
#include <iostream>

int main()
{
    int a = 0x1F;
    int b = 0b1'0000;
    int c = 017;
    int d = 1'024;
    std::cout << a << ' ' << b << ' ' << c << ' ' << d << '\n';
    std::cout << std::hex << a + b << ' ' << std::oct << c << '\n';
    std::cout << std::bitset<8>(c) << ' ' << std::format("{:#x}", d) << '\n';
}
```

2. Pourquoi `int mois = 09;` ne compile-t-il pas, alors que `int mois = 07;` compile ?

## Exercice 5 — Afficher dans toutes les bases

Écrire une fonction `void afficher_bases(int n)` qui affiche `n` en décimal, en hexadécimal, en octal et en binaire sur 16 bits. Pour 2026 :

```
2026 = 0x7ea = 03752 = 0b0000011111101010
```

### Bonus

Réécrire la conversion en binaire sans `std::format` ni `std::bitset`, par divisions successives.
