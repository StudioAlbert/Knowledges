---
title: GDD
source: https://sae-team-924.atlassian.net/wiki/spaces/PC/pages/7536779
confluence_id: 7536779
space: PC — Projet Commun
version: 47
updated: 2025-12-02
author: Maximilien de Heer
tags: [confluence, projet-commun, gdd]
---

# GDD

## Pitch

Les employés de l'aéroport vont être mis à rude épreuve ! Gérez un avion en plein vol, empêchez le de s'écraser, triez les valises piégées à la douane ! Vous ne vous en sortirez pas sans coopérer.

## Eléments globaux

- **Caméra** : Isométrique ou top down 3D
- **Scène** : Le jeu se jouera sur une seule et même scène afin d'éviter des chargements entre elles, à part pour le menu principal
- **Timer** : Présent dans chaque niveau
- **Contrôles** :
    - *Bouger* : Stick gauche
    - *Interaction* : Button South
    - *Jeter* : Button East
    - *Dash* : ?
    - *Emote* : ?
- **Score** : Obtenu après avoir joué aux mini-jeux
    - **Temps** : Récolter afin d'aider à compléter le dernier niveau
    - **Argent** : Utiliser pour acheter des améliorations présentes à travers des magasins dans l'aéroport
- **Emotes** : Les emotes ne seront que des stickers

## Mini-jeux

- Description des mini-jeux → [[01 courses/projects/Unity/924 - Projet Commun - Airport/Idées/Liste des mini-jeux]]
- Le design de certaines missions changera dépendant du nombre de joueurs présents

| **Mini-jeux** | **Controls** | **Début** | **Fin** | **Caméra** |
| --- | --- | --- | --- | --- |
| **HUB** | • *Prendre un objet* → Button South<br>• *Réparer la porte* → **Appuie long** Button South<br>• *Remplir snack* → **Spam** Button South<br>• *Mettre à jour les vols* → Button South<br>• *Passer la serpillère* → Stick Gauche<br>• *Toilettes* → Stick Gauche/Droit Haut Bas<br>• *Lâcher un objet* → Button East<br>• *Lancer un objet* → **Appuie long** Button East | Début du jeu | | *Standard* |
| **Douane** | • *Valise problématique* → Button South<br>• *Changer de tapis* → Button South | Première mission à faire | • Le temps est écoulé<br>• Tous les bagages et NPC ont passé | *Standard* |
| **Tapis roulant** | • *Prendre une valise* → Button South<br>• *Poser la valise* → Button East<br>• *Lancer la valise* → **Appuie Long** Button East | Seconde mission à faire, se débloque après la douane | • Le temps est écoulé<br>• Plus de valise dans un camp | *Standard* |
| **Valise perdue** | • *Tirer une caisse* → **Appuie Long** Button South<br>• *Pousser* → soit **Appuie Long** Button South, soit avancer dedans | Troisième mission à faire, se débloque après le tapis roulant | • Le temps est écoulé<br>• Les valises ont été retrouvées | *Standard* |
| **Embarquement** | • *Prendre une valise* → Button South<br>• *Poser la valise* → Button East<br>• *Lancer la valise* → **Appuie Long** Button East | Quatrième mission à faire, se débloque après la valise perdue | • Le temps est écoulé<br>• Il n'y a plus de bagage ni de passager | *Standard* ou agencé différemment (pas isométrique) |
| **Avion** | • *Prendre un item* → Button South<br>• *Lâcher/Lancer* → Button East (maintenir ou non)<br>• *Réparer* → maintenir Button South<br>• *Redresser l'avion* → **Spam** Button South | Dernière mission, se débloque après toutes les autres missions | • Le temps récolté dans les niveaux précédents est fini<br>• Trop d'erreurs sont produites sur l'avion et il crashe | *Standard* |
| **(Parachute)** | • *Mouvement* → stick gauche | Fin du mini-jeu de l'avion | Les personnages atterrissent sur une île et les scores finaux sont montrés (Timer) | *Vu de côté* |

## IA

- **Karen** : IA méchante présente pour faire chier
- **IA Hub** : Foule n'ayant pas réellement un but précis
- **Mini-jeux** :
    - *Douane* : Passe les scanners et attend d'être vérifiée avant d'être soit arrêtée, soit laissée dedans
    - *Tapis roulant* : Attend devant les tapis roulants afin de récolter leurs valises
    - *Valise perdue* : (Normalement il n'y en a pas mais peut changer)
    - *Embarquement* : Passe au comptoir pour faire vérifier son passeport avant d'être soit rejeté, soit laissé sur l'avion
    - *Avion* : Demande certains items dans un temps donné, si le client n'est pas satisfait, cela va affecter le niveau de satisfaction global dans le mini-jeu

## Questions

- Réfléchir comment les karts vont être utilisés ? Quel moment ? Quel parcours ? Prix à payer pour utilisation de kart ? (à répondre plus tard)
- Props qui traversent les murs car c'est en kinematic ? (à voir plus tard)
- Cinématique ?
- Lost luggage avec IA ? Si oui, ramener la valise à l'IA ?
- Amélioration du Grab ?

## Assets

- Certains assets peuvent se casser dépendant si l'asset le permet ou non
- Pour les emotes, il y aura besoin d'assets pour les stickers

| **HUB** | **Avion** | **Douane** | **Tapis roulant** | **Valise perdue** | **Embarquement** | **(Parachute)** |
| --- | --- | --- | --- | --- | --- | --- |
| • Poubelles<br>• Tableau de bord<br>• Toilettes<br>• Serpillère<br>• Portes<br>• Machine à snack | • Sièges<br>• Parachutes fermés<br>• Snacks/boissons<br>• Avion ouvert | • Tapis roulant<br>• Bagages | • Bagages<br>• Tapis roulant | • Caisses en bois<br>• Bagages | • Bagages<br>• Tapis roulant<br>• Soute d'avion | • Parachute ouvert<br>• Débris<br>• Argent |
