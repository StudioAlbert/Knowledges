# -*- coding: utf-8 -*-
"""Schéma PCO-925 — les phases du projet commun, semaine par semaine.

  00 images/pco925_phases.svg
  Excalidraw/PCO-925 - Phases du projet.excalidraw.md

    python "tools/schemas/pco925_phases.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 280)
X0, X1, Y = 40, 960, 120
WEEKS = 24
def wx(s):            # bord gauche de la semaine s (1-indexée)
    return X0 + (s - 1) * (X1 - X0) / WEEKS

PHASES = [
    (1, 4, "Prototypage", "idéation, POC", RED, "#ffffff"),
    (5, 9, "V1", "features, play tests", INK, "#ffffff"),
    (10, 14, "V2", "+ budget assets", INK, "#ffffff"),
    (15, 19, "V3", "vers le livrable", INK, "#ffffff"),
    (20, 23, "Polish", "fix ou cut", GREY, "#ffffff"),
    (24, 24, "Fin", "build", RED, "#ffffff"),
]
for a, b, name, sub, col, txt in PHASES:
    xa, xb = wx(a) + 2, wx(b + 1) - 2
    fig.rect(xa, Y, xb - xa, 64, stroke=col, fill=col, width=2, radius=6)
    fig.text((xa + xb) / 2, Y + 30, name, size=17 if b > a else 13, weight=800, color=txt, halo=False)
    if b > a:
        fig.text((xa + xb) / 2, Y + 52, sub, size=12, weight=600, color=txt, halo=False)
    else:
        fig.text((xa + xb) / 2, Y + 52, sub, size=10, weight=600, color=txt, halo=False)

# graduation des semaines
for s in range(1, WEEKS + 1):
    x = (wx(s) + wx(s + 1)) / 2
    fig.text(x, Y + 92, "S%d" % s, size=10, weight=700, color=GREY, mono=True)
# sprints de 2 semaines
for s in range(1, WEEKS + 1, 2):
    fig.line([(wx(s) + 3, Y + 104), (wx(s + 2) - 3, Y + 104)], SOFT, 2)
fig.text((X0 + X1) / 2, Y + 132, "un sprint = 2 semaines, un point bi-hebdomadaire à chaque fin de sprint",
         size=13, weight=700, color=SOFT)

# livrables
fig.text(wx(1), 40, "PROTOTYPE + PLANNING", anchor="start", size=12, weight=800, color=RED)
fig.line([(wx(5) - 2, 50), (wx(5) - 2, Y - 6)], RED, 2, dash=True)
fig.text(wx(5) + 6, 70, "chaque version : play tests, puis scope de la suivante", anchor="start",
         size=12, weight=700, color=INK)
fig.text(X1, 40, "LIVRAISON : 15.02.2027", anchor="end", size=13, weight=800, color=RED)
fig.line([(X1 - 2, 50), (X1 - 2, Y - 6)], RED, 2, dash=True)

fig.save("pco925_phases", "PCO-925 - Phases du projet")
