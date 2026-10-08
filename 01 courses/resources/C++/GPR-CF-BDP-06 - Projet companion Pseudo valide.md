---
seances: [GPR-CF-BDP-06]
---
# Projet companion : pseudo valide ?

Ce que nous avons tapé **ensemble en classe** pour l'exercice 3 de la séance *Chaînes de
caractères*. Le squelette tourne : il lit un pseudo et refuse le vide.

```github
StudioAlbert/GPR_CF_BDP_06_ChainesDeCaracteres
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

Restent les trois règles suivantes — longueur minimale, longueur maximale, pas d'espace —
testées **dans cet ordre**, en s'arrêtant à la première qui échoue. Le message de
`checkEmpty` est celui du direct, pas celui de l'énoncé : à remplacer.
