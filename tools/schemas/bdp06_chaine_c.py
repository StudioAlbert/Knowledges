# -*- coding: utf-8 -*-
"""Schéma BDP-06 — une chaîne de caractères à la C, case par case en mémoire.

  00 images/bdp06_chaine_c.svg
  Excalidraw/BDP-06 - Chaîne de caractères en mémoire.excalidraw.md

Slide « Historique de la chaîne de caractères ».

    python "tools/schemas/bdp06_chaine_c.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 280)
word = "Sebastien"
cells = list(word) + ["\\0"]
X0, Y, CW, CH = 95, 120, 84, 96

# le pointeur : l'adresse du premier caractère
fig.rect(20, 18, 190, 44, stroke=INK, fill="#ffffff", width=2.5)
fig.text(115, 46, "const char* nom", size=16, weight=700, mono=True)
fig.arrow((115, 64), (X0 + CW / 2, Y - 6), color=RED, width=3)
fig.text(250, 50, "nom ne contient qu'une adresse : celle de la 1ʳᵉ case", anchor="start",
         size=14, weight=600, color=RED)

for i, c in enumerate(cells):
    x = X0 + i * CW
    end = (c == "\\0")
    fig.rect(x, Y, CW, CH, stroke=RED if end else INK, fill="#fdeaea" if end else "#ffffff",
             width=3 if end else 2.5, radius=0)
    fig.text(x + CW / 2, Y + 44, "'%s'" % c, size=24, weight=800, color=RED if end else INK, mono=True)
    code = 0 if end else ord(c)
    fig.text(x + CW / 2, Y + 78, str(code), size=16, weight=600, color=RED if end else GREY, mono=True)
    fig.text(x + CW / 2, Y + CH + 24, "[%d]" % i, size=13, weight=600, color=SOFT, mono=True)

fig.text(X0 - 12, Y + 44, "caractère", anchor="end", size=13, weight=700, color=SOFT)
fig.text(X0 - 12, Y + 78, "code ASCII", anchor="end", size=13, weight=700, color=SOFT)
fig.text(X0 - 12, Y + CH + 24, "indice", anchor="end", size=13, weight=700, color=SOFT)

xe = X0 + 9 * CW + CW / 2
fig.text(xe, Y + CH + 50, "caractère de fin", size=14, weight=800, color=RED)
fig.text(X0 + 4.5 * CW, Y + CH + 50, "9 lettres → 10 cases", size=14, weight=700, color=INK)

fig.save("bdp06_chaine_c", "BDP-06 - Chaîne de caractères en mémoire")
