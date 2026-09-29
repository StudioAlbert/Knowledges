---
title: GPR-UN-APU-04 - ScriptableObjects
type: slides
status: Backlog
subject: Unity
duration_h: 1
bloc_gsda: Architecture et Patterns Unity
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: false
---

# Scriptable Objects
<!-- .slide: class="title" -->

### Les données hors du code, partagées par tous

<small>GPR-UN-APU-04 · Architecture et Patterns Unity</small>

Note:
Deck créé le 28.09 depuis `lectures/Unity/scriptable_objects.md` (le plan en
dungeon : loot, armes, valeurs, runtime set) et les sources Unity citées en
fin de deck. Une seule séance pour tout le sujet : les canaux d'événement
sont en APU-05, avec l'Observer.

---

## Objectifs

- Sortir les réglages du code vers des **assets**
- créer un `ScriptableObject` et son entrée de menu
- partager une valeur ou une liste entre objets et scènes
- connaître le piège de l'état qui persiste

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-APU-01 - SOLID en Unity|GPR-UN-APU-01]] — Dungeon Crawler, branche `main`.

---

## Le problème : 
### les chiffres vivent dans les scripts et les prefabs

- rééquilibrer une araignée = ouvrir un prefab, ou pire, un script
- vingt ennemis = vingt copies des mêmes valeurs
- une variante = un prefab dupliqué, qui diverge tout seul
- le game designer attend un programmeur

Note:
Dans le Dungeon Crawler, `Enemy` porte `health`, `attackRange`,
`attackCooldown` en `[SerializeField]`, et `Spider` ajoute `speed` et
`detectionRadius`. Chaque instance posée dans la scène stocke sa propre copie.

---

## Un asset qui ne contient que des données

- un `ScriptableObject` est un **fichier du projet**, pas un objet de la scène
- pas de `Transform`, pas de `Update` : des champs, éventuellement des méthodes
- il se crée, se duplique et se règle comme un matériau
- tout le monde peut y **faire référence**, depuis n'importe quelle scène

Note:
Manuel Unity : « un conteneur de données partagées par plusieurs objets à
l'exécution, qui réduit la mémoire utilisée en évitant les copies de
valeurs ». C'est le pattern Flyweight : cent araignées, un seul jeu de
statistiques en mémoire.

---

## Asset ou instance de scène
<!-- .slide: class="schema" -->

L'asset existe une fois dans le projet ; les instances le **référencent**.

![[apu04_asset_instances.svg]]

Note:
Les flèches partent toujours de la scène vers l'asset : un asset ne peut
pas pointer un objet de scène (il n'existe pas encore quand l'asset est
chargé). Modifier `Araignée.asset` change les trois premières araignées
d'un coup.

---

## Créer le sien

Une classe qui hérite de `ScriptableObject`, et un attribut pour l'ajouter au menu *Create*.

```csharp
using UnityEngine;

[CreateAssetMenu(menuName = "Dungeon/Loot", fileName = "Loot")]
public class LootData : ScriptableObject
{
    [SerializeField] private int mana;
    [SerializeField] private int health;
    [SerializeField] private Vector2Int money;   // min, max

    public int Mana => mana;
    public int Health => health;
    public int RollMoney() => Random.Range(money.x, money.y + 1);
}
```

Note:
Clic droit dans le Project → Create → Dungeon → Loot. Les champs privés
sérialisés + propriétés en lecture seule : le designer règle dans
l'Inspector, le code ne peut que lire.

---

## Un asset par profil

Même classe, quatre fichiers : aucune ligne de code en plus.

| Asset | Mana | Santé | Argent |
|---|:-:|:-:|:-:|
| `HealthPotion` | 0 | 10 | 0 – 0 |
| `Gold` | 0 | 0 | 5 – 10 |
| `ManaPotion` | 2 | 0 | 0 – 0 |
| `Banco` | 3 | 25 | 10 – 50 |

Note:
Tableau repris du synopsis de `scriptable_objects.md`. Faire créer
`Banco` en direct : dupliquer `Gold`, changer trois valeurs, c'est fini.

---

## S'en servir

Le prefab garde une **référence** vers l'asset, réglée dans l'Inspector.

```csharp
public class Pickup : MonoBehaviour
{
    [SerializeField] private LootData loot;

    void OnTriggerEnter2D(Collider2D other)
    {
        if (!other.TryGetComponent(out PlayerHealth player)) return;

        player.Heal(loot.Health);
        Destroy(gameObject);
    }
}
```

Note:
Un seul prefab `Pickup`, quatre assets : la potion, l'or, le banco sont le
même objet avec une donnée différente. `PlayerHealth.Heal` existe sur la
branche `01-srp` du Dungeon Crawler.

---

## Ce qu'un designer peut en faire

- régler sans ouvrir de code, **pendant** le jeu
- dupliquer un asset pour créer une variante
- comparer deux profils côte à côte dans l'Inspector
- versionner les réglages : un asset = un fichier texte dans Git

Note:
Les `.asset` sont du YAML : un diff Git montre exactement quelle valeur a
changé et qui l'a changée.

---

# Partager à l'exécution
<!-- .slide: class="title" -->

---

## La variable partagée

Un asset qui contient une valeur : le joueur l'écrit, l'interface la lit, aucun ne connaît l'autre.

```csharp
[CreateAssetMenu(menuName = "ScriptableValues/Float")]
public class FloatValue : ScriptableObject
{
    [SerializeField] private float initialValue;
    [System.NonSerialized] private float value;

    public float Value { get => value; set => this.value = value; }

    void OnEnable() => value = initialValue;
}
```

Note:
Assets `HealthValue`, `ManaValue`, `GoldValue` depuis le même menu. Le
`[NonSerialized]` + `OnEnable` sont la réponse au piège de la slide
suivante : la valeur de jeu n'est jamais écrite dans l'asset.
Première étape vers les canaux d'événement d'APU-05 : ici, l'interface
doit encore relire la valeur ; là-bas, on la prévient.

---

## Le piège : l'état qui persiste

- dans l'**éditeur**, une valeur changée en Play mode **reste** changée après l'arrêt
- dans un **build**, l'asset est en lecture seule : tout est perdu à la fermeture
- une partie qui démarre peut donc hériter de la précédente
- parade : valeur de jeu non sérialisée, remise à zéro explicite

Note:
Manuel Unity : « dans l'éditeur, on peut enregistrer des données dans un
ScriptableObject en Edit mode et en Play mode » ; « dans un Player
autonome, on ne peut que lire les données enregistrées ». Conséquence :
un ScriptableObject n'est **pas** un système de sauvegarde.
Démo : modifier `initialValue` pendant le jeu, arrêter, constater.

---

## Le Runtime Set

Une liste tenue à jour par ceux qui y entrent et en sortent : plus besoin de `FindObjectsByType`.

```csharp
[CreateAssetMenu(menuName = "ScriptableValues/Runtime Set")]
public class EnemySet : ScriptableObject
{
    private readonly List<Enemy> items = new();
    public IReadOnlyList<Enemy> Items => items;

    public void Add(Enemy enemy)    { if (!items.Contains(enemy)) items.Add(enemy); }
    public void Remove(Enemy enemy) => items.Remove(enemy);
}
```

Note:
Chaque ennemi fait `set.Add(this)` dans `OnEnable` et `set.Remove(this)`
dans `OnDisable`. L'`EnemyDirector` du Dungeon Crawler, qui fait
aujourd'hui un `FindObjectsByType<Enemy>()` au `Start`, lirait
`set.Items` à la place — et verrait les ennemis apparus en cours de
partie. Même idée pour l'inventaire (`List<LootData>` du support d'origine).

---

## Ce qu'on y met, ce qu'on n'y met pas

| Oui | Non |
|---|---|
| réglages d'équilibrage | l'état d'une partie à **sauvegarder** |
| profils d'ennemis, d'armes, de loot | une référence à un objet de **scène** |
| tables de dialogue, de niveaux | du code qui dépend d'une scène |
| valeurs partagées **réinitialisées** | tout, par principe |

Note:
La dernière ligne compte : un projet où chaque booléen est un asset devient
aussi illisible qu'un `GameManager` de mille lignes.

---

## Atelier — 20 min

Sortir les statistiques des ennemis du Dungeon Crawler vers des assets, puis créer une araignée géante sans écrire de code.

Note:
Énoncé : [[01 courses/exercises/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|exercice 1]].
Branche `main`. Critère : `Enemy` et `Spider` ne contiennent plus aucun
réglage numérique en `[SerializeField]`, seulement une référence
`EnemyStats`.

---

## À retenir

- un `ScriptableObject` est un **asset de données**, partagé par référence
- `[CreateAssetMenu]` : une variante = un asset, zéro ligne de code
- valeurs partagées et runtime sets découplent les objets et les scènes
- dans l'éditeur, ce qui est modifié en jeu **reste** modifié

---

## Ressources

- [ScriptableObject — Manuel Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html)
- [Create modular game architecture in Unity with ScriptableObjects — e-book Unity](https://unity.com/resources/create-modular-game-architecture-with-scriptable-objects-ebook) et son [projet démo](https://unity.com/how-to/get-started-with-scriptableobjects-demo)
- [Separate game data and logic with ScriptableObjects — Unity](https://unity.com/how-to/separate-game-data-logic-scriptable-objects)
- [Unite Austin 2017 — Game Architecture with Scriptable Objects](https://www.youtube.com/watch?v=raQ3iHhE_Kk) (Ryan Hipple)
- Suite : [[GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|GPR-UN-APU-05 — Observer]], où les ScriptableObjects deviennent des canaux d'événement
