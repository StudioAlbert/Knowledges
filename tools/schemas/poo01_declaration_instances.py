# -*- coding: utf-8 -*-
"""Schéma POO-01 — la déclaration décrit la forme, chaque instance porte ses valeurs.

  00 images/poo01_declaration_instances.svg
  Excalidraw/POO-01 - Déclaration et instances.excalidraw.md

    python "tools/schemas/poo01_declaration_instances.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 380)
FIELDS = [("std::string", "nom"), ("int", "pointsDeVie"), ("int", "defense"), ("int", "attaque")]

# ------------------------------------------- la déclaration : un plan
X, Y, W, H = 30, 70, 360, 220
fig.text(X + W / 2, 40, "DÉCLARATION : LE PLAN", size=13, weight=800, color=GREY)
fig.rect(X, Y, W, H, stroke=GREY, fill=PALE, width=2.2, dash=True, radius=10)
fig.text(X + 24, Y + 36, "struct Ennemi", anchor="start", size=19, weight=800, color=INK, mono=True, halo=False)
for i, (t, n) in enumerate(FIELDS):
    y = Y + 80 + i * 34
    fig.text(X + 40, y, t, anchor="start", size=15, weight=600, color=SOFT, mono=True, halo=False)
    fig.text(X + 190, y, n, anchor="start", size=15, weight=800, color=INK, mono=True, halo=False)
fig.text(X + W / 2, Y + H + 34, "une forme, aucune valeur, aucune mémoire", size=13, weight=700, color=SOFT)

# ------------------------------------------- deux instances
def instance(x, y, name, vals):
    w, h = 420, 128
    fig.rect(x, y, w, h, stroke=INK, fill="#ffffff", width=2.5, radius=10)
    fig.text(x + 20, y + 30, name, anchor="start", size=17, weight=800, color=RED, mono=True, halo=False)
    for i, ((_, n), v) in enumerate(zip(FIELDS, vals)):
        cx = x + 20 + (i % 2) * 200
        cy = y + 68 + (i // 2) * 34
        fig.text(cx, cy, n, anchor="start", size=13, weight=600, color=SOFT, mono=True, halo=False)
        fig.text(cx + 185, cy, v, anchor="end", size=15, weight=800,
                 color=RED if (n == "pointsDeVie" and v == "20") else INK, mono=True, halo=False)
    return (x, y + h / 2)

fig.text(770, 40, "INSTANCES : LES OBJETS", size=13, weight=800, color=GREY)
a = instance(555, 62, "Ennemi gobelinA", ["\"Gobelin\"", "20", "2", "5"])
b = instance(555, 222, "Ennemi gobelinB", ["\"Gobelin\"", "30", "2", "5"])
fig.arrow((X + W + 6, Y + 80), (a[0] - 6, a[1]), color=INK, width=2.5)
fig.arrow((X + W + 6, Y + 150), (b[0] - 6, b[1]), color=INK, width=2.5)
fig.text(480, 205, "instancier", size=14, weight=800, color=INK)
fig.text(770, 372, "même forme, chacun ses valeurs", size=13, weight=700, color=RED)

fig.save("poo01_declaration_instances", "POO-01 - Déclaration et instances")
