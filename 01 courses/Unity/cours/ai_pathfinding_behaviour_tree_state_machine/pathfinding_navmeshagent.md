---
title: "Pathfinding : NavMeshAgent"
type: section
module: "🐰 - Medium"
section:
  - Game Sup 1A
  - SAE 1A
parent: "[[ai_pathfinding_behaviour_tree_state_machine|AI Pathfinding (Behaviour Tree, State machine)]]"
source: notion
---
# Pathfinding : NavMeshAgent

# Ressources

- Documentation Unity
    
    
    [https://youtu.be/vU6fCMC_IXA?feature=shared](https://youtu.be/vU6fCMC_IXA?feature=shared)
    
    [https://youtu.be/SMWxCpLvrcc?feature=shared](https://youtu.be/SMWxCpLvrcc?feature=shared)
    
    [AI Navigation | AI Navigation | 2.0.5](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/index.html)
    
    [New AI Navigation 2.0 video tutorials series](https://discussions.unity.com/t/new-ai-navigation-2-0-video-tutorials-series/1565073)
    

## Process

Bake Surface, add GameObject NavMeshsurface

ClickToMove script

```csharp
agent.destination = hitInfo.point;
```

Set animations

```csharp
void OnAnimatorMove(){
{
	agent.speed = (aniamtor.deltaposition / Time.deltaTime).magnitude;
}
```

View all NavMeshModifier

Multiple NavMeshSurfaces + HaveAcessScript
