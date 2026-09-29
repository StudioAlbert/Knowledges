# -*- coding: utf-8 -*-
"""Schéma BDP-06 — l'aller-retour nombre ↔ texte, et ce qui fait échouer le retour.

  00 images/bdp06_to_string_stoi.svg
  Excalidraw/BDP-06 - to_string et stoi.excalidraw.md

    python "tools/schemas/bdp06_to_string_stoi.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 320)

num = fig.box(190, 140, "int pv = 42", w=220, h=70, size=20)
fig.text(190, 200, "une valeur : on peut calculer", size=13, weight=600, color=SOFT)

X0, Y, CW, CH = 650, 105, 60, 70
for i, c in enumerate(["'4'", "'2'"]):
    fig.rect(X0 + i * CW, Y, CW, CH, stroke=INK, width=2.5, radius=0)
    fig.text(X0 + i * CW + CW / 2, Y + 44, c, size=20, weight=800, mono=True, halo=False)
fig.text(X0 + CW, Y - 14, "std::string \"42\"", size=15, weight=800, mono=True)
fig.text(X0 + CW, 200, "deux caractères : on peut afficher", size=13, weight=600, color=SOFT)

fig.line([(310, 115), (480, 95), (636, 115)], INK, 3, arrow=True)
fig.text(475, 82, "std::to_string(pv)", size=16, weight=800, mono=True)
fig.text(475, 128, "réussit toujours", size=12, weight=600, color=SOFT)

fig.line([(636, 168), (480, 188), (310, 168)], RED, 3, arrow=True)
fig.text(475, 212, "std::stoi(texte)", size=16, weight=800, color=RED, mono=True)
fig.text(475, 164, "peut échouer", size=12, weight=700, color=RED)

fig.line([(40, 240), (960, 240)], GREY, 1, opacity=0.35)
fig.text(40, 266, "LE RETOUR ÉCHOUE", anchor="start", size=13, weight=800, color=RED)
fails = [('"abc"', "invalid_argument"), ('""', "invalid_argument"),
         ('"99999999999"', "out_of_range")]
for k, (inp, exc) in enumerate(fails):
    x = 230 + k * 250
    fig.text(x, 266, inp, anchor="start", size=15, weight=800, mono=True)
    fig.text(x, 290, "→ " + exc, anchor="start", size=13, weight=700, color=RED, mono=True)
fig.text(40, 312, "piège : stoi(\"42abc\") rend 42 sans erreur — il s'arrête au premier caractère non chiffre",
         anchor="start", size=13, weight=600, color=SOFT)

fig.save("bdp06_to_string_stoi", "BDP-06 - to_string et stoi")
