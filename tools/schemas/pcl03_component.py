# -*- coding: utf-8 -*-
"""Schéma PCL-03 — Component.

Deux entités très différentes, faites des mêmes pièces. Ce qui se voit : `Vie`
et `Rendu` sont écrits une fois et servent aux deux, et la caisse n'hérite de
rien.

  00 images/pcl03_component.svg
  Excalidraw/PCL-03 - Component.excalidraw.md

    python "tools/schemas/pcl03_component.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)

PIECES = ["Vie", "Rendu", "Déplacement", "Tir", "Destructible"]
X0, PW, PH = 390, 220, 44
positions = {}

fig.text(X0 + PW / 2, 44, "LES PIÈCES, ÉCRITES UNE FOIS", size=14, weight=800, color=GREY)

for i, nom in enumerate(PIECES):
    y = 70 + i * 54
    fig.rect(X0, y, PW, PH, stroke=INK, fill="#ffffff", width=2.5, radius=10)
    fig.text(X0 + PW / 2, y + 28, nom, size=16, weight=700, color=INK)
    positions[nom] = (X0, X0 + PW, y + PH / 2)

ennemi = fig.box(165, 140, "Ennemi volant", w=230, h=62, active=True, size=17,
                 sub="aucune classe mère")
caisse = fig.box(165, 258, "Caisse", w=230, h=62, size=17, sub="aucune classe mère")

for nom in ("Vie", "Rendu", "Déplacement", "Tir"):
    g, _, y = positions[nom]
    fig.arrow((ennemi.cx + ennemi.w / 2, ennemi.cy), (g - 6, y), color=RED, width=2.5)

for nom in ("Vie", "Rendu", "Destructible"):
    g, _, y = positions[nom]
    fig.arrow((caisse.cx + caisse.w / 2, caisse.cy), (g - 6, y), color=INK, width=2.5, dash=True)

fig.text(860, 100, "« Vie » et « Rendu »", size=16, weight=800, color=INK)
fig.text(860, 124, "servent aux deux,", size=16, weight=800, color=INK)
fig.text(860, 148, "et sont écrits une fois.", size=16, weight=800, color=INK)

fig.rect(740, 200, 240, 76, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(860, 228, "une sixième pièce", size=15, weight=800, color=RED)
fig.text(860, 252, "n'ouvre aucun fichier", size=15, weight=800, color=RED)

fig.text(165, 312, "une entité = une liste de pièces", size=15, weight=800, color=SOFT)

fig.save("pcl03_component", "PCL-03 - Component")
