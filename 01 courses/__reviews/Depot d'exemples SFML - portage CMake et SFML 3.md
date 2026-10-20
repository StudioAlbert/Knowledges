---
depot: https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples
---
Fiche de **session code**, pas de révision de séance : elle ne pilote aucune note de
`lectures/` et n'apparaît pas au kanban. Elle décrit un chantier à faire dans le dépôt
d'exemples, en une ou deux sessions dédiées.

## 1 — Passer la solution Visual Studio en CMake

- [x] `CMakeLists.txt` racine : `cmake_minimum_required(VERSION 3.16)`, C++23, `EXTENSIONS OFF`, un `add_subdirectory` par cible
- [x] récupérer SFML 3 par `FetchContent` plutôt que par chemin absolu — le dépôt doit se cloner et compiler sans rien installer
- [x] un `CMakeLists.txt` par cible, un seul `add_executable`, nommé comme le dossier
- [x] copier les `data/` à côté de l'exécutable (`add_custom_command POST_BUILD`), sinon rien ne charge
- [x] supprimer les `.vcxproj`, `.vcxproj.filters` et le `.sln` une fois que tout compile
- [x] `.gitignore` : `build/`, `cmake-build-*/`, `.vs/`, `out/`
- [x] `README.md` racine : la liste des cibles, ce que chacune montre, et les deux commandes

## 2 — Porter les quatorze cibles en SFML 3

Audit du 20.10, dix-neuf cibles (`LevelEditor` en porte trois). **Quatre sont déjà propres** et servent de modèle :
`Audio`, `ConstMethods`, `HelloWorld`, `TimeClock`.

### Les quatre corrections, toujours les mêmes

| SFML 2 | SFML 3 |
|---|---|
| `sf::Event e; while (window.pollEvent(e))` | `while (const std::optional event = window.pollEvent())` |
| `switch (event.type)` / `event.type == sf::Event::X` | `event->is<sf::Event::X>()`, `event->getIf<sf::Event::X>()` |
| `sf::VideoMode(800, 600)` | `sf::VideoMode({800, 600})` |
| `setPosition(x, y)`, `setOrigin(x, y)`, `move(x, y)` | un **vecteur** : `setPosition({x, y})` |
| `sf::Sprite s; s.setTexture(t);` | `sf::Sprite s(t);` — la texture est obligatoire |
| `sf::Keyboard::Escape` | `sf::Keyboard::Scancode::Escape`, via `->scancode` |
| `event.size.width` / `.height` | `resized->size.x` / `.y` |

### Cible par cible

- [x] `Events-a` — boucle d'événements, `setPosition(x, y)`
- [x] `Events-b` — boucle d'événements, `VideoMode(w, h)`
- [x] `Events-c` — les quatre à la fois, plus `sf::Keyboard::Key` sans scancode
- [x] `Events-d` — boucle, `VideoMode`, `setPosition`, `setTexture`
- [x] `Graphics` — boucle, `switch (event.type)`, `VideoMode`, `setPosition`
- [x] `Animation` — `sprite.setTexture()`
- [x] `AnimationClass` — `sprite.setTexture()`
- [x] `OOPHero` — `sprite.setTexture()`
- [x] `Motor` — `setPosition(x, y)`, `setTexture()` (le plus gros : sept paires de fichiers)
- [x] `MoveAndJump` — boucle, `VideoMode`, `setOrigin`, `setPosition`, `Keyboard::Key`
- [x] `Sound` — boucle, `VideoMode`, `Keyboard::Key`
- [x] `Views` — les six marqueurs, le cas le plus abîmé
- [x] `LevelEditor` (trois sous-projets) — boucle, `switch`, `VideoMode`, `setPosition`, `Keyboard::Key`
- [x] `Views.cpp` à la racine — **doublon** de `Views/Views.cpp` : c'était le squelette vide, supprimé ; `Views/Views.cpp` fait foi

## 3 — Vérifier

- [x] chaque cible **compile** et **se lance**, data comprise
- [ ] `Motor` et `LevelEditor` sont les deux seuls à avoir un vrai comportement à vérifier à l'écran
- [x] une passe `grep` finale sur les marqueurs du tableau : aucun ne doit subsister

## Ce que ça débloque

Les séances SBD citent ce dépôt comme source de code. Tant que quatorze cibles sur dix-huit
ne compilent pas, **on ne peut pas y envoyer les étudiants** : ils tomberaient sur les
erreurs que la feuille d'exercices leur dit justement d'éviter.

Correspondance entre les cibles et le nouveau découpage de la série :

| Séance | Cibles qui la servent |
|---|---|
| SBD-01 — Afficher | `HelloWorld` ✅, `Graphics` |
| SBD-02 — Gameplay et événements | `Events-a` à `-d`, `Audio` ✅, `Sound` |
| SBD-03 — Déplacer et animer | `TimeClock` ✅, `Animation`, `AnimationClass`, `MoveAndJump` |
| SBD-05 — Relier les deux mondes | `Views`, `Motor` |
| SBD-06 — Les ficelles | `MoveAndJump`, `LevelEditor` |

> [!note] Ordre proposé
> Commencer par `Events-a` à `-d` : quatre petits fichiers, les mêmes corrections, et ils
> servent la séance la plus proche. Finir par `Motor` et `LevelEditor`, qui sont les seuls
> vrais projets.

## Fait le 20.10

Le dépôt est aplati : les dix-neuf répertoires de cibles sont remontés à la racine, le dossier
`923-4FSC0PF001-SFML/` a disparu, les `git mv` gardent l'historique. SFML est épinglée en
**3.1.0**, statique, par `FetchContent` : rien à installer, pas de DLL à copier. Racine :
`CMakeLists.txt`, `README.md`, `.gitignore`, `.clang-format`.

Vérifié ici, MSVC 14.51 / CMake 4.3 / Ninja : **les dix-neuf cibles compilent**, zéro
avertissement sur notre code, et **les dix-sept qui ouvrent une fenêtre tournent** avec leur
`data/` à côté — rien sur `stderr`, donc aucune texture ni aucun son manquant.
`ConstMethods` et `TimeClock` n'ont pas de fenêtre et sortent en 0. Passe `grep` finale : plus
un seul marqueur du tableau.

Corrigé en passant, hors portage SFML :

- `ConstMethods` ne compilait pas — `Machin m;` sans constructeur par défaut.
- `AnimationClass` utilisait `std::filesystem` sans l'inclure, et `Animation.hpp` `std::vector`
  sans l'inclure.
- `Views/Views.cpp` dessinait **dans** la boucle d'événements, et son `default:` était imbriqué
  dans un `if`.
- `Motor` : `StarshipPlayer::Load(spawnPosition)` ignorait son paramètre et plaçait le vaisseau
  en `{400, 0}` ; `#include "Motor.h"` au lieu de `motor.h` ; chemins `data\sprites\` en
  antislashs.
- `LevelEditor/03_save_load` : `F9` sur un niveau absent passait un `FILE*` nul à `fread`.
- Sources converties en UTF-8 (trois fichiers étaient en CP1252), `/utf-8` ajouté pour MSVC.

Reste à faire, et ça demande quelqu'un au clavier : jouer `Motor` (tirer, faire apparaître un
ennemi avec `E`, se faire toucher) et les trois `LevelEditor` (peindre des tuiles, se déplacer
en `WASD`, `F5` puis `F9`).

> [!note] Deux propositions non faites
> Les headers de `Motor` et de `AnimationClass` sont en `.hpp` et mélangés aux `.cc`, contre la
> convention `.h` / `.cc` de la skill `programmation-cpp` ; renommer demande de toucher aux
> `#include`. Et `/W4 /permissive-` sur nos cibles seulement, pour que les exemples ne passent
> plus un avertissement sous silence.
