# -*- coding: utf-8 -*-
"""Schéma RNLB-03 — −6,5 en float : le bit de signe et le déplacement de la virgule.

  00 images/rnlb03_moins_6_5.svg
  Excalidraw/RNLB-03 - Moins 6,5 en float.excalidraw.md

    python "tools/schemas/rnlb03_moins_6_5.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 345)
BLUE = "#1f5fbf"

# ------------------------------------------- 1. normaliser : la virgule se déplace
fig.text(20, 30, "1 · NORMALISER", anchor="start", size=13, weight=800, color=GREY)
fig.text(40, 80, "−6,5  =", anchor="start", size=24, weight=800, mono=True)
chars = ["−", "1", "1", "0", ",", "1"]
CX = [175 + i * 18 for i in range(len(chars))]
for x, c in zip(CX, chars):
    fig.text(x, 80, c, size=26, weight=800, color=RED if c == "," else INK, mono=True)
fig.text(CX[-1] + 12, 84, "₂", anchor="start", size=16, weight=800, mono=True)
fig.text(330, 80, "=  −1,101₂ × 2²", anchor="start", size=24, weight=800, mono=True)
# la virgule recule de 2 rangs : de sa place (entre 0 et 1) à après le premier 1
xa, xb = CX[4], (CX[1] + CX[2]) / 2
fig.line([(xa, 92), (xa - 6, 104), ((xa + xb) / 2, 110), (xb + 6, 104), (xb, 94)], RED, 2.5, arrow=True)
fig.text(260, 132, "la virgule recule de 2 rangs → exposant 2", size=13, weight=700, color=RED)
fig.text(700, 62, "signe : négatif → 1", anchor="start", size=14, weight=700, color=RED)
fig.text(700, 86, "exposant : 2 + 127 = 129", anchor="start", size=14, weight=700, color=BLUE)
fig.text(700, 110, "mantisse : 101 (1, implicite)", anchor="start", size=14, weight=700, color=INK)

# ------------------------------------------- 2. les 32 bits
fig.text(20, 168, "2 · RANGER SUR 32 BITS", anchor="start", size=13, weight=800, color=GREY)
bits = "1" + "10000001" + "101" + "0" * 20
X0, Y, W, H = 52, 190, 28, 40
for i, b in enumerate(bits):
    x = X0 + i * W
    if i == 0:
        stroke, fill, col = RED, "#fdeaea", RED
    elif i <= 8:
        stroke, fill, col = BLUE, "#e8eef9", BLUE
    elif i <= 11:
        stroke, fill, col = INK, "#ffffff", INK
    else:
        stroke, fill, col = GREY, PALE, GREY
    fig.rect(x, Y, W, H, stroke=stroke, fill=fill, width=1.5, radius=0)
    fig.text(x + W / 2, Y + 27, b, size=17, weight=800, color=col, mono=True, halo=False)

def brace(i0, i1, label, color):
    xa, xb = X0 + i0 * W + 3, X0 + (i1 + 1) * W - 3
    fig.line([(xa, Y - 6), (xa, Y - 12), (xb, Y - 12), (xb, Y - 6)], color, 2)
    return (xa + xb) / 2

brace(0, 0, "", RED)
brace(1, 8, "", BLUE)
brace(9, 31, "", INK)
fig.text(X0 + W / 2, Y + H + 22, "signe", size=13, weight=800, color=RED)
fig.text(X0 + 4.5 * W + W / 2, Y + H + 22, "exposant 129", size=13, weight=800, color=BLUE)
fig.text(X0 + 20.5 * W, Y + H + 22, "mantisse : 101 puis 20 zéros", size=13, weight=800, color=INK)

# ------------------------------------------- 3. par paquets de 4 : l'hexadécimal
hexd = "C0D00000"
for k, h in enumerate(hexd):
    xa, xb = X0 + 4 * k * W + 4, X0 + 4 * (k + 1) * W - 4
    fig.line([(xa, Y + H + 36), (xa, Y + H + 42), (xb, Y + H + 42), (xb, Y + H + 36)], GREY, 1.5)
    fig.text((xa + xb) / 2, Y + H + 66, h, size=20, weight=800, color=INK, mono=True)
fig.text(X0 + 32 * W, Y + H + 98, "= 0xC0D00000", anchor="end", size=18, weight=800,
         color=RED, mono=True)

fig.save("rnlb03_moins_6_5", "RNLB-03 - Moins 6,5 en float")
