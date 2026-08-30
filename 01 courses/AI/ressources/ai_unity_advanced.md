---
title: Unity Advanced — Static classes & Singleton
type: ressource
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
source_slides: https://docs.google.com/presentation/d/1UdWkuQDiRLKUcL6KLw971OaxbBGgTYaLGTaSxFqRjes/edit
---

# Unity advanced
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

### Static classes

<small>Singleton · service locator</small>

Note:
Ce deck est le n° 10 de la série Drive, donc importé avec le module AI — mais son
contenu ne parle pas d'IA du tout : c'est un cours d'architecture Unity. Il est
rangé en `ressources/` et non en `cours/` pour cette raison, et il recouvre
[[singletons_in_unity]], déjà dans le vault et plus complet (6 h, avec code et
captures). Voir la note d'import dans `02 Notes/Historique`.

---

# Singleton
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

### Ensure a class has one instance, and provide a global point of access to it.

<small>La définition du Gang of Four, mot pour mot. Les deux moitiés de la phrase
sont deux responsabilités distinctes — et c'est là que tout se joue.</small>

Note:
Faire remarquer que la définition mélange deux choses : *garantir l'unicité* et
*offrir un accès global*. On veut presque toujours la première ; c'est la seconde
qui pose problème.

---

# Everyone can access
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

### Everyone can make mess happen

<small>Un point d'accès global, c'est un couplage global : n'importe quelle
classe peut modifier l'état, et plus rien ne dit qui l'a fait.</small>

Note:
C'est l'argument central du chapitre de *Game Programming Patterns* : le
singleton est une variable globale à laquelle on a mis une cravate.

---

# Singleton Player Object
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

### Only one? What if I need two…

<small>Le jour où le jeu passe en écran splitté, le `Player.Instance` devient
une dette. Et ce jour arrive toujours.</small>

Note:
Exemple canonique à donner : le mode deux joueurs demandé en fin de projet. Le
singleton n'était pas faux, il encodait une hypothèse de design comme une
contrainte de code.

---

# Service Locator
<!-- .slide: data-background="00 images/01_slide_GP_GA_22_08_22.jpg" -->

L'alternative présentée dans le deck : au lieu que chaque classe expose sa
propre instance, un **registre** rend un service à la demande.

```text
   ServiceLocator.Get<IAudioService>()
        |
        `-- retourne l'implémentation enregistrée au démarrage
```

<small>On garde le point d'accès unique, on retrouve la possibilité de
substituer l'implémentation — pour les tests, ou pour une version muette.</small>

Note:
Ce n'est pas une solution miracle : le couplage global reste, il est simplement
déplacé vers une interface. C'est l'étape intermédiaire honnête avant
l'injection de dépendances.

---

# References
<!-- .slide: data-background="00 images/01_slide_fond_GP_22_08_22.jpg" -->

- `fr.wikipedia.org/wiki/Singleton_(patron_de_conception)`
- `gamedevbeginner.com/singletons-in-unity-the-right-way/`
- `gameprogrammingpatterns.com/singleton.html`

<small>Cours complet déjà dans le vault : [[singletons_in_unity|Singletons in Unity]]
(6 h, bloc *Architecture et Design Patterns*).</small>
