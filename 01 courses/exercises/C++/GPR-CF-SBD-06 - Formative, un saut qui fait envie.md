---
seances: [GPR-CF-SBD-06]
---
# Formative — un saut qui fait envie

**Une seule ficelle, bien réglée.** Vous choisissez une façon de rendre le saut agréable,
vous l'implémentez dans votre platformer, et **la semaine prochaine tout le monde joue à
tout le monde**.

Ce n'est pas noté sur la quantité. Un jeu avec un seul saut qui fait envie passe devant un
jeu avec cinq ficelles mal réglées — et le playtest le dira tout seul.

---

## Choisissez-en **une**

| Ficelle | Ce que le joueur sent |
|---|---|
| **Coyote time** | « j'étais sûr d'avoir sauté à temps » — et le jeu vous donne raison |
| **Jump buffer** | la touche pressée trop tôt n'est pas perdue |
| **Saut à hauteur variable** | une petite tape fait un petit saut, un appui long fait un grand |
| **Gravité asymétrique** | on monte doucement, on retombe vite : le saut devient nerveux |
| **Apex hang** | une suspension de quelques centièmes au sommet, le temps de viser |
| **Squash and stretch** | le personnage s'étire en montant, s'écrase à l'atterrissage |
| **Poussière et impact** | un nuage au décollage, une secousse à l'atterrissage |

Les trois dernières ne touchent pas à la physique : elles touchent à ce qu'on **voit**. Elles
comptent autant.

> [!tip] Si vous hésitez
> Prenez **la gravité asymétrique**. C'est trois lignes, l'effet s'entend presque, et c'est
> celle qui transforme le plus un saut mou en saut de platformer.

---

## Ce qu'on attend

1. **La ficelle marche**, dans votre jeu, avec votre héros.
2. **Elle est réglable** : ses valeurs sont dans votre fichier de réglages, nommées, avec
   leur unité. Pas de nombre magique au milieu du contrôleur.
3. **Vous l'avez réglée en jouant**, pas en calculant. Notez les deux ou trois valeurs que
   vous avez essayées avant celle que vous gardez.
4. **Un interrupteur** : on doit pouvoir l'éteindre et la rallumer sans recompiler — une
   touche, un booléen de réglage. C'est ce qui permettra de la montrer au playtest.

> [!warning] Le point qui coûte des points
> Une ficelle qu'on ne peut pas éteindre ne se démontre pas. Si personne ne peut jouer
> **sans**, personne ne sentira ce qu'elle apporte — y compris vous.

---

## Le playtest, la semaine suivante

Vingt minutes, en salle, tout le monde debout.

1. **On tourne.** Chacun laisse son jeu lancé et va jouer à celui du voisin, trois minutes
   par poste.
2. **Deux questions, à chaque poste** : *le saut te paraît-il juste ?* et *qu'est-ce que tu
   changerais en premier ?*
3. **Interrupteur.** Avant de partir, on joue trente secondes avec la ficelle **éteinte**,
   et on dit si ça se sent.
4. **On note.** Chacun repart avec les remarques reçues, écrites par les autres.

Ce que le playtest mesure n'est pas votre code : c'est l'écart entre ce que vous croyiez
avoir réglé et ce que quelqu'un d'autre ressent en trois minutes.

---

## Ce qu'on rend, après le playtest

| | Ce qui est attendu |
|---|---|
| **le code** | la ficelle, ses réglages nommés, et son interrupteur |
| **trois lignes** | la valeur retenue, et les deux que vous avez essayées avant |
| **trois lignes** | ce que les autres ont dit, et ce que vous avez changé après |

Le dernier point est le vrai exercice. Une remarque reçue et ignorée, assumée en une phrase,
vaut mieux qu'une remarque recopiée sans suite.

> [!check] Je sais…
>
> | | Vérification |
> |---|---|
> | implémenter une ficelle de game feel | elle marche dans mon jeu, pas dans un exemple |
> | sortir ses réglages | quelqu'un peut la régler sans ouvrir mon contrôleur |
> | la démontrer | je peux l'éteindre devant quelqu'un, et il sent la différence |
> | entendre un retour | j'ai changé quelque chose après le playtest, ou j'explique pourquoi non |
