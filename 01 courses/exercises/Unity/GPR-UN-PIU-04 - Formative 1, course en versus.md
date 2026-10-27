# Exercices — GPR-UN-PIU-04 — Formative 1 : course en versus

> [!info] Terrain de jeu
> **Votre propre dépôt**, celui créé en séance 7 — pas de projet fourni. Unity **6000.3**,
> template 3D (URP), la version posée au Hub en séance 1.
>
> Assets libres, à importer et à ranger comme en séance 2 :
> [Car Kit](https://kenney.nl/assets/car-kit) et
> [City Kit (Roads)](https://kenney.nl/assets/city-kit-roads) de Kenney.
> Référence de gameplay : [Micro Machines](https://youtu.be/NCOpOhL19Xg).
>
> **Ce qui est supposé acquis** : séances 2, 5, 6, 7, 8, 9, 10, 11 et 12. Rien d'autre.
> Vous n'avez pas encore vu le tir, les coroutines ni l'interface : la fiche en tient compte.

**Temps encadré** : les workshops des séances 9 à 12, plus **2 créneaux spécifiques** le
vendredi 18 décembre. Terminé à la maison pendant la fermeture d'hiver.

## Ce qui est demandé

Un jeu de course à deux, sur un écran, qui tient 5 à 10 minutes.

### 1 — Le circuit et la caméra · *[Apply]*

Un parcours fermé, **entièrement composé de prefabs** — un prefab de segment de route, un de
virage, un d'obstacle de décor — et une **caméra orthographique fixe vue de dessus** qui cadre
le circuit entier et les deux véhicules pendant toute la partie. Pas de caméra qui suit, pas
d'écran partagé.

### 2 — La conduite · *[Apply]*

Un véhicule en `Rigidbody` : gauche et droite font **pivoter**, avant et arrière **accélèrent
et freinent**. Un **boost** à l'impulsion, avec un temps de recharge.

> [!warning] Deux pièges de la séance 9
> Les forces s'appliquent dans `FixedUpdate`, jamais dans `Update` : sinon la voiture accélère
> plus vite sur une machine rapide. Et une voiture qui décolle au premier trottoir a son centre
> de masse trop haut ou ses rotations non contraintes — regardez `Rigidbody.centerOfMass` et
> les contraintes d'axes avant de baisser la force.

### 3 — Deux joueurs sur un écran · *[Apply]*

Joueur 1 au clavier (ZQSD **et** flèches), joueur 2 à la manette. **Une seule action map, un
seul script de contrôle** : si vous dupliquez le code d'entrée pour le second joueur, le
critère n'est pas acquis. Passez par `PlayerInputManager` et le pairing de périphériques.

Gérez la **déconnexion de manette en cours de course** : la partie se met en pause et affiche
de quoi réassocier le joueur. C'est le sujet du workshop accompagné de la séance 11.

### 4 — Les collisions · *[Analyze]*

Véhicule contre véhicule et véhicule contre décor. Les deux voitures se poussent sans
s'interpénétrer et sans partir en orbite. Qualifiez ce que vous touchez **par composant, avec
`TryGetComponent`**, pas par une chaîne de `CompareTag`.

### 5 — Les réglages hors du code · *[Apply]*

Vitesse maximale, couple de rotation, force de boost, temps de recharge, masse, drag : tous en
`[SerializeField]` avec un `[Range]` quand la valeur a des bornes. **Quelqu'un doit pouvoir
régler la conduite sans ouvrir un seul fichier.**

## Bonus

Dans l'ordre de ce qu'ils rapportent :

- **Checkpoints et tours** — des triggers posés sur le circuit, un compte de tours par joueur,
  un classement, une condition de victoire, et un anti-triche minimal : franchir les
  checkpoints dans l'ordre.
- **Obstacles de décor réactifs** — caisses qui se renversent, barrières qui cèdent.
- **Tir et power-ups** — attendez les séances 21 et 23 ; à faire après le jalon si le sujet
  vous tient.

## Barème — sur 20

| Critère | Pts | Non acquis | En cours | Acquis |
|---|---|---|---|---|
| Circuit et caméra | 4 | Scène posée à la main, objets dupliqués | Prefabs présents mais le cadrage perd un joueur | Tout en prefabs, le circuit entier et les deux voitures toujours visibles |
| Conduite | 4 | Déplacement en `Transform`, ou forces dans `Update` | Conduite correcte mais la voiture décolle ou glisse sans contrôle | Conduite lisible et stable, boost avec recharge, tenue de route réglée |
| Deux joueurs | 5 | Un seul joueur, ou deux scripts de contrôle | Deux joueurs mais déconnexion non gérée | Une action map, un script, les deux périphériques, déconnexion et réassociation |
| Réglages hors du code | 3 | Valeurs en dur | Partiellement exposé | Toute la conduite réglable dans l'Inspector, bornes posées |
| Dépôt et livraison | 4 | Dépôt absent ou `Library/` commité | Dépôt propre mais README muet | `.gitignore` et `.gitattributes` corrects, branche dédiée, README qui dit quoi jouer et comment |

## Livrables

Sur **votre dépôt GitHub** de la séance 7, pas sur le NAS :

```bash
git switch -c formative-1-course
# ... votre travail, en commits lisibles
git push -u origin formative-1-course
```

À la racine du dépôt, un `README.md` qui dit, en une page : **les contrôles des deux joueurs**,
ce qui est fait, ce qui ne l'est pas, les bugs connus, et les bonus tentés. Rien d'autre à
rendre : c'est le dépôt qui est corrigé.

> [!check] Réussi si
> - Un camarade clone le dépôt, ouvre la scène et joue à deux **sans vous poser de question** ;
> - le second joueur fonctionne sans qu'une ligne de code d'entrée ait été dupliquée ;
> - débrancher la manette en pleine course ne casse ni la partie ni la console ;
> - deux voitures qui se percutent se poussent et restent au sol ;
> - vous changez la force de boost dans l'Inspector, en jeu, et la différence se sent.
