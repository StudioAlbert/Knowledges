---
title: SOLID Principles in Unity
type: course
status: Backlog
subject: Unity
duration_h: 3
bloc_gsda: Architecture et Patterns Unity
created: 2022-12-13T22:10
---
# SOLID Principles in Unity

# 🧱 Architecture logicielle SOLID appliquée aux jeux vidéo (Unity + Dungeon Crawler)

---

## Introduction : Pourquoi appliquer les principes SOLID dans un jeu vidéo ?

### 🔧 Problèmes fréquents :

- Ajout d’un nouvel ennemi ou d’un piège = modification de plusieurs scripts
- Code fragile : un changement en casse d’autres
- Difficultés de test, de réutilisation, d’évolution

### 🧩 Ce qu’apporte SOLID :

- **Modularité** : comportements séparés, testables individuellement
- **Évolutivité** : facile d’ajouter un sort, un objet, un ennemi
- **Ré-utilisabilité** : composants indépendants et interchangeables

### 🎯 Fil rouge pédagogique : le **Dungeon Crawler**

Tout au long du cours, nous partons d’un mini-jeu type donjon, avec :

- Un héros (le joueur)
- Des ennemis (corps à corps, distance, pièges)
- Des objets, loot, sortilèges

---

## S — Single Responsibility Principle (SRP)

### 🎯 But :

> *une [classe](https://fr.wikipedia.org/wiki/Classe_(informatique)), une fonction ou une méthode doit avoir une et une seule unique raison d'être modifiée. Cela favorise la modularité et facilite la maintenance en évitant les classes surchargées de responsabilités.*
[https://fr.wikipedia.org/wiki/Principe_de_responsabilité_unique](https://fr.wikipedia.org/wiki/Principe_de_responsabilit%C3%A9_unique)
> 

> Une classe ne doit avoir qu’une seule raison de changer (one reason to fail)
> 

![[solid_principles_in_unity_01.png]]

![[solid_principles_in_unity_02.png]]

### ❌ Mauvais exemple :

```csharp
public class PlayerController : MonoBehaviour {
    void Move() {...}
    void CastFireBall() {...}
    void UpdateUI() {...}
    void Die() {...}
    void TakeDamage() {...}
}

```

➡️ Trop de responsabilités mélangées : difficile à tester, maintenir, étendre.

### ✅ Bon exemple (composants) :

- `PlayerMovement.cs`
- `PlayerCombat.cs`
- `PlayerHealth.cs`

Sur le même GameObject : Unity encourage cette **composition**.

### 🛠️ Exercice :

Refactorer le `PlayerController` monolithique en composants SRP.

## O — Open/Closed Principle (OCP)

### 🎯 But :

> une entité applicative (classe, fonction, module ...) doit être fermée à la modification directe mais ouverte à l'extension. L'objectif est de permettre l'ajout de nouvelles fonctionnalités sans altérer le code existant.
[https://fr.wikipedia.org/wiki/Principe_ouvert/fermé](https://fr.wikipedia.org/wiki/Principe_ouvert/ferm%C3%A9)
> 

> Le code doit être ouvert à l’extension mais fermé à la modification.
> 

![[solid_principles_in_unity_03.png]]

![[solid_principles_in_unity_04.png]]

### ❌ Mauvais exemple :

```csharp
public class Attack: MonoBehaviour {
    public enum AttackType { Missile, ElectricArc, Trap }
    void DoDamage() {
        switch (type) {
            case Melee: ...
            case Ranged: ...
            case Trap: ...
        }
    }
}
```

```csharp
void OnTriggerEnter2D(Collider2D other)
{
    if (other.CompareTag("Enemy"))
    {
        TakeDamage(10); // Fixed damage for Enemy
    }
    if (other.CompareTag("EnemyProjectile"))
    {
        TakeDamage(Random.Range(5, 10)); // Random damage for projectiles
    }
}
```

➡️ Chaque ajout d’ennemi ou d’impact implique de **modifier** le script, enfreint l’Open Closed Principle

### ✅ Bon exemple :

- Interface `IProjectile`, ou héritage `DamageDealer`
- Implémentations : `ElectricArc`, `Misssile`, `Trap`

➡️ Le comportement est hérité d’une abstraction, sans embranchement.

### 🛠️ Exercice :

Ajouter un nouvel type de dommage (e.g. `Trap`) sans toucher à `Enemy.cs`.

---

## L — Liskov Substitution Principle (LSP)

### 🎯 But :

> Si q(x) est une propriété démontrable pour tout objet x de type T, alors q(y) est vraie pour tout objet y de type S tel que S est un sous-type de T.
> 
> 
> [https://fr.wikipedia.org/wiki/Principe_de_substitution_de_Liskov](https://fr.wikipedia.org/wiki/Principe_de_substitution_de_Liskov)
> 

> Une classe dérivée doit pouvoir remplacer sa classe de base sans effet indésirable.
> 

![[solid_principles_in_unity_05.png]]

![[solid_principles_in_unity_06.png]]

### ❌ Mauvais exemple :

```csharp
public class Enemy {...}

public class Spider : Enemy {
    public override void Move() {}
    public override void Attack() {}
    public override int DoDamage() {}
}

public class Barrel : Enemy {
    public override void Move() {} // vide : viole le principe Liskov Substitution
    public override void Attack() {} // vide : viole le principe Liskov Substitution
    public override int DoDamage() {}
}

```

➡️ `Trap` viole LSP : il hérite de méthodes qu’il **ne peut pas garantir**.

### ✅ Bon exemple :

- Interfaces spécialisées :
    - `IMovable`
    - `IAttacker`
    - `IDamageDealer`
- `Enemy` : `IMovable`, `IAttacker`
- `Trap` : seulement `IDamageDealer`

### 🛠️ Exercice :

Identifier une hiérarchie incohérente (héritage abusif), proposer une refonte par composition ou interface.

---

## I — Interface Segregation Principle (ISP)

### 🎯 But :

> aucun client ne devrait dépendre de méthodes qu'il n'utilise pas
[https://fr.wikipedia.org/wiki/Principe_de_ségrégation_des_interfaces](https://fr.wikipedia.org/wiki/Principe_de_s%C3%A9gr%C3%A9gation_des_interfaces)
> 

> Mieux vaut plusieurs interfaces spécifiques qu’une trop large.
> 

![[solid_principles_in_unity_07.png]]

### ❌ Mauvais exemple :

```csharp
public interface IEntity {
    void Move();
    void Attack();
    void UseItem();
    void Talk();
}

```

➡️ Un `Projectile` ou un `Trap` n'a **rien à faire** avec `UseItem()` ou `Talk()`.

### ✅ Bon exemple :

- Interfaces fines :
    - `IMovable`
    - `IAttacker`
    - `ISpellCaster`
    - `IUsableItem`

➡️ Chaque entité implémente **uniquement ce qui lui est utile**.

### 🛠️ Exercice :

Créer les bonnes interfaces, réorganiser les scripts selon les besoins réels des entités (héros, monstres, pièges, objets).

> 🧠 **Remarque :**
Les principes Liskov Substitution et Interface Segregation, présentent certaines similitudes et peuvent aboutir à des solutions similaires (= des interfaces séparées)
> 

---

## D — Dependency Inversion Principle (DIP)

### 🎯 But :

> Les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. Les deux doivent dépendre d'abstractions.
[https://fr.wikipedia.org/wiki/Inversion_des_dépendances](https://fr.wikipedia.org/wiki/Inversion_des_d%C3%A9pendances)
> 

> Les modules de haut niveau ne doivent pas dépendre des détails, mais d’abstractions.
> 

![[solid_principles_in_unity_08.png]]

![[solid_principles_in_unity_09.png]]

### ❌ Mauvais exemple :

```csharp
public class Door {
    void Open() {...}
    void Close() {...}
}

public class Switch{

	[SerializeField] private Door door;

    void OnTriggerEnter() {
        door.Open();
    }
    void OnTriggerExit() {
        door.Close();
    }
}

```

```csharp
// Other use case
public class Light{}
public class OtherSwitch{}
```

➡️ `Switch` dépend **des classes concrètes** : difficile à tester, à modifier.

### ✅ Bon exemple :

- Interface `ISwitchable`
- Implémentations : `LightBulb`,  `Door`, `Trap`, `Robot`
- Injection via Unity, Zenject, Ninject, ou constructeur

### 🛠️ Exercice :

Créer un système de portes et passages (grilles de donjon) en inversant les dépendances.

---

---

## 🧪 — Atelier final : Dungeon Crawler modulaire

[https://github.com/StudioAlbert/UnityCourse-SOLID-DungeonCrawler](https://github.com/StudioAlbert/UnityCourse-SOLID-DungeonCrawler)

### 🎯 Objectif :

Refactorer une scène Unity fournie (non SOLID) pour appliquer tous les principes.

### 💡 Objectifs pédagogiques :

- Identifier les responsabilités mal réparties
- Repenser les hiérarchies de classes
- Introduire des interfaces
- Injecter des comportements dynamiquement

### 🛠️ Livrables :

- Scène fonctionnelle avec comportements refactorés
- Bonus : ajout d’un nouvel ennemi, sort ou piège, sans toucher aux classes existantes

---

## ⚒️ — Outils : Design Patterns utiles en Unity

### ✏️ Keep everything designer friendly

- Dans Unity : Les interfaces ne sont pas vues dans l’inspecteur, les classes abstraites oui
- Pro-Tip : Les classes abstrait

```csharp
public interface ISwitchable
{
    public void Activate();
    public void Deactivate();
}
```

```csharp
public abstract class Switchable : MonoBehaviour
{
    public abstract void Activate();
    public abstract void Deactivate();
}
```

### ⚙️ Strategy Pattern :

- Pour les IA d’ennemis ou les styles d’attaque (ex. : `IAttackStrategy`)

[[strategy_pattern|Strategy pattern]]

### 🔔 Observer / Event System

- Pour décorréler les événements : UI, dégâts, ouverture de portes, etc.

### 🎭 State Pattern

- Pour la gestion d'états : patrouille, poursuite, attaque, mort

### 🧱 Composition over Inheritance

- Dans Unity, préférez les **composants** aux hiérarchies profondes

---

# 📚 — Ressources

### Principles Knowledge

[Level up your code with design patterns and SOLID E-book | Unity](https://unity.com/resources/design-patterns-solid-ebook)

Examples, uses cases book (+ Patterns)

[Unite Austin 2017 - S.O.L.I.D. Unity](https://youtu.be/eIf3-aDTOOA?si=6G4eXiqtIaYnNvGY)

Same (But in video)

---

### Why code architecture ?

[Software Architecture in Unity](https://youtu.be/sh7f4K9Wbj8?si=It6Ro6IxQcEvLUao)

---

### More

[SOLID Principles in Unity](https://www.youtube.com/watch?v=QDldZWvNK_E)

[SOLID Unity3D](https://youtube.com/playlist?list=PLB5_EOMkLx_WjcjrsGUXq9wpTib3NCuqg&si=Mty-_oGn24xuK6dX)

[SOLID](https://en.wikipedia.org/wiki/SOLID)

[S.O.L.I.D principles for Unity](https://medium.com/@alejandrodiazjllo/s-o-l-i-d-principles-for-unity-a1556ee99e7c)

[Mastering SOLID Principles: A Comprehensive Guide for Software Engineers](https://medium.com/@GetInRhythm/mastering-solid-principles-a-comprehensive-guide-for-software-engineers-da53b054c9e1)

[The Importance and Application of SOLID Principles in Unity Game Development](https://medium.com/@mthndmr16/the-importance-and-application-of-solid-principles-in-unity-game-development-94be186ad51f)
