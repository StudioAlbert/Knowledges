---
seances: [GPR-CF-POO-03]
---
# Projet companion : le donjon

Le point de départ des exercices de la séance *Découpage en fichiers* : un petit jeu de
donjon en console, **entièrement dans un seul `main.cpp`** de près de 300 lignes.

Il marche. Il est juste illisible — et c'est le sujet.

```github
StudioAlbert/GPR_CF_POO_03_DecoupageEnFichiers
readme: false
```

> [!Tip] Forker et cloner en une commande
> `gh repo fork` fait les deux d'un coup : il crée le fork sur votre compte, le clone, et
> branche les deux remotes — `origin` sur votre fork, `upstream` sur le dépôt d'origine.
> Dans la commande qui suit :
> 1. Remplacez `<DEPOT>` par l'adresse de la fiche ci-dessus
> 2. Remplacez `<NOM-DU-FORK>` par le nom à donner à votre copie sur GitHub.
> 3. Remplacez `<DOSSIER-LOCAL>` par le dossier où cloner — il ne doit pas exister encore.

```bash
gh repo fork <DEPOT> --clone --fork-name <NOM-DU-FORK> -- <DOSSIER-LOCAL>
```

Quatre bandeaux de commentaires marquent les frontières : `Vector2`, `Journal`, `Entite`,
`Salle`. Chacun devient un duo `.h` / `.cpp`, et les deux premiers ne dépendent de personne
— c'est par là qu'on commence.

Ce qu'on vérifiera : **le jeu se comporte exactement pareil** après le découpage, chaque
en-tête a sa garde, et chaque `.cpp` est déclaré dans le `CMakeLists.txt` — aucun `.h`.
