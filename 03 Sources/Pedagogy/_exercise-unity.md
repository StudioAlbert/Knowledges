# C#/Unity exercise packages

If the user has their own coding standards (e.g. a team or studio standards page, or another
installed review skill), those take priority over the defaults below.

## Naming defaults (Microsoft C# conventions + common Unity practice)

| Element | Convention | Example |
|---|---|---|
| Classes, structs, enums, methods, properties, events | PascalCase | `EnemyBrain`, `TakeDamage()` |
| Interfaces | `I` + PascalCase | `IDamageable` |
| Private fields | `_camelCase` | `_currentState` |
| Serialized private fields | `[SerializeField] private` + `_camelCase` | `[SerializeField] private float _speed;` |
| Locals, parameters | camelCase | `targetPosition` |
| Constants | PascalCase | `MaxAgents` |
| Namespaces | PascalCase, match folders | `SaeGames.Ai` |
| Files | match the type name | `EnemyBrain.cs` |

Avoid public fields for inspector exposure; prefer `[SerializeField] private`.

## Project layout

```
Assets/
├── _Exercise/
│   ├── Scripts/            # Exercise.Runtime.asmdef
│   ├── Scenes/
│   └── Prefabs/
└── Tests/
    ├── EditMode/           # Exercise.Tests.EditMode.asmdef (references Runtime + test runner)
    └── PlayMode/           # only when behaviour needs frames, physics or coroutines
```

Assembly definitions are required for the Unity Test Framework to see the runtime code.

## Tests (Unity Test Framework / NUnit)

- Prefer EditMode tests on plain C# logic: they are fast and CI-friendly. Design the exercise so
  core logic (FSM, pathfinding, generation) lives in testable classes, not only in `MonoBehaviour`s.
  This is also a good pedagogical point to make explicit in the brief.
- PlayMode tests with `[UnityTest]` + `yield return null` for frame-dependent behaviour.
- Test names: `MethodName_Condition_ExpectedResult`.

## CI

Unity CI (e.g. GameCI's `unity-test-runner` action) needs a Unity license stored as repository
secrets. Mention this requirement in instructor notes; if the user doesn't have CI for Unity, deliver
the tests for local runs via the Test Runner window and skip the workflow.
