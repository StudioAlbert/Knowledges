---
slides: "[[01 courses/slides/C++/GPR-CF-POO-03 - Découpage en fichiers]]"
---
- [x] Prendre en compte les modifications du companion
	- [x] -> supprimer exercices
	- [x] Corriger Notes ressources
	- [x] Supprimer Ateliers
- [x] Schéma pour expliquer l'enjeu de la forward declaration, c'est à dire la connaissance reciproque des objets

## Traité le 12.10 — à vérifier

**Le companion ne garde que la déclaration anticipée.** `01_donjon_monolithe` est retiré ;
l'étape qui reste est renumérotée **`01_forward_declaration`** — un dossier `02_` seul, sans
`01_`, se lit comme un oubli. Reconfiguré et recompilé au MSVC : la target sort et tourne.

> [!bug] Le commentaire d'`arme.h` était faux
> Il disait « décommenter l'include pour voir l'erreur ». L'annonce `class Joueur;` restant
> en place, le projet **compilait quand même** : la garde suffisait. Il faut commenter l'une
> **et** décommenter l'autre. Vérifié au compilateur, et le message obtenu est maintenant
> dans le README comme dans la fiche :
> `arme.h(18): error C2143: erreur de syntaxe: absence de ';' avant '*'`

**Feuille d'exercices supprimée.** `exercises/C++/GPR-CF-POO-03 - Découpage en fichiers.md`
(six exercices assis sur le donjon) disparaît avec lui. Le site ne rattache donc plus
d'exercice à POO-03 — le build le signale, comme pour EDC-01 à 03, GTE-01 et TRG-02/03.

**Fiche ressources réécrite et renommée** : *Projet companion Le donjon* →
*Projet companion Déclaration anticipée*. Elle dit comment voir le problème, puis les deux
façons de se convaincre que l'annonce ne suffit qu'à un pointeur — l'attribut par valeur et
l'appel de méthode. Aucune note ne pointait l'ancien titre, et le rattachement au site passe
par le préfixe du nom de fichier : rien à recâbler.

**Deck.** La slide *Atelier — 20 min* est retirée : elle renvoyait aux exercices 1, 2 et 5 de
la feuille. La slide *Forward declaration* est retournée pour coller au companion — c'est
`Arme` qui annonce `Joueur`, pas l'inverse — et suivie du schéma. 22 slides, inchangé.

**Schéma** `poo03_connaissance_reciproque.svg` : à gauche l'inclusion croisée et son verdict,
à droite l'annonce. Format très large et court (1000 x 330), calé sur ce que le cadre laisse
à une figure sous un titre et une ligne de légende — mesuré à 978 x 323 sur la slide, soit le
texte aussi gros que le cadre le permet.

## Deux points à trancher

- **`.cpp` dans le deck, `.cc` dans le companion.** Le deck écrit `Joueur.cpp` partout, le
  companion suit la skill `programmation-cpp` (Google : `.h` / `.cc`). Les deux se tiennent,
  mais l'étudiant voit les deux le même jour. Hors périmètre de cette révision — à décider.
- ~~Le deck est en `publish: draft`~~ — **repassé en `online` le 12.10**, révision validée.
  Vérifié par un build de production : 29 séances actives, POO-03 dedans, aucun brouillon.
