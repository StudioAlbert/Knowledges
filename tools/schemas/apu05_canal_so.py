# -*- coding: utf-8 -*-
"""Schéma APU-05 — un canal d'événement en ScriptableObject relie deux scènes.

  00 images/apu05_canal_so.svg
  Excalidraw/APU-05 - Canal d'événement en ScriptableObject.excalidraw.md

    python "tools/schemas/apu05_canal_so.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 330)

# deux scènes et le projet au milieu
fig.rect(20, 40, 300, 270, stroke=GREY, fill=PALE, width=2, dash=True)
fig.text(35, 65, "SCÈNE Gameplay", anchor="start", size=14, weight=800, color=GREY)
fig.rect(680, 40, 300, 270, stroke=GREY, fill=PALE, width=2, dash=True)
fig.text(695, 65, "SCÈNE Interface", anchor="start", size=14, weight=800, color=GREY)
fig.text(500, 65, "PROJET (assets)", size=14, weight=800, color=GREY)

guard = fig.box(170, 130, "Garde", w=150)
cam = fig.box(170, 230, "Caméra de sécurité", w=210)
chan = fig.box(500, 180, "RaiseAlarm", w=170, h=56, active=True, sub="EventChannelFloatSO")
hud = fig.box(830, 110, "Jauge d'alerte", w=190)
snd = fig.box(830, 180, "Sirène", w=190)
mgr = fig.box(830, 250, "Journal de mission", w=190)

fig.arrow(guard, chan, "RaiseEvent(20)", label_dy=-14, color=INK)
fig.arrow(cam, chan, "RaiseEvent(5)", label_dy=22, color=INK)
for b in (hud, snd, mgr):
    fig.arrow(b, chan, color=GREY, width=2)
fig.text(695, 298, "abonnés : OnEventRaised +=", size=13, weight=600, color=GREY, anchor="start")
fig.text(500, 280, "les deux scènes connaissent l'asset,", size=13, weight=600, color=INK)
fig.text(500, 298, "jamais l'une l'autre", size=13, weight=700, color=RED)

fig.save("apu05_canal_so", "APU-05 - Canal d'événement en ScriptableObject")
