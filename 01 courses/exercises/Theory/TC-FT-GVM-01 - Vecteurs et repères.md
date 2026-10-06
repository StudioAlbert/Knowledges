# Exercices — TC-FT-GVM-01 — Vecteurs et repères

> Cours associé : [[01 courses/slides/Theory/TC-FT-GVM-01 - Vecteurs et repères|TC-FT-GVM-01 - Vecteurs et repères]]

Exercices 1 à 3 **sur papier d'abord**, puis vérifiés au clavier. Exercice 4 en C++, avec la
structure `Vector2` du cours. Arrondir à deux décimales quand ça ne tombe pas juste.

```cpp
struct Vector2 { float x, y; };

float   Norme(Vector2 v);        // √(x² + y²)
Vector2 Normaliser(Vector2 v);   // v / ‖v‖, et {0, 0} si ‖v‖ vaut 0
```

## Courts — valider la compréhension

### 1 — Du joueur à l'ennemi

> [!abstract] Objectifs
> `B − A`, norme, vecteur opposé, déplacement d'une distance donnée

Le joueur est en **(2, 1)**, l'ennemi en **(5, 5)**.

1. Donner le vecteur qui va **du joueur vers l'ennemi**, et dire quelle soustraction vous avez faite.
2. Calculer sa norme : à quelle distance l'ennemi se trouve-t-il ?
3. Le joueur décide de fuir. Donner la **direction de fuite**, normalisée.
4. Où se trouve le joueur après avoir fui de **2 unités** dans cette direction ?

```text
1. versEnnemi = (5, 5) − (2, 1) = (3, 4)
2. ‖(3, 4)‖ = √(9 + 16) = 5
3. fuite = −(3, 4) / 5 = (−0,6 ; −0,8)
4. (2, 1) + 2 · (−0,6 ; −0,8) = (0,8 ; −0,6)
```

> [!tip] Le piège du signe
> `ennemi − joueur` pointe **vers** l'ennemi, `joueur − ennemi` pointe vers le joueur. Une
> inversion ici, et le personnage court dans les bras de ce qu'il devait fuir.

### 2 — Viser juste

> [!abstract] Objectifs
> normaliser avant de multiplier par une vitesse, et voir ce que coûte l'oubli

Un projectile part de **(1, 2)**. La direction visée est donnée par le vecteur **(6, 8)**, qui
n'est pas normalisé. Le projectile vole à **4 unités par seconde**.

1. Calculer la norme de (6, 8), puis la direction **normalisée**.
2. Quel déplacement le projectile fait-il en **3 secondes** ?
3. Où arrive-t-il ?
4. Un camarade a oublié de normaliser et a écrit `position + direction × 4 × 3`. Où son
   projectile arrive-t-il, et de combien s'est-il trompé ?

```text
1. ‖(6, 8)‖ = 10        normalisée : (0,6 ; 0,8)
2. (0,6 ; 0,8) × 4 × 3 = (7,2 ; 9,6)      soit 12 unités parcourues
3. (1, 2) + (7,2 ; 9,6) = (8,2 ; 11,6)
4. (1, 2) + (6, 8) × 12 = (73, 98) — il a parcouru 120 unités au lieu de 12
```

> [!tip] Pourquoi c'est l'erreur la plus fréquente
> Sans normalisation, la vitesse réelle dépend de la longueur du vecteur de direction : plus
> la cible est loin, plus le projectile va vite. Le jeu devient incontrôlable sans qu'aucune
> ligne n'ait l'air fausse.

### 3 — Résoudre un déplacement

> [!abstract] Objectifs
> somme de vecteurs, vitesse résultante, position après un temps donné, cas d'annulation

Un vaisseau part de **(0, 0)**. Son moteur le pousse à **(3, 1)** unités par seconde, et le
courant le pousse à **(−1, 2)** unités par seconde.

1. Quelle est sa **vitesse résultante** ? Détailler la somme composante par composante.
2. À quelle vitesse avance-t-il **réellement** ? Comparer à la vitesse du moteur seul.
3. Où se trouve-t-il après **2 secondes** ?
4. Quel courant faudrait-il pour que le vaisseau **reste sur place**, moteur à fond ?

```text
1. (3, 1) + (−1, 2) = (3 − 1 ; 1 + 2) = (2, 3)
2. ‖(2, 3)‖ = √13 ≈ 3,61    moteur seul : ‖(3, 1)‖ = √10 ≈ 3,16
   le courant le pousse plus vite — mais pas là où il voulait aller
3. (0, 0) + (2, 3) × 2 = (4, 6)
4. l'opposé de la poussée : (−3, −1), et la résultante devient le vecteur nul
```

> [!tip] À remarquer
> La vitesse résultante est **plus grande** que celle du moteur, alors qu'une des deux
> composantes du courant est négative : ‖u + v‖ ne se déduit pas de ‖u‖ et ‖v‖.

## Complet — reprendre toute la séance

### 4 — Le vaisseau, la poussée et le courant

> [!abstract] Objectifs
> toutes les opérations de la séance dans une boucle de simulation : soustraire pour viser,
> normaliser, multiplier par une vitesse, additionner pour composer, mesurer pour s'arrêter

Le vaisseau de l'exercice 3, mais cette fois il **se dirige tout seul** vers une cible, pas à
pas, pendant que le courant le pousse.

1. Écrire la structure `Vector2` et les fonctions `Ajouter`, `Soustraire`, `Multiplier`
   (par un scalaire), `Norme` et `Normaliser`. Chacune tient sur une ligne.
2. Poser l'état de départ : `position` en (0, 0), `cible` en (20, 10), `courant` de
   (−1 ; 0,5), moteur à **4 unités par seconde**, pas de temps `dt` de **0,5 s**.
3. Écrire la boucle. À chaque pas :
   - `versCible = cible − position`, et sa norme est la **distance restante** ;
   - si cette distance est inférieure à **0,5**, afficher `Arrive !` et sortir ;
   - `direction = Normaliser(versCible)` ;
   - `vitesse = direction × moteur + courant` ;
   - `position = position + vitesse × dt`.
4. Afficher à chaque pas le temps écoulé, la position et la distance restante.
5. Borner la boucle à 40 pas, pour qu'elle se termine toujours.

```text
t =  0.0 s   position (  0.00,   0.00)   reste 22.36
t =  0.5 s   position (  1.29,   1.14)   reste 20.70
t =  1.0 s   position (  2.60,   2.25)   reste 19.05
...
t =  6.0 s   position ( 16.75,  10.07)   reste  3.25
t =  6.5 s   position ( 18.25,  10.28)   reste  1.77
t =  7.0 s   position ( 19.72,  10.21)   reste  0.35
Arrive !
```

**Puis répondre, en modifiant le programme :**

6. Remplacer le courant par **(−5 ; 0)**, plus fort que le moteur. Le vaisseau arrive-t-il ?
   Que fait la distance restante au fil des pas, et pourquoi la borne de 40 pas sert-elle ?
7. Supprimer l'appel à `Normaliser`. Que devient le déplacement du premier pas, et pourquoi ?
8. Que se passerait-il si la position de départ était **exactement** la cible ? Quelle ligne
   du programme empêche la catastrophe ?

> [!tip] Vérification de l'étape 6
> La distance ne diminue jamais : elle passe de 22,36 à plus de 40 en vingt secondes. Le
> vaisseau pousse vers la cible de toutes ses forces et **recule quand même** — c'est
> exactement ce que fait un personnage sur un tapis roulant trop rapide.

