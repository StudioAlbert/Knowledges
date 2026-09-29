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
```
