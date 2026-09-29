# Chasse au trésor — companion GPR-CF-GTE-02

Petit jeu console en C++ qui sert de terrain à l'atelier **Branches et intégration**.
Un trésor est enterré sous une plage de 5 × 5 cases ; le joueur creuse et un détecteur
lui dit s'il chauffe.

## Compiler et lancer

Ouvrir le dossier dans CLion (ou Visual Studio), qui lit le `CMakeLists.txt` — ou en
ligne de commande :

```bash
cmake -S . -B build
cmake --build build
./build/ChasseAuTresor        # Windows : build\Debug\ChasseAuTresor.exe
```

## Organisation du code

| Fichier | Rôle |
|---|---|
| `src/main.cpp` | Initialise le hasard et lance une partie |
| `src/Game.hpp/.cpp` | La boucle de jeu : creuser, compter les essais, finir la partie |
| `src/Treasure.hpp/.cpp` | Tirage de la position du trésor, calcul de distance |
| `src/Messages.hpp/.cpp` | Tout ce qui s'affiche et se saisit |
| `src/GameConfig.hpp` | Les réglages : taille de la plage, nombre d'essais |

## Bug connu

> Des joueurs signalent que, parfois, **on ne trouve jamais le trésor**, même en
> creusant toutes les cases. Abandonner (colonne `0`) affiche où il était.

L'énoncé complet de l'atelier est donné en cours.
