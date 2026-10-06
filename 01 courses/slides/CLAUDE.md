# slides/ — écriture des decks

Les decks reveal.js (`type: slides`), nommés par code de département :
`GPR-CF-BDP-06 - Chaînes de caractères.md`. **C'est ce que lit le site build**, donc
`publish` se met ici, pas sur la note de séance.

## publish : trois états

| `publish` | Effet |
|---|---|
| `false` ou absent | non publié, la séance n'existe pas sur le site |
| `draft` | brouillon : visible du seul serveur de test, avec bandeau « brouillon » et `noindex` |
| `online` | en ligne, visible des étudiants |

Une séance **en cours de révision passe en `draft`**, jamais directement en `online` : le
build de production ignore les brouillons, donc un deck laissé en `draft` ne peut pas
atteindre le site des étudiants. Repasser en `online` est un geste délibéré, une fois la
révision validée. Détail du contrat dans `site-build/CLAUDE.md`.

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
