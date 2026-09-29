# -*- coding: utf-8 -*-
"""Schéma APU-09 — la navigation dans l'interface est une machine à états.

  00 images/apu09_ui_navigation.svg
  Excalidraw/APU-09 - Navigation d'interface.excalidraw.md

    python "tools/schemas/apu09_ui_navigation.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)
W = 124

title = fig.box(70, 165, "Écran titre", w=W)
menu = fig.box(245, 165, "Menu", w=W)
options = fig.box(245, 50, "Options", w=W)
levels = fig.box(430, 165, "Choix niveau", w=W)
loading = fig.box(615, 165, "Chargement", w=W)
game = fig.box(800, 165, "En jeu", w=W, active=True)
pause = fig.box(800, 285, "Pause", w=W)

fig.arrow(title, menu, "Entrée", label_dy=-10)
fig.arrow(menu, options, "Options", bend=-26, label_dx=-40)
fig.arrow(options, menu, "Retour", bend=-26, label_dx=40)
fig.arrow(menu, levels, "Jouer", label_dy=-10)
fig.arrow(levels, menu, "Retour", bend=-34, label_dy=26)
fig.arrow(levels, loading, "choisi", label_dy=-10)
fig.arrow(loading, game, "prêt", label_dy=-10)
fig.arrow(game, pause, "Échap", bend=-24, label_dx=-46)
fig.arrow(pause, game, "Échap", bend=-24, label_dx=46)
fig.arrow(pause, menu, "Quitter", bend=-60, label_dy=26)

fig.text(600, 60, "un écran = un état", size=15, weight=700, color=INK)
fig.text(600, 82, "un bouton = une transition", size=15, weight=700, color=RED)

fig.save("apu09_ui_navigation", "APU-09 - Navigation d'interface")
