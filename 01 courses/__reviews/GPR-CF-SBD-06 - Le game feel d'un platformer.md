---
slides: "[[01 courses/slides/C++/GPR-CF-SBD-06 - Le game feel d'un platformer]]"
---
- [x] intégrer widget dans les slides 
- [x] ficelle ???? le terme est mal traduit (Astuces ? Features ?)
- [x] Présenter dans l'ordre suivant GamePlay avec slides de widget -> Exemples de code box2D
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

## Traité le 26.10 — le mot, l'ordre, et un rappel qui avait changé

### « ficelle » devient « game feel »

Tu as tranché pour le terme du métier. Le concept est **le game feel**, et chaque
élément est **une technique** — un mot dénombrable, ce que « game feel » n'est pas.

Trois fichiers renommés, et la séance avec :

| Avant | Après |
|---|---|
| `GPR-CF-SBD-06 - Les ficelles d'un platformer` | `GPR-CF-SBD-06 - Le game feel d'un platformer` |
| « une ficelle », « sept ficelles » | « une technique », « sept techniques » |
| « Les ficelles sont là » *(summative)* | « Le game feel est là » |

Touchés : la note de séance, le deck, cette fiche, la summative, la formative, le
widget et l'inventaire `00 widgets/README.md`. **Plus aucune occurrence** du mot
hors `_archive/`, qu'on ne touche pas.

### L'ordre que tu demandais

Le deck est en **deux moitiés**, gameplay puis code, comme demandé.

**Ce que le joueur sent** — aucune ligne de C++ :

- le widget, qui ouvre maintenant la séance
- ce qui rend un saut agréable
- le wall jump
- l'accessibilité

**Et dans le code** — Box2D, une fois qu'ils ont vu :

- « au sol » n'est pas un contact
- le capteur de sol, puis le compteur
- le coyote time, puis le jump buffer
- l'arête des tuiles, puis la plateforme à sens unique

Vingt slides au lieu de vingt-et-une : les trois titres de section — *Le sol*, *Le
saut*, *Le fun* — deviennent deux. La note de présentation de la slide du widget
dit de ne rien coder à ce moment-là.

### Deux erreurs de code trouvées en vérifiant

Les en-têtes de **Box2D 3.2.0** sont clonés et lus, pas cités de mémoire.

> [!bug] Le saut ne compilait pas
> La slide du coyote time appelait `corps_->SetLinearVelocity(...)` — de la
> syntaxe Box2D **2.x**, avec une variable `v` qui n'existait nulle part. C'est
> maintenant `b2Body_GetLinearVelocity` puis `b2Body_SetLinearVelocity`.

> [!bug] Le rappel pre-solve a changé en 3.2
> Il renvoyait un `bool` en 3.0 et 3.1 ; en **3.2 il renvoie `void`**, et on annule
> la collision en mettant `manifold->pointCount` à zéro. La slide de la plateforme
> à sens unique est corrigée, et sa note prévient que les exemples trouvés en ligne
> ne compileront pas.
>
> Au passage, « le seul rappel qui reste dans Box2D 3 » était faux : il reste aussi
> le filtrage personnalisé et le pre-continuous. La slide dit maintenant ce qui est
> vrai — c'est le seul endroit où l'on intervient **pendant** la simulation.

### La slide de fin disait le contraire de la formative

Elle affirmait « cette séance n'a **pas** d'exercice à elle » alors que la
formative existe et est liée depuis la note. Elle présente maintenant la
formative et le playtest, et garde le lien vers la summative.

> [!bug] Correction du 26.10 — ma propre formulation
> J'avais remplacé « le seul rappel qui reste » par « le seul endroit où l'on
> intervient **pendant** la simulation ». C'était faux aussi : les rappels de
> friction et de restitution tournent eux aussi pendant le solveur.
>
> Vérifié dans `box2d.h` de la 3.2.0, il reste **quatre** poseurs de rappel au
> niveau du monde : `b2World_SetCustomFilterCallback`,
> `b2World_SetPreSolveCallback`, `b2World_SetFrictionCallback` et
> `b2World_SetRestitutionCallback`.
>
> La slide dit maintenant ce qui est vrai et sert le propos : le pre-solve est le
> seul endroit où l'on peut **annuler un contact au cas par cas**. Ce qui a
> disparu de la version 2, c'est le `b2ContactListener` — les contacts se lisent
> après le pas au lieu d'être reçus.
