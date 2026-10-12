# -*- coding: utf-8 -*-
"""Schéma POO-04 — l'ordre d'initialisation des membres.

En haut la liste d'initialisation telle qu'on l'écrit, en bas l'ordre qui a
vraiment lieu, celui de la déclaration. Les deux ne coïncident pas : les flèches
se croisent, et le membre initialisé en premier lit celui qui n'existe pas encore.

  00 images/poo04_ordre_initialisation.svg
  Excalidraw/POO-04 - Ordre d initialisation.excalidraw.md

    python "tools/schemas/poo04_ordre_initialisation.py"
"""
from schema_lib import Figure, RED, INK, GREY

# Même format très large et court que les autres figures de slide : c'est ce que
# le cadre laisse sous un titre et une ligne de légende.
fig = Figure(1000, 330)

BOX_W, BOX_H = 390, 56
GAUCHE, DROITE = 250, 740
HAUT, BAS = 52, 212


def bande(titre, y_titre, y, couleur, cases):
    # Le titre se pose à gauche, dans la bande blanche que les flèches laissent.
    fig.text(20, y_titre, titre, anchor="start", size=14, weight=800, color=GREY)
    centres = []
    for cx, rang, code in cases:
        fig.rect(cx - BOX_W / 2, y, BOX_W, BOX_H, stroke=couleur, fill="#ffffff",
                 width=2.5, radius=10)
        fig.dot(cx - BOX_W / 2, y + BOX_H / 2, 15, couleur)
        fig.text(cx - BOX_W / 2, y + BOX_H / 2 + 6, rang, size=16, weight=800,
                 color="#ffffff", halo=False)
        fig.text(cx - BOX_W / 2 + 32, y + BOX_H / 2 + 6, code, anchor="start", size=15,
                 weight=700, color=INK, mono=True, halo=False)



bande("CE QUE VOUS ÉCRIVEZ — la liste d'initialisation", 36, HAUT, GREY, [
    (GAUCHE, "1", "pointsDeVieMax_(max)"),
    (DROITE, "2", "pointsDeVie_(pointsDeVieMax_)"),
])

bande("CE QUI A LIEU — l'ordre de déclaration des membres", 176, BAS, INK, [
    (GAUCHE, "1", "int pointsDeVie_;"),
    (DROITE, "2", "int pointsDeVieMax_;"),
])

# Le même membre, en haut et en bas : les deux liaisons se croisent.
fig.line([(GAUCHE, HAUT + BOX_H), (DROITE, BAS)], GREY, 2.2, dash=True, arrow=True)
fig.line([(DROITE, HAUT + BOX_H), (GAUCHE, BAS)], RED, 2.6, arrow=True)

fig.text(500, 308, "1 initialise pointsDeVie_ à partir de pointsDeVieMax_, "
                   "qui ne sera construit qu'en 2.",
         size=15, weight=700, color=RED)

fig.save("poo04_ordre_initialisation", "POO-04 - Ordre d initialisation")
