---
title: GPR-UN-APU-05 - Observer, prévenir sans connaître
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
publish: false
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

**Prérequis :** [[01 courses/slides/Unity/GPR-UN-APU-04 - ScriptableObjects — les données hors du code|GPR-UN-APU-04]] — ScriptableObjects ; Dungeon Crawler, branche `01-srp`.

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

## Laquelle choisir ?

| | `event Action` | `UnityEvent` | Canal en SO |
|---|---|---|---|
| Qui câble | le code | l'Inspector | l'Inspector (asset) |
| Le sujet connaît, dans son code | personne | personne | personne |
| L'observateur connaît | le sujet | personne | l'asset |
| Entre deux scènes | non | non | **oui** |
| Retrouver les liens | « Find usages » | ouvrir la scène | chercher l'asset |

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

---

## `event` ou pas `event`

- sans `event`, un champ délégué public accepte `=` : un script **efface** tous les abonnés
- sans `event`, n'importe qui peut **déclencher** l'annonce à la place du sujet
- avec `event` : dehors, seuls `+=` et `-=` compilent
- réflexe : `public event …`, jamais `public Action …`

Note:
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

## Une valeur qui prévient quand elle change

Variante générique : la valeur et son événement dans un même objet.

```csharp
[Serializable]
public class Observable<T>
{
    [SerializeField] private T value;
    public event Action<T> Changed;

    public T Value
    {
        get => value;
        set
        {
            if (Equals(this.value, value)) return;
            this.value = value;
            Changed?.Invoke(value);
        }
    }
}
```

Note:
Version simplifiée du `Observer<T>` d'Adam Myhre (gist cité en
ressources), qui utilise un `UnityEvent<T>` pour être câblable dans
l'Inspector. Usage : `public Observable<int> Gold;`, puis
`Gold.Changed += UpdateLabel;`. Le test d'égalité évite de notifier pour
rien.

---

## Atelier — 20 min

Sur la branche `01-srp` du Dungeon Crawler : couper le lien `PlayerHealth → HealthBar` avec un événement, puis ajouter un son sans toucher à `PlayerHealth`.

Note:
Énoncé : [[01 courses/exercises/Unity/GPR-UN-APU-05 - ScriptableObjects — architecture data-driven|exercice 1]].
Critère de réussite : `PlayerHealth` ne contient plus aucune référence à
une classe d'UI ou d'audio, et désactiver la barre de vie en jeu ne
déclenche aucune erreur.

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
