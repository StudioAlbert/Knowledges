---
title: Dungeon Crawler Rogue-Lite
type: projet
specialisation: "[[Unity]]"
---
# Dungeon Crawler Rogue-Lite

### Dungeon Crawler Definition

> Dungeon crawler games are a subgenre of role-playing games (RPGs) characterized by players navigating through maze-like environments, typically underground settings like dungeons or labyrinths. These games often emphasize exploration, combat, and looting items. Players usually control a single character or a party of characters, moving through grid-based or free-form environments, encountering various monsters, traps, and puzzles along the way.
> 
> 
> Key elements of dungeon crawler games include:
> 
> - Exploration
> - Combat
> - Character Progression *(skipped)*
> - Loot and Inventory Management
> - Randomization

> **Berlin Interpretation (2008) of roguelike**
> 
> - Use of random dungeon to increase replayability
> - Use of permadeath
> - Turn-based
> - Non-modal (every action should be available to the player)
> - Degree of complexity allowing to couple certain goals in multiple ways
> - Player must use resource management to survive
> - Peaceful options does not exist
> - Requires the player to explore the map.

### Features required

- Camera
    - Top Down ou Vue isométrique
    - Vue compléte d’une salle
- 6 Levels / Tableaux
    - Les 6 tableaux sont générés procéduralement :
        - Difficulté croissante et équilibrée
        - Générations des pools d’ennemis
        - Génération du loot : récompenses, scoring, améliorations, etc.
        - Génération de la configuration spatiale (grand, petit, moyen)
    
    ---
    
    [Procedural Content Generation](Procedural%20Content%20Generation%201f1d4ff561f981e6a1f8d657bed8a178.md)
    
- Affrontement de 3 IA différentes parmi les suivants
    - Melee
    - Shooter
    - Doppelganger
    - Spawner / Wizard
    - Support
    - etc.
    
    ---
    
- Feedbacks
    - VFX
    - Sound design : music
    - Sound design : feedbacks
- Condition de fin

### Document préparatoire

Thematique narrative et graphique

3C : Camera, Character, Controls

3 Typologie d’ennemies

Grille de lecture :

Comportement : Blocker, chaser, shooter

Differents attaques et capacités

Typologie de groupes : pool dans une salle 

### Experience content (Time / Levels)

- Solo Game
- Rogue elements
- une durée de jeu de 5 à 10 minutes doit permettre de comprendre intentions et donner une impression représentative. Vous pouvez produire d’autres éléments (video ou screenshots) pour compléter.

### Elements d’evaluation

- une scène de test des IA :
    
    [AI Behaviour](AI%20Behaviour%201f1d4ff561f9814abe31c5a17e08ac96.md)
    
    Possibilité par des éléments de menu de choisir et de combattre les différentes IA 
    
- Eléments de test de la génération procédurale depuis l’éditeur
- jeu complet sous forme de release

### Contenu pédagogique (prévu…)

- Elements théoriques
    - Théorie des graphes
    - Pattterns/Algos : Finite State Machine, Behaviour Tree, Goal Oriented Action Planner
    - Génération procédurale : Game of life, Drunkyard, Wave function collapse

---

### Screenshots / References

### Ressources / Assets

---