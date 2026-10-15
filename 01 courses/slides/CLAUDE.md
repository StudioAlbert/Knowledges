# slides/ — écriture des decks

Les decks reveal.js (`type: slides`), nommés par code de département :
`GPR-CF-BDP-06 - Chaînes de caractères.md`. **C'est ce que rend le site build**, mais le deck
ne décide pas de sa publication : il n'a ni `publish` ni `status`.

## La publication se décide dans `lectures/`

C'est le `status` de la note de séance qui publie, par son code :

| `status` de la séance | Effet |
|---|---|
| `Backlog`, `To prepare` | non publié, la séance n'existe pas sur le site |
| `To check` | brouillon : visible du seul serveur de test, avec bandeau « brouillon » et `noindex` |
| `Ready`, `Post-mortem`, `Post-mortem-done` | en ligne, visible des étudiants |

Une séance **neuve en cours de révision est en `To check`**, jamais directement en `Ready` :
le build de production ignore les brouillons, donc elle ne peut pas atteindre le site des
étudiants. Une séance déjà donnée, elle, reste en ligne pendant sa révision
(`Post-mortem` → `Post-mortem-done`). Détail du contrat dans `site-build/CLAUDE.md`.

## Construction des slides

- **4 bullet points maximum** par slide.
- Privilégier les visuels pour expliciter les points plutôt que du texte.
- Un **exemple de code** est seul sur sa slide, avec une seule phrase de contexte ou
  d'explication.
- Un **schéma** est seul sur sa slide, avec une seule ligne de contexte ou d'explication
  (`class="schema"`, SVG généré par un script de `tools/schemas/`).
- Proposer des **widgets** et des **schémas** dès qu'un point s'explique mieux en image.

## Technique

Slides Extended (reveal.js) avec `00 templates/css/sae_styles.css`. Le cadre utilisable d'une
slide 1280x720 est x 0->1189, y 97->622 — `sae_styles.css` est découpé par concern et fait
référence pour les limites de mise en page.

Seules trois classes de slide sont en usage, et elles sont porteuses pour le CSS :

- `<!-- .slide: class="title" -->` — slide de section / de titre
- `<!-- .slide: class="schema" -->` — un SVG généré de `00 images/`, `![[nom.svg]]`
- `<!-- .slide: class="widget" -->` — un widget plein écran, via
  `data-background-iframe="00 widgets/_widgets/….html#anchor" data-background-interactive`
  et **sans titre**, puisque le widget affiche le sien

Référencer un widget par son chemin **vault**, jamais par `/widgets/…` : c'est le build qui
réécrit (voir `site-build/CLAUDE.md`).
