# Widgets

Démos interactives utilisées en cours par Sébastien Albert (programmation de jeux, maths,
IA). Chaque widget est **une page HTML autonome** : pas de build, pas de dépendance, un
double-clic suffit à l'ouvrir. Tout est inline — styles, SVG, JavaScript — sauf les polices
Google Fonts et, pour A\*, `_templates/css/astar_widget.css`.

Ce dossier fait partie du vault `Knowledges` ; il en était un sous-module, il ne l'est plus.

## Inventaire

| Fichier | Ce qu'il montre | Ancres | Utilisé par |
| --- | --- | --- | --- |
| `_widgets/astar_widgets.html` | A\* pas à pas, heuristique, comparaison avec Dijkstra | — | `lectures/C++/cpp_a_star_` |
| `_widgets/droites_remarquables_widget.html` | Médianes, hauteurs, médiatrices, bissectrices et leurs points de concours | `#quelconque` `#isocele` `#equilateral` `#rectangle` `#obtus`, + `?fams=med,haut` (ou `all`) | TC-FT-TRG-01 |
| `_widgets/pythagore_widget.html` | Les trois carrés, la preuve par réarrangement, la réciproque, la distance | `#carres` `#preuve` `#reciproque` `#distance` | TC-FT-TRG-01 |
| `_widgets/thales_widget.html` | Thalès, sa réciproque, le calcul par les ombres | `#thales` `#reciproque` `#ombre` | TC-FT-TRG-01 |
| `_widgets/cercle_trigo_widget.html` | Cercle unité et unités d'angle, symétries, du cercle à l'onde | `#cercle` `#symetries` `#onde` | TC-FT-TRG-02 |
| `_widgets/resolution_triangles_widget.html` | Loi des sinus, loi des cosinus, rôle d'`atan2` | `#sinus` `#cosinus` `#atan2` | TC-FT-TRG-03 |
| `_widgets/utility_ai.html` | Courbes de réponse pour la décision des PNJ | — | portfolio uniquement |

## Dans une slide

La slide ne porte **que** le commentaire, sans titre : le widget affiche le sien. Le chemin
est celui du vault — c'est ce que sert Obsidian, et le build du site le réécrit en
`/widgets/…`. L'ancre choisit l'onglet ou le préréglage ouvert au chargement.

```markdown
<!-- .slide: data-background-iframe="00 widgets/_widgets/cercle_trigo_widget.html#symetries" data-background-interactive -->
```

Voir la section *WIDGET* de [`00 templates/css/sae_styles.css`](../00%20templates/css/sae_styles.css).
Une séance peut aussi lister ses widgets dans l'onglet *Ressources* du site, via une note
`01 courses/resources/<matière>/<CODE> - Widgets.md`.

## Conventions d'un widget

Ce que les cinq widgets du bloc Trigonométrie respectent, et que reprendra le prochain.
`astar_widgets.html` et `utility_ai.html` sont antérieurs et n'en suivent aucune — ils
fonctionnent, mais en iframe ils avalent les flèches du clavier.

- **Palette SAE** : rouge `#E30613`, encre `#1a1a1a`, gris `#6e6e6e` / `#a8a8a8`, fond blanc.
  Le rouge ne sert qu'à ce que la slide veut faire voir.
- **Mode intégré** : la page ajoute la classe `embed` à `<html>` quand elle est dans une
  iframe (ou avec `?embed`). Le CSS `html.embed` masque le sous-titre et le pied de page,
  et étire le dessin sur la hauteur disponible.
- **Onglets par ancre** : un onglet par `data-tab`, `show(location.hash.slice(1))` au
  chargement, `history.replaceState` au clic, et un écouteur `hashchange`. C'est ce qui
  permet à trois slides de pointer trois vues d'un même fichier.
- **Clavier rendu à reveal.js** : en mode intégré, les flèches et Page↑/↓ sont renvoyées au
  parent par `postMessage`, sinon l'iframe capture la navigation entre slides.
- **Dessin en SVG** construit en JavaScript, avec un `viewBox` fixe ; les libellés portent un
  halo blanc (`stroke` + `paint-order`) pour rester lisibles au-dessus des traits.

## Publication

- **Site des cours** : `site-build/build.mjs` recopie ce dossier tel quel sous `/widgets/`,
  y compris les dossiers préfixés `_`. Rien à faire de plus que committer.
- **GitHub Pages** : `index.html` et `.nojekyll` viennent du dépôt public
  [StudioAlbert/widgets](https://github.com/StudioAlbert/widgets), d'où le
  [portfolio](https://github.com/StudioAlbert/Portfolio) embarque A\* et Utility AI. Cette
  copie se met à jour à la main, et `index.html` ne liste encore que ces deux widgets.
