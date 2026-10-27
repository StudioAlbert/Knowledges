---
title: GPR-UN-APU-05 - Observer, prévenir sans connaître
type: slides
subject: Unity
duration_h: 1
bloc_gsda: Architecture et Patterns Unity
specialisation: Unity
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
---

# Observer, prévenir sans connaître
<!-- .slide: class="title" -->

### Un objet annonce, ceux que ça intéresse écoutent

<small>GPR-UN-APU-05 · Architecture et Patterns Unity</small>

Note:
Séance réécrite le 28.09 : elle portait « ScriptableObjects, architecture
data-driven » ; les ScriptableObjects tiennent désormais en une séance
(APU-04) et celle-ci devient le pattern Observer. Les canaux d'événement en
ScriptableObject y sont la troisième façon de faire, d'où le lien avec APU-04.

---

## Objectifs

- reconnaître un couplage « qui prévient qui »
- publier un événement en C# : `event Action`
- choisir entre `event`, `UnityEvent` et canal en ScriptableObject
- éviter l'abonné fantôme

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|GPR-UN-APU-04]] — ScriptableObjects.

---

## Le problème : qui prévenir quand le joueur perd un PV ?

`PlayerHealth` connaît sa barre de vie… et bientôt le son, la caméra, les succès.

```csharp
public class PlayerHealth : MonoBehaviour
{
    [SerializeField] private HealthBar healthBar;
    [SerializeField] private AudioSource hurtSound;
    [SerializeField] private CameraShake cameraShake;
    private int health = 100;

    public void TakeDamage(int amount)
    {
        health -= amount;
        healthBar.Show(health);
        hurtSound.Play();
        cameraShake.Shake(0.2f);
    }
}
```

Note:
Point de départ : la branche `01-srp` du Dungeon Crawler, où `PlayerHealth`
appelle `HealthBar`. Le deck SOLID annonçait déjà qu'on retirerait ce lien
avec un événement. Chaque réacteur ajouté = un champ et une ligne de plus dans
`PlayerHealth`, qui n'a rien demandé.

---

## Avant, après
<!-- .slide: class="schema" -->

Le nombre de flèches qui partent de `PlayerHealth` est l'argument.

![[apu05_couplage.svg]]

Note:
À gauche, PlayerHealth dépend de quatre classes. À droite, il ne dépend de
personne : il annonce « j'ai pris des dégâts », et chacun s'abonne. C'est
l'exemple des succès de Nystrom : « je ne sais pas si ça intéresse
quelqu'un, mais ce truc vient de tomber ».

---

## Le pattern Observer

- le **sujet** annonce qu'il s'est passé quelque chose
- les **observateurs** s'**abonnent** à cette annonce, et s'en désabonnent
- le sujet ne sait ni **qui** écoute, ni **combien**
- l'annonce est un appel de méthode : immédiat, sans magie

Note:
Aussi appelé publish / subscribe. « Sans magie » : notifier = parcourir une
liste et appeler une méthode sur chacun, synchrone. Nystrom insiste : ce
n'est pas lent, aucune allocation au moment de la notification.

---

# Trois façons en Unity
<!-- .slide: class="title" -->

---

## 1 · `event Action` : le sujet

Le mot-clé `event` : les autres peuvent s'abonner, mais seul le sujet peut déclencher.

```csharp
using System;

public class PlayerHealth : MonoBehaviour
{
    public event Action<int, int> Damaged;   // (PV restants, PV max)

    [SerializeField] private int maxHealth = 100;
    private int health;

    void Awake() => health = maxHealth;

    public void TakeDamage(int amount)
    {
        health -= amount;
        Damaged?.Invoke(health, maxHealth);
    }
}
```

Note:
`?.` : si personne n'écoute, l'événement est `null` et on n'appelle rien.
`Action<int, int>` : le délégué décrit la forme de l'annonce. On peut aussi
passer une structure si l'annonce grossit.

---

## 1 · `event Action` : l'observateur

On s'abonne dans `OnEnable`, on se désabonne dans `OnDisable` — toujours par paire.

```csharp
public class HealthBar : MonoBehaviour
{
    [SerializeField] private PlayerHealth player;
    [SerializeField] private TMP_Text label;

    void OnEnable()  => player.Damaged += Show;
    void OnDisable() => player.Damaged -= Show;

    private void Show(int health, int max) => label.text = $"PV : {health} / {max}";
}
```

Note:
Le sens de la dépendance s'est inversé : c'est la barre de vie qui connaît
`PlayerHealth`, plus l'inverse. Retirer la barre de la scène ne casse plus
rien. `TMP_Text` demande `using TMPro;`.

---

## 2 · `UnityEvent` : câbler dans l'Inspector

Même principe, mais les abonnés se branchent à la souris, sans code.

- le lien vit **dans la scène**, pas dans le code
- c'est le **game designer** qui câble, à l'intégration

```csharp
using UnityEngine.Events;

public class PressurePlate : MonoBehaviour
{
    [SerializeField] private UnityEvent pressed;

    void OnTriggerEnter2D(Collider2D other) => pressed.Invoke();
}
```

Note:
Dans l'Inspector : une liste « Pressed () » où l'on glisse la porte et
choisit `Door.Open`. Idéal pour les level designers. Coût : un peu plus
lent qu'un `event` C#, et les liens sont invisibles dans le code — on ne
les trouve qu'en ouvrant la scène. Exemple réel : `FactionQuestCollector`
de MallLife expose `_onCollected`, `_onCollectFailed`, `_onQuestComplete`.

---

## Câblé, vu de l'Inspector
<!-- .slide: class="schema" -->

`All Collected ()` appelle `GameObject.SetActive` sur `EndPanel` : le panneau n'a pas de script.

![[apu05_inspector_unityevent.png]]

Note:
C'est l'`ItemManager` du companion de l'atelier. Une seule entrée dans la
liste : *Runtime Only*, l'objet `EndPanel`, la méthode `GameObject.SetActive`,
case cochée. Personne n'a écrit de script pour ce panneau, et le gestionnaire
ne connaît pas son existence — il invoque un `UnityEvent`, point.

Le composant que tout le monde a déjà vu, c'est **`PlayerInput`** : en mode
*Behavior › Invoke Unity Events*, il expose un `UnityEvent` par action
(`On Move`, `On Jump`, …) qu'on câble exactement comme celui-ci. L'Observer
est déjà dans leurs projets, ils ne l'avaient pas nommé.

Les deux emplacements du dessus, *Remaining Channel* et *Item Collected
Channel*, sont le troisième mécanisme : on y arrive dans deux slides.

---

## 3 · Le canal d'événement en ScriptableObject
<!-- .slide: class="schema" -->

Le sujet et les observateurs ne se connaissent plus du tout : ils partagent un asset.

![[apu05_canal_so.svg]]

Note:
Suite directe d'APU-04 : l'asset existe une fois dans le projet, toutes les
scènes peuvent le référencer. Garde et caméra ne savent pas qu'une jauge
existe ; la jauge ne sait pas qui déclenche l'alarme. Deux scènes chargées
séparément peuvent communiquer. Architecture popularisée par Ryan Hipple
(Unite Austin 2017) et reprise dans l'Open Project de Unity.

---

## 3 · Le canal, en code

Tiré de MallLife : un asset par événement, un type par forme d'annonce.

```csharp
public abstract class GenericEventChannelSO<T> : ScriptableObject
{
    public event UnityAction<T> OnEventRaised;

    public void RaiseEvent(T parameter) => OnEventRaised?.Invoke(parameter);
}

[CreateAssetMenu(menuName = "Events/Float EventChannel")]
public class EventChannelFloatSO : GenericEventChannelSO<float> { }
```

Note:
Source : `MallLifeStealthGame/…/Core/Events/GenericEventChannelSO.cs`.
`UnityAction` demande `using UnityEngine.Events;`.
Seule différence avec l'original : le mot-clé `event` devant
`OnEventRaised` (voir la slide des pièges). Les assets `RaiseAlarm`,
`ReleaseAlarm`, `ResetAlarm` sont dans `_Datas/Events`.

---

## 3 · S'abonner au canal

`AlertManager` écoute trois canaux, sans savoir qui les déclenche.

```csharp
public class AlertManager : MonoBehaviour
{
    [SerializeField] private EventChannelFloatSO raiseAlertEvt;
    [SerializeField] private EventChannelFloatSO releaseAlertEvt;
    [SerializeField] private EventChannelVoidSO resetAlertEvt;

    void OnEnable()
    {
        raiseAlertEvt.OnEventRaised += RaiseAlert;
        releaseAlertEvt.OnEventRaised += ReleaseAlert;
        resetAlertEvt.OnEventRaised += ResetAlert;
    }

    void OnDisable() { /* les trois -= */ }
}
```

Note:
Extrait simplifié de `Alarm/AlertManager.cs` (MallLife). L'AlertManager
publie à son tour `OnAlertStateChanged` en `event Action<AlertState>` : un
observateur peut être le sujet d'autres observateurs.

---

## Et Unity l'a mis dans ses graphes

Le paquet **Behavior** fait communiquer ses graphes par… un canal d'événement.

- **Send Event Message** publie ; **Start On** et **Wait for Event Message** écoutent
- le canal naît dans le Blackboard : `+` › *Events* › *Create new event channel type*
- pour relier **deux graphes**, un asset partagé : *Create › Behavior › Event Channels*
- la classe générée dérive de `EventChannel<T>` — donc d'un **ScriptableObject**

Note:
`com.unity.behavior`, 1.0.16 pour Unity 6.3. Le point à faire passer : le canal
en ScriptableObject n'est pas une astuce de forum, c'est l'architecture que
Unity a retenue pour son propre outil de comportement. La même idée que la
slide précédente, livrée dans la boîte.

Un graphe qui écoute avec *Start On Event Message* démarre quand l'annonce
tombe ; *Wait for* met la branche en pause jusque-là. C'est l'Observer, avec
une boîte à la place du `+=`.

---

## Un graphe publie, un autre écoute
<!-- .slide: class="schema" -->

À gauche *Send Event Message*, à droite *On EventChannel* : ni l'un ni l'autre ne se connaissent.

![[apu05_behavior_graph.png]]

Note:
Deux branches du même graphe, reliées par un seul asset de canal. Celle de
gauche publie « Empty Event received » toutes les 0,5 à 1 seconde ; celle de
droite démarre sur l'annonce et écrit dans la console. Remplacer l'une ne
demande pas de toucher à l'autre — c'est l'Observer, avec une boîte à la
place du `+=`.

Côté C#, la classe générée dérive de `EventChannel<T>`, donc d'un
ScriptableObject : un script s'abonne au même asset avec `+=`, et publie avec
`SendEventMessage`. Designer et programmeur avancent sans s'attendre.

---

## Laquelle choisir ?

| | `event Action` | `UnityEvent` | Canal en SO |
|---|---|---|---|
| Qui câble | le code | l'Inspector | l'Inspector (asset) |
| Le sujet connaît, dans son code | **personne** | **personne** | **personne** |
| L'observateur connaît | le sujet | **personne** | l'asset |
| Entre deux scènes | non | non | **oui** |
| Retrouver les liens | **« Find usages »** | **ouvrir la scène** | **chercher l'asset** |

Note:
Règle pratique : `event` entre scripts d'un même objet ou d'un même
système ; `UnityEvent` pour ce que le level designer câble ; canal en SO
pour ce qui traverse les scènes ou relie des systèmes indépendants (UI,
audio, sauvegarde).

---

# Les pièges
<!-- .slide: class="title" -->

---

## L'abonné fantôme

Un abonnement jamais retiré garde en vie un objet détruit — et l'appelle quand même.

```csharp
void OnEnable()
{
    channel.OnEventRaised += () => view.Show();   // lambda anonyme
}

void OnDisable()
{
    channel.OnEventRaised -= () => view.Show();   // une AUTRE lambda : rien n'est retiré
}
```

Note:
Le *lapsed listener problem* de Nystrom. Cas réel, repris de
`QuestManager` dans MallLife : deux lambdas identiques à l'écriture sont
deux délégués différents, le `-=` ne retire rien. Au rechargement de la
scène : `MissingReferenceException`. Correction : une méthode nommée
(`ShowView`), abonnée et désabonnée par son nom.

**Démonstration en direct, trente secondes, dans le companion.** Dans
`CounterLabel`, remplacer `remainingChannel.Raised += Show;` par la lambda
`remainingChannel.Raised += n => Show(n);` et faire de même dans `OnDisable`.
Lancer, désactiver l'objet **HUD** dans la Hierarchy, ramasser une gemme :
l'abonnement n'a pas été retiré, et la console sort une
`MissingReferenceException`. Réactiver la méthode nommée, refaire le même
geste : plus rien. C'est le critère « désactiver le HUD ne déclenche aucune
erreur » de la fiche d'exercices.

---

## `event` ou pas `event`

Un seul mot-clé change ce que le reste du projet a le droit de faire.

```csharp
public Action<int> Damaged;         // sans event
public event Action<int> Damaged;   // avec event

// depuis n'importe quelle autre classe :
subject.Damaged += Show;     // les deux : d'accord
subject.Damaged = Show;      // sans event : efface tous les abonnés
subject.Damaged.Invoke(3);   // sans event : annonce à la place du sujet
                             // avec event : ne compile pas
```

Réflexe : `public event …`, jamais `public Action …`.

Note:
`event` ne change ni le type ni le coût : il restreint les droits de
l'extérieur. Dedans, la classe fait ce qu'elle veut ; dehors, seuls `+=` et
`-=` compilent. Sans lui, un `=` posé ailleurs efface silencieusement tous
les abonnés déjà en place, et n'importe qui peut déclencher l'annonce à la
place du sujet — l'annonce ne veut alors plus rien dire.

C'est la seule retouche faite au code de MallLife dans ce deck :
l'original déclare `public UnityAction<T> OnEventRaised;`, sans `event`.
Un `OnEventRaised = Foo;` ailleurs dans le projet détacherait
silencieusement l'AlertManager.

---

## Qui a appelé qui ?

- l'ordre des observateurs n'est **pas** un contrat : ne pas en dépendre
- un canal sans trace devient indébogable : prévoir un `Debug.Log` activable
- un observateur qui publie à son tour crée une **chaîne** : attention aux boucles
- trop d'événements, et plus personne ne sait ce que fait le jeu

Note:
Nystrom : le couplage devient dynamique, donc invisible à la lecture. La
parade : des noms d'événements au passé (`Damaged`, `AlarmRaised`), un seul
endroit qui les déclare, et un mode verbeux dans le canal.

---

## Un canal qui se raconte

Une case à cocher sur l'asset, et la console dit qui écoute vraiment.

```csharp
[SerializeField] private bool verbose;

public void Raise(T value)
{
    if (verbose) Debug.Log($"{name} = {value} -> {Listeners(Raised)}", this);
    Raised?.Invoke(value);
}

// Listeners() lit Raised.GetInvocationList() : le nom de chaque abonné,
// et « <destroyed> » pour celui qui n'aurait pas fait son -=.
```

Note:
C'est la réponse aux quatre points de la slide précédente, en une case à
cocher. `GetInvocationList()` rend les délégués un par un ; `subscriber.Target`
est l'objet abonné, `subscriber.Method.Name` la méthode. Un abonné détruit
donne un `Target` à `null` côté Unity — l'abonné fantôme devient **visible**
au lieu de planter trois minutes plus tard.

Le deuxième argument de `Debug.Log`, `this`, fait clignoter l'asset du canal
dans le Project quand on clique la ligne de console.

Dans le companion, branche `main` : cocher *Verbose* sur `GemsRemaining`,
jouer, ramasser une gemme.

```
GemsRemaining = 5 -> 1 : HUD.Show
GemCollected  -> 1 : SoundManager.PlayPickup
GemsRemaining = 3 -> nobody        (HUD désactivé en cours de partie)
```

---

## Atelier — 20 min

Un platformer pirate où l'on ramasse cinq gemmes, branche `01-depart` : **tout y est couplé**. On démonte, dans l'ordre des trois mécanismes.

<small>[[01 courses/exercises/Unity/GPR-UN-APU-05 - Observer, prévenir sans connaître|Énoncé]] · [GPR-UN-APU-05 — Observer](https://github.com/StudioAlbert/GPR-UN-APU-05---Observer)</small>

Note:
Trois démontages, après la prise en main : `Item` annonce au lieu
d'appeler ; le panneau de fin passe en `UnityEvent` câblé dans
l'Inspector ; le son et le compteur arrivent par deux canaux en SO.

Le critère de réussite est le **dernier** : une fois les canaux posés, ils
écrivent `SoundManager` sans rouvrir un seul fichier existant. C'est la
seule chose qu'ils doivent retenir du TP, et elle ne se démontre qu'en la
faisant.

Le bouton **Restart** du HUD reste couplé exprès : il appelle
`ItemManager.ResetItems()` et personne n'y touche. Deux façons de faire sur
le même écran — la question n'est pas « laquelle est bien », mais pourquoi
pas la même partout.

La branche `main` est le corrigé — ne la montrer qu'à la fin.

---

## À retenir

- le sujet **annonce**, il ne sait pas qui écoute
- `event Action` en code, `UnityEvent` dans l'Inspector, canal en SO entre les scènes
- `+=` dans `OnEnable`, `-=` dans `OnDisable`, avec une méthode nommée
- `public event`, jamais un délégué public nu

---

## Ressources

- [Create modular and maintainable code with the observer pattern — Unity Learn](https://learn.unity.com/tutorial/create-modular-and-maintainable-code-with-the-observer-pattern)
- [Observer — Game Programming Patterns](https://gameprogrammingpatterns.com/observer.html) (Robert Nystrom) : les succès, l'abonné fantôme
- [Observer — Unity Design Patterns](https://www.unitydesignpatterns.com/patterns/observer)
- [Observer — Refactoring.Guru](https://refactoring.guru/design-patterns/observer)
- [Generic Observer\<T\> — gist d'Adam Myhre](https://gist.github.com/adammyhre/353195d4870e8fd0cc0028659e66f208)
- Scriptable Events de MallLife : [StudioAlbert/MallLifeStealthGame — `_Datas/Events`](https://github.com/StudioAlbert/MallLifeStealthGame/tree/main/MallLife-UnityProject/Assets/03%20-%20Scripts/_Datas/Events)
