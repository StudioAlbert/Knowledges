#pragma once

// Companion du cours TC-FT-RNLB-02 — Entiers signés et dépassements
//
// Une fonction par slide, dans l'ordre du deck. Chaque fonction :
//   - porte en commentaire le nom de sa slide ;
//   - affiche ce nom en dur, en première ligne, avec titre().

#include <climits>
#include <cstddef>
#include <cstdint>
#include <iostream>
#include <limits>
#include <print>
#include <vector>

#include "Affichage.h"

// =================================================================
// Entiers non signés
// =================================================================

// Slide « Pac-Man, niveau 256 »
inline void pacMan()
{
    titre("Pac-Man, niveau 256");

    std::uint8_t niveau = 254;
    for (int i = 0; i < 3; i++)
    {
        std::println("niveau stocké = {:3}   bits = {}", niveau, bits8(niveau));
        ++niveau;
    }
    std::println("-> l'octet ne connaît pas 256 : le compteur est reparti de 0.");
}

// Slide « n bits, 2ⁿ valeurs »
inline void nBits()
{
    titre("n bits, 2^n valeurs");

    std::println("{:>6} | {:>22} | {}", "Bits", "Nombre de valeurs", "Plage non signée");
    std::println("{:>6} | {:>22} | 0 ... {}", 8, 1ull << 8, std::numeric_limits<std::uint8_t>::max());
    std::println("{:>6} | {:>22} | 0 ... {}", 16, 1ull << 16, std::numeric_limits<std::uint16_t>::max());
    std::println("{:>6} | {:>22} | 0 ... {}", 32, 1ull << 32, std::numeric_limits<std::uint32_t>::max());

    const std::uint8_t tousA1 = 0b1111'1111;
    std::println("\n{} = {} = 2^8 - 1", bits8(tousA1), tousA1);
}

// =================================================================
// Les nombres négatifs
// =================================================================

// Slide « Première idée : un bit de signe »
// Simulation : le signe dans le bit 7, la valeur absolue dans les 7 autres.
inline std::uint8_t signeEtValeur(int x)
{
    const int valeurAbsolue = x < 0 ? -x : x;
    const int bitDeSigne = x < 0 ? 0b1000'0000 : 0;
    return static_cast<std::uint8_t>(bitDeSigne | valeurAbsolue);
}

inline void bitDeSigne()
{
    titre("Première idée : un bit de signe");

    std::println("+5 = {}", bits8(signeEtValeur(5)));
    std::println("-5 = {}", bits8(signeEtValeur(-5)));
    std::println("deux zéros : {} et {}", bits8(0b0000'0000), bits8(0b1000'0000));

    // Le processeur additionne bit à bit, sans rien savoir du « signe »
    const std::uint8_t somme = signeEtValeur(5) + signeEtValeur(-5);
    std::println("{} + {} = {}  -> lu en signe + valeur : -{}",
                 bits8(signeEtValeur(5)), bits8(signeEtValeur(-5)), bits8(somme), somme & 0b0111'1111);
}

// Slide « Le complément à deux »
inline void complementADeux()
{
    titre("Le complément à deux");

    const std::int8_t valeurs[] = {127, -128, -5, -1};
    for (std::int8_t v : valeurs)
    {
        const auto octet = static_cast<std::uint8_t>(v);   // mêmes bits, lus sans signe
        std::println("{} = {:4}", bits8(octet), v);
    }
}

// Slide « Obtenir −x : inverser, puis ajouter 1 »
inline void inverserPuisAjouter1()
{
    titre("Obtenir -x : inverser, puis ajouter 1");

    const std::uint8_t cinq = 5;
    const std::uint8_t inverse = ~cinq;           // ~ inverse chaque bit
    const std::uint8_t moinsCinq = inverse + 1;

    std::println("  5        = {}", bits8(cinq));
    std::println("  inverser = {}", bits8(inverse));
    std::println("  + 1      = {}   = {}", bits8(moinsCinq), static_cast<std::int8_t>(moinsCinq));

    const std::uint8_t retour = static_cast<std::uint8_t>(~moinsCinq) + 1;
    std::println("et retour  : {}   = {}", bits8(retour), retour);

    // L'addition redevient juste : la retenue sort des 8 bits
    const int sommeComplete = cinq + moinsCinq;                    // calcul en int : 256
    const auto sommeSur8Bits = static_cast<std::uint8_t>(sommeComplete);
    std::println("5 + (-5) = {} (9 bits)  -> sur 8 bits : {} = {}",
                 sommeComplete, bits8(sommeSur8Bits), sommeSur8Bits);
}

// Slide « Plages représentables »
template <typename T>
inline void ligneDePlage(const char* nom)
{
    std::println("{:<9} | {:>21} | {:>21}", nom,
                 +std::numeric_limits<T>::min(), +std::numeric_limits<T>::max());
}

inline void plages()
{
    titre("Plages représentables");

    ligneDePlage<std::int8_t>("int8_t");
    ligneDePlage<std::uint8_t>("uint8_t");
    ligneDePlage<std::int16_t>("int16_t");
    ligneDePlage<std::uint16_t>("uint16_t");
    ligneDePlage<std::int32_t>("int32_t");
    ligneDePlage<std::uint32_t>("uint32_t");
    ligneDePlage<std::int64_t>("int64_t");
    ligneDePlage<std::uint64_t>("uint64_t");
}

// Slide « À vous » — pour VÉRIFIER vos réponses, pas pour les trouver
inline void aVous()
{
    titre("À vous — vérification");

    const std::int8_t aCoder[] = {42, -42};
    for (std::int8_t v : aCoder)
    {
        std::println("{:4} = {}", v, bits8(static_cast<std::uint8_t>(v)));
    }
    const std::uint8_t aDecoder[] = {0b1001'0110, 0b1100'1000};
    for (std::uint8_t b : aDecoder)
    {
        std::println("{} = {}", bits8(b), static_cast<std::int8_t>(b));
    }
}

// =================================================================
// Dépassements
// =================================================================

// Slide « Opérateurs arithmétiques »
inline void operateurs()
{
    titre("Opérateurs arithmétiques");

    const int x = 17, y = 5;
    std::println("x + y = {}", x + y);
    std::println("x - y = {}", x - y);
    std::println("x * y = {}", x * y);
    std::println("x / y = {}   (division entière)", x / y);
    std::println("x % y = {}   (reste)", x % y);
}

// Slide « Dépassement non signé : ça tourne »
inline void nonSigneTourne()
{
    titre("Dépassement non signé : ça tourne");

    std::uint8_t vie = 255;
    ++vie;
    std::println("uint8_t vie = 255; ++vie;        -> {}", vie);

    unsigned int stock = 0;
    --stock;
    std::println("unsigned int stock = 0; --stock; -> {}", stock);
}

// Slide « Le piège classique du non signé »
inline void piegeNonSigne()
{
    titre("Le piège classique du non signé");

    std::vector<int> scores;                                       // vide
    std::println("scores.size() - 1 = {}", scores.size() - 1);    // pas -1 !

    // i >= 0 est toujours vrai pour un non signé : on s'arrête nous-mêmes après 6 tours.
    int tours = 0;
    for (unsigned int i = 3; i >= 0 && tours < 6; --i, ++tours)   // avertissement attendu
    {
        std::println("i = {}", i);
    }
}

// Slide « Dépassement signé : comportement indéfini »
// Compilez avec -DSANITIZE=ON (GCC / Clang) : le programme signale l'erreur.
inline bool plusGrandQueLui(int x)
{
    return x + 1 > x;   // le compilateur a le droit de remplacer ça par « true »
}

inline void signeIndefini()
{
    titre("Dépassement signé : comportement indéfini");

    int score = 2'147'483'647;   // INT_MAX
    score = score + 1;           // comportement indéfini (UB)
    std::println("INT_MAX + 1 -> {}  (ici ; rien ne le garantit)", score);

    const bool reponse = plusGrandQueLui(INT_MAX);
    std::println("INT_MAX + 1 > INT_MAX ? {}", reponse);
    if (reponse)
    {
        std::println("-> le compilateur a supposé que le débordement n'arrive jamais : x + 1 > x devient true");
    }
    else
    {
        std::println("-> ici le calcul a fait le tour ; optimisé (-O2), le compilateur peut répondre true");
    }
}

// Slide « Mélanger signé et non signé »
inline void melange()
{
    titre("Mélanger signé et non signé");

    int a = -1;
    unsigned int b = 1;
    if (a < b)   // avertissement -Wsign-compare / C4018 attendu
    {
        std::println("-1 < 1 : vrai");
    }
    else
    {
        std::println("-1 < 1 : FAUX, car -1 est converti en {}", static_cast<unsigned int>(a));
    }
}

// Slide « Les petits types grandissent »
inline void promotion()
{
    titre("Les petits types grandissent");

    std::uint8_t a = 200, b = 100;
    auto c = a + b;                                        // int
    std::uint8_t d = a + b;                                // 300 rangé sur 8 bits
    std::println("auto c = a + b         -> {} (sizeof = {} : c'est un int)", c, sizeof(c));
    std::println("std::uint8_t d = a + b -> {} = 300 - 256", d);
}

// Slide « std::numeric_limits, en code »
inline void numericLimits()
{
    titre("std::numeric_limits, en code");

    std::println("int      : {} ... {}", std::numeric_limits<int>::min(), std::numeric_limits<int>::max());
    std::println("uint8_t  : max = {}", +std::numeric_limits<std::uint8_t>::max());
    std::println("long     : max = {}   (dépend de la plateforme)", std::numeric_limits<long>::max());
    std::println("int      : {} bits de valeur", std::numeric_limits<int>::digits);
    std::println("unsigned : signé ? {}", std::numeric_limits<unsigned int>::is_signed);
}

// Slide « Tester avant de déborder »
inline bool additionSure(int a, int b)
{
    if (b > 0 && a > std::numeric_limits<int>::max() - b) return false;   // dépasserait par le haut
    if (b < 0 && a < std::numeric_limits<int>::min() - b) return false;   // dépasserait par le bas
    return true;
}

inline void testerAvantDeDeborder()
{
    titre("Tester avant de déborder");

    std::println("additionSure(1, 2)             -> {}", additionSure(1, 2));
    std::println("additionSure(INT_MAX, 1)       -> {}", additionSure(INT_MAX, 1));
    std::println("additionSure(INT_MIN, -1)      -> {}", additionSure(INT_MIN, -1));
    std::println("additionSure(INT_MAX, INT_MIN) -> {}", additionSure(INT_MAX, INT_MIN));
}

// =================================================================
// Taille des types
// =================================================================

// Slide « À vous : mesurer sa plateforme »
inline void mesurerSaPlateforme()
{
    titre("À vous : mesurer sa plateforme");

    std::println("char {}  short {}  int {}  long {}  long long {}",
                 sizeof(char), sizeof(short), sizeof(int), sizeof(long), sizeof(long long));
    std::println("wchar_t {}  size_t {}  pointeur {}",
                 sizeof(wchar_t), sizeof(std::size_t), sizeof(void*));
    std::println("char signé ? {}", CHAR_MIN < 0);
}

// Slide « Les types de taille fixe »
inline void typesDeTailleFixe()
{
    titre("Les types de taille fixe");

    static_assert(sizeof(std::int32_t) == 4, "int32_t fait toujours 4 octets");
    std::println("int8_t {} · int16_t {} · int32_t {} · int64_t {}",
                 sizeof(std::int8_t), sizeof(std::int16_t), sizeof(std::int32_t), sizeof(std::int64_t));

    // Piège d'affichage : int8_t est un signed char
    std::int8_t x = 65;
    std::cout << "std::cout << x  -> " << x << "   (un caractère !)\n";
    std::cout << "std::cout << +x -> " << +x << '\n';
}
