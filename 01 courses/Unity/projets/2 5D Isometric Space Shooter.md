---
title: 2.5D Isometric Space Shooter
type: projet
specialisation: "[[Unity]]"
---
# 2.5D Isometric Space Shooter

### Genre definition

> A 2.5D isometric space shooter combines the visual depth of 3D with the simplicity of 2D mechanics. Players control a spacecraft in an isometric environment, engaging enemies and avoiding obstacles. The genre emphasizes fast-paced action, strategic navigation, and precise shooting.

iIsometric video game graphics, **a style in video games, with the playfield viewed at an angle instead of flat from the side or top**; perspective is used to give a 3D effect; also known as "3/4 perspective", "2.5D", and "pseudo-3D"
> 

### Screenshots / References

- **"Steredenn"**: Roguelike space shooter with randomized challenges.
    - [https://www.youtube.com/watch?v=Pu9xEWhsfxg](https://www.youtube.com/watch?v=Pu9xEWhsfxg)
- **"Galaga"**: Classic gameplay with wave-based enemy attacks.
- ***Steambirds Alliance :***
    - [**https://youtu.be/wAa2Ay3eVUQ**](https://youtu.be/wAa2Ay3eVUQ)
    - [https://www.f2pg.com/steambirds-alliance/](https://www.f2pg.com/steambirds-alliance/)
- From Space : example of 45° isometric Camera
    - [https://www.youtube.com/watch?v=4Eib4mX4SkM](https://www.youtube.com/watch?v=4Eib4mX4SkM)
- Viewpoint
    - [https://youtu.be/yScJmYzP4p8?si=Q9r5qYZNf9dKPmfM](https://youtu.be/yScJmYzP4p8?si=Q9r5qYZNf9dKPmfM)
- R-Type 3 Evolved
    - [https://youtu.be/zlRoqZwGbzo?si=EYxB2rgKvCrcjUYQ](https://youtu.be/zlRoqZwGbzo?si=EYxB2rgKvCrcjUYQ)

## **Timeline**

### **Phase 1 :**

**Core Mechanics** (6 hours / Mercredi)

### **Phase 2 :**

**Optional Mechanics** (6 hours / Vendredi)

---

## **Controls Overview**

### **Keyboard + Mouse:**

- **WASD or Arrow Keys:** Move the spaceship.
- **Mouse:** Aim.
- **Left Mouse Button:** Fire missiles.
- **Right Mouse Button or Spacebar:** Activate/deactivate the laser.

### **Gamepad (Optional):**

- **Left Stick:** Move the spaceship.
- **Right Stick:** Aim.
- **Right Trigger (RT):** Fire missiles.
- **Left Trigger (LT):** Activate/deactivate the laser.

## **Evaluation Criteria**

1. **Core Systems (70%)**
    - Smooth controls and properly implemented shooting mechanics for both missile and laser.
    - Functioning enemy AI, spawning, and wave system.
    - Operational health, collision, and score-tracking systems.
2. **Optional Mechanics (30%)**
    - Creativity and functionality of the two chosen mechanics.
    - Extra credit for well-polished visual and audio effects.

## **Phase 1 : Core Systems**

You are required to build the foundational mechanics of the game, including two distinct shot types.

### **A / Core Features to Implement:**

- **Player Controls:**
    - **Movement:** Use the keyboard (WASD) or arrow keys to move the spaceship.
    - **Shooting:** Implement two types of weapons:
        1. **Missile:** A projectile that travels straight forward, dealing damage on impact.
        2. **Laser:** A continuous beam that deals sustained damage while active.
- **Camera:**
    - Fixed isometric perspective (configured using Unity's camera system).
- **Enemy Spawning:**
    - Create a system for spawning enemies at set intervals or in waves.
- **Collision System:**
    - Handle interactions between missiles, lasers, enemies, and the player using Unity's physics.

### **B / Unity Components:**

- **GameObjects & Prefabs:**
    - Player spaceship, enemy ships, missiles, lasers, and UI elements.
- **Physics:**
    - Rigidbody for movement and collision detection.
- **UI Elements:**
    - Score counter, health bar, and game-over screen.
- **Audio:**
    - Basic sound effects for shooting, explosions, and game events.

### **C / Scripting Requirements:**

- Movement scripts
    - player
    - enemies
    - projectiles
- mechanics scripts for **missile firing** and **laser activation**:
    - **Missiles:** Instantiate a prefab that travels in a straight direction.
    - **Laser:** Activate and deactivate a continuous beam using raycasting or a stretched sprite.
- Enemy AI for basic movement or targeting the player.
- Damage handling for health reduction and object destruction.
- A UI manager to track and display points, health and more …

![image.png](2%205D%20Isometric%20Space%20Shooter/image.png)

---

## **Phase 2: Optional Mechanics**

You must implement **at least two** of the following additional features:

### **1. Power-Ups**

- Temporary weapon upgrades (e.g., rapid-fire missiles, enhanced lasers).
- Health packs to restore player health.

### **2. Advanced Enemy Behavior**

- Introduce different enemy types (e.g., shielded, fast-moving, or kamikaze enemies).
- Create a boss enemy with unique attack patterns and higher health.

### **3. Environmental Hazards**

- Moving obstacles such as asteroids or laser barriers.
- Mines or traps that activate when approached.

### **4. Upgrade System**

- Allow players to improve their ship with upgrades (e.g., speed, damage, fire rate).

### **5. Improved GameFeel and Visual Effects**

- Add particle effects for explosions, thrusters, and weapon firing.
- Every elements that can improve gaming experience
- Implement a parallax scrolling background for depth.

### **6. Twin-Stick Controls**

- Enable movement with one joystick and aiming/shooting with another (mouse or gamepad).

---

### **Expected Deliverables**

A zipped folder in the folder of the NAS : **/GD_02/02_RENDUS/Sébastien Albert/TP Unity**

- Zip Folder named following these conventions : NomPrenom (Respecter les majuscules, pas d’accent ou caractères spéciaux)
- Content :
    - one file report.pdf file =  A brief report explaining the implemented features, challenges faced, and optional mechanics selected.
    - one folder named TPUnity = the Unity Project (Only Assets, Packages, ProjectSettings folders)