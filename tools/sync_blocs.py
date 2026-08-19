#!/usr/bin/env python3
"""Synchronise les notes de bloc depuis les notes de cours.

Chaque note de cours porte `bloc: "[[Nom du bloc]]"` et `duration_h`.
Ce script relit ces valeurs et, pour chaque note de `blocs/` :
  - recalcule `cours:` dans le frontmatter (= somme des duration_h) ;
  - regenere le tableau de la section `## Cours` entre les marqueurs
    <!-- cours:auto --> et <!-- /cours:auto -->.

Le frontmatter reste la source de verite lue par GSDA/Aurora : rien
ici ne depend d'un plugin Obsidian.

    python tools/sync_blocs.py            tous les cours
    python tools/sync_blocs.py "C++"      un seul cours
    python tools/sync_blocs.py --check    n'ecrit rien, sort 1 si divergence
"""
import re
import sys
import pathlib
import collections

CATALOGUE = pathlib.Path(__file__).resolve().parent.parent / "01 courses"
COURS_SUIVIS = ("Unity", "C++")

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


def lire_cours(COURS):
    """Groupe les notes de cours par bloc, triees par titre."""
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


def traiter(cours_nom, verif):
    """Synchronise un cours. Rend la liste de ses divergences."""
    racine = CATALOGUE / cours_nom
    COURS, BLOCS = racine / "cours", racine / "blocs"
    if not BLOCS.is_dir():
        return [f"{cours_nom}: dossier blocs/ absent"]
    par_bloc, orphelins, sans_duree = lire_cours(COURS)
    divergences, touches = [], []

    for chemin in sorted(BLOCS.glob("*.md")):
        texte = chemin.read_text(encoding="utf-8")
        fm, corps = decoupe(texte)
        if fm is None or champ(fm, "type") != "bloc":
            continue
        nom = chemin.stem
        if DEBUT not in corps:
            # tableau tenu a la main (schema GSDA) : on n'y touche pas, et on
            # ne recalcule pas `cours:` non plus, il compte des lignes ecrites
            # a la main et non des notes de cours.
            continue
        cours = par_bloc.pop(nom, [])
        if not cours:
            divergences.append(f"{nom}: aucun cours rattache")
        total = sum(c["duree"] for c in cours if c["duree"] is not None)
        attendu = f"{total:g}"

        if champ(fm, "cours") != attendu:
            divergences.append(f"{nom}: cours={champ(fm, 'cours')} attendu {attendu}")
            fm = re.sub(r'^cours:.*$', f'cours: {attendu}', fm, count=1, flags=re.M)

        # lignes vides obligatoires : sans elles Obsidian prolonge le bloc HTML
        # ouvert par le commentaire et avale le tableau au lieu de le rendre
        neuf = f"{DEBUT}\n\n{tableau(cours)}\n\n{FIN}"
        ancien = corps[corps.index(DEBUT):corps.index(FIN) + len(FIN)]
        if ancien != neuf:
            divergences.append(f"{nom}: tableau des cours desynchronise")
            corps = corps.replace(ancien, neuf)

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

    if not verif and touches:
        divergences.append(f"-> {len(touches)} note(s) reecrite(s)")
    return divergences


def main():
    verif = "--check" in sys.argv
    demandes = [a for a in sys.argv[1:] if not a.startswith("--")]

    total = 0
    for nom in demandes or list(COURS_SUIVIS):
        divergences = traiter(nom, verif)
        print(f"\n[{nom}]")
        for ligne in divergences:
            print("  " + ligne)
        if not divergences:
            print("  rien a signaler")
        total += sum(1 for d in divergences if not d.startswith("->"))

    print(f"\n{total} divergence(s)")
    return 1 if (verif and total) else 0


if __name__ == "__main__":
    sys.exit(main())
