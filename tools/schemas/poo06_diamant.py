# -*- coding: utf-8 -*-
"""Schéma POO-06 — le diamant de l'héritage multiple, et sa sortie.

À gauche, deux parents qui descendent du même aïeul : l'enfant en reçoit les
données deux fois. À droite, la façon de s'en passer — une seule base porteuse de
données, et le second parent réduit à une interface, qui ne porte rien.

  00 images/poo06_diamant.svg
  Excalidraw/POO-06 - Diamant.excalidraw.md

    python "tools/schemas/poo06_diamant.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

VERT = "#2e9e5b"

fig = Figure(1000, 340)

W, H = 190, 50
HAUT, MILIEU, BAS = 66, 156, 250


def titre(cx, s):
    fig.text(cx, 26, s, size=14, weight=800, color=GREY)


def legende(cx, s, couleur):
    fig.text(cx, 322, s, size=15, weight=700, color=couleur)


# ---------------------------------------------------------------- le diamant
titre(240, "HÉRITAGE MULTIPLE — le diamant")

aieul = fig.box(240, HAUT, "Personnage", w=W, h=H, sub="pointsDeVie_")
comb = fig.box(110, MILIEU, "Combattant", w=170, h=44)
mage = fig.box(370, MILIEU, "Magicien", w=170, h=44)
pala = fig.box(240, BAS, "Paladin", w=W, h=H, sub="pointsDeVie_ deux fois")

for enfant, parent in ((comb, aieul), (mage, aieul), (pala, comb), (pala, mage)):
    fig.arrow(enfant, parent, color=GREY, width=2.2)

fig.text(240, 292, "quel pointsDeVie_ ? il y en a deux", size=14, weight=800, color=RED)
legende(240, "Chaque chemin apporte sa copie de l'aïeul.", INK)

# ---------------------------------------------------------------- la sortie
titre(740, "UNE BASE, ET UNE INTERFACE")

base = fig.box(640, HAUT, "Personnage", w=W, h=H, sub="pointsDeVie_")
inter = fig.box(870, HAUT, "Incantateur", w=180, h=H, muted=True, sub="virtuelle pure")
pal2 = fig.box(740, BAS, "Paladin", w=W, h=H, sub="pointsDeVie_ une fois")

fig.arrow(pal2, base, color=GREY, width=2.2)
fig.arrow(pal2, inter, color=VERT, width=2.2, dash=True)

legende(740, "L'interface ne porte aucune donnée : rien à dupliquer.", INK)

fig.line([(500, 44), (500, 300)], GREY, 1.5, dash=True, opacity=0.6)

fig.save("poo06_diamant", "POO-06 - Diamant")
