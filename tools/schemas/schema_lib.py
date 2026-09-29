# -*- coding: utf-8 -*-
"""Primitives communes aux générateurs de schémas.

Reprend la méthode de `trg02_rapports_trigo.py` — une seule description de la figure,
deux sorties (SVG publié dans `00 images/`, `.excalidraw.md` éditable dans `Excalidraw/`)
— et ajoute ce qu'il faut pour les diagrammes : boîtes, flèches et cercles.

Un script de schéma fait :

    from schema_lib import Figure, RED, INK, GREY, SOFT
    fig = Figure(1000, 330)
    fig.box(...); fig.arrow(...); fig.text(...)
    fig.save("apu09_fsm_principes", "APU-09 - Principes d'une machine à états")

Rejouer un script écrase ses deux fichiers : le script est la source.
"""
import io, json, math, os, random, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RED, INK, GREY, SOFT, PALE = "#E30613", "#1a1a1a", "#6e6e6e", "#555555", "#f5f5f5"


class Figure:
    def __init__(self, w, h, seed=20260928):
        self.W, self.H = w, h
        self.els = []
        self.seed = seed

    # ------------------------------------------------------------ primitives
    def line(self, pts, color=INK, width=3, dash=False, opacity=1.0, arrow=False):
        self.els.append(("line", dict(pts=[(float(x), float(y)) for x, y in pts], color=color,
                                      width=width, dash=dash, opacity=opacity, arrow=arrow)))

    def dot(self, x, y, r=6, color=INK):
        self.els.append(("dot", dict(x=float(x), y=float(y), r=r, color=color)))

    def text(self, x, y, s, anchor="middle", size=16, weight=600, color=INK, mono=False, halo=True):
        """(x, y) = point d'ancrage et ligne de base, comme en SVG. `halo` : liseré blanc."""
        self.els.append(("text", dict(x=float(x), y=float(y), s=s, anchor=anchor, size=size,
                                      weight=weight, color=color, mono=mono, halo=halo)))

    def rect(self, x, y, w, h, stroke=INK, fill="#ffffff", width=2.5, dash=False, radius=10):
        self.els.append(("rect", dict(x=float(x), y=float(y), w=float(w), h=float(h), stroke=stroke,
                                      fill=fill, width=width, dash=dash, radius=radius)))

    # ------------------------------------------------------------ composés
    def box(self, cx, cy, label, w=150, h=46, active=False, muted=False, size=16, sub=None):
        """Un état : boîte arrondie centrée en (cx, cy). Renvoie ses bords pour les flèches."""
        if active:
            self.rect(cx - w / 2, cy - h / 2, w, h, stroke=RED, fill=RED, width=2.5)
            color = "#ffffff"
        elif muted:
            self.rect(cx - w / 2, cy - h / 2, w, h, stroke=GREY, fill=PALE, width=2, dash=True)
            color = GREY
        else:
            self.rect(cx - w / 2, cy - h / 2, w, h, stroke=INK, fill="#ffffff", width=2.5)
            color = INK
        dy = 6 if sub is None else -2
        self._label(cx, cy + dy, label, size, color)
        if sub:
            self._label(cx, cy + 16, sub, 12, "#ffffff" if active else GREY, weight=500)
        return Box(cx, cy, w, h)

    def _label(self, x, y, s, size, color, weight=700):
        self.els.append(("text", dict(x=float(x), y=float(y), s=s, anchor="middle", size=size,
                                      weight=weight, color=color, mono=False, halo=False)))

    def arrow(self, a, b, label=None, color=INK, width=2.5, bend=0.0, dash=False,
              label_at=0.5, label_dx=0, label_dy=-8, label_color=None, size=13):
        """Flèche de a vers b (points ou Box). `bend` courbe la flèche (px, signe = côté)."""
        p0 = a.edge_towards(b.center if isinstance(b, Box) else b) if isinstance(a, Box) else a
        p1 = b.edge_towards(a.center if isinstance(a, Box) else a) if isinstance(b, Box) else b
        if bend:
            mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
            dx, dy = p1[0] - p0[0], p1[1] - p0[1]
            n = math.hypot(dx, dy) or 1
            c = (mx - dy / n * bend, my + dx / n * bend)
            if isinstance(a, Box):
                p0 = a.edge_towards(c)
            if isinstance(b, Box):
                p1 = b.edge_towards(c)
            pts = [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t ** 2 * p1[0],
                    (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t ** 2 * p1[1])
                   for t in [i / 20 for i in range(21)]]
        else:
            pts = [p0, p1]
        self.line(pts, color, width, dash=dash, arrow=True)
        if label:
            i = min(len(pts) - 1, max(0, int(round(label_at * (len(pts) - 1)))))
            lx, ly = pts[i] if len(pts) > 2 else (p0[0] + (p1[0] - p0[0]) * label_at,
                                                    p0[1] + (p1[1] - p0[1]) * label_at)
            self.text(lx + label_dx, ly + label_dy, label, size=size, weight=600,
                      color=label_color or (color if color != INK else SOFT))

    def start(self, box, dx=-55, dy=0):
        """Pastille d'état initial reliée à une boîte."""
        p = (box.cx + dx - (box.w / 2 if dx < 0 else -box.w / 2 if dx > 0 else 0), box.cy + dy)
        self.dot(p[0], p[1], 7, INK)
        self.arrow(p, box, width=2.5)

    def circle(self, cx, cy, r, color=INK, width=3, n=72):
        pts = [(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n))
               for i in range(n + 1)]
        self.line(pts, color, width)

    # ------------------------------------------------------------ sorties
    def save(self, name, title):
        svg = os.path.join(ROOT, "00 images", name + ".svg")
        exc = os.path.join(ROOT, "Excalidraw", title + ".excalidraw.md")
        os.makedirs(os.path.dirname(svg), exist_ok=True)
        os.makedirs(os.path.dirname(exc), exist_ok=True)
        self.svg_out(svg)
        self.excalidraw_out(exc, title)
        print("%d éléments écrits dans :" % len(self.els))
        print("  " + svg)
        print("  " + exc)

    def svg_out(self, path):
        W, H = self.W, self.H
        o = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
             'font-family="Inter, Segoe UI, system-ui, sans-serif">' % (W, H, W, H),
             '<defs><marker id="head-ink" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
             '<marker id="head-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
             '<marker id="head-grey" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
             '</defs>' % (INK, RED, GREY),
             '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H)]
        heads = {RED: "head-red", GREY: "head-grey"}
        for kind, e in self.els:
            if kind == "line":
                d = " ".join(("%s%.1f,%.1f" % ("M" if i == 0 else "L", x, y))
                             for i, (x, y) in enumerate(e["pts"]))
                dash = ' stroke-dasharray="7 6"' if e["dash"] else ""
                op = '' if e["opacity"] == 1.0 else ' stroke-opacity="%.2f"' % e["opacity"]
                mk = ' marker-end="url(#%s)"' % heads.get(e["color"], "head-ink") if e["arrow"] else ""
                o.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s" '
                         'stroke-linecap="round" stroke-linejoin="round"%s%s%s/>'
                         % (d, e["color"], e["width"], dash, op, mk))
            elif kind == "rect":
                dash = ' stroke-dasharray="7 6"' if e["dash"] else ""
                o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" fill="%s" '
                         'stroke="%s" stroke-width="%s"%s/>'
                         % (e["x"], e["y"], e["w"], e["h"], e["radius"], e["fill"], e["stroke"],
                            e["width"], dash))
            elif kind == "dot":
                o.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>'
                         % (e["x"], e["y"], e["r"], e["color"]))
            else:
                fam = ' font-family="JetBrains Mono, Consolas, monospace"' if e.get("mono") else ""
                halo = (' stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round"'
                        if e.get("halo", True) else "")
                o.append('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%d" font-weight="%d" '
                         'fill="%s"%s%s>%s</text>'
                         % (e["x"], e["y"], e["anchor"], e["size"], e["weight"], e["color"], fam, halo,
                            e["s"].replace("&", "&amp;").replace("<", "&lt;")))
        o.append('</svg>')
        io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(o) + "\n")

    def excalidraw_out(self, path, title):
        random.seed(self.seed)

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

        elements, texts = [], []
        for kind, e in self.els:
            i = rid()
            if kind == "line":
                xs = [p[0] for p in e["pts"]]
                ys = [p[1] for p in e["pts"]]
                x0, y0 = xs[0], ys[0]
                d = base(i, "arrow" if e["arrow"] else "line", x0, y0, max(xs) - min(xs),
                         max(ys) - min(ys), e["color"], sw=min(4, e["width"]))
                d["strokeStyle"] = "dashed" if e["dash"] else "solid"
                d["opacity"] = int(e["opacity"] * 100)
                d["points"] = [[p[0] - x0, p[1] - y0] for p in e["pts"]]
                d.update(lastCommittedPoint=None, startBinding=None, endBinding=None,
                         startArrowhead=None, endArrowhead="arrow" if e["arrow"] else None)
                elements.append(d)
            elif kind == "rect":
                d = base(i, "rectangle", e["x"], e["y"], e["w"], e["h"], e["stroke"],
                         e["fill"] if e["fill"] != "#ffffff" else "transparent", sw=2)
                d["strokeStyle"] = "dashed" if e["dash"] else "solid"
                d["roundness"] = {"type": 3}
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
                d.update(text=e["s"], fontSize=fs, fontFamily=3 if e.get("mono") else 1,
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
                "==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==\n\n"
                "# %s\n\n# Excalidraw Data\n\n## Text Elements\n" % title)
        body = "\n\n".join(texts) + "\n\n%%\n## Drawing\n```json\n"
        tail = "\n```\n%%\n"
        io.open(path, "w", encoding="utf-8", newline="\n").write(
            head + body + json.dumps(doc, ensure_ascii=False, indent=2) + tail)


class Box:
    def __init__(self, cx, cy, w, h):
        self.cx, self.cy, self.w, self.h = cx, cy, w, h

    @property
    def center(self):
        return (self.cx, self.cy)

    def edge_towards(self, p, gap=4):
        """Point du bord de la boîte sur la droite centre → p (plus un petit jeu)."""
        dx, dy = p[0] - self.cx, p[1] - self.cy
        if dx == 0 and dy == 0:
            return self.center
        sx = (self.w / 2 + gap) / abs(dx) if dx else float("inf")
        sy = (self.h / 2 + gap) / abs(dy) if dy else float("inf")
        s = min(sx, sy)
        return (self.cx + dx * s, self.cy + dy * s)
