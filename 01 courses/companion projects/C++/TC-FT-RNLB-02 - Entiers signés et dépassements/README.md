# Entiers signés et dépassements — companion TC-FT-RNLB-02

Tous les exemples de code du cours, prêts à compiler et à modifier.

| Fichier | Rôle |
|---|---|
| `src/EntiersSignes.h` | **Toutes les démos**, une fonction par slide, dans l'ordre du deck |
| `src/Affichage.h/.cpp` | Outils d'affichage : titre de slide, bits d'un octet, pause |
| `src/main.cpp` | Enchaîne les démos, partie par partie |

Chaque fonction porte en commentaire le nom de sa slide, et l'affiche en première ligne.

## Compiler et lancer

```bash
cmake -S . -B build
cmake --build build
./build/EntiersSignes        # Windows : build\Debug\EntiersSignes.exe
```

Deux avertissements de compilation sont **voulus** : la comparaison signé / non signé
(`melange`) et la boucle `i >= 0` toujours vraie (`piegeNonSigne`). Lisez-les.

## Voir le comportement indéfini (GCC / Clang)

```bash
cmake -S . -B build-ub -DSANITIZE=ON
cmake --build build-ub
./build-ub/EntiersSignes
```

Le programme signale `signed integer overflow` à la ligne de `INT_MAX + 1`.

## À essayer

- Changer `niveau = 254` dans `pacMan()` et prévoir la sortie avant de relancer.
- Lire `plusGrandQueLui` : pourquoi le compilateur a-t-il le droit de répondre `true` ?
- Lancer le programme sur un autre système et comparer `mesurerSaPlateforme()`.
