# -*- coding: utf-8 -*-
"""Schéma POO-01 — six variables éparpillées, puis une seule structure qui les range.

  00 images/poo01_regrouper.svg
  Excalidraw/POO-01 - Regrouper dans une structure.excalidraw.md

    python "tools/schemas/poo01_regrouper.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 360)

# ------------------------------------------- gauche : six variables éparpillées
fig.text(200, 28, "AVANT : SIX VARIABLES", size=13, weight=800, color=GREY)
VARS = [("nom", "\"Gobelin\"", 95, 85), ("pv", "30", 265, 70), ("degats", "5", 110, 175),
        ("vitesse", "2.5", 300, 165), ("posX", "0", 120, 270), ("posY", "0", 285, 265)]
pts = [(x, y) for _, _, x, y in VARS]
# liens pointillés « ça va ensemble », dessinés sous les boîtes
for a, b in [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5), (2, 3)]:
    fig.line([pts[a], pts[b]], GREY, 1.4, dash=True, opacity=0.7)
for n, v, x, y in VARS:
    fig.rect(x - 70, y - 24, 140, 48, stroke=GREY, fill="#ffffff", width=1.8, radius=6)
    fig.text(x, y - 3, n, size=15, weight=800, color=INK, mono=True, halo=False)
    fig.text(x, y + 16, v, size=13, weight=600, color=SOFT, mono=True, halo=False)
fig.text(200, 330, "leur lien n'existe que dans votre tête", size=13, weight=700, color=SOFT)

# ------------------------------------------- flèche
fig.line([(420, 175), (560, 175)], RED, 3, arrow=True)
fig.text(490, 160, "struct", size=15, weight=800, color=RED, mono=True)

# ------------------------------------------- droite : une boîte Ennemi
X, Y, W = 600, 55, 330
fig.text(X + W / 2, 28, "APRÈS : UN TYPE", size=13, weight=800, color=GREY)
fig.rect(X, Y, W, 250, stroke=RED, fill="#ffffff", width=3, radius=10)
fig.rect(X, Y, W, 44, stroke=RED, fill=RED, width=3, radius=10)
fig.text(X + W / 2, Y + 29, "Ennemi", size=18, weight=800, color="#ffffff", mono=True, halo=False)
for i, (n, v, _, _) in enumerate(VARS):
    y = Y + 76 + i * 33
    fig.text(X + 26, y, n, anchor="start", size=15, weight=800, color=INK, mono=True, halo=False)
    fig.text(X + W - 26, y, v, anchor="end", size=15, weight=600, color=SOFT, mono=True, halo=False)
    if i < 5:
        fig.line([(X + 16, y + 12), (X + W - 16, y + 12)], "#e5e5e5", 1)
fig.text(X + W / 2, 330, "un seul type, six champs qui voyagent ensemble", size=13, weight=700, color=RED)

fig.save("poo01_regrouper", "POO-01 - Regrouper dans une structure")
