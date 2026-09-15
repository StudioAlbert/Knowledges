---
title: SOLID en Unity
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
---

# SOLID en Unity
<!-- .slide: class="title" -->

### Cinq principes pour un code qui encaisse le changement

<small>GPR-UN-APU-01 · Architecture et Patterns Unity</small>

Note:
Une heure, cinq principes, un seul exemple : un dungeon crawler.
Les exercices sont dans la note « Exercices - GPR-UN-APU-01 ».

---

## Objectifs

À la fin de la séance, vous savez :

- repérer un script qui porte trop de responsabilités
- ajouter un comportement **sans modifier** le code existant
- choisir entre héritage, classe abstraite et interface
- relier deux composants Unity par une abstraction
- dire quand SOLID **ne vaut pas** le coût

**Prérequis :** classes, héritage, `abstract`, `virtual` / `override`, `interface` en C#.

---

## Le problème

- ajouter un ennemi ou un piège = modifier cinq scripts
- corriger un bug en crée un autre ailleurs
- impossible de réutiliser un script dans une autre scène
- un `PlayerController` de 800 lignes que personne n'ose ouvrir

Note:
Demander qui a déjà eu un script de joueur qui fait tout.
Tout le monde lève la main.

---

## SOLID en une slide

| | Principe | En une phrase |
|---|---|---|
| **S** | Single Responsibility | une classe, une seule raison de changer |
| **O** | Open / Closed | on étend sans modifier |
| **L** | Liskov Substitution | un sous-type tient les promesses de son parent |
| **I** | Interface Segregation | pas de méthode imposée qu'on n'utilise pas |
| **D** | Dependency Inversion | on dépend d'abstractions, pas de détails |

---

## Fil rouge : le Dungeon Crawler

- un **héros** : se déplace, lance des sorts, prend des dégâts
- des **ennemis** : araignée (corps à corps), squelette archer (distance)
- des **pièges** : pics, baril explosif
- des **mécanismes** : plaques de pression, portes, herses, torches

<small>Code en C# Unity 6. Les corps notés `/* … */` sont laissés vides.</small>

---

# S — Single Responsibility
<!-- .slide: class="title" -->

---

## Une seule raison de changer

> Une classe ne doit avoir qu'**une seule raison d'être modifiée**.

- une raison de changer = un métier : déplacement, combat, vie, affichage
- si le game designer **et** le UI designer modifient le même script : deux responsabilités

<small>[Principe de responsabilité unique — Wikipédia](https://fr.wikipedia.org/wiki/Principe_de_responsabilit%C3%A9_unique)</small>

---

## Avant, en schéma

![[solid_principles_in_unity_01.png]]

<small>Schéma de l'e-book Unity : un `Player` qui gère audio, input et mouvement.</small>

---

## Après, en schéma

![[solid_principles_in_unity_02.png]]

Un composant par responsabilité. Unity est déjà construit comme ça : **plusieurs composants sur un même GameObject**.

---

## Avant : le script fourre-tout

```csharp
public class PlayerController : MonoBehaviour
{
    [SerializeField] private float speed = 5f;
    [SerializeField] private GameObject fireballPrefab;
    [SerializeField] private TMP_Text healthLabel;
    private int health = 100;

    void Update()
    {
        var input = new Vector2(Input.GetAxis("Horizontal"), Input.GetAxis("Vertical"));
        transform.Translate(input * speed * Time.deltaTime);
        if (Input.GetButtonDown("Fire1"))
            Instantiate(fireballPrefab, transform.position, transform.rotation);
    }

    public void TakeDamage(int amount)
    {
        health -= amount;
        healthLabel.text = health.ToString();
        if (health <= 0) Destroy(gameObject);
    }
}
```

➡️ Déplacement, combat, vie et UI dans une seule classe.

Note:
`TMP_Text` demande `using TMPro;`. Quatre raisons de changer :
les contrôles, les sorts, les règles de vie, la maquette de l'UI.

---

## Après : un composant par responsabilité

```csharp
public class PlayerMovement : MonoBehaviour
{
    [SerializeField] private float speed = 5f;
    void Update()
    {
        var input = new Vector2(Input.GetAxis("Horizontal"), Input.GetAxis("Vertical"));
        transform.Translate(input * speed * Time.deltaTime);
    }
}

public class PlayerCombat : MonoBehaviour
{
    [SerializeField] private GameObject fireballPrefab;
    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
            Instantiate(fireballPrefab, transform.position, transform.rotation);
    }
}

public class PlayerHealth : MonoBehaviour
{
    [SerializeField] private HealthBar healthBar;
    private int health = 100;
    public void TakeDamage(int amount)
    {
        health -= amount;
        healthBar.Show(health);
        if (health <= 0) Destroy(gameObject);
    }
}
```

Note:
`HealthBar` est un quatrième composant, côté UI, qui se contente
d'afficher. Le lien direct `PlayerHealth → HealthBar` reste un couplage :
on le supprimera avec un événement en APU-09.

---

## SRP dans Unity

- un composant = un métier, un nom qui le dit
- `[RequireComponent(typeof(PlayerHealth))]` pour déclarer une dépendance entre composants
- signal d'alerte : un nom en `Manager`, `Controller` ou `Handler` qui grossit

```csharp
[RequireComponent(typeof(PlayerHealth))]
public class PlayerCombat : MonoBehaviour { /* … */ }
```

---

# O — Open / Closed
<!-- .slide: class="title" -->

---

## Ouvert à l'extension, fermé à la modification

> Ajouter un comportement ne doit pas obliger à **modifier** le code qui marche déjà.

- **ouvert** : on peut ajouter un nouveau cas
- **fermé** : sans rouvrir les fichiers existants
- symptôme : un `switch` ou une cascade de `if` sur un type

<small>[Principe ouvert/fermé — Wikipédia](https://fr.wikipedia.org/wiki/Principe_ouvert/ferm%C3%A9)</small>

---

## Avant, en schéma

![[solid_principles_in_unity_03.png]]

<small>Exemple de l'e-book Unity : `AreaCalculator` doit connaître chaque forme. Ajouter un triangle = le modifier.</small>

---

## Après, en schéma

![[solid_principles_in_unity_04.png]]

<small>`AreaCalculator` ne connaît que `Shape`. Ajouter un triangle = une nouvelle classe.</small>

---

## Avant : un `if` par danger

```csharp
public class PlayerHealth : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Spider"))
            TakeDamage(10);
        else if (other.CompareTag("Arrow"))
            TakeDamage(Random.Range(5, 11));
        else if (other.CompareTag("SpikeTrap"))
            TakeDamage(25);
        // nouveau danger ? on revient modifier ce fichier
    }

    public void TakeDamage(int amount) { /* … */ }
}
```

➡️ Chaque nouvel ennemi ou piège **modifie** `PlayerHealth`.

---

## Après : une abstraction

```csharp
public abstract class DamageSource : MonoBehaviour
{
    public abstract int GetDamage();
}

public class Arrow : DamageSource
{
    public override int GetDamage() => Random.Range(5, 11);
}

public class SpikeTrap : DamageSource
{
    [SerializeField] private int damage = 25;
    public override int GetDamage() => damage;
}

public class PlayerHealth : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.TryGetComponent(out DamageSource source))
            TakeDamage(source.GetDamage());
    }

    public void TakeDamage(int amount) { /* … */ }
}
```

➡️ Nouveau danger = **nouveau fichier**. `PlayerHealth` ne bouge plus.

---

# L — Liskov Substitution
<!-- .slide: class="title" -->

---

## Un sous-type tient les promesses du parent

> Partout où le code attend un `Enemy`, n'importe quel sous-type d'`Enemy` doit fonctionner **sans surprise**.

Symptômes d'une hiérarchie qui ment :

- une méthode `override` **vide**
- une méthode qui lève `NotSupportedException`
- un `if (enemy is Barrel)` dans le code client

<small>[Principe de substitution de Liskov — Wikipédia](https://fr.wikipedia.org/wiki/Principe_de_substitution_de_Liskov)</small>

---

## Avant, en schéma

![[solid_principles_in_unity_05.png]]

<small>Exemple de l'e-book Unity : un `Train` hérite de `TurnLeft()` / `TurnRight()` qu'il ne peut pas implémenter.</small>

---

## Après, en schéma

![[solid_principles_in_unity_06.png]]

<small>On découpe selon ce que l'objet **sait faire** : avancer, tourner.</small>

---

## Avant : le baril n'est pas un ennemi

```csharp
public abstract class Enemy : MonoBehaviour
{
    public abstract void Move(Vector3 target);
    public abstract void Attack(PlayerHealth player);
    public abstract void TakeDamage(int amount);
}

public class ExplodingBarrel : Enemy
{
    public override void Move(Vector3 target) { }          // ne bouge pas
    public override void Attack(PlayerHealth player)
        => throw new System.NotSupportedException();       // n'attaque pas
    public override void TakeDamage(int amount) { /* explose */ }
}

// Ailleurs, le code client :
foreach (Enemy enemy in enemies)
    enemy.Attack(player);   // exception sur le baril
```

➡️ `ExplodingBarrel` hérite de promesses qu'il **ne peut pas tenir**.

---

## Après : des capacités, pas une famille

```csharp
public interface IMovable    { void Move(Vector3 target); }
public interface IAttacker   { void Attack(PlayerHealth player); }
public interface IDamageable { void TakeDamage(int amount); }

public class Spider : MonoBehaviour, IMovable, IAttacker, IDamageable
{
    [SerializeField] private float speed = 3f;
    public void Move(Vector3 target) => transform.position =
        Vector3.MoveTowards(transform.position, target, speed * Time.deltaTime);
    public void Attack(PlayerHealth player) => player.TakeDamage(10);
    public void TakeDamage(int amount) => Destroy(gameObject);
}

public class ExplodingBarrel : MonoBehaviour, IDamageable
{
    public void TakeDamage(int amount) { /* explose */ }
}

foreach (IAttacker attacker in attackers)
    attacker.Attack(player);   // le baril n'est pas dans la liste
```

---

# Parenthèse C# : les interfaces
<!-- .slide: class="title" -->

---

## Qu'est-ce qu'une interface ?

- un **contrat** : une liste de méthodes (et de propriétés), sans code
- mot-clé `interface`, nom préfixé par `I` par convention
- une classe qui l'implémente fournit **toutes** ses méthodes, en `public`
- une classe hérite d'**une seule** classe, mais implémente **plusieurs** interfaces
- on n'instancie pas une interface : on manipule un objet **à travers** elle

| | Classe abstraite | Interface |
|---|---|---|
| Contient du code | oui | non (sauf cas avancés) |
| Champs | oui | non |
| Combien par classe | une | autant qu'on veut |

Note:
Depuis C# 8, une interface peut porter une implémentation par défaut.
On ne s'en sert pas ici : une interface reste un contrat.

---

## Exemple : `IAnimal`

```csharp
public interface IAnimal
{
    void Cry();
}

public class Cat : IAnimal
{
    public void Cry() => Debug.Log("Miaou");
}

public class Dog : IAnimal
{
    public void Cry() => Debug.Log("Wouf");
}

// Le code client ne connaît que le contrat
IAnimal[] animals = { new Cat(), new Dog() };
foreach (IAnimal animal in animals)
    animal.Cry();                 // Miaou, puis Wouf

// IAnimal a = new IAnimal();    // erreur : on n'instancie pas une interface
```

➡️ Ajouter un `Cow` ne change rien à la boucle.

---

## Les interfaces dans Unity

- `GetComponent<IDamageable>()` et `TryGetComponent(out IDamageable d)` **acceptent** une interface
- un champ `[SerializeField] IDamageable target;` **n'apparaît pas** dans l'Inspector

| Solution | Pour | Contre |
|---|---|---|
| champ `GameObject` + `GetComponent<IDamageable>()` | garde l'interface | erreur visible seulement au lancement |
| classe abstraite `Damageable : MonoBehaviour` | champ typé, glisser-déposer | un seul héritage possible |

```csharp
public abstract class Damageable : MonoBehaviour
{
    public abstract void TakeDamage(int amount);
}

public class Bomb : MonoBehaviour
{
    [SerializeField] private Damageable[] targets;   // visible et typé
}
```

Note:
`[SerializeReference]` sérialise un champ de type interface, mais
uniquement pour des classes C# simples, pas pour des composants de scène.
Pour la première solution, un `OnValidate` qui vérifie l'interface
rattrape l'erreur dès l'éditeur.

---

# I — Interface Segregation
<!-- .slide: class="title" -->

---

## Pas de méthode imposée inutilement

> Aucun client ne doit dépendre de méthodes qu'il n'utilise pas.

- plusieurs petites interfaces valent mieux qu'une grosse
- une classe peut implémenter **plusieurs** interfaces, mais n'hériter que d'**une** classe

<small>[Principe de ségrégation des interfaces — Wikipédia](https://fr.wikipedia.org/wiki/Principe_de_s%C3%A9gr%C3%A9gation_des_interfaces)</small>

---

## Après, en schéma

![[solid_principles_in_unity_07.png]]

<small>Chaque objet n'implémente que ses interfaces. Une interface peut aussi porter des propriétés : `Health`, `Defense`…</small>

---

## Avant : l'interface « tout-en-un »

```csharp
public interface IEntity
{
    void Move(Vector3 target);
    void Attack(PlayerHealth player);
    void TakeDamage(int amount);
    void Talk();
    void Use();
}

public class Merchant : MonoBehaviour, IEntity
{
    public void Move(Vector3 target) { }
    public void Attack(PlayerHealth player) { }   // un marchand n'attaque pas
    public void TakeDamage(int amount) { }        // invulnérable
    public void Talk() { /* ouvre la boutique */ }
    public void Use() { }
}
```

➡️ Quatre méthodes vides sur cinq. Chaque ajout à `IEntity` casse **toutes** les classes.

---

## Après : des interfaces fines

```csharp
public interface ITalkable { void Talk(); }
public interface IUsable   { void Use(PlayerHealth user); }

public class Merchant : MonoBehaviour, ITalkable
{
    public void Talk() { /* ouvre la boutique */ }
}
```

| | `IMovable` | `IAttacker` | `IDamageable` | `ITalkable` | `IUsable` |
|---|:-:|:-:|:-:|:-:|:-:|
| Héros | ✔ | ✔ | ✔ | | |
| Araignée | ✔ | ✔ | ✔ | | |
| Baril explosif | | | ✔ | | |
| Marchand | | | | ✔ | |
| Potion | | | | | ✔ |

---

## Liskov ou ségrégation ?

Les deux aboutissent souvent au **même remède** : des interfaces séparées.

| | Liskov (L) | Ségrégation (I) |
|---|---|---|
| Question | le sous-type tient-il les promesses ? | le contrat est-il trop gros ? |
| Regarde | une **hiérarchie** | une **interface** |
| Symptôme | `override` vide ou qui lève une exception | méthodes vides imposées |

---

# D — Dependency Inversion
<!-- .slide: class="title" -->

---

## Dépendre d'abstractions

> Les modules de haut niveau ne dépendent pas des modules de bas niveau. **Les deux dépendent d'abstractions.**

- **haut niveau** : la règle (« une plaque déclenche un mécanisme »)
- **bas niveau** : le détail (« une porte s'ouvre »)

<small>[Inversion des dépendances — Wikipédia](https://fr.wikipedia.org/wiki/Inversion_des_d%C3%A9pendances)</small>

---

## Avant, en schéma

![[solid_principles_in_unity_08.png]]

<small>`Switch` (haut niveau) dépend directement de `Door` (bas niveau).</small>

---

## Après, en schéma

![[solid_principles_in_unity_09.png]]

`Switch` et `Door` dépendent tous deux de `ISwitchable` : la flèche vers `Door` s'est **inversée**.

---

## Avant : l'interrupteur connaît la porte

```csharp
public class Door : MonoBehaviour
{
    public void Open()  => gameObject.SetActive(false);
    public void Close() => gameObject.SetActive(true);
}

public class Switch : MonoBehaviour
{
    [SerializeField] private Door door;

    void OnTriggerEnter2D(Collider2D other) => door.Open();
    void OnTriggerExit2D(Collider2D other)  => door.Close();
}
```

➡️ Demain la même plaque doit baisser une herse ou allumer une torche : il faut **réécrire** `Switch`.

---

## Après : l'interrupteur connaît un contrat

```csharp
public interface ISwitchable
{
    void Activate();
    void Deactivate();
}

public class Door : MonoBehaviour, ISwitchable
{
    public void Activate()   => gameObject.SetActive(false);
    public void Deactivate() => gameObject.SetActive(true);
}

public class Torch : MonoBehaviour, ISwitchable
{
    [SerializeField] private GameObject flame;
    public void Activate()   => flame.SetActive(true);
    public void Deactivate() => flame.SetActive(false);
}

public class Switch : MonoBehaviour
{
    [SerializeField] private GameObject target;
    private ISwitchable client;

    void Awake() => client = target.GetComponent<ISwitchable>();
    void OnTriggerEnter2D(Collider2D other) => client.Activate();
    void OnTriggerExit2D(Collider2D other)  => client.Deactivate();
}
```

Note:
`GetComponent` accepte une interface. Le champ reste un `GameObject`
parce que l'Inspector n'affiche pas un champ de type interface :
voir « Les interfaces dans Unity ». Une classe abstraite `Switchable`
permettrait un champ typé `Switchable[] targets`.

---

## Inversion ≠ injection

- **Inversion de dépendance** : un principe de conception. *Qui dépend de quoi ?*
  `Switch → ISwitchable ← Door`
- **Injection de dépendance** : une technique. *Qui fournit l'objet ?*
  - l'Inspector : glisser la porte dans le champ, c'est déjà de l'injection
  - une méthode `Init(ISwitchable client)` : un `MonoBehaviour` n'a **pas de constructeur**
  - un framework : VContainer, Zenject / Extenject

On peut inverser sans framework. Un framework ne garantit pas l'inversion.

---

# Clôture
<!-- .slide: class="title" -->

---

## Quand ne pas appliquer SOLID

- **prototype, game jam** : le code sera jeté, allez vite
- **une seule implémentation** et aucune autre en vue : pas d'interface (YAGNI)
- extraire l'abstraction quand le **deuxième** cas arrive, pas avant
- chaque abstraction coûte : un fichier de plus, une indirection de plus à lire

SOLID sert à **diagnostiquer** un code qui résiste au changement. Ce n'est pas une checklist.

---

## Récapitulatif

| | Symptôme | Remède en Unity |
|---|---|---|
| **S** | script fourre-tout | un composant par métier |
| **O** | `switch` / `if` sur un type | classe abstraite ou interface + `TryGetComponent` |
| **L** | `override` vide, exception | interfaces de capacités |
| **I** | méthodes vides imposées | interfaces fines |
| **D** | champ d'un type concret | contrat + injection par l'Inspector |

---

## Atelier : Dungeon Crawler modulaire

[github.com/StudioAlbert/UnityCourse-SOLID-DungeonCrawler](https://github.com/StudioAlbert/UnityCourse-SOLID-DungeonCrawler)

- refactorer une scène fournie, qui n'est pas SOLID
- un exercice par principe, puis l'atelier complet
- **bonus** : ajouter un ennemi, un sort ou un piège sans modifier une seule classe existante

Énoncés : [[01 courses/exercises/Unity/GPR-UN-APU-01 - SOLID en Unity]]

---

## Pour aller plus loin

- Strategy (styles d'attaque, IA) : [[GPR-UN-APU-08 - Strategy pattern en Unity]]
- Observer, State, composition : [[GPR-UN-APU-09 - Observer, State et composition]]
- Couplage et cohésion : [[TC-FT-PCL-01 - Couplage et cohésion]]
- Composition contre héritage : [[TC-FT-PCL-04 - Composition contre héritage]]

---

## Ressources

- [Level up your code with design patterns and SOLID — e-book Unity](https://unity.com/resources/design-patterns-solid-ebook) : source des schémas
- [Unite Austin 2017 — S.O.L.I.D. Unity](https://youtu.be/eIf3-aDTOOA) : le même contenu en vidéo
- [Software Architecture in Unity](https://youtu.be/sh7f4K9Wbj8) : pourquoi architecturer
- [SOLID Principles in Unity](https://www.youtube.com/watch?v=QDldZWvNK_E)
- [SOLID Unity3D — playlist](https://youtube.com/playlist?list=PLB5_EOMkLx_WjcjrsGUXq9wpTib3NCuqg)
- [SOLID — Wikipédia](https://en.wikipedia.org/wiki/SOLID)
