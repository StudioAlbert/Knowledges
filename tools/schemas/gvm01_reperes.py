# -*- coding: utf-8 -*-
"""Schéma GVM-01 — trois trièdres : Unity, Unreal et le repère mathématique usuel.

La même lettre garde la même couleur dans les trois panneaux : ce qui change d'un moteur
à l'autre, c'est le rôle que cette lettre joue — et la main qui décrit la rotation.

  00 images/gvm01_reperes.svg
  Excalidraw/GVM-01 - Reperes directs et indirects.excalidraw.md

    python "tools/schemas/gvm01_reperes.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

AX, AY, AZ = RED, "#2e9e5b", "#2b6cb0"   # x, y, z — couleurs des gizmos des éditeurs

fig = Figure(1140, 390)

OY = 200          # ligne des origines
L = 95            # longueur d'un axe dans le plan
D = 52            # longueur d'un axe en profondeur (projeté en diagonale)

PANELS = [
    ("UNITY", 190, "main gauche", [
        ("x", AX, (L, 0), "droite"),
        ("y", AY, (0, -L), "haut"),
        ("z", AZ, (D, -D), "avant"),
    ], "1 unité = 1 m"),
    ("UNREAL", 570, "main gauche", [
        ("y", AY, (L, 0), "droite"),
        ("z", AZ, (0, -L), "haut"),
        ("x", AX, (D, -D), "avant"),
    ], "1 unité = 1 cm"),
    ("MATHS, OPENGL", 950, "main droite", [
        ("x", AX, (L, 0), "droite"),
        ("y", AY, (0, -L), "haut"),
        ("z", AZ, (-D, D), "vers vous"),
    ], "1 unité = 1 unité"),
]

for i, (titre, cx, main, axes, unite) in enumerate(PANELS):
    fig.text(cx, 46, titre, size=14, weight=800, color=GREY)
    fig.dot(cx, OY, 6, INK)
    for nom, couleur, (dx, dy), role in axes:
        tx, ty = cx + dx, OY + dy
        fig.line([(cx, OY), (tx, ty)], couleur, 3.5, arrow=True)
        # la lettre au bout de l'axe, son rôle juste dessous ; l'axe qui descend
        # vers l'observateur se fait légender à sa gauche, sinon il percute la pastille
        if dx < 0:
            lx, ly, anchor = tx - 10, ty + 4, "end"
        elif dx > 0:
            lx, ly, anchor = tx + 24, ty + 6, "middle"
        else:
            lx, ly, anchor = tx, ty - 14, "middle"
        fig.text(lx, ly, nom, anchor=anchor, size=18, weight=800, color=couleur, mono=True)
        fig.text(lx, ly + 17, role, anchor=anchor, size=12, weight=600, color=SOFT)
    # la main, et l'unité du moteur
    droite = main.endswith("droite")
    fig.rect(cx - 78, 296, 156, 32, stroke=INK if droite else RED,
             fill="#ffffff", width=2.5, radius=16)
    fig.text(cx, 318, main, size=15, weight=800, color=INK if droite else RED, halo=False)
    fig.text(cx, 352, unite, size=13, weight=600, color=GREY, mono=True)
    if i:
        fig.line([(cx - 190, 62), (cx - 190, 364)], "#e5e5e5", 1.5, dash=True)

fig.text(570, 382, "Règle de la main : pouce = x, index = y, majeur = z — "
                   "si les trois tiennent avec la main droite, le repère est direct.",
         size=13, weight=700, color=INK)

fig.save("gvm01_reperes", "GVM-01 - Reperes directs et indirects")
