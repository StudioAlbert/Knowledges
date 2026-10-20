# -*- coding: utf-8 -*-
"""Schéma PCL-04 — ce que coûte chaque nouvelle demande.

Pas le pire cas combinatoire : huit demandes **réelles**, toutes des classes de
Donjons et Dragons, posées l'une après l'autre sur une base de quatre classes.
Chacune oblige l'héritage à écrire une classe de plus et à recopier un
comportement qu'il possède déjà. La composition, elle, ne bouge qu'à la
huitième — parce que le Druide apporte une capacité qui n'existait pas encore.

  00 images/pcl04_croissance_classes.svg
  Excalidraw/PCL-04 - Croissance des classes.excalidraw.md

    python "tools/schemas/pcl04_croissance_classes.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1060, 400)

X0, X1, Y0, Y1 = 86, 614, 330, 64
XMAX, YMAX = 8.0, 14.0

# Les huit demandes, dans l'ordre où le game designer les pose.
CLASSES = [5, 6, 7, 8, 9, 10, 11, 12, 13]      # héritage : une classe de plus à chaque fois
COPIES = [0, 1, 2, 3, 4, 6, 7, 8, 8]           # comportements recopiés, cumulés
COMPOSANTS = [6, 6, 6, 6, 6, 6, 6, 6, 7]       # une capacité neuve, et une seule


def ecran(x, y):
    return (X0 + x / XMAX * (X1 - X0), Y0 - y / YMAX * (Y0 - Y1))


# --------------------------------------------------------------------- le repère
fig.line([(X0, Y0), (X1 + 12, Y0)], GREY, 2)
fig.line([(X0, Y0), (X0, Y1 - 12)], GREY, 2)
fig.text(X1, Y0 + 42, "demandes du game designer", anchor="end", size=13, weight=700, color=GREY)
fig.text(X0 - 12, Y1 - 16, "classes", anchor="end", size=13, weight=700, color=GREY)

for v in range(2, 15, 2):
    _, sy = ecran(0, v)
    fig.line([(X0 - 5, sy), (X1, sy)], GREY, 1, dash=True, opacity=0.3)
    fig.text(X0 - 10, sy + 5, str(v), anchor="end", size=12, weight=700, color=SOFT)

for v in range(0, 9):
    sx, _ = ecran(v, 0)
    fig.text(sx, Y0 + 20, str(v), size=12, weight=700, color=SOFT)

# --------------------------------------------------------------------- les courbes
fig.line([ecran(i, v) for i, v in enumerate(CLASSES)], RED, 3.5)
fig.line([ecran(i, v) for i, v in enumerate(COPIES)], RED, 2.5, dash=True, opacity=0.75)
fig.line([ecran(i, v) for i, v in enumerate(COMPOSANTS)], INK, 3.5)

for i, v in enumerate(CLASSES):
    fig.dot(*ecran(i, v), r=4, color=RED)
for i, v in enumerate(COMPOSANTS):
    fig.dot(*ecran(i, v), r=4, color=INK)

sx, sy = ecran(8, 13)
fig.text(sx - 6, sy - 14, "héritage : une classe de plus", anchor="end",
         size=15, weight=800, color=RED)
sx, sy = ecran(8, 8)
fig.text(sx - 6, sy - 13, "et le même code recopié", anchor="end",
         size=13, weight=700, color=RED)

# Le coin bas-droite du repère est vide : la composition s'y explique en deux lignes.
sx, sy = ecran(5.8, 2.2)
fig.text(sx, sy, "composition : un composant par capacité",
         size=15, weight=800, color=INK)
fig.text(sx, sy + 24, "+1 au Druide, qui apporte une capacité neuve",
         size=13, weight=700, color=SOFT)

sx, sy = ecran(8, 7)
fig.dot(sx, sy, 7, INK)

# --------------------------------------------------------------------- le compte
CX = 845
fig.text(CX, 82, "APRÈS HUIT DEMANDES RÉELLES", size=14, weight=800, color=GREY)

for i, (titre, chiffre, detail, couleur) in enumerate((
    ("Héritage", "13 classes", "dont 8 copies du même comportement", RED),
    ("Composition", "7 composants", "aucune copie, huit assemblages", INK),
)):
    y = 126 + i * 80
    fig.text(CX - 190, y, titre, anchor="start", size=15, weight=800, color=SOFT)
    fig.text(CX - 190, y + 30, chiffre, anchor="start", size=25, weight=800, color=couleur)
    fig.text(CX - 190, y + 52, detail, anchor="start", size=13, weight=700, color=SOFT)

fig.rect(CX - 200, 286, 400, 48, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(CX, 316, "« sorts arcaniques » : écrit 4 fois, puis 1 fois",
         size=16, weight=800, color=RED)

fig.text(CX, 362, "La composition ne grandit que sur une capacité nouvelle,",
         size=14, weight=700, color=INK)
fig.text(CX, 384, "jamais sur une combinaison nouvelle.",
         size=14, weight=700, color=INK)

fig.save("pcl04_croissance_classes", "PCL-04 - Croissance des classes")
