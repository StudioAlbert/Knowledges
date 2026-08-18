---
title: Physics
type: course
chapter: "1.2"
module: "🐣 - Beginner"
topic:
  - Physics
created: 2025-11-20T22:15
source: notion
---
# Physics

### Exemples

## Contenu

Timing : 6h

### Rigidbody

Le composant Rigidbody assure le déplacement des objets en accord avec les lois de la physique (Chute, Inertie, Applications des forces)

![[physics_01.png]]

### Colliders

Les colliders assurent les interactions entre les objects.

Le rôle des colliders ***non-triggers*** est de faire en sorte que les objets interagissent “physiquement” :

- ils ne se rentrent pas les uns dans les autres
- on peut pousser un objet avec un autre
- on peut poser un objet sur un autre

![[physics_02.png]]

Collider standard

Les colliders ***triggers*** servent de détecteurs, de déclencheurs sans véritable interaction physique. 
Par ex : Un personnage arrive devant une porte, elle s’ouvre.

![[physics_03.png]]

Trigger

Les colliders peuvent avoir différentes formes qui servent d’approximations aux collisions

![[physics_04.png]]

Différents colliders

![[physics_05.png]]

Bouton de modification

### Events

Les collisions déclenchent des évènements dans le code, selon les règles suivantes.

il faut un rigidbody sur au moins un des objets 

| ***Collider A*** | ***Collider B*** | ***Event OnTriggerXXXX*** | ***Event OnCollisionXXXX*** |
| --- | --- | --- | --- |
| Standard | Standard |  | Oui A, Oui B |
| Standard | Trigger | Oui A, Oui B |  |
| Trigger | Standard | Oui A, Oui B |  |
| Trigger | Trigger | Oui A, Oui B |  |

Les fonctions OnTriggerXXXX, OnCollision recoivent en paramétre l’objet entré en collision avec l’objet propriétaire su script.

Cela nous permet de qualifier la collision survenue  (Ex : Bullet vs Vehicules)  en testant la présence de Tags ou de composants.

Une fois la collision qualifiée, on déclenche de nouvelles interactions (Dommages, Score, Captation dans l’inventaire, etc.)

```cpp
private void OnCollisionEnter(Collision other)
{
    if(other.gameObject.CompareTag("Bullet") || other.gameObject.CompareTag("Tank"))
    {
        Debug.Log("Box touched !");
        _capRb.AddForce(Vector3.up * _capForce);
        _boxRb.AddForce((other.transform.position - transform.position) * _boxForce);

        Collider myCollider = GetComponent<Collider>();
        Destroy(myCollider);
    }
}

```

---

---
