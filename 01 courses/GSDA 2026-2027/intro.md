---
title: GSDA 2026-2027 — préparation des séances
type: index
---

# GSDA 2026-2027 — préparation des séances

Une note par **heure de cours** attribuée à Sébastien Albert sur les modules 1 et 2 de
l'année académique 2026-2027, soit **69 séances**. Ce dossier n'est pas un cursus : c'est
la liste de travail qui relie le planning du département au matériel de ce vault.

| | |
|---|---|
| Module 1 | 7 sept. → 13 nov. 2026 — **55 séances** |
| Module 2 | 23 nov. 2026 → 12 févr. 2027 — **14 séances** |
| Datées | 37 · les 32 autres attendent que le département pose leur créneau |

## Ce que ces notes ne sont pas

`cours/` contient ici des **séances d'1 h**, pas des decks. Les supports, eux, restent où
ils sont — `01 courses/C++/cours/`, `Unity/cours/`, `Theory/` — et gardent leur `duration_h`
de 3 h. Une séance porte `type: seance` et **aucun** `duration_h` : elle n'entre donc ni
dans `index_cours.base`, ni dans le total d'heures d'un bloc, ni dans `sync_blocs.py`.

## Le nom d'une note

`<MINEURE>-<SPÉCIALISATION>-<BLOC>-<NN> - <Titre>.md` — par exemple
`GPR-CF-EDC-02 - Gestionnaires de paquets.md`.

Les quatre segments viennent du vault `_GSDA_Tech_Vault` et ne s'inventent pas : `code:` de
`Mineure/`, de `Spécialisations/`, de `Bloc/`, puis la colonne `Code` de la table `## Cours`
du bloc — **jamais le rang de la ligne**. Le Tronc Commun porte `TC-`, pas `GPR-`.

## Le kanban

Ces notes apparaissent dans `01 courses/__course base.base`, colonne **To prepare**,
réparties en deux couloirs par leur `projet`. Le champ `tache` dit la nature du travail :

| `tache` | Ce que ça veut dire |
|---|---|
| `découper` | Un deck de 3 h existe et couvre plusieurs heures du lot : en extraire une tranche |
| `adapter` | Un deck existe et ne sert qu'à cette séance : le recadrer sur 1 h |
| `découper + écrire`, `adapter + écrire` | Deux sources citées, une seule utilisable |
| `écrire depuis les livres` | Pas de deck : rédiger depuis les sections M3D / FGED1 citées |
| `créer de zéro` | Rien d'exploitable — souvent un fichier qui **existe** mais ne fait que quelques centaines d'octets |

> [!warning] Un `duration_h` ne prouve pas qu'un support existe
> Six notes Unity annoncent 3 ou 6 h alors qu'elles sont vides ou à l'état de gabarit :
> `strategy_pattern` (314 o), `Entity Component System` (160 o), `shader_graph` (165 o),
> `lightning_rendering` (271 o), `lightning` (164 o), `feedbacks_juice` (1,3 ko). C'est ce
> qui fait passer 14 séances de « découper » à « créer de zéro ».

## Régénérer

```bash
python tools/generer_seances.py --check    # n'écrit rien, liste les divergences
python tools/generer_seances.py --apply    # crée ce qui manque, rafraîchit l'en-tête
```

Une note a deux zones. Entre `<!-- seance:auto -->` et `<!-- /seance:auto -->`, tout est
recalculé depuis `_GSDA_Tech_Vault` à chaque exécution — **ne rien y écrire à la main**.
Sous `## Notes de préparation`, la place est au rédacteur : le script n'y touche jamais.
Le frontmatter est régénéré, à une exception près : une `date_scheduled` posée à la main y
est relue et conservée tant que le département n'en a pas arrêté une.

## Liens

- Programme : `_GSDA_Tech_Vault/Classes/GP-925.md` § 5-1 et 5-2, `GP-926.md` § 4-1 et 4-2
- Dates : `_GSDA_Tech_Vault/Plan/Créneaux fixes 2026-2027.md`, `Calendrier académique 2026-2027.md`
- Catalogue : `_GSDA_Tech_Vault/Bloc/`
