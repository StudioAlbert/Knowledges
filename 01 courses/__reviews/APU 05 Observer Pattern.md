---
status: To check
manual_order: 3
parent:
  - "[[APU 04 APU 05 APU 09 deviennent]]"
slides:
  - "[[01 courses/slides/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|Slides APU-05]]"
exercices:
  - "[[01 courses/exercises/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|Exos APU-05]]"
---
- [x] Faire propositions dans cette note des différentes situations dans un jeu de voiture qui permettent d'utiliser le pattern; relier ces situations a une implementation parmi les 3 identifiées 

- Sources :
	- https://learn.unity.com/tutorial/create-modular-and-maintainable-code-with-the-observer-pattern
	- https://gist.github.com/adammyhre/353195d4870e8fd0cc0028659e66f208
	- https://www.unitydesignpatterns.com/patterns/observer
	- https://gameprogrammingpatterns.com/observer.html
	- https://refactoring.guru/design-patterns/observer
	- Scriptable Events : https://github.com/StudioAlbert/MallLifeStealthGame/tree/main/MallLife-UnityProject/Assets/03%20-%20Scripts/_Datas/Events

## Traité le 28.09 — à vérifier

- **Deck** réécrit : [[01 courses/slides/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven]] — *Observer, prévenir sans connaître*, 21 slides, `publish: false`.
	- Problème (branche `01-srp` : `PlayerHealth → HealthBar`), schéma avant / après, le pattern.
	- Trois façons : `event Action` (sujet, observateur), `UnityEvent`, canal en SO (schéma + `GenericEventChannelSO` et `AlertManager` de MallLife), tableau de choix.
	- Pièges : abonné fantôme (la lambda de `QuestManager`), `event` ou pas, traçabilité ; `Observable<T>` d'après le gist.
- **Atelier** rédigé ; pistes maison en overview.
- Sources : toutes lues sauf le dépôt MallLife en ligne (robots.txt) — lu en local dans `D:\_dev\repos\unity\MallLifeStealthGame`.
- **Refactoring.Guru** n'a pas pu être relu (lien conservé tel quel).

> [!warning] Renommer dans Obsidian
> Fichiers `… - ScriptableObjects — architecture data-driven.md` (lectures, slides, exercises) → `GPR-UN-APU-05 - Observer, prévenir sans connaître`.

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
