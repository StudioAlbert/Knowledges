# -*- coding: utf-8 -*-
"""Schéma BDP-06 — ce qu'il y a dans une std::string : un char* bien gardé.

  00 images/bdp06_std_string.svg
  Excalidraw/BDP-06 - Ce qu'il y a dans une std string.excalidraw.md

    python "tools/schemas/bdp06_std_string.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 320)

# l'objet std::string
fig.text(20, 30, "L'OBJET  std::string nom", anchor="start", size=13, weight=800, color=GREY)
fig.rect(20, 45, 250, 170, stroke=INK, fill="#ffffff", width=3)
rows = [("pointeur", "●", RED), ("taille", "9", INK), ("capacité", "15", INK)]
for k, (name, val, col) in enumerate(rows):
    y = 60 + k * 50
    fig.rect(35, y, 220, 40, stroke=GREY, fill=PALE, width=1.5, radius=4)
    fig.text(50, y + 26, name, anchor="start", size=15, weight=700, color=SOFT)
    fig.text(235, y + 27, val, anchor="end", size=18, weight=800, color=col, mono=True, halo=False)

# le tampon de caractères
fig.text(360, 30, "LE TEXTE, GÉRÉ PAR L'OBJET", anchor="start", size=13, weight=800, color=GREY)
cells = list("Sebastien") + ["\\0"] + [""] * 6
X0, Y, CW, CH = 360, 55, 38, 50
for i, c in enumerate(cells):
    x = X0 + i * CW
    spare = c == ""
    end = c == "\\0"
    fig.rect(x, Y, CW, CH, stroke=GREY if spare else (RED if end else INK),
             fill=PALE if spare else "#ffffff", width=1.5 if spare else 2.2, dash=spare, radius=0)
    if c:
        fig.text(x + CW / 2, Y + 32, c, size=17 if not end else 14, weight=800,
                 color=RED if end else INK, mono=True, halo=False)
fig.text(X0 + 4.5 * CW, Y + CH + 22, "taille = 9 : connue, jamais recomptée", size=13, weight=700, color=INK)
fig.text(X0 + 13 * CW, Y + CH + 22, "place en réserve", size=13, weight=700, color=GREY)
fig.line([(X0, Y + CH + 32), (X0 + 9 * CW, Y + CH + 32)], INK, 1.5)
fig.line([(X0 + 10 * CW, Y + CH + 32), (X0 + 16 * CW, Y + CH + 32)], GREY, 1.5, dash=True)

fig.arrow((255, 80), (X0 - 4, Y + 25), color=RED, width=2.5)

# ce que l'objet offre en échange
fig.text(360, 190, "CE QUE L'OBJET GARANTIT", anchor="start", size=13, weight=800, color=GREY)
items = [("+  +=", "il grandit tout seul"),
         ("=  ==", "copie et comparaison du texte, pas de l'adresse"),
         ("at()", "vérifie l'indice avant de lire"),
         ("c_str()", "rend le const char* pour les fonctions C")]
for k, (code, txt) in enumerate(items):
    y = 218 + k * 26
    fig.text(360, y, code, anchor="start", size=15, weight=800, color=RED, mono=True)
    fig.text(460, y, txt, anchor="start", size=14, weight=600, color=INK)

fig.text(145, 245, "3 champs, toujours à jour", size=13, weight=700, color=SOFT)
fig.text(145, 265, "le ~string() libère la mémoire", size=13, weight=700, color=SOFT)

fig.save("bdp06_std_string", "BDP-06 - Ce qu'il y a dans une std string")
