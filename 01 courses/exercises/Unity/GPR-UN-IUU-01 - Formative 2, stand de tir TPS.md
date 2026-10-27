# Exercices — GPR-UN-IUU-01 — Formative 2 : stand de tir en vue 3e personne

> [!info] Terrain de jeu
> Le **companion du module, scène `08-Depart-TPS`** : un blockout de zone de tir, un personnage
> Mixamo rigué en Humanoid, les Input Actions déjà déclarées, un Cinemachine Brain et une
> caméra virtuelle posée — et **aucune logique de contrôle, de visée ni de tir**. Tout ce qui
> compte reste à écrire.
>
> **Les Starter Assets de l'Asset Store sont interdits.** Ils fournissent précisément le
> controller, la caméra, le câblage d'entrée et l'Animator que cette formative évalue : les
> importer revient à rendre une copie. Le companion existe pour vous donner le décor et le rig
> sans vous donner la réponse.
>
> **Ce qui est supposé acquis** : séances 4, 6, 9, 12, 13, 14, 15, 16, 17, 18 et 19.
> Vous n'avez pas encore vu les coroutines, le tir par projectile ni les menus.

**Temps encadré** : les workshops des séances 15 à 19, plus **2 créneaux spécifiques** le
jeudi 28 janvier. Terminé à la maison.

## Ce qui est demandé

Le joueur se déplace dans la zone et abat toutes les cibles avant la fin du chrono.
**Victoire** : toutes les cibles touchées à temps. **Défaite** : le chrono arrive à zéro.

### 1 — Le déplacement · *[Apply]*

Marcher, courir, sauter, regarder autour de soi au clavier et à la souris. Déplacement en
`Rigidbody` ou en `CharacterController` — votre choix, mais sachez le défendre.

### 2 — Le test de sol · *[Analyze]*

Un `isGrounded` qui **ne se déclenche pas quand le joueur frotte un mur**. C'est le piège
nommé en séance 13 : un rayon unique vers le bas ne suffit pas dès qu'il y a deux colliders,
et un `OnCollisionExit` naïf rend le saut aléatoire. Montrez dans le README le cas que votre
version gère et que la version naïve rate.

### 3 — L'animation · *[Apply]*

Un Animator qui suit l'état de gameplay : repos, marche, course, saut, chute, visée. L'état
d'animation est **lu depuis le gameplay, jamais dupliqué** — pas de `bool isRunning` tenu à
deux endroits qui finissent par diverger.

### 4 — La caméra · *[Apply]*

Une caméra à l'épaule, derrière et légèrement au-dessus du personnage, pilotée à la souris,
en Cinemachine. Elle ne doit pas traverser les murs du blockout.

### 5 — Le tir · *[Apply]* puis *[Evaluate]*

Un tir instantané au raycast, un réticule au centre de l'écran, un retour visible à l'impact.
Les cibles sont **fixes, en nombre connu (8 à 12)**, dissimulées dans le décor mais **toutes
atteignables** : vérifiez-le vous-même avant de rendre.

Puis, en trois à cinq lignes dans le README : **le rayon part-il de la caméra ou du canon de
l'arme, et pourquoi ?** Les deux choix sont défendables et donnent des jeux différents. Dites
ce que le vôtre coûte — le cas où le réticule annonce une touche que l'arme ne peut pas faire,
ou l'inverse.

### 6 — L'interface · *[Apply]*

En uGUI, avec un `HudManager` comme en séance 19 : un **chrono décroissant**, un **compteur de
cibles restantes**, et les deux écrans de fin. Le jeu appelle `SetTimer` et `SetTargetsLeft` ;
il ne connaît aucun élément de Canvas, et le HUD ne va rien chercher par `Find`.

### 7 — Les réglages hors du code · *[Apply]*

C'est une exigence explicite du brief d'origine : **toutes les valeurs de gameplay du contrôle
se règlent dans l'éditeur, sans toucher au code.** Vitesse de marche et de course, hauteur de
saut, sensibilité de la souris, portée et cadence de tir, durée du chrono, nombre de cibles.

## Bonus

- **Système de couverture** — se coller à un mur, tirer par-dessus, la caméra qui suit.
- **Orientation du buste vers la cible** — une passe d'IK, même approximative.
- **Blockout ProBuilder** — refaire la zone vous-même au lieu d'utiliser celle du companion.
- **Cibles mobiles** — une patrouille simple, sans NavMesh, qui n'est pas au programme.

## Barème — sur 20

| Critère | Pts | Non acquis | En cours | Acquis |
|---|---|---|---|---|
| Déplacement et test de sol | 4 | Le joueur flotte, traverse, ou saute contre un mur | Déplacement correct, `isGrounded` fragile | Déplacement net, test de sol que le mur ne trompe pas, cas documenté |
| Animation | 4 | Pas d'Animator, ou animations désynchronisées | Transitions présentes mais état dupliqué | Animator piloté depuis l'état de gameplay, une seule source de vérité |
| Caméra | 3 | Caméra fille du personnage, sans Cinemachine | VCam posée mais traverse le décor | Caméra à l'épaule réglée, collider actif, confortable à jouer |
| Tir et cibles | 5 | Pas de raycast, ou cibles inatteignables | Tir fonctionnel, réticule et impact approximatifs | Tir précis, réticule juste, toutes les cibles trouvables, choix du point d'origine justifié |
| Interface et réglages | 4 | Valeurs en dur, HUD câblé par `Find` | HUD complet mais couplé au jeu | `HudManager` découplé, chrono et compteur justes, tout le contrôle réglable dans l'Inspector |

## Livrables

```bash
gh repo fork <le-companion-du-module> --clone
cd <le-clone>
git switch -c formative-2-tps
# ... votre travail
git push -u origin formative-2-tps
```

Un `README.md` à la racine : les contrôles, le cas de test de sol que vous gérez, la
justification du point d'origine du rayon, ce qui est fait et ce qui ne l'est pas, les bonus
tentés.

> [!check] Réussi si
> - On joue avec le clavier et la souris sans mode d'emploi ;
> - sauter en frottant un mur ne marche pas, et sauter sur une pente marche ;
> - l'animation ne se décale jamais de ce que fait le personnage ;
> - les cibles sont cachées mais on les trouve toutes sans fouiller la hiérarchie ;
> - le chrono tombe à zéro et l'écran de défaite s'affiche, une fois, proprement ;
> - vous doublez la vitesse de course depuis l'Inspector, en jeu, sans recompiler.
