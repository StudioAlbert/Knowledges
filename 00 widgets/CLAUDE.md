# 00 widgets/ — pages interactives

Les widgets (`_widgets/*.html`) sont des pages uniques autonomes et sans dépendance —
styles, SVG et JS inline — ouvrables par double-clic, sans serveur ni build.

`README.md` est l'inventaire et liste les ancres de chaque fichier : **le mettre à jour en
ajoutant un widget**.

Ce dossier est copié en entier vers `/widgets/` par le site build — c'est la seule exception
à la règle qui ignore les dossiers préfixés `_`. Un deck y renvoie par le chemin vault
(`00 widgets/_widgets/x.html#anchor`), jamais par `/widgets/…`.
