# -*- coding: utf-8 -*-
"""Schéma GTE-02 — le cycle d'une pull request.

  00 images/gte02_pull_request.svg
  Excalidraw/GTE-02 - Cycle d'une pull request.excalidraw.md

    python "tools/schemas/gte02_pull_request.py"
"""
from schema_lib import Figure, RED, INK, GREY, SOFT, PALE

fig = Figure(1000, 330)
S = dict(w=150, h=52, size=15)

fig.text(20, 28, "CHEZ VOUS", anchor="start", size=13, weight=800, color=GREY)
fig.text(330, 28, "SUR GITHUB", anchor="start", size=13, weight=800, color=GREY)
fig.line([(305, 20), (305, 310)], GREY, 1, opacity=0.35)

branch = fig.box(150, 90, "Branche", sub="git switch -c", **S)
push = fig.box(150, 210, "Push", sub="git push -u origin", **S)
pr = fig.box(420, 210, "PR ouverte", sub="titre + description", **S)
review = fig.box(640, 210, "Revue", sub="commentaires", active=True, **S)
ok = fig.box(860, 210, "Approuvée", sub="Approve", **S)
merge = fig.box(860, 90, "Fusionnée", sub="Merge pull request", **S)
fix = fig.box(640, 90, "Correction", sub="commit + push", **S)

fig.arrow(branch, push, "commits", label_dx=-40, label_dy=4)
fig.arrow(push, pr, "Compare & pull request", label_dy=44, size=12)
fig.arrow(pr, review, "relecteur", label_dy=44, size=12)
fig.arrow(review, ok)
fig.arrow(ok, merge)
fig.arrow(review, fix, "Request changes", color=RED, bend=-30, label_dx=-62, label_dy=0)
fig.arrow(fix, review, "la PR se met à jour", color=GREY, bend=-30, label_dx=70, label_dy=0)
fig.text(860, 40, "puis on supprime la branche", size=13, weight=600, color=SOFT)
fig.text(640, 290, "on boucle jusqu'à l'approbation", size=13, weight=700, color=RED)

fig.save("gte02_pull_request", "GTE-02 - Cycle d'une pull request")
