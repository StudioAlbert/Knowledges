---
title: Gestionnaires de paquets
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

# Gestionnaires de paquets
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

---

## vcpkg — pros
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- easy to get going (`git clone` then bootstrap it)
- easy to use existing packages (`vcpkg install foo`, plus the integration is nice for Visual Studio)
- non-intrusive CMake integration
- not too difficult to add new packages if you need them
- apparently very active work, meaning new packages get added all the time

---

## vcpkg — cons
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- builds everything from source. If you only want Boost as a header-only library, you still have to build it, which takes 30 min to 1 hour
- no easy way to request a particular version of a package

---

## Conan — pros
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- easy to get going (not quite as easy as vcpkg or Hunter, but still easy, with `pip install conan`)
- integrates into every build system
- recently got non-intrusive CMake integration
- gets **pre-built packages by default**, though you can request to build from source
- the Conan channel on the cpplang Slack has people who are very helpful

---

## Conan — cons
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- requires Python
- non-intrusive CMake integration is still somewhat intrusive by default, because it came much later — existing packages weren't aware of how to be easily consumed non-intrusively from Conan
- doesn't seem as easy to add new packages that you don't own, but doesn't seem that hard either

---

## Hunter — pros
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- easy to get going (just add the `HunterGate` command)
- easy to use with CMake — the command to find dependencies mirrors `find_package`
- designed with CMake as its only target, which means it adheres to good CMake practice with its generated targets. Of all the build systems tried, Hunter seems to understand good CMake practice the best.

---

## Hunter — cons
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- only supports CMake, and intrusive CMake integration
- adding new packages requires submitting a PR
- builds from source — Boost again takes a long time
- packages can only be installed when you run the configure step ; no way to install packages beforehand
- no easy way to request a particular version of a package

---

## Le package manager Windows
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

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
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

---

## vcpkg — installation
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

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
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

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
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

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
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

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
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Installez vcpkg, puis la bibliothèque **Protobuf**.

Check which build you need (in VC++) :

- Win32 → `x86-windows`
- Win64 → `x64-windows`

You can always install both ;P

---

## Pause
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Question time !

Vous pouvez aussi jouer avec VS2019 — ou faire une pause, au cas où votre cerveau serait en train de fondre…

---
