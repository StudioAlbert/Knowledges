# -*- coding: utf-8 -*-
"""Schéma PCL-03 — Strategy.

L'ennemi ne tient pas trois `if`, il tient **un objet**. Les trois façons de se
comporter sont interchangeables derrière la même interface, et le code de
l'ennemi ne change jamais.

  00 images/pcl03_strategy.svg
  Excalidraw/PCL-03 - Strategy.excalidraw.md

    python "tools/schemas/pcl03_strategy.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)

ennemi = fig.box(180, 110, "Ennemi", w=220, h=66, size=18, sub="le contexte")
interface = fig.box(560, 110, "ComportementIA", w=280, h=66, muted=True, size=18,
                    sub="Decider(cible)")

fig.arrow(ennemi, interface, "tient un", label_dy=-12, color=RED, width=3)

strategies = ["Foncer", "Garder ses distances", "Fuir"]
for i, nom in enumerate(strategies):
    b = fig.box(240 + i * 300, 268, nom, w=250, h=50, size=16)
    fig.arrow(b, interface, color=GREY, width=2, dash=True)

fig.text(560, 196, "trois mises en œuvre, une seule signature", size=14, weight=700, color=SOFT)

fig.rect(760, 24, 230, 76, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(875, 52, "à 20 % de vie,", size=15, weight=800, color=RED)
fig.text(875, 76, "on échange l'objet", size=15, weight=800, color=RED)

fig.text(180, 196, "son code ne change jamais", size=15, weight=800, color=INK)

fig.save("pcl03_strategy", "PCL-03 - Strategy")
