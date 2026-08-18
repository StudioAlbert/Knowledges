---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Setup
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Installation logicielle — vcpkg, CMake

<small>Module 4FSC0PF001 · Introduction to Games Programming</small>

Note:
Séance outillage. L'objectif est qu'à la fin, chacun puisse récupérer une
bibliothèque externe et générer une solution Visual Studio sans toucher
manuellement aux propriétés du projet.

---

## Source
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine (contient les captures d'écran non transposées) :

- 🔗 [Google Slides — 00 Setup : vcpkg, cmake](https://docs.google.com/presentation/d/1OVcZbS1UI66iGssrPsT8pxC9PYVNvyA1RSnN8WcpXuM/edit)

Voir aussi : [[00 Tips - How to (Git, etc.)]]

</div>

---

# Prérequis
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Prerequisites
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

1. **OS** — Windows (11, 10, 8.1, 7), Linux ou macOS
2. **Visual Studio** — Community 2022 (fourni avec Unity)
    - english language pack
    - C++ development tools
    - Unity development tools
3. **Git**
4. **CMake** 3.12.4

---

## Install Git
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Download on the Git website : [gitforwindows.org](https://gitforwindows.org/)

Launch the install, pick every default option, except those below :

- pick a text editor (Atom advised)
- pick « Use Windows' default console window »

---

## Install CMake
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Download on the CMake website : [cmake.org/download](https://cmake.org/download/)

Launch the install, pick every default option, except those below :

- **add CMake to the system PATH**
- pick « Use Windows' default console window »

---

# Gestionnaires de paquets
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## vcpkg — pros
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- easy to get going (`git clone` then bootstrap it)
- easy to use existing packages (`vcpkg install foo`, plus the integration is nice for Visual Studio)
- non-intrusive CMake integration
- not too difficult to add new packages if you need them
- apparently very active work, meaning new packages get added all the time

---

## vcpkg — cons
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- builds everything from source. If you only want Boost as a header-only library, you still have to build it, which takes 30 min to 1 hour
- no easy way to request a particular version of a package

---

## Conan — pros
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- easy to get going (not quite as easy as vcpkg or Hunter, but still easy, with `pip install conan`)
- integrates into every build system
- recently got non-intrusive CMake integration
- gets **pre-built packages by default**, though you can request to build from source
- the Conan channel on the cpplang Slack has people who are very helpful

---

## Conan — cons
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- requires Python
- non-intrusive CMake integration is still somewhat intrusive by default, because it came much later — existing packages weren't aware of how to be easily consumed non-intrusively from Conan
- doesn't seem as easy to add new packages that you don't own, but doesn't seem that hard either

---

## Hunter — pros
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- easy to get going (just add the `HunterGate` command)
- easy to use with CMake — the command to find dependencies mirrors `find_package`
- designed with CMake as its only target, which means it adheres to good CMake practice with its generated targets. Of all the build systems tried, Hunter seems to understand good CMake practice the best.

---

## Hunter — cons
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- only supports CMake, and intrusive CMake integration
- adding new packages requires submitting a PR
- builds from source — Boost again takes a long time
- packages can only be installed when you run the configure step ; no way to install packages beforehand
- no easy way to request a particular version of a package

---

## Le package manager Windows
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- the package manager for Windows (and Linux and macOS)
- a central place to store different open-source projects — think `/port` for Windows
- have them included and linked automatically in all our projects (no more fiddling with the Visual Studio files)
- made and maintained by Microsoft

Note:
Cette diapo porte le titre « Hunter » dans la présentation d'origine,
mais son contenu décrit vcpkg. C'est vcpkg qui est le gestionnaire
maintenu par Microsoft, et c'est celui que l'on utilise dans le module.

---

# Utiliser vcpkg
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## vcpkg — installation
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small>[vcpkg.io](https://vcpkg.io/en/index.html)</small>

```bash
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
```

Start PowerShell and build :

```powershell
.\bootstrap-vcpkg.bat
```

---

## vcpkg — intégration et paquets
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Install vcpkg for the current system (only needed by msbuild) :

```powershell
.\vcpkg integrate install
```

Start installing the software needed :

```powershell
.\vcpkg install box2D
.\vcpkg install sfml
```

---

## vcpkg — triplets
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

You can specify the **triplet** at the end of the install to get a specific version of the library :

```
box2d:x64-windows
box2d:x86-windows
box2d:x64-windows-static
…
```

You can have multiple versions of the same library installed with different triplets.

---

## vcpkg — commandes
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

| Commande | Effet |
|---|---|
| `search` | search for packages available to be built |
| `install` | install a package |
| `remove` | uninstall a package |
| `list` | list installed packages |
| `update` | display list of packages for updating |
| `upgrade` | rebuild all outdated packages |

---

## vcpkg — à vous
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Installez vcpkg, puis la bibliothèque **Protobuf**.

Check which build you need (in VC++) :

- Win32 → `x86-windows`
- Win64 → `x64-windows`

You can always install both ;P

---

## Pause
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Question time !

Vous pouvez aussi jouer avec VS2019 — ou faire une pause, au cas où votre cerveau serait en train de fondre…

---

# CMake
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## CMake-gui
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

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
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- **choix de l'IDE**
- **choix du toolchain** : outil d'inclusion des librairies externes

---

## CMake — les instructions générées
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

À la fin du processus d'installation vcpkg, vous avez dû remarquer quelque chose comme :

```cmake
find_package(SDL2 CONFIG REQUIRED)
target_link_libraries(main PRIVATE SDL2::SDL2 SDL2::SDL2main)
```

These are instructions for CMake !

---

## So what is CMake?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- CMake is an open-source, cross-platform family of tools designed to **build, test and package** software
- it generates Visual Studio files, Xcode files and makefiles
- so in a single file you can have multiple project generators
- this is a full language, so you could script your way out of it

---

## CMake — comment l'utiliser
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- create a new file named `CMakeLists.txt` in the root of your project
- edit this file

---

## CMake — l'en-tête du fichier
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

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
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Then you specify which outside libraries you want to use, and link them (remember vcpkg?) :

```cmake
find_package(SDL2 CONFIG REQUIRED)
find_package(GLEW REQUIRED)
```

We are almost done !

---

## CMake — les bibliothèques
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

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
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

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
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

```cmake
target_link_libraries(SoftwareGL
  PRIVATE
    SDL2::SDL2
    GLEW::GLEW
)
```

---

## CMake — l'exécutable
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

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
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

You may or may not need the `WIN32` descriptor in your exe : it tells the linker to use `WinMain` and not `main` as an entry point.

As explained before, the `WIN32` descriptor specifies whether you want an executable without a command-line interface.

---

## CMake — lier l'exécutable
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

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
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Now save it !

The usual way is to generate the files in a new directory, so create a `build` directory in your main folder :

```bash
mkdir build
cd build
```

---

## CMake — générer la solution
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

```powershell
cmake .. -DCMAKE_TOOLCHAIN_FILE="$Env:VCPKG_ROOT\vcpkg\scripts\buildsystems\vcpkg.cmake"
```

- this should generate the `.sln` and the project files needed
- you can also drop the `.obj` and `.tga` (`.bmp`) in the build directory for it to work

---

## CMake — et maintenant
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- vous savez utiliser CMake et vcpkg : vous pouvez convertir tous vos projets C++
- ça demande un peu de temps pour s'y faire, mais ça vaut le temps passé
- **n'oubliez pas de déplacer les DLL pour les releases !**

---

## Questions ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Question time !
