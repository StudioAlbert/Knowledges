# -*- coding: utf-8 -*-
"""Schéma PCL-03 — Observer.

Un sujet qui ne connaît personne, et quatre abonnés qui réagissent. Le point du
dessin : les flèches partent toutes du même côté, et en ajouter une cinquième
n'ouvre pas la boîte de gauche.

  00 images/pcl03_observer.svg
  Excalidraw/PCL-03 - Observer.excalidraw.md

    python "tools/schemas/pcl03_observer.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)

sujet = fig.box(180, 150, "Points de vie", w=230, h=66, active=True, size=18,
                sub="le sujet : il émet")

abonnes = ["Barre de vie", "Son de dégât", "Animation de recul", "Succès « survivant »"]
boites = []
for i, nom in enumerate(abonnes):
    boites.append(fig.box(760, 52 + i * 68, nom, w=290, h=50, size=15))

for b in boites:
    fig.arrow(sujet, b, color=RED, width=2.5)

fig.text(470, 32, "prévient ses abonnés", size=15, weight=800, color=RED)

fig.text(180, 232, "il ne sait pas qui l'écoute,", size=15, weight=700, color=INK)
fig.text(180, 254, "ni combien ils sont", size=15, weight=700, color=INK)

fig.rect(40, 276, 420, 44, stroke=INK, fill="#ffffff", width=2.5, radius=10)
fig.text(250, 304, "un cinquième abonné n'ouvre pas la boîte de gauche",
         size=15, weight=800, color=INK)

fig.text(760, 310, "chacun s'abonne et se désabonne seul", size=13, weight=700, color=SOFT)

fig.save("pcl03_observer", "PCL-03 - Observer")
