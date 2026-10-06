---
status: Ready
manual_order: -0.5
slides:
  - "[[01 courses/slides/Unity/GPR-UN-PCO-925 - Projet Commun|Slides PCO-925]]"
url_test: http://localhost:3000/unity/gpr-un-pco-925/
---
- [x] Basculer Fiches de ressources en slides
- [x] Garder une fiche de ressources compilant Overview / Prérequis + Asset pack
- [x] les éléments traités dans les slides doivent n'etre plus présentés dans la fiche de ressources
- [x] traiter les recommandations de l'encart ci dessous de maniére automatique

## Traité le 05.10 — à vérifier

- **Fiches → slides** : *Objectifs*, *Organisation - Echéances* et *Rôle* sont passées dans le deck `GPR-UN-PCO-925 - Projet Commun` (16 slides, 3 sections) : objectifs pédagogiques et techniques ; calendrier en schéma (`pco925_phases.svg`, S1 → S24, livraison 15.02.2027), prototypage, cycle V1 – V3, polish / fix / cut, point bi-hebdomadaire, bon play test ; tableau des rôles.
- **Une seule fiche de ressources** : `Overview` regroupe genre / gameplay et références (vides, comme avant), **prérequis** (version Unity, repo, Hack'n plan — repris d'*Organisation*) et **asset pack**.
- Liens d'asset pack réparés : `polygon-prototype-pack` sans domaine, `interface-fantasy-warrior-hud` fusionné avec un autre lien, `animation-sword-combat` en double.

> [!warning] À faire de ton côté
> - Supprimer `resources/Unity/925 - Projet Commun/Objectifs.md`, `Organisation - Echéances.md` et `Rôle.md` : tant qu'ils existent, ils restent publiés dans l'onglet Ressources (champ `seances`). Le `_Home.md` de `projects/Unity/925 - Projet Commun` pointe encore vers eux.
> - **Noms des élèves** : la fiche *Rôle* listait « Alex + Arthur + Thibault + Nathan » sans rôle associé ; je ne les ai pas mis dans un deck publié. La colonne *Qui* est à remplir.
> - **Polish** : la fiche disait S19 – S23 alors que la V3 finit en S19 ; le schéma le fait commencer en S20.
> - **Repo** : le prérequis pointe vers `GPR926---Unity-Projet-Commun` pour la promotion 925 — à confirmer.
> - `[[GDD]]` du 925 n'est qu'un gabarit vide issu de Confluence — à écrire ou à retirer.

## Traité le 05.10 — complément

**La fiche de ressources ne redit plus ce que disent les slides.** `Overview.md` est la seule
fiche restante : elle ouvre sur « Objectifs, calendrier, point bi-hebdomadaire et rôles :
voir les slides de la séance », et ne garde que genre / références, prérequis et asset packs.

**Les recommandations de l'encart, celles qui pouvaient se faire sans toi :**

- **Les trois fiches sont supprimées** — `Objectifs.md`, `Organisation - Echéances.md` et
  `Rôle.md`. Vérifié avant de les retirer : leur contenu est entièrement dans le deck
  (objectifs pédagogiques et techniques, les six phases, le point bi-hebdomadaire, le bon
  play test, le tableau des rôles). Elles ne polluent plus l'onglet *Ressources*.
- **`_Home.md` est recablé** : il pointe le deck et `Overview`, plus une ligne pour le GDD
  à créer. Un encadré dit où est parti le contenu des trois fiches.
- **`[[GDD]]`** disparait du deck, remplacé par « à créer pour cette promotion ».
- **Polish** : la contradiction S19 – S23 venait de la fiche Confluence, maintenant
  supprimée. La note du deck ne renvoie plus à une fiche qui n'existe pas : elle dit
  simplement que la V3 finit en S19 et que le polish commence en S20, comme le schéma.

> [!question] Ce qui reste et qui n'est qu'à toi
> - **Noms des élèves** : la colonne *Qui* du deck est toujours vide. « Alex + Arthur +
>   Thibault + Nathan » était la seule trace, sans rôle associé — et la fiche qui la portait
>   vient d'être supprimée. Elle est recopiée ici pour ne pas la perdre.
> - **Repo** : `Overview` pointe toujours
>   `SAE-Geneve/GPR926---Unity-Projet-Commun` pour la promotion **925**. Je ne l'ai pas
>   changé : si c'est une coquille, seul toi sais vers quel dépôt pointer.
> - **GDD 925** : à créer. Celui de 924 est dans
>   `01 courses/projects/Unity/924 - Projet Commun - Airport/GDD.md`.
