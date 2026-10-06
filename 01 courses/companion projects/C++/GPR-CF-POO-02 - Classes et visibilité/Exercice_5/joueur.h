// =============================================================================
//  GPR-CF-POO-02 — Exercice 5 — La classe Joueur
//
//  LE SEUL FICHIER QUE VOUS AVEZ A MODIFIER.
//
//  Le menu de main.cpp est deja ecrit et fonctionne : il appelle les methodes
//  ci-dessous. Votre travail est de faire tenir les cinq regles du jeu par la
//  classe elle-meme — pas par le menu.
//
//  Regle d'or : aucun attribut public. Si le menu avait besoin d'ecrire
//  directement dans un compteur, c'est que la methode manque.
// =============================================================================
#pragma once

#include <algorithm>
#include <print>
#include <string>

class Joueur
{
public:
    // -------------------------------------------------------------- 1. courir
    // Courir coute 10 points d'endurance.
    // Si l'endurance est insuffisante, le joueur ne court pas : il ne se passe
    // rien, et l'endurance ne descend JAMAIS sous zero.
    // Renvoie true si le joueur a effectivement couru.
    bool courir()
    {
        // TODO : verifier l'endurance, la depenser, renvoyer le bon resultat.
        return false;
    }

    // ---------------------------------------------------------- 2. se reposer
    // Se reposer remonte l'endurance jusqu'au maximum, jamais au-dela.
    void seReposer()
    {
        // TODO
    }

    // -------------------------------------------------------- 3. ouvrir porte
    // Ouvrir une porte consomme une cle.
    // Sans cle, la porte reste fermee et le compteur ne devient pas negatif.
    // Renvoie true si la porte s'est ouverte.
    bool ouvrirPorte()
    {
        // TODO
        return false;
    }

    // -------------------------------------------------------------- 4. acheter
    // Acheter coute `prix` pieces d'or.
    // Si l'or manque, l'achat est refuse et l'or ne bouge pas.
    // Renvoie true si l'achat a eu lieu.
    bool acheter(int prix)
    {
        // TODO
        return false;
    }

    // --------------------------------------------------------- 5. subir degats
    // Les points de vie restent entre 0 et le maximum, quoi qu'il arrive.
    void subirDegats(int degats)
    {
        // TODO
    }

    // --------------------------------------------------------------- lecture
    // Le menu a besoin d'afficher l'etat du joueur et de savoir s'il est en vie.
    // Ces deux methodes ne modifient rien : elles sont `const`.
    bool estVivant() const
    {
        // TODO
        return true;
    }

    void afficherFiche() const
    {
        std::println("{} | vie {}/{} | endurance {}/{} | or {} | cles {}",
                     nom_, vie_, vieMax_, endurance_, enduranceMax_, or_, cles_);
    }

private:
    // Rien de tout cela ne doit devenir public.
    std::string nom_ = "Kael";
    int vie_ = 100;
    int vieMax_ = 100;
    int endurance_ = 50;
    int enduranceMax_ = 50;
    int or_ = 30;
    int cles_ = 2;
};
