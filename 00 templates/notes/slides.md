<%*
const [code, ...reste] = tp.file.title.split(" - ");
const titre = reste.join(" - ");
const matiere = tp.file.folder(true).split("/").pop();
-%>
---
title: <% titre %>
type: slides
status: Backlog
subject: <% matiere %>
duration_h: 1
bloc_gsda:
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: false
---

# <% titre %>
<!-- .slide: class="title" -->

<small><% code %></small>

---

## Objectifs

À la fin de la séance, vous savez :

- 

---

# Clôture
<!-- .slide: class="title" -->

---

## Exercices

Énoncés : [[01 courses/exercises/<% matiere %>/<% tp.file.title %>]]
