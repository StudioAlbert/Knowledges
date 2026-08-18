# Formative — OOP — Inventory

> Source : [Google Drawing](https://docs.google.com/drawings/d/1X45oBgULpG9qzEvc8ll08ZfwipjnNe3kia-BOQkQYb8/edit)
> Cours associé : [[04 - OOP Advanced]] · [[Exercices - 04 - OOP]]

![[formative_oop_inventory.png]]

## Hiérarchie proposée

La classe de base `Item` expose une méthode `virtual use();` que chaque objet spécialise. L'`Inventory` stocke des `Item` et déclenche leur utilisation.

```mermaid
classDiagram
    class Inventory {
        vector~item~ items
        Add(item)
        UseHealthPotion()
        UseForcePotion()
        EquipBow()
        EquipSword()
        Equip(Weapon w)
        Attack()
    }
    class Item {
        <<abstract>>
        virtual use()
    }
    class Potion {
        int intensity
    }
    class Weapon {
        String name
        equip()
    }
    class Map {
        use()  // consult
    }
    class HealthPotion {
        use()
    }
    class ForcePotion {
        use()
    }
    class Sword {
        equip()
        use()  // attack
    }
    class Bow {
        equip()
        use()  // attack
    }

    Item <|-- Potion
    Item <|-- Weapon
    Item <|-- Map
    Potion <|-- HealthPotion
    Potion <|-- ForcePotion
    Weapon <|-- Sword
    Weapon <|-- Bow
    Inventory o-- Item
```

Le schéma laisse une question ouverte pour l'`Inventory` : soit une méthode par action concrète (`UseHealthPotion()`, `EquipBow()`, `EquipSword()`…), soit une méthode générique paramétrée (`Equip(Weapon w)`). C'est le point de discussion de l'exercice.
