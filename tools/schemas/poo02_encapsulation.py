# -*- coding: utf-8 -*-
"""Schéma POO-02 — ce que l'objet montre, ce qu'il garde.

L'interface publique est la seule porte ; la donnée privée est inatteignable depuis
l'extérieur, et c'est ce qui permet à la règle du jeu de tenir.

  00 images/poo02_encapsulation.svg
  Excalidraw/POO-02 - Encapsulation.excalidraw.md

    python "tools/schemas/poo02_encapsulation.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1060, 390)

X, Y, W = 330, 60, 400
H_PUB, H_PRIV = 150, 115

# ------------------------------------------- l'objet : deux zones
fig.rect(X, Y, W, H_PUB + H_PRIV + 46, stroke=INK, fill="#ffffff", width=3, radius=12)
fig.rect(X, Y, W, 46, stroke=INK, fill=INK, width=3, radius=12)
fig.text(X + W / 2, Y + 30, "Joueur", size=20, weight=800, color="#ffffff", mono=True, halo=False)

# zone publique
fig.text(X + 24, Y + 78, "public:", anchor="start", size=15, weight=800, color=RED, mono=True, halo=False)
METHODES = ["subirDegats(int)", "soigner(int)", "estVivant()"]
for i, m in enumerate(METHODES):
    y = Y + 108 + i * 30
    fig.rect(X + 24, y - 19, W - 48, 26, stroke=RED, fill="#ffffff", width=1.8, radius=6)
    fig.text(X + 38, y, m, anchor="start", size=14, weight=700, color=INK, mono=True, halo=False)

# separation
fig.line([(X + 12, Y + H_PUB + 46), (X + W - 12, Y + H_PUB + 46)], GREY, 1.8, dash=True)

# zone privee
fig.rect(X + 12, Y + H_PUB + 54, W - 24, H_PRIV - 14, stroke=GREY, fill=PALE, width=1.8, radius=8)
fig.text(X + 24, Y + H_PUB + 82, "private:", anchor="start", size=15, weight=800, color=GREY, mono=True, halo=False)
# les deux champs tiennent sur une ligne : la boite reste dans le cadre de la slide
CHAMPS = [("int", "pointsDeVie_", 40), ("int", "pointsDeVieMax_", 210)]
for t, n, dx in CHAMPS:
    y = Y + H_PUB + 114
    fig.text(X + dx, y, t, anchor="start", size=14, weight=600, color=SOFT, mono=True, halo=False)
    fig.text(X + dx + 45, y, n, anchor="start", size=14, weight=800, color=INK, mono=True, halo=False)
fig.text(X + W / 2, Y + H_PUB + H_PRIV + 20, "0 ≤ pointsDeVie_ ≤ pointsDeVieMax_",
         size=13, weight=800, color=RED)

# ------------------------------------------- a gauche : l'appel qui passe
fig.text(150, 40, "LE RESTE DU JEU", size=13, weight=800, color=GREY)
fig.rect(30, 95, 240, 52, stroke=INK, fill="#ffffff", width=2, radius=8)
fig.text(150, 127, "joueur.subirDegats(9999)", size=14, weight=700, color=INK, mono=True, halo=False)
fig.arrow((272, 121), (X - 6, 121), color=INK, width=2.6)
fig.text(300, 100, "✔", size=22, weight=800, color=INK)
fig.text(150, 170, "passe par la porte", size=13, weight=700, color=SOFT)
fig.text(150, 190, "les dégâts sont bornés", size=13, weight=700, color=RED)

# ------------------------------------------- a gauche, plus bas : l'acces refuse
fig.rect(30, 268, 240, 52, stroke=GREY, fill=PALE, width=2, radius=8, dash=True)
fig.text(150, 300, "joueur.pointsDeVie_ = -50", size=14, weight=700, color=GREY, mono=True, halo=False)
fig.arrow((272, 294), (X - 30, 294), color=RED, width=2.6)
# la croix barre la pointe de la fleche : l'acces s'arrete la
fig.line([(X - 44, 280), (X - 16, 308)], RED, 4)
fig.line([(X - 16, 280), (X - 44, 308)], RED, 4)
fig.text(150, 343, "n'existe pas pour l'extérieur", size=13, weight=700, color=SOFT)
fig.text(150, 363, "erreur de compilation", size=13, weight=800, color=RED)

# ------------------------------------------- a droite : ce que ca achete
fig.text(880, 40, "CE QUE ÇA ACHÈTE", size=13, weight=800, color=GREY)
ACQUIS = ["la règle est écrite", "une seule fois,", "dans l'objet qui la porte",
          "", "le dedans peut changer", "sans casser le dehors"]
for i, ligne in enumerate(ACQUIS):
    fig.text(880, 100 + i * 26, ligne, size=14, weight=700 if i < 3 else 600,
             color=INK if i < 3 else SOFT)

fig.save("poo02_encapsulation", "POO-02 - Encapsulation")
