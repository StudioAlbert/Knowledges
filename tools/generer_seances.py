#!/usr/bin/env python3
"""Génère les notes de préparation de séance dans `01 courses/GSDA 2026-2027/cours`.

Une note par heure de cours attribuée à Sébastien Albert sur les modules 1 et 2 de
l'année 2026-2027, nommée `<MINEURE>-<SPÉCIALISATION>-<BLOC>-<NN> - <Titre>.md`.

Tout ce qui est factuel est lu dans le vault `_GSDA_Tech_Vault` :

- `Mineure/*.md`, `Spécialisations/*.md`, `Bloc/*.md` → les `code:` du code hiérarchique
- la table `## Cours` de chaque bloc → titre, contenu, source
- `Sources/Seb2026/*.md` → `fichier:` donne le chemin du deck dans `_knowledges`
- `Courses/*.md` → `date_scheduled`, `manual_order`
- `Plan/Créneaux fixes 2026-2027.md` → les dates qui font autorité

Seul PROGRAMME est saisi à la main : les notes de `Classes/` décrivent le programme
par bloc et en prose (« cours 01, 08 et 09 »), pas ligne à ligne.

Usage :
    python tools/generer_seances.py --check    # n'écrit rien, liste les divergences
    python tools/generer_seances.py --apply    # crée ce qui manque, met à jour l'en-tête
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path

KNOWLEDGES = Path(__file__).resolve().parent.parent
GSDA = KNOWLEDGES.parent / "_GSDA_Tech_Vault"
DEST = KNOWLEDGES / "01 courses" / "GSDA 2026-2027" / "cours"

# Un support plus petit que cela est un squelette, pas un deck exploitable.
TAILLE_SQUELETTE = 1500

DEBUT, FIN = "<!-- seance:auto -->", "<!-- /seance:auto -->"

# --- Programme -------------------------------------------------------------
# Module 1 : Classes/GP-926.md § 4-1, GP-925.md § 5-1, WEB-925.md § 5-1, WEB-926.md § 4-1
# Module 2 : Classes/GP-925.md § 5-2, GP-926.md § 4-2
# (module, bloc GSDA, [(codes de cours, volées convoquées)])
G6W6 = ["GP-926", "WEB-926"]
PROGRAMME = [
    (1, "Environnement de Développement C++", [(["01", "02", "03"], G6W6)]),
    (1, "Git et Travail en Équipe", [(["01", "02"], G6W6),
                                     (["03"], ["GP-926", "WEB-926", "WEB-925"])]),
    (1, "Bases de la Programmation", [(["01", "02", "03", "04", "05", "06"], G6W6)]),
    (1, "Programmation Orientée Objet", [(["01", "02", "03", "04", "05", "06"], G6W6)]),
    (1, "Structures de Données et STL", [(["01", "02", "03", "04", "05", "06"], G6W6)]),
    (1, "SFML et Box2D", [(["01", "02", "03", "04", "05", "06"], ["GP-926"])]),
    (1, "Représentation des Nombres et Logique Binaire",
        [(["01", "02", "03", "04"], ["GP-926", "WEB-926", "WEB-925"])]),
    (1, "Trigonométrie", [(["01", "02", "03"], G6W6)]),
    (1, "Résolution d'Équation", [(["01", "02", "03"], ["GP-925", "WEB-926"])]),
    (1, "Géométrie Vectorielle et Matricielle", [(["01", "02", "05"], ["GP-925", "GP-926"]),
                                                 (["03", "04"], ["GP-925", "WEB-925"])]),
    (1, "Principes de Conception Logicielle", [(["01", "03", "04"], ["GP-926", "WEB-925"])]),
    (1, "Probabilités et Statistiques", [(["00"], ["GP-926", "GP-925", "WEB-926"])]),
    (1, "Cinématique et Dynamique", [(["00"], ["GP-926", "GP-925"])]),
    (1, "Architecture et Patterns Unity", [(["01", "08", "09"], ["GP-925"])]),
    (1, "VFX, Rendu et Game Feel", [(["15", "16"], ["GP-925"])]),
    (2, "VFX, Rendu et Game Feel",
        [(["07", "08", "09", "10", "11", "12", "13", "14", "17", "18"], ["GP-925"])]),
    (2, "Architecture et Patterns Unity", [(["04", "05", "06", "07"], ["GP-926"])]),
]

# Dates posées à la main par l'enseignant, le 06.09.2026, dans les notes
# `01 courses/Tools/cours/Git - *.md` absorbées ici. Le vault GSDA ne date pas le
# bloc GTE : sans cette table, ces trois heures repasseraient « non datées ».
DATES_MANUELLES = {
    "GTE-01": "2026-09-09",
    "GTE-02": "2026-09-09",
    "GTE-03": "2026-09-16",
}

MODULES = {
    1: "Module 1 — 7 sept. → 13 nov. 2026",
    2: "Module 2 — 23 nov. 2026 → 12 févr. 2027",
}

SUBJECT = {"CF": "C++", "FT": "Theory", "PE": "Theory", "UN": "Unity"}

# Bloc GSDA → note de `blocs/` dans _knowledges : les deux vaults ne les nomment pas pareil.
BLOC_LOCAL = {
    "Environnement de Développement C++": "Outillage et Environnement",
    "Git et Travail en Équipe": "Outillage et Environnement",
    "Bases de la Programmation": "Bases de la Programmation",
    "Programmation Orientée Objet": "Programmation Orientée Objet",
    "Structures de Données et STL": "Structures de Données",
    "SFML et Box2D": "Game Prog 101",
    "Représentation des Nombres et Logique Binaire":
        "Représentation des Nombres et Logique Binaire",
    "Trigonométrie": "Trigonometrie",
    "Résolution d'Équation": "Resolution d'equation",
    "Géométrie Vectorielle et Matricielle": "Géométrie Vectorielle et Matricielle",
    "Principes de Conception Logicielle": "Principes de Conception Logicielle",
    "Probabilités et Statistiques": "Statistiques, probabilités",
    "Cinématique et Dynamique": "Physique Newtonienne 101",
    "Architecture et Patterns Unity": "Architecture et Design Patterns",
    "VFX, Rendu et Game Feel": "VFX, Rendu et Game Feel",
}

# Une cellule de table peut contenir un « \| » échappé : ne couper que sur les autres.
# Un split("|") naïf décalerait toutes les colonnes suivantes.
ANTISLASH = chr(92)
_NI = "[^" + re.escape("]" + ANTISLASH + "|") + "]+"
CELLULE = re.compile("(?<!" + re.escape(ANTISLASH) + ")[|]")
LIEN_SEB = re.compile(re.escape("[[") + "Sources/Seb2026/(" + _NI + ")")
LIEN_LIVRE = re.compile(re.escape("[[") + "Sources/((?:M3D|FGED1)" + _NI + ")")
ALIAS = re.compile(re.escape("[[") + "Sources/" + _NI + re.escape(ANTISLASH) +
                   "[|]([^]]+)" + re.escape("]]"))
SLIDES = re.compile("https://docs[.]google[.]com/presentation/[^ )" + chr(34) + "]+")
SANS_ALIAS = re.compile(re.escape("[[") + "Sources/(" + _NI + ")" + re.escape("]]"))


def plie(texte):
    """Neutralise casse et accents, pour comparer deux graphies d'un même nom."""
    sans = unicodedata.normalize("NFD", texte)
    return "".join(c for c in sans if unicodedata.category(c) != "Mn").lower()


def lire(chemin):
    return chemin.read_text(encoding="utf-8")


def champ(texte, cle):
    m = re.search(r"^%s: (.+)$" % re.escape(cle), texte, re.M)
    return m.group(1).strip().strip('"') if m else ""


def entete(texte):
    """Rend (frontmatter, corps), ou (None, texte) si la note n'a pas d'en-tête."""
    if not texte.startswith("---\n"):
        return None, texte
    fin = texte.find("\n---\n", 4)
    if fin == -1:
        return None, texte
    return texte[4:fin + 1], texte[fin + 5:]


# --- Lecture du vault GSDA -------------------------------------------------

def codes_par_dossier(dossier):
    """{nom de note plié: code} pour Mineure/, Spécialisations/ ou Bloc/."""
    table = {}
    for f in sorted((GSDA / dossier).glob("*.md")):
        code = champ(lire(f), "code")
        if code:
            table[plie(f.stem)] = (f.stem, code)
    return table


def table_cours(texte_bloc):
    """Rend les lignes de la table `## Cours` d'un bloc, en dictionnaires."""
    if "## Cours" not in texte_bloc:
        return []
    section = texte_bloc.split("## Cours", 1)[1].split("\n## ")[0]
    lignes = []
    for ligne in section.splitlines():
        if not ligne.strip().startswith("|"):
            continue
        cellules = [c.strip() for c in CELLULE.split(ligne)[1:-1]]
        if len(cellules) < 6 or cellules[0] == "#" or set(cellules[0]) <= set("- :"):
            continue
        lignes.append(dict(zip(("rang", "code", "titre", "contenu", "source", "staff"),
                               cellules[:6])))
    return lignes


def index_sources():
    """{nom de note Sources/Seb2026: chemin relatif dans _knowledges}."""
    table = {}
    for f in sorted((GSDA / "Sources" / "Seb2026").glob("*.md")):
        fichier = champ(lire(f), "fichier")
        if fichier:
            table[f.stem] = fichier
    return table


def seances_datees():
    """{code cours GSDA (ex. BDP-01): (date, manual_order, salle)} depuis Courses/."""
    table = {}
    for f in sorted((GSDA / "Courses").glob("*.md")):
        texte = lire(f)
        code = champ(texte, "code")
        if not code:
            continue
        salle = champ(texte, "salle")
        table[code] = (champ(texte, "date_scheduled"),
                       champ(texte, "manual_order"),
                       salle.strip("[]"))
    return table


def creneaux_fixes(bloc_codes):
    """{code cours GSDA: date} depuis Plan/Créneaux fixes 2026-2027.md.

    Ces dates l'emportent sur celles de Courses/ : la note de créneaux est la
    décision du département, les notes de Courses/ en gardent une version périmée
    pour APU 08 et APU 09 (datées de janvier 2027 alors qu'elles sont en module 1).
    """
    fichier = GSDA / "Plan" / "Créneaux fixes 2026-2027.md"
    if not fichier.exists():
        return {}
    table = {}
    for ligne in lire(fichier).splitlines():
        if not ligne.strip().startswith("| 20"):
            continue
        cellules = [c.strip() for c in CELLULE.split(ligne)[1:-1]]
        if len(cellules) < 5:
            continue
        date = cellules[0]
        bloc = re.sub(r"\[\[(.+?)\]\]", r"\1", cellules[3]).strip()
        cours = cellules[4]
        code_bloc = bloc_codes.get(plie(bloc))
        if code_bloc and re.fullmatch(r"\d{2}", cours):
            table["%s-%s" % (code_bloc[1], cours)] = date
    return table


# --- Construction des séances ----------------------------------------------

def date_locale(prefixe, code_cours, titre):
    """`date_scheduled` déjà posée à la main dans la note de destination, s'il y en a une."""
    nom = "%s-%s - %s.md" % (prefixe, code_cours,
                             titre.replace("/", "-").replace(":", " -"))
    chemin = DEST / nom
    if not chemin.exists():
        return ""
    return champ(lire(chemin), "date_scheduled")


def collecte():
    mineures = codes_par_dossier("Mineure")
    specialisations = codes_par_dossier("Spécialisations")
    blocs = codes_par_dossier("Bloc")
    sources = index_sources()
    datees = seances_datees()
    fixes = creneaux_fixes(blocs)

    seances = []
    for module, nom_bloc, tranches in PROGRAMME:
        fichier_bloc = GSDA / "Bloc" / (nom_bloc + ".md")
        texte = lire(fichier_bloc)
        code_bloc = champ(texte, "code")
        spe = champ(texte, "specialisation").strip("[]")
        mineur = champ(texte, "mineur")
        code_spe = specialisations[plie(spe)][1]
        code_min = mineures[plie(mineur)][1]
        prefixe = "%s-%s-%s" % (code_min, code_spe, code_bloc)
        lignes = {l["code"]: l for l in table_cours(texte)}

        voulus = {}
        for codes, classes in tranches:
            for c in codes:
                voulus[c] = classes

        for code_cours, classes in sorted(voulus.items()):
            ligne = lignes.get(code_cours)
            if ligne is None:
                raise SystemExit("cours %s absent de Bloc/%s.md" % (code_cours, nom_bloc))
            cle = "%s-%s" % (code_bloc, code_cours)
            date, ordre, salle = datees.get(cle, ("", "", ""))
            if cle in DATES_MANUELLES:
                date = DATES_MANUELLES[cle]
            if cle in fixes:
                date = fixes[cle]           # les créneaux fixes l'emportent
            if not salle:
                # Définitions.md : la salle suit la volée, GP-926/WEB-926 → Arve, sinon Leman.
                salle = "Arve" if {"GP-926", "WEB-926"} & set(classes) else "Leman"
            if not date:
                # Le vault GSDA ne date pas tout. Une date posée à la main dans la note
                # locale fait foi tant que le département n'a rien arrêté.
                date = date_locale(prefixe, code_cours, ligne["titre"])

            supports = []
            for nom in LIEN_SEB.findall(ligne["source"]):
                rel = sources.get(nom)
                if rel:
                    chemin = KNOWLEDGES / rel
                    supports.append({"nom": nom, "rel": rel,
                                     "stem": Path(rel).stem,
                                     "taille": chemin.stat().st_size if chemin.exists() else 0,
                                     "existe": chemin.exists()})
            livres = LIEN_LIVRE.findall(ligne["source"])
            a_ecrire = bool(re.search(r"à écrire|à compléter", ligne["source"])) \
                or ligne["source"].strip() in ("—", "")

            seances.append({
                "module": module, "code": "%s-%s" % (prefixe, code_cours),
                "code_gsda": cle, "code_bloc": code_bloc, "code_spe": code_spe,
                "bloc": nom_bloc, "bloc_local": BLOC_LOCAL[nom_bloc], "spe": spe,
                "titre": ligne["titre"], "contenu": ligne["contenu"],
                "source_brute": ligne["source"], "supports": supports,
                "livres": livres, "a_ecrire": a_ecrire,
                "classes": classes, "salle": salle,
                "date": date, "ordre_gsda": ordre,
                "num": code_cours,
            })

    # Fan-out : combien de séances de ce lot partagent un même support ?
    partage = {}
    for s in seances:
        for sup in s["supports"]:
            partage.setdefault(sup["rel"], []).append(s["code"])
    for s in seances:
        s["partage"] = partage

    # manual_order recalculé sur l'ensemble : les datées d'abord, dans l'ordre du
    # calendrier, puis les autres groupées par bloc. Le kanban n'a pas d'autre tri.
    def tri(s):
        return (s["module"], s["date"] or "9999-99-99",
                int(s["ordre_gsda"]) if s["ordre_gsda"] else 999,
                s["code_bloc"], s["num"])
    seances.sort(key=tri)
    for i, s in enumerate(seances, 1):
        s["ordre"] = i
    return seances


def taille_lisible(octets):
    return "%s ko" % ("%.1f" % (octets / 1024)).replace(".", ",")


def classe(seance):
    """Rend (tache, consigne) — la nature du travail de préparation.

    La règle croise deux choses : ce que la colonne `Source` du bloc GSDA annonce,
    et l'état réel du fichier dans `_knowledges`. Six supports Unity portent un
    `duration_h` de 3 ou 6 h alors qu'ils ne font que quelques centaines d'octets :
    seule la taille sur disque dit s'il y a quelque chose à découper.
    """
    utiles = [s for s in seance["supports"] if s["taille"] >= TAILLE_SQUELETTE]
    squelettes = [s for s in seance["supports"] if s["taille"] < TAILLE_SQUELETTE]

    if utiles:
        principal = max(utiles, key=lambda s: s["taille"])
        freres = [c for c in seance["partage"][principal["rel"]] if c != seance["code"]]
        cite = ", ".join("`%s`" % f for f in freres)

        if squelettes and freres:
            return "découper + écrire", (
                "**Deux sources, une seule utilisable.** `%s` (%s) couvre une partie du "
                "contenu ci-dessus et porte %d heures de ce lot — les autres tranches vont "
                "à %s. `%s` ne fait que %d o : c'est un squelette, et ce qu'il devait "
                "apporter est à écrire. Prévoir les deux temps."
                % (principal["stem"], taille_lisible(principal["taille"]), len(freres) + 1,
                   cite, squelettes[0]["stem"], squelettes[0]["taille"]))

        if squelettes:
            return "adapter + écrire", (
                "**Deux sources, une seule utilisable.** `%s` (%s) couvre une partie du "
                "contenu ci-dessus, mais pas tout — c'est un support d'appoint, pas le "
                "cours. `%s` ne fait que %d o : c'est un squelette, et ce qu'il devait "
                "apporter est à écrire. Prévoir les deux temps."
                % (principal["stem"], taille_lisible(principal["taille"]),
                   squelettes[0]["stem"], squelettes[0]["taille"]))

        if freres:
            return "découper", (
                "**Découper un deck existant.** `%s` (%s) porte %d heures de ce lot : en "
                "extraire la tranche d'1 h correspondant au contenu ci-dessus. Les autres "
                "tranches vont à %s — les découper en une seule passe évite de rouvrir le "
                "deck %d fois."
                % (principal["stem"], taille_lisible(principal["taille"]), len(freres) + 1,
                   cite, len(freres) + 1))

        return "adapter", (
            "**Adapter un deck existant.** `%s` (%s) n'alimente que cette séance : le "
            "recadrer sur 1 h — le format GSDA prévoit 1 h de contenu, les 20 min "
            "restantes allant aux questions et aux exercices."
            % (principal["stem"], taille_lisible(principal["taille"])))

    if seance["livres"] and not seance["supports"]:
        return "écrire depuis les livres", (
            "**Écrire le support depuis les livres.** Aucun deck n'existe dans ce vault : "
            "la fiche GSDA renvoie aux sections listées plus bas, à rédiger en un deck d'1 h.")

    if squelettes:
        s0 = squelettes[0]
        return "créer de zéro", (
            "**Créer le support de zéro.** `%s` existe mais ne fait que %d o — c'est un "
            "squelette (un titre, parfois deux liens), pas un deck, malgré le `duration_h` "
            "qu'il annonce. Il n'y a rien à découper : tout est à écrire."
            % (s0["stem"], s0["taille"]))

    return "créer de zéro", (
        "**Créer le support de zéro.** La fiche GSDA porte « %s » en source : aucun "
        "matériel n'existe, ni dans ce vault ni dans les livres de référence."
        % (source_lisible(seance["source_brute"]) or "—"))


# --- Rendu de la note ------------------------------------------------------

def slides_origine(rel):
    chemin = KNOWLEDGES / rel
    if not chemin.exists():
        return ""
    texte = lire(chemin)
    depuis_entete = champ(texte, "source_slides")
    if depuis_entete:
        return depuis_entete
    # Les decks C++ citent la presentation d'origine dans leur corps, pas en entete.
    trouve = SLIDES.search(texte)
    return trouve.group(0) if trouve else ""


def exercices_cites(rel):
    chemin = KNOWLEDGES / rel
    if not chemin.exists():
        return []
    trouves = re.findall(r"\[\[(Exercices - [^\]|]+)", lire(chemin))
    return sorted(set(trouves))


def source_lisible(brute):
    """Rend la cellule Source du bloc GSDA en texte, alias des wikilinks conservés."""
    texte = ALIAS.sub(lambda m: m.group(1), brute)
    texte = SANS_ALIAS.sub(lambda m: m.group(1), texte)
    return texte.strip()


def rendre(seance, voisins):
    tache, consigne = classe(seance)
    quand = ("**%s**" % seance["date"]) if seance["date"] else "**non datée**"
    classes = " + ".join(seance["classes"])

    tete = ["---",
            "title: %s" % seance["titre"],
            "type: seance",
            "code: %s" % seance["code"],
            "status: To prepare",
            "projet: %s" % MODULES[seance["module"]],
            "subject: %s" % SUBJECT[seance["code_spe"]],
            'bloc: "[[%s]]"' % seance["bloc_local"],
            "bloc_gsda: %s" % seance["bloc"],
            'specialisation: "[[%s]]"' % seance["spe"],
            "classes: [%s]" % ", ".join(seance["classes"]),
            "salle: %s" % seance["salle"],
            "staff: Sébastien Albert"]
    if seance["date"]:
        tete.append("date_scheduled: %s" % seance["date"])
    tete += ["manual_order: %d" % seance["ordre"],
             "estimate: 1h",
             "tache: %s" % tache,
             'source_gsda: "_GSDA_Tech_Vault/Bloc/%s.md"' % seance["bloc"],
             "---"]

    corps = ["",
             DEBUT,
             "",
             "# %s" % seance["titre"],
             "",
             "> [!abstract] Séance d'1 h — `%s` · bloc GSDA *%s*" % (seance["code"], seance["bloc"]),
             "> %s · salle %s · %s (%s)" % (classes, seance["salle"], quand,
                                            MODULES[seance["module"]]),
             "",
             "## À couvrir",
             "",
             seance["contenu"],
             "",
             "## Ce qu'il y a à faire",
             "",
             consigne,
             "",
             "## Matériel",
             ""]

    if seance["supports"]:
        for sup in sorted(seance["supports"], key=lambda x: -x["taille"]):
            etat = ("squelette, %d o" % sup["taille"]) \
                if sup["taille"] < TAILLE_SQUELETTE else taille_lisible(sup["taille"])
            corps.append("- Support : [[%s]] — `%s` (%s)" % (sup["stem"], sup["rel"], etat))
            url = slides_origine(sup["rel"])
            if url:
                corps.append("    - Slides d'origine : %s" % url)
            for ex in exercices_cites(sup["rel"]):
                corps.append("    - Exercices : [[%s]]" % ex)
    else:
        corps.append("- Support : **aucun** dans ce vault.")

    if seance["livres"]:
        corps.append("- Références livres : %s" % source_lisible(seance["source_brute"]))
    corps += ["- Fiche du bloc : `_GSDA_Tech_Vault/Bloc/%s.md`, ligne `%s`"
              % (seance["bloc"], seance["num"]),
              "- Bloc local : [[%s]]" % seance["bloc_local"],
              "",
              "## Liens",
              ""]
    prec, suiv = voisins
    corps.append("- Séance précédente : %s" % ("[[%s]]" % prec if prec else "—"))
    corps.append("- Séance suivante : %s" % ("[[%s]]" % suiv if suiv else "—"))
    corps += ["", FIN, "", "## Notes de préparation", "", ""]
    return "\n".join(tete), "\n".join(corps)


def nom_fichier(seance):
    titre = seance["titre"].replace("/", "-").replace(":", " -")
    return "%s - %s.md" % (seance["code"], titre)


# --- Écriture --------------------------------------------------------------

def voisinage(seances):
    """{code: (nom du fichier précédent, suivant)} dans l'ordre du bloc."""
    par_bloc = {}
    for s in seances:
        par_bloc.setdefault(s["code_bloc"], []).append(s)
    table = {}
    for lot in par_bloc.values():
        lot.sort(key=lambda s: s["num"])
        for i, s in enumerate(lot):
            prec = Path(nom_fichier(lot[i - 1])).stem if i else None
            suiv = Path(nom_fichier(lot[i + 1])).stem if i + 1 < len(lot) else None
            table[s["code"]] = (prec, suiv)
    return table


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="écrit les notes")
    ap.add_argument("--check", action="store_true",
                    help="n'écrit rien, sort 1 s'il reste des divergences")
    args = ap.parse_args()
    if not (args.apply or args.check):
        ap.error("choisir --check ou --apply")

    seances = collecte()
    voisins = voisinage(seances)
    DEST.mkdir(parents=True, exist_ok=True)

    crees, majs, inchanges, attendus = [], [], [], set()
    for s in seances:
        chemin = DEST / nom_fichier(s)
        attendus.add(chemin.name)
        tete, corps = rendre(s, voisins[s["code"]])

        if chemin.exists():
            ancien = lire(chemin)
            _, corps_ancien = entete(ancien)
            if DEBUT in corps_ancien and FIN in corps_ancien:
                # Seule la zone entre marqueurs suit le vault GSDA. Ce que le
                # rédacteur écrit sous « Notes de préparation » lui appartient
                # et survit à une régénération.
                libre = corps_ancien.split(FIN, 1)[1]
                corps = corps.split(FIN, 1)[0] + FIN + libre
            elif corps_ancien.strip():
                corps = corps_ancien.rstrip() + chr(10)
            neuf = tete + chr(10) + corps
            if neuf == ancien:
                inchanges.append(chemin.name)
                continue
            majs.append(chemin.name)
        else:
            neuf = tete + chr(10) + corps
            crees.append(chemin.name)

        if args.apply:
            chemin.write_text(neuf, encoding="utf-8", newline="\n")

    orphelins = sorted(p.name for p in DEST.glob("*.md") if p.name not in attendus)

    print("séances au programme : %d  (module 1 : %d · module 2 : %d)"
          % (len(seances),
             sum(1 for s in seances if s["module"] == 1),
             sum(1 for s in seances if s["module"] == 2)))
    print("datées : %d · non datées : %d"
          % (sum(1 for s in seances if s["date"]),
             sum(1 for s in seances if not s["date"])))
    repartition = {}
    for s in seances:
        repartition[classe(s)[0]] = repartition.get(classe(s)[0], 0) + 1
    for tache, n in sorted(repartition.items(), key=lambda kv: -kv[1]):
        print("  %-24s %d" % (tache, n))
    verbe = "créées" if args.apply else "à créer"
    print("notes %s : %d · à mettre à jour : %d · inchangées : %d"
          % (verbe, len(crees), len(majs), len(inchanges)))
    for nom in crees[:5]:
        print("    + %s" % nom)
    if len(crees) > 5:
        print("    + … et %d autres" % (len(crees) - 5))
    for nom in majs[:10]:
        print("    ~ %s" % nom)
    if orphelins:
        print("fichiers hors programme dans le dossier :")
        for nom in orphelins:
            print("    ? %s" % nom)

    if args.check and (crees or majs or orphelins):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
