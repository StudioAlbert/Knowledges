# -*- coding: utf-8 -*-
"""Schéma GVM-02 — la normale d'un triangle, et le côté qu'elle décide.

Deux fois le même triangle, vu en 3D. À gauche les sommets sont lus A, B, C ;
à droite C, B, A. Les deux arêtes et le produit vectoriel sont dessinés : la
normale se retourne, et la face devient invisible.

  00 images/gvm02_normale_3d.svg
  Excalidraw/GVM-02 - Normale d'un triangle.excalidraw.md

    python "tools/schemas/gvm02_normale_3d.py"
"""
import math
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

VERT, BLEU = "#2e9e5b", "#2b6cb0"

# ---------------------------------------------------------------- projection
def rot_x(a):
    c, s = math.cos(a), math.sin(a)
    return ((1, 0, 0), (0, c, -s), (0, s, c))

def rot_y(a):
    c, s = math.cos(a), math.sin(a)
    return ((c, 0, s), (0, 1, 0), (-s, 0, c))

def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def apply(M, p):
    return tuple(sum(M[i][k] * p[k] for k in range(3)) for i in range(3))

VUE = mul(rot_y(math.radians(34)), rot_x(math.radians(-24)))

def proj(p, cx, cy, ech=1.0):
    """Orthographique : on garde x et y de la vue, z ne sert qu'à l'ordre."""
    v = apply(VUE, p)
    return (cx + v[0] * ech, cy - v[1] * ech)

# ---------------------------------------------------------------- le dessin
fig = Figure(1180, 400)

A, B, C = (-1.2, -0.8, 0.9), (1.5, -0.6, 0.4), (0.1, 1.3, -0.9)
ECH = 78

def triangle(cx, cy, ordre, titre, couleur_titre, sens_normale, mention, remplissage):
    P = {nom: proj(pt, cx, cy, ECH) for nom, pt in (("A", A), ("B", B), ("C", C))}
    s0, s1, s2 = ordre
    pts = {"A": A, "B": B, "C": C}

    # le sol, pour que la 3D se lise
    sol = [proj((x, -1.4, z), cx, cy, ECH) for x, z in ((-2, -2), (2, -2), (2, 2), (-2, 2))]
    fig.line(sol + [sol[0]], "#ededed", 1.4)

    # la face, remplie selon qu'elle est vue de face ou de dos
    poly = [P[s0], P[s1], P[s2]]
    fig.line(poly + [poly[0]], INK, 2.6, fill=remplissage)

    # les deux aretes qui servent au calcul, depuis le premier sommet
    fig.line([P[s0], P[s1]], VERT, 4, arrow=True)
    fig.line([P[s0], P[s2]], BLEU, 4, arrow=True)

    # la normale, au centre de gravite
    g = tuple(sum(pts[n][i] for n in ordre) / 3 for i in range(3))
    # produit vectoriel des deux aretes, dans l'ordre lu
    e1 = tuple(pts[s1][i] - pts[s0][i] for i in range(3))
    e2 = tuple(pts[s2][i] - pts[s0][i] for i in range(3))
    n = (e1[1]*e2[2] - e1[2]*e2[1], e1[2]*e2[0] - e1[0]*e2[2], e1[0]*e2[1] - e1[1]*e2[0])
    ln = math.sqrt(sum(c * c for c in n)) or 1
    n = tuple(c / ln * 1.5 for c in n)
    fig.line([proj(g, cx, cy, ECH), proj(tuple(g[i] + n[i] for i in range(3)), cx, cy, ECH)],
             RED, 4.5, arrow=True)
    # le libelle se decale sur le cote de la fleche : vers le bas il tombait
    # sinon dans la legende
    bout = proj(tuple(g[i] + n[i] * 1.1 for i in range(3)), cx, cy, ECH)
    base_n = proj(g, cx, cy, ECH)
    dx, dy = bout[0] - base_n[0], bout[1] - base_n[1]
    d = math.hypot(dx, dy) or 1
    fig.text(bout[0] - dy / d * 20, bout[1] + dx / d * 20 + 5, "n",
             size=19, weight=800, color=RED, mono=True)

    for nom in ordre:
        p = P[nom]
        fig.dot(p[0], p[1], 5, INK)
    # les etiquettes de sommets, ecartees du centre
    for nom in ("A", "B", "C"):
        p, c = P[nom], proj(g, cx, cy, ECH)
        dx, dy = p[0] - c[0], p[1] - c[1]
        d = math.hypot(dx, dy) or 1
        fig.text(p[0] + dx / d * 22, p[1] + dy / d * 22 + 5, nom, size=16, weight=800, color=INK)

    fig.text(cx, 44, titre, size=15, weight=800, color=couleur_titre)
    fig.text(cx, 338, sens_normale, size=14, weight=800, color=RED)
    fig.text(cx, 362, mention, size=13, weight=700, color=SOFT)

triangle(300, 195, ("A", "B", "C"), "SOMMETS LUS A → B → C", INK,
         "n sort vers vous", "la face est visible", "#eef4ee")
triangle(880, 195, ("A", "C", "B"), "SOMMETS LUS A → C → B", RED,
         "n part derrière", "la face est éliminée — backface culling", PALE)

fig.line([(590, 70), (590, 320)], "#e5e5e5", 1.5, dash=True)

fig.text(300, 392, "n = (B \u2212 A) \u00d7 (C \u2212 A)", size=14, weight=800, color=INK, mono=True)
fig.text(880, 392, "n = (C \u2212 A) \u00d7 (B \u2212 A)", size=14, weight=800, color=INK, mono=True)

fig.save("gvm02_normale_3d", "GVM-02 - Normale d'un triangle")
