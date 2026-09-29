# -*- coding: utf-8 -*-
"""Schéma RNLB-03 — un octet à virgule : après la virgule, les puissances de 2 deviennent négatives.

  00 images/rnlb03_poids_negatifs.svg
  Excalidraw/RNLB-03 - Poids négatifs après la virgule.excalidraw.md

    python "tools/schemas/rnlb03_poids_negatifs.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 360)
BLUE = "#1f5fbf"

POW = ["2³", "2²", "2¹", "2⁰", "2⁻¹", "2⁻²", "2⁻³", "2⁻⁴"]
WGT = ["8", "4", "2", "1", "0,5", "0,25", "0,125", "0,0625"]
FRA = ["", "", "", "", "½", "¼", "⅛", "¹⁄₁₆"]
BITS = "01101000"

W, H, GAP = 88, 58, 34
X0, YC = 190, 150


def cx(i):
    return X0 + i * W + (GAP if i >= 4 else 0) + W / 2


# ------------------------------------------- en-têtes : partie entière / après la virgule
fig.text((cx(0) + cx(3)) / 2, 18, "PARTIE ENTIÈRE", size=13, weight=800, color=GREY)
fig.text((cx(4) + cx(7)) / 2, 18, "APRÈS LA VIRGULE", size=13, weight=800, color=BLUE)

# ------------------------------------------- ÷2 d'un rang au suivant
for i in range(7):
    a, b = cx(i) + 16, cx(i + 1) - 16
    fig.line([(a, 58), ((a + b) / 2, 50), (b, 58)], SOFT, 1.5, arrow=True)
    fig.text((a + b) / 2, 45, "÷2", size=11, weight=700, color=SOFT)

# ------------------------------------------- libellés de lignes
fig.text(20, 84, "puissance", anchor="start", size=14, weight=700, color=GREY)
fig.text(20, 112, "poids", anchor="start", size=14, weight=700, color=GREY)
fig.text(20, YC + 37, "bit", anchor="start", size=14, weight=700, color=GREY)
fig.text(20, YC + H + 40, "compte pour", anchor="start", size=14, weight=700, color=GREY)

for i in range(8):
    frac = i >= 4
    col = BLUE if frac else INK
    fig.text(cx(i), 84, POW[i], size=19, weight=800, color=col, mono=True)
    fig.text(cx(i), 112, WGT[i], size=15, weight=700, color=col, mono=True)
    if FRA[i]:
        fig.text(cx(i), 130, FRA[i], size=12, weight=600, color=SOFT)
    x = cx(i) - W / 2 + 4
    on = BITS[i] == "1"
    fig.rect(x, YC, W - 8, H, stroke=col, fill=("#e8eef9" if frac else "#ffffff") if on else PALE,
             width=2 if on else 1.2, radius=4)
    fig.text(cx(i), YC + 39, BITS[i], size=26, weight=800, color=col if on else GREY, mono=True, halo=False)
    if on:
        fig.text(cx(i), YC + H + 40, WGT[i], size=16, weight=800, color=col, mono=True)

# ------------------------------------------- la virgule
xv = X0 + 4 * W + GAP / 2
fig.text(xv, YC + 44, ",", size=40, weight=800, color=RED, mono=True, halo=False)

# ------------------------------------------- total
fig.text(X0 + 8 * W + GAP, 300, "0110,1000₂  =  4 + 2 + 0,5  =  6,5",
         anchor="end", size=22, weight=800, color=INK, mono=True)
fig.text(X0 + 8 * W + GAP, 334, "à droite de la virgule, chaque rang vaut la moitié du précédent",
         anchor="end", size=13, weight=700, color=RED)

fig.save("rnlb03_poids_negatifs", "RNLB-03 - Poids négatifs après la virgule")
