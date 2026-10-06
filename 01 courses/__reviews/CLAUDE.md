# __reviews/ — checklists de révision et kanban

Ce dossier tient les checklists de révision par séance, dont le frontmatter lie les notes
`slides:` et `exercices:` en cours de révision. `Reviews.base` et `__course base.base` sont
les vues Obsidian Bases par-dessus.

`__course base.base` met `lectures/` en colonnes par `status`
(Backlog / To prepare / Ready / Done), groupe par `projet` et met en couloirs par
`bloc_gsda`.

`bloc_gsda` est du texte simple, **jamais un wikilink** (aucune note de bloc n'existe dans ce
vault), et est volontairement vide sur les notes encore en attente de placement GSDA.

Les métadonnées de séance sont lues depuis le checkout voisin `_GSDA_Tech_Vault` et
maintenues **à la main** — aucun script ne les rafraîchit, donc un changement côté
département doit être reporté manuellement.

Pour traiter les révisions en attente, utiliser la skill `traiter-revisions`.
