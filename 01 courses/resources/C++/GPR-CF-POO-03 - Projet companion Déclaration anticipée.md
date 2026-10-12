---
seances: [GPR-CF-POO-03]
---
# Projet companion : la déclaration anticipée

Deux classes qui se connaissent : `Joueur` garde son `Arme`, et `Arme` connaît son porteur
pour écrire dans le journal. Écrit naïvement, **ça ne compile pas** — et la sortie tient en
une ligne.

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

## Voir le problème

`01_forward_declaration/include/arme.h` porte les deux versions, l'une commentée.
**Commenter l'annonce et décommenter le `#include`** — les deux, sinon l'annonce suffit
encore et le projet compile. Recompiler, et lire :

```text
arme.h(18): error C2143: erreur de syntaxe: absence de ';' avant '*'
```

Peu importe lequel des deux en-têtes est lu en premier : la garde de l'autre casse la
boucle, et celui qui passe en second n'a jamais vu la déclaration dont il a besoin.

## Ce qu'il reste à comprendre

L'annonce `class Joueur;` suffit à `Arme` parce qu'`Arme` ne garde qu'un **pointeur** : sa
taille est connue sans connaître le type. Deux façons de s'en convaincre, et le compilateur
répond aux deux :

- remplacer `Joueur* joueur_` par un `Joueur joueur_` **par valeur** ;
- appeler une méthode de `Joueur` depuis `arme.h`.

`Joueur`, lui, garde son `Arme` par valeur : il lui faut le type complet, donc le vrai
`#include "arme.h"`. Une seule des deux dépendances est un vrai include — c'est ce qui coupe
le cycle.
