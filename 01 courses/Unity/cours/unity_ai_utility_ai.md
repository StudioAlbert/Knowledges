---
title: Unity AI - Utility AI
type: course
section:
  - Game Sup 2A
  - SAE 1A
created: 2026-03-17T16:09
source: notion
---
# Unity AI - Utility AI

# Principes

## Qu'est-ce que l'Utility AI ?

L'Utility AI est un système de prise de décision pour les NPC (Non-Player Characters) où **chaque action possible reçoit un score numérique** représentant son "utilité" dans la situation actuelle. Le NPC exécute simplement l'action avec le score le plus élevé.

## Le cycle fondamental

Le système suit un cycle en 4 étapes à chaque tick de décision :

[https://link.excalidraw.com/readonly/4qPqy0ilXyA7UBSeALNU?darkMode=true](https://link.excalidraw.com/readonly/4qPqy0ilXyA7UBSeALNU?darkMode=true)

**Observer** → Le NPC collecte les données du monde (vie, distance ennemi, faim, alliés…) et les normalise entre 0 et 1 dans un objet `AIContext`.

**Évaluer** → Chaque action possible calcule son score d'utilité en passant les données du contexte dans ses courbes de réponse, puis en multipliant les résultats.

**Choisir** → L'action avec le score le plus élevé est sélectionnée. Un léger bonus de momentum est appliqué à l'action en cours pour éviter le flip-flop.

**Agir** → Le NPC exécute l'action choisie. Au prochain tick, le cycle recommence depuis l'observation.

## Exemple concret : le garde

Imaginons un NPC garde avec 5 actions possibles. Voici les **inputs** qu'il observe :

| Input | Description | Plage |
| --- | --- | --- |
| Vie (HP) | Points de vie restants | 0% → 100% |
| Distance ennemi | Distance au plus proche ennemi | 1m → 100m |
| Faim | Niveau de faim accumulé | 0% → 100% |
| Force ennemi | Estimation de la puissance de l'ennemi | 0% → 100% |
| Alliés proches | Nombre d'alliés à proximité | 0 → 5 |

Et voici comment chaque action utilise ces inputs :

| Action | Inputs utilisés | Logique |
| --- | --- | --- |
| **Attaquer** | Vie, distance, force ennemi, alliés | Score élevé quand en bonne santé, ennemi proche et faible |
| **Fuir** | Vie, distance, force ennemi | Score élevé quand vie basse et ennemi proche et fort |
| **Se soigner** | Vie | Score élevé quand vie très basse |
| **Manger** | Faim | Score élevé quand faim critique |
| **Appeler renforts** | Vie, force ennemi, alliés | Score élevé quand ennemi fort et peu d'alliés |

## La normalisation : tout ramener entre 0 et 1

Avant de pouvoir comparer les scores entre eux, **chaque input doit être normalisé** entre 0 et 1. La décision ne peut se faire qu’à partir de données comparable.

> 💡 **Point clé** : L'inversion (`1 - x`) est très courante. "Pourcentage de vie restant" et "niveau de danger" sont la même donnée, mais inversée. Le choix de la direction dépend de ce que la considération mesure.
> 

## La multiplication des considérations

Chaque action a plusieurs **considérations** (= facteurs). Leurs scores sont **multipliés** entre eux pour obtenir le score final de l'action.

**Pourquoi multiplier plutôt qu'additionner ?**

- Si **un seul** facteur vaut 0, tout le score tombe à 0. Un NPC à pleine vie ne fuira **jamais**, même si l'ennemi est terrifiant.
- La multiplication crée une logique ET implicite : toutes les conditions doivent être au moins partiellement remplies.
- Exemple en C#
    
    ```csharp
    // Score de l'action "Fuir"
    public float ScoreFlee(float hpNormalized, float distNormalized, float enemyStrength)
    {
        float danger = 1f - hpNormalized;                    // Vie basse = danger élevé
        float threatClose = 1f - distNormalized;             // Ennemi proche = menace
        float enemyStrong = enemyStrength;                   // Force brute de l'ennemi
    
        // Multiplication : toutes les conditions doivent être présentes
        return danger * threatClose * enemyStrong;
    }
    
    // Scénario 1 : HP=20%, ennemi à 10m, force 90%
    // → 0.80 * 0.90 * 0.90 = 0.648 (score élevé → fuite probable)
    
    // Scénario 2 : HP=90%, ennemi à 10m, force 90%
    // → 0.10 * 0.90 * 0.90 = 0.081 (score faible → pas de fuite)
    
    // Scénario 3 : HP=20%, ennemi à 80m, force 90%
    // → 0.80 * 0.20 * 0.90 = 0.144 (trop loin pour paniquer)
    ```
    

> ⚠️ **Piège de la multiplication** : avec beaucoup de facteurs, les scores tendent vers 0 (chaque multiplication réduit le résultat). Solutions : utiliser la **moyenne géométrique**, ou limiter le nombre de considérations par action à 3-4.
> 

---

# Courbes de compensation

Les courbes de réponse sont le **cœur** du système Utility AI. Elles transforment un input normalisé (0→1) en un score d'utilité (0→1) en lui donnant une **forme** qui reflète le comportement souhaité.

Sans courbes, la relation entre input et output est linéaire — ce qui est rarement réaliste. Un humain ne panique pas progressivement en perdant de la vie : il reste calme longtemps, puis bascule soudainement quand ça devient critique.

## Types de courbes

[https://studio-albert-widgets.netlify.app/utility-ai-curves-widget.html](https://studio-albert-widgets.netlify.app/utility-ai-curves-widget.html)

## Implémentation via AnimationCurve dans Unity

Unity offre un outil natif parfait pour les courbes de réponse : **AnimationCurve**. Il permet aux game designers de dessiner visuellement la courbe dans l'Inspector, sans toucher au code.

- Exemple de Code C# : Usage d’une Animation Curve
    
    ```csharp
    using UnityEngine;
    
    [CreateAssetMenu(fileName = "NewConsideration", menuName = "AI/Consideration")]
    public class Consideration : ScriptableObject
    {
        [Header("Input")]
        public string inputName;             // Ex: "Health", "EnemyDistance"
    
        [Header("Courbe de réponse")]
        public AnimationCurve responseCurve = AnimationCurve.Linear(0f, 0f, 1f, 1f);
    
        /// <summary>
        /// Évalue la considération : prend un input normalisé (0-1),
        /// le passe dans la courbe, retourne un score (0-1).
        /// </summary>
        public float Evaluate(float normalizedInput)
        {
            return Mathf.Clamp01(responseCurve.Evaluate(normalizedInput));
        }
    }
    ```
    
- Exemple de Code C# : Configurer les courbes prédéfinies dans l'Inspector
    
    ```csharp
    // Créer les courbes par défaut en code pour les affecter ensuite dans l'Inspector
    
    // Linéaire : AnimationCurve.Linear(0, 0, 1, 1)
    // Quadratique douce : 
    AnimationCurve quadratic = new AnimationCurve(
        new Keyframe(0f, 0f, 0f, 0f),
        new Keyframe(1f, 1f, 2f, 0f)  // tangente entrante = 2 pour accélération
    );
    
    // Sigmoïde approximée :
    AnimationCurve sigmoid = new AnimationCurve(
        new Keyframe(0f, 0f, 0f, 0f),
        new Keyframe(0.5f, 0.5f, 2f, 2f),  // point d'inflexion raide
        new Keyframe(1f, 1f, 0f, 0f)
    );
    
    // Exponentielle inverse (saturation rapide) :
    AnimationCurve expInverse = new AnimationCurve(
        new Keyframe(0f, 0f, 3f, 3f),      // montée rapide au départ
        new Keyframe(0.5f, 0.9f, 0.3f, 0.3f),
        new Keyframe(1f, 1f, 0f, 0f)       // plateau
    );
    ```
    

> 💡 **Astuce** : Créez une bibliothèque de ScriptableObjects de type `Consideration` avec des courbes prédéfinies (Linear, Quadratic, Sigmoid, etc.). Les designers n'ont qu'à les glisser-déposer et les ajuster.
> 

## Application de variantes : téméraire vs pleutre

### Comparaison des comportements

| Points de vie | Score fuite (Pleutre) | Score fuite (Téméraire) | Résultat |
| --- | --- | --- | --- |
| 80% | ~0.40 | ~0.02 | Le pleutre hésite déjà, le téméraire est serein |
| 50% | ~0.85 | ~0.08 | Le pleutre fuit, le téméraire continue à se battre |
| 25% | ~0.98 | ~0.45 | Les deux pensent à fuir, mais le téméraire hésite encore |
| 10% | ~1.00 | ~0.85 | Les deux fuient — le téméraire cède enfin |

> 💡 **Point clé** : La "personnalité" d'un NPC est entièrement définie par la **forme de ses courbes**, pas par du code spécifique. Un designer peut créer des dizaines de profils comportementaux juste en ajustant des courbes dans l'Inspector.
> 

---

# Architecture

> 🔗 **Implémentation de référence** : [github.com/adammyhre/Unity-Utility-AI](http://github.com/adammyhre/Unity-Utility-AI) — Le code ci-dessous est inspiré de ce dépôt.
> 

L'architecture repose sur 5 composants clés, tous basés sur le pattern **ScriptableObject** de Unity pour un workflow data-driven.

## Vue d'ensemble

```
NPCController (MonoBehaviour)
│
├── AIBrain              → Décideur : évalue et choisit la meilleure action
│   ├── Action[]          → ScriptableObjects : comportements possibles
│   │   ├── Consideration[]   → ScriptableObjects : facteurs de scoring
│   │   │   └── AnimationCurve    → Courbe de réponse (Response Curve)
│   │   └── Execute()         → Code spécifique de l'action
│   └── DecideBestAction() → Sélection du score le plus élevé
│
└── MoveController    → Navigation / déplacement du NPC
```

## NPCController

Le **NPCController** est le composant MonoBehaviour attaché au GameObject du NPC. Il expose les stats du NPC (vie, faim, énergie, argent…) et référence l'AIBrain et le MoveController.

- Exemple de code C# : NPCController
    
    ```csharp
    public class NPCController : MonoBehaviour
    {
        public AIBrain aiBrain;
        public MoveController moveController;
        public NPCStats stats; // Vie, faim, énergie, argent...
    
        void Start()
        {
            aiBrain.Initialize(this);
        }
    
        void Update()
        {
            aiBrain.Think();
        }
    }
    
    [System.Serializable]
    public class NPCStats
    {
        public float health = 100f;
        public float maxHealth = 100f;
        public float hunger;
        public float energy = 100f;
        public float money;
    }
    ```
    

## AIBrain

L'**AIBrain** est le cerveau décisionnel. Il possède une liste d'Actions, les évalue toutes, et sélectionne la meilleure via `DecideBestAction`. Il contient aussi `ScoreAction` qui calcule le score d'une action en multipliant les scores de ses Considerations.

- Implémentation C# : AIBrain
    
    ```csharp
    public class AIBrain : MonoBehaviour
    {
        public Action[] actions;          // Liste des actions possibles
        Action bestAction;
        NPCController npc;
    
        public void Initialize(NPCController controller)
        {
            npc = controller;
        }
    
        public void Think()
        {
            bestAction = DecideBestAction();
            bestAction?.Execute(npc);
        }
    
        Action DecideBestAction()
        {
            float bestScore = float.MinValue;
            Action best = null;
    
            foreach (var action in actions)
            {
                float score = ScoreAction(action);
                if (score > bestScore)
                {
                    bestScore = score;
                    best = action;
                }
            }
            return best;
        }
    
        float ScoreAction(Action action)
        {
            float score = 1f;
            foreach (var consideration in action.considerations)
            {
                float s = consideration.ScoreConsideration(npc);
                score *= s;
                if (score == 0) return 0; // Court-circuit
            }
            // Compensation factor (Dave Mark)
            float originalScore = score;
            float modFactor = 1f - (1f / action.considerations.Length);
            float makeUpValue = (1f - originalScore) * modFactor;
            return originalScore + (makeUpValue * originalScore);
        }
    }
    ```
    

> 💡 Le **Compensation Factor** (formule de Dave Mark) remplace la simple moyenne géométrique. Il atténue le problème de l'effondrement des scores quand on multiplie beaucoup de considérations, sans perdre l'effet "un zéro annule tout".
> 

## Action (ScriptableObject)

Chaque **Action** est un ScriptableObject abstrait avec une liste de Considerations et une méthode `Execute` à implémenter.

```csharp
public abstract class AIAction : ScriptableObject {
    public string targetTag;
    public Consideration consideration;

    public virtual void Initialize(Context context) {
        // Optional initialization logic
    }
    
    public float CalculateUtility(Context context) => consideration.Evaluate(context);
    
    public abstract void Execute(Context context);
}
```

- Exemples d'actions concrètes
    
    ```csharp
    [CreateAssetMenu(menuName = "UtilityAI/Actions/IdleAction")]
    public class IdleAIAction : AIAction {
        public override void Execute(Context context) {
            context.agent.SetDestination(context.agent.transform.position);
        }
    }
    
    [CreateAssetMenu(menuName = "UtilityAI/Actions/MoveToTargetAction")]
    public class MoveToTargetAIAction : AIAction {
        public override void Initialize(Context context) {
            context.sensor.targetTags.Add(targetTag);
        }
    
        public override void Execute(Context context) {
            var target = context.sensor.GetClosestTarget(targetTag);
            if (target == null) return;
    
            context.target = target;
            
            context.agent.SetDestination(target.position);
        }
    }
    ```
    

## Consideration (ScriptableObject)

Chaque **Consideration** lit une stat du NPC, la normalise (0→1), la passe dans une **AnimationCurve**, et retourne un score.

```csharp
public abstract class Consideration : ScriptableObject {
    public abstract float Evaluate(Context context);
}

[CreateAssetMenu(menuName = "UtilityAI/Considerations/Constant")]
public class ConstantConsideration : Consideration {
    public float value;
    
    public override float Evaluate(Context context) => value;
}
[CreateAssetMenu(menuName = "UtilityAI/Considerations/CurveConsideration")]
public class CurveConsideration : Consideration {
    public AnimationCurve curve;
    public string contextKey;

    public override float Evaluate(Context context) {
        float inputValue = context.GetData<float>(contextKey);
        
        float utility = curve.Evaluate(inputValue);
        return Mathf.Clamp01(utility);
    }

    void Reset() {
        curve = new AnimationCurve(
            new Keyframe(0f, 1f), // At normalized distance 0, utility is 1
            new Keyframe(1f, 0f)  // At normalized distance 1, utility is 0
        );
    }
	}
```

## Composite Consideration

Une **Composite Consideration** combine plusieurs considérations simples en une seule évaluation. Utile pour les décisions complexes du type "est-ce que je peux me permettre de combattre ?" qui dépend à la fois de la vie ET de la force de l'ennemi.

- Implementation C#
    
    ```csharp
    [CreateAssetMenu(menuName = "UtilityAI/Considerations/CompositeConsideration")]
    public class CompositeConsideration : Consideration {
        public enum OperationType { Average, Multiply, Add, Subtract, Divide, Max, Min }
        
        public bool allMustBeNonZero = true;
        
        public OperationType operation = OperationType.Max;
        public List<Consideration> considerations;
    
        public override float Evaluate(Context context) {
            if (considerations == null || considerations.Count == 0) return 0f;
            
            float result = considerations[0].Evaluate(context);
            if (result == 0f && allMustBeNonZero) return 0f;
    
            // Suggestion: Only 2 Considerations per Composite
            for (int i = 1; i < considerations.Count; i++) {
                float value = considerations[i].Evaluate(context);
                
                if (value == 0f && allMustBeNonZero) return 0f;
    
                switch (operation) {
                    case OperationType.Average:
                        result = (result + value) / 2;
                        break;
                    case OperationType.Multiply:
                        result *= value;
                        break;
                    case OperationType.Add:
                        result += value;
                        break;
                    case OperationType.Subtract:
                        result -= value;
                        break;
                    case OperationType.Divide:
                        result = value != 0 ? result / value : result; // Prevent division by zero
                        break;
                    case OperationType.Max:
                        result = Mathf.Max(result, value);
                        break;
                    case OperationType.Min:
                        result = Mathf.Min(result, value);
                        break;
                }
            }
            
            return Mathf.Clamp01(result);
        }
    }
    ```
    

## Workflow designer

Grâce au pattern ScriptableObject, le workflow de création d'un NPC est entièrement data-driven :

1. **Créer des Considerations** (clic droit → Create → UtilityAI → Considerations) et dessiner la courbe de réponse dans l'Inspector
2. **Créer des Actions** (Create → UtilityAI → Actions) et y glisser-déposer les Considerations pertinentes
3. **Assigner les Actions** dans le composant AIBrain sur le GameObject du NPC
4. **Tester et itérer** : modifier les courbes en temps réel pendant le Play Mode

> 💡 **Tout est ScriptableObject** : Un designer peut assembler le comportement d'un nouveau NPC par glisser-déposer dans l'Inspector, sans écrire une seule ligne de code. Les mêmes Considerations et Actions peuvent être réutilisées entre différents types de NPC.
> 

---

## Références

- **Dave Mark & Kevin Dill** — "Improving AI Decision Modeling Through Utility Theory" (GDC 2010) — [GDC Vault](https://www.gdcvault.com/play/1012410/Improving-AI-Decision-Modeling-Through)
- **Dave Mark** — *Behavioral Mathematics for Game AI* (2009, Charles River Media)
- **Dave Mark & Mike Lewis** — "Building a Better Centaur: AI at Massive Scale" (GDC 2015) — [GDC Vault](https://www.gdcvault.com/play/1021848/Building-a-Better-Centaur-AI)
- **Infinite Axis Utility System (IAUS)** — [gameai.com/iaus](http://gameai.com/iaus)
- **Game AI Pro** — Chapitres sur l'Utility AI par Kevin Dill et Mike Lewis — [gameaipro.com](http://gameaipro.com)
- **Wikipedia** — [Utility system](https://en.wikipedia.org/wiki/Utility_system)
