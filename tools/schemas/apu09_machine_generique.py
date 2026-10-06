# -*- coding: utf-8 -*-
"""Schéma APU-09 — la machine générique : des transitions déclarées, pas écrites.

Montre la correspondance « une ligne de code = une flèche », et la transition
depuis n'importe quel état (`AddAnyTransition`), sur l'exemple du garde.

  00 images/apu09_machine_generique.svg
  Excalidraw/APU-09 - La machine generique.excalidraw.md

    python "tools/schemas/apu09_machine_generique.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1060, 400)

# ------------------------------------------------------- le graphe, à gauche
idle = fig.box(158, 110, "Idle")
patrol = fig.box(158, 250, "Patrouille")
alarm = fig.box(400, 180, "Alarme")
fig.start(idle, dx=-55)

fig.arrow(idle, patrol, "attente finie", bend=42, label_dx=-62, label_dy=4)
fig.arrow(patrol, idle, "point atteint", bend=42, label_dx=62, label_dy=2)

# la transition « depuis n'importe quel état » : une flèche par état, en rouge
fig.arrow(idle, alarm, color=RED, dash=True, width=2.5)
fig.arrow(patrol, alarm, "joueur vu", color=RED, dash=True, width=2.5,
          label_dx=14, label_dy=22)

fig.text(280, 60, "depuis n'importe quel état", size=14, weight=700, color=RED)

# ------------------------------------------------------- le code, à droite
X, Y = 540, 72
fig.rect(X, Y, 480, 212, stroke=GREY, fill=PALE, width=2, dash=False)

lines = [
    ("machine.ChangeState(idle);", INK),
    ("", INK),
    ("machine.AddTransition(idle, patrol, AttenteFinie);", INK),
    ("machine.AddTransition(patrol, idle, PointAtteint);", INK),
    ("machine.AddAnyTransition(alarm, JoueurVu);", RED),
]
for i, (s, color) in enumerate(lines):
    if s:
        fig.text(X + 22, Y + 40 + i * 34, s, anchor="start", size=15, weight=600,
                 color=color, mono=True, halo=False)

fig.text(X + 240, Y - 16, "ce qu'on écrit une fois, dans Awake", size=15, weight=700,
         color=SOFT)

# ------------------------------------------------------- la boucle, en bas
tick = fig.box(780, 332, "machine.Tick(dt)", w=260, h=44, size=15)
fig.text(780, 384, "chaque frame : la machine teste les conditions et change d'état seule",
         size=14, weight=600, color=GREY)
fig.arrow((780, Y + 212), tick, width=2.5, color=GREY)

fig.text(280, 332, "une ligne de code = une flèche", size=16, weight=700, color=SOFT)

fig.save("apu09_machine_generique", "APU-09 - La machine generique")
