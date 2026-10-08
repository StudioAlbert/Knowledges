---
seances: [GPR-UN-APU-09]
---
# Projet companion : la machine à états

Quatre démos techniques d'une **même machine à états générique**. Ce ne sont pas des jeux :
des primitives, un panneau de debug qui affiche l'état courant, et rien de plus, pour que le
code de la machine reste lisible. Unity 6000.3.25f1, URP, Input System.

```github
StudioAlbert/GPR_UN_APU_09_StateMachine
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

Les scènes de `Assets/01 - Scenes/` s'ouvrent dans l'ordre : *Hero*, *Guard*, *QTE*,
*TurnBased*. La machine elle-même tient dans `Assets/03 - Scripts/Core/` — `IState` avec
`OnEnter` / `OnExit` / `Tick`, et les transitions **déclarées à côté du graphe** plutôt
qu'écrites dans les états.

Deux pièges à connaître avant de lire les démos : les transitions sont indexées par
`GetType()`, donc **deux états de la même classe partagent leurs transitions** ; et `Tick`
prend **la première** condition vraie, les « any » d'abord — l'ordre de déclaration est
l'ordre de priorité.
