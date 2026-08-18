# Algo — Treasure Hunt

> Source : [Google Drawing](https://docs.google.com/drawings/d/1hfEww8cZW_o6jgRDN31vgWN90Qm3_1RFU8nXuPFGSpE/edit)
> Cours associé : [[03 - Data Structures (array, vector, map, etc.)]]

![[algo_treasure_hunt.png]]

## Organigramme

Exemple d'organigramme (schéma de séquence) attendu avant d'implémenter : on décrit le déroulement du programme avant d'écrire la moindre ligne de code.

```mermaid
flowchart TD
    A([Début de la chasse]) --> B[Demander au joueur une taille de carte]
    B --> C[Initialisation de la carte<br/>taille 6x6]
    C --> D[Cacher le trésor<br/>Choix aléatoire d'un index dans le tableau]
    D --> E{Voulez-vous continuer ?}
    E -- oui --> B
    E -- non --> F([Fin de la chasse])
```
