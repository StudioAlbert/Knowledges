---
title: PCG — Annexes
type: ressource
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
source_slides: https://docs.google.com/presentation/d/1B3tzViqqicNWe_oAYo197ClvVPVZ1Ac3uzQtG8DlW18/edit
---

# PCG — Annexes
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

<small>Deux fiches techniques sorties du cours principal : la formule de coupe
BSP, et le masque de bits des voisins de tuile.</small>

Note:
Le deck source ne contient que trois planches, sans texte : ce sont des schémas
de référence à projeter pendant le TP. Ils sont reconstruits ici à partir des
étiquettes.

---

# Coupe BSP — verticale
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

Une région est décrite par `xMin, xMax, yMin, yMax`. La coupe **verticale** se
place à :

```text
   x = xMin + ratio * size

   yMax +----------------+----------------+
        |                |                |
        |      gauche    |     droite     |
        |                |                |
   yMin +----------------+----------------+
      xMin              x                xMax
```

<small>`ratio` tiré dans `[0.3, 0.7]` évite les régions dégénérées ; `ratio = 0.5`
donne la coupe exacte.</small>

Note:
Le garde-fou sur `ratio` est ce qui empêche le générateur de produire un couloir
d'une case de large. À rappeler à chaque TP BSP.

---

# Coupe BSP — horizontale
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

Même formule sur l'autre axe :

```text
   y = yMin + ratio * size

   yMax +---------------------------------+
        |               haut              |
      y +---------------------------------+
        |               bas               |
   yMin +---------------------------------+
      xMin                              xMax
```

<small>Le choix de l'axe se fait sur le rapport largeur / hauteur : on coupe
toujours dans la dimension la plus longue, sinon les salles s'allongent.</small>

Cours de référence : [[pcg_introduction]], slide *Binary space partitioning*.

---

# Masque de voisinage
<!-- .slide: data-background="00 images/01_slide_fond_content.jpg" -->

Quatre directions, quatre bits — un entier par tuile décrit tout son voisinage :

| Direction | Binaire | Décimal |
| --- | --- | --- |
| **Bottom** | `1000` | 8 |
| **Left** | `0100` | 4 |
| **Top** | `0010` | 2 |
| **Right** | `0001` | 1 |

```text
              Top = 0010
                  |
   Left = 0100 --[ ]-- Right = 0001
                  |
             Bottom = 1000
```

Note:
Seize combinaisons possibles, donc seize tuiles à dessiner pour un tileset
complet — c'est le calcul à faire *avant* de commander les assets à l'artiste.
Le masque sert aussi à décider où poser un collider : une tuile de mur dont le
masque vaut `1111` est entourée de murs, donc invisible et sans collider.

---

# Utilisation
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```text
   mask = 0
   if (voisinBas   est plein) mask |= 8
   if (voisinGauche est plein) mask |= 4
   if (voisinHaut  est plein) mask |= 2
   if (voisinDroite est plein) mask |= 1

   tile = tileset[mask]
```

<small>Un tableau de 16 entrées remplace toute une cascade de `if`. C'est le
même passage « algorithme → géométrie » que dans
[[pcg_applications|Applications]].</small>
