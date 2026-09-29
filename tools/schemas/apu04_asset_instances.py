# -*- coding: utf-8 -*-
"""Schéma APU-04 — un asset dans le projet, des instances dans la scène.

  00 images/apu04_asset_instances.svg
  Excalidraw/APU-04 - Asset et instances de scène.excalidraw.md

    python "tools/schemas/apu04_asset_instances.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 335)

fig.rect(20, 30, 330, 290, stroke=GREY, fill=PALE, width=2, dash=True)
fig.text(35, 56, "PROJET — une fois", anchor="start", size=14, weight=800, color=GREY)
fig.rect(470, 30, 510, 290, stroke=GREY, fill=PALE, width=2, dash=True)
fig.text(485, 56, "SCÈNE — autant qu'on en pose", anchor="start", size=14, weight=800, color=GREY)

small = fig.box(185, 125, "Araignée.asset", w=250, h=62, active=True, sub="PV 30 · vitesse 2 · dégâts 5")
big = fig.box(185, 240, "Araignée géante.asset", w=250, h=62, sub="PV 80 · vitesse 1 · dégâts 12")

pos = [(590, 85), (590, 135), (590, 185), (590, 245), (590, 295)]
for i, (x, y) in enumerate(pos):
    b = fig.box(x, y, "Spider (%d)" % (i + 1), w=150, h=36, size=14)
    target = small if i < 3 else big
    fig.arrow(b, target, color=RED if i < 3 else GREY, width=2)

fig.text(840, 150, "5 ennemis", size=15, weight=800, color=INK)
fig.text(840, 172, "2 jeux de données", size=15, weight=800, color=RED)
fig.text(840, 215, "la référence va", size=13, weight=600, color=SOFT)
fig.text(840, 233, "de la scène vers l'asset", size=13, weight=600, color=SOFT)

fig.save("apu04_asset_instances", "APU-04 - Asset et instances de scène")
