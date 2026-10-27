# Exercices — GPR-UN-APU-05 — Observer, prévenir sans connaître

> [!info] Terrain de jeu
> Le companion **[GPR-UN-APU-05 — Observer](https://github.com/StudioAlbert/GPR-UN-APU-05---Observer)** : un platformer pirate où l'on ramasse cinq gemmes, et quand il n'en reste plus un panneau s'affiche.
>
> Sa branche `01-depart` en est la version **tout couplée** : `Item` appelle `ItemManager`, qui écrit lui-même dans l'étiquette et allume le panneau. Elle marche, et c'est bien le problème.

## Atelier — 20 min en classe

On démonte le couplage dans l'ordre, une technique par étape. **Le jeu doit marcher après chacune.**

![[apu05_dependances.svg]]

### 1 — Prendre le terrain

```bash
git clone https://github.com/StudioAlbert/GPR-UN-APU-05---Observer.git
cd GPR-UN-APU-05---Observer
git switch -c apu05-observer 01-depart
```

Ouvrez `Assets/01 - Scenes/Collect.unity` et jouez une fois avant de toucher au code.

Repérez le bouton **Restart** du HUD : `ResetButton` appelle `ItemManager.ResetItems()`, directement, sans passer par rien. Il ne bougera pas de tout l'atelier — c'est le contre-exemple, gardez-le en tête.

### 2 — `Item` ne connaît plus personne

`Item` tient une référence à `ItemManager`. C'est le sens de dépendance qu'on inverse.

1. Dans `Item`, remplacer le champ `manager` par `public event Action<Item> Collected;`, et déclencher l'événement dans `OnTriggerEnter2D`.
2. Dans `ItemManager`, s'abonner à chaque item dans `OnEnable`, se désabonner dans `OnDisable` — **une méthode nommée**, pas une lambda.
3. Vérifier dans l'Inspector d'une gemme : plus aucune case à remplir.

### 3 — Le panneau de fin, sans une ligne de code

`ItemManager` connaît encore l'objet du panneau. Il n'a aucune raison de le connaître.

1. Remplacer le champ `endPanel` par `[SerializeField] private UnityEvent allCollected;`, invoqué quand le compte tombe à zéro.
2. Dans l'Inspector, glisser le panneau dans la liste et choisir `GameObject.SetActive`, coché.
3. Faire de même pour le retour en arrière : un second `UnityEvent reset`, décoché, invoqué par `ResetItems()`.
4. Supprimer le script du panneau s'il en restait un : il n'en faut aucun.

### 4 — Les canaux : on ouvre `ItemManager` une dernière fois

C'est l'étape qui compte.

1. Écrire `EventChannelSO<T>`, `IntEventChannelSO` et `VoidEventChannelSO` (voir le cours), puis créer les deux assets `GemCollected` et `GemsRemaining` par *Create › Observer › …*.
2. `ItemManager` publie dessus : le ramassage sur l'un, le compte restant sur l'autre. Il ne touche plus ni à l'UI, ni au son.
3. Écrire `CounterLabel` : il s'abonne à `GemsRemaining` et écrit dans le `Label` du HUD.
4. **Puis écrire `SoundManager` sans rouvrir un seul fichier existant** : il s'abonne à `GemCollected` et joue `handleCoins.ogg`, posé sur un objet avec un `AudioSource`.

> [!warning] L'ordre compte
> Le compte de départ se publie dans `Start`, pas dans `OnEnable` : à ce moment-là seulement, tout le monde s'est abonné.

> [!check] Réussi si
> - `Item` ne cite aucune autre classe du jeu ;
> - `ItemManager` ne cite ni l'UI, ni l'audio, ni le panneau ;
> - vous avez ajouté le son **sans ouvrir** `Item.cs` ni `ItemManager.cs` ;
> - désactiver le HUD en jeu ne déclenche aucune erreur ;
> - le bouton **Restart** marche toujours, et vous ne l'avez jamais touché.

La branche `main` du companion est le corrigé.
