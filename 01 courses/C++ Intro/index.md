# C++ Intro — 4FSC0PF001 · Introduction to Games Programming

Transposition en markdown du dossier Drive [1 - 4FSC0PF001 - Introduction to Games Programming](https://drive.google.com/drive/folders/1LIp0FH63ayK0ZbEqpVyEaAEoMpkfIllI), soit 35 fichiers : 15 présentations, 15 documents, 4 schémas et 1 tableur.

Les présentations sont des decks **Obsidian Advanced Slides**, directement projetables (`theme: white`, `_templates/css/sae_styles.css`). Chaque note porte en tête un lien vers son original Drive.

## Déroulé du module

| # | Cours | Exercices | Formative |
|:-:|---|---|---|
| 00 | [[00 - Setup - vcpkg, cmake]] | | |
| 00 | [[00 Tips - How to (Git, etc.)]] | [[00 - Git]] | |
| 01.01 | [[01.01 - Programming Basics - if, loops]] | [[Exercices - 01 - Programming Basics]] | |
| 01.02 | [[01.02 - Programming Basics 2-2 - enum, string]] | [[Exercices - 01b - Programming Basics (2-2) - enum, arrays, string]] | |
| 01.03 | [[01.03 - Basics OOP]] | | |
| 02 | [[02 - Introduction to logic - non decimal arithmetic]] | [[Exercices - 02 - Introduction to Logic]] | |
| 03 | [[03 - Data Structures (array, vector, map, etc.)]] | [[Exercices - 03 - Data Structures]] · [[Exercices - 03 - Data Structures - array]] | [[Formative - Poker Card Game]] |
| 04 | [[04 - OOP Advanced]] | [[Exercices - 04 - OOP]] | [[Formative - OOP Minigame (Monster Fight Simulator)]] · [[Formative - OOP - Creer un verger]] |
| 04 | [[04 - Good practices]] | | |
| 06 | [[06 - Program Structure, Function pointers, lambdas]] | [[Exercices - 06 - Program Structure, Function pointers, lambdas]] | |
| 07 | [[07 - Deeper dive into STD 1-2 - iofile, stringstream, algorithms]] | [[Exercices - 07b - Deeper dive into STD - File IO]] | |
| 07 | [[07 - Deeper dive into STD 2-2 - Algorithms]] | [[Exercices - 07a - Deeper dive into STD - algorithms]] | |
| 08 | [[08 - Theorical Notions of graphics programming - Maths]] | [[Exercices - 08 - Introduction to Maths]] | |
| 10 | [[10 - SFML]] | [[Exercices - 10 - SFML]] | |
| 11 | [[11 - Box 2D]] | | |

## Schémas et ressources

- [[Formative - Poker Card Game - Sequence]] — ordre de distribution des cartes
- [[Formative - Poker - Hand Evaluation]] — constitution de la main à évaluer
- [[Formative - OOP - Inventory]] — hiérarchie de classes `Item` / `Inventory`
- [[Algo Treasure Hunt]] — organigramme d'exemple, avant implémentation
- [[Truth table]] — tables de vérité de référence des opérateurs booléens

## À savoir sur cette transposition

**Numérotation.** Elle est celle du Drive et comporte des irrégularités conservées telles quelles : deux séances portent le numéro `04` (*OOP Advanced* et *Good practices*), deux le numéro `07`, et les numéros **05 et 09 sont absents** du dossier d'origine.

**Doublon 07.** La présentation `07 - 2/2 : Algorithms` reprend à l'identique la seconde moitié de `07 - 1/2`. Les deux decks sont transposés séparément, comme dans le Drive ; si vous projetez le 1/2 en entier, le 2/2 fait doublon.

**Visuels.** L'export texte de Google Slides ne récupère ni les images, ni les captures d'écran, ni les notes du présentateur. Les diapos qui n'étaient qu'un visuel portent une note l'indiquant et renvoient vers l'original Drive. Deux cas notables : [[04 - Good practices]], dont la revue de code est entièrement en captures, et les schémas mémoire de [[03 - Data Structures (array, vector, map, etc.)]], reconstitués ici en ASCII.

**Reconstitutions.** Quand une diapo n'était qu'une capture de code, l'exemple a parfois été reconstitué à partir du texte de la diapo voisine ; ces cas sont signalés par un bloc `Note:` dans le deck concerné.

**Coquilles conservées.** Les erreurs de la source sont transposées telles quelles et signalées en note, plutôt que corrigées silencieusement : l'inversion *turn* / *river* dans [[Formative - Poker Card Game - Sequence]], le titre « Hunter » sur une diapo décrivant vcpkg dans [[00 - Setup - vcpkg, cmake]], et le « std::list » mis pour « std::stack » dans [[03 - Data Structures (array, vector, map, etc.)]].
