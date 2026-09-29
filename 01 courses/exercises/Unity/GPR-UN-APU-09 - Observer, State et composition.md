# Exercices — GPR-UN-APU-09 — State, un pattern de gameplay

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-09 - Observer, State et composition|GPR-UN-APU-09 - State, un pattern de gameplay]]

Terrain de jeu : le **Dungeon Crawler** de [[GPR-UN-APU-01 - SOLID en Unity|GPR-UN-APU-01]], branche `main`.

## Atelier — 20 min en classe

### 1 — L'araignée a quatre états

Aujourd'hui, le comportement de l'araignée est éclaté entre `Spider.Move` (poursuivre si le
héros est à moins de `detectionRadius`) et `EnemyDirector.Update` (mordre si le héros est à
portée et que le délai `AttackCooldown` est écoulé). Ses états existent, mais aucun ne porte
de nom.

1. **Au papier, 5 min.** Dessiner la machine de l'araignée avec quatre états — **Repos**,
   **Poursuite**, **Morsure**, **Récupération** — et nommer chaque transition par sa
   condition (distance, portée, fin de morsure, délai écoulé).
2. **En code, 15 min.** Depuis la branche `main`, créer sa branche :
   ```bash
   git switch -c apu09-araignee main
   ```
   Dans `Spider`, déclarer `enum SpiderState { Idle, Chase, Bite, Recover }` et un champ
   `state`, puis écrire un `Update` en `switch` qui applique **exactement** votre dessin.
   Retirer l'araignée de `EnemyDirector` (`if (enemy is Spider) continue;`) : elle se pilote
   seule désormais, et retrouve le héros par `FindAnyObjectByType<PlayerController>()` dans
   `Start`. Vérifier en jeu que le comportement n'a pas changé.
3. **À la maison.** Remplacer le `switch` par une classe `IState` par état et la
   `StateMachine` du cours. Le rendu : le dessin, et le lien vers la branche poussée.

> [!tip] Pour vérifier son dessin
> Chaque flèche du dessin doit correspondre à exactement un `state = …` dans le code, et
> réciproquement. S'il y a un `state = …` sans flèche, c'est le dessin qui est faux.

---

## Pour aller plus loin — à la maison

> [!todo] Overview à valider
> Pistes en deux ou trois lignes. Énoncés complets, scènes de départ et corrigés à venir.

### Courts — valider la compréhension

#### 2 — Le héros du cours
Coder la machine du héros de platformer (Idle, Course, Saut, Chute) sur un cube, avec un
`Debug.Log` dans chaque `Enter` et `Exit`, puis ajouter la transition manquante Idle → Saut.

#### 3 — Le menu en états
Quatre panneaux d'UI (Titre, Menu, Options, Pause) : un état par panneau, `Enter` l'affiche,
`Exit` le cache. Aucun `SetActive` ailleurs que dans les états.

#### 4 — Un QTE
Une invite qui demande une touche tirée au sort en 1,5 s ; réussite et échec sont deux
états. Enchaîner trois invites.

### Complet — reprendre toute la séance

#### 5 — Le duel au tour par tour
Deux camps de trois unités sur une grille. La partie est une machine (début de manche, tour
du joueur, tour ennemi, fin de manche, fin de partie) ; chaque unité a la sienne (en attente,
active, a joué). Le tour ennemi joue au hasard. Le rendu : la scène jouable et le schéma des
deux machines.

### Difficile — se projeter

#### 6 — Le boss qui change de phase
Un boss à trois phases, chacune étant elle-même une machine à états (machine hiérarchique),
avec des transitions déclenchées par un seuil de PV, un chrono et la mort d'un sbire.
Contrainte : ajouter une quatrième phase ne demande aucune modification des trois autres.
