# RTS  Pacifique / City Builder

## Pitch

Vous incarnez le guide bienveillant d'une communauté en expansion, habitant une île mystérieuse et fertile.
Votre objectif est de développer votre territoire en récoltant et en exploitant les ressources naturelles tout en maintenant une harmonie parfaite avec la nature.
Aucun conflit ne vient perturber cette quête de prospérité; au lieu de cela, la réussite dépend de la planification stratégique et de l'utilisation judicieuse des ressources disponibles.

---

## Attendus / Eléments d’évaluations

### Gameplay

Génération procédurale persistente
Ressources de base : bois, pierre, nourriture
Batiments relatifs a chaque type de NPC
3C :  Vue Top Down, zoom/dezoom, panoramique

### Implementations

SFML as Graphic Framework
Ressource management
Behaviour tree
Callback systems : Lambda expressions, functions pointers

### High quality code

Google C++ Style Guide ([link](https://google.github.io/styleguide/cppguide.html))
Efficient
Test Driven Archtecture
Extensible

---

## 🤖 Typologies d’IA

### 🫒 Cueilleurs (requis)

Description :
Les cueilleurs sont spécialisés dans la collecte des ressources naturelles telles que les baies, les fruits et les herbes médicinales.

Rôle :
Parcourir les forêts et les prairies pour ramasser les ressources nécessaires à la survie et au commerce.

### 🪵Bûcherons (requis)

Description :
Experts dans la gestion forestière, les bûcherons coupent les arbres tout en replantant de nouveaux pour assurer la durabilité.

Rôle :
Récolter le bois pour la construction et les feux de camp, tout en préservant l'équilibre forestier.

### ⛏️ Mineurs (requis)

Description :
Habiles dans l'extraction des minéraux et des pierres précieuses, les mineurs travaillent dans les mines et les carrières.

Rôle :
Extraire les ressources minérales nécessaires pour la construction d'infrastructures et la fabrication d'outils.

### ⚒️ Constructeurs

Description :
Les constructeurs utilisent les ressources collectées pour ériger des bâtiments et améliorer les infrastructures de la communauté.

Rôle :
Concevoir et construire des structures variées pour améliorer la vie des habitants et renforcer la communauté.

---

## 🏠Liste des bâtiments

### 🧑‍🌾 Production et de Récolte (requis)

Cabane de Cueilleurs : Augmente l'efficacité de la collecte des fruits et des herbes par les cueilleurs.
Cabane de Bûcherons : Permet aux bûcherons de couper du bois et de replanter des arbres pour une gestion durable des forêts.
Mine : Lieu d'extraction des minéraux et des pierres précieuses par les mineurs.

### 🏭 Bâtiments de Transformation

Scierie : Transforme le bois brut en planches et autres matériaux de construction.
Forge : Permet de fondre les métaux extraits pour fabriquer des outils et des équipements.
Atelier de Tisserand : Transforme les ressources naturelles en textiles et vêtements.

### 🏬 Bâtiments de Stockage

Entrepôt : Offre une capacité de stockage supplémentaire pour toutes les ressources collectées.
Grenier : Spécialisé dans le stockage des denrées alimentaires

### 💰 Suggestions d’éléments d’économie

Récolte et stockage des ressources
Système de troc/marché entre ressources
Taxation : génération d’or en fonction basée sur la population

---

### Références

[https://interfaceingame.com/games/frostpunk/](https://interfaceingame.com/games/frostpunk/)

[https://store.steampowered.com/app/1044720/Farthest_Frontier/](https://store.steampowered.com/app/1044720/Farthest_Frontier/)

[Discussions](Discussions%20313d4ff561f980b3ad8ac8d561fe7284.md)