# Exercices — GPR-UN-APU-04 — ScriptableObjects

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|GPR-UN-APU-04 - ScriptableObjects]]

Terrain de jeu : le **Dungeon Crawler** de [[GPR-UN-APU-01 - SOLID en Unity|GPR-UN-APU-01]], branche `main`, dont les statistiques d'ennemis sont écrites en `[SerializeField]` dans `Enemy` et `Spider`.

## Atelier — 20 min en classe

### 1 — Les ennemis en assets

```bash
git switch -c apu04-stats main
```

1. Créer `EnemyStats : ScriptableObject` avec `[CreateAssetMenu(menuName = "Dungeon/Enemy Stats")]`
   et les réglages aujourd'hui dispersés : `health`, `attackRange`, `attackCooldown`, `speed`,
   `detectionRadius`. Champs privés sérialisés, propriétés en lecture seule.
2. Dans `Enemy`, remplacer les trois champs par `[SerializeField] private EnemyStats stats;`
   et relire `stats.AttackRange`, `stats.AttackCooldown`. Même chose pour `speed` et
   `detectionRadius` dans `Spider`.
3. Créer l'asset `Araignée` avec les valeurs actuelles, le brancher sur le prefab, rejouer :
   rien ne doit avoir changé.
4. Créer `Araignée géante` (plus lente, plus résistante) **sans écrire de code**, et en poser
   deux dans la salle.

> [!warning] Les PV
> `health` diminue en jeu : ce n'est pas un réglage mais un **état**. Garder dans `Enemy` un
> champ `currentHealth` initialisé depuis `stats.Health` dans `Awake`, sinon toutes les
> araignées partagent la même vie — et l'asset garde les dégâts après l'arrêt du jeu.

> [!check] Réussi si
> - `Enemy` et `Spider` ne contiennent plus aucun réglage numérique sérialisé ;
> - changer la vitesse dans `Araignée.asset` pendant le jeu modifie toutes les araignées
>   normales, et aucune géante.

---

## Pour aller plus loin — à la maison

> [!todo] Overview à valider
> Pistes en deux ou trois lignes. Énoncés complets et corrigés à venir.

### Courts — valider la compréhension

#### 2 — Le loot du cours
Créer `LootData` et les quatre profils du cours (potion de soin, or, potion de mana, banco),
puis un seul prefab `Pickup` qui les utilise tous.

#### 3 — Le piège de l'exécution
Modifier une valeur de l'asset par code pendant le jeu, arrêter, constater qu'elle est
restée. Corriger avec un champ `[NonSerialized]` réinitialisé dans `OnEnable`.

#### 4 — La jauge de mana
Une `FloatValue` « Mana » écrite par le joueur et lue par une barre d'interface, sans que
l'un connaisse l'autre.

### Complet — reprendre toute la séance

#### 5 — Le catalogue d'ennemis
Un catalogue en assets (statistiques, butin, son, prefab visuel) et un générateur de vagues
qui le lit sans connaître aucun type d'ennemi. Ajouter une sixième famille en fin
d'exercice sans écrire de code. Les ennemis vivants sont tenus dans un Runtime Set.

### Difficile — se projeter

#### 6 — L'équilibrage comme donnée
Des tables d'équilibrage par difficulté, une validation (`OnValidate`) qui refuse un asset
incohérent — vitesse négative, butin manquant — et un outil d'éditeur qui liste les assets
fautifs. Faire relire l'équilibrage par quelqu'un qui ne programme pas, et corriger ce qui
l'a bloqué.
