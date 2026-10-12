# -*- coding: utf-8 -*-
"""Schéma RDE-01 — la fonction logarithme.

Le jumeau de `rde01_exponentielle.py`, lu dans l'autre sens : il faut multiplier
x par deux pour gagner un pas sur y. Mêmes six points, mêmes valeurs, axes
échangés — c'est ce qui se voit en mettant les deux schémas l'un sous l'autre.

  00 images/rde01_logarithme.svg
  Excalidraw/RDE-01 - Logarithme.excalidraw.md

    python "tools/schemas/rde01_logarithme.py"
"""
import math

from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)

X0, X1, Y0, Y1 = 78, 398, 288, 46
XMAX, YMAX = 35.0, 5.6


def ecran(x, y):
    return (X0 + x / XMAX * (X1 - X0), Y0 - y / YMAX * (Y0 - Y1))


# --------------------------------------------------------------------- le repère
fig.line([(X0, Y0), (X1 + 10, Y0)], GREY, 2)
fig.line([(X0, Y0), (X0, Y1 - 10)], GREY, 2)
fig.text(X1 + 14, Y0 + 5, "x", anchor="start", size=14, weight=700, color=GREY)
fig.text(X0 - 10, Y1 - 14, "y", anchor="end", size=14, weight=700, color=GREY)

for v in range(1, 6):
    _, sy = ecran(0, v)
    fig.line([(X0 - 5, sy), (X1, sy)], GREY, 1, dash=True, opacity=0.35)
    fig.text(X0 - 10, sy + 5, str(v), anchor="end", size=12, weight=700, color=SOFT)

for v in (0, 8, 16, 24, 32):
    sx, _ = ecran(v, 0)
    fig.text(sx, Y0 + 20, str(v), size=12, weight=700, color=SOFT)

# --------------------------------------------------------------------- la courbe
# le logarithme n'existe pas en 0 : on part de x = 1, là où il vaut 0
pts = [ecran(1 + i * (XMAX - 1) / 400, math.log2(1 + i * (XMAX - 1) / 400)) for i in range(401)]
fig.line(pts, RED, 3)
fig.text(X0 + 16, Y1 + 18, "y = log base 2 de x", anchor="start", size=15, weight=800, color=RED)

for v in range(6):
    sx, sy = ecran(2 ** v, v)
    fig.dot(sx, sy, 5, RED)

# --------------------------------------------------------------------- la lecture
CX = 700
fig.text(CX, 70, "CE QU'ON LIT SUR LA COURBE", size=14, weight=800, color=GREY)

for i, (titre, lignes) in enumerate((
    ("x", ["1", "2", "4", "8", "16", "32"]),
    ("log base 2", ["0", "1", "2", "3", "4", "5"]),
)):
    y = 118 + i * 34
    fig.text(CX - 250, y, titre, anchor="start", size=15, weight=800,
             color=INK if i else SOFT, mono=True, halo=False)
    for j, val in enumerate(lignes):
        fig.text(CX - 100 + j * 56, y, val, size=15, weight=800,
                 color=RED if i else SOFT, mono=True, halo=False)

fig.rect(CX - 240, 168, 480, 54, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(CX, 202, "deux fois plus sur x, un pas de plus sur y",
         size=17, weight=800, color=RED)

fig.text(CX, 258, "Il répond à « combien de fois diviser par deux avant d'arriver",
         size=15, weight=700, color=INK)
fig.text(CX, 282, "à un » : la dichotomie, les arbres, et le coût qui ne s'envole pas.",
         size=15, weight=700, color=INK)

fig.save("rde01_logarithme", "RDE-01 - Logarithme")
