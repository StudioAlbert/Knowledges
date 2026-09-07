---
title: 2D in Unity
type: course
status: Backlog
subject: Unity
duration_h: 12
bloc_gsda:
created: 2023-12-11T15:55
manual_order: 36
---
# 2D in Unity

[https://github.com/SAE-Geneve/924-UnityCourse-Platformer](https://github.com/SAE-Geneve/924-UnityCourse-Platformer)

[[2d_aventure_game|2D Aventure Game]]

# What is 2D in unity

Orthographic camera, Z aligned, no perspective

= the distance does not matter

= a cube is a square

Import settings

---

## Syllabus

### **Session 1: Introduction to Unity & 2D Tilemap System (3 hours)**

- **Theoretical Concepts:**
    - Introduction to Unity interface and 2D game development basics
    - Understanding Tilemaps, Tilesets, and Tile Palettes
    - Organizing assets and project structure
- **Practical Exercises:**
    - Creating and configuring a new 2D project
        - Setting up the Unity environment and project settings
        - Importing essential assets and organizing them in the project folder
    - Designing a simple level using Tilemaps and Tile Palettes
        - Creating a Tilemap grid and painting basic terrain
        - Customizing tiles for platforms, ground, and hazards

### **Session 2: Platformer Player Controller Basics (3 hours)**

- **Theoretical Concepts:**
    - Introduction to 2D physics in Unity (Rigidbody2D, Colliders, Physics Materials)
        - Explanation of Rigidbody2D properties (mass, gravity scale, drag)
        - Usage of BoxCollider2D and CircleCollider2D for collision detection
    - Handling player input (Input System vs. traditional Input)
        - Configuring Unity's new Input System
        - Mapping inputs for movement and actions
- **Practical Exercises:**
    - Implementing basic player movement: walking, jumping, and falling
        - Attaching Rigidbody2D and Collider components to the player character
        - Writing C# scripts to handle player input for horizontal movement and jump mechanics using Unity's new Input System.
- Applying physics materials for realistic interactions
    - Adjusting friction and bounciness for smoother gameplay
    - Testing and refining movement dynamics

### **Session 3: Enhancing Game Feel (1.5 hours)**

- **Theoretical Concepts:**
    - Importance of game feel: responsive controls, feedback mechanisms
        - Principles of "juice" in game design (visual, audio, and tactile feedback)
        - Enhancing player experience through subtle animations and effects
    - Advanced mechanics: double jump, wall slide, dash
        - State management for complex player movements
        - Transitioning smoothly between different movement states
- **Practical Exercises:**
    - Adding particle effects and sound for feedback
    - Implementing and tweaking advanced movement abilities
        - Scripting double jumps with conditions for activation
        - Coding wall sliding mechanics with friction adjustments
        - Designing a dash mechanic with cooldown management
    - Balancing gameplay mechanics for better user experience

### **Session 4: Specialized Tiles for Enhanced Gameplay (1.5 hours)**

- **Theoretical Concepts:**
    - Specialization of Tiles for Enhanced Gameplay
        - Introduction to interactive tiles (moving platforms, breakable tiles, bounce pads)
        - Designing environmental hazards and dynamic tile behaviors
- **Practical Exercises:**
    - Developing Specialized Tiles: moving platforms, breakable tiles, bounce pads

### **Session 5: Basic AI & Final Project (3 hours)**

- **Theoretical Concepts:**
    - Introduction to basic AI principles: state machines, simple pathfinding
        - Understanding finite state machines (FSM) for behavior control
        - Concepts of basic pathfinding algorithms
    - Designing enemy behaviors: patrol, chase, idle
        - Defining enemy states and transitions
        - Handling AI triggers using colliders and player detection
- **Practical Exercises:**
    - Implementing simple enemy AI with basic behavior patterns
        - Coding patrol routes with waypoints
        - Adding chase behavior when the player enters detection range
        - Transitioning between idle, patrol, and chase states
    - Integrating AI into the game environment
        - Placing enemies strategically within levels
        - Testing AI interactions with the player and environment
    - Final project: Students design and develop a small platformer level combining all learned concepts
        - Level design emphasizing gameplay mechanics and AI challenges
        - Polishing the final project with visual and audio enhancements

---

## **Resources:**

- Unity documentation and tutorials
- Example assets for practice

### Sample code snippets for reference

```csharp
using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerController : MonoBehaviour
{
    private Rigidbody2D rb;
    private Vector2 moveInput;
    public float moveSpeed = 5f;
    public float jumpForce = 10f;
    private bool isGrounded;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    public void OnMove(InputAction.CallbackContext context)
    {
        moveInput = context.ReadValue<Vector2>();
    }

    public void OnJump(InputAction.CallbackContext context)
    {
        if (context.performed && isGrounded)
        {
            rb.AddForce(Vector2.up * jumpForce, ForceMode2D.Impulse);
        }
    }

    void Update()
    {
        rb.velocity = new Vector2(moveInput.x * moveSpeed, rb.velocity.y);
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.contacts[0].normal.y > 0.5)
        {
            isGrounded = true;
        }
    }

    private void OnCollisionExit2D(Collision2D collision)
    {
        isGrounded = false;
    }
}

```

## Sprite sheet

A sprite sheet is a single image file that contains multiple smaller images (sprites) arranged in a grid pattern. In Unity, these are commonly used for 2D game development to store:

- Character animations frames
- Multiple states of game objects
- Collections of related UI elements

The main advantages of using sprite sheets are:

- Improved performance through better memory management
- Reduced number of file loads
- Easier organization of related sprites

In Unity, you can slice sprite sheets into individual sprites using the Sprite Editor, making it easy to use specific frames or elements in your game.

![[2d_in_unity_01.png]]

![[2d_in_unity_02.png]]

![[2d_in_unity_03.png]]

main types of sprite slicing in Unity:

- **Automatic** - Unity automatically attempts to detect and slice sprites based on the image content
- **Grid by cell size :** Slices the sprite sheet into equal-sized cells
- **Grid by cell size :** Slices based on specified numbers of rows and columns
- **Isometric Grid**

![[2d_in_unity_04.png]]

### Processus d’utilisation des outils Unity

![[2d_in_unity_05.png]]
