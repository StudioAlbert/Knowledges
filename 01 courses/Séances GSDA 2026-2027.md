---
title: Séances GSDA 2026-2027
type: index
---

# Séances GSDA 2026-2027

Une note par **heure de cours** attribuée à Sébastien Albert sur les modules 1 et 2 de
l'année académique 2026-2027, soit **69 séances**. Ce n'est pas un cursus : c'est la liste
de travail qui relie le planning du département au matériel de ce vault.

| | |
|---|---|
| Module 1 | 7 sept. → 13 nov. 2026 — **54 séances** |
| Module 2 | 23 nov. 2026 → 12 févr. 2027 — **15 séances** |
| Datées | 49 — les créneaux posés par Aurora, du 9 sept. au 26 nov. 2026 |

## Où elles vivent

Chaque séance est dans le `lectures/` de sa matière, **à côté du deck qu'elle découpe** :

| Dossier | Séances |
|---|---|
| `01 courses/lectures/C++` | 30 — `GPR-CF-*` |
| `01 courses/lectures/Theory` | 20 — `TC-FT-*` et `GPR-PE-CD-00` |
| `01 courses/lectures/Unity` | 19 — `GPR-UN-*` |

Le code dans le nom de fichier suffit à les distinguer d'un deck. Elles portent
`type: seance` et **aucun `duration_h`** : une séance d'1 h n'est pas un cours de 3 h et ne
doit pas entrer dans les totaux d'heures.

Leur `bloc_gsda` nomme le bloc du vault GSDA qu'elles découpent ; `source_gsda` pointe sur
le dépôt où ce bloc est tenu.

## Les dates viennent d'Aurora

**La référence de planification est Aurora**, https://aurora.eliasfarhan.ch — pas les
`date_scheduled` du vault GSDA, qui sont en retard. Ses leçons se lisent sur
`/api/lessons/?year=2026-2027&from=…&to=…` (ou, côté admin,
`/admin/schedule/lesson/?teacher__id__exact=4`) et portent exactement le `code` de ces
notes.

Une journée compte **quatre créneaux de 1 h 20** — 09:30, 11:10, 13:30, 15:10 — soit **1 h
de cours et 20 min d'échanges**. C'est pourquoi les notes restent des séances d'1 h avec
`estimate: 1h`, tandis que l'encadré du corps annonce l'horaire réel du créneau.

`date_scheduled` et l'encadré portent donc tous deux la date Aurora. Dernier alignement le
**2026-09-27** : les 49 leçons planifiées sont conformes sur les quatre champs (date,
horaire, salle, classes).

Les 20 notes sans créneau à moi :

- **planifiées, mais pour Elias Farhan** : `TC-FT-GVM-03` (30.09), `TC-FT-PS-00` (04.11),
  `GPR-CF-SDS-05` et `GPR-CF-SDS-06` (05.11) ;
- **pas encore planifiées** : `TC-FT-GVM-04`, `GPR-UN-APU-04` à `07`, `GPR-UN-VRG-07` à
  `14`, `GPR-UN-VRG-17` et `GPR-UN-VRG-18` ;
- **manquante dans Aurora** : `GPR-CF-SDS-04`. Le cours est bien à moi et garde sa date du
  14.10 — c'est la leçon qui manque au planning, pas la date à la note.

## Le nom d'une note

`<MINEURE>-<SPÉCIALISATION>-<BLOC>-<NN> - <Titre>.md` — par exemple
`GPR-CF-EDC-02 - Gestionnaires de paquets.md`.

Les quatre segments viennent du vault `_GSDA_Tech_Vault` et ne s'inventent pas : `code:` de
`Mineure/`, de `Spécialisations/`, de `Bloc/`, puis la colonne `Code` de la table `## Cours`
du bloc — **jamais le rang de la ligne**. Le Tronc Commun porte `TC-`, pas `GPR-`.

## Le kanban

Ces notes apparaissent dans `01 courses/__course base.base`, colonne **To prepare**,
réparties en deux couloirs par leur `projet`. Le champ `tache` dit la nature du travail :

| `tache` | Ce que ça veut dire | Nombre |
|---|---|---|
| `découper` | Un deck de 3 h existe et couvre plusieurs heures du lot : en extraire une tranche | 50 |
| `créer de zéro` | Rien d'exploitable — souvent un fichier qui **existe** mais ne fait que quelques centaines d'octets | 14 |
| `écrire depuis les livres` | Pas de deck : rédiger depuis les sections M3D / FGED1 citées | 3 |
| `découper + écrire` · `adapter + écrire` | Deux sources citées, une seule utilisable | 1 · 1 |

> [!warning] Un `duration_h` ne prouve pas qu'un support existe
> Six notes Unity annoncent 3 ou 6 h alors qu'elles sont vides ou à l'état de gabarit :
> `strategy_pattern` (314 o), `Entity Component System` (160 o), `shader_graph` (165 o),
> `lightning_rendering` (271 o), `lightning` (164 o), `feedbacks_juice` (1,3 ko). C'est ce
> qui fait passer 14 séances de « découper » à « créer de zéro ».

## Tenues à la main

Ces notes ont été générées une fois depuis `_GSDA_Tech_Vault`, puis le script a été
retiré : **elles n'ont plus de source automatique**. Ce qui y est écrit y reste, et ce qui
change dans le vault GSDA ne redescend plus tout seul — c'est à reporter à la main.

## Liens

- Programme : `_GSDA_Tech_Vault/Classes/GP-925.md` § 5-1 et 5-2, `GP-926.md` § 4-1 et 4-2
- Dates : Aurora, https://aurora.eliasfarhan.ch/calendar — puis, pour mémoire,
  `_GSDA_Tech_Vault/Plan/Créneaux fixes 2026-2027.md` et `Calendrier académique 2026-2027.md`
- Catalogue : `_GSDA_Tech_Vault/Bloc/`
