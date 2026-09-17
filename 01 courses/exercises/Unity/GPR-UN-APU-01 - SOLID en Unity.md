# Exercices — GPR-UN-APU-01 — Atelier SOLID : Dungeon Crawler

Un projet Unity 6 jouable, écrit volontairement **sans** SOLID. Vous le refactorez principe par principe. Chaque étape a sa branche de solution, qui est aussi le point de départ de l'étape suivante :

`main` → `01-srp` → `02-ocp` → `03-lsp` → `04-isp` → `05-dip`

## Mise en place

1. Cloner le dépôt, ouvrir le projet avec Unity **6000.4** (Unity 6.4), ouvrir la scène `01 - Scenes/Dungeon`.
2. Jouer une partie. Contrôles : **WASD / flèches** pour se déplacer, **Espace** pour lancer une boule de feu, **E** pour interagir.
3. Objectif : une plaque de pression ouvre la porte du fond ; sortir par la porte. Chaque passage sur une plaque l'active ou la désactive.
4. Créer sa branche de travail : `git switch -c atelier main`.

**Règle de l'atelier :** un refactor ne change pas le comportement. Après chaque étape, rejouez la partie, puis faites un commit.

## Tour du projet (branche `main`)

| Élément | Scripts | Défaut à corriger |
|---|---|---|
| Héros | `PlayerController` | S, O |
| Araignées, archer, baril explosif | `Enemy`, `Spider`, `Archer`, `ExplodingBarrel`, `EnemyDirector` | L |
| Marchand, potion | `IEntity`, `Merchant`, `Potion` | I |
| Plaques, porte, fontaine | `PressurePlate`, `Door`, `WallFountain` | D |

Tous les scripts sont dans `Assets/03 - Scripts`, les prefabs dans `Assets/02 - Prefabs`.

## Étape 1 — Responsabilité unique : démonter `PlayerController`

**Départ :** `main` · **Solution :** `01-srp`

### Constat

Lister les **raisons de changer** de `PlayerController` : une ligne par métier.

### Étapes

1. Créer un composant par métier :
    - `PlayerMovement` : action `Move`, vitesse, retournement du sprite ; expose la dernière direction (`Facing`) ;
    - `PlayerCombat` : action `Attack`, boule de feu dans la direction `Facing` ;
    - `PlayerHealth` : PV, `TakeDamage`, `Heal`, mort, dégâts reçus ;
    - `HealthBar` : affiche les PV, posé sur `HUD/HealthLabel` ;
    - `PlayerInteractor` : action `Interact`.
2. Déclarer les dépendances entre composants avec `[RequireComponent]`.
3. Remplacer `PlayerController` par ces composants dans le prefab `Player`, puis brancher `HealthBar` dans la scène.
4. Adapter les signatures qui attendaient un `PlayerController`.

### Critères de réussite

- la partie se joue exactement comme avant
- chaque composant lit au plus une action d'input
- `HealthBar` ne connaît ni les dégâts ni les soins

### Pièges Unity

- Supprimer un script laisse un « Missing Script » sur le prefab : retirer ce composant, puis réassigner `fireballPrefab` et `healthBar`.

### Bonus

Réutiliser `PlayerHealth` sur un autre objet sans le modifier : qu'est-ce qui l'en empêche encore ?

## Étape 2 — Ouvert / fermé : un `if` par danger

**Départ :** `01-srp` · **Solution :** `02-ocp`

### Constat

Pour ajouter un nouveau danger (un chaudron brûlant, par exemple), combien de fichiers faut-il modifier ? Lesquels ?

### Étapes

1. Créer la classe abstraite `DamageSource` avec `public abstract int GetDamage();`.
2. En faire hériter `Arrow` (5 à 10) et `Explosion` (30).
3. Créer `SpikeTrap` (25), à poser sur le prefab des pics.
4. Créer `ContactDamage` (10), à poser sur la zone de morsure de l'araignée.
5. Réduire `PlayerHealth.OnTriggerEnter2D` à un seul `TryGetComponent(out DamageSource source)`.
6. Supprimer les tags de dégâts, devenus inutiles.

### Critères de réussite

- `PlayerHealth` ne contient plus aucun `CompareTag`
- les dégâts restent identiques : morsure 10, flèche 5 à 10, pics 25, explosion 30

### Pièges Unity

- `Spider` hérite déjà d'`Enemy` : pas de second héritage possible. D'où le composant `ContactDamage` : de la composition plutôt que de l'héritage.
- La boule de feu n'est pas une `DamageSource` : elle apparaît sur le héros et le blesserait.

### Bonus

Ajouter un nouveau danger. Le `git diff` du commit ne doit montrer qu'un fichier nouveau et un prefab.

## Étape 3 — Substitution de Liskov : le baril n'est pas un ennemi

**Départ :** `02-ocp` · **Solution :** `03-lsp`

### Constat

Repérer dans `Enemy`, `Archer`, `ExplodingBarrel` et `EnemyDirector` les trois symptômes d'une hiérarchie qui ment : une méthode vide, une exception, un test de type.

### Étapes

1. Créer les interfaces de capacités :
    - `IMovable` : `Move(Vector3 target)` ;
    - `IAttacker` : `AttackRange`, `AttackCooldown`, `Attack(PlayerHealth player)` ;
    - `IDamageable` : `TakeDamage(int amount)`.
2. Faire implémenter à chaque ennemi **uniquement** ce qu'il sait faire : `Spider` les trois, `Archer` `IAttacker` et `IDamageable`, `ExplodingBarrel` `IDamageable`.
3. Supprimer `Enemy`. `EnemyDirector` parcourt une liste de `IMovable` et une liste de `IAttacker`.
4. `Fireball`, `Explosion` et `Arrow` visent `IDamageable`.
5. Retirer `IEntity` des ennemis : sinon le baril retrouve un `Move` et un `Attack` impossibles.

### Critères de réussite

- plus de méthode vide, de `NotSupportedException` ni de `is ExplodingBarrel`
- une explosion de baril tue toujours l'archer voisin

### Pièges Unity

- Un ennemi détruit reste dans une liste d'interfaces : le tester avec `(Object)ennemi == null`, pas `ennemi == null`.
- Une interface n'a pas de `transform` : `((Component)attacker).transform.position`.

### Bonus

Ajouter une chauve-souris (tuile 120) qui se déplace sans attaquer, sans modifier `EnemyDirector`.

## Étape 4 — Ségrégation des interfaces : l'interface « tout-en-un »

**Départ :** `03-lsp` · **Solution :** `04-isp`

### Constat

Compter les méthodes vides que `IEntity` impose à `Merchant`, `Potion` et `PlayerHealth`.

### Étapes

1. Créer `ITalkable` (`Talk()`) et `IUsable` (`Use(PlayerHealth user)`).
2. `Merchant` implémente `ITalkable`, `Potion` implémente `IUsable`, `PlayerHealth` n'implémente plus rien.
3. Supprimer `IEntity`.
4. `PlayerInteractor` interroge chaque capacité avec `TryGetComponent`.

### Critères de réussite

- aucune méthode vide imposée par une interface
- E près du marchand joue son jingle ; E sur la potion rend 30 PV

### Bonus

Comparer les étapes 3 et 4 en deux phrases : pourquoi le remède est-il le même, et qu'est-ce qui distingue les deux problèmes ?

## Étape 5 — Inversion de dépendance : la plaque connaît chaque mécanisme

**Départ :** `04-isp` · **Solution :** `05-dip`

### Constat

Que faut-il modifier dans `PressurePlate` pour qu'une plaque abaisse une herse ?

### Étapes

1. Créer le contrat `ISwitchable` : `Activate()` et `Deactivate()`.
2. `Door` et `WallFountain` l'implémentent.
3. `PressurePlate` ne garde qu'un champ `GameObject target`, résolu en `ISwitchable` dans `Awake`.
4. `OnValidate` avertit dès l'éditeur quand la cible n'implémente pas `ISwitchable`.
5. Régler la cible de chaque plaque dans la scène.

### Critères de réussite

- `PressurePlate` ne nomme plus ni `Door` ni `WallFountain`
- une cible invalide est signalée dans l'éditeur, pas pendant la partie
- échanger les cibles des deux plaques ne demande aucune modification de code

### Pièges Unity

- Un champ de type interface n'apparaît pas dans l'Inspector : d'où le champ `GameObject` et `GetComponent<ISwitchable>()`.

### Bonus

Ajouter une herse (barrière, tuiles 76 à 78) qui bloque un passage et implémente `ISwitchable`, sans modifier `PressurePlate`.

## Pour finir

- Relire votre code avec la slide « Quand ne pas appliquer SOLID » : supprimer les abstractions qui n'ont qu'une implémentation et aucune raison d'en avoir une seconde.
- **Bonus final :** ajouter un ennemi, un piège ou un mécanisme sans modifier une seule classe existante. Le `git diff` du commit ne doit montrer que des fichiers nouveaux, des prefabs et la scène.
- Comparer votre travail avec la solution : `git diff 05-dip atelier -- "Assets/03 - Scripts"`.
