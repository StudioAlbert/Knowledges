---
title: Premier projet CMake
type: course
status: Backlog
subject: C++
duration_h: 3
bloc_gsda: Environnement de Développement C++
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
manual_order: 7
---

---
 
# CMake
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

---

## CMake-gui
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Les champs à renseigner dans l'interface :

- répertoire contenant le code des projets VS
- répertoire de destination de la solution VS
- check de la configuration du projet CMake
- création de la solution

Note:
Cette diapo était une capture annotée de CMake-gui. Les libellés
ci-dessus sont les annotations d'origine ; se référer à la présentation
Drive pour voir l'emplacement exact des champs.

---

## CMake-gui — configuration
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- **choix de l'IDE**
- **choix du toolchain** : outil d'inclusion des librairies externes

---

## CMake — les instructions générées
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

À la fin du processus d'installation vcpkg, vous avez dû remarquer quelque chose comme :

```cmake
find_package(SDL2 CONFIG REQUIRED)
target_link_libraries(main PRIVATE SDL2::SDL2 SDL2::SDL2main)
```

These are instructions for CMake !

---

## So what is CMake?
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- CMake is an open-source, cross-platform family of tools designed to **build, test and package** software
- it generates Visual Studio files, Xcode files and makefiles
- so in a single file you can have multiple project generators
- this is a full language, so you could script your way out of it

---

## CMake — comment l'utiliser
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- create a new file named `CMakeLists.txt` in the root of your project
- edit this file

---

## CMake — l'en-tête du fichier
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

A CMake file starts with the version of CMake you intend to use :

```cmake
cmake_minimum_required(VERSION 3.10)
```

Then you need the name of your project :

```cmake
project(SoftwareGL)
```

---

## CMake — les dépendances
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Then you specify which outside libraries you want to use, and link them (remember vcpkg?) :

```cmake
find_package(SDL2 CONFIG REQUIRED)
find_package(GLEW REQUIRED)
```

We are almost done !

---

## CMake — les bibliothèques
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Now we can specify what we need to build : libraries and executables (you can have multiple of each).

`STATIC` is for the linking step — this means it is not a DLL.

```cmake
add_library(SoftwareGL STATIC
    ${PROJECT_SOURCE_DIR}/software_gl/Mesh.h
    ${PROJECT_SOURCE_DIR}/software_gl/Mesh.cpp
    […]
)
```

---

## CMake — les variables de chemin
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

`${PROJECT_SOURCE_DIR}` can be replaced by :

```cmake
${CMAKE_CURRENT_SOURCE_DIR}
```

You also have :

```cmake
${CMAKE_CURRENT_BINARY_DIR}
```

<small>[cmake.org/cmake/help/latest/manual/cmake-variables.7.html](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)</small>

---

## CMake — lier la bibliothèque
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```cmake
target_link_libraries(SoftwareGL
  PRIVATE
    SDL2::SDL2
    GLEW::GLEW
)
```

---

## CMake — l'exécutable
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Same thing for the executable. The `WIN32` flag specifies that we want a Windows executable, not a command-line one.

```cmake
add_executable(Game WIN32
    ${PROJECT_SOURCE_DIR}/example/main.cpp
    ${PROJECT_SOURCE_DIR}/example/WindowSoftwareGL.h
    ${PROJECT_SOURCE_DIR}/example/WindowSoftwareGL.cpp
)
```

---

## CMake — à propos de WIN32
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

You may or may not need the `WIN32` descriptor in your exe : it tells the linker to use `WinMain` and not `main` as an entry point.

As explained before, the `WIN32` descriptor specifies whether you want an executable without a command-line interface.

---

## CMake — lier l'exécutable
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```cmake
target_link_libraries(Game
  PRIVATE
    SoftwareGL
    SDL2::SDL2
    GLEW::GLEW
)
```

You may need `SDL2::SDL2main` too.

---

## CMake — le dossier build
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Now save it !

The usual way is to generate the files in a new directory, so create a `build` directory in your main folder :

```bash
mkdir build
cd build
```

---

## CMake — générer la solution
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```powershell
cmake .. -DCMAKE_TOOLCHAIN_FILE="$Env:VCPKG_ROOT\vcpkg\scripts\buildsystems\vcpkg.cmake"
```

- this should generate the `.sln` and the project files needed
- you can also drop the `.obj` and `.tga` (`.bmp`) in the build directory for it to work

---

## CMake — et maintenant
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- vous savez utiliser CMake et vcpkg : vous pouvez convertir tous vos projets C++
- ça demande un peu de temps pour s'y faire, mais ça vaut le temps passé
- **n'oubliez pas de déplacer les DLL pour les releases !**

---
