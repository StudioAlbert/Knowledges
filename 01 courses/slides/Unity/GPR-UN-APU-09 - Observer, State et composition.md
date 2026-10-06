---
title: GPR-UN-APU-09 - State, un pattern de gameplay
type: slides
status: Backlog
subject: Unity
duration_h: 1
bloc_gsda: Architecture et Patterns Unity
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: draft
---

# State, un pattern de gameplay
<!-- .slide: class="title" -->

### Un comportement par état, des transitions nommées

<small>GPR-UN-APU-09 · Architecture et Patterns Unity</small>

Note:
Séance recentrée le 28.09 sur le seul pattern State (Observer passe en APU-05,
la composition est abandonnée pour cette année). Fil conducteur : la machine à
états n'est pas un outil d'IA, c'est une façon d'écrire **n'importe quel**
gameplay qui a des phases — un héros, un tour de jeu, un menu, un QTE.

---

## Objectifs

- reconnaître un comportement qui a des **états**
- dessiner sa machine : états, transitions, conditions
- l'écrire en `enum` + `switch`, puis en classes `IState`
- appliquer au tour par tour, à l'interface et aux QTE

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-APU-01 - SOLID en Unity|GPR-UN-APU-01]] — interfaces C#, Dungeon Crawler.

---

## Le problème : les booléens qui s'accumulent

Chaque nouveau cas ajoute un booléen, et chaque booléen double les combinaisons possibles.

```csharp
void Update()
{
    if (isGrounded && !isAttacking && jumpPressed) { isJumping = true; }
    if (isJumping && body.linearVelocity.y < 0f) { isJumping = false; isFalling = true; }
    if (isFalling && isGrounded) { isFalling = false; }
    if (isAttacking && isJumping) { /* on a le droit ? */ }
}
```

Note:
Quatre booléens = 16 combinaisons, dont la plupart n'ont aucun sens
(`isJumping && isFalling`). Rien dans le code n'interdit de les atteindre.
Demander : qui a déjà eu un saut infini ou un personnage bloqué en l'air ?

---

# Rappel : la machine à états
<!-- .slide: class="title" -->

---

## Trois mots

- **état** : ce que fait l'objet *maintenant* — Idle, Course, Saut
- **transition** : le passage d'un état à un autre, déclenché par une **condition**
- **état courant** : un seul à la fois, jamais deux
- tout ce qui n'est pas une transition dessinée est **interdit**

Note:
Machine à états finis (FSM, *finite state machine*) : « finis » parce que la
liste des états est connue d'avance. La dernière ligne est la plus
importante : c'est elle qui supprime les combinaisons absurdes du slide
précédent.

---

## Le héros d'un platformer
<!-- .slide: class="schema" -->

Quatre états, six transitions : tout ce qui n'est pas dessiné est impossible.

![[apu09_fsm_principes.svg]]

Note:
Faire lire le schéma à voix haute : « depuis Course, si je presse saut, je
passe en Saut ». Puis poser la question inverse : peut-on sauter depuis
Chute ? Non — il n'y a pas de flèche. C'est une décision de game design,
rendue visible.
Transition volontairement absente : Idle → Saut. Demander de l'ajouter.

---

## Les règles d'une bonne machine

- chaque état sait **entrer**, **agir** à chaque frame, et **sortir**
- une transition a un nom : « joueur vu », pas `state = 3`
- le dessin vient **avant** le code
- si deux états font la même chose, ce n'en est qu'un

Note:
Entrer / sortir : c'est là qu'on lance une animation, joue un son, active
une hitbox — et qu'on les coupe. Sans Exit, on oublie toujours de désactiver
quelque chose.

---

# En code
<!-- .slide: class="title" -->

---

## Première version : `enum` + `switch`

Suffisant tant que les états tiennent en quelques lignes chacun.

```csharp
public enum HeroState { Idle, Run, Jump, Fall }

private HeroState state = HeroState.Idle;

void Update()
{
    switch (state)
    {
        case HeroState.Idle:
            if (move != Vector2.zero) state = HeroState.Run;
            break;
        case HeroState.Run:
            if (jumpPressed) state = HeroState.Jump;
            else if (move == Vector2.zero) state = HeroState.Idle;
            break;
        // Jump, Fall : même principe
    }
}
```

Note:
Avantage : tout est dans un seul fichier, lisible d'un coup d'œil. Limite :
quand chaque `case` fait 30 lignes, le `switch` redevient le script
fourre-tout de SOLID (S). Et il n'y a pas d'Enter / Exit.

---

## Le pattern State : une classe par état

Chaque état porte son propre code d'entrée, de mise à jour et de sortie.

```csharp
public interface IState
{
    void Enter();   // une fois, en entrant
    void Tick();    // à chaque frame
    void Exit();    // une fois, en sortant
}
```

Note:
On retrouve O de SOLID : ajouter un état = ajouter une classe, sans toucher
aux autres. Et l'interface est celle vue en APU-01.

---

## La machine elle-même

Une dizaine de lignes, réutilisables pour tous les objets du jeu.

```csharp
public class StateMachine
{
    public IState Current { get; private set; }

    public void ChangeState(IState next)
    {
        Current?.Exit();
        Current = next;
        Current.Enter();
    }

    public void Tick() => Current?.Tick();
}
```

Note:
Le `MonoBehaviour` propriétaire crée ses états, appelle `ChangeState` une
fois dans `Start`, puis `machine.Tick()` dans son `Update`. C'est tout.
La machine ne connaît aucun état en particulier : DIP, encore.

---

# Une machine réutilisable
<!-- .slide: class="title" -->

### Celle du companion, tirée d'un projet de jeu

---

## Déclarer les transitions plutôt que les écrire
<!-- .slide: class="schema" -->

![[apu09_machine_generique.svg]]

Note:
Version du companion. La différence avec le slide précédent : les
transitions ne sont plus des `ChangeState` dispersés dans les états, elles
sont **déclarées une fois** à côté du graphe. Le dessin et le code se
relisent ligne pour ligne — c'est tout l'intérêt.
Attention au vocabulaire : cette machine nomme `OnEnter` / `OnExit` ce que
nos slides appellent `Enter` / `Exit`, et son `Tick` reçoit le `deltaTime`.

---

## Les deux méthodes à connaître

Une transition, c'est un état d'arrivée et une condition — une fonction qui rend `true` ou `false`.

```csharp
// depuis un état précis
machine.AddTransition(IState from, IState to, Func<bool> condition);

// depuis n'importe quel état, testée en priorité
machine.AddAnyTransition(IState to, Func<bool> condition);
```

Note:
`Func<bool>` : une méthode sans paramètre qui rend un booléen, passée en
argument — `() => Keyboard.current.spaceKey.wasPressedThisFrame`, ou un nom
de méthode comme `JoueurVu`. C'est ce qui permet de nommer la condition.
`AddAnyTransition` sert à la mort, à la pause, à l'alarme : ce qui peut
arriver quoi qu'on soit en train de faire. Une par machine, rarement plus.

---

## Ce que fait `Tick`

Chaque frame, dans l'ordre : les transitions globales, celles de l'état courant, puis l'état agit.

```csharp
public void Tick(float deltaTime)
{
    IState newState = CheckTransition(_currentState);
    if (newState != _currentState) ChangeState(newState);

    _currentState.Tick(deltaTime);
}
```

Note:
`CheckTransition` regarde d'abord les transitions « any », puis le
dictionnaire `Type -> transitions` de l'état courant, et prend **la
première** condition vraie. L'ordre de déclaration est donc l'ordre de
priorité : à déclarer du plus urgent au moins urgent.
Le `MonoBehaviour` n'a plus qu'une ligne dans son `Update` :
`_machine.Tick(Time.deltaTime);`.

---

## Quatre démos dans le companion

- **Héros** : Grounded, Jumping, Landing — saut à la barre d'espace, atterrissage temporisé
- **Garde** : Idle, Patrouille, Alarme — l'alarme en `AddAnyTransition`
- **QTE** : Invite, Confirmation, Échec, Succès — un état = un panneau d'UI
- **Tour par tour** : deux tourelles, le joueur passe la main, l'IA tire jusqu'à vide

Note:
Ce sont des démos techniques, pas des jeux : des primitives, un panneau de
debug qui affiche l'état courant, rien de plus. Une scène par cas, à ouvrir
et à lire dans l'ordre. Le garde et le QTE sont les deux à montrer en
direct ; le tour par tour se lit mieux à la maison.

---

# Le tour par tour
<!-- .slide: class="title" -->

---

## Chaque tour est un état
<!-- .slide: class="schema" -->

Le jeu a sa machine, chaque unité la sienne : en entrant dans un tour, le jeu réveille son camp.

![[apu09_tour_par_tour.svg]]

Note:
Deux niveaux de machines. En haut, le déroulé de la partie. En bas, ce que
vit chaque unité. Les flèches rouges pointillées sont des `Enter` : entrer
dans « Tour du joueur » passe les unités du joueur en « Active ».
Et la transition du haut (« toutes ont joué ») dépend de l'état des unités
du bas. Exemples : XCOM, Into the Breach, Slay the Spire, Pokémon.

---

## Un tour, en code

L'état « Tour du joueur » active son camp en entrant, et passe la main quand tout le monde a joué.

```csharp
public class PlayerTurnState : IState
{
    private readonly TurnManager turns;
    public PlayerTurnState(TurnManager turns) => this.turns = turns;

    public void Enter()
    {
        foreach (Unit unit in turns.PlayerUnits) unit.Activate();
    }

    public void Tick()
    {
        if (turns.PlayerUnits.All(unit => unit.HasPlayed))
            turns.Machine.ChangeState(turns.EnemyTurn);
    }

    public void Exit() { }
}
```

Note:
`All` demande `using System.Linq;`. `TurnManager` est le `MonoBehaviour` qui
possède la machine et les listes d'unités. L'état ennemi est symétrique :
il active les unités ennemies, et l'IA joue à leur place.

---

# L'interface
<!-- .slide: class="title" -->

---

## Naviguer dans les menus
<!-- .slide: class="schema" -->

Un écran est un état, un bouton une transition : le schéma est déjà la maquette des menus.

![[apu09_ui_navigation.svg]]

Note:
Enter affiche le panneau, Exit le cache : plus de `SetActive(false)` oubliés
sur six panneaux. Le bouton Retour n'est qu'une transition de plus.
Question : que se passe-t-il si on appuie sur Échap pendant le Chargement ?
Rien — il n'y a pas de flèche. C'est exactement ce qu'on veut.

---

## Un QTE
<!-- .slide: class="schema" -->

Le temps est une transition comme une autre : la condition est « chrono écoulé ».

![[apu09_qte.svg]]

Note:
QTE : *quick time event* — God of War, Resident Evil 4, Detroit. L'invite a
son chrono, lancé dans Enter. Deux sorties : la bonne touche avant la fin,
ou le temps écoulé / la mauvaise touche. Enchaîner plusieurs QTE =
enchaîner plusieurs états Invite.

---

## Le QTE, en code

Le chrono démarre en entrant ; chaque frame, on teste la touche, puis le temps.

```csharp
public class QtePromptState : IState
{
    /* champs et constructeur omis */

    public void Enter()
    {
        timeLeft = duration;
        prompt.Show(key);
    }

    public void Tick()
    {
        timeLeft -= Time.deltaTime;
        if (key.WasPressedThisFrame()) machine.ChangeState(success);
        else if (timeLeft <= 0f)       machine.ChangeState(failure);
    }

    public void Exit() => prompt.Hide();
}
```

Note:
`key` est une `InputAction` (nouvel Input System) ; `prompt` le widget d'UI
qui affiche la touche. L'`Exit` cache l'invite quelle que soit l'issue :
c'est l'intérêt d'avoir un point de sortie unique.

---

# Et ailleurs
<!-- .slide: class="title" -->

---

## Quatre autres machines
<!-- .slide: class="schema" -->

Dès qu'un objet a des phases, il a une machine à états — dessinée ou non.

![[apu09_autres_cas.svg]]

Note:
Arme, garde, porte, déroulé de partie. D'autres à faire proposer par la
salle : dialogue (ligne → choix → réponse), boss à phases, véhicule
(au sol / en l'air / détruit), connexion réseau, cycle jour / nuit.

---

## Unity en a déjà une

- l'**Animator** est une machine à états : états, transitions, conditions
- ses `StateMachineBehaviour` offrent `OnStateEnter` / `OnStateExit`
- réservé à l'**animation** : la logique de jeu reste dans votre code
- les deux machines se parlent par les paramètres (`SetBool`, `SetTrigger`)

Note:
Tentation classique : mettre le gameplay dans l'Animator parce que « la
machine est déjà là ». Ça marche jusqu'au jour où l'animation et la règle
de jeu doivent diverger. Garder l'Animator comme **affichage** de l'état.

---

## Quand ça ne suffit plus

- deux ou trois états : un `bool` ou un `enum` suffit
- une dizaine d'états et beaucoup de transitions : machine **hiérarchique** (des états qui contiennent une machine)
- des décisions à priorités multiples : arbre de comportement
- le dessin illisible est le signal d'alarme

Note:
Machine hiérarchique : le boss de l'exercice 6 — chaque phase est une
machine. Arbres de comportement : vus dans le bloc IA
([[cpp_behaviour_tree_lecture]]).

---

## À retenir

- un comportement à phases est une machine : **dessinez-la d'abord**
- un seul état courant ; ce qui n'est pas une transition est interdit
- `enum` + `switch` pour démarrer, une classe `IState` par état quand ça grossit
- tour de jeu, menu, QTE, arme, IA : le même outil

---

## Ressources

- [State — Game Programming Patterns](https://gameprogrammingpatterns.com/state.html) (Robert Nystrom) : le chapitre de référence, avec l'héroïne qui saute
- [State — Refactoring.Guru](https://refactoring.guru/fr/design-patterns/state) : le pattern en schémas et en C#
- [Level up your code with design patterns and SOLID — e-book Unity](https://unity.com/resources/design-patterns-solid-ebook) : chapitre *State pattern*
- [State Machine Basics — Unity Manual](https://docs.unity3d.com/Manual/StateMachineBasics.html) : l'Animator comme machine à états
