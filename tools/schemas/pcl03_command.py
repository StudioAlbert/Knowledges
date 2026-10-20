# -*- coding: utf-8 -*-
"""Schéma PCL-03 — Command.

L'action devient un objet, et une fois qu'elle est un objet on peut l'empiler.
La pile d'annulation est le dessin : quatre actions posées, et le Ctrl+Z qui
remonte en appelant `Undo` dans l'autre sens.

  00 images/pcl03_command.svg
  Excalidraw/PCL-03 - Command.excalidraw.md

    python "tools/schemas/pcl03_command.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)

fig.text(60, 44, "LA PILE D'ANNULATION", anchor="start", size=14, weight=800, color=GREY)

actions = ["Poser un mur", "Poser une tour", "Vendre la tour", "Poser un mur"]
boites = []
for i, nom in enumerate(actions):
    dernier = i == len(actions) - 1
    b = fig.box(160 + i * 225, 110, nom, w=200, h=62, size=15, active=dernier,
                sub="Execute / Undo")
    boites.append(b)
    if i:
        fig.arrow(boites[i - 1], b, color=GREY, width=2)

fig.arrow((boites[3].cx, 158), (boites[0].cx, 158), "Ctrl+Z appelle Undo, dans l'autre sens",
          color=RED, width=3, bend=-46, label_dy=30, label_color=RED, size=15)

fig.rect(60, 250, 400, 60, stroke=INK, fill="#ffffff", width=2.5, radius=10)
fig.text(260, 276, "l'action existe sans celui qui la demande", size=15, weight=800, color=INK)
fig.text(260, 298, "ni celui qui l'exécute", size=14, weight=700, color=SOFT)

fig.text(740, 268, "la même boîte derrière une touche,", size=15, weight=700, color=INK)
fig.text(740, 290, "un bouton ou un script : c'est le remapping.",
         size=15, weight=700, color=INK)

fig.save("pcl03_command", "PCL-03 - Command")
