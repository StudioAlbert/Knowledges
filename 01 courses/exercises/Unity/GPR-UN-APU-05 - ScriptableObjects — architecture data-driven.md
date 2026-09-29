# Exercices — GPR-UN-APU-05 — Observer, prévenir sans connaître

> Cours associé : [[01 courses/slides/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|GPR-UN-APU-05 - Observer, prévenir sans connaître]]

Terrain de jeu : le **Dungeon Crawler** de [[GPR-UN-APU-01 - SOLID en Unity|GPR-UN-APU-01]], branche `01-srp`, où `PlayerHealth` appelle directement `HealthBar`.

## Atelier — 20 min en classe

### 1 — La barre de vie qui n'est appelée par personne

```bash
git switch -c apu05-observer 01-srp
```

1. Dans `PlayerHealth`, supprimer le champ `healthBar` et déclarer
   `public event Action<int, int> Damaged;` (PV restants, PV max). `TakeDamage` le
   déclenche.
2. Dans `HealthBar`, ajouter une référence à `PlayerHealth`, s'abonner dans `OnEnable`,
   se désabonner dans `OnDisable`, avec une **méthode nommée**.
3. Ajouter un composant `HurtSound` qui joue un son à chaque dégât — **sans modifier**
   `PlayerHealth`.
4. En jeu, désactiver l'objet de la barre de vie, prendre un coup, le réactiver.

> [!check] Réussi si
> - `PlayerHealth` ne cite plus aucune classe d'interface ni d'audio ;
> - désactiver la barre de vie ne provoque aucune erreur dans la console ;
> - le son a été ajouté sans ouvrir `PlayerHealth.cs`.

---

## Pour aller plus loin — à la maison

> [!todo] Overview à valider
> Pistes en deux ou trois lignes. Énoncés complets, scènes de départ et corrigés à venir.

### Courts — valider la compréhension

#### 2 — L'abonné fantôme
S'abonner avec une lambda dans `OnEnable` et tenter de se désabonner avec la même lambda
dans `OnDisable`. Recharger la scène, lire l'erreur, corriger avec une méthode nommée, et
expliquer en une phrase pourquoi la première version ne retirait rien.

#### 3 — Sans le mot-clé `event`
Retirer `event` devant `Damaged` et écrire, dans un autre script, la ligne qui efface tous
les abonnés. Remettre `event` et lire l'erreur de compilation.

#### 4 — La plaque en `UnityEvent`
Transformer `PressurePlate` pour qu'elle expose un `UnityEvent` : la porte et une lumière
s'y branchent dans l'Inspector, sans code.

### Complet — reprendre toute la séance

#### 5 — L'alarme du donjon
Un canal `EventChannelFloatSO` « Bruit » : les pièges et le baril y publient une intensité.
Une jauge d'alerte, une musique qui change et les ennemis qui passent en alerte s'y
abonnent, chacun dans son propre script. Le rendu : la scène jouable, la liste des assets
de canal, et un schéma d'une page de qui publie et qui écoute.

### Difficile — se projeter

#### 6 — Traçable
Ajouter au canal générique un mode verbeux (activable dans l'Inspector) qui journalise
chaque annonce avec son émetteur et la liste de ses abonnés. Provoquer deux pannes — un
abonné détruit qui écoute encore, une annonce qui en déclenche une autre en boucle — et
montrer que le journal les trouve en moins d'une minute.
