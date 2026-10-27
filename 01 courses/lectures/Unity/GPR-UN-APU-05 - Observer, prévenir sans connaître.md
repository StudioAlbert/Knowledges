---
title: Observer, prévenir sans connaître
type: seance
code: GPR-UN-APU-05
review:
  - "[[01 courses/__reviews/APU 05 Observer Pattern|Review APU-05]]"
status: Ready
projet: Module 2 — 23 nov. 2026 → 12 févr. 2027
subject: Unity
bloc_gsda: Architecture et Patterns Unity
specialisation: "[[Unity]]"
classes:
  - GP-926
manual_order: -1
estimate: 1h
tache: créer de zéro
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# Observer, prévenir sans connaître

> [!abstract] Séance d'1 h — `GPR-UN-APU-05` · bloc GSDA *Architecture et Patterns Unity*
> GP-926 · salle Arve · **non datée** (Module 2 — 23 nov. 2026 → 12 févr. 2027)

## À couvrir

Le pattern Observer : sujet, observateurs, abonnement ; `event Action`, `UnityEvent`, canal d'événement en `ScriptableObject` (Scriptable Events de MallLife) ; pièges : abonné fantôme, délégué public sans `event`, traçabilité ; valeur observable générique

> [!info] Révision du 28.09
> Cette séance portait la 2ᵉ heure de ScriptableObjects ; ils tiennent désormais en `GPR-UN-APU-04`, et l'Observer quitte `GPR-UN-APU-09` pour venir ici — voir `01 courses/__reviews/Programme 2027-2028 - APU.md`.

## Ce qu'il y a à faire

**Deck créé le 28.09**, **atelier monté puis repris le 27.10** sur son propre companion.

- **Deck** : [[01 courses/slides/Unity/GPR-UN-APU-05 - Observer, prévenir sans connaître|GPR-UN-APU-05 - Observer, prévenir sans connaître]] — 23 slides, 2 schémas générés (`tools/schemas/apu05_*.py`). Les deux dernières ajoutées : les canaux d'événement du **Behavior Graph**.
- **Exercices** : [[01 courses/exercises/Unity/GPR-UN-APU-05 - Observer, prévenir sans connaître|atelier]] — **quatre étapes en classe**, plus rien à la maison : la section *Pour aller plus loin* a été retirée, et le compteur sur canal est remonté dans l'atelier.
- **Companion** : [[01 courses/companion projects/Unity/GPR-UN-APU-05---Observer/README|GPR-UN-APU-05 — Observer]], sous-module. `01-depart` est la version couplée, `main` le corrigé. Platformer pirate (Treasure Hunters), interface en **UI Toolkit**, bouton *Restart* laissé couplé en contre-exemple.
- **Widget proposé, non fait** : `observer_bus_widget.html` — un sujet, un bus, quatre abonnés qui s'allument ; désabonner, détruire sans désabonner (abonné fantôme).
- **Reste de ton côté** : le schéma Excalidraw avant / après, à produire depuis ton compte et à embarquer dans la fiche exercices.

## Matériel

- Sources (révision) : [Unity Learn — observer pattern](https://learn.unity.com/tutorial/create-modular-and-maintainable-code-with-the-observer-pattern), [gist Observer<T> d'Adam Myhre](https://gist.github.com/adammyhre/353195d4870e8fd0cc0028659e66f208), [unitydesignpatterns.com](https://www.unitydesignpatterns.com/patterns/observer), [Game Programming Patterns](https://gameprogrammingpatterns.com/observer.html), [Refactoring.Guru](https://refactoring.guru/design-patterns/observer)
- Scriptable Events : `MallLifeStealthGame/MallLife-UnityProject/Assets/03 - Scripts/Core/Events/GenericEventChannelSO.cs`, assets dans `_Datas/Events`, abonné `Alarm/AlertManager.cs`
- Schémas : `00 images/apu05_couplage.svg`, `00 images/apu05_canal_so.svg`, `00 images/apu05_dependances.svg`
- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/Architecture et Patterns Unity.md`, ligne `05`

## Liens

- Séance précédente : [[GPR-UN-APU-04 - ScriptableObjects — les données hors du code]] (les canaux d'événement s'appuient sur les SO)
- Séance suivante : [[GPR-UN-APU-06 - Singleton en Unity]]

## Notes de préparation

> [!warning] Deux défauts relevés dans MallLife en préparant la séance
> - `QuestManager` : `OnEventRaised -= () => _viewQuestResolve.Show();` ne désabonne rien (nouvelle lambda) — repris tel quel comme exemple d'abonné fantôme.
> - `GenericEventChannelSO` : `OnEventRaised` est un délégué public sans `event` ; le deck montre la version avec `event`.
> - (hors sujet) `FactionQuestCollector.Collect` invoque `_onCollected` au lieu de `_onQuestComplete` quand la quête est terminée.
