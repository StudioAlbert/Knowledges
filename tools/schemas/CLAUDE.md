# tools/schemas/ — générateurs de figures

Un script Python 3 par figure, lancé à la main :

```bash
python "tools/schemas/bdp06_std_string.py"
```

Chaque script est la **source de vérité** de sa figure et écrase ses deux sorties : le SVG
dans `00 images/` et le `.excalidraw.md` dans `Excalidraw/`. **Éditer la copie Excalidraw ne
met pas le SVG à jour** — repasser par le script.

Les primitives de dessin partagées sont dans `schema_lib.py` ; un nouveau générateur
s'appuie dessus plutôt que d'émettre du SVG à la main.

Les figures sont consommées par des slides `class="schema"` (voir
`01 courses/slides/CLAUDE.md`) : une figure est seule sur sa slide, donc elle doit être
lisible à 1280x720 sans texte d'accompagnement.
