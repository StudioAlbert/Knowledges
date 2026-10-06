# -*- coding: utf-8 -*-
"""Schéma GVM-05 — la forme de la courbe, et la sensation qu'elle donne.

À gauche les quatre courbes dans le carré unité. À droite, la même chose vue
autrement : onze instants régulièrement espacés, et où la bille se trouve à
chacun. C'est l'espacement des points qui se voit à l'écran, pas la courbe.

  00 images/gvm05_easing.svg
  Excalidraw/GVM-05 - Courbes d'easing.excalidraw.md

    python "tools/schemas/gvm05_easing.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

BLEU, VERT = "#2b6cb0", "#2e9e5b"

COURBES = [
    ("lin\u00e9aire",      "t",            GREY, lambda t: t,                     True),
    ("smooth start",  "t\u00b2",           RED,  lambda t: t * t,                 False),
    ("smooth stop",   "1 \u2212 (1 \u2212 t)\u00b2", BLEU, lambda t: 1 - (1 - t) ** 2,      False),
    ("smoother step", "t\u00b2(3 \u2212 2t)",   VERT, lambda t: t * t * (3 - 2 * t),  False),
]

fig = Figure(1180, 400)

# ----------------------------------------------------------- le carre unite
X0, Y0, COTE = 80, 68, 250
X1, Y1 = X0 + COTE, Y0 + COTE
px = lambda t: X0 + t * COTE
py = lambda v: Y1 - v * COTE

fig.text(X0 + COTE / 2, 44, "LA COURBE", size=13, weight=800, color=GREY)
fig.rect(X0, Y0, COTE, COTE, stroke="#e5e5e5", fill="#fcfcfc", width=1.5, radius=4)
for k in (0.25, 0.5, 0.75):
    fig.line([(px(k), Y0), (px(k), Y1)], "#f0f0f0", 1)
    fig.line([(X0, py(k)), (X1, py(k))], "#f0f0f0", 1)
fig.line([(X0, Y1), (X1, Y1)], INK, 1.8)
fig.line([(X0, Y0), (X0, Y1)], INK, 1.8)
fig.text(X0 - 14, Y1 + 4, "0", size=12, weight=600, color=GREY)
fig.text(X1, Y1 + 20, "t = 1", size=12, weight=600, color=GREY)
fig.text(X0 - 16, Y0 + 6, "1", size=12, weight=600, color=GREY)

for nom, _, couleur, f, pointille in COURBES:
    pts = [(px(i / 60.0), py(f(i / 60.0))) for i in range(61)]
    fig.line(pts, couleur, 2.2 if pointille else 3, dash=pointille)

# ----------------------------------------------------------- les bandes
BX0, BX1 = 560, 1090
fig.text((BX0 + BX1) / 2, 44, "CE QUE L'\u0152IL VOIT : O\u00d9 EST LA BILLE \u00c0 CHAQUE INSTANT",
         size=13, weight=800, color=GREY)

N = 11
for i, (nom, formule, couleur, f, pointille) in enumerate(COURBES):
    y = 92 + i * 74
    fig.text(BX0 - 10, y - 16, nom, anchor="end", size=14, weight=800, color=couleur)
    fig.text(BX0 - 10, y + 6, formule, anchor="end", size=12.5, weight=600, color=SOFT, mono=True)
    fig.line([(BX0, y), (BX1, y)], "#e0e0e0", 5)
    for k in range(N):
        t = k / float(N - 1)
        x = BX0 + f(t) * (BX1 - BX0)
        dernier = k == N - 1
        fig.dot(x, y, 8 if dernier else 6, couleur if not pointille else GREY)
    fig.text(BX0, y + 26, "A", size=12, weight=700, color=GREY)
    fig.text(BX1, y + 26, "B", size=12, weight=700, color=GREY)

fig.text(300, 352, "les onze instants sont r\u00e9guliers ; seule la courbe change",
         size=13, weight=700, color=SOFT)
fig.text(300, 376, "points serr\u00e9s = lent \u00b7 points \u00e9cart\u00e9s = rapide",
         size=13, weight=800, color=INK)

fig.save("gvm05_easing", "GVM-05 - Courbes d'easing")
