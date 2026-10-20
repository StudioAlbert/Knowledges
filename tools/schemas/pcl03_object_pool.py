# -*- coding: utf-8 -*-
"""Schéma PCL-03 — Object Pool.

Seize projectiles alloués une seule fois, au chargement. Pendant la partie, on
ne crée rien et on ne détruit rien : on prend une case libre, et on la rend.

  00 images/pcl03_object_pool.svg
  Excalidraw/PCL-03 - Object Pool.excalidraw.md

    python "tools/schemas/pcl03_object_pool.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 330)

# ----------------------------------------------------------------- la réserve
X0, Y0, C, L = 70, 96, 52, 46
EN_VOL = {0, 1, 4, 7, 8, 12}

fig.text(X0, 74, "LA RÉSERVE — 16 PROJECTILES, ALLOUÉS AU CHARGEMENT",
         anchor="start", size=14, weight=800, color=GREY)

for i in range(16):
    x = X0 + (i % 8) * (C + 6)
    y = Y0 + (i // 8) * (L + 10)
    if i in EN_VOL:
        fig.rect(x, y, C, L, stroke=RED, fill=RED, width=2.5, radius=8)
    else:
        fig.rect(x, y, C, L, stroke=GREY, fill=PALE, width=2, dash=True, radius=8)

fig.text(X0, 222, "6 en vol", anchor="start", size=15, weight=800, color=RED)
fig.text(X0 + 110, 222, "10 libres, prêtes", anchor="start", size=15, weight=700, color=SOFT)

fig.rect(X0 - 12, 250, 490, 56, stroke=INK, fill="#ffffff", width=2.5, radius=10)
fig.text(X0 + 233, 274, "pendant la partie : aucune allocation,", size=15, weight=800, color=INK)
fig.text(X0 + 233, 296, "aucune destruction", size=14, weight=700, color=SOFT)

# ----------------------------------------------------------------- le cycle
tirer = fig.box(800, 108, "Tirer", w=200, h=54, size=17)
impact = fig.box(800, 228, "Impact ou sortie d'écran", w=280, h=54, size=15)

fig.arrow(tirer, impact, "prendre", bend=54, label_dx=-120, label_dy=4,
          color=RED, width=3, label_color=RED, size=15)
fig.arrow(impact, tirer, "rendre", bend=54, label_dx=105, label_dy=4,
          color=INK, width=3, size=15)

fig.text(800, 52, "LE CYCLE", size=14, weight=800, color=GREY)

fig.save("pcl03_object_pool", "PCL-03 - Object Pool")
