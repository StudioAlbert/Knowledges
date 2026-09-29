# -*- coding: utf-8 -*-
"""Schéma APU-09 — quatre autres machines à états courantes en jeu.

  00 images/apu09_autres_cas.svg
  Excalidraw/APU-09 - Autres cas d'usage.excalidraw.md

    python "tools/schemas/apu09_autres_cas.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1000, 360)
S = dict(w=118, h=36, size=14)


def title(x, y, s):
    fig.text(x, y, s, anchor="start", size=14, weight=800, color=RED)


# --------------------------------------------------------- Arme (haut gauche)
title(20, 24, "ARME")
a1 = fig.box(90, 70, "Prête", **S)
a2 = fig.box(290, 70, "Tir", **S)
a3 = fig.box(190, 150, "Rechargement", **S)
fig.arrow(a1, a2, "gâchette", size=12)
fig.arrow(a2, a3, "chargeur vide", size=12, label_dx=44, label_dy=0)
fig.arrow(a3, a1, "2 s", size=12, label_dx=-22, label_dy=8)

# --------------------------------------------------------- Garde (haut droite)
title(520, 24, "GARDE (IA)")
g1 = fig.box(600, 70, "Patrouille", **S)
g2 = fig.box(870, 70, "Alerte", **S)
g3 = fig.box(870, 150, "Poursuite", **S)
g4 = fig.box(600, 150, "Retour", **S)
fig.arrow(g1, g2, "bruit", size=12)
fig.arrow(g2, g3, "joueur vu", size=12, label_dx=40, label_dy=4)
fig.arrow(g3, g4, "joueur perdu", size=12, label_dy=-8)
fig.arrow(g4, g1, "au poste", size=12, label_dx=-40, label_dy=4)

fig.line([(20, 190), (980, 190)], GREY, 1, opacity=0.35)
fig.line([(500, 20), (500, 350)], GREY, 1, opacity=0.35)

# --------------------------------------------------------- Porte (bas gauche)
title(20, 218, "PORTE")
p1 = fig.box(90, 290, "Verrouillée", **S)
p2 = fig.box(260, 290, "Fermée", **S)
p3 = fig.box(430, 290, "Ouverte", **S)
fig.arrow(p1, p2, "clé", size=12)
fig.arrow(p2, p3, "E", bend=-22, size=12, label_dy=-6)
fig.arrow(p3, p2, "E", bend=-22, size=12, label_dy=22)

# --------------------------------------------------------- Partie (bas droite)
title(520, 218, "PARTIE")
f1 = fig.box(600, 262, "Menu", **S)
f2 = fig.box(870, 262, "En jeu", **S)
f3 = fig.box(735, 330, "Game over", **S)
fig.arrow(f1, f2, "Jouer", size=12)
fig.arrow(f2, f3, "PV = 0", size=12, label_dx=36, label_dy=4)
fig.arrow(f3, f1, "Entrée", size=12, label_dx=-40, label_dy=14)

fig.save("apu09_autres_cas", "APU-09 - Autres cas d'usage")
