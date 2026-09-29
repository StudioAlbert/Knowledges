---
status: Ready
manual_order: 3
slides:
  - "[[01 courses/slides/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements|Slides RNLB-02]]"
exercices:
  - "[[01 courses/exercises/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements|Exos RNLB-02]]"
---
- [x] preparer projet companion avec tous les snippets du cours
- [x] Clarifier ce point, ajouter des notes de slide, donner sources.
> Un entier non signé calcule **modulo 2ⁿ**. C'est défini par la norme.

- [x] Remplacer "Detecte avant de ..." par une presentation de std::numeric_limits et son interet pour notre problematique
- [x] Refaire companion
	- [x] un seul fichier .h avec les fonctions necessaires (exception : Garder fichier Affichage.h )
	- [x] Le titre est mis en dur en haut de chaque fonction
	- [x] Mettre commentaires avec le nom des slides
- [x] supprimer slides sur modulo 2n
- [x] Transformer cet exercice 6 en slides, ajouter dans les notes presentateur les differentes plateformes a essayer (si possible proposer page godbolt toute faite)
- [x] le markdown des slides est bizarre, vérifier formatage a pertir de Plages representables


Comparer avec les résultats d'un camarade sur un autre système, ou sur [Compiler Explorer](https://godbolt.org/) avec un compilateur GCC pour Linux.

## Traité le 28.09 — à vérifier

- **Companion** : `01 courses/companion projects/C++/TC-FT-RNLB-02 - Entiers signés et dépassements` — 4 fichiers de démo (un par partie du deck), chaque fonction titrée comme sa slide ; option CMake `SANITIZE` pour voir l'UB. Note ressources `01 courses/resources/Theory/TC-FT-RNLB-02 - Projet companion.md`.
- **Modulo 2ⁿ** : 1 slide → 4 slides (code ; schéma du cercle 3 bits ; table « n bits gardés = reste de la division par 2ⁿ » ; pourquoi « défini par la norme » compte), notes de slide, sources dans les notes et dans *Pour aller plus loin*.
- Schéma : `00 images/rnlb02_modulo_roue.svg`, généré par `tools/schemas/rnlb02_modulo_roue.py` (+ `Excalidraw/RNLB-02 - Modulo 2n, le cercle.excalidraw.md`), selon la convention du README.

> [!warning] Fichiers à supprimer à la main
> Une première version du schéma a été posée par erreur dans `01 courses/slides/Theory/` : supprimer `rnlb02_modulo_roue.png` et `rnlb02_modulo_roue.svg` de ce dossier (je ne peux pas supprimer de fichiers).

> [!warning] À faire de ton côté
> Publier `StudioAlbert/TC_FT_RNLB_02_EntiersSignes` (procédure dans la note de séance).

## Retraité le 28.09 (2ᵉ passe)

- **numeric_limits** : *Détecter avant de déborder* remplacée par *std::numeric_limits : la fiche d'identité d'un type* (4 puces), *std::numeric_limits, en code* et *Tester avant de déborder* (l'intérêt pour le dépassement : comparer à la borne avant de calculer).
- **Companion refait** : un seul `src/EntiersSignes.h` avec toutes les démos (plus `Affichage.h/.cpp` gardé à part) ; chaque fonction commence par `titre("…")` en dur et porte en commentaire `// Slide « … »` ; ordre et titres alignés sur le deck révisé. Compilé et exécuté (GCC 14, Clang 18).
- **Modulo 2ⁿ** : les 3 slides supprimées ; une phrase d'explication et la source restent dans la note de *Dépassement non signé : ça tourne*.
- **Exercice 6** : devenu la slide *À vous : mesurer sa plateforme* (code + lien Compiler Explorer). Notes présentateur : résultats attendus sur Linux 64, Windows MSVC, 32 bits, ARM64, AVR (x86-64 et AVR vérifiés ici). Lien Compiler Explorer préparé (GCC x86-64 et `-m32`) mais **non testé** : le site était injoignable depuis ma session.
- Slide *Exercices* du deck mise à jour (plus d'« additionner sans déborder »).

> [!warning] À faire de ton côté
> - Supprimer dans le companion : `src/01_NonSignes.cpp`, `02_ComplementADeux.cpp`, `03_Depassements.cpp`, `04_TailleDesTypes.cpp`, `Affichage.hpp`, `Demos.hpp` (et relancer CMake dans CLion).
> - Tester le lien Compiler Explorer de la slide *À vous : mesurer sa plateforme*.
> - Fiche d'exercices : l'intro annonce encore « les exercices 5 et 6 sont des programmes C++ », et un *Bonus — même chose pour la multiplication* reste orphelin depuis que l'exercice 5 a été retiré.

## Retraité le 29.09

- **Markdown bizarre dans l'éditeur** : la ligne `<small>` de *Plages représentables* contenait `` `std::numeric_limits<T>` `` et `` `<limits>` ``. Une ligne qui commence par une balise HTML est lue comme du HTML par l'éditeur : les backticks n'y protègent rien, `<T>` et `<limits>` deviennent des balises jamais fermées, et la coloration part en vrille jusqu'à la fin de la note. Remplacée par une ligne Markdown simple : *En code : `std::numeric_limits<T>::min()` et `max()`, dans `<limits>`.*
- Vérifié : plus aucune ligne HTML contenant `<…>` dans le deck ; rendu du site (reveal.js) contrôlé slide par slide, inchangé.
