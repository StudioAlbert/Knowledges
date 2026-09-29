# -*- coding: utf-8 -*-
"""Schéma RNLB-02 — modulo 2ⁿ : les valeurs d'un entier non signé forment un cercle.

  00 images/rnlb02_modulo_roue.svg
  Excalidraw/RNLB-02 - Modulo 2n, le cercle.excalidraw.md

Slide « Modulo 2ⁿ : un cercle, pas une droite » (titre + une ligne de contexte).

    python "tools/schemas/rnlb02_modulo_roue.py"
"""
import math
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)
CX, CY, R = 230, 172, 112

fig.circle(CX, CY, R)
for i in range(8):
    a = -math.pi / 2 + i * 2 * math.pi / 8
    x, y = CX + R * math.cos(a), CY + R * math.sin(a)
    hot = i in (0, 7)
    fig.dot(x, y, 19 if hot else 16, RED if hot else INK)
    fig.text(x, y + 6, str(i), size=17, weight=800, color="#ffffff", halo=False)
    lx, ly = CX + (R + 40) * math.cos(a), CY + (R + 40) * math.sin(a)
    fig.text(lx, ly + 5, format(i, "03b"), size=15, weight=700 if hot else 500,
             color=RED if hot else GREY, mono=True)

# +1 de 7 vers 0, à l'intérieur du cercle
pts = []
for k in range(13):
    a = -math.pi / 2 + (7.15 + 0.7 * k / 12) * 2 * math.pi / 8
    pts.append((CX + (R - 34) * math.cos(a), CY + (R - 34) * math.sin(a)))
fig.line(pts, RED, 3.5, arrow=True)
fig.text(CX - 30, CY - 42, "+1", size=17, weight=800, color=RED)
fig.text(CX, CY + 2, "3 bits", size=19, weight=800, color=INK)
fig.text(CX, CY + 26, "2³ = 8 positions", size=14, weight=500, color=GREY)

# ------------------------------------------------ à droite : on garde n bits
X = 480
fig.text(X, 42, "On calcule, puis on garde les 3 bits du bas", anchor="start", size=18, weight=800)
fig.line([(X, 56), (960, 56)], RED, 3)
rows = [("7 + 1", "111 + 001 = 1 000", "000 = 0"),
        ("0 − 1", "(1)000 − 001", "111 = 7"),
        ("5 + 6", "101 + 110 = 1 011", "011 = 3")]
y = 98
for a, b, c in rows:
    fig.text(X, y, a, anchor="start", size=18, weight=800)
    fig.text(X + 90, y, b, anchor="start", size=16, weight=500, color=GREY, mono=True)
    fig.text(X + 330, y, "→", anchor="start", size=17, weight=800, color=RED)
    fig.text(X + 360, y, c, anchor="start", size=16, weight=800, color=RED, mono=True)
    y += 58
fig.text(X, 290, "Retenue perdue à gauche, emprunt à un bit fictif :", anchor="start", size=14, weight=500, color=SOFT)
fig.text(X, 312, "c'est le reste de la division par 2ⁿ.", anchor="start", size=14, weight=700, color=INK)

fig.save("rnlb02_modulo_roue", "RNLB-02 - Modulo 2n, le cercle")
