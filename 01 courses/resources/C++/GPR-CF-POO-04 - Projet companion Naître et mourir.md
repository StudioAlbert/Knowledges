---
seances: [GPR-CF-POO-04]
---
# Projet companion : naître et mourir

Une classe `Entity` qui écrit une ligne à sa naissance et une à sa mort, et trois programmes
qui la font vivre dans trois situations. **La sortie console est le cours** : prédire la
trace avant de lancer, puis comparer.

```github
StudioAlbert/GPR_CF_POO_04_CycleDeVieDeLObjet
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

## Les trois situations

| Étape | Ce qu'elle montre |
|---|---|
| `01_dans_le_main` | l'objet meurt à l'accolade fermante, donc **après** la dernière ligne du `main` |
| `02_dans_une_fonction` | la fonction a sa propre portée : l'objet y meurt **avant** que le `main` reprenne |
| `03_deux_entites` | deux objets, construits dans l'ordre, détruits dans l'ordre **inverse** |

`entity/` porte la classe, partagée par les trois cibles : une seule ligne changée se voit
dans les trois traces.

## La règle du jeu

Avant de lancer un programme, **écrire la trace qu'on attend**. Puis lancer, et expliquer
l'écart. Les trois traces attendues sont dans le `README.md` du dépôt, à ne lire qu'après.

## À essayer

- mettre une entité dans un bloc `{ }` au milieu du `main`, et prédire où passe sa mort ;
- dans `03`, échanger les deux déclarations : qu'est-ce qui change ?
- ajouter une troisième entité entre les deux, et vérifier la règle sur trois.
