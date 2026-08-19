---
title: Tank vs Towers
type: projet
specialisation: "[[Unity]]"
---
# Tank vs Towers

### Pitch

Aller à la fin du niveau sans se faire détruire

### Camera

Camera Orthographique Top Down - Fixe : Tout le plateau de jeu est visible

### Controls

Exemple de controle “Twin stick shooter”

[https://docs.google.com/drawings/d/e/2PACX-1vQXD8zlpfbEoefCM_npbFNJJnb8mgbibGVQr4Uk1URh1n1iwbyhaJcBdKpVd0oiHbXHn7a1RMgmdG7T/pub?w=1145&h=771](https://docs.google.com/drawings/d/e/2PACX-1vQXD8zlpfbEoefCM_npbFNJJnb8mgbibGVQr4Uk1URh1n1iwbyhaJcBdKpVd0oiHbXHn7a1RMgmdG7T/pub?w=1145&h=771)

### Système de tir

- Projectile physique (au choix)
    - la trajectoire peut tenir compte de l’inclinaison verticale de la tourelle.
    - la trajectoire est rectiligne

![images.jpg](Tank%20vs%20Towers/images.jpg)

![images.png](Tank%20vs%20Towers/images.png)

- Le tir est déclenché en continu à cadence régulière (Coroutine)
    - Instantiation
    - Ajout d’une force à la “création” du projectile

### Experience content (Time / Levels)

- Détruire toutes les tourelles + une cible de fin de niveau
- Tourelles fixes
- Temps limité

---

### Ressources / Assets