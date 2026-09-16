---
title: SOLID en Unity
type: slides
code: GPR-UN-APU-01
status: To check
subject: Unity
duration_h: 1
bloc_gsda: Architecture et Patterns Unity
source: "[[solid_principles_in_unity]]"
exercices: "[[01 courses/exercises/Unity/GPR-UN-APU-01 - SOLID en Unity]]"
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# SOLID en Unity
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

### Cinq principes pour un code qui encaisse le changement

<small>GPR-UN-APU-01 · Architecture et Patterns Unity · fil rouge : Dungeon Crawler</small>

Note:
Séance d'1 h. Pas le temps de tout coder en direct : on montre un
avant / après par principe, les exercices sont dans la note dédiée.
Minutage indicatif : intro 5 min, 9 min par principe, clôture 10 min.

---

## À la fin de la séance, vous savez…
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- **reconnaître** le symptôme de chacun des cinq principes dans un script
- **découper** un `MonoBehaviour` fourre-tout en composants
- **remplacer** un `switch` ou une hiérarchie bancale par une interface
- **brancher** une dépendance abstraite depuis l'Inspector
- **décider** quand SOLID n'est *pas* nécessaire

<small>Prérequis : classes, héritage, `abstract`, `interface` en C#.</small>

---

## Le problème
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Symptômes d'un projet qui grossit :

- ajouter un ennemi ou un piège = modifier **plusieurs** scripts
- un changement ici casse quelque chose là-bas
- deux personnes modifient le même fichier → conflits Git
- impossible de réutiliser un script dans une autre scène

La cause la plus fréquente : le **script fourre-tout**.

---

## SOLID en une slide
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

| | Principe | En une phrase |
|---|---|---|
| **S** | Single Responsibility | une seule raison de changer |
| **O** | Open / Closed | on ajoute sans modifier |
| **L** | Liskov Substitution | un sous-type tient les promesses du parent |
| **I** | Interface Segregation | pas de méthode imposée inutilement |
| **D** | Dependency Inversion | on dépend d'abstractions, pas de détails |

<small>Robert C. Martin, début des années 2000.</small>

---

## Fil rouge : le Dungeon Crawler
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- un **héros** : déplacement, combat, santé, sons
- des **ennemis** : corps à corps, distance
- des **pièges** et des **tonneaux explosifs**
- des **portes** et des **interrupteurs**

Chaque principe part d'un script de ce donjon.

Note:
Les schémas UML viennent de l'e-book Unity (Shape, Vehicle). On les
montre comme « le même mécanisme, sur un autre exemple » — le code, lui,
reste toujours dans le donjon.

---

# S — Single Responsibility
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

> Une classe n'a qu'**une seule raison de changer**.

Une « raison de changer » = une personne ou un besoin qui peut demander une modification.

---

## SRP — avant
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```csharp
public class PlayerController : MonoBehaviour
{
    void ReadInput()       { … } // le game designer change les contrôles
    void Move()            { … } // le feel du déplacement change
    void PlayFootsteps()   { … } // le sound designer change les sons
    void TakeDamage(int d) { … } // les règles de combat changent
    void UpdateHealthBar() { … } // l'UI change
}
```

**Cinq** raisons de changer, **un** fichier.

---

## SRP — le découpage
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

![[solid_principles_in_unity_01.png]]

↓

![[solid_principles_in_unity_02.png]]

Note:
Premier schéma : un seul bloc qui fait tout. Second : le Player est
un GameObject qui porte des composants. C'est exactement le modèle
de Unity.

---

## SRP — après
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Un composant par responsabilité, **sur le même GameObject** :

`PlayerInput` · `PlayerMovement` · `PlayerAudio` · `Health` · `HealthBar`

```csharp
[RequireComponent(typeof(PlayerMovement))]
public class PlayerInput : MonoBehaviour
{
    PlayerMovement movement;

    void Awake()  => movement = GetComponent<PlayerMovement>();
    void Update() => movement.Move(ReadDirection());

    Vector2 ReadDirection() { … }
}
```

Unity pousse déjà vers ce modèle : la **composition**.

Note:
Faire remarquer que Health et HealthBar sont séparés : la santé existe
aussi pour les ennemis, qui n'ont pas de barre à l'écran.

---

# O — Open / Closed
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

> Ouvert à l'**extension**, fermé à la **modification**.

Ajouter un comportement ne doit pas obliger à rouvrir le code qui marche.

---

## OCP — avant
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```csharp
public class Health : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Enemy"))           TakeDamage(10);
        else if (other.CompareTag("Projectile")) TakeDamage(Random.Range(5, 11));
        else if (other.CompareTag("Trap"))       TakeDamage(25);
        // nouveau danger → nouvelle branche ICI
    }

    void TakeDamage(int amount) { … }
}
```

Chaque nouveau danger **modifie** `Health`.

---

## OCP — le même problème en UML
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

![[solid_principles_in_unity_03.png]]

Une méthode par forme : chaque nouvelle forme modifie `AreaCalculator`.

---

## OCP — la solution en UML
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

![[solid_principles_in_unity_04.png]]

`AreaCalculator` ne connaît que `Shape`. Une nouvelle forme = une nouvelle classe.

---

## OCP — après
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```csharp
public interface IDamageDealer
{
    int GetDamage();
}

public class Health : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.TryGetComponent(out IDamageDealer dealer))
            TakeDamage(dealer.GetDamage());
    }
    …
}

public class Trap : MonoBehaviour, IDamageDealer
{
    [SerializeField] int damage = 25;
    public int GetDamage() => damage;
}
```

Nouveau danger = nouvelle classe. `Health` ne bouge plus.

Note:
GetComponent et TryGetComponent acceptent une interface comme type.
Plus de tags à maintenir : c'est le composant qui porte l'information.

---

# L — Liskov Substitution
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

> Partout où le code attend un `T`, on doit pouvoir donner un sous-type de `T` **sans surprise**.

<small>Barbara Liskov, 1987.</small>

---

## LSP — avant
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```csharp
public abstract class Enemy : MonoBehaviour
{
    public abstract void Move(Vector3 target);
    public abstract void Attack(IDamageable target);
}

public class ExplodingBarrel : Enemy
{
    public override void Move(Vector3 target) { }  // ne bouge pas
    public override void Attack(IDamageable target)
        => throw new System.NotSupportedException();
}
```

```csharp
foreach (Enemy enemy in enemies)
    enemy.Move(player.position);   // le tonneau casse le contrat
```

Note:
Question à poser : « la salle est terminée quand tous les ennemis sont
morts ». Faut-il détruire les tonneaux pour finir la salle ? La
hiérarchie ment : un tonneau n'EST PAS un ennemi.

---

## LSP — le même problème en UML
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

![[solid_principles_in_unity_05.png]]

Un `Train` ne tourne pas : il ne peut pas tenir la promesse de `Vehicle`.

---

## LSP — le test
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

La hiérarchie ment si un sous-type :

- laisse une méthode **vide** qui devrait agir
- lève `NotSupportedException`
- oblige l'appelant à écrire `if (enemy is ExplodingBarrel)`

Remède : revoir **ce que chaque type promet vraiment**.

---

## LSP — après
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

![[solid_principles_in_unity_06.png]]

Dans le donjon : `EnemyUnit` bouge et attaque, `ExplodingBarrel` subit des dégâts et explose — **pas de parent commun forcé**.

---

# I — Interface Segregation
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

> Aucun client ne doit dépendre de méthodes qu'il n'utilise pas.

Plusieurs petites interfaces valent mieux qu'une grosse.

---

## ISP — avant
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```csharp
public interface IEntity
{
    void Move(Vector3 target);
    void Attack(IDamageable target);
    void UseItem(Item item);
    void Talk(string line);
}

public class SpikeTrap : MonoBehaviour, IEntity
{
    public void Move(Vector3 target) { }          // inutile
    public void Attack(IDamageable target) { … }
    public void UseItem(Item item) { }            // inutile
    public void Talk(string line) { }             // inutile
}
```

---

## ISP — après
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```csharp
public interface IMovable  { void Move(Vector3 target); }
public interface IAttacker { void Attack(IDamageable target); }
public interface IItemUser { void UseItem(Item item); }
public interface ITalker   { void Talk(string line); }

public class Hero      : MonoBehaviour, IMovable, IAttacker, IItemUser, ITalker { … }
public class Goblin    : MonoBehaviour, IMovable, IAttacker { … }
public class SpikeTrap : MonoBehaviour, IAttacker { … }
```

Chaque entité implémente **ce qu'elle fait vraiment**.

---

## ISP — dans le donjon
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

![[solid_principles_in_unity_07.png]]

`IDamageable` est partagé : on peut frapper un ennemi **et** un tonneau.

---

## LSP ou ISP ?
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Les deux mènent souvent au même résultat : des interfaces séparées.

| | LSP | ISP |
|---|---|---|
| Question | le sous-type tient-il les promesses ? | l'interface est-elle trop large ? |
| Porte sur | l'**héritage** | la **taille** du contrat |
| Symptôme | override vide, exception, `is` | méthodes imposées inutiles |

---

# D — Dependency Inversion
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

> Les modules de haut niveau ne dépendent pas des modules de bas niveau : **les deux** dépendent d'abstractions.

> Les abstractions ne dépendent pas des détails.

---

## DIP — avant
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```csharp
public class Door : MonoBehaviour
{
    public void Open()  { … }
    public void Close() { … }
}

public class Switch : MonoBehaviour
{
    [SerializeField] Door door;   // dépend d'une classe concrète

    void OnTriggerEnter(Collider other) => door.Open();
    void OnTriggerExit(Collider other)  => door.Close();
}
```

Demain l'interrupteur doit allumer une torche → `TorchSwitch` ?

---

## DIP — en UML
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

![[solid_principles_in_unity_08.png]]

↓

![[solid_principles_in_unity_09.png]]

Note:
Le point clé : l'interface appartient au haut niveau. C'est Switch qui
dit « j'ai besoin de quelque chose qu'on active » ; Door s'y conforme.
La flèche de dépendance de Door est inversée.

---

## DIP — après
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

```csharp
public interface ISwitchable
{
    void Activate();
    void Deactivate();
}

public class Door  : MonoBehaviour, ISwitchable { … }
public class Torch : MonoBehaviour, ISwitchable { … }

public class Switch : MonoBehaviour
{
    [SerializeField] MonoBehaviour target;   // doit implémenter ISwitchable
    ISwitchable switchable;

    void Awake() => switchable = (ISwitchable)target;
    void OnTriggerEnter(Collider other) => switchable.Activate();
    void OnTriggerExit(Collider other)  => switchable.Deactivate();
}
```

---

## Unity : interfaces et Inspector
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Un champ de type interface **n'apparaît pas** dans l'Inspector.

| Option | + | − |
|---|---|---|
| `MonoBehaviour` + cast | garde l'interface | pas de filtre dans l'Inspector → valider dans `OnValidate` |
| classe `abstract Switchable : MonoBehaviour` | visible et typé dans l'Inspector | consomme le seul héritage possible |
| `GetComponent<ISwitchable>()` | zéro configuration | cible sur le même GameObject |

Pour rester **designer friendly** : la classe abstraite est souvent le bon compromis.

Note:
SerializeReference ne résout pas le problème : il ne sérialise pas les
références vers des UnityEngine.Object (donc pas vers un MonoBehaviour).

---

## Inversion ≠ injection
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- **Inversion** (DIP) : *qui dépend de quoi* → le haut niveau définit l'abstraction
- **Injection** : *comment* on fournit l'objet concret

Injecter en Unity :

- par l'**Inspector** (le plus courant)
- par `GetComponent` / `FindAnyObjectByType`
- par constructeur → classes C# pures uniquement, pas de `MonoBehaviour`
- par un framework : VContainer, Zenject / Extenject

---

## Quand ne PAS appliquer SOLID
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

- prototype, game jam : la vitesse d'abord
- une seule implémentation prévue → pas d'interface (**YAGNI**)
- dix classes de trois lignes pour un comportement simple

Règle pratique : on abstrait à la **troisième** variante, pas à la première.

Note:
SOLID est un outil pour gérer le changement. S'il n'y a pas de
changement prévisible, il n'y a rien à gérer.

---

## Récapitulatif
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

| | Symptôme | Remède Unity |
|---|---|---|
| **S** | script fourre-tout | un composant par responsabilité |
| **O** | `switch` / tags qui grossissent | interface + `TryGetComponent` |
| **L** | override vide, `is` dans l'appelant | revoir la hiérarchie |
| **I** | méthodes vides imposées | interfaces fines |
| **D** | champ vers une classe concrète | interface ou classe abstraite |

---

## Atelier : Dungeon Crawler modulaire
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Refactorer une scène fournie, non SOLID.

- dépôt : [StudioAlbert/UnityCourse-SOLID-DungeonCrawler](https://github.com/StudioAlbert/UnityCourse-SOLID-DungeonCrawler)
- consignes : [[01 courses/exercises/Unity/GPR-UN-APU-01 - SOLID en Unity]]

**Bonus** : ajouter un ennemi, un sort ou un piège **sans modifier** une classe existante.

---

## Pour aller plus loin
<!-- .slide: data-background="00 images/01_slide_fond_titre.jpg" -->

Séances suivantes : [[GPR-UN-APU-08 - Strategy pattern en Unity|Strategy]] · [[GPR-UN-APU-09 - Observer, State et composition|Observer, State, composition]]

- [Level up your code with design patterns and SOLID](https://unity.com/resources/design-patterns-solid-ebook) — e-book Unity
- [Unite Austin 2017 — S.O.L.I.D. Unity](https://youtu.be/eIf3-aDTOOA)
- [Software Architecture in Unity](https://youtu.be/sh7f4K9Wbj8)
- [SOLID Principles in Unity](https://www.youtube.com/watch?v=QDldZWvNK_E)
- [SOLID — Wikipedia](https://en.wikipedia.org/wiki/SOLID)
