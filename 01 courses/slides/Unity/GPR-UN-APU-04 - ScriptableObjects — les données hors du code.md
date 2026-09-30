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
publish: true
---

# Scriptable Objects
<!-- .slide: class="title" -->

### Les données hors du code, partagées par tous

<small>GPR-UN-APU-04 · Architecture et Patterns Unity</small>

Note:
Deck réécrit le 01.10 sur le projet companion « stand de tir », qui remplace
les exemples Dungeon Crawler. Tous les extraits sont copiés du projet, sans
retouche : on peut ouvrir le fichier pendant le cours.
Les canaux d'événement restent en APU-05, avec l'Observer.

---

## Objectifs

- reconnaître **cinq usages** distincts du `ScriptableObject`
- sortir les réglages du code vers des **assets**
- partager une valeur, une référence, un état, une liste
- connaître le piège de l'état qui persiste

**Projet :** [GPR_UN_APU_04_ScriptableObjects](https://github.com/StudioAlbert/GPR_UN_APU_04_ScriptableObjects) — trois tourelles, six cibles, une boutique.

Note:
Insister d'entrée : ce n'est pas « un » pattern, c'est une brique qui sert à
cinq choses différentes. La confusion habituelle vient de là — on croit avoir
compris parce qu'on a fait un fichier de stats, et on ne voit pas les autres.

---

## Un asset qui ne contient que des données

- un `ScriptableObject` est un **fichier du projet**, pas un objet de la scène
- pas de `Transform`, pas d'`Update` : des champs, parfois des méthodes
- il se crée, se duplique et se règle comme un matériau
- tout le monde peut y **faire référence**, depuis n'importe quelle scène

Note:
Manuel Unity : « un conteneur de données partagées par plusieurs objets à
l'exécution, qui réduit la mémoire utilisée en évitant les copies de valeurs ».
C'est le pattern Flyweight : six cibles, un seul jeu de réglages en mémoire.

---

## Créer le sien

Une classe qui hérite de `ScriptableObject`, et un attribut pour l'ajouter au menu *Create*.

```csharp
[CreateAssetMenu(menuName = "Turrets/Turret Profile", fileName = "TurretProfile")]
public class TurretProfile : ScriptableObject
{
    [SerializeField] private string _displayName = "Tourelle";
    [SerializeField, Min(1)] private int _damage = 10;

    public string DisplayName => _displayName;
    public int Damage => _damage;
}
```

Champs privés sérialisés, propriétés en **lecture seule** : le designer règle dans l'Inspector, le code ne peut que lire.

Note:
Clic droit dans le Project → Create → Turrets → Turret Profile.
Montrer que le `.asset` produit est du YAML lisible : un diff Git dira
exactement quelle valeur a changé, et qui l'a changée.

---

## Usage 1 — Le préréglage
### Le problème

- cadence, dégâts, chargeur, coût de rechargement en `[SerializeField]` sur la tourelle
- trois tourelles = **trois copies** des mêmes valeurs, qui divergent toutes seules
- une variante = un prefab dupliqué, qui divergera aussi
- le game designer attend un programmeur

Note:
Faire le compte à voix haute : neuf réglages × trois tourelles = vingt-sept
nombres à tenir cohérents à la main. Personne ne le fait.

---

## Tout le réglage dans un asset

```csharp
public class TurretProfile : ScriptableObject
{
    [SerializeField] private string _displayName = "Tourelle";
    [SerializeField] private Color _color = Color.white;

    [SerializeField, Min(0.1f)] private float _shootingRate = 2f;
    [SerializeField, Min(1)] private int _damage = 10;
    [SerializeField, Min(1f)] private float _range = 40f;

    [SerializeField, Min(1)] private int _magazineSize = 12;
    [SerializeField, Min(0.1f)] private float _reloadDuration = 1.5f;
    [SerializeField, Min(0)] private int _reloadCost = 5;

    /// <summary>Délai entre deux tirs, déduit de la cadence.</summary>
    public float ShotInterval => 1f / _shootingRate;
}
```

<small>Projet : `03 - Scripts/Data/TurretProfile.cs`</small>

Note:
Le point qui porte : après ça, `Turret.cs` ne contient plus **aucun** nombre de
gameplay. Ouvrir le fichier et chercher un chiffre — il n'y a que des durées de
montage (vitesse de rotation, durée du trait de tir), ce qui est un autre sujet.
`ShotInterval` montre qu'un SO a le droit de calculer, pas seulement de stocker.

---

## Trois assets, zéro ligne de code

| | Mk I | Mk II | Mk III |
|---|:-:|:-:|:-:|
| dégâts | 1 | 3 | 10 |
| cadence (tir/s) | 5 | 2,5 | 0,75 |
| chargeur | 5 | 8 | 12 |
| rechargement | 3 s | 2 s | 5 s |
| coût du rechargement | 2 | 5 | 10 |

Même classe, trois fichiers : le mitrailleur, l'intermédiaire, le canon lourd.

Note:
Démo en direct : dupliquer `Mk II`, changer trois valeurs, glisser le nouvel
asset dans la tourelle, appuyer sur Play. Aucune recompilation.
Mieux : changer une valeur **pendant** que le jeu tourne, l'effet est immédiat.

---

# Partager à l'exécution
<!-- .slide: class="title" -->

### Les quatre usages suivants ne servent plus à régler, mais à relier

---

## Usage 2 — La valeur partagée
### `Or` : qui écrit, qui lit

| Écrivent | Lisent |
|---|---|
| la cible détruite (`+30`) | le HUD |
| le rechargement d'une tourelle (`−coût`) | la boutique |
| l'achat en boutique (`−prix`) | la tourelle, avant de recharger |

Aucun de ces six-là ne connaît les autres. Ils connaissent **le même asset**.

Note:
C'est la slide la plus importante de la séance. Le découplage n'est pas une
idée abstraite : la cible n'a pas de référence vers la tourelle, la boutique
n'a pas de référence vers la cible, et pourtant abattre une cible paie le
rechargement d'une tourelle, dans une autre scène.

---

## La valeur du designer, et celle de la partie

```csharp
public class IntVariable : ScriptableObject
{
    [SerializeField] private int _initialValue;
    [SerializeField] private int _minimum = 0;

    [System.NonSerialized] private int _runtimeValue;

    public int Value
    {
        get => _runtimeValue;
        set => _runtimeValue = Mathf.Max(_minimum, value);
    }

    public void ResetToInitial() => _runtimeValue = _initialValue;

    public bool TrySpend(int amount)
    {
        if (_runtimeValue < amount) return false;
        Value = _runtimeValue - amount;
        return true;
    }
}
```

<small>Deux champs, pas un : `_initialValue` est sérialisé, `_runtimeValue` ne l'est jamais.</small>

Note:
Si l'on n'avait qu'un champ, la partie écrirait dans l'asset — voir la slide
suivante. `TrySpend` renvoie un booléen plutôt que de lancer une exception :
c'est lui qui décide qu'une tourelle sans or reste muette.
Deux assets de cette classe suffisent au jeu : `Or` et `Temps restant`.

---

## Le piège : l'état qui persiste

- dans l'**éditeur**, une valeur changée en Play mode **reste** changée après l'arrêt
- dans un **build**, l'asset est en lecture seule : tout est perdu à la fermeture
- une partie qui démarre peut donc hériter de la précédente

**La parade :** valeur de jeu non sérialisée, et une remise à zéro explicite.

Note:
Manuel Unity : « dans l'éditeur, on peut enregistrer des données dans un
ScriptableObject en Edit mode et en Play mode » ; « dans un Player autonome,
on ne peut que lire les données enregistrées ».
Conséquence : un ScriptableObject n'est **pas** un système de sauvegarde.
Dans le projet, `RunController.RestartRun()` est le seul endroit qui remet à
zéro, et il le fait en une ligne par asset. Le trajet par la boutique, lui,
ne remet rien : c'est voulu.

---

## Usage 3 — La référence partagée

Une donnée partagée n'est pas forcément un nombre.

```csharp
public class TurretProfileVariable : ScriptableObject
{
    [SerializeField] private TurretProfile initialValue;
    [System.NonSerialized] private TurretProfile runtimeValue;

    public TurretProfile Value
    {
        get => runtimeValue != null ? runtimeValue : initialValue;
        set => runtimeValue = value;
    }
}
```

La boutique écrit&nbsp;: `_equipped.Value = next;` — la tourelle lit&nbsp;: `Profile => _equipped.Value`

Note:
Même forme que `IntVariable`, mais le contenu est une référence vers un autre
asset. La boutique, dans la scène `Shop`, ne connaît aucune tourelle ; la
tourelle, dans la scène `Game`, ne connaît aucune boutique.
Dans le projet, seule la tourelle de droite lit ce profil équipé — les deux
autres gardent un profil posé dans l'Inspector, pour montrer les deux cas
côte à côte.

---

## Usage 4 — L'état qui survit à la scène
### Le problème

- la cible abattue est un objet de **scène**
- passer en boutique décharge la scène : l'objet n'existe plus
- au retour, une cible toute neuve est instanciée
- où était écrit « celle-là est morte » ?

Note:
Poser la question et laisser chercher. La mauvaise réponse classique : « dans
un GameManager en DontDestroyOnLoad ». Elle marche, mais elle recrée un objet
global qui connaît tout le monde — exactement ce qu'on essaie d'éviter.

---

## Un asset par cible

```csharp
[CreateAssetMenu(menuName = "Turrets/Shared/Tower State")]
public class TowerState : ScriptableObject
{
    private int _health;
    private bool _isDead;

    public int Health { get => _health; set => _health = value; }
    public bool IsDead { get => _isDead; set => _isDead = value; }

    public void Reset() { _health = 0; _isDead = false; }
}
```

Six cibles, six assets. **Les champs ne sont ni `[SerializeField]` ni publics : rien n'est écrit sur le disque.**

Note:
Le point subtil : un champ privé sans `[SerializeField]` n'est pas sérialisé
par Unity. L'état vit donc dans l'asset **chargé en mémoire**, et nulle part
ailleurs. C'est ce qui le fait survivre au changement de scène — l'asset reste
chargé tant que quelqu'un le référence — sans en faire une sauvegarde.
Faire remarquer que c'est implicite : un `[NonSerialized]` explicite, comme
dans `IntVariable`, dirait la même chose en le montrant.

---

## La démonstration

`Tower` ne retient rien elle-même : elle lit et écrit son asset d'état.

```csharp
private void OnEnable()
{
    if (_standingTowers != null) _standingTowers.Add(_state);
    if (_state.IsDead) Collapse(false);      // déjà morte avant la boutique
}

public void TakeDamage(int amount)
{
    _state.Health = Mathf.Max(0, _state.Health - amount);
    if (_state.Health > 0) return;

    if (_gold != null) _gold.Add(_reward);   // l'usage 2, ici
    Collapse(true);
}
```

**En direct :** abattre deux cibles → Boutique → Retour. Elles sont toujours au sol.

Note:
Le `Collapse(false)` de `OnEnable` est toute l'astuce : la cible neuve demande
à son asset « est-ce que j'étais morte ? » et se remet dans cet état sans
effet ni récompense. Le `false` évite de rejouer l'explosion et de repayer.
Montrer aussi la ligne `_gold.Add(_reward)` : les usages se composent.

---

## Usage 5 — La collection vivante
### Le problème

```csharp
// Au Start : rate tout ce qui apparaît ensuite.
var towers = FindObjectsByType<Tower>(FindObjectsSortMode.None);
```

- coûteux, et faux dès qu'un objet apparaît ou disparaît en cours de partie
- il faut le relancer, et savoir **quand** le relancer

Note:
`FindObjectsByType` parcourt toute la scène. Au `Start` c'est tolérable, à
chaque image c'est une faute. Et le vrai problème n'est pas la vitesse : c'est
qu'une liste prise au démarrage est périmée à la première vague suivante.

---

## Chacun s'inscrit lui-même

```csharp
public abstract class RuntimeSet<T> : ScriptableObject
{
    [System.NonSerialized] private readonly List<T> items = new();

    public IReadOnlyList<T> Items => items;
    public int Count => items.Count;

    public void Add(T item) { if (item != null && !items.Contains(item)) items.Add(item); }
    public void Remove(T item) => items.Remove(item);
}

[CreateAssetMenu(menuName = "Turrets/Shared/Tower Set (debout)")]
public class TowerSet : RuntimeSet<TowerState> { }
```

`OnEnable` → `Add`, `OnDisable` → `Remove`. Le HUD lit `Count`, et voit juste.

Note:
Deux choses à expliquer. **Un :** la classe est générique *et* abstraite, et
`TowerSet` n'ajoute rien — parce qu'Unity ne sait créer un asset que depuis une
classe concrète et non générique. C'est la rançon du sérialiseur, pas un choix
de design.
**Deux :** le set contient des `TowerState`, donc des **assets**, pas des
objets de scène. Un SO ne doit jamais garder une référence vers la scène : elle
serait morte au chargement suivant. C'est la même règle que l'usage 4.

---

## Les cinq usages

| | Ce qu'on y met | Dans le projet |
|---|---|---|
| **Préréglage** | des réglages figés | `TurretProfile` × 3 |
| **Valeur partagée** | un nombre que plusieurs lisent et écrivent | `Or`, `Temps restant` |
| **Référence partagée** | un choix, un profil équipé | `Profil équipé` |
| **État hors scène** | ce qui doit survivre au changement de scène | `TowerState` × 6 |
| **Collection vivante** | qui est là, maintenant | `Targets` |

Note:
Si les étudiants ne retiennent qu'une slide, c'est celle-là. Les quatre
derniers usages ont la même forme — un asset, une valeur dedans — et des
intentions complètement différentes.

---

## Ce qu'on y met, ce qu'on n'y met pas

| Oui | Non |
|---|---|
| réglages d'équilibrage | l'état d'une partie à **sauvegarder** |
| profils de tourelles, de loot, d'armes | une référence à un objet de **scène** |
| valeurs partagées **réinitialisées** | du code qui dépend d'une scène |
| l'état qui doit franchir une scène | tout, par principe |

Note:
La dernière ligne compte : un projet où chaque booléen est un asset devient
aussi illisible qu'un `GameManager` de mille lignes. La question à se poser
n'est pas « est-ce que ça peut être un SO ? » mais « qu'est-ce que ça
découple ? ». Si la réponse est « rien », c'est un champ, pas un asset.

---

## Atelier — 20 min

Ajouter un quatrième profil de tourelle, puis une septième cible — **sans écrire une ligne de code.**

Ensuite seulement : faire payer quelque chose de neuf avec l'or partagé.

Note:
Les deux premières étapes doivent se faire entièrement dans le Project et
l'Inspector — c'est le critère de réussite. La troisième demande une ligne de
code, et c'est là qu'on vérifie qu'ils ont compris quel asset toucher.
Tout part du projet companion, branche `main` : dupliquer un profil, dupliquer
une cible et son `TowerState`, les glisser dans la scène.

---

## À retenir

- un `ScriptableObject` est un **asset**, partagé par référence
- `[CreateAssetMenu]` : une variante = un fichier, zéro ligne de code
- une valeur partagée découple celui qui écrit de celui qui lit
- un asset survit au changement de scène ; un objet de scène, non
- ce qui est modifié en jeu **reste** modifié dans l'éditeur

---

## Ressources

- [ScriptableObject — Manuel Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html)
- [Create modular game architecture in Unity with ScriptableObjects — e-book Unity](https://unity.com/resources/create-modular-game-architecture-with-scriptable-objects-ebook) et son [projet démo](https://unity.com/how-to/get-started-with-scriptableobjects-demo)
- [Separate game data and logic with ScriptableObjects — Unity](https://unity.com/how-to/separate-game-data-logic-scriptable-objects)
- [Unite Austin 2017 — Game Architecture with Scriptable Objects](https://www.youtube.com/watch?v=raQ3iHhE_Kk) (Ryan Hipple)
- Projet de la séance : [GPR_UN_APU_04_ScriptableObjects](https://github.com/StudioAlbert/GPR_UN_APU_04_ScriptableObjects)
- Suite : [[GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|GPR-UN-APU-05 — Observer]], où les ScriptableObjects deviennent des canaux d'événement
