---
parent:
  - "[[APU 04 APU 05 APU 09 deviennent]]"
slides:
  - "[[01 courses/slides/Unity/GPR-UN-APU-05 - Observer, prévenir sans connaître|Slides APU-05]]"
exercices:
  - "[[01 courses/exercises/Unity/GPR-UN-APU-05 - Observer, prévenir sans connaître|Exos APU-05]]"
---
- [x] Edit the map to setup with the Treasure Hunters set
- [x] Migrate UI to UI Toolkit using the Treasure Hunters UI assets
- [x] Add a Button to Reset Gemms : 
	- [x] Restore collected gemms (trough A public method on item manager)
	- [x] Reset the counter (through an event Reset)
- [x] Less platforms
- [ ] Edit a diagram in my excalidraw account with the before / after dependencies — **pour toi** : c'est ton compte, je n'y touche pas. Dis-moi si tu préfères un SVG généré par `tools/schemas/` à la place.
	- [ ] embed it in the exercice sheet
- [x] Supprimer la section Pour aller plus loin

- [x] Ajouter les events du Behaviour Graph dans les slides
- [x] Proposer Atelier
	- [x] Proposition
		- [x] le jeu est un platformer
		- [x] Assets 2D : https://pixelfrog-assets.itch.io/treasure-hunters — pack déposé par toi le 27.10, la scène et l'interface sont dessus.
		- [x] Assets audio : https://kenney.nl/assets/rpg-audio
		- [x] un personnage basique peut collecter des items
		- [x] Une fois collecté l'ensemble des items, on affiche un panneau Finish
	- [x] Montage / Implémentation
		- [x] Sound Manager
		- [x] Item to Item Manager : C# Action
		- [x] Item Manager : Unity Event
		- [x] Generalisation via Scriptable Events : ouverture aux autres systèmes
	- [x] Créer le jeu companion via Unity CLI, l'ajouter dans le Vaultcomm sub module (git url : https://github.com/StudioAlbert/GPR-UN-APU-05---Observer.git)
	- [x] Rédiger Fiche exercices en fonction
- [x]  Faire propositions dans cette note des différentes situations dans un jeu de voiture qui permettent d'utiliser le pattern; relier ces situations a une implementation parmi les 3 identifiées 

- Sources :
	- https://learn.unity.com/tutorial/create-modular-and-maintainable-code-with-the-observer-pattern
	- https://gist.github.com/adammyhre/353195d4870e8fd0cc0028659e66f208
	- https://www.unitydesignpatterns.com/patterns/observer
	- https://gameprogrammingpatterns.com/observer.html
	- https://refactoring.guru/design-patterns/observer
	- Scriptable Events : https://github.com/StudioAlbert/MallLifeStealthGame/tree/main/MallLife-UnityProject/Assets/03%20-%20Scripts/_Datas/Events

## Traité le 28.09 — à vérifier

- **Deck** réécrit : [[01 courses/slides/Unity/GPR-UN-APU-05 - Observer, prévenir sans connaître]] — *Observer, prévenir sans connaître*, 21 slides, `publish: false`.
	- Problème (branche `01-srp` : `PlayerHealth → HealthBar`), schéma avant / après, le pattern.
	- Trois façons : `event Action` (sujet, observateur), `UnityEvent`, canal en SO (schéma + `GenericEventChannelSO` et `AlertManager` de MallLife), tableau de choix.
	- Pièges : abonné fantôme (la lambda de `QuestManager`), `event` ou pas, traçabilité ; `Observable<T>` d'après le gist.
- **Atelier** rédigé ; pistes maison en overview.
- Sources : toutes lues sauf le dépôt MallLife en ligne (robots.txt) — lu en local dans `D:\_dev\repos\unity\MallLifeStealthGame`.
- **Refactoring.Guru** n'a pas pu être relu (lien conservé tel quel).

> [!done] Renommage terminé le 26.10
> Les trois fichiers portent le même nom : `GPR-UN-APU-05 - Observer, prévenir sans
> connaître.md` dans `lectures/`, `slides/` et `exercises/`. Tu avais renommé les deux
> premiers ; j'ai fait le troisième et repris les liens.
>
> **17 références, 4 cibles, aucun lien mort.** La table de
> [[Programme 2027-2028 - APU]] garde *ScriptableObjects — architecture data-driven* : ce
> n'est pas un lien, c'est le titre du programme GSDA, cité exprès en face de ce qu'on
> enseigne vraiment.

## Traité le 27.10 — l'atelier a son companion

**[GPR-UN-APU-05 — Observer](https://github.com/StudioAlbert/GPR-UN-APU-05---Observer)**, sous-module, Unity 6000.3.25f1 en URP 2D. Un platformer où l'on ramasse cinq gemmes ; quand il n'en reste plus, un panneau s'affiche.

Deux branches : `01-depart` est la version **tout couplée**, `main` le corrigé. Entre les deux, les trois mécanismes du cours, dans l'ordre où l'atelier les pose.

| Étape | Mécanisme | Ce qu'elle démontre |
|---|---|---|
| 1 | `event Action` | `Item` annonce au lieu d'appeler |
| 2 | `UnityEvent` | le panneau de fin, câblé dans l'Inspector, **sans un script** |
| 3 | canal en SO | le son s'ajoute **sans rouvrir** `Item.cs` ni `ItemManager.cs` |

La troisième étape est le critère de réussite : c'est la seule qui ne se démontre qu'en la faisant.

- **Vérifié dans l'éditeur**, sur les deux branches : les cinq gemmes se ramassent, le compteur descend, le panneau s'allume à zéro, zéro erreur console.
- **Deck** : deux slides ajoutées sur les canaux d'événement du **Behavior Graph** (`com.unity.behavior` 1.0.16) — les nœuds *Send / Start On / Wait for Event Message*, puis le pont C# `canal.Event += …`. L'argument : `EventChannelBase` dérive de `ScriptableObject`, donc Unity a retenu **exactement** l'architecture de la slide précédente.
- **Atelier** réécrit : trois étapes en classe, cinq pistes à la maison. Le Dungeon Crawler n'est plus le terrain de jeu — les slides qui y renvoyaient ont été repointées.
- Assets : deux packs **CC0** de Kenney, commités dans le dépôt comme pour le Dungeon Crawler.

> [!question] À trancher
> Le widget `observer_bus_widget.html` reste proposé et non fait. L'atelier le rend moins utile — ils voient désormais la chaîne tourner dans un vrai jeu.

## Traité le 27.10 (2) — Treasure Hunters, UI Toolkit, un bouton à contre-courant

Le pack de Pixel Frog est arrivé ; la scène et l'interface sont dessus, et l'atelier a changé
de forme.

- **Carte** : deux plateformes au lieu de quatre, terrain / capitaine / gemmes / décor en
  Treasure Hunters à **32 px par unité**. Les deux sprites de terrain et les deux cadres d'UI
  sont des **réassemblages 9-slice** du pack (`04 - Sprites`, `06 - UI`) : les tuiles de coin,
  de bord et de centre remises en une image 3×3, pour pouvoir les étirer.
- **Interface en UI Toolkit** : le Canvas uGUI et TextMeshPro laissent la place à deux
  `UIDocument`, le HUD et le panneau de fin. **Le panneau reste un GameObject à part** — c'est
  ce qui permet à `allCollected` de l'allumer par `SetActive`, donc sans une ligne de code. La
  démonstration de l'étape 3 tient toujours.
- **Bouton *Recommencer*** : `ResetButton` appelle `ItemManager.ResetItems()`, directement. La
  méthode rend les gemmes, referme le panneau par un second `UnityEvent` (`reset`) et republie
  le compte sur le canal — le compteur se remet à jour sans qu'on lui ait parlé. **Les deux
  façons de faire sur le même objet**, à trois lignes l'une de l'autre : le bouton appelle, le
  compteur écoute. C'est le meilleur support de discussion du TP.
- **Atelier à quatre étapes** : prise en main, `event Action`, `UnityEvent`, puis les canaux.
  Le compteur sur canal, qui était la piste maison n° 4, est remonté en classe — sans lui le
  corrigé n'était plus atteignable depuis l'énoncé.
- **Annotations de la fiche** traitées : la ligne « Cours associé » est retirée (le site a
  déjà ses onglets), le terrain de jeu passe en encart, le clone + lancement deviennent
  l'étape 1.
- **Vérifié en play mode sur les deux branches** : les cinq gemmes se ramassent, le compteur
  descend, le panneau s'allume à zéro, et un **vrai clic** sur *Recommencer* rend les gemmes
  et remet le compteur à cinq. Zéro erreur console.

> [!warning] Ce que la suppression de *Pour aller plus loin* emporte
> Quatre pistes maison disparaissent avec la section : l'**abonné fantôme**, le **délégué sans
> `event`**, le **canal traçable**, et le **canal dans un graphe `com.unity.behavior`**. Les
> deux premières restent couvertes par le deck (slides *Pièges*), la dernière par les deux
> slides du Behavior Graph. La **traçabilité** n'est plus nulle part — à décider si elle
> revient en slide ou si elle tombe pour cette année.

> [!question] Reste de ton côté
> Le schéma Excalidraw avant / après : c'est ton compte, je n'y touche pas. Si tu préfères, je
> le produis en SVG par un script de `tools/schemas/`, comme les deux autres figures de la
> séance — dis-moi.

## Propositions du 06.10 — Observer dans un jeu de voiture

Grille de tri, celle de la slide *Laquelle choisir ?* : **qui câble**, et **ce que
l'observateur doit connaître**. Un seul critère départage presque toujours — si l'émetteur et
le récepteur vivent dans le même prefab c'est `event Action` ; si c'est le level designer qui
décide au cas par cas c'est `UnityEvent` ; si ça traverse une scène ou relie deux systèmes qui
ne devraient pas se connaître, c'est le canal en SO.

### 1 · `event Action` — à l'intérieur d'une voiture

Même prefab, même durée de vie, câblage en code : l'observateur a une référence directe au
sujet, et ça ne pose aucun problème.

| Situation | Émetteur → observateurs |
|---|---|
| Le régime moteur franchit la zone rouge | `CarEngine.RedlineReached` → `Gearbox` passe le rapport, `DashboardNeedle` fait clignoter |
| Une roue perd l'adhérence | `Wheel.GripLost(float slip)` → `TractionControl` coupe les gaz, `SkidMarks` dessine, `TyreSmoke` émet |
| Un rapport est engagé | `Gearbox.GearChanged(int gear)` → `EngineSound` change de sample, `DashboardGear` affiche |
| Une pièce casse | `CarDamage.PartBroken(CarPart part)` → `CarPerformance` applique le malus, `DeformationMesh` déforme la tôle |

> Celui à montrer en cours : **la roue qui perd l'adhérence**. Trois observateurs d'un coup
> — physique, trace au sol, particules — et la démonstration tient en une phrase : on ajoute
> la fumée sans ouvrir `Wheel.cs`. C'est exactement le critère de réussite de l'atelier
> Dungeon Crawler, transposé.

### 2 · `UnityEvent` — ce que le level designer câble par piste

Même pièce de gameplay, réaction différente à chaque instance posée dans la scène : c'est
précisément ce que l'Inspector sert à régler, et ce qu'on ne veut surtout pas en dur.

| Situation | Ce que le LD branche dessus, selon l'instance |
|---|---|
| Une zone de déclenchement sur la piste | ouvrir une barrière, réveiller une foule, allumer un raccourci — différent à chaque virage |
| Un plot / une plaque de boost | VFX, son, secousse de caméra, parfois rien de plus |
| Un obstacle scripté (éboulement, train qui passe) | l'enchaînement d'objets de *cette* scène uniquement |
| La ligne d'arrivée, côté décor | feux d'artifice et banderoles propres à cette piste |

> Celui à montrer : **la zone de déclenchement**. On pose deux fois le même prefab et on
> branche deux réactions différentes, sans toucher au code — la démo dure trente secondes et
> fait comprendre la ligne « qui câble : l'Inspector » mieux qu'un paragraphe.

### 3 · Canal en ScriptableObject — entre systèmes et entre scènes

Les deux cas où rien d'autre ne marche : les objets ne coexistent pas dans la même scène, ou
ils appartiennent à des systèmes qui n'ont aucune raison de se connaître.

| Situation | Pourquoi le canal, et pas les deux autres |
|---|---|
| **Course terminée** (position, temps, meilleur tour) | l'écran de résultats, la sauvegarde, la musique et les succès écoutent ; plusieurs vivent dans une **autre scène** que la piste |
| **Impact** (force, point de contact) | audio, secousse de caméra, vibration de la manette, dégâts cosmétiques : quatre systèmes indépendants, aucun propriétaire commun |
| **Monnaie / voiture achetée** | émis depuis la scène *Garage*, écouté par le HUD et la sauvegarde |
| **Pause** | tout le jeu l'écoute : moteur, audio, UI, IA — le canal est le seul à ne pas créer un singleton |

> Celui à montrer : **course terminée**. Il justifie la ligne « entre deux scènes : oui » du
> tableau, qui est la seule chose que les deux autres implémentations ne savent pas faire.
> C'est aussi celui qui ressemble le plus au `GenericEventChannelSO` de MallLife déjà cité
> dans le deck.

### Le piège propre à la voiture

Une voiture est **instanciée au départ et détruite à l'arrivée**, et le canal en SO est un
asset qui, lui, survit. Un abonnement pris dans `Awake` sans `-=` dans `OnDisable` laisse un
abonné mort par course : au bout de trois courses, l'impact suivant déclenche quatre fois le
son. C'est l'abonné fantôme du deck, mais avec une cause que les étudiants rencontrent pour
de vrai — et un symptôme qui s'entend.

### Ce que j'en ferais

Trois situations suffisent, une par implémentation (roue / zone de déclenchement / course
terminée). Deux usages possibles, au choix :

- **une seule slide** après le tableau *Laquelle choisir ?*, trois lignes, qui ancre la règle
  dans un jeu que tout le monde se représente ;
- **un exercice maison** : on donne les douze situations du tableau ci-dessus en vrac, les
  étudiants les trient dans les trois colonnes et justifient en une ligne. Ça teste la règle
  de décision, pas la syntaxe — ce qui manque aux pistes 2 à 6 actuelles.

> [!question] À trancher
> Slide, exercice, les deux, ou rien pour cette année ? Le deck est à 21 slides, il a la
> place. Rien n'a été modifié dans le deck ni dans les exercices tant que ce n'est pas
> décidé — il reste en `publish: false`.
