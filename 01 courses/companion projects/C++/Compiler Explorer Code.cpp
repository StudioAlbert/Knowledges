// TC-FT-RNLB-02 — Selon la plateforme
// Chaque fonction renvoie une taille en octets : lisez la valeur dans l'assembleur
// (« mov eax, 8 » veut dire 8), puis ajoutez d'autres compilateurs :
// « + Add new… → Compiler » : x64 msvc, ARM64 gcc, AVR gcc (Arduino)…
#include <cstddef>
#include <iostream>

void taille_char()      { std::cout << sizeof(char) << '\n'; }
void taille_short()     { std::cout << sizeof(short) << '\n'; }
void taille_int()       { std::cout << sizeof(int) << '\n'; }
void taille_long()      { std::cout << sizeof(long) << '\n'; }
void taille_long_long() { std::cout << sizeof(long long) << '\n'; }
void taille_wchar_t()   { std::cout << sizeof(wchar_t) << '\n'; }
void taille_size_t()    { std::cout << sizeof(std::size_t) << '\n'; }
void taille_pointeur()  { std::cout << sizeof(void*) << '\n'; }
void char_est_signe()   { std::cout << (char(-1) < 0) << '\n'; }   // 1 : signé, 0 : non signé

int main(){
    taille_char();
    taille_short();
    taille_int();
    taille_long();
    taille_long_long();
    taille_wchar_t();
    taille_size_t();
    taille_pointeur();
    char_est_signe(); 
    return 0;
}