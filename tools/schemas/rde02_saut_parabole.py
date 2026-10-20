# -*- coding: utf-8 -*-
"""Schéma RDE-02 — le saut d'un platformer, en deux paraboles.

Un saut agréable n'est pas une parabole : c'en est **deux**. On monte avec une
gravité, on retombe avec une plus forte, et les deux morceaux se recollent au
sommet. Résoudre l'équation donne l'instant où le héros passe à huit mètres ;
le discriminant dit qu'à onze mètres il n'y passe jamais.

  00 images/rde02_saut_parabole.svg
  Excalidraw/RDE-02 - Saut en deux paraboles.excalidraw.md

    python "tools/schemas/rde02_saut_parabole.py"
"""
import math

from schema_lib import Figure, RED, INK, GREY, SOFT

fig = Figure(1040, 340)

X0, X1, Y0, Y1 = 86, 606, 288, 50
TMAX, HMAX = 1.8, 12.0

V0, G_MONTEE, G_CHUTE = 20.0, 20.0, 60.0
T_SOMMET = V0 / G_MONTEE                       # 1 s
H_SOMMET = V0 * T_SOMMET - G_MONTEE / 2 * T_SOMMET ** 2   # 10 m
T_FIN = T_SOMMET + math.sqrt(2 * H_SOMMET / G_CHUTE)      # 1,707 s


def h(t):
    if t <= T_SOMMET:
        return V0 * t - G_MONTEE / 2 * t * t
    return H_SOMMET - G_CHUTE / 2 * (t - T_SOMMET) ** 2


def ecran(t, hauteur):
    return (X0 + t / TMAX * (X1 - X0), Y0 - hauteur / HMAX * (Y0 - Y1))


# --------------------------------------------------------------------- le repère
fig.line([(X0, Y0), (X1 + 12, Y0)], GREY, 2)
fig.line([(X0, Y0), (X0, Y1 - 12)], GREY, 2)
fig.text(X1 + 16, Y0 + 5, "t (s)", anchor="start", size=13, weight=700, color=GREY)
fig.text(X0 - 12, Y1 - 16, "h (m)", anchor="end", size=13, weight=700, color=GREY)

for v in range(2, 13, 2):
    _, sy = ecran(0, v)
    fig.line([(X0 - 5, sy), (X1, sy)], GREY, 1, dash=True, opacity=0.28)
    fig.text(X0 - 10, sy + 5, str(v), anchor="end", size=12, weight=700, color=SOFT)

for v in (0.5, 1.0, 1.5):
    sx, _ = ecran(v, 0)
    fig.text(sx, Y0 + 20, str(v).replace(".", ","), size=12, weight=700, color=SOFT)

# --------------------------------------------------------------------- les deux moitiés
montee = [ecran(T_SOMMET * i / 120, h(T_SOMMET * i / 120)) for i in range(121)]
chute = [ecran(T_SOMMET + (T_FIN - T_SOMMET) * i / 120,
               h(T_SOMMET + (T_FIN - T_SOMMET) * i / 120)) for i in range(121)]
fig.line(montee, RED, 3.5)
fig.line(chute, INK, 3.5)

fig.text(ecran(0.22, 0)[0], ecran(0, 0.8)[1], "montée : g = 20", size=14, weight=800, color=RED)
fig.text(ecran(1.42, 0)[0], Y1 + 2, "chute : g = 60", size=14, weight=800, color=INK)

sx, sy = ecran(T_SOMMET, H_SOMMET)
fig.dot(sx, sy, 6, INK)
fig.text(sx, sy - 14, "sommet", size=13, weight=800, color=SOFT)

# --------------------------------------------------------------------- la plateforme
H_PLATEFORME = 8.0
# montee : V0 t - (g/2) t^2 = 8
T_A = (V0 - math.sqrt(V0 ** 2 - 2 * G_MONTEE * H_PLATEFORME)) / G_MONTEE
# chute : H_SOMMET - (g/2) (t - t_sommet)^2 = 8
T_B = T_SOMMET + math.sqrt(2 * (H_SOMMET - H_PLATEFORME) / G_CHUTE)

fig.line([ecran(0, 8), ecran(TMAX, 8)], INK, 2.5, dash=True)
fig.text(X1, ecran(0, 8)[1] - 10, "plateforme à 8 m", anchor="end",
         size=13, weight=800, color=INK)

for t in (T_A, T_B):
    sx, sy = ecran(t, 8)
    fig.dot(sx, sy, 6, RED)
    fig.text(sx, Y0 - 8, str(round(t, 2)).replace(".", ",") + " s",
             size=12, weight=800, color=RED)
    fig.line([(sx, sy), (sx, Y0 - 22)], RED, 1.5, dash=True, opacity=0.6)

fig.line([ecran(0, 11), ecran(TMAX, 11)], GREY, 2, dash=True)
fig.text(X0 + 10, ecran(0, 11)[1] - 9, "11 m : il n'y arrive jamais", anchor="start",
         size=13, weight=800, color=GREY)

# --------------------------------------------------------------------- le compte
CX = 840
fig.text(CX, 76, "UN SEUL EXEMPLE, ET IL SUFFIT", size=14, weight=800, color=GREY)

fig.text(CX - 180, 112, "h(t) = 20t − 10t²", anchor="start", size=17, weight=800,
         color=RED, mono=True, halo=False)
fig.text(CX - 180, 134, "tant qu'il monte", anchor="start", size=13, weight=700, color=SOFT)

fig.text(CX - 180, 172, "h(t) = 10 − 30(t − 1)²", anchor="start", size=17, weight=800,
         color=INK, mono=True, halo=False)
fig.text(CX - 180, 194, "une fois le sommet passé", anchor="start", size=13, weight=700,
         color=SOFT)

fig.rect(CX - 190, 216, 380, 50, stroke=RED, fill="#ffffff", width=2.5, radius=10)
fig.text(CX, 246, "au-dessus de 8 m pendant " + ("%.2f" % (T_B - T_A)).replace(".", ",") + " s",
         size=16, weight=800, color=RED)

fig.text(CX, 292, "À 11 m, Δ = −0,4 : l'équation n'a pas de solution,", size=14,
         weight=700, color=INK)
fig.text(CX, 314, "et le héros n'atteint pas la plateforme.", size=14, weight=700, color=INK)

fig.save("rde02_saut_parabole", "RDE-02 - Saut en deux paraboles")
