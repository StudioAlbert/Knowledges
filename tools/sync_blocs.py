#!/usr/bin/env python3
"""Synchronise les notes de bloc Unity depuis les notes de cours.

Chaque note de cours porte `bloc: "[[Nom du bloc]]"` et `duration_h`.
Ce script relit ces valeurs et, pour chaque note de `blocs/` :
  - recalcule `cours:` dans le frontmatter (= somme des duration_h) ;
  - regenere le tableau de la section `## Cours` entre les marqueurs
    <!-- cours:auto --> et <!-- /cours:auto -->.

Le frontmatter reste la source de verite lue par GSDA/Aurora : rien
ici ne depend d'un plugin Obsidian.

    python tools/sync_blocs.py            applique les mises a jour
    python tools/sync_blocs.py --check    n'ecrit rien, sort 1 si divergence
"""
import re
import sys
import pathlib
import collections

RACINE = pathlib.Path(__file__).resolve().parent.parent / "01 courses" / "Unity"
COURS = RACINE / "cours"
BLOCS = RACINE / "blocs"

DEBUT, FIN = "<!-- cours:auto -->", "<!-- /cours:auto -->"


def decoupe(texte):
    """Rend (frontmatter, corps) ou (None, texte) si pas de frontmatter."""
    if not texte.startswith("---\n"):
        return None, texte
    fin = texte.find("\n---\n", 3)
    if fin == -1:
        return None, texte
    return texte[4:fin + 1], texte[fin + 5:]


def champ(fm, nom):
    m = re.search(rf'^{nom}:\s*(.*?)\s*$', fm, re.M)
    return m.group(1) if m else None


def lire_cours():
    """Groupe les notes de cours par bloc, triees par chapter puis titre."""
    par_bloc = collections.defaultdict(list)
    orphelins, sans_duree = [], []
    for chemin in sorted(COURS.glob("*.md")):
        fm, _ = decoupe(chemin.read_text(encoding="utf-8"))
        if fm is None or champ(fm, "type") != "course":
            continue
        lien = champ(fm, "bloc") or ""
        m = re.search(r'\[\[(.+?)\]\]', lien)
        if not m:
            orphelins.append(chemin.stem)
            continue
        duree = champ(fm, "duration_h")
        duree = float(duree) if duree else None
        if duree is None:
            sans_duree.append(chemin.stem)
        titre = (champ(fm, "title") or chemin.stem).strip()
        par_bloc[m.group(1)].append(
            {"stem": chemin.stem, "titre": titre, "duree": duree}
        )
    for liste in par_bloc.values():
        liste.sort(key=lambda c: c["titre"])
    return par_bloc, orphelins, sans_duree


def tableau(cours):
    lignes = ["| # | Cours | Heures | Lien |", "| --- | --- | --- | --- |"]
    for i, c in enumerate(cours, 1):
        h = f"{c['duree']:g}" if c["duree"] is not None else "**?**"
        lignes.append(f"| {i} | {c['titre']} | {h} | [[{c['stem']}]] |")
    total = sum(c["duree"] for c in cours if c["duree"] is not None)
    inconnus = sum(1 for c in cours if c["duree"] is None)
    note = f" — {inconnus} cours sans `duration_h`" if inconnus else ""
    lignes.append("")
    lignes.append(f"**Total : {len(cours)} cours, {total:g} h{note}.**")
    return "\n".join(lignes)


def main():
    verif = "--check" in sys.argv
    par_bloc, orphelins, sans_duree = lire_cours()
    divergences, touches = [], []

    for chemin in sorted(BLOCS.glob("*.md")):
        texte = chemin.read_text(encoding="utf-8")
        fm, corps = decoupe(texte)
        if fm is None or champ(fm, "type") != "bloc":
            continue
        nom = chemin.stem
        cours = par_bloc.pop(nom, [])
        if not cours:
            divergences.append(f"{nom}: aucun cours rattache")
        total = sum(c["duree"] for c in cours if c["duree"] is not None)
        attendu = f"{total:g}"

        if champ(fm, "cours") != attendu:
            divergences.append(f"{nom}: cours={champ(fm, 'cours')} attendu {attendu}")
            fm = re.sub(r'^cours:.*$', f'cours: {attendu}', fm, count=1, flags=re.M)

        neuf = f"{DEBUT}\n{tableau(cours)}\n{FIN}"
        if DEBUT in corps:
            ancien = corps[corps.index(DEBUT):corps.index(FIN) + len(FIN)]
            if ancien != neuf:
                divergences.append(f"{nom}: tableau des cours desynchronise")
                corps = corps.replace(ancien, neuf)
        else:
            divergences.append(f"{nom}: marqueurs {DEBUT} absents")

        nouveau = "---\n" + fm + "---\n" + corps
        if nouveau != texte and not verif:
            chemin.write_text(nouveau, encoding="utf-8")
            touches.append(nom)

    for nom in par_bloc:
        divergences.append(f"bloc inexistant reference par des cours : {nom}")
    for stem in orphelins:
        divergences.append(f"cours sans bloc : {stem}")
    for stem in sans_duree:
        divergences.append(f"cours sans duration_h : {stem}")

    for ligne in divergences:
        print("  " + ligne)
    if verif:
        print(f"\n{len(divergences)} divergence(s)")
        return 1 if divergences else 0
    print(f"\n{len(touches)} note(s) de bloc mise(s) a jour : {', '.join(touches) or '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
