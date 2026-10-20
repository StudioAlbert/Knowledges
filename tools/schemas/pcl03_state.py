# -*- coding: utf-8 -*-
"""Schéma PCL-03 — State.

À gauche l'automate du héros : quatre états, un seul courant, des transitions
qui portent un nom. À droite ce qu'il remplace — trois booléens dont une
combinaison décrit une situation qui n'existe pas.

  00 images/pcl03_state.svg
  Excalidraw/PCL-03 - State.excalidraw.md

    python "tools/schemas/pcl03_state.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 330)

sol = fig.box(150, 78, "Au sol", w=170, h=50, active=True, size=17)
air = fig.box(430, 78, "En l'air", w=170, h=50, size=17)
mur = fig.box(430, 232, "Au mur", w=170, h=50, size=17)
accroupi = fig.box(150, 232, "Accroupi", w=170, h=50, size=17)

fig.start(sol, dx=-60)

fig.arrow(sol, air, "saut", bend=30, label_dy=24)
fig.arrow(air, sol, "atterrit", bend=30, label_dy=-14)
fig.arrow(air, mur, "touche un mur", label_dx=66, label_dy=4)
fig.arrow(mur, air, "wall jump", bend=34, label_dx=-66, label_dy=4)
fig.arrow(sol, accroupi, "bas", label_dx=-30, label_dy=4)
fig.arrow(accroupi, sol, "relâche", bend=36, label_dx=34, label_dy=4)

fig.text(150, 300, "un seul état courant, toujours", size=15, weight=800, color=RED)

# ------------------------------------------------------------------ l'avant
CX = 770
fig.text(CX, 44, "CE QU'IL REMPLACE", size=14, weight=800, color=GREY)

fig.rect(CX - 190, 60, 380, 104, stroke=GREY, fill=PALE, width=2, radius=10)
for i, ligne in enumerate(("bool au_sol;", "bool en_lair;", "bool accroupi;")):
    fig.text(CX - 168, 88 + i * 28, ligne, anchor="start", size=16, weight=700,
             color=SOFT, mono=True, halo=False)

fig.rect(CX - 190, 182, 380, 56, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(CX, 206, "au_sol && en_lair", size=17, weight=800, color=RED, mono=True)
fig.text(CX, 228, "un état qui n'existe pas", size=14, weight=700, color=SOFT)

fig.text(CX, 272, "trois booléens font huit combinaisons,", size=15, weight=700, color=INK)
fig.text(CX, 294, "et seulement quatre ont un sens.", size=15, weight=700, color=INK)

fig.save("pcl03_state", "PCL-03 - State")
