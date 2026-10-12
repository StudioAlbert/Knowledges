# -*- coding: utf-8 -*-
"""Schéma POO-03 — la connaissance réciproque de deux classes.

À gauche l'inclusion croisée : chacun doit être lu avant l'autre, et la garde
casse la boucle en laissant une déclaration manquante. À droite la sortie :
un seul vrai include, et une annonce en face, qui suffit à un pointeur.

  00 images/poo03_connaissance_reciproque.svg
  Excalidraw/POO-03 - Connaissance reciproque.excalidraw.md

    python "tools/schemas/poo03_connaissance_reciproque.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT

VERT = "#2e9e5b"

# Format très large et court : la figure est seule sur sa slide, sous un titre et
# une ligne de légende, donc le cadre lui laisse environ 1030 x 325. Coller à ce
# rapport est ce qui rend son texte lisible au projecteur.
fig = Figure(1000, 330)

BOX_W, HAUT, BAS = 360, 46, 182
H2 = 36 + 2 * 24 + 12          # bandeau + deux lignes de code + respiration
SEPARATEUR = 505


def fichier(cx, y, nom, accent, lignes):
    """Une boîte de fichier : bandeau nommé, puis ses lignes en chasse fixe."""
    x = cx - BOX_W / 2
    fig.rect(x, y, BOX_W, H2, stroke=INK, fill="#ffffff", width=2.5, radius=10)
    fig.rect(x, y, BOX_W, 30, stroke=INK, fill=INK, width=2.5, radius=10)
    fig.text(x + 16, y + 21, nom, anchor="start", size=16, weight=800, color="#ffffff",
             mono=True, halo=False)
    for i, (txt, fort) in enumerate(lignes):
        fig.text(x + 20, y + 54 + i * 24, txt, anchor="start", size=15,
                 weight=800 if fort else 600, color=accent if fort else SOFT,
                 mono=True, halo=False)
    return y + H2 / 2


def panneau(cx, titre, lignes_haut, lignes_bas, couleur, retour_pointille,
            etiquette_descend, etiquette_monte, verdict, legende):
    fig.text(cx, 26, titre, size=14, weight=800, color=GREY)
    cy_haut = fichier(cx, HAUT, 'joueur.h', couleur, lignes_haut)
    cy_bas = fichier(cx, BAS, 'arme.h', couleur, lignes_bas)

    bord, canal = BOX_W / 2, BOX_W / 2 + 36
    fig.line([(cx + bord, cy_haut), (cx + canal, cy_haut), (cx + canal, cy_bas),
              (cx + bord, cy_bas)], couleur, 2.4, arrow=True)
    fig.line([(cx - bord, cy_bas), (cx - canal, cy_bas), (cx - canal, cy_haut),
              (cx - bord, cy_haut)], couleur, 2.4, arrow=True, dash=retour_pointille)
    # Les étiquettes se posent à l'origine de leur flèche, faute de place dans le
    # couloir vertical.
    fig.text(cx + bord + 6, cy_haut - 12, etiquette_descend, anchor="start", size=13,
             weight=700, color=couleur)
    fig.text(cx - bord - 6, cy_bas - 12, etiquette_monte, anchor="end", size=13,
             weight=700, color=couleur)

    fig.text(cx, (cy_haut + cy_bas) / 2 + 7, verdict, size=20, weight=800, color=couleur)
    fig.text(cx, 312, legende, size=15, weight=700, color=INK)


panneau(
    248, "L'INCLUSION CROISÉE",
    [('#include "arme.h"', True), ('class Joueur { Arme arme_; };', False)],
    [('#include "joueur.h"', True), ('class Arme { Joueur* joueur_; };', False)],
    RED, False, "inclut", "inclut", "ne compile pas",
    "Chacun doit être lu avant l'autre — une déclaration manque toujours.",
)

panneau(
    752, "LA DÉCLARATION ANTICIPÉE",
    [('#include "arme.h"', True), ('class Joueur { Arme arme_; };', False)],
    [('class Joueur;', True), ('class Arme { Joueur* joueur_; };', False)],
    VERT, True, "inclut", "annonce", "compile",
    "Un seul vrai include ; en face, une annonce suffit à un pointeur.",
)

fig.line([(SEPARATEUR, 40), (SEPARATEUR, 290)], GREY, 1.5, dash=True, opacity=0.6)

fig.save("poo03_connaissance_reciproque", "POO-03 - Connaissance reciproque")
