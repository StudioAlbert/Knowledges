# -*- coding: utf-8 -*-
"""Schéma PCL-01 — la direction des dépendances.

Deux projets réels du dépôt SAE-Geneve. À gauche SpaceShooter, tout à plat :
une classe au centre qui connaît tout le monde. À droite CityBuilder, en trois
couches : les flèches ne vont que vers l'intérieur, et jamais l'inverse.

  00 images/pcl01_direction_dependances.svg
  Excalidraw/PCL-01 - Direction des dependances.excalidraw.md

    python "tools/schemas/pcl01_direction_dependances.py"
"""
import math

from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

VERT = "#2e9e5b"

fig = Figure(1000, 340)

fig.text(20, 30, "À PLAT — SpaceShooter", anchor="start", size=14, weight=800, color=GREY)
fig.text(560, 30, "EN COUCHES — CityBuilder", anchor="start", size=14, weight=800, color=GREY)

# ------------------------------------------------- a gauche : tout au centre
CX, CY = 250, 160
centre = fig.box(CX, CY, "StarshipPlayer", w=190, h=48, active=True)

VOISINS = ["sf::RenderWindow", "Motor", "ProjectileManager", "AutoEntity", "sf::Texture", "EntityManager"]
for i, nom in enumerate(VOISINS):
    a = -math.pi / 2 + 2 * math.pi * i / len(VOISINS)
    x, y = CX + 185 * math.cos(a), CY + 108 * math.sin(a)
    b = fig.box(x, y, nom, w=152, h=34, size=12)
    fig.arrow(centre, b, color=RED, width=2)

fig.text(250, 304, "Six dépendances, une seule classe : tout changement la traverse.",
         size=14.5, weight=700, color=RED)

# ------------------------------------------- a droite : trois couches gigognes
COUCHES = [
    ("game", 560, 62, 420, 66, "game.cc"),
    ("api", 596, 136, 348, 66, "ui · motion · resources · graphics"),
    ("core", 632, 210, 276, 60, "maths · a_star · bt_node"),
]
for nom, x, y, w, h, contenu in COUCHES:
    fig.rect(x, y, w, h, stroke=INK, fill=PALE if nom == "core" else "#ffffff",
             width=2.5, radius=10)
    fig.text(x + 14, y + 24, nom + "/", anchor="start", size=15, weight=800,
             color=INK, mono=True, halo=False)
    fig.text(x + 14, y + 48, contenu, anchor="start", size=12.5, weight=700, color=SOFT)

for y0, y1 in ((128, 136), (202, 210)):
    fig.line([(770, y0), (770, y1 + 6)], VERT, 2.6, arrow=True)

fig.text(960, 104, "dépend de", anchor="end", size=12.5, weight=700, color=VERT)
fig.text(960, 178, "dépend de", anchor="end", size=12.5, weight=700, color=VERT)

fig.text(770, 304, "Les flèches ne remontent jamais : core ignore qu'api existe.",
         size=14.5, weight=700, color=VERT)

fig.line([(510, 48), (510, 288)], GREY, 1.5, dash=True, opacity=0.6)

fig.save("pcl01_direction_dependances", "PCL-01 - Direction des dependances")
