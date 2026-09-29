# -*- coding: utf-8 -*-
"""Schéma APU-05 — avant / après Observer : qui connaît qui quand le joueur perd un PV.

  00 images/apu05_couplage.svg
  Excalidraw/APU-05 - Couplage avant et après Observer.excalidraw.md

    python "tools/schemas/apu05_couplage.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 330)
S = dict(w=130, h=40, size=15)

# ------------------------------------------------------------ avant
fig.text(20, 30, "AVANT : PlayerHealth appelle tout le monde", anchor="start", size=15, weight=800, color=INK)
hp = fig.box(110, 175, "PlayerHealth", w=140, h=46, active=True)
targets = [("HUD", 60), ("Audio", 135), ("Caméra", 210), ("Succès", 285)]
for name, y in targets:
    b = fig.box(380, y, name, **S)
    fig.arrow(hp, b, color=RED, width=2.5)
fig.text(245, 322, "4 dépendances · ajouter un réacteur = modifier PlayerHealth", size=13, weight=600, color=RED)

fig.line([(500, 20), (500, 320)], GREY, 1, opacity=0.35)

# ------------------------------------------------------------ après
fig.text(520, 30, "APRÈS : PlayerHealth annonce, les autres écoutent", anchor="start", size=15, weight=800, color=INK)
hp2 = fig.box(590, 175, "PlayerHealth", w=140, h=46)
ev = fig.box(785, 175, "Damaged", w=110, h=46, active=True, sub="événement")
fig.arrow(hp2, ev, "annonce", label_dy=-16, color=INK)
for name, y in targets:
    b = fig.box(915, y, name, w=110, h=40, size=15)
    fig.arrow(b, ev, color=GREY, width=2)
fig.text(750, 322, "PlayerHealth ne connaît personne · chacun s'abonne", size=13, weight=600, color=INK)

fig.save("apu05_couplage", "APU-05 - Couplage avant et après Observer")
