---
seances: [TC-FT-RNLB-03]
---
# Projet companion : flottants IEEE 754

De quoi **vérifier ses réponses** aux exercices 1 à 3, qui se font sur papier. `std::bit_cast` donne le motif binaire d'un `float` sans passer par un cast qui mentirait, et le relit dans l'autre sens :

- `std::bit_cast<std::uint32_t>(12.5f)` — le motif de bits d'un flottant connu ;
- `std::bit_cast<float>(std::uint32_t{0xC0D00000})` — la valeur d'un motif donné.

Changez la constante, relancez, comparez avec ce que vous aviez trouvé à la main. Le [Float Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html) fait la même chose dans le navigateur, mais sans montrer le `bit_cast`.

```github
StudioAlbert/TC_FT_RNLB_03_FlottantsIEEE754
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
