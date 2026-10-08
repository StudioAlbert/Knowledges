---
seances: [GPR-CF-POO-02]
---
# Projet companion : la classe `Joueur`

Le squelette de l'**exercice 4** de la séance *Classes et visibilité*. Le menu de commandes
est déjà écrit : vous ne complétez que **`joueur.h`**, où chaque méthode porte un `// TODO`
et la règle à tenir.

```github
StudioAlbert/GPR_CF_POO_02_ClassesEtVisibilite
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

Le projet compile et tourne tel quel — toutes les actions sont refusées, c'est le point de
départ.
La règle qu'on vérifiera : **aucun attribut public**.
