---
depot: https://github.com/StudioAlbert/GPR-CF-SBD-XX---SFML-Examples
---
Fiche de **session code**, pas de révision de séance : elle ne pilote aucune note de
`lectures/` et n'apparaît pas au kanban. Elle décrit un chantier à faire dans le dépôt
d'exemples, en une ou deux sessions dédiées.

## 1 — Passer la solution Visual Studio en CMake

- [ ] `CMakeLists.txt` racine : `cmake_minimum_required(VERSION 3.16)`, C++23, `EXTENSIONS OFF`, un `add_subdirectory` par cible
- [ ] récupérer SFML 3 par `FetchContent` plutôt que par chemin absolu — le dépôt doit se cloner et compiler sans rien installer
- [ ] un `CMakeLists.txt` par cible, un seul `add_executable`, nommé comme le dossier
- [ ] copier les `data/` à côté de l'exécutable (`add_custom_command POST_BUILD`), sinon rien ne charge
- [ ] supprimer les `.vcxproj`, `.vcxproj.filters` et le `.sln` une fois que tout compile
- [ ] `.gitignore` : `build/`, `cmake-build-*/`, `.vs/`, `out/`
- [ ] `README.md` racine : la liste des cibles, ce que chacune montre, et les deux commandes

## 2 — Porter les quatorze cibles en SFML 3

Audit du 20.10, dix-huit cibles. **Quatre sont déjà propres** et servent de modèle :
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

- [ ] `Events-a` — boucle d'événements, `setPosition(x, y)`
- [ ] `Events-b` — boucle d'événements, `VideoMode(w, h)`
- [ ] `Events-c` — les quatre à la fois, plus `sf::Keyboard::Key` sans scancode
- [ ] `Events-d` — boucle, `VideoMode`, `setPosition`, `setTexture`
- [ ] `Graphics` — boucle, `switch (event.type)`, `VideoMode`, `setPosition`
- [ ] `Animation` — `sprite.setTexture()`
- [ ] `AnimationClass` — `sprite.setTexture()`
- [ ] `OOPHero` — `sprite.setTexture()`
- [ ] `Motor` — `setPosition(x, y)`, `setTexture()` (le plus gros : sept paires de fichiers)
- [ ] `MoveAndJump` — boucle, `VideoMode`, `setOrigin`, `setPosition`, `Keyboard::Key`
- [ ] `Sound` — boucle, `VideoMode`, `Keyboard::Key`
- [ ] `Views` — les six marqueurs, le cas le plus abîmé
- [ ] `LevelEditor` (trois sous-projets) — boucle, `switch`, `VideoMode`, `setPosition`, `Keyboard::Key`
- [ ] `Views.cpp` à la racine — **doublon** de `Views/Views.cpp` : vérifier lequel fait foi, et supprimer l'autre

## 3 — Vérifier

- [ ] chaque cible **compile** et **se lance**, data comprise
- [ ] `Motor` et `LevelEditor` sont les deux seuls à avoir un vrai comportement à vérifier à l'écran
- [ ] une passe `grep` finale sur les marqueurs du tableau : aucun ne doit subsister

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
