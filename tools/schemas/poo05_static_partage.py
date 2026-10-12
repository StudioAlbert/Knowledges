# -*- coding: utf-8 -*-
"""Schéma POO-05 — ce que `static` partage.

Trois objets, chacun avec son propre attribut, et une seule case qui n'appartient
à aucun d'eux : elle appartient à la classe.

  00 images/poo05_static_partage.svg
  Excalidraw/POO-05 - Static partage.excalidraw.md

    python "tools/schemas/poo05_static_partage.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 320)

W, H, Y = 250, 74, 56
STATIQUE_Y = 186


def boite(cx, y, w, h, titre, ligne, couleur, fond="#ffffff", sous_titre=None):
    x = cx - w / 2
    fig.rect(x, y, w, h, stroke=couleur, fill=fond, width=2.5, radius=10)
    fig.rect(x, y, w, 28, stroke=couleur, fill=couleur, width=2.5, radius=10)
    fig.text(cx, y + 20, titre, size=14, weight=800, color="#ffffff", mono=True, halo=False)
    fig.text(cx, y + 54, ligne, size=15, weight=700, color=INK, mono=True, halo=False)
    if sous_titre:
        fig.text(cx, y + h - 8, sous_titre, size=12, weight=700, color=couleur, halo=False)
    return (cx, y + h)


fig.text(20, 32, "TROIS OBJETS, CHACUN LE SIEN", anchor="start", size=14, weight=800, color=GREY)

bas = []
for cx, nom, pv in ((150, "gobelin", "pointsDeVie_ = 30"),
                    (420, "troll", "pointsDeVie_ = 120"),
                    (690, "dragon", "pointsDeVie_ = 400")):
    bas.append(boite(cx, Y, W, H, nom, pv, INK))

partage = boite(420, STATIQUE_Y, 320, 82, "Monstre::vivants_", "3", RED, fond=PALE,
                sous_titre="static : une seule case, pour toute la classe")

for cx, y in bas:
    fig.line([(cx, y), (cx, STATIQUE_Y - 18), (420, STATIQUE_Y - 18), (420, STATIQUE_Y)],
             RED, 2.2, arrow=True, dash=True)

fig.text(860, 232, "aucun objet", size=14, weight=800, color=SOFT)
fig.text(860, 252, "ne la possède", size=14, weight=800, color=SOFT)

fig.text(500, 304, "Détruire un objet ne touche pas la case partagée — c'est son constructeur "
                   "et son destructeur qui la tiennent à jour.",
         size=15, weight=700, color=INK)

fig.save("poo05_static_partage", "POO-05 - Static partage")
