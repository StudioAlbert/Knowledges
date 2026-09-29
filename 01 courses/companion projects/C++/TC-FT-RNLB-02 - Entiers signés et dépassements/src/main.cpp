// Companion du cours TC-FT-RNLB-02 — Entiers signés et dépassements
//
// Les démos s'enchaînent dans l'ordre du deck. Gardez EntiersSignes.h ouvert à côté :
// chaque fonction porte le nom de sa slide.

#include "Affichage.h"
#include "EntiersSignes.h"

int main()
{
    // Entiers non signés
    pacMan();
    nBits();
    pause();

    // Les nombres négatifs
    bitDeSigne();
    complementADeux();
    inverserPuisAjouter1();
    plages();
    aVous();
    pause();

    // Dépassements
    operateurs();
    nonSigneTourne();
    piegeNonSigne();
    signeIndefini();
    melange();
    promotion();
    numericLimits();
    testerAvantDeDeborder();
    pause();

    // Taille des types
    mesurerSaPlateforme();
    typesDeTailleFixe();
    return 0;
}
