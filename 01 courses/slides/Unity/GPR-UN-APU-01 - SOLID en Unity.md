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
publish: true
---

# SOLID en Unity
<!-- .slide: class="title" -->

### Cinq principes pour un code qui encaisse le changement

<small>GPR-UN-APU-01 · Architecture et Patterns Unity</small>

Note:
Une heure, cinq principes, un seul exemple : un dungeon crawler.
Tous les extraits viennent du projet de l'atelier, une branche par principe.

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

- un **héros** magicien : se déplace, lance des boules de feu, interagit
- des **ennemis** : araignées (corps à corps), archer (distance)
- des **pièges** : pics, baril explosif
- un **marchand** et une **potion**
- des **mécanismes** : plaques de pression, porte de sortie, fontaine murale

<small>Projet Unity 6 : [Companion-Solid-DungeonCrawler](https://github.com/StudioAlbert/Companion-Solid-DungeonCrawler). Les corps notés `/* … */` sont omis.</small>

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
    private InputAction moveAction, attackAction;
    private int health = 100;

    void Awake()
    {
        moveAction = InputSystem.actions.FindAction("Move");
        attackAction = InputSystem.actions.FindAction("Attack");
    }

    void Update()
    {
        GetComponent<Rigidbody2D>().linearVelocity = moveAction.ReadValue<Vector2>() * speed;
        if (attackAction.WasPressedThisFrame())
            Instantiate(fireballPrefab, transform.position, Quaternion.identity);
    }

    public void TakeDamage(int amount)
    {
        health -= amount;
        healthLabel.text = "PV : " + health;
        if (health <= 0) Destroy(gameObject);
    }
}
```

➡️ Déplacement, combat, vie et UI dans une seule classe.

Note:
`TMP_Text` demande `using TMPro;`, `InputAction` demande `using UnityEngine.InputSystem;`.
Quatre raisons de changer : les contrôles, les sorts, les règles de vie, la maquette de l'UI.
Dans le projet (branche `main`), le même script gère aussi la touche E et les dégâts reçus.

---

## Après : se déplacer, attaquer

```csharp
public class PlayerMovement : MonoBehaviour
{
    [SerializeField] private float speed = 5f;
    private InputAction moveAction;
    public Vector2 Facing { get; private set; } = Vector2.right;

    void Awake() => moveAction = InputSystem.actions.FindAction("Move");

    void Update()
    {
        Vector2 input = moveAction.ReadValue<Vector2>();
        GetComponent<Rigidbody2D>().linearVelocity = input * speed;
        if (input != Vector2.zero) Facing = input.normalized;
    }
}

public class PlayerCombat : MonoBehaviour
{
    [SerializeField] private GameObject fireballPrefab;
    [SerializeField] private float fireballSpeed = 8f;
    /* Awake : action Attack, composant PlayerMovement */

    void Update()
    {
        if (!attackAction.WasPressedThisFrame()) return;
        GameObject fireball = Instantiate(fireballPrefab, transform.position, Quaternion.identity);
        fireball.GetComponent<Rigidbody2D>().linearVelocity = movement.Facing * fireballSpeed;
    }
}
```

➡️ Le combat lit la direction dans `PlayerMovement` : il ne lit pas l'input de déplacement.

---

## Après : la vie et son affichage

```csharp
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

public class HealthBar : MonoBehaviour
{
    [SerializeField] private TMP_Text label;

    public void Show(int health) => label.text = "PV : " + health;
}
```

➡️ Refaire la maquette de l'UI ne touche plus aux règles de vie.

<small>Projet : branche `01-srp`, avec aussi `PlayerInteractor` pour la touche E.</small>

Note:
Le lien direct `PlayerHealth → HealthBar` reste un couplage : on le
supprimera avec un événement en APU-09.

---

## SRP dans Unity

- un composant = un métier, un nom qui le dit
- `[RequireComponent]` pour déclarer une dépendance entre composants
- signal d'alerte : un nom en `Manager`, `Controller` ou `Handler` qui grossit

```csharp
[RequireComponent(typeof(PlayerMovement))]
public class PlayerCombat : MonoBehaviour { /* … */ }

[RequireComponent(typeof(PlayerHealth))]
public class PlayerInteractor : MonoBehaviour { /* … */ }
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
        else if (other.CompareTag("Explosion"))
            TakeDamage(30);
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

<small>Projet : branche `02-ocp`, avec aussi `Explosion` et `ContactDamage` (la morsure de l'araignée).</small>

Note:
L'araignée hérite déjà d'une autre classe : ses dégâts passent par un
composant `ContactDamage` posé sur sa zone de morsure. De la composition
plutôt qu'un second héritage, impossible en C#.

---

# L — Liskov Substitution
<!-- .slide: class="title" -->

---

## Un sous-type tient les promesses du parent

> Partout où le code attend un `Enemy`, n'importe quel sous-type d'`Enemy` doit fonctionner **sans surprise**.

Symptômes d'une hiérarchie qui ment :

- une méthode `override` **vide**
- une méthode qui lève `NotSupportedException`
- un `if (enemy is ExplodingBarrel)` dans le code client

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

// EnemyDirector, le code client :
foreach (Enemy enemy in enemies)
{
    enemy.Move(player.transform.position);
    if (enemy is ExplodingBarrel) continue;   // sinon : exception
    enemy.Attack(player);
}
```

➡️ `ExplodingBarrel` hérite de promesses qu'il **ne peut pas tenir**.

---

## Après : des capacités, pas une famille

```csharp
public interface IMovable    { void Move(Vector3 target); }
public interface IDamageable { void TakeDamage(int amount); }
public interface IAttacker
{
    float AttackRange { get; }
    void Attack(PlayerHealth player);
}

public class Spider : MonoBehaviour, IMovable, IAttacker, IDamageable { /* … */ }
public class Archer : MonoBehaviour, IAttacker, IDamageable { /* … */ }   // ne bouge pas

public class ExplodingBarrel : MonoBehaviour, IDamageable
{
    [SerializeField] private GameObject explosionPrefab;

    public void TakeDamage(int amount)
    {
        Instantiate(explosionPrefab, transform.position, Quaternion.identity);
        Destroy(gameObject);
    }
}

// EnemyDirector : plus aucun test de type
foreach (IMovable mover in movers) mover.Move(player.transform.position);
foreach (IAttacker attacker in attackers) attacker.Attack(player);
```

<small>Projet : branche `03-lsp` (`IAttacker` y porte aussi `AttackCooldown`).</small>

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
rattrape l'erreur dès l'éditeur : c'est le choix du projet pour les
plaques de pression (branche `05-dip`).

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
    void Use(PlayerHealth user);
}

public class Merchant : MonoBehaviour, IEntity
{
    public void Talk() { /* joue un jingle */ }

    public void Move(Vector3 target) { }
    public void Attack(PlayerHealth player) { }   // un marchand n'attaque pas
    public void TakeDamage(int amount) { }        // invulnérable
    public void Use(PlayerHealth user) { }
}
```

➡️ Quatre méthodes vides sur cinq. Chaque ajout à `IEntity` casse **toutes** les classes.

Note:
Dans le projet, la potion et le héros implémentent aussi `IEntity` :
douze méthodes vides au total.

---

## Après : des interfaces fines

```csharp
public interface ITalkable { void Talk(); }
public interface IUsable   { void Use(PlayerHealth user); }

public class Merchant : MonoBehaviour, ITalkable
{
    public void Talk() { /* joue un jingle */ }
}

// PlayerInteractor, touche E : chaque capacité est interrogée séparément
if (hit.TryGetComponent(out ITalkable talkable)) talkable.Talk();
if (hit.TryGetComponent(out IUsable usable)) usable.Use(health);
```

| | `IMovable` | `IAttacker` | `IDamageable` | `ITalkable` | `IUsable` |
|---|:-:|:-:|:-:|:-:|:-:|
| Araignée | ✔ | ✔ | ✔ | | |
| Archer | | ✔ | ✔ | | |
| Baril explosif | | | ✔ | | |
| Marchand | | | | ✔ | |
| Potion | | | | | ✔ |

<small>Projet : branche `04-isp`.</small>

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

<small>`Switch` (haut niveau) dépend directement de `Door` (bas niveau). Dans le projet, la plaque de pression joue le rôle de `Switch`.</small>

---

## Après, en schéma

![[solid_principles_in_unity_09.png]]

`Switch` et `Door` dépendent tous deux de `ISwitchable` : la flèche vers `Door` s'est **inversée**.

---

## Avant : la plaque connaît chaque mécanisme

```csharp
public class PressurePlate : MonoBehaviour
{
    [SerializeField] private Door door;
    [SerializeField] private WallFountain fountain;
    private bool isOn;

    // Chaque passage sur la plaque inverse son état
    void OnTriggerEnter2D(Collider2D other)
    {
        if (!other.CompareTag("Player")) return;
        isOn = !isOn;

        if (door != null)
        {
            if (isOn) door.Open();
            else door.Close();
        }
        if (fountain != null)
        {
            if (isOn) fountain.TurnOn();
            else fountain.TurnOff();
        }
    }
}
```

➡️ Demain la plaque doit baisser une herse : un champ et un `if` de plus dans `PressurePlate`.

---

## Après : la plaque connaît un contrat

```csharp
public interface ISwitchable
{
    void Activate();
    void Deactivate();
}

public class Door : MonoBehaviour, ISwitchable
{
    public void Activate()   { /* sprite ouvert, collider coupé */ }
    public void Deactivate() { /* sprite fermé, collider actif */ }
}

public class PressurePlate : MonoBehaviour
{
    [SerializeField] private GameObject target;   // doit porter un ISwitchable
    private ISwitchable switchable;
    private bool isOn;

    void Awake() => switchable = target.GetComponent<ISwitchable>();

    void OnTriggerEnter2D(Collider2D other)
    {
        if (!other.CompareTag("Player")) return;
        isOn = !isOn;
        if (isOn) switchable.Activate();
        else switchable.Deactivate();
    }
}
```

<small>Projet : branche `05-dip`. `WallFountain` implémente aussi `ISwitchable`.</small>

Note:
`GetComponent` accepte une interface. Le champ reste un `GameObject`
parce que l'Inspector n'affiche pas un champ de type interface :
voir « Les interfaces dans Unity ». Dans le projet, `OnValidate` signale
dès l'éditeur une cible qui n'implémente pas `ISwitchable`. Une classe
abstraite `Switchable` permettrait un champ typé `Switchable[] targets`.

---

## Inversion ≠ injection

- **Inversion de dépendance** : un principe de conception. *Qui dépend de quoi ?*
  `PressurePlate → ISwitchable ← Door`
- **Injection de dépendance** : une technique. *Qui fournit l'objet ?*
  - l'Inspector : glisser la porte dans le champ `target`, c'est déjà de l'injection
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
| **D** | un champ par type concret | contrat + cible réglée dans l'Inspector |

---

## Atelier : Dungeon Crawler modulaire

[github.com/StudioAlbert/Companion-Solid-DungeonCrawler](https://github.com/StudioAlbert/Companion-Solid-DungeonCrawler)

- un donjon jouable, écrit volontairement **sans** SOLID : branche `main`
- une étape par principe : `01-srp` → `02-ocp` → `03-lsp` → `04-isp` → `05-dip`
- chaque branche est la solution d'une étape et le départ de la suivante
- **bonus** : ajouter un ennemi, un piège ou un mécanisme sans modifier une seule classe existante

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
