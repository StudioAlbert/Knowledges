# -*- coding: utf-8 -*-
"""Schéma APU-09 — le tour par tour : chaque tour est un état, les unités suivent.

  00 images/apu09_tour_par_tour.svg
  Excalidraw/APU-09 - Tour par tour.excalidraw.md

    python "tools/schemas/apu09_tour_par_tour.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 360)

fig.text(20, 30, "LE JEU", anchor="start", size=13, weight=800, color=GREY)
start = fig.box(120, 95, "Début de manche", w=160)
player = fig.box(345, 95, "Tour du joueur", w=160, active=True)
enemy = fig.box(570, 95, "Tour ennemi", w=160)
end = fig.box(795, 95, "Fin de manche", w=160)
over = fig.box(795, 190, "Fin de partie", w=160)
fig.start(start, dx=-30)

fig.arrow(start, player)
fig.arrow(player, enemy)
fig.text(457, 130, "toutes ont joué", size=12, weight=600, color=SOFT)
fig.arrow(enemy, end)
fig.text(677, 130, "toutes ont joué", size=12, weight=600, color=SOFT)
fig.arrow(end, over, "un camp vide", label_dx=55, label_dy=6)
fig.arrow(end, start, "sinon", bend=62, label_dy=-6)

fig.text(20, 232, "CHAQUE UNITÉ", anchor="start", size=13, weight=800, color=GREY)
wait = fig.box(160, 290, "En attente", w=150)
act = fig.box(400, 290, "Active", w=150)
done = fig.box(640, 290, "A joué", w=150)
fig.arrow(wait, act)
fig.arrow(act, done, "action choisie", label_dy=-10)
fig.arrow(done, wait, bend=-38)

# Le jeu pilote les unités : en entrant dans un tour, il réveille son camp
fig.arrow((345, 120), (280, 285), color=RED, dash=True, width=2)
fig.text(330, 190, "OnEnter : son camp", size=13, weight=700, color=RED)
fig.text(330, 206, "→ Active", size=13, weight=700, color=RED)
fig.arrow((765, 120), (412, 318), color=RED, dash=True, width=2)
fig.text(575, 172, "OnEnter : tout le monde", size=13, weight=700, color=RED, anchor="end")
fig.text(575, 188, "→ En attente", size=13, weight=700, color=RED, anchor="end")

fig.save("apu09_tour_par_tour", "APU-09 - Tour par tour")
