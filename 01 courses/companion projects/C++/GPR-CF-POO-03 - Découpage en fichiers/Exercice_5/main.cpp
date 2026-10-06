// =============================================================================
//  GPR-CF-POO-03 — Le donjon, tout dans un seul fichier
//
//  Ce programme marche. Il est juste illisible : quatre concepts sans rapport
//  cohabitent dans un fichier unique, et personne ne peut travailler dessus en
//  meme temps que vous.
//
//  Votre travail : le decouper en quatre duos .h / .cpp, sans changer une
//  virgule de son comportement. Les quatre bandeaux ci-dessous marquent les
//  frontieres.
// =============================================================================
#include <algorithm>
#include <iostream>
#include <print>
#include <string>
#include <vector>

// =============================================================================
//  CONCEPT 1 — Vector2 : une position dans le donjon
// =============================================================================

struct Vector2
{
    int x = 0;
    int y = 0;
};

Vector2 Ajouter(Vector2 a, Vector2 b)
{
    return {a.x + b.x, a.y + b.y};
}

bool Identiques(Vector2 a, Vector2 b)
{
    return a.x == b.x && a.y == b.y;
}

std::string EnTexte(Vector2 v)
{
    return "(" + std::to_string(v.x) + ", " + std::to_string(v.y) + ")";
}

// =============================================================================
//  CONCEPT 2 — Journal : tout ce qui s'est passe, dans l'ordre
// =============================================================================

class Journal
{
public:
    void ecrire(const std::string& ligne)
    {
        lignes_.push_back(ligne);
    }

    void afficherTout() const
    {
        std::println("--- journal ---");
        for (const std::string& l : lignes_)
        {
            std::println("  {}", l);
        }
        std::println("--- {} evenements ---", lignes_.size());
    }

    void afficherDernier() const
    {
        if (!lignes_.empty())
        {
            std::println("{}", lignes_.back());
        }
    }

private:
    std::vector<std::string> lignes_;
};

// =============================================================================
//  CONCEPT 3 — Entite : le joueur, et tout ce qui peut recevoir des coups
// =============================================================================

class Entite
{
public:
    Entite() = default;

    void nommer(const std::string& nom) { nom_ = nom; }
    void placer(Vector2 position) { position_ = position; }
    void reglerVie(int vie, int degats)
    {
        pointsDeVieMax_ = vie;
        pointsDeVie_ = vie;
        degats_ = degats;
    }

    void subirDegats(int degats)
    {
        pointsDeVie_ = std::max(0, pointsDeVie_ - degats);
    }

    void deplacer(Vector2 pas) { position_ = Ajouter(position_, pas); }

    bool estVivant() const { return pointsDeVie_ > 0; }
    int degats() const { return degats_; }
    Vector2 position() const { return position_; }
    const std::string& nom() const { return nom_; }

    std::string fiche() const
    {
        return nom_ + " " + EnTexte(position_) + " " + std::to_string(pointsDeVie_)
             + "/" + std::to_string(pointsDeVieMax_) + " pv";
    }

private:
    std::string nom_ = "sans nom";
    Vector2 position_;
    int pointsDeVieMax_ = 1;
    int pointsDeVie_ = 1;
    int degats_ = 0;
};

// =============================================================================
//  CONCEPT 4 — Salle : un endroit du donjon, et ce qu'il contient
// =============================================================================

class Salle
{
public:
    void decrire(const std::string& nom, const std::string& texte, Vector2 position)
    {
        nom_ = nom;
        texte_ = texte;
        position_ = position;
    }

    void poserMonstre(const Entite& monstre)
    {
        monstre_ = monstre;
        aUnMonstre_ = true;
    }

    bool estIci(Vector2 position) const { return Identiques(position_, position); }
    bool aUnMonstreVivant() const { return aUnMonstre_ && monstre_.estVivant(); }
    Entite& monstre() { return monstre_; }

    std::string description() const
    {
        std::string s = nom_ + " — " + texte_;
        if (aUnMonstreVivant())
        {
            s += " Un " + monstre_.nom() + " vous barre le passage.";
        }
        return s;
    }

private:
    std::string nom_ = "nulle part";
    std::string texte_;
    Vector2 position_;
    Entite monstre_;
    bool aUnMonstre_ = false;
};

// =============================================================================
//  LE JEU
// =============================================================================

namespace
{
    Salle* salleEn(std::vector<Salle>& salles, Vector2 position)
    {
        for (Salle& s : salles)
        {
            if (s.estIci(position)) { return &s; }
        }
        return nullptr;
    }

    void afficherAide()
    {
        std::println("");
        std::println("  z s q d  se deplacer");
        std::println("  a        attaquer");
        std::println("  j        lire le journal");
        std::println("  x        quitter");
        std::print("> ");
    }
}

int main()
{
    Journal journal;

    Entite joueur;
    joueur.nommer("Kael");
    joueur.placer({0, 0});
    joueur.reglerVie(60, 12);

    Entite gobelin;
    gobelin.nommer("gobelin");
    gobelin.reglerVie(30, 6);

    Entite troll;
    troll.nommer("troll");
    troll.reglerVie(55, 11);

    std::vector<Salle> salles(4);
    salles[0].decrire("Entree", "Une porte rouillee claque derriere vous.", {0, 0});
    salles[1].decrire("Couloir", "Des torches, et une odeur de moisi.", {0, 1});
    salles[2].decrire("Cave", "Il fait froid, et quelque chose respire.", {1, 1});
    salles[3].decrire("Tresor", "Un coffre, enfin.", {1, 0});
    salles[1].poserMonstre(gobelin);
    salles[2].poserMonstre(troll);

    journal.ecrire("Kael entre dans le donjon.");

    std::string commande;
    while (joueur.estVivant())
    {
        Salle* ici = salleEn(salles, joueur.position());
        if (ici == nullptr)
        {
            std::println("Le vide. Vous revenez sur vos pas.");
            joueur.placer({0, 0});
            continue;
        }

        std::println("");
        std::println("{}", ici->description());
        std::println("{}", joueur.fiche());
        afficherAide();

        if (!(std::cin >> commande)) { break; }
        if (commande.empty()) { continue; }

        Vector2 pas;
        switch (commande[0])
        {
        case 'z': pas = {0, 1}; break;
        case 's': pas = {0, -1}; break;
        case 'q': pas = {-1, 0}; break;
        case 'd': pas = {1, 0}; break;

        case 'a':
            if (!ici->aUnMonstreVivant())
            {
                journal.ecrire("Kael frappe dans le vide.");
                journal.afficherDernier();
                continue;
            }
            ici->monstre().subirDegats(joueur.degats());
            journal.ecrire("Kael frappe le " + ici->monstre().nom() + ".");
            if (ici->monstre().estVivant())
            {
                joueur.subirDegats(ici->monstre().degats());
                journal.ecrire("Le " + ici->monstre().nom() + " riposte.");
            }
            else
            {
                journal.ecrire("Le " + ici->monstre().nom() + " tombe.");
            }
            journal.afficherDernier();
            continue;

        case 'j':
            journal.afficherTout();
            continue;

        case 'x':
            journal.ecrire("Kael ressort du donjon.");
            journal.afficherTout();
            return 0;

        default:
            std::println("Commande inconnue.");
            continue;
        }

        if (ici->aUnMonstreVivant())
        {
            journal.ecrire("Le " + ici->monstre().nom() + " bloque le passage.");
            journal.afficherDernier();
            continue;
        }

        joueur.deplacer(pas);
        journal.ecrire("Kael passe en " + EnTexte(joueur.position()) + ".");
    }

    std::println("");
    std::println("Kael est mort dans le donjon.");
    journal.afficherTout();
    return 0;
}
