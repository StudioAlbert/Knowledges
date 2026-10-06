# -*- coding: utf-8 -*-
"""Schéma POO-03 — une inclusion est un copier-coller.

Trois fichiers à gauche, l'unique fichier que le préprocesseur fabrique à droite.
Chaque bloc garde la couleur de son fichier d'origine, et les numéros donnent l'ordre
de recopie.

  00 images/poo03_unite_compilation.svg
  Excalidraw/POO-03 - Unite de compilation.excalidraw.md

    python "tools/schemas/poo03_unite_compilation.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

BLEU, VERT = "#2b6cb0", "#2e9e5b"

fig = Figure(1160, 440)

FICHIERS = [
    ("main.cpp", RED, 60, [
        ('#include "Joueur.h"', True),
        ("int main()", False),
        ("{ Joueur j; }", False),
    ]),
    ("Joueur.h", VERT, 180, [
        ('#include "Vector2.h"', True),
        ("class Joueur", False),
        ("{ Vector2 pos_; };", False),
    ]),
    ("Vector2.h", BLEU, 300, [
        ("struct Vector2", False),
        ("{ float x, y; };", False),
    ]),
]

fig.text(205, 34, "CE QUE VOUS ÉCRIVEZ", size=13, weight=800, color=GREY)

ancres = {}
for nom, couleur, y, lignes in FICHIERS:
    h = 36 + len(lignes) * 22 + 12
    fig.rect(40, y, 330, h, stroke=couleur, fill="#ffffff", width=2.5, radius=10)
    fig.rect(40, y, 330, 30, stroke=couleur, fill=couleur, width=2.5, radius=10)
    fig.text(56, y + 21, nom, anchor="start", size=15, weight=800, color="#ffffff",
             mono=True, halo=False)
    for i, (txt, inclusion) in enumerate(lignes):
        if not txt:
            continue
        fig.text(60, y + 52 + i * 22, txt, anchor="start", size=13.5, weight=700 if inclusion else 600,
                 color=couleur if inclusion else SOFT, mono=True, halo=False)
    ancres[nom] = (y, h)

# ------------------------------------------- a droite : l'unite de compilation
X, Y, W = 700, 52, 420
fig.text(X + W / 2, 34, "CE QUE VOIT LE COMPILATEUR", size=13, weight=800, color=GREY)
fig.rect(X, Y, W, 338, stroke=INK, fill=PALE, width=3, radius=12)
fig.text(X + W / 2, Y + 26, "une seule unité de compilation", size=14, weight=800, color=INK)

BLOCS = [
    ("Vector2.h", BLEU, ["struct Vector2", "{ float x, y; };"], 48),
    ("Joueur.h", VERT, ["class Joueur", "{ Vector2 pos_; };"], 152),
    ("main.cpp", RED, ["int main()", "{ Joueur j; }"], 256),
]
for ordre, (src, couleur, lignes, dy) in enumerate(BLOCS, start=1):
    y = Y + dy
    h = 24 + len(lignes) * 24
    fig.rect(X + 24, y, W - 48, h, stroke=couleur, fill="#ffffff", width=2, radius=8)
    fig.line([(X + 24, y + 6), (X + 24, y + h - 6)], couleur, 6)
    for i, t in enumerate(lignes):
        fig.text(X + 46, y + 28 + i * 24, t, anchor="start", size=14, weight=700,
                 color=INK, mono=True, halo=False)
    fig.text(X + W - 44, y - 8, "recopié de " + src, anchor="end", size=11.5,
             weight=700, color=couleur)
    # la pastille d'ordre
    fig.dot(X + 8, y + h / 2, 13, couleur)
    fig.text(X + 8, y + h / 2 + 5, str(ordre), size=14, weight=800, color="#ffffff", halo=False)

# ------------------------------------------- les fleches de recopie
for nom, dest in (("Vector2.h", 0), ("Joueur.h", 1), ("main.cpp", 2)):
    y0, h0 = ancres[nom]
    couleur = dict((f[0], f[1]) for f in FICHIERS)[nom]
    y1 = Y + BLOCS[dest][3] + (24 + len(BLOCS[dest][2]) * 24) / 2
    fig.line([(376, y0 + h0 / 2), (520, y0 + h0 / 2), (520, y1), (X - 22, y1)],
             couleur, 2.2, arrow=True, dash=True)

fig.text(580, 424, "L'ordre vient des inclusions : le plus profond est recopié en premier. "
                   "Un en-tête lu deux fois déclare deux fois — d'où les gardes.",
         size=13, weight=700, color=INK)

fig.save("poo03_unite_compilation", "POO-03 - Unite de compilation")
