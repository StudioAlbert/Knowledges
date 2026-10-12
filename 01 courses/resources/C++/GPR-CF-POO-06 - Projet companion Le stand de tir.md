---
seances: [GPR-CF-POO-06]
---
# Projet companion : le stand de tir

Le point de départ de la formative *L'armurerie*. Une arme, une classe, aucun parent, et un
menu qui l'appelle directement.

```github
StudioAlbert/GPR_CF_POO_06_HeritageEtPolymorphisme
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

## Ce qu'il contient

`Weapon` : un nom, des dégâts, un poids, un chargeur. `Fire()`, `Reload()`, `CanFire()`.
Le menu lit une touche et appelle la méthode.

Touches : `1` pour tirer, `r` pour recharger, `q` pour quitter.

## Ce qu'on en fait

Ajoutez une deuxième arme. Puis une troisième. Au bout de deux copier-coller, la hiérarchie
s'impose — et c'est exactement le sujet de la séance.

L'énoncé complet :
[[01 courses/projects/C++/Formative - OOP - L'armurerie|Formative — l'armurerie]].
