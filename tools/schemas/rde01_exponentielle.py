# -*- coding: utf-8 -*-
"""Schéma RDE-01 — la fonction exponentielle.

La courbe de 2^x à gauche, et à droite la lecture qui compte : un pas de plus
sur x double la valeur. Les six points entiers sont posés sur la courbe pour
qu'on puisse lire les valeurs sans calculatrice.

  00 images/rde01_exponentielle.svg
  Excalidraw/RDE-01 - Exponentielle.excalidraw.md

    python "tools/schemas/rde01_exponentielle.py"
"""
import math

from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)

X0, X1, Y0, Y1 = 78, 398, 288, 46      # le cadre du graphe, en pixels
XMAX, YMAX = 5.5, 34.0                 # les bornes du repère


def ecran(x, y):
    return (X0 + x / XMAX * (X1 - X0), Y0 - y / YMAX * (Y0 - Y1))


# --------------------------------------------------------------------- le repère
fig.line([(X0, Y0), (X1 + 10, Y0)], GREY, 2)
fig.line([(X0, Y0), (X0, Y1 - 10)], GREY, 2)
fig.text(X1 + 14, Y0 + 5, "x", anchor="start", size=14, weight=700, color=GREY)
fig.text(X0 - 10, Y1 - 14, "y", anchor="end", size=14, weight=700, color=GREY)

for v in (8, 16, 24, 32):
    _, sy = ecran(0, v)
    fig.line([(X0 - 5, sy), (X1, sy)], GREY, 1, dash=True, opacity=0.35)
    fig.text(X0 - 10, sy + 5, str(v), anchor="end", size=12, weight=700, color=SOFT)

for v in range(6):
    sx, _ = ecran(v, 0)
    fig.text(sx, Y0 + 20, str(v), size=12, weight=700, color=SOFT)

# --------------------------------------------------------------------- la courbe
# on s'arrête là où la courbe sort du cadre : 2^5.09 = 34
XFIN = math.log2(YMAX)
pts = [ecran(i / 40, 2 ** (i / 40)) for i in range(int(XFIN * 40) + 1)]
fig.line(pts, RED, 3)
fig.text(X0 + 16, Y1 + 18, "y = 2 puissance x", anchor="start", size=15, weight=800, color=RED)

for v in range(6):
    sx, sy = ecran(v, 2 ** v)
    fig.dot(sx, sy, 5, RED)

# --------------------------------------------------------------------- la lecture
CX = 700
fig.text(CX, 70, "CE QU'ON LIT SUR LA COURBE", size=14, weight=800, color=GREY)

for i, (titre, lignes) in enumerate((
    ("x", ["0", "1", "2", "3", "4", "5"]),
    ("2 puissance x", ["1", "2", "4", "8", "16", "32"]),
)):
    y = 118 + i * 34
    fig.text(CX - 250, y, titre, anchor="start", size=15, weight=800,
             color=INK if i else SOFT, mono=True, halo=False)
    for j, val in enumerate(lignes):
        fig.text(CX - 100 + j * 56, y, val, size=15, weight=800,
                 color=RED if i else SOFT, mono=True, halo=False)

fig.rect(CX - 240, 168, 480, 54, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(CX, 202, "un pas de plus sur x, deux fois plus sur y",
         size=17, weight=800, color=RED)

fig.text(CX, 258, "C'est la courbe d'expérience d'un jeu de rôle : chaque palier",
         size=15, weight=700, color=INK)
fig.text(CX, 282, "coûte le double du précédent, et le dernier coûte tout le reste.",
         size=15, weight=700, color=INK)

fig.save("rde01_exponentielle", "RDE-01 - Exponentielle")
