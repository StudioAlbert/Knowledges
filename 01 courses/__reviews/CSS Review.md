---
status: To do
manual_order: 1
url_test: http://localhost:60720/
---
> [!tip] Revisiter l'ensemble des slides

- [ ] Fleches de défilement en blanc sur tous les slides
- [x] Execption pour les slides Titre (contenu centré)
![[{5637A15E-82B6-45C6-84AF-4E1CB2B91556}.png]]
![[{7F99BE4A-6ED3-4B90-9FD8-51474B0A11F2}.png]]


- [x] Les titres sont tres hauts, baisser un peu
	- [x] centrer le contenu dans l'espace restant
![[Pasted image 20261006134032.png]]
- [x] Fleches de défilement en blanc

## Traité le 06.10 — à vérifier

> [!bug] Ce que la capture m'a appris
> Ma règle d'hier ne faisait pas ce que j'ai écrit. **reveal pose `display: block` en
> ligne** sur la slide courante, et un style en ligne bat une feuille de style : mon
> `display: flex` n'a jamais pris. Le contenu n'était donc pas centré dans le cadre, il
> était **aligné en haut** — exactement ce que montrait ta capture de *Smoother step*.
> Corrigé avec un `!important`, qui est ici nécessaire et non cosmétique.

**1. Exception pour les slides de titre.** Leur fond est une photo avec le logo en haut au
centre : le cadre des slides de contenu n'y a pas cours, et mon padding de 104 px poussait
le titre dans le logo. Elles sont désormais **exclues** de la règle (`:not(.title)`) et
reprennent le centrage vertical de reveal sur toute la hauteur, comme avant. Vérifié sur
une slide d'ouverture de deck **et** sur une slide de section en cours de deck.

**2. Titre baissé, contenu centré dans ce qui reste.**

- le padding haut passe de **104 → 124 px** : le titre respire sous la bande noire ;
- le titre reste en haut, et **tout ce qui le suit se centre dans la hauteur restante**,
  au lieu de s'empiler juste dessous en laissant le bas vide. Les marges `auto` d'un
  conteneur flex s'en chargent, sans conteneur supplémentaire dans le Markdown.
- Mesuré sur *Smoother step* : titre à 124–183, contenu de 310 à 515 — centré entre le
  titre et le bas du cadre.

**3. Flèches de défilement en blanc.** reveal les pose en bas à droite, donc sur la bande
noire, et les dessinait en noir. `.reveal .controls { color: blanc }`, plus un rouge SAE au
survol.

**Audit rejoué** sur les **715 slides des 29 decks**, cette fois avec la vraie mise en page
(flex actif). Une seule débordait encore — APU-01, *Les interfaces dans Unity* : deux
puces, un tableau et dix lignes de code sur la même slide. Le code a pris sa propre slide
(*La classe abstraite, en pratique*). **0 slide hors cadre.**
