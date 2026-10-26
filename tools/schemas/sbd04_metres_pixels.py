# -*- coding: utf-8 -*-
"""Schéma SBD-04 — deux mondes, deux unités.

L'écran compte en pixels, Box2D en mètres. Le même héros vaut 180 d'un côté et
1,8 de l'autre, et c'est **un seul nombre** qui fait le passage. Oublier ce
nombre ne produit pas une erreur : ça produit un personnage qui tombe comme un
immeuble.

  00 images/sbd04_metres_pixels.svg
  Excalidraw/SBD-04 - Metres et pixels.excalidraw.md

    python "tools/schemas/sbd04_metres_pixels.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1040, 340)

SOL = 238


def monde(x0, titre, unite, hauteur_px, etiquette, couleur):
    fig.text(x0 + 140, 56, titre, size=15, weight=800, color=GREY)
    fig.rect(x0, 74, 280, 190, stroke=GREY, fill=PALE, width=2, radius=12)
    fig.line([(x0 + 14, SOL), (x0 + 266, SOL)], INK, 3)
    fig.text(x0 + 266, SOL + 18, "le sol", anchor="end", size=12, weight=700, color=SOFT)

    larg = hauteur_px * 0.42
    fig.rect(x0 + 140 - larg / 2, SOL - hauteur_px, larg, hauteur_px,
             stroke=couleur, fill="#ffffff", width=3, radius=8)
    fig.text(x0 + 140, SOL - hauteur_px - 14, etiquette, size=17, weight=800, color=couleur)
    fig.text(x0 + 140, 96, unite, size=13, weight=700, color=SOFT)


monde(70, "L'ÉCRAN", "tout est en pixels", 150, "180 px", INK)
monde(690, "BOX2D", "tout est en mètres", 150, "1,8 m", RED)

# ------------------------------------------------------------------ le passage
fig.arrow((360, 150), (680, 150), width=3, color=RED)
fig.arrow((680, 196), (360, 196), width=3, color=INK)

fig.rect(400, 92, 240, 48, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(520, 122, "1 m = 100 px", size=20, weight=800, color=RED, mono=True)

fig.text(520, 176, "Metres(pixels) = pixels / 100", size=14, weight=700,
         color=SOFT, mono=True, halo=False)
fig.text(520, 222, "Pixels(metres) = metres * 100", size=14, weight=700,
         color=SOFT, mono=True, halo=False)

fig.text(520, 262, "un seul nombre, écrit une seule fois", size=14, weight=800, color=INK)

# ------------------------------------------------------------------ l'oubli
fig.rect(70, 284, 900, 44, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(520, 312,
         "Oublier la conversion : un héros de 180 mètres, une gravité qui paraît nulle, "
         "des forces sans effet.",
         size=15, weight=800, color=RED)

fig.save("sbd04_metres_pixels", "SBD-04 - Metres et pixels")
