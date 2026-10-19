# -*- coding: utf-8 -*-
"""Schéma PCL-03 — la carte des trois familles.

Trois colonnes, une question par colonne, et les patrons rangés dessous. Ceux
qu'on croise vraiment dans un jeu sont en rouge ; les autres sont là pour que la
carte soit complète, pas pour être appris.

  00 images/pcl03_trois_familles.svg
  Excalidraw/PCL-03 - Trois familles.excalidraw.md

    python "tools/schemas/pcl03_trois_familles.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 340)

COL_W, X0, GAP = 310, 24, 16

FAMILLES = [
    ("CRÉATION", "Qui décide quel objet naît ?",
     [("Factory Method", False), ("Abstract Factory", False), ("Builder", False),
      ("Prototype", False), ("Singleton", False), ("Object Pool", True)]),
    ("STRUCTURE", "Comment des objets s'emboîtent ?",
     [("Adapter", False), ("Composite", False), ("Decorator", False),
      ("Facade", False), ("Proxy", False), ("Component", True)]),
    ("COMPORTEMENT", "Comment se répartir une décision ?",
     [("Observer", True), ("State", True), ("Strategy", True),
      ("Command", True), ("Iterator", False), ("Visitor", False)]),
]

for i, (titre, question, patrons) in enumerate(FAMILLES):
    x = X0 + i * (COL_W + GAP)
    fig.rect(x, 30, COL_W, 276, stroke=INK, fill="#ffffff", width=2.5, radius=10)
    fig.rect(x, 30, COL_W, 34, stroke=INK, fill=INK, width=2.5, radius=10)
    fig.text(x + COL_W / 2, 53, titre, size=15, weight=800, color="#ffffff", halo=False)
    fig.text(x + COL_W / 2, 86, question, size=13.5, weight=700, color=SOFT)

    for j, (nom, en_jeu) in enumerate(patrons):
        y = 108 + j * 32
        fig.rect(x + 18, y, COL_W - 36, 26, stroke=RED if en_jeu else "#e2e2e2",
                 fill=PALE if en_jeu else "#ffffff", width=2 if en_jeu else 1.5, radius=5)
        fig.text(x + COL_W / 2, y + 18, nom, size=13.5,
                 weight=800 if en_jeu else 600, color=RED if en_jeu else GREY,
                 mono=True, halo=False)

fig.text(500, 328, "En rouge, les six qu'on croise vraiment dans un jeu. "
                   "Les autres sont sur la carte, pas au programme.",
         size=14.5, weight=700, color=INK)

fig.save("pcl03_trois_familles", "PCL-03 - Trois familles")
