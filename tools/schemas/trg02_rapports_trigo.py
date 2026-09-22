# -*- coding: utf-8 -*-
"""Schéma TRG-02 — rapports trigonométriques (opposé, adjacent, hypoténuse).

Une seule description de la figure, deux sorties :

  00 images/trg02_rapports_trigo.svg                        affiché dans le deck
  Excalidraw/TRG-02 - Rapports trigonométriques.excalidraw.md  source éditable

Le SVG est la version publiée : la slide l'embarque par `![[trg02_rapports_trigo.svg]]`
sous `<!-- .slide: class="schema" -->`. Le .excalidraw.md permet de rouvrir le dessin
dans Obsidian pour le retoucher à la main — mais une retouche faite là n'est pas
reportée dans le SVG : rejouer ce script écrase les deux fichiers.

Repères de mise en page : la figure est dessinée dans un canevas `W × H` ; pour tenir
dans le cadre blanc d'une slide 1280×720 **sans titre H2**, garder H/W ≈ 0,37
(1000 × 372 ici). Avec un titre, compter ~60 px de moins.

Usage :

    python "tools/schemas/trg02_rapports_trigo.py"
"""
import io, json, math, os, random, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RED, INK, GREY, SOFT = "#E30613", "#1a1a1a", "#6e6e6e", "#555"
W, H = 1000, 372

els = []          # (kind, payload)


def line(pts, color=INK, width=3, dash=False, opacity=1.0):
    els.append(("line", dict(pts=[(float(x), float(y)) for x, y in pts],
                             color=color, width=width, dash=dash, opacity=opacity)))


def arc(cx, cy, r, a0, a1, color=RED, width=2):
    """Angles en degres, sens trigo, y vers le bas."""
    n = 24
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    line(pts, color, width)


def dot(x, y, r=5, color=INK):
    els.append(("dot", dict(x=float(x), y=float(y), r=r, color=color)))


def text(x, y, s, anchor="middle", size=17, weight=600, color=INK):
    """(x, y) = point d'ancrage et ligne de base, comme en SVG."""
    els.append(("text", dict(x=float(x), y=float(y), s=s, anchor=anchor,
                             size=size, weight=weight, color=color)))


def right_angle(v, u1, u2, s=18, color=INK):
    """Petit carre d'angle droit au sommet v, vers les directions u1 et u2."""
    def unit(u):
        n = math.hypot(*u)
        return (u[0] / n * s, u[1] / n * s)
    a, b = unit(u1), unit(u2)
    line([(v[0] + a[0], v[1] + a[1]),
          (v[0] + a[0] + b[0], v[1] + a[1] + b[1]),
          (v[0] + b[0], v[1] + b[1])], color, 2)


# ----------------------------------------------------------------- bandeau
text(175, 30, "sin α = opposé / hypoténuse", size=18, weight=700, color=INK)
text(500, 30, "cos α = adjacent / hypoténuse", size=18, weight=700, color=INK)
text(830, 30, "tan α = opposé / adjacent", size=18, weight=700, color=INK)
text(W / 2, 54, "S O H   ·   C A H   ·   T O A", size=14, weight=600, color=GREY)
line([(40, 70), (960, 70)], SOFT, 1, opacity=0.35)

BASE, APEX, WID = 296, 168, 200


def triangle(ox, tag):
    """Triangle rectangle : A en bas a gauche, B angle droit, C en haut."""
    A = (ox, BASE)
    B = (ox + WID, BASE)
    C = (ox + WID, APEX)
    line([A, B], GREY if tag == "alpha" else RED, 4)          # adjacent / oppose
    line([B, C], RED if tag == "alpha" else GREY, 4)          # oppose / adjacent
    line([C, A], INK, 4)                                       # hypotenuse
    right_angle(B, (-1, 0), (0, -1), s=16)
    return A, B, C


# --------------------------------------------------- 1 : vu depuis alpha
A1, B1, C1 = triangle(70, "alpha")
text(170, 100, "1 · vu depuis α", size=16, weight=700, color=INK)
arc(A1[0], A1[1], 42, 0, 33)
text(A1[0] + 54, A1[1] - 12, "α", size=18, weight=700, color=RED)
text(A1[0] + 85, (BASE + APEX) / 2 - 22, "hypoténuse", size=15, weight=700, color=INK)
text(170, 322, "adjacent", size=15, weight=700, color=GREY)
text(B1[0] + 10, (BASE + APEX) / 2 + 6, "opposé", anchor="start", size=15, weight=700, color=RED)
text(170, 340, "les côtés se nomment", size=14, weight=600, color=SOFT)
text(170, 362, "depuis l'angle choisi", size=14, weight=600, color=SOFT)

# ---------------------------------------------------- 2 : vu depuis beta
A2, B2, C2 = triangle(390, "beta")
text(490, 100, "2 · vu depuis β", size=16, weight=700, color=INK)
arc(C2[0], C2[1], 42, 213, 270)
text(C2[0] - 24, C2[1] + 46, "β", size=18, weight=700, color=RED)
text(A2[0] + 85, (BASE + APEX) / 2 - 22, "hypoténuse", size=15, weight=700, color=INK)
text(490, 322, "opposé", size=15, weight=700, color=RED)
text(B2[0] + 10, (BASE + APEX) / 2 + 6, "adjacent", anchor="start", size=15, weight=700, color=GREY)
text(490, 340, "opposé et adjacent s'échangent", size=14, weight=600, color=SOFT)
text(490, 362, "β = 90° − α", size=14, weight=600, color=SOFT)

# ------------------------------------ 3 : deux tailles, meme angle alpha
ox = 700
A3 = (ox, BASE)
slope = float(BASE - APEX) / WID
Bs = (ox + 100, BASE)
Cs = (ox + 100, BASE - 100 * slope)
Bb = (ox + WID, BASE)
Cb = (ox + WID, APEX)
line([A3, Bb], GREY, 4)
line([Bb, Cb], RED, 4)
line([Cb, A3], INK, 4)
line([Bs, Cs], RED, 3)
line([(Bs[0], BASE - 6), (Bs[0], BASE + 6)], GREY, 2)
right_angle(Bb, (-1, 0), (0, -1), s=16)
right_angle(Bs, (-1, 0), (0, -1), s=11)
arc(A3[0], A3[1], 42, 0, 33)
text(A3[0] + 54, A3[1] - 12, "α", size=18, weight=700, color=RED)
text(810, 100, "3 · deux tailles, même α", size=16, weight=700, color=INK)
text(Bs[0] - 8, (BASE + Cs[1]) / 2 + 6, "a", anchor="end", size=15, weight=700, color=RED)
text(A3[0] + 42, BASE - 42 * slope - 10, "c", size=15, weight=700, color=INK)
text(Bb[0] + 10, (BASE + APEX) / 2 + 6, "a′", anchor="start", size=15, weight=700, color=RED)
text(A3[0] + 162, BASE - 162 * slope - 12, "c′", size=15, weight=700, color=INK)
text(852, 322, "× k", size=15, weight=700, color=GREY)
text(810, 340, "triangles semblables :", size=14, weight=600, color=SOFT)
text(810, 362, "sin α = a / c = a′ / c′", size=15, weight=700, color=RED)


# ------------------------------------------------------------------ SVG
def svg_out(path):
    o = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
         'font-family="Inter, Segoe UI, system-ui, sans-serif">' % (W, H, W, H),
         '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H)]
    for kind, e in els:
        if kind == "line":
            d = " ".join(("%s%.1f,%.1f" % ("M" if i == 0 else "L", x, y))
                         for i, (x, y) in enumerate(e["pts"]))
            dash = ' stroke-dasharray="7 6"' if e["dash"] else ""
            op = '' if e["opacity"] == 1.0 else ' stroke-opacity="%.2f"' % e["opacity"]
            o.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
                     'stroke-linecap="round" stroke-linejoin="round"%s%s/>'
                     % (d, e["color"], e["width"], dash, op))
        elif kind == "dot":
            o.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>'
                     % (e["x"], e["y"], e["r"], e["color"]))
        else:
            o.append('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%d" font-weight="%d" '
                     'fill="%s" stroke="#fff" stroke-width="4" paint-order="stroke" '
                     'stroke-linejoin="round">%s</text>'
                     % (e["x"], e["y"], e["anchor"], e["size"], e["weight"], e["color"],
                        e["s"].replace("&", "&amp;").replace("<", "&lt;")))
    o.append('</svg>')
    io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(o) + "\n")


# ----------------------------------------------------------- Excalidraw
random.seed(20260922)
def rid():
    return "el%09d" % random.randrange(10 ** 9)


def base(el_id, kind, x, y, w, h, stroke, bg="transparent", sw=2):
    return {"id": el_id, "type": kind, "x": x, "y": y, "width": w, "height": h, "angle": 0,
            "strokeColor": stroke, "backgroundColor": bg, "fillStyle": "solid",
            "strokeWidth": sw, "strokeStyle": "solid", "roughness": 1, "opacity": 100,
            "groupIds": [], "frameId": None, "roundness": None,
            "seed": random.randrange(10 ** 9), "version": 1,
            "versionNonce": random.randrange(10 ** 9), "isDeleted": False,
            "boundElements": None, "updated": 1758499200000, "link": None, "locked": False}


def excalidraw_out(path, title):
    elements, texts = [], []
    for kind, e in els:
        i = rid()
        if kind == "line":
            xs = [p[0] for p in e["pts"]]
            ys = [p[1] for p in e["pts"]]
            x0, y0 = xs[0], ys[0]
            d = base(i, "line", x0, y0, max(xs) - min(xs), max(ys) - min(ys),
                     e["color"], sw=min(4, e["width"]))
            d["strokeStyle"] = "dashed" if e["dash"] else "solid"
            d["opacity"] = int(e["opacity"] * 100)
            d["points"] = [[p[0] - x0, p[1] - y0] for p in e["pts"]]
            d.update(lastCommittedPoint=None, startBinding=None, endBinding=None,
                     startArrowhead=None, endArrowhead=None)
            elements.append(d)
        elif kind == "dot":
            r = e["r"]
            elements.append(base(i, "ellipse", e["x"] - r, e["y"] - r, 2 * r, 2 * r,
                                 e["color"], e["color"]))
        else:
            fs = e["size"]
            w = len(e["s"]) * fs * 0.55
            x = e["x"] - (w / 2 if e["anchor"] == "middle" else w if e["anchor"] == "end" else 0)
            d = base(i, "text", round(x, 1), e["y"] - fs, round(w, 1), fs * 1.25, e["color"])
            d.update(text=e["s"], fontSize=fs, fontFamily=1,
                     textAlign="left", verticalAlign="top", baseline=int(fs * 0.82),
                     containerId=None, originalText=e["s"], lineHeight=1.25, autoResize=True)
            elements.append(d)
            texts.append("%s ^%s" % (e["s"], i))

    doc = {"type": "excalidraw", "version": 2,
           "source": "https://github.com/StudioAlbert/Knowledges",
           "elements": elements,
           "appState": {"gridSize": 20, "gridStep": 5, "gridModeEnabled": False,
                        "viewBackgroundColor": "#ffffff"},
           "files": {}}
    head = ("---\n\nexcalidraw-plugin: parsed\ntags: [excalidraw]\n\n---\n"
            "==\u26a0  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. \u26a0==\n\n"
            "# %s\n\n# Excalidraw Data\n\n## Text Elements\n" % title)
    body = "\n\n".join(texts) + "\n\n%%\n## Drawing\n```json\n"
    tail = "\n```\n%%\n"
    io.open(path, "w", encoding="utf-8", newline="\n").write(
        head + body + json.dumps(doc, ensure_ascii=False, indent=2) + tail)


svg = os.path.join(ROOT, "00 images", "trg02_rapports_trigo.svg")
exc = os.path.join(ROOT, "Excalidraw", "TRG-02 - Rapports trigonométriques.excalidraw.md")
svg_out(svg)
excalidraw_out(exc, "Rapports trigonométriques — opposé, adjacent, hypoténuse")
print("%d éléments écrits dans :" % len(els))
print("  " + svg)
print("  " + exc)
