---
status: Ready
manual_order: 2
slides:
  - "[[01 courses/slides/Theory/TC-FT-RNLB-03 - Flottants IEEE 754|Slides RNLB-03]]"
exercices:
  - "[[01 courses/exercises/Theory/TC-FT-RNLB-03 - Flottants IEEE 754|Exos RNLB-03]]"
---
- [x] Créer situation d'imprecision flottante dans snippet de code
- [x] ajouter slide sur Nan, ce qu'il signifie, a quoi ca sert
- [x] mettre en coherence (choisir la mm valeur pour tous les slides)
	- [x] Lire un `float` en hexadécimal + Dans l'autre sens : −6,5 + Le vérifier en C++
- [x] Exercice 6 etre plus explicite sur la signification de tolerance relative et absolue
- [x] Partout est supposé comme évidente la conversion d'un nombre reel non entier décimal en reel "binaire"
      mais pour moi ce n'est pas l'evidence.
      
      Ca pose un probleme pour expliquer l'ecriture de la mantisse.
      est ce l'explication proposée par ce slide ? La même idée en binaire
      
      si oui, rentrer dans le détail (stopper le traitement et me solliciter uen foir arrivé a ce point)

## Traité le 28.09 — à vérifier

- **Imprécision** : nouvelle slide *L'imprécision en action : le chrono de partie* — un `float` qui additionne 1/60 pendant une heure affiche 3597.2068 au lieu de 3600 (sortie vérifiée, GCC 14). Explication et parades dans la note.
- **NaN** : nouvelle slide *NaN : ce que c'est, à quoi ça sert* (opération sans réponse, ne pas planter, valeur absente, `std::isnan`), avant *NaN contamine tout*.
- **Cohérence** : valeur unique **−6,5 = `0xC0D00000`** pour lire, coder et vérifier — bit de signe à 1 et exposant 129 (virgule déplacée de 2 rangs).
- **Schéma** ajouté : *−6,5 en mémoire* (`00 images/rnlb03_moins_6_5.svg`, script `tools/schemas/rnlb03_moins_6_5.py`) — normalisation, 32 bits colorés par champ, regroupement en hexadécimal.

> [!warning] Deck publié
> Le deck est en `publish: true` : ces changements partent en ligne au prochain push.
> Au passage : l'encadré de la note de séance annonce le **17.09**, alors que `date_scheduled` dit **30.09**.

## Retraité le 29.09

- **Exercice 6** : cadre *Deux façons de dire « assez proche »* — absolue = écart fixe `|a − b| ≤ 1e-6` ; relative = écart proportionnel `|a − b| ≤ 1e-5 × max(|a|, |b|)` (0,001 % du plus grand). Tableau de l'écart accepté à 0, 1, 1 000, 100 000 ; pourquoi l'une seule ne suffit pas ; étapes de la fonction. La consigne « justifier » devient « dire quelle tolérance accepte chaque paire ».
	- Résultats attendus (GCC 14) : `0.1f+0.2f / 0.3f` → vrai (absolue, écart 0) ; `1e-8f / 0` → vrai (absolue) ; `100000 / 100000.01` → vrai (relative, écart 0,0078) ; `1 / 1.1` → faux ; NaN / NaN → faux.
- **Décimal → binaire** : oui, *La même idée en binaire* était la seule explication (RNLB-01 ne traite que les entiers). Selon ta réponse : nouvelle slide schéma **avant** elle, *Après la virgule : des poids négatifs* — un octet `0110,1000₂` avec puissances 2³…2⁻⁴, poids 8…0,0625, « ÷2 » d'un rang à l'autre, total 4 + 2 + 0,5 = 6,5 (`00 images/rnlb03_poids_negatifs.svg`, script `tools/schemas/rnlb03_poids_negatifs.py`, + Excalidraw). Notes : conversion par retrait des poids, question 0,75, lien vers « 0,1 n'existe pas ». Pas de widget.
- *La même idée en binaire* : sa première ligne renvoie désormais au schéma.
- Au passage : la ligne `<small>` de *Le vérifier en C++* contenait `` `<bit>` `` — même piège que RNLB-02 dans l'éditeur Obsidian ; `<small>` retiré.
