# -*- coding: utf-8 -*-
"""Schéma APU-09 — un QTE (quick time event) : le temps est une transition.

  00 images/apu09_qte.svg
  Excalidraw/APU-09 - QTE.excalidraw.md

    python "tools/schemas/apu09_qte.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 340)

play = fig.box(110, 160, "Cinématique", w=160)
prompt = fig.box(370, 160, "Invite", w=160, h=58, active=True, sub="touche A · 1,5 s")
win = fig.box(640, 70, "Réussite", w=150)
fail = fig.box(640, 250, "Échec", w=150)
next_ = fig.box(880, 70, "Suite", w=150)
retry = fig.box(880, 250, "Reprise", w=150)

fig.arrow(play, prompt, "moment clé", label_dy=-12)
fig.arrow(prompt, win)
fig.text(470, 100, "bonne touche à temps", size=13, weight=600, color=SOFT)
fig.arrow(prompt, fail, color=RED)
fig.text(470, 232, "temps écoulé", size=13, weight=700, color=RED)
fig.text(470, 250, "ou mauvaise touche", size=13, weight=600, color=SOFT)
fig.arrow(win, next_, "animation", label_dy=-10)
fig.arrow(fail, retry, "dégâts", label_dy=-10)
fig.arrow(retry, prompt, "on recommence", bend=90, dash=True, color=GREY, label_dy=20)
fig.arrow(next_, (975, 160), color=GREY, dash=True)
fig.text(975, 185, "invite 2…", size=13, weight=600, color=GREY, anchor="end")

fig.save("apu09_qte", "APU-09 - QTE")
