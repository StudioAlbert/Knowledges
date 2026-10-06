# Le donjon — companion GPR-CF-POO-03

Le point de départ des exercices de la séance *Découpage en fichiers* : un petit jeu de
donjon en console, **entièrement dans un seul `main.cpp`** de près de 300 lignes.

Il marche. Il est juste illisible — et c'est le sujet.

## Compiler et lancer

```bash
cmake -S . -B build
cmake --build build
./build/Donjon               # Windows : build\Debug\Donjon.exe
```

Commandes du jeu : `z s q d` pour se déplacer, `a` pour attaquer, `j` pour lire le journal,
`x` pour sortir.

## Les quatre concepts à séparer

`Exercice_5/main.cpp` est découpé par des bandeaux de commentaires. Chacun devient un duo
de fichiers.

| Concept | Ce qu'il porte | Dépend de |
|---|---|---|
| `Vector2` | une position, `Ajouter`, `Identiques`, `EnTexte` | rien |
| `Journal` | la liste des événements, et son affichage | rien |
| `Entite` | nom, vie, dégâts, position — le joueur et les monstres | `Vector2` |
| `Salle` | nom, description, position, le monstre qui s'y trouve | `Vector2`, `Entite` |

La dernière colonne donne l'ordre : `Vector2` et `Journal` d'abord, ils n'ont besoin de
personne.

## Ce qu'on vérifiera

- **le jeu se comporte exactement pareil** après le découpage qu'avant ;
- une **garde** en première ligne de chaque `.h` ;
- dans chaque en-tête, seulement ce que la **déclaration** exige — `<vector>` n'a rien à
  faire dans `Vector2.h` ;
- chaque `.cpp` déclaré dans le `CMakeLists.txt`, et aucun `.h`.

## Attention

`main.cpp` ne contient **aucune** garde d'inclusion aujourd'hui, et c'est normal : un `.cpp`
n'est jamais inclus par personne. Les gardes sont pour les en-têtes que vous allez créer.
