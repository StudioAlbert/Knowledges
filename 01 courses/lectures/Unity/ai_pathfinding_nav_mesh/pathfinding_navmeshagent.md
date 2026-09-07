---
title: "Pathfinding : NavMeshAgent"
type: section
parent: "[[ai_pathfinding_nav_mesh|AI Pathfinding (Nav mesh)]]"
---
# Pathfinding : NavMeshAgent

# Ressources

- Documentation Unity
    
    
    [https://youtu.be/vU6fCMC_IXA?feature=shared](https://youtu.be/vU6fCMC_IXA?feature=shared)
    
    [https://youtu.be/SMWxCpLvrcc?feature=shared](https://youtu.be/SMWxCpLvrcc?feature=shared)
    
    [AI Navigation | AI Navigation | 2.0.5](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/index.html)
    
    [New AI Navigation 2.0 video tutorials series](https://discussions.unity.com/t/new-ai-navigation-2-0-video-tutorials-series/1565073)
    

https://youtu.be/8eNk_5oRxbg?is=XVDxdWjKhm87DkrI

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
