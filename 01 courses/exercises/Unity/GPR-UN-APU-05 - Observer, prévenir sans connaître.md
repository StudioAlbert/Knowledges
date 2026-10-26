# Exercices — GPR-UN-APU-05 — Observer, prévenir sans connaître

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-05 - Observer, prévenir sans connaître|GPR-UN-APU-05 - Observer, prévenir sans connaître]]

Terrain de jeu : le companion **[GPR-UN-APU-05 — Observer](https://github.com/StudioAlbert/GPR-UN-APU-05---Observer)**, un platformer où l'on ramasse cinq gemmes. Quand il n'en reste plus, un panneau s'affiche.

La branche `01-depart` en est la version **tout couplée** : `Item` appelle `ItemManager`, qui appelle lui-même l'étiquette et le panneau. Elle marche, et c'est bien le problème.

```bash
git clone https://github.com/StudioAlbert/GPR-UN-APU-05---Observer.git
cd GPR-UN-APU-05---Observer
git switch -c apu05-observer 01-depart
```

Ouvrez `Assets/01 - Scenes/Collecte.unity` et jouez une fois avant de toucher au code.

## Atelier — 20 min en classe

On démonte le couplage dans l'ordre, une technique par étape. **Le jeu doit marcher après chacune.**

### 1 — `Item` ne connaît plus personne

`Item` tient une référence à `ItemManager`. C'est le sens de dépendance qu'on inverse.

1. Dans `Item`, remplacer le champ `manager` par `public event Action<Item> Collected;`, et déclencher l'événement dans `OnTriggerEnter2D`.
2. Dans `ItemManager`, s'abonner à chaque item dans `OnEnable`, se désabonner dans `OnDisable` — **une méthode nommée**, pas une lambda.
3. Vérifier dans l'Inspector d'une gemme : plus aucune case à remplir.

> [!warning] L'ordre compte
> Le compte de départ se publie dans `Start`, pas dans `OnEnable` : à ce moment-là seulement, tout le monde s'est abonné.

### 2 — Le panneau de fin, sans une ligne de code

`ItemManager` connaît encore l'objet du panneau. Il n'a aucune raison de le connaître.

1. Remplacer le champ `panneauFin` par `[SerializeField] private UnityEvent allCollected;`, invoqué quand le compte tombe à zéro.
2. Dans l'Inspector, glisser le panneau dans la liste et choisir `GameObject.SetActive`, coché.
3. Supprimer le script du panneau s'il en restait un : il n'en faut aucun.

### 3 — Le son, sans ouvrir `Item` ni `ItemManager`

C'est l'étape qui compte. On ajoute un système entier **sans rouvrir** ce qui existe.

1. Écrire `EventChannelSO<T>` et `VoidEventChannelSO` (voir le cours), puis créer l'asset `GemmeRamassee` par *Create › Observer › Void Event Channel*.
2. `ItemManager` publie dessus à chaque ramassage.
3. Écrire `SoundManager` : il s'abonne au canal et joue `handleCoins.ogg`. Le poser sur un objet avec un `AudioSource`.

> [!check] Réussi si
> - `Item` ne cite aucune autre classe du jeu ;
> - `ItemManager` ne cite ni l'UI, ni l'audio, ni le panneau ;
> - vous avez ajouté le son **sans ouvrir** `Item.cs` ni `ItemManager.cs` ;
> - désactiver l'étiquette du compteur en jeu ne déclenche aucune erreur.

La branche `main` du companion est le corrigé.

---

## Pour aller plus loin — à la maison

### 4 — Le compteur sur le canal

L'étiquette lit encore le compte par un appel direct. La faire passer par un second canal, `GemmesRestantes`, en `IntEventChannelSO`. Deux observateurs sur deux canaux : constater que le sujet n'a pas changé d'une ligne.

### 5 — L'abonné fantôme

S'abonner avec une lambda dans `OnEnable`, tenter de se désabonner avec la même lambda dans `OnDisable`. Recharger la scène, lire l'erreur, corriger avec une méthode nommée. Expliquer en une phrase pourquoi le `-=` ne retirait rien.

### 6 — Sans le mot-clé `event`

Retirer `event` devant `Collected`, puis écrire dans un autre script la ligne qui efface tous les abonnés. Remettre `event` et lire l'erreur de compilation.

### 7 — Traçable

Ajouter au canal générique un mode verbeux, activable dans l'Inspector, qui journalise chaque annonce avec son émetteur et le nombre d'abonnés. Provoquer deux pannes — un abonné détruit qui écoute encore, une annonce qui en déclenche une autre en boucle — et montrer que le journal les trouve en moins d'une minute.

### 8 — Le même canal, dans un graphe

Installer `com.unity.behavior`, créer un canal d'événement depuis le Blackboard d'un graphe, et le faire écouter par un script C# — `canal.Event += …`. Comparer en trois lignes avec le canal écrit à l'étape 3.
