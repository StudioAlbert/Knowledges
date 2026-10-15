# -*- coding: utf-8 -*-
"""Schéma POO-06 — la hiérarchie des armes de la formative.

Trois niveaux : une base abstraite que personne n'instancie, l'étage qui porte ce
que seules les armes à feu partagent, et les deux armes à feu concrètes. `Melee`
descend directement de la base — un couteau ne recharge pas.

  00 images/poo06_hierarchie_armes.svg
  Excalidraw/POO-06 - Hierarchie des armes.excalidraw.md

    python "tools/schemas/poo06_hierarchie_armes.py"
"""
from schema_lib import Figure, RED, INK, GREY

fig = Figure(1000, 400)

HAUT, MILIEU, BAS = 70, 200, 320

weapon = fig.box(500, HAUT, "Weapon", w=300, h=58, muted=True,
                 sub="name_ damage_ weight_ · Fire() = 0")
fig.text(676, 76, "abstraite", anchor="start", size=14, weight=800, color=RED)

firearm = fig.box(310, MILIEU, "Firearm", w=300, h=58,
                  sub="caliber_ magazineCapacity_ · Reload()")
melee = fig.box(760, MILIEU, "Melee", w=260, h=58, sub="bladeLength_ · Swing()")

semi = fig.box(170, BAS, "SemiAutomatic", w=250, h=54, sub="SingleShotMode()")
full = fig.box(450, BAS, "FullAuto", w=270, h=54, sub="burstLength_ · FireFullAuto()")

for enfant, parent in ((firearm, weapon), (melee, weapon), (semi, firearm), (full, firearm)):
    fig.arrow(enfant, parent, color=GREY, width=2.2)

fig.text(500, 378, "Le menu ne tient que des Weapon : il appelle Fire(), l'objet décide.",
         size=15, weight=700, color=INK)

fig.save("poo06_hierarchie_armes", "POO-06 - Hierarchie des armes")
