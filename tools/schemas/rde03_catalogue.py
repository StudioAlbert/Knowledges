# -*- coding: utf-8 -*-
"""Schéma RDE-03 — le catalogue des formes.

Six courbes côte à côte, chacune avec sa formule et ce qu'elle sert à régler
dans un jeu. Le but n'est pas de les étudier, c'est de les **reconnaître** : à
quoi ressemble une racine, à quoi ressemble un logarithme.

  00 images/rde03_catalogue.svg
  Excalidraw/RDE-03 - Catalogue des formes.excalidraw.md

    python "tools/schemas/rde03_catalogue.py"
"""
import math

from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1020, 330)

CW, CH = 158, 128          # la boîte d'un tracé
Y0 = 72                    # le haut des tracés
MARGE = 10

COURBES = [
    ("y = ax + b", lambda t: t, "une pente constante"),
    ("y = ax²", lambda t: t * t, "accélérer, freiner"),
    ("y = √x", lambda t: math.sqrt(t), "monte vite, puis mollit"),
    ("y = 2^x", lambda t: (2 ** (3 * t) - 1) / 7, "l'XP d'un niveau"),
    ("y = log x", lambda t: math.log(1 + 7 * t) / math.log(8), "le volume en dB"),
    ("y = |x|", lambda t: abs(2 * t - 1), "un écart, sans signe"),
]

fig.text(20, 36, "SIX FORMES À RECONNAÎTRE — l'allure suffit, le calcul vient après",
         anchor="start", size=14, weight=800, color=GREY)

for i, (formule, f, usage) in enumerate(COURBES):
    x0 = 18 + i * (CW + 10)
    fig.rect(x0, Y0, CW, CH, stroke="#e2e2e2", fill="#ffffff", width=1.5, radius=8)

    # les axes du petit repère
    fig.line([(x0 + MARGE, Y0 + CH - MARGE), (x0 + CW - MARGE, Y0 + CH - MARGE)], GREY, 1.5)
    fig.line([(x0 + MARGE, Y0 + CH - MARGE), (x0 + MARGE, Y0 + MARGE)], GREY, 1.5)

    # la courbe, normalisée dans la boîte
    pts = []
    for k in range(81):
        t = k / 80
        v = max(0.0, min(1.0, f(t)))
        pts.append((x0 + MARGE + t * (CW - 2 * MARGE),
                    Y0 + CH - MARGE - v * (CH - 2 * MARGE)))
    fig.line(pts, RED, 2.8)

    fig.text(x0 + CW / 2, Y0 - 12, formule, size=15, weight=800, color=INK,
             mono=True, halo=False)
    fig.text(x0 + CW / 2, Y0 + CH + 22, usage, size=12.5, weight=700, color=SOFT)

fig.text(510, 300, "La même question revient à chaque fois : où ça monte, où ça plafonne, "
                   "et à quelle vitesse.",
         size=15, weight=700, color=INK)

fig.save("rde03_catalogue", "RDE-03 - Catalogue des formes")
