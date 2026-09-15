# Exercices — GPR-UN-APU-01 — SOLID en Unity

> Cours associé : [[GPR-UN-APU-01 - SOLID en Unity]]
> Projet : [UnityCourse-SOLID-DungeonCrawler](https://github.com/StudioAlbert/UnityCourse-SOLID-DungeonCrawler)

Unity 6, C#. Un script par classe, nommé comme la classe. Chaque exercice se fait dans sa propre scène.

## Exercice 1 — Responsabilité unique : démonter le `PlayerController`

### Code de départ

```csharp
using TMPro;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [SerializeField] private float speed = 5f;
    [SerializeField] private GameObject fireballPrefab;
    [SerializeField] private float fireballCooldown = 0.5f;
    [SerializeField] private int maxHealth = 100;
    [SerializeField] private TMP_Text healthLabel;
    [SerializeField] private AudioClip hurtSound;

    private int health;
    private float nextFireTime;

    void Start()
    {
        health = maxHealth;
        healthLabel.text = health.ToString();
    }

    void Update()
    {
        var input = new Vector2(Input.GetAxis("Horizontal"), Input.GetAxis("Vertical"));
        transform.Translate(input * speed * Time.deltaTime);

        if (Input.GetButtonDown("Fire1") && Time.time >= nextFireTime)
        {
            Instantiate(fireballPrefab, transform.position, transform.rotation);
            nextFireTime = Time.time + fireballCooldown;
        }
    }

    public void TakeDamage(int amount)
    {
        health -= amount;
        healthLabel.text = health.ToString();
        AudioSource.PlayClipAtPoint(hurtSound, transform.position);
        if (health <= 0) Destroy(gameObject);
    }
}
```

### Étapes

1. Lister les **raisons de changer** de ce script : une ligne par métier.
2. Créer un composant par métier : déplacement, combat, vie, affichage de la vie, son.
3. Déplacer chaque champ et chaque ligne dans le bon composant.
4. Supprimer `PlayerController`, poser les nouveaux composants sur le GameObject du héros.
5. Ajouter `[RequireComponent]` là où un composant a besoin d'un autre.

### Critères de réussite

- le héros se déplace, tire et meurt comme avant
- aucun composant ne dépasse une trentaine de lignes
- le composant de vie ne contient aucune référence à `TMP_Text` ni à `AudioClip`
- on peut retirer le composant de son sans casser les autres

### Bonus

Réutiliser le composant de vie sur un ennemi, sans le modifier.

## Exercice 2 — Ouvert / fermé : les sorts du héros

### Code de départ

```csharp
using UnityEngine;

public enum SpellType { Fireball, IceShard, Lightning }

public class Spell : MonoBehaviour
{
    public SpellType type;
}

public class EnemyHealth : MonoBehaviour
{
    [SerializeField] private int health = 50;

    void OnTriggerEnter2D(Collider2D other)
    {
        if (!other.TryGetComponent(out Spell spell)) return;

        switch (spell.type)
        {
            case SpellType.Fireball:
                health -= 20;
                break;
            case SpellType.IceShard:
                health -= 10;
                GetComponent<Rigidbody2D>().linearVelocity = Vector2.zero;
                break;
            case SpellType.Lightning:
                health -= Random.Range(5, 31);
                break;
        }

        Destroy(spell.gameObject);
        if (health <= 0) Destroy(gameObject);
    }
}
```

### Étapes

1. Repérer ce qu'il faut modifier pour ajouter un sort `PoisonCloud`.
2. Remplacer l'`enum` par une classe abstraite `Spell : MonoBehaviour` avec une méthode `abstract void Apply(EnemyHealth target)`.
3. Créer une classe par sort : `Fireball`, `IceShard`, `Lightning`.
4. Réduire `EnemyHealth.OnTriggerEnter2D` à : récupérer le `Spell`, appeler `Apply`, détruire le sort. Exposer `public void TakeDamage(int amount)` pour les sorts.
5. Ajouter `PoisonCloud` : 5 dégâts par seconde pendant 3 secondes. Le sort étant détruit à l'impact, lancer la coroutine sur la cible : `target.StartCoroutine(...)`.

### Critères de réussite

- plus aucun `enum` ni `switch` sur le type de sort
- l'ajout de `PoisonCloud` ne modifie **aucun** fichier existant : `git diff` ne montre qu'un fichier nouveau
- les trois sorts d'origine infligent les mêmes dégâts qu'avant

### Bonus

Rendre les dégâts de chaque sort réglables dans l'Inspector, sans toucher à `EnemyHealth`.

## Exercice 3 — Substitution de Liskov : l'inventaire qui ment

### Code de départ

```csharp
using UnityEngine;

public abstract class Item : MonoBehaviour
{
    public abstract void Use(PlayerHealth user);
    public abstract void Equip(Transform hand);
    public abstract void Drop(Vector3 position);
}

public class Potion : Item
{
    public override void Use(PlayerHealth user) => user.Heal(30);
    public override void Equip(Transform hand) =>
        throw new System.NotSupportedException("On n'équipe pas une potion");
    public override void Drop(Vector3 position) => transform.position = position;
}

public class Sword : Item
{
    public override void Use(PlayerHealth user) { }   // rien à faire
    public override void Equip(Transform hand) => transform.SetParent(hand, false);
    public override void Drop(Vector3 position) => transform.SetParent(null);
}

public class QuestRelic : Item
{
    public override void Use(PlayerHealth user) { }
    public override void Equip(Transform hand) { }
    public override void Drop(Vector3 position) =>
        Debug.LogWarning("Impossible de lâcher la relique");
}

public class Inventory : MonoBehaviour
{
    [SerializeField] private Item[] items;
    [SerializeField] private Transform hand;

    public void EquipAll()
    {
        foreach (Item item in items)
            item.Equip(hand);   // exception dès qu'on tombe sur une potion
    }
}
```

`PlayerHealth.Heal(int)` est à ajouter au composant de vie de l'exercice 1.

### Étapes

1. Pour chaque sous-classe, marquer les méthodes vides, celles qui lèvent une exception et celles qui ne font pas ce que le nom promet.
2. Écrire, pour chaque méthode d'`Item`, la promesse qu'elle fait au code client.
3. Remplacer la hiérarchie par des interfaces de capacités : `IUsable`, `IEquipable`, `IDroppable`.
4. Faire implémenter à chaque objet **uniquement** ce qu'il sait faire.
5. Adapter `Inventory` pour qu'il ne manipule que des objets capables de l'action demandée.

### Critères de réussite

- plus aucune méthode vide, aucune `NotSupportedException`
- `Inventory` ne contient aucun test de type (`is Potion`, `as Sword`)
- `EquipAll()` n'échoue jamais, quel que soit le contenu de l'inventaire

### Bonus

Ajouter un `Shield`, équipable et lâchable, et vérifier que `Inventory` n'a pas besoin d'être modifié.

## Exercice 4 — Ségrégation des interfaces : les habitants du donjon

### Code de départ

```csharp
using UnityEngine;

public interface IDungeonEntity
{
    void Move(Vector3 target);
    void Attack(PlayerHealth player);
    void TakeDamage(int amount);
    void CastSpell(Vector3 target);
    void Talk();
    void Open();
}

public class SkeletonArcher : MonoBehaviour, IDungeonEntity { /* à compléter */ }
public class SpikeTrap      : MonoBehaviour, IDungeonEntity { /* à compléter */ }
public class Merchant       : MonoBehaviour, IDungeonEntity { /* à compléter */ }
public class Chest          : MonoBehaviour, IDungeonEntity { /* à compléter */ }
public class Hero           : MonoBehaviour, IDungeonEntity { /* à compléter */ }
```

Ce code ne compile pas tel quel : c'est l'étape 1.

### Étapes

1. Implémenter `IDungeonEntity` dans les cinq classes, et compter les méthodes laissées vides.
2. Remplir ce tableau : une ligne par classe, une colonne par méthode, ✔ si la méthode a un vrai sens.
3. Regrouper les colonnes en interfaces fines, d'**une ou deux méthodes** chacune.
4. Supprimer `IDungeonEntity`, faire implémenter à chaque classe ses seules interfaces.
5. Écrire un composant `Interactor` sur le héros : touche `E`, il appelle `Talk()` ou `Open()` sur l'objet devant lui s'il en est capable.

### Critères de réussite

- aucune méthode vide dans les cinq classes
- aucune interface de plus de deux méthodes
- `Interactor` utilise `TryGetComponent` avec des interfaces, sans connaître les classes concrètes

### Bonus

Comparer avec l'exercice 3 : écrire en deux phrases pourquoi on aboutit à la même forme de solution, et ce qui distingue le problème de départ.

## Exercice 5 — Inversion de dépendance : leviers, portes et herses

### Code de départ

```csharp
using UnityEngine;

public class Door : MonoBehaviour
{
    public void Open()  => gameObject.SetActive(false);
    public void Close() => gameObject.SetActive(true);
}

public class Portcullis : MonoBehaviour
{
    [SerializeField] private float liftHeight = 3f;
    public void Raise() => transform.position += Vector3.up * liftHeight;
    public void Lower() => transform.position -= Vector3.up * liftHeight;
}

public class Lever : MonoBehaviour
{
    [SerializeField] private Door door;
    [SerializeField] private Portcullis portcullis;
    private bool isOn;

    void OnTriggerEnter2D(Collider2D other)
    {
        if (!other.CompareTag("Player")) return;
        isOn = !isOn;

        if (door != null)
        {
            if (isOn) door.Open(); else door.Close();
        }
        if (portcullis != null)
        {
            if (isOn) portcullis.Raise(); else portcullis.Lower();
        }
    }
}
```

### Étapes

1. Dessiner le schéma de dépendances actuel : qui connaît qui ?
2. Créer le contrat `ISwitchable` avec `Activate()` et `Deactivate()`.
3. Faire implémenter `ISwitchable` à `Door` et `Portcullis`.
4. Réécrire `Lever` pour qu'il ne connaisse **que** `ISwitchable`, avec une liste de cibles réglable dans l'Inspector.
5. Choisir et justifier la solution Inspector : champ `GameObject` + `GetComponent<ISwitchable>()`, ou classe abstraite `Switchable : MonoBehaviour`.
6. Ajouter une `PressurePlate` : active tant que le héros est dessus, désactive quand il en sort.
7. Construire la scène : une plaque ouvre deux portes, un levier lève une herse.

### Critères de réussite

- `Lever` et `PressurePlate` ne contiennent aucun nom de mécanisme concret (`Door`, `Portcullis`)
- une cible qui n'implémente pas `ISwitchable` est signalée dans l'éditeur, pas au lancement (`OnValidate`)
- ajouter une `Torch` ne modifie ni `Lever` ni `PressurePlate`

### Bonus

Un mécanisme qui implémente `ISwitchable` et commande lui-même d'autres `ISwitchable` : un relais qui ouvre toutes les grilles d'une salle.

## Atelier — Dungeon Crawler modulaire

Dépôt : [UnityCourse-SOLID-DungeonCrawler](https://github.com/StudioAlbert/UnityCourse-SOLID-DungeonCrawler)

### Point de départ

Une scène jouable, volontairement non SOLID : héros, ennemis, pièges, portes.

### Étapes

1. Jouer la scène, lister les comportements à conserver.
2. Lire le code et noter, pour chaque script, le principe qu'il enfreint et le symptôme observé.
3. Prioriser : commencer par ce qui bloque le plus l'ajout de contenu.
4. Refactorer par petites étapes, en rejouant la scène après chacune. Un commit par étape.
5. Relire le résultat avec la slide « Quand ne pas appliquer SOLID » : supprimer les abstractions qui n'ont qu'une implémentation et aucune raison d'en avoir une seconde.

### Critères de réussite

- la scène se joue exactement comme avant
- l'historique Git montre des commits courts, chacun rattaché à un principe
- un fichier `NOTES.md` liste les problèmes trouvés et la correction retenue pour chacun

### Bonus

Ajouter un ennemi, un sort **ou** un piège sans modifier une seule classe existante. Le `git diff` du commit ne doit montrer que des fichiers nouveaux, des prefabs et la scène.
