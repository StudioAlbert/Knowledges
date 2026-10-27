---
title: Module 2 - Unity Beginner
type: index
subject: Unity
specialisation: "[[Unity]]"
classes:
  - GP-926
projet: Module 2 — 23 nov. 2026 → 12 févr. 2027
---

# Module 2 — Unity Beginner

Le cours Unity de la **1re année**, pour une volée sans aucun bagage : le module 1 est
entièrement C++, personne n'a encore ouvert l'éditeur ni écrit une ligne de C#. **26 lectures
d'1 h + 26 créneaux de pratique = 52 créneaux**, organisés autour des trois formatives
existantes posées en jalons.

> [!abstract] Le cadre
> **Période 2** — lun. 23 nov. 2026 → ven. 12 févr. 2027, summatives du 15–20 février.
> Cours le **jeudi et le vendredi, 4 créneaux de 1 h 20 par jour**.
> La semaine du 21 décembre n'a **ni jeudi ni vendredi enseignés** — la fermeture d'hiver
> commence le jeu. 24 déc. : il reste **9 semaines, soit 72 créneaux**. Les 20 créneaux non
> utilisés vont aux réunions et aux interventions externes.

## Objectifs

La lecture reste courte parce que la pratique a son propre créneau. Chaque formative n'exige
que ce qui vient d'être enseigné.

| Objectif | Validé par |
|---|---|
| **Poser** un projet Unity versionné et **implémenter** un véhicule jouable à deux périphériques différents, sans réécrire le code d'entrée | Jalon 1 — *Apply* |
| **Construire** un personnage en 3e personne qui vise et tire au raycast, animé par un Animator synchronisé sur l'état de gameplay, et **diagnostiquer** un cast qui ne touche rien | Jalon 2 — *Apply / Analyze* |
| **Concevoir** une boucle de jeu complète — tir, dégâts, mort, spawn, interface, son — et **justifier** le choix des mécaniques optionnelles | Jalon 3 — *Create / Evaluate* |

## Les blocs parcourus

| Code | Bloc | Séances | Nombre |
|---|---|---|---|
| `PMU` | Prise en Main d'Unity | 1 · 2 · 6 · 7 | 4 |
| `CSU` | **C# pour Unity** — bloc à créer | 4 · 5 · 26 | 3 |
| `SBL` | **Scènes, Build et Livraison** — bloc à créer | 3 | 1 |
| `CTD` | Contrôle et Déplacement | 8 · 9 · 10 · 11 | 4 |
| `PIU` | Physique et Interactions Unity | 12 · 13 · 14 · 23 | 4 |
| `CEA` | Caméra et Animation | 15 · 16 · 17 · 18 | 4 |
| `PGY` | Programmation Gameplay | 20 · 21 · 22 | 3 |
| `IUU` | Interface Utilisateur Unity | 19 · 24 | 2 |
| `VRG` | VFX, Rendu et Game Feel | 25 | 1 |

> [!warning] Deux blocs sont à créer au catalogue
> Rien dans `_GSDA_Tech_Vault/Bloc/` ne couvre le C#, le modèle d'exécution du moteur, le
> débogage ni la livraison d'un build — et le C# n'apparaît sur aucun des 116 cours de la
> spécialisation Unity. Détail et notification :
> `01 courses/__reviews/Nouveaux blocs Unity - CSU et SBL.md`.

## Les trois formatives

Reprises des briefs de `01 courses/projects/Unity/_archives_to_cut/`, reformulées en fiches
d'exercices. Chacune prend 2 créneaux en fin d'acte et se termine à la maison. Le calendrier
d'une formative, c'est la liste des séances qui la rendent faisable.

### Jalon 1 · Course en versus, à la Micromachines

Deux joueurs sur un écran, caméra fixe vue de dessus, un véhicule, un parcours.
**Valide** projet versionné, prefabs, déplacement physique, Input System multi-périphérique,
triggers. **Bonus** tours et classement, tir et power-ups.
**Séances** 2 · 5 · 6 · 7 · 8 · 9 · 10 · 11 · 12, plus 21 et 23 pour les bonus.

### Jalon 2 · Stand de tir en vue 3e personne

Abattre toutes les cibles de la zone avant la fin du chrono.
**Valide** raycast, Animator, personnage rigué, Cinemachine, HUD.
**Séances** 4 · 6 · 9 · 12 · 13 · 14 · 15 · 16 · 17 · 18 · 19.

### Jalon 3 · Shooter spatial isométrique 2.5D

Un vaisseau, deux armes — missile et laser —, vagues d'ennemis, santé, score, écran de fin,
sons. **Valide** coroutines, les trois familles de tir, dégâts et mort, spawn, menu et HUD,
audio. **Bonus** power-ups, obstacles, juice.
**Séances** 2 · 3 · 6 · 8 · 9 · 12 · 14 · 18 · 19 · 20 · 21 · 22 · 23 · 24 · 25.

## Calendrier

Quatre créneaux par jour : **09:30 · 11:10 · 13:30 · 15:10**. Les cases vides vont aux
réunions et aux interventions externes.

| Sem. | Jour | 09:30 | 11:10 | 13:30 | 15:10 |
|---|---|---|---|---|---|
| 1 | jeu. 26 nov. | **1** Moteur et éditeur | *Workshop 1* | **2** Structure d'un projet | **3** Scènes et build |
| 1 | ven. 27 nov. | *Workshop 2–3* | — | — | — |
| 2 | jeu. 3 déc. | **4** Cycle de vie MonoBehaviour | **5** Déboguer dans Unity | *Workshop 4–5* | **6** Prefabs et spawn |
| 2 | ven. 4 déc. | *Workshop 6* | — | — | — |
| 3 | jeu. 10 déc. | **7** Dépôt Git pour Unity | *Workshop 7* | **8** Déplacement par Transform | *Workshop 8* |
| 3 | ven. 11 déc. | **9** Rigidbody et colliders | *Workshop 9* | — | — |
| 4 | jeu. 17 déc. | **10** New Input System | *Workshop 10* | **11** Deux joueurs sur un écran | *Workshop accompagné 11* |
| 4 | ven. 18 déc. | **12** Triggers et collisions | *Workshop 12* | **J1** Course en versus | **J1** Course en versus |
| — | *sem. du 21 déc.* | *fermeture d'hiver dès le jeu. 24 déc. — aucun jour enseigné* | | | |
| 5 | jeu. 14 janv. | **13** Le rayon | *Workshop 13* | **14** Raycast et volumes | **15** Clips et interpolation |
| 5 | ven. 15 janv. | *Workshop 14–15* | — | — | — |
| 6 | jeu. 21 janv. | **16** Animator | *Workshop 16* | **17** Rig et IK | **18** Cinemachine |
| 6 | ven. 22 janv. | *Workshop 17–18* | — | — | — |
| 7 | jeu. 28 janv. | **19** HUD en uGUI | *Workshop 19* | **J2** Stand de tir TPS | **J2** Stand de tir TPS |
| 7 | ven. 29 janv. | — | — | — | — |
| 8 | jeu. 4 févr. | **20** Coroutines | *Workshop 20* | **21** Tirer | *Workshop 21* |
| 8 | ven. 5 févr. | **22** Dégâts et mort | **23** Ramasser et porter | *Workshop 22–23* | — |
| 9 | jeu. 11 févr. | **24** Menu en UI Toolkit | *Workshop 24* | **25** Le son | *Workshop 25* |
| 9 | ven. 12 févr. | **26** Les spécificités du C# | **J3** Shooter isométrique | **J3** Shooter isométrique | — |

Les créneaux de pratique suivent leur lecture, **deux consécutifs au maximum**. Six séances —
**2 · 4 · 14 · 17 · 22 · 26** — partagent le workshop de leur voisine : ce sont les six
créneaux rendus aux trois formatives.

## Hors périmètre

`APU` en entier (architecture et patterns, 2e année) · `VRG-07→18` (juice, rendu, shaders,
éclairage, particules, donné à la 2e année ce même module) · `IUU-03→06` (les cas d'usage
Tower Defense) · `CEA-06` et `CEA-09` · `IAU` (NavMesh et IA) · `J2D` · `UEC` · `GPC` ·
profiling. **Reporté au module 3** : la montée en difficulté et le budget d'entités
simultanées (`PGY-09`).

## Liens

- Plan de travail détaillé, companion, widgets et schémas : voir le plan de session
- Notification des deux blocs : `01 courses/__reviews/Nouveaux blocs Unity - CSU et SBL.md`
- Séances de l'année : [[01 courses/Séances GSDA 2026-2027|Séances GSDA 2026-2027]]
- Calendrier qui fait autorité : `_GSDA_Tech_Vault/Calendrier académique 2026-2027.md`
- Programme de la volée : `_GSDA_Tech_Vault/Classes/GP-926.md` § 4-2
