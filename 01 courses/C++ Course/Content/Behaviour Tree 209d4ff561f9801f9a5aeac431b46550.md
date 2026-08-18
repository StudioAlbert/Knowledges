# Behaviour Tree

### Code

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <string>

// ============================================================================
// BEHAVIOR TREE IMPLEMENTATION
// ============================================================================

// Statuts de retour des nœuds
enum class NodeStatus {
    SUCCESS,
    FAILURE,
    RUNNING
};

// Classe de base abstraite pour tous les nœuds
class BehaviorNode {
public:
    virtual ~BehaviorNode() = default;
    virtual NodeStatus tick() = 0;
    virtual void reset() {}
    
protected:
    NodeStatus status = NodeStatus::FAILURE;
};

// ============================================================================
// NŒUDS DE CONTRÔLE
// ============================================================================

// Nœud Composite (base pour les nœuds avec enfants)
class CompositeNode : public BehaviorNode {
protected:
    std::vector<std::unique_ptr<BehaviorNode>> children;
    size_t currentChild = 0;

public:
    void addChild(std::unique_ptr<BehaviorNode> child) {
        children.push_back(std::move(child));
    }
    
    void reset() override {
        currentChild = 0;
        for (auto& child : children) {
            child->reset();
        }
    }
};

// Sequence : Réussit si tous les enfants réussissent (ET logique)
class SequenceNode : public CompositeNode {
public:
    NodeStatus tick() override {
        while (currentChild < children.size()) {
            NodeStatus childStatus = children[currentChild]->tick();
            
            if (childStatus == NodeStatus::FAILURE) {
                reset();
                return NodeStatus::FAILURE;
            }
            
            if (childStatus == NodeStatus::RUNNING) {
                return NodeStatus::RUNNING;
            }
            
            // SUCCESS : passer au prochain enfant
            currentChild++;
        }
        
        // Tous les enfants ont réussi
        reset();
        return NodeStatus::SUCCESS;
    }
};

// Selector : Réussit si au moins un enfant réussit (OU logique)
class SelectorNode : public CompositeNode {
public:
    NodeStatus tick() override {
        while (currentChild < children.size()) {
            NodeStatus childStatus = children[currentChild]->tick();
            
            if (childStatus == NodeStatus::SUCCESS) {
                reset();
                return NodeStatus::SUCCESS;
            }
            
            if (childStatus == NodeStatus::RUNNING) {
                return NodeStatus::RUNNING;
            }
            
            // FAILURE : essayer le prochain enfant
            currentChild++;
        }
        
        // Tous les enfants ont échoué
        reset();
        return NodeStatus::FAILURE;
    }
};

// Parallel : Exécute tous les enfants simultanément
class ParallelNode : public CompositeNode {
private:
    int successThreshold;
    int failureThreshold;

public:
    ParallelNode(int successThreshold = 1, int failureThreshold = 1) 
        : successThreshold(successThreshold), failureThreshold(failureThreshold) {}
    
    NodeStatus tick() override {
        int successCount = 0;
        int failureCount = 0;
        int runningCount = 0;
        
        for (auto& child : children) {
            NodeStatus childStatus = child->tick();
            
            switch (childStatus) {
                case NodeStatus::SUCCESS: successCount++; break;
                case NodeStatus::FAILURE: failureCount++; break;
                case NodeStatus::RUNNING: runningCount++; break;
            }
        }
        
        if (successCount >= successThreshold) {
            return NodeStatus::SUCCESS;
        }
        
        if (failureCount >= failureThreshold) {
            return NodeStatus::FAILURE;
        }
        
        return NodeStatus::RUNNING;
    }
};

// ============================================================================
// NŒUDS DÉCORATEURS
// ============================================================================

class DecoratorNode : public BehaviorNode {
protected:
    std::unique_ptr<BehaviorNode> child;

public:
    void setChild(std::unique_ptr<BehaviorNode> childNode) {
        child = std::move(childNode);
    }
    
    void reset() override {
        if (child) child->reset();
    }
};

// Inverter : Inverse le résultat de l'enfant
class InverterNode : public DecoratorNode {
public:
    NodeStatus tick() override {
        if (!child) return NodeStatus::FAILURE;
        
        NodeStatus childStatus = child->tick();
        
        switch (childStatus) {
            case NodeStatus::SUCCESS: return NodeStatus::FAILURE;
            case NodeStatus::FAILURE: return NodeStatus::SUCCESS;
            case NodeStatus::RUNNING: return NodeStatus::RUNNING;
        }
        
        return NodeStatus::FAILURE;
    }
};

// Repeater : Répète l'enfant N fois ou indéfiniment
class RepeaterNode : public DecoratorNode {
private:
    int maxRepeats;
    int currentRepeats = 0;

public:
    RepeaterNode(int maxRepeats = -1) : maxRepeats(maxRepeats) {}
    
    NodeStatus tick() override {
        if (!child) return NodeStatus::FAILURE;
        
        while (maxRepeats == -1 || currentRepeats < maxRepeats) {
            NodeStatus childStatus = child->tick();
            
            if (childStatus == NodeStatus::RUNNING) {
                return NodeStatus::RUNNING;
            }
            
            currentRepeats++;
            child->reset();
            
            if (maxRepeats != -1 && currentRepeats >= maxRepeats) {
                break;
            }
        }
        
        currentRepeats = 0;
        return NodeStatus::SUCCESS;
    }
};

// ============================================================================
// NŒUDS FEUILLES (ACTIONS ET CONDITIONS)
// ============================================================================

// Action de base (fonction lambda ou callable)
template<typename Callable>
class ActionNode : public BehaviorNode {
private:
    Callable action;

public:
    ActionNode(Callable action) : action(action) {}
    
    NodeStatus tick() override {
        return action();
    }
};

// Condition de base
template<typename Callable>
class ConditionNode : public BehaviorNode {
private:
    Callable condition;

public:
    ConditionNode(Callable condition) : condition(condition) {}
    
    NodeStatus tick() override {
        return condition() ? NodeStatus::SUCCESS : NodeStatus::FAILURE;
    }
};

// ============================================================================
// HELPER FUNCTIONS POUR CRÉER LES NŒUDS
// ============================================================================

template<typename Callable>
auto makeAction(Callable action) {
    return std::make_unique<ActionNode<Callable>>(action);
}

template<typename Callable>
auto makeCondition(Callable condition) {
    return std::make_unique<ConditionNode<Callable>>(condition);
}

auto makeSequence() {
    return std::make_unique<SequenceNode>();
}

auto makeSelector() {
    return std::make_unique<SelectorNode>();
}

auto makeParallel(int successThreshold = 1, int failureThreshold = 1) {
    return std::make_unique<ParallelNode>(successThreshold, failureThreshold);
}

auto makeInverter() {
    return std::make_unique<InverterNode>();
}

auto makeRepeater(int maxRepeats = -1) {
    return std::make_unique<RepeaterNode>(maxRepeats);
}

// ============================================================================
// EXEMPLE D'UTILISATION
// ============================================================================

class NPCActor {
public:
    bool hasEnemy = false;
    bool isEnemyClose = false;
    bool hasAmmo = true;
    bool isHealthLow = false;
    
    NodeStatus moveToEnemy() {
        std::cout << "Moving to enemy..." << std::endl;
        return NodeStatus::SUCCESS;
    }
    
    NodeStatus attack() {
        std::cout << "Attacking!" << std::endl;
        hasAmmo = false; // Simule l'épuisement des munitions
        return NodeStatus::SUCCESS;
    }
    
    NodeStatus flee() {
        std::cout << "Fleeing!" << std::endl;
        return NodeStatus::SUCCESS;
    }
    
    NodeStatus patrol() {
        std::cout << "Patrolling..." << std::endl;
        return NodeStatus::SUCCESS;
    }
    
    NodeStatus reload() {
        std::cout << "Reloading..." << std::endl;
        hasAmmo = true;
        return NodeStatus::SUCCESS;
    }
};

// Fonction pour construire l'arbre de comportement
std::unique_ptr<BehaviorNode> buildNPCBehaviorTree(NPCActor& npc) {
    // Construction de l'arbre principal
    auto root = makeSelector();
    
    // Branche 1: Combat (si ennemi détecté)
    auto combatSequence = makeSequence();
    combatSequence->addChild(makeCondition([&npc]() { return npc.hasEnemy; }));
    
    auto combatSelector = makeSelector();
    
    // Sous-branche: Fuir si santé faible
    auto fleeSequence = makeSequence();
    fleeSequence->addChild(makeCondition([&npc]() { return npc.isHealthLow; }));
    fleeSequence->addChild(makeAction([&npc]() { return npc.flee(); }));
    combatSelector->addChild(std::move(fleeSequence));
    
    // Sous-branche: Attaquer si possible
    auto attackSequence = makeSequence();
    attackSequence->addChild(makeCondition([&npc]() { return npc.hasAmmo; }));
    attackSequence->addChild(makeAction([&npc]() { return npc.moveToEnemy(); }));
    attackSequence->addChild(makeAction([&npc]() { return npc.attack(); }));
    combatSelector->addChild(std::move(attackSequence));
    
    // Sous-branche: Recharger si pas de munitions
    combatSelector->addChild(makeAction([&npc]() { return npc.reload(); }));
    
    combatSequence->addChild(std::move(combatSelector));
    root->addChild(std::move(combatSequence));
    
    // Branche 2: Patrouille par défaut
    root->addChild(makeAction([&npc]() { return npc.patrol(); }));
    
    return std::move(root);
}

// ============================================================================
// MAIN - DÉMONSTRATION
// ============================================================================

int main() {
    NPCActor npc;
    auto behaviorTree = buildNPCBehaviorTree(npc);
    
    std::cout << "=== Behavior Tree Demo ===" << std::endl;
    
    // Scénario 1: Patrouille normale
    std::cout << "\n1. Normal patrol:" << std::endl;
    behaviorTree->tick();
    
    // Scénario 2: Ennemi détecté, combat
    std::cout << "\n2. Enemy detected, combat:" << std::endl;
    npc.hasEnemy = true;
    behaviorTree->tick();
    
    // Scénario 3: Plus de munitions, rechargement
    std::cout << "\n3. Out of ammo, reloading:" << std::endl;
    behaviorTree->tick();
    
    // Scénario 4: Santé faible, fuite
    std::cout << "\n4. Low health, fleeing:" << std::endl;
    npc.isHealthLow = true;
    behaviorTree->tick();
    
    return 0;
}
```

### Exemple de comportement

[https://link.excalidraw.com/readonly/vaBJwQM4p9gBsyU5Fupa](https://link.excalidraw.com/readonly/vaBJwQM4p9gBsyU5Fupa)