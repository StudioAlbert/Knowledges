---
title: Principes et premier dépôt
type: course
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Git et Travail en Équipe
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
manual_order: 8
---

# Principes et premier dépôt
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

### Tips & how-to — Git

<small>Module 4FSC0PF001 · Introduction to Games Programming</small>

Note:
Séance courte et pratique : à quoi sert Git, comment l'installer, et les
quatre commandes qui couvrent 95 % de ce que vous ferez pendant le
module.

---

## Git — principes
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- sauvegarder son code sur un serveur
- travailler à plusieurs
- partager son code (open-source)

---

## Git — les branches
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Créer des branches :

- différentes versions du logiciel (v0.9, beta, alpha)
- isoler les fonctionnalités

---

## Git — l'écosystème
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Les dépôts d'hébergement Git distants — GitHub, GitLab, Bitbucket…

Les interfaces graphiques Git (GUI) côté client :

- SourceTree (Mac, Windows)
- GitHub Desktop (Mac, Windows)
- TortoiseGit (Windows)
- Git Extensions (Linux, Mac, Windows)
- la ligne de commande :)
- des plugins pour votre IDE préféré

---

## Install Git
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Download on the Git website : [git-scm.com/downloads](https://git-scm.com/downloads)

Launch the install, pick every default option, except those below :

- pick a text editor (VS Code advised)
- pick « Use Windows' default console window »

---

## Récupérer un dépôt de code (depuis GitHub)
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Depuis la page GitHub du projet :

- choix de la branche
- URL pour la ligne de commande
- récupérer directement dans l'IDE
- récupérer le code en ZIP — **pas de possibilité de commit**

```bash
cd [repo_root_directory]
git clone [repo_url]
```

---

## Mettre à jour, et partager
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

**Mettre à jour et fusionner le repo local**

```bash
git pull
```

**Partager les modifications**

```bash
git add .
git commit -m "easily_and_short_readable_description"
git push
```

---

## Créer un repo avec des fichiers existants
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```bash
git init
git add .
git commit -m "first commit"
git remote add origin [repo_url]
git push -u origin main
```

Note:
Cette diapo n'était qu'une capture d'écran de la page d'accueil d'un
dépôt GitHub vide, celle qui affiche justement cette séquence de
commandes. La séquence ci-dessus la reconstitue.

---

## En savoir plus
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- [Atlassian — Git cheat sheet](https://www.atlassian.com/fr/git/tutorials/atlassian-git-cheatsheet)
- [Présentation Git (CNRS)](https://giorgi.pages.math.cnrs.fr/git_pres/#15)
- [W3Schools — Git exercises](https://www.w3schools.com/git/git_exercises.asp)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=fr_FR)
- [Git Exercises](https://gitexercises.fracz.com/)
- [Oh My Git!](https://ohmygit.org/)

---

## Pause
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Question time !

Vous pouvez aussi jouer avec VS2019 — ou faire une pause, au cas où votre cerveau serait en train de fondre…
