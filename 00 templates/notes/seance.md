<%*
const [code, ...reste] = tp.file.title.split(" - ");
const titre = reste.join(" - ");
const matiere = tp.file.folder(true).split("/").pop();
-%>
---
title: <% titre %>
type: seance
code: <% code %>
status: Backlog
projet:
subject: <% matiere %>
bloc_gsda:
classes: []
date_scheduled:
estimate: 1h
tache:
source_gsda: https://github.com/EliasFarhan/GSDA_CodeTech_Vault
---

# <% titre %>

## À couvrir

## Matériel

- Support : [[01 courses/slides/<% matiere %>/<% tp.file.title %>|<% tp.file.title %>]]
- Exercices : [[01 courses/exercises/<% matiere %>/<% tp.file.title %>|<% tp.file.title %>]]

## Liens

- Séance précédente : —
- Séance suivante : —

## Notes de préparation
