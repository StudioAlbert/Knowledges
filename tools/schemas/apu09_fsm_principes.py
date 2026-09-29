# -*- coding: utf-8 -*-
"""Schéma APU-09 — principes d'une machine à états : le héros d'un platformer.

  00 images/apu09_fsm_principes.svg
  Excalidraw/APU-09 - Principes d'une machine à états.excalidraw.md

    python "tools/schemas/apu09_fsm_principes.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)

idle = fig.box(150, 175, "Idle")
run = fig.box(400, 80, "Course", active=True)
jump = fig.box(650, 80, "Saut")
fall = fig.box(650, 265, "Chute")
fig.start(idle)

fig.arrow(idle, run, "déplacement", bend=-28, label_dx=-38, label_dy=-4)
fig.arrow(run, idle, "arrêt", bend=-28, label_dx=26, label_dy=18)
fig.arrow(run, jump, "bouton saut")
fig.arrow(jump, fall, "vitesse y < 0", label_dx=58, label_dy=4)
fig.arrow(run, fall, "plus de sol", label_dx=-30, label_dy=14)
fig.arrow(fall, idle, "au sol", bend=-40, label_dy=22)

# ----------------------------------------------------------- légende
X = 800
fig.dot(X + 10, 70, 7)
fig.text(X + 30, 76, "état initial", anchor="start", size=15, weight=600, color=SOFT)
fig.rect(X, 100, 26, 20, stroke=INK)
fig.text(X + 38, 116, "un état", anchor="start", size=15, weight=600, color=SOFT)
fig.rect(X, 140, 26, 20, stroke=RED, fill=RED)
fig.text(X + 38, 156, "l'état courant", anchor="start", size=15, weight=600, color=SOFT)
fig.text(X + 38, 176, "— un seul à la fois", anchor="start", size=13, weight=500, color=GREY)
fig.line([(X, 212), (X + 28, 212)], INK, 2.5, arrow=True)
fig.text(X + 38, 218, "une transition", anchor="start", size=15, weight=600, color=SOFT)
fig.text(X + 38, 238, "— et sa condition", anchor="start", size=13, weight=500, color=GREY)

fig.save("apu09_fsm_principes", "APU-09 - Principes d'une machine à états")
