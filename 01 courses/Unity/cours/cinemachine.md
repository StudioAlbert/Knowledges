---
title: Cinemachine
type: course
status: Backlog
subject: Unity
duration_h: 3
bloc: "[[Caméra et Animation]]"
created: 2025-01-10T11:36
---
# Cinemachine

### **Objectifs pédagogiques :**

1. Comprendre les fonctionnalités principales de Cinemachine.
2. Apprendre à configurer et personnaliser les caméras virtuelles.
3. Intégrer des transitions et suivre dynamiquement des objets dans une scène Unity.
4. Réaliser une séquence de caméra fluide et dynamique dans un mini-projet.

---

### **I. Introduction**

1. **Qu'est-ce que Cinemachine ?**
    - Présentation et cas d'usage.
    - Les avantages par rapport à la caméra par défaut de Unity.
    - Introduction rapide à l'interface de Cinemachine.
2. **Les principaux composants de Cinemachine :**
    - **Cameras virtuelles** : Concept et utilité.
    - **Brain Cinemachine** : Rôle dans la gestion des caméras.
    - **Timeline et interaction avec Cinemachine.**
    
    ### **Exercice 1 :**
    
    Créer une première scène Unity :
    
    - Ajouter une caméra avec **Cinemachine Brain**.
    - Configurer une caméra virtuelle simple pour suivre un objet.

### **II. Fonctionnalités principales de Cinemachine**

1. **Cinemachine Free Look :**
    - Utilisation pour les vues à la troisième personne (caméra orbitale).
    - Ajustement des rigues (Top, Middle, Bottom) et des courbes de suivi.
2. **Cinemachine Virtual Camera (VCam) :**
    - Réglages de base : champ de vision, profondeur de champ.
    - Modes de suivi et de cadrage : "Composer", "Do Nothing", "Hard Lock".
    - Ajout d'un objectif : cadrage dynamique pour suivre un personnage ou un objet.
3. **Transitions entre caméras :**
    - Configuration des blends dans **Cinemachine Brain**.
    - Création de transitions douces entre plusieurs VCams.
        
        ### **Exercice 2 :**
        
        Créer une scène où :
        
        - La caméra suit un personnage avec une caméra orbitale.
        - Un changement de caméra se produit lorsqu’un événement (ex. : appui sur une touche) survient.

### **III. Scénarisation avancée et outils supplémentaires**

1. **Cinemachine Dolly Track :**
    - Configuration et ajout d’un chemin pour des mouvements de caméra complexes.
    - Synchronisation avec des triggers ou un événement.
2. **Cinemachine State-Driven Camera :**
    - Gestion des caméras basée sur les animations ou états du personnage (exemple : courir, sauter, attaquer).
3. **Cinemachine Collider et autres extensions :**
    - Éviter que la caméra traverse des objets.
    - Configurer des limites pour améliorer l’expérience utilisateur.
    
    ### **Exercice 3 :**
    
    Créer une petite cinématique :
    
    - Une caméra qui suit un chemin défini (Dolly Track).
    - Ajouter des transitions automatiques entre plusieurs perspectives pour raconter une action (par exemple, un personnage traversant un environnement).

### **IV. Synthèse et conclusion (30 minutes)**

1. **Recap des fonctionnalités explorées.**
2. **Questions-réponses.**
3. **Travail individuel** :
    - Améliorer la cinématique créée en ajoutant des détails (effets visuels, transition personnalisée, ou interactions avec Timeline).

---

### **Matériel requis :**

- Unity (version récente) avec Cinemachine installé via le **Package Manager**.
- Un projet Unity de base contenant des modèles 3D simples (personnage, environnement).
