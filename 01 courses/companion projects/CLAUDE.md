# Companion projects

Le code d'une séance. Un companion = un dépôt public `<CODE>_<Nom>` ajouté ici en
**sous-module** : un changement dedans demande un commit là-bas *et* un bump de pointeur ici.

Pour tout ce qui est nommage, extensions et découpe des fichiers, voir la skill
**`programmation-cpp`** (Google C++ Style Guide : headers `.h`, implémentations `.cc`).

## Structure — intangible à la création

- **Jamais de `main` à la racine** du projet, ni de header : la racine ne porte que
  `CMakeLists.txt`, `README.md`, `.gitignore`, `.clang-format`.
- **Un répertoire par programme** — un sujet d'exercice, une démonstration — et **une target
  par répertoire**.
- `CMakeLists.txt` racine : réglages communs puis un `add_subdirectory` par répertoire.

  ```cmake
  cmake_minimum_required(VERSION 3.16)
  project(GPR_CF_POO_01_Structures CXX)

  set(CMAKE_CXX_STANDARD 23)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
  set(CMAKE_CXX_EXTENSIONS OFF)

  add_subdirectory(01_structures)
  add_subdirectory(02_membres)
  ```

- `CMakeLists.txt` de sous-répertoire : un seul `add_executable`, nommé comme le dossier.

  ```cmake
  add_executable(01_structures main.cc)
  ```

- Répertoires **numérotés** quand l'ordre pédagogique compte (`01_…`, `02_…`), imbriqués si une
  étape a plusieurs variantes.
- `README.md` dans le répertoire dès que l'étape porte une consigne.
- Gabarit de référence : `C++/cpp_astar_course_companion`.

## Hygiène

`.gitignore` dès la création — `build/`, `cmake-build-*/`, `.idea/`. Les dossiers de build et
les réglages d'IDE ne sont pas versionnés.

## Existant

Les companions nés sous CLion sont plats (`main.cpp` + headers à la racine, une seule target) et
ne sont pas conformes. On ne les migre pas d'office : proposer la mise en conformité au cas par
cas et la faire valider. `GPR-CF-BDP-04` et `GPR-CF-GTE-02` restent volontairement en l'état.
