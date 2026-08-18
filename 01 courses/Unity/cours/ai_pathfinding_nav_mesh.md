---
title: AI Pathfinding (Nav mesh)
type: course
duration_h: 6
bloc: "[[Intelligence Artificielle]]"
created: 2023-05-17T14:01
---
# AI Pathfinding (Nav mesh)

[[01 courses/Unity/cours/ai_pathfinding_nav_mesh/autonomous_behaviours|Autonomous behaviours]]

[[01 courses/Unity/cours/ai_pathfinding_nav_mesh/pathfinding_navmeshagent|Pathfinding : NavMeshAgent]]

# Ressources

- Documentation Unity
    
    
    [https://youtu.be/vU6fCMC_IXA?feature=shared](https://youtu.be/vU6fCMC_IXA?feature=shared)
    
    [https://youtu.be/SMWxCpLvrcc?feature=shared](https://youtu.be/SMWxCpLvrcc?feature=shared)
    
    [AI Navigation | AI Navigation | 2.0.5](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/index.html)
    
    [New AI Navigation 2.0 video tutorials series](https://discussions.unity.com/t/new-ai-navigation-2-0-video-tutorials-series/1565073)
    

## Process

Define a Surface

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
