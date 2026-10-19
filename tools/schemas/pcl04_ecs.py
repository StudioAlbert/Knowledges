# -*- coding: utf-8 -*-
"""Schéma PCL-04 — le principe de l'ECS.

Des entités qui ne sont qu'un numéro, des composants rangés par type dans des
tableaux sans trou, et sous chaque tableau la flèche du système qui le balaie.
Le tableau dense est tout l'argument : la donnée suivante est déjà dans la ligne
de cache.

  00 images/pcl04_ecs.svg
  Excalidraw/PCL-04 - ECS.excalidraw.md

    python "tools/schemas/pcl04_ecs.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

BLEU, VERT = "#2b6cb0", "#2e9e5b"

fig = Figure(1000, 330)

X0, CELL_W, CELL_H = 230, 54, 30


def cellules(y, etiquettes, couleur, fond):
    for i, e in enumerate(etiquettes):
        x = X0 + i * CELL_W
        fig.rect(x, y, CELL_W, CELL_H, stroke=couleur, fill=fond, width=2, radius=4)
        fig.text(x + CELL_W / 2, y + 20, e, size=13, weight=700, color=couleur,
                 mono=True, halo=False)
    return X0 + len(etiquettes) * CELL_W


# ----------------------------------------------------------------- les entités
fig.text(20, 30, "ENTITÉS — un numéro, rien d'autre", anchor="start", size=13,
         weight=800, color=GREY)
fin = cellules(40, ["1", "2", "3", "4", "5", "6"], INK, "#ffffff")
fig.text(fin + 18, 60, "pas de code, pas de données", anchor="start", size=13,
         weight=700, color=SOFT)

# ---------------------------------------- les composants, et qui les parcourt
fig.text(20, 108, "COMPOSANTS — un tableau par type, sans trou", anchor="start",
         size=13, weight=800, color=GREY)

for nom, ids, couleur, y, systeme, note in (
        ("Position", ["1", "2", "3", "4", "5", "6"], BLEU, 120, "Rendu", None),
        ("Vitesse", ["1", "2", "4", "6"], VERT, 194, "Déplacement",
         "3 et 5 ne bougent pas : ils n'y sont pas")):
    fig.text(X0 - 14, y + 20, nom, anchor="end", size=14, weight=800, color=couleur,
             mono=True, halo=False)
    fin = cellules(y, ids, couleur, PALE)
    if note:
        fig.text(fin + 18, y + 20, note, anchor="start", size=13, weight=700, color=SOFT)
    # le balayage se dessine sous son tableau : c'est là qu'est la donnée
    fig.line([(X0, y + CELL_H + 14), (fin, y + CELL_H + 14)], couleur, 2.2, arrow=True)
    fig.text(fin + 18, y + CELL_H + 19,
             "%s balaie les %d, d'affilée" % (systeme, len(ids)),
             anchor="start", size=13.5, weight=800, color=couleur)

fig.text(500, 312, "La donnée suivante est déjà dans la ligne de cache : "
                   "c'est tout ce que l'ECS achète.",
         size=15, weight=700, color=INK)

fig.save("pcl04_ecs", "PCL-04 - ECS")
