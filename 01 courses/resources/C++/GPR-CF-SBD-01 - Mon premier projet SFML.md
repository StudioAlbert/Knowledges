---
seances:
  - GPR-CF-SBD-01
---
# Mon premier projet SFML

Quatre étapes, un quart d'heure. À la fin, une fenêtre noire s'ouvre et se ferme
proprement. C'est le point de départ de **tous** vos travaux de la série.

> [!info] Ce qu'on installe
> **SFML 3.1**, récupérée par **vcpkg**. Vous ne téléchargez rien à la main, et
> vous ne copiez aucune DLL : vcpkg et CMake s'en occupent.

---

## 1 — Le projet, dans CLion

**File → New Project → C++ Executable**.

- **Language standard** : `C++23`
- **Location** : un dossier sans accent ni espace dans le chemin

CLion crée un `CMakeLists.txt` et un `main.cpp`. On va remplacer les deux.

---

## 2 — vcpkg

CLion sait installer vcpkg lui-même.

1. **View → Tool Windows → Vcpkg**
2. le **+** en haut du panneau, puis **Add vcpkg repository**
3. laissez *Download and install* coché, validez

CLion clone vcpkg et ajoute tout seul la toolchain à votre profil CMake. C'est la
ligne que vous n'aurez plus à écrire.

> [!tip] Si vous préférez la main
> `git clone https://github.com/microsoft/vcpkg` puis `.\bootstrap-vcpkg.bat`, et
> dans **Settings → Build, Execution, Deployment → CMake → CMake options** :
>
> ```
> -DCMAKE_TOOLCHAIN_FILE=C:/chemin/vers/vcpkg/scripts/buildsystems/vcpkg.cmake
> ```

---

## 3 — Déclarer SFML

Deux fichiers à la racine du projet, à côté du `CMakeLists.txt`.

**`vcpkg.json`** — ce que le projet demande :

```json
{
  "name": "mon-platformer",
  "version": "0.1.0",
  "dependencies": [
    {
      "name": "sfml",
      "default-features": false,
      "features": ["graphics", "window", "audio"]
    }
  ]
}
```

**`CMakeLists.txt`** — remplacez celui de CLion :

```cmake
cmake_minimum_required(VERSION 3.28)
project(MonPlatformer CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Vos sources sont en UTF-8 ; MSVC ne le devine pas.
if(MSVC)
    add_compile_options(/utf-8)
endif()

find_package(SFML 3 COMPONENTS Graphics Audio REQUIRED)

add_executable(MonPlatformer main.cpp)
target_link_libraries(MonPlatformer PRIVATE SFML::Graphics SFML::Audio)
```

Rechargez le projet — **le petit icône de rechargement**, ou `Ctrl+Maj+A` puis
*Reload CMake Project*. vcpkg télécharge et compile SFML. **La première fois prend
quelques minutes** ; les suivantes sont instantanées, le résultat est mis en cache.

> [!check] Ce que vous devez lire dans la console
> ```
> -- Found SFML 3.1.0 in .../vcpkg_installed/x64-windows/share/sfml
> -- Configuring done
> ```
> Si `find_package` échoue, c'est la toolchain qui manque : reprenez l'étape 2.

---

## 4 — Afficher une fenêtre

**`main.cpp`** :

```cpp
#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow fenetre(sf::VideoMode({800, 600}), "Mon platformer");
    fenetre.setFramerateLimit(60);

    while (fenetre.isOpen())
    {
        while (const std::optional evenement = fenetre.pollEvent())
        {
            if (evenement->is<sf::Event::Closed>())
                fenetre.close();
        }

        fenetre.clear(sf::Color(26, 26, 26));
        fenetre.display();
    }
}
```

Lancez. Une fenêtre gris foncé de 800 × 600 s'ouvre, et la croix la ferme.

---

## Ce que fait chaque ligne

| Ligne | Ce qu'elle fait |
|---|---|
| `sf::VideoMode({800, 600})` | la taille, en un seul vecteur — SFML 3 a abandonné les deux entiers séparés |
| `setFramerateLimit(60)` | plafonne la boucle, sinon elle tourne à fond et chauffe la machine |
| `while (const std::optional evenement = ...)` | `pollEvent` rend un **optionnel** : vide quand la file est épuisée |
| `evenement->is<sf::Event::Closed>()` | les événements de SFML 3 sont des **types**, plus un `enum` |
| `clear` puis `display` | on efface, on dessine, on montre — dans cet ordre, à chaque image |

> [!warning] Les exemples trouvés en ligne
> La plupart datent de **SFML 2** et ne compileront pas. Le signe qui ne trompe
> pas : `sf::Event event; while (window.pollEvent(event))`. Si vous lisez ça, la
> page est périmée.

---

## Le dépôt d'exemples

```github
https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples
```

Dix-neuf programmes qu'on lit ensemble en cours, du `HelloWorld` ci-dessus au
`Motor`, qui ressemble à un vrai jeu. Deux détails utiles :

- `_Resources/sprites/` tient les images — planches Cuphead, Zelda, un village,
  un mur. Vous n'avez pas à chercher des PNG.
- Le dépôt récupère SFML par `FetchContent` et non par vcpkg. C'est un choix fait
  pour qu'il se compile partout sans rien installer ; **votre** projet, lui, prend
  vcpkg.

> [!check] Je sais…
>
> | | Vérification |
> |---|---|
> | créer un projet CMake dans CLion | il configure sans erreur |
> | brancher vcpkg | la console affiche `Found SFML 3.1.0` |
> | déclarer une dépendance | ajouter `audio` à `vcpkg.json` suffit à l'obtenir |
> | ouvrir une fenêtre | elle s'affiche, et la croix la ferme |
