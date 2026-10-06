# -*- coding: utf-8 -*-
"""Schéma BDP-05 — un tableau de 3 cases, ses index, et la case de trop.

  00 images/bdp05_index.svg
  Excalidraw/BDP-05 - Index et dépassement.excalidraw.md

    python "tools/schemas/bdp05_index.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 330)
X0, Y, W, H = 150, 110, 130, 80

fig.text(30, Y + 50, "int vies[3]", anchor="start", size=17, weight=800, color=INK, mono=True)

# accolade « le tableau »
xa, xb = X0, X0 + 3 * W
fig.line([(xa + 4, Y - 46), (xa + 4, Y - 54), (xb - 4, Y - 54), (xb - 4, Y - 46)], INK, 2)
fig.text((xa + xb) / 2, Y - 64, "LE TABLEAU : 3 CASES", size=13, weight=800, color=INK)

for i in range(3):
    x = X0 + i * W
    fig.text(x + W / 2, Y - 14, "[%d]" % i, size=17, weight=800, color=RED, mono=True)
    fig.rect(x + 4, Y, W - 8, H, stroke=INK, fill="#ffffff", width=2.5, radius=6)
    fig.text(x + W / 2, Y + 52, "3", size=28, weight=800, color=INK, mono=True, halo=False)

# la case de trop
x = X0 + 3 * W + 20
fig.text(x + W / 2, Y - 14, "[3]", size=17, weight=800, color=RED, mono=True)
fig.rect(x + 4, Y, W - 8, H, stroke=RED, fill="#fdeaea", width=2.5, dash=True, radius=6)
fig.text(x + W / 2, Y + 52, "?", size=30, weight=800, color=RED, mono=True, halo=False)
x2 = x + W
fig.rect(x2 + 4, Y, W - 8, H, stroke=GREY, fill=PALE, width=1.5, dash=True, radius=6)
fig.text(x2 + W / 2, Y + 34, "score", size=14, weight=700, color=GREY, mono=True, halo=False)
fig.text(x2 + W / 2, Y + 58, "1200", size=16, weight=700, color=GREY, mono=True, halo=False)
fig.text(x + W, Y - 64, "HORS DU TABLEAU : LA MÉMOIRE VOISINE", size=13, weight=800, color=RED)

# légendes
fig.text(X0 + 1.5 * W, Y + H + 40, "premier index : 0 — dernier : taille − 1", size=15, weight=700, color=INK)
fig.text(x + W, Y + H + 40, "vies[3] compile, et lit n'importe quoi", size=15, weight=700, color=RED)
fig.text(500, Y + H + 92, "C++ ne vérifie pas l'index d'un tableau C : aucune erreur, aucun message",
         size=14, weight=700, color=SOFT)

fig.save("bdp05_index", "BDP-05 - Index et dépassement")
