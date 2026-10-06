# -*- coding: utf-8 -*-
"""Schéma BDP-05 — une grille de morpion en 2D, et la même grille rangée en 1D.

  00 images/bdp05_grille_1d.svg
  Excalidraw/BDP-05 - Grille 2D et tableau 1D.excalidraw.md

    python "tools/schemas/bdp05_grille_1d.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 400)
BLUE, GREEN = "#1f5fbf", "#2e7d32"
LINE_COL = [INK, BLUE, GREEN]
CELLS = "XO  X O X"

# ------------------------------------------- 2D
GX, GY, C = 60, 80, 78
fig.text(GX + 1.5 * C, 32, "char grille[3][3]", size=17, weight=800, color=INK, mono=True)
for l in range(3):
    fig.text(GX - 16, GY + l * C + C / 2 + 6, str(l), anchor="end", size=14, weight=800, color=LINE_COL[l], mono=True)
    for c in range(3):
        x, y = GX + c * C, GY + l * C
        hit = (l, c) == (2, 0)
        fig.rect(x + 3, y + 3, C - 6, C - 6, stroke=RED if hit else LINE_COL[l],
                 fill="#fdeaea" if hit else "#ffffff", width=3 if hit else 2, radius=4)
        v = CELLS[l * 3 + c]
        fig.text(x + C / 2, y + C / 2 + 11, v if v != " " else "", size=30, weight=800,
                 color=RED if hit else LINE_COL[l], mono=True, halo=False)
        fig.text(x + C - 8, y + 18, "%d,%d" % (l, c), anchor="end", size=10, weight=600, color=GREY, mono=True, halo=False)
for c in range(3):
    fig.text(GX + c * C + C / 2, GY - 10, str(c), size=14, weight=800, color=GREY, mono=True)
fig.text(GX - 16, GY - 10, "l\\c", anchor="end", size=11, weight=700, color=GREY, mono=True)
fig.text(GX + 1.5 * C, GY + 3 * C + 32, "grille[2][0]", size=16, weight=800, color=RED, mono=True)

# ------------------------------------------- 1D
LX, LY, LC = 380, 150, 64
fig.text(LX + 4.5 * LC, 32, "char grille[9]", size=17, weight=800, color=INK, mono=True)
for i in range(9):
    l = i // 3
    x = LX + i * LC
    hit = i == 6
    fig.text(x + LC / 2, LY - 12, str(i), size=14, weight=800, color=RED if hit else GREY, mono=True)
    fig.rect(x + 2, LY, LC - 4, 64, stroke=RED if hit else LINE_COL[l], fill="#fdeaea" if hit else "#ffffff",
             width=3 if hit else 2, radius=4)
    v = CELLS[i]
    fig.text(x + LC / 2, LY + 43, v if v != " " else "", size=26, weight=800,
             color=RED if hit else LINE_COL[l], mono=True, halo=False)
for l in range(3):
    xa, xb = LX + l * 3 * LC + 4, LX + (l + 1) * 3 * LC - 4
    fig.line([(xa, LY + 74), (xa, LY + 82), (xb, LY + 82), (xb, LY + 74)], LINE_COL[l], 2)
    fig.text((xa + xb) / 2, LY + 102, "ligne %d" % l, size=13, weight=800, color=LINE_COL[l])


# formule
fig.text(LX + 4.5 * LC, 330, "index = ligne × 3 + colonne", size=22, weight=800, color=INK, mono=True)
fig.text(LX + 4.5 * LC, 364, "2 × 3 + 0 = 6", size=18, weight=800, color=RED, mono=True)

fig.save("bdp05_grille_1d", "BDP-05 - Grille 2D et tableau 1D")
