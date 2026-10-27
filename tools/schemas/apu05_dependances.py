# -*- coding: utf-8 -*-
"""Schéma APU-05 — les dépendances du companion, avant et après l'atelier.

Mêmes blocs des deux côtés : seules les flèches changent de nature, et celle du
bouton ne change pas du tout.

  00 images/apu05_dependances.svg
  Excalidraw/APU-05 - Dependances du companion.excalidraw.md

    python "tools/schemas/apu05_dependances.py"
"""
from schema_lib import Figure, RED, INK, GREY

fig = Figure(1080, 395)


def half(x0, titre, chaud):
    """Pose les cinq blocs d'un côté, toujours au même endroit."""
    fig.text(x0 + 5, 32, titre, anchor="start", size=15, weight=800, color=INK)
    return dict(
        hud=fig.box(x0 + 450, 130, "HUD", w=100, h=40, size=15),
        item=fig.box(x0 + 55, 200, "Item", w=100, h=42, size=15),
        manager=fig.box(x0 + 300, 200, "ItemManager", w=150, h=46, active=chaud),
        panel=fig.box(x0 + 450, 270, "EndPanel", w=110, h=40, size=15),
        button=fig.box(x0 + 70, 305, "ResetButton", w=130, h=40, size=15),
    )


def cablage(c, aller, vers_hud, vers_panneau, couleur, dash):
    """Les cinq flèches, toujours dans le même sens.

    Deux restent noires des deux côtés — la liste que le gestionnaire assume, et
    le bouton qui a le droit de piloter le jeu. Les trois autres changent.
    """
    fig.arrow(c["item"], c["manager"], aller, color=couleur, dash=dash,
              bend=24, label_dy=22)
    fig.arrow(c["manager"], c["hud"], vers_hud, color=couleur, dash=dash, label_dx=-16)
    fig.arrow(c["manager"], c["panel"], vers_panneau, color=couleur, dash=dash,
              label_dx=-18, label_dy=16)
    fig.arrow(c["manager"], c["item"], "liste items", color=INK, bend=24, label_dy=-14)
    fig.arrow(c["button"], c["manager"], "ResetItems()", color=INK,
              label_dx=36, label_dy=14)


# ------------------------------------------------------------ avant
a = half(10, "AVANT — branche 01-depart", True)
cablage(a, "ItemCollected()", "champ", "champ", RED, False)
fig.text(20, 372, "Tout est un champ : ajouter un son = rouvrir ItemManager.",
         anchor="start", size=13, weight=600, color=RED)

fig.line([(545, 20), (545, 378)], GREY, 1, opacity=0.35)

# ------------------------------------------------------------ après
b = half(570, "APRÈS — branche main", False)
cablage(b, "1 · Collected", "3 · canal", "2 · UnityEvent", GREY, True)
fig.text(580, 372, "1 event Collected · 2 UnityEvent · 3 canal GemmesRestantes",
         anchor="start", size=13, weight=600, color=INK)

fig.save("apu05_dependances", "APU-05 - Dependances du companion")
