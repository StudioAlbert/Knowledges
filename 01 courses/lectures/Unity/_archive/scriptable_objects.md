---
title: Scriptable Objects
type: course
status: Backlog
subject: Unity
bloc_gsda: Architecture et Patterns Unity
created: 2022-12-13T22:38
manual_order: 56
---
# Scriptable Objects

1. Principles
    1. un autre type de scripts, les scriptable objects
    2. Assets = Fichiers = Datas
2. Data containers
    
    ```csharp
    using UnityEngine;
    
    [CreateAssetMenu(menuName = "Dungeon/Loot", fileName = "loot")]
    public class LootData : ScriptableObject
    {
        [SerializeField] private int _atk;
        [SerializeField] private float _weight;
    }
    ```
    
    1. as Loot
    2. as Weapons
3. Managers
    1. Float value
        
        ```csharp
        using UnityEngine;
        
        [CreateAssetMenu(menuName = "ScriptableValues/float", fileName = "floatValueName")]
        public class FloatValue : ScriptableObject
        {
            private float _floatValue;
            public float Value { get => _floatValue; set => _floatValue = value; }
        }
        
        ```
        
    2. Runtime Set
        
        ```csharp
        [CreateAssetMenu(menuName = "ScriptableValues/runtimeSet", fileName = "runtimeSet")]
        public class SORuntimeSet : ScriptableObject
        {
        
            [SerializeField] private int _limit;
            
            private readonly List<LootData> _list = new List<LootData>();
        ```
        
    
4. UI

---

# Synopsis

1. PrincipesUnt
    1. Création et entrée de Menu
2. Scriptable as data containers
    1. Items
        1. Créer un modèle de data container. 4 Informations : Mana Gain, Health, Money Min/Max
        2. Créer différents profils de loots
            
            
            |  | Mana | Health | Money |
            | --- | --- | --- | --- |
            | Health potion | 0 | 10 | 0,0 |
            | Gold | 0 | 0 | 5,10 |
            | Mana Potion | 2 | 0 | 0,0 |
            | Banco | 3 | 25 | 10,50 |
    2. Inventory Item
        1. Créer un modéle de data container pour l’inventaire : Name, Atk Stat, Weight
        2. Créer 3 profils d’items
        
        | Name | Atk | Weight |
        | --- | --- | --- |
        | Axe | 6 | 10 |
        | Sword | 2 | 1 |
        | Long sword | 4 | 5 |
3. Scriptable as Runtime persistent datas
    1. Float value
        1. créer un scriptable object avec un membre de type float et son accesseur
        2. Depuis le menu choisi, instancier plusieurs déclinaisons : HealthValue, Mana, Gold
        3. Créer un objet d’interface UI prenant en paramètre (SerializeField) une des objets FloatValue pour mettre à jour l’interface
    2. Runtime Set
        1. Créer un scriptable object avec un membre de type List<> + des méthodes pour ajouter un élément à la liste
    3. Usage
        1. Ausein d’un script player, en fonction de l’objet collided, utiliser les données pour :
            1. Soigner (Health datas)
            2. Collecter Mana et Gold
            3. Stocker sous forme d’inventaires les armes ramassées
