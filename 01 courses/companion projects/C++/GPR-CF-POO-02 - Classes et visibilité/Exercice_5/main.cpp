// =============================================================================
//  GPR-CF-POO-02 — Exercice 5 — La classe Joueur
//
//  CE FICHIER EST FOURNI. NE LE MODIFIEZ PAS.
//
//  Il ne fait que lire une commande et appeler une methode de Joueur. Il ne
//  connait aucun compteur, aucune borne, aucune regle : tout cela vit dans
//  joueur.h. C'est exactement ce que veut dire « encapsuler ».
// =============================================================================
#include <iostream>
#include <print>
#include <string>

#include "joueur.h"

namespace
{
    void afficherMenu()
    {
        std::println("");
        std::println("  c  courir        (10 d'endurance)");
        std::println("  r  se reposer");
        std::println("  o  ouvrir une porte  (1 cle)");
        std::println("  a  acheter une potion (25 d'or)");
        std::println("  p  tomber dans un piege (30 degats)");
        std::println("  f  fiche");
        std::println("  x  quitter");
        std::print("> ");
    }
}

int main()
{
    Joueur joueur;

    std::println("=== GPR-CF-POO-02 — Exercice 5 ===");
    joueur.afficherFiche();

    std::string commande;
    while (joueur.estVivant())
    {
        afficherMenu();
        if (!(std::cin >> commande)) { break; }
        if (commande.empty()) { continue; }

        switch (commande[0])
        {
        case 'c':
            if (joueur.courir()) { std::println("Vous courez."); }
            else                 { std::println("Trop fatigue pour courir."); }
            break;

        case 'r':
            joueur.seReposer();
            std::println("Vous reprenez votre souffle.");
            break;

        case 'o':
            if (joueur.ouvrirPorte()) { std::println("La porte s'ouvre."); }
            else                      { std::println("Pas de cle."); }
            break;

        case 'a':
            if (joueur.acheter(25)) { std::println("Potion achetee."); }
            else                    { std::println("Pas assez d'or."); }
            break;

        case 'p':
            joueur.subirDegats(30);
            std::println("Aie !");
            break;

        case 'f':
            break;

        case 'x':
            std::println("A bientot.");
            return 0;

        default:
            std::println("Commande inconnue.");
            break;
        }

        joueur.afficherFiche();
    }

    std::println("Vous etes mort.");
    return 0;
}
