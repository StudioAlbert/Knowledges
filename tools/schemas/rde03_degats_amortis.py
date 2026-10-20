# -*- coding: utf-8 -*-
"""Schéma RDE-03 — la courbe d'amorti du formatif.

Les deux courbes respectent **les mêmes règles de game design** : 25 dégâts à
bout portant, 0 à cinq mètres. Seule la forme entre les deux change. La droite
perd ses dégâts régulièrement ; l'amortie les garde, puis s'effondre.

C'est la figure que l'étudiant doit reproduire : les cinq points marqués sont
les valeurs à retrouver, la formule n'est pas donnée.

  00 images/rde03_degats_amortis.svg
  Excalidraw/RDE-03 - Degats amortis.excalidraw.md

    python "tools/schemas/rde03_degats_amortis.py"
"""
import math

from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1040, 350)

X0, X1, Y0, Y1 = 86, 626, 292, 54
DMAX, DEGMAX = 6.0, 28.0
D_MIN, D_MAX, DEGATS = 0.25, 5.0, 25.0


def t(d):
    return min(1.0, max(0.0, (d - D_MIN) / (D_MAX - D_MIN)))


def proportionnel(d):
    return DEGATS * (1 - t(d))


def amorti(d):
    return DEGATS * math.sqrt(1 - t(d))


def ecran(d, deg):
    return (X0 + d / DMAX * (X1 - X0), Y0 - deg / DEGMAX * (Y0 - Y1))


# --------------------------------------------------------------------- le repère
fig.line([(X0, Y0), (X1 + 12, Y0)], GREY, 2)
fig.line([(X0, Y0), (X0, Y1 - 12)], GREY, 2)
fig.text(X1 + 16, Y0 + 5, "d (m)", anchor="start", size=13, weight=700, color=GREY)
fig.text(X0 - 12, Y1 - 16, "dégâts", anchor="end", size=13, weight=700, color=GREY)

for v in (5, 10, 15, 20, 25):
    _, sy = ecran(0, v)
    fig.line([(X0 - 5, sy), (X1, sy)], GREY, 1, dash=True, opacity=0.28)
    fig.text(X0 - 10, sy + 5, str(v), anchor="end", size=12, weight=700, color=SOFT)

for v in (1, 2, 3, 4, 5, 6):
    sx, _ = ecran(v, 0)
    fig.text(sx, Y0 + 20, str(v), size=12, weight=700, color=SOFT)

# --------------------------------------------------------------------- les deux courbes
fig.line([ecran(i * DMAX / 300, proportionnel(i * DMAX / 300)) for i in range(301)],
         GREY, 2.5, dash=True)
fig.line([ecran(i * DMAX / 300, amorti(i * DMAX / 300)) for i in range(301)], RED, 3.5)

fig.text(ecran(3.5, 0)[0], ecran(0, 7.5)[1], "proportionnelle", size=14, weight=700, color=SOFT)
fig.text(ecran(1.5, 0)[0], ecran(0, 26.4)[1], "amortie", size=15, weight=800, color=RED)

# --------------------------------------------------------------------- les points à retrouver
REPERES = [0.25, 1.4, 2.6, 3.8, 5.0]
for d in REPERES:
    sx, sy = ecran(d, amorti(d))
    fig.dot(sx, sy, 5.5, RED)

sx, sy = ecran(3.8, amorti(3.8))
fig.line([(X0, sy), (sx, sy)], RED, 1.5, dash=True, opacity=0.55)
fig.text(X0 + 14, sy - 9, "la moitié des dégâts, à 3,8 m", anchor="start",
         size=13, weight=800, color=RED)

# --------------------------------------------------------------------- le tableau
CX = 836
fig.text(CX, 78, "LES CINQ POINTS À RESPECTER", size=14, weight=800, color=GREY)

fig.text(CX - 160, 112, "d (m)", anchor="start", size=13, weight=800, color=SOFT,
         mono=True, halo=False)
fig.text(CX + 70, 112, "dégâts", anchor="start", size=13, weight=800, color=SOFT,
         mono=True, halo=False)

for i, d in enumerate(REPERES):
    y = 142 + i * 28
    fig.text(CX - 160, y, ("%.2f" % d).replace(".", ","), anchor="start", size=15,
             weight=700, color=INK, mono=True, halo=False)
    fig.text(CX + 70, y, ("%.1f" % amorti(d)).replace(".", ","), anchor="start", size=15,
             weight=800, color=RED, mono=True, halo=False)

fig.text(CX, 316, "Les deux bornes sont imposées. La forme entre elles, non.",
         size=14, weight=700, color=INK)

fig.save("rde03_degats_amortis", "RDE-03 - Degats amortis")
