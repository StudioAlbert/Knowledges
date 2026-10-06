---
status: Backlog
manual_order: 1
echeance: rentrée 2027-2028
slides:
  - "[[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|Slides APU-04]]"
  - "[[01 courses/slides/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|Slides APU-05]]"
  - "[[01 courses/slides/Unity/GPR-UN-APU-09 - Observer, State et composition|Slides APU-09]]"
exercices:
  - "[[01 courses/exercises/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|Exos APU-04]]"
  - "[[01 courses/exercises/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|Exos APU-05]]"
  - "[[01 courses/exercises/Unity/GPR-UN-APU-09 - Observer, State et composition|Exos APU-09]]"
---
# Révisions de programme à reporter — bloc *Architecture et Patterns Unity*

> [!info] Note de suivi, pas une tâche de cette année
> Les changements faits le 28.09.2026 sur APU-04, 05 et 09 s'écartent de la fiche du bloc
> dans `_GSDA_Tech_Vault`. Ils sont appliqués dans ce vault pour 2026-2027 ; ils sont à
> reporter dans le programme départemental (`_GSDA_Tech_Vault/Bloc/Architecture et Patterns Unity.md`)
> avant la planification 2027-2028. À traiter à ce moment-là — laisser en *To do* d'ici là.

## Ce qui change

| Ligne du bloc | Programme GSDA | Enseigné en 2026-2027 |
|---|---|---|
| `04` | ScriptableObjects — les données hors du code | ScriptableObjects, **tout le sujet** (données, variable partagée, Runtime Set, piège de l'état) |
| `05` | ScriptableObjects — architecture data-driven | **Observer** : `event Action`, `UnityEvent`, canal d'événement en SO |
| `09` | Observer, State et composition | **State** comme pattern de gameplay (tour par tour, UI, QTE) |

- **Retiré** : *composition plutôt qu'héritage* en `09`. Toujours couverte par `TC-FT-PCL-04 - Composition contre héritage` (Tronc commun).
- **Déplacé** : l'Observer passe de `09` à `05` ; les événements en ScriptableObject passent de `05` au sein de l'Observer.

## Points à trancher avant 2027-2028

- [ ] Renommer les intitulés des lignes `04`, `05`, `09` dans la fiche du bloc GSDA.
- [ ] **Classes** : `APU-05` est planifiée pour GP-926 (module 2), `APU-09` pour GP-925 (module 1). En 2026-2027, **GP-925 n'a donc pas d'Observer** et **GP-926 pas de State** — décider si les deux classes suivent les deux séances.
- [ ] **Ordre** : `APU-09` (State, 01.10) passe avant `APU-08` (Strategy, 15.10) pour GP-925 ; le deck State ne s'appuie pas sur Strategy, mais l'ordre du bloc devrait le refléter.
- [ ] Le deck SOLID (`APU-01`, GP-925) renvoie maintenant à APU-05 pour retirer le lien `PlayerHealth → HealthBar` : vrai seulement si GP-925 suit APU-05.
- [ ] Mettre à jour `Séances GSDA 2026-2027.md` si les intitulés changent côté GSDA.
