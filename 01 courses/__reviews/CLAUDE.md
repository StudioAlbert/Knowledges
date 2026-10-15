# __reviews/ — checklists de révision

Ce dossier tient les checklists de révision par séance, dont le frontmatter lie les notes
`slides:` et `exercices:` à corriger. **Ce sont des fiches de travail, pas des cartes de
kanban** : elles n'ont ni `status` ni `manual_order`, et la séance les atteint par sa clé
`review:`. Il n'y a qu'un kanban dans ce vault, `__course base.base`, qui porte les notes
de `lectures/`.

`__course base.base` met `lectures/` en colonnes par `status`
(Backlog / To prepare / To check / Ready / Post-mortem / Post-mortem-done), groupe par
`projet` et met en couloirs par `bloc_gsda`. Il ne retient que les notes `type: seance`, et
ignore les dossiers préfixés `_` : c'est ainsi qu'on sort une séance du kanban sans toucher
à son statut.

**Ce `status` pilote aussi la publication du site** — voir `site-build/CLAUDE.md`. Changer la
colonne d'une séance, c'est décider de ce que voient les étudiants.

Trois fiches ne décrivent pas une séance et ne sont donc reliées à aucune note :
`CSS Review - Publication`, `Programme 2027-2028 - APU` et `APU 04 APU 05 APU 09 deviennent`.

`bloc_gsda` est du texte simple, **jamais un wikilink** (aucune note de bloc n'existe dans ce
vault), et est volontairement vide sur les notes encore en attente de placement GSDA.

Les métadonnées de séance sont lues depuis le checkout voisin `_GSDA_Tech_Vault` et
maintenues **à la main** — aucun script ne les rafraîchit, donc un changement côté
département doit être reporté manuellement.

Pour traiter les révisions en attente, utiliser la skill `traiter-revisions`.
