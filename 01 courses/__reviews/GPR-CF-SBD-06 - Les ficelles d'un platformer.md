---
slides: "[[01 courses/slides/C++/GPR-CF-SBD-06 - Les ficelles d'un platformer]]"
---
- [x] Rajouter animation faisant demonstration avec des différents principes
	- [x] Trouver le sprite le plus adapté parmi ceux fournis dans la sesson Code ou les ressources du companion (si possible CupHead)
- [x] Atelier : rédigé une fiche qui sera donné en formative
	- [x] L'idée, implémenter une feature de saut FUN, playtest collectif la semaine suivante !

## Traité le 20.10

### L'animation de démonstration

`saut_fun_widget.html` — **deux coureurs, le même niveau, la même touche au même instant**.
Celui du haut n'a aucune ficelle, celui du bas en a une. C'est la seule variable, et elle
décide qui passe.

| Onglet | Ce qu'on voit |
|---|---|
| `#coyote` | la touche part **80 ms trop tard** : sans coyote time le saut n'a pas lieu du tout, et il tombe |
| `#buffer` | le second appui part **100 ms trop tôt** : sans jump buffer il est perdu, et le trou suivant arrive |
| `#variable` | même appui, **61 px** de haut sans la ficelle, **31 px** avec — le petit saut redevient possible |
| `#asym` | même hauteur, mais la descente est deux fois plus rapide : la courbe se penche |

**Le sprite est Cuphead**, comme demandé : les trois poses de course de
`_Resources/sprites/` sont **embarquées en base64** dans le fichier, qui reste donc un
widget autonome d'un seul tenant — 24 ko en tout.

> [!check] Comment c'est vérifié
> Les quatre scénarios sont rejoués **en simulation pure**, hors animation, et donnent :
> coyote `sans tombe / avec passe`, buffer `sans tombe / avec passe`, variable `61 contre
> 31 px`, asym `61 contre 61 px`. Les instants d'appui ne sont pas écrits en dur : ils sont
> **sondés** au chargement à partir du niveau, donc ils restent justes si on change la
> vitesse ou la gravité.
>
> **Ce qui n'est pas vérifié** : l'animation en mouvement. Le panneau du navigateur tourne
> en arrière-plan et `requestAnimationFrame` y est gelé. Le rendu statique est juste —
> plateformes, sprites, étiquettes des deux voies — mais il faut l'ouvrir une fois à
> l'écran pour voir la course.

Deux niveaux ont dû être ajustés pour que la démonstration tienne. Celui du jump buffer
surtout : la plateforme du milieu doit être **courte**, sinon le coureur sans ficelle a le
temps de retomber sur la suivante et la ficelle ne prouve rien. J'ai cherché la bande de
valeurs qui marche plutôt que de prendre la première qui passait.

### La formative

[[01 courses/exercises/C++/GPR-CF-SBD-06 - Formative, un saut qui fait envie|Un saut qui fait envie]] :
**une seule ficelle, bien réglée**, et un playtest collectif la semaine suivante.

Sept ficelles au choix, dont trois qui ne touchent pas à la physique — squash and stretch,
poussière, secousse. Elles comptent autant, et c'est dit.

Quatre exigences, dont une qui n'était pas dans ta consigne et que je crois nécessaire :
**un interrupteur**. Une ficelle qu'on ne peut pas éteindre ne se démontre pas — au
playtest, personne ne sentira ce qu'elle apporte si personne ne peut jouer sans.

Le playtest est décrit minute par minute : on tourne trois minutes par poste, deux
questions à chaque poste, trente secondes avec la ficelle **éteinte**, et chacun repart
avec les remarques écrites par les autres. Le rendu final tient en six lignes — les valeurs
essayées, et ce qui a changé après le playtest. C'est ce dernier point qui est le vrai
exercice.
