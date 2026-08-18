---
title: Singletons in Unity
type: course
duration_h: 6
bloc: "[[Architecture et Design Patterns]]"
created: 2025-12-18T06:38
---
# Singletons in Unity

### Exemples

## Contenu

### A télécharger

[github.example.git](github.example.git)

### Principes

# Restricting a class to one instance

# Providing a global point of access

```csharp
public class ScoreKeeper
{
    private static ScoreKeeper _instance;
    public static ScoreKeeper Instance => _instance ??= new ScoreKeeper();

    private ScoreKeeper() { }

    public int Score;
}
```

```csharp
    public class ScoreKeeperAsComponent : MonoBehaviour
    {
        public static ScoreKeeperAsComponent Instance { get; private set; }
        
        public int Score { get; private set; }

        private void Awake()
        {
            if (Instance == null)
            {
                Instance = this;
            }
            else
            {
                Destroy(this);
            }
        }

        public void AddScore(int score)
        {
            Score += score;
        }

    }
```

### Generic singleton

```csharp
public class GenericSingleton<T> : MonoBehaviour where T : Component
    {
        protected static T instance;

        public static bool HasInstance => instance != null;
        public static T TryGetInstance => HasInstance ? instance : null;

        public static T Instance
        {
            get
            {
                if (instance == null)
                {
                    instance = FindAnyObjectByType<T>();
                    if (instance == null)
                    {
                        var go = new GameObject("new singleton generated");
                        instance = go.AddComponent<T>();
                    }
                }

                return instance;
                
            }
        }

        protected void Awake()
        {
            Initialize();
        }

        private void Initialize()
        {
            if(!Application.isPlaying) return;

            instance = this as T;
        } 

    }
```

### Persistent and regulated singletons

![[singletons_in_unity_01.png]]

![[singletons_in_unity_02.png]]

![[singletons_in_unity_03.png]]

---

## Références

[Singleton · Design Patterns Revisited · Game Programming Patterns](https://gameprogrammingpatterns.com/singleton.html)

[Better Singletons in Unity C#](https://youtu.be/LFOXge7Ak3E?si=Rvk6LubEnV7LpOBg)

---

## Exercices

### Exercice 1

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
