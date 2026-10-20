# -*- coding: utf-8 -*-
"""Schéma RDE-03 — composer deux fonctions, en trois graphes.

Le même exemple que le formatif : une distance entre dans `f`, qui la ramène
entre 0 et 1 ; ce résultat entre dans `g`, qui en fait des dégâts. Le troisième
graphe est la composée, et c'est elle qu'on branche dans le jeu.

  00 images/rde03_composition.svg
  Excalidraw/RDE-03 - Composer.excalidraw.md

    python "tools/schemas/rde03_composition.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1040, 340)

PH = 152          # hauteur utile d'un graphe
BASE = 262        # ligne des abscisses
LARG = 250

PANNEAUX = [
    dict(x=52, titre="f : la distance, ramenée entre 0 et 1",
         formule="t = clamp((d − 0,25) / 4,75 ; 0 ; 1)",
         xlab="d (m)", ylab="t", couleur=INK),
    dict(x=394, titre="g : de 0 et 1 vers des dégâts",
         formule="g(t) = 25 (1 − t)",
         xlab="t", ylab="dégâts", couleur=INK),
    dict(x=736, titre="g ∘ f : ce qu'on branche dans le jeu",
         formule="dégâts(d) = g(f(d))",
         xlab="d (m)", ylab="dégâts", couleur=RED),
]


def courbe(p, points, couleur, epaisseur=3.2):
    fig.line([(p["x"] + a * LARG, BASE - b * PH) for a, b in points], couleur, epaisseur)


for p in PANNEAUX:
    x = p["x"]
    fig.text(x, 48, p["titre"], anchor="start", size=14, weight=800, color=GREY)
    fig.text(x, 76, p["formule"], anchor="start", size=14, weight=700,
             color=p["couleur"], mono=True, halo=False)
    fig.line([(x, BASE), (x + LARG + 10, BASE)], GREY, 2)
    fig.line([(x, BASE), (x, BASE - PH - 10)], GREY, 2)
    fig.text(x + LARG + 14, BASE + 5, p["xlab"], anchor="start", size=12,
             weight=700, color=SOFT)
    fig.text(x - 8, BASE - PH - 14, p["ylab"], anchor="end", size=12,
             weight=700, color=SOFT)

# f : palier a 0, rampe, palier a 1 — les distances vont de 0 a 6 m
D = 6.0
courbe(PANNEAUX[0], [(0, 0), (0.25 / D, 0), (5 / D, 1), (1, 1)], INK)
fig.text(PANNEAUX[0]["x"] + 0.25 / D * LARG, BASE + 20, "0,25", size=12, weight=700, color=SOFT)
fig.text(PANNEAUX[0]["x"] + 5 / D * LARG, BASE + 20, "5", size=12, weight=700, color=SOFT)
fig.text(PANNEAUX[0]["x"] - 8, BASE - PH + 5, "1", anchor="end", size=12, weight=700, color=SOFT)

# g : une droite descendante
courbe(PANNEAUX[1], [(0, 1), (1, 0)], INK)
fig.text(PANNEAUX[1]["x"] - 8, BASE - PH + 5, "25", anchor="end", size=12, weight=700, color=SOFT)
fig.text(PANNEAUX[1]["x"] + LARG, BASE + 20, "1", size=12, weight=700, color=SOFT)

# la composee : plateau, descente, zero
courbe(PANNEAUX[2], [(0, 1), (0.25 / D, 1), (5 / D, 0), (1, 0)], RED, 3.6)
fig.text(PANNEAUX[2]["x"] + 0.25 / D * LARG, BASE + 20, "0,25", size=12, weight=700, color=SOFT)
fig.text(PANNEAUX[2]["x"] + 5 / D * LARG, BASE + 20, "5", size=12, weight=700, color=SOFT)
fig.text(PANNEAUX[2]["x"] - 8, BASE - PH + 5, "25", anchor="end", size=12, weight=700, color=SOFT)

# les deux passages
for i in (0, 1):
    a = PANNEAUX[i]["x"] + LARG + 30
    b = PANNEAUX[i + 1]["x"] - 20
    fig.arrow((a, BASE - PH / 2), (b, BASE - PH / 2), width=2.5, color=RED)
    fig.text((a + b) / 2, BASE - PH / 2 - 14, "puis", size=13, weight=800, color=RED)

fig.text(52, 312, "L'image de f tient dans le domaine de g : c'est la seule condition pour composer.",
         anchor="start", size=15, weight=800, color=INK)
fig.text(736, 312, "f monte, g descend : la composée descend.", anchor="start",
         size=14, weight=700, color=SOFT)

fig.save("rde03_composition", "RDE-03 - Composer")
