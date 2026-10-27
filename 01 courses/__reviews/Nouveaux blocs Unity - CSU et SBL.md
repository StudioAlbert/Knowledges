---
echeance: avant la rentrée du module 2 — 23 nov. 2026
---
# Deux blocs Unity à créer — *C# pour Unity* et *Scènes, Build et Livraison*

> [!info] Note de suivi, pas une tâche de séance
> Le cours **Unity Beginner** du module 2 (1re année) a besoin de quatre heures qu'aucun bloc
> du catalogue ne couvre. Elles tiennent dans **deux blocs nouveaux**, proposés ici, plutôt
> qu'en lignes greffées sur *Prise en Main d'Unity*, qui aurait gonflé à 10 cours sans
> cohérence. À reporter dans `_GSDA_Tech_Vault/Bloc/` et dans
> `_GSDA_Tech_Vault/Spécialisations/Unity.md` avant que les séances soient nommées : le `NN`
> d'une séance se lit dans la colonne `Code` de la fiche de bloc, et ne s'invente pas.
> Plan du module : [[01 courses/Module 2 - Unity Beginner|Module 2 - Unity Beginner]].

## Pourquoi

Le trou est réel et mesuré sur le catalogue entier :

- **Le C# n'est enseigné nulle part.** Aucun des 116 cours de la spécialisation *Unity* ne le
  nomme, aucun bloc du vault non plus — et la volée arrive d'un module 1 **entièrement C++**.
- **Le modèle d'exécution du moteur** — `Awake` / `Start` / `Update` / `FixedUpdate`, l'ordre
  d'exécution, `[SerializeField]` — n'est couvert par aucune ligne.
- **Le débogage** n'apparaît pas une seule fois : ni Console, ni point d'arrêt, ni Profiler.
- **Les scènes et le build** ne sont qu'une mention en fin de contenu de `PMU-02`
  (« scènes et build settings »), déjà chargée de l'arborescence d'assets, de l'import, des
  GameObject et des réglages de projet.

## `GPR-UN-CSU` · C# pour Unity

Le langage et le modèle d'exécution du moteur, pour qui arrive du C++ : écrire, comprendre
quand le code tourne, et diagnostiquer quand il ne tourne pas.

- `code: CSU` · `specialisation: "[[Unity]]"` · `mineur: Games Programming`
- `prerequis` : *Prise en Main d'Unity*, *Programmation Orientée Objet*
- `cours: 3`
- Ordre dans la spécialisation : **2**, entre *Prise en Main d'Unity* et *Contrôle et
  Déplacement*, qui en devient le bloc suivant.

| # | Code | Cours (1h) | Contenu |
|---|---|---|---|
| 1 | `01` | MonoBehaviour : la frame et le cycle de vie | `Awake`, `OnEnable`, `Start`, `Update`, `FixedUpdate`, `LateUpdate`, `OnDestroy` ; ordre d'exécution entre objets ; `[SerializeField]` et l'Inspector comme interface de réglage |
| 2 | `02` | Déboguer dans Unity | Lire la Console et une stack trace ; `Debug.Log` et ses limites ; point d'arrêt dans Rider ou Visual Studio ; inspecter en cours de jeu, et le piège des valeurs modifiées en Play ; `NullReferenceException` |
| 3 | `03` | C# : ce que le langage fait autrement | Interfaces ; ramasse-miettes ; un langage à référence par défaut ; LINQ ; écriture en propriétés et fonction courte `=>` ; l'absence de `.h` |

**Validation** : un comportement dont tous les réglages sont exposés dans l'Inspector, dont
l'étudiant sait dire à quelle phase chaque ligne s'exécute, et dont il diagnostique seul une
référence nulle au point d'arrêt.

## `GPR-UN-SBL` · Scènes, Build et Livraison

Ce qui sépare un projet qui tourne dans l'éditeur d'un jeu qu'on envoie à quelqu'un.

- `code: SBL` · `specialisation: "[[Unity]]"` · `mineur: Games Programming`
- `prerequis` : *Prise en Main d'Unity*
- `cours: 2`
- Ordre dans la spécialisation : **3**, après *C# pour Unity*.

| # | Code | Cours (1h) | Contenu |
|---|---|---|---|
| 1 | `01` | Scènes, chargement et build | Une scène, ce qu'elle contient et ce qu'elle ne garde pas ; `SceneManager`, recharger, enchaîner ; Build Profiles et la Scene List ; Player Settings — nom, icône, résolution, plein écran ; produire un exécutable et le faire tourner ailleurs ; publier le build dans une release GitHub (`git tag`, `gh release create`), et ce qu'on ne commite jamais |
| 2 | `02` | Cibles et distribution | Plateformes et profils, taille du build et stripping, signature et avertissements système, dépôt sur une page publique |

**Validation** : un exécutable produit par l'étudiant, publié en release sur son dépôt, qui
s'ouvre et se joue sur la machine d'un camarade.

Seul le cours `01` est donné au module 2 ; le `02` attend un module ultérieur.

## Ce que ça change dans `Spécialisations/Unity.md`

| | Avant | Après |
|---|---|---|
| `blocs` | 12 | **14** |
| `cours` | 116 | **121** |
| Table *Blocs* | 1 Prise en Main, 2 Contrôle et Déplacement, … | 1 Prise en Main, **2 C# pour Unity**, **3 Scènes, Build et Livraison**, 4 Contrôle et Déplacement, … |

La chaîne de prérequis ne change pas en aval : *Contrôle et Déplacement* garde *Prise en Main
d'Unity* comme prérequis et gagne *C# pour Unity*.

## À faire côté département

- [ ] Créer `_GSDA_Tech_Vault/Bloc/C# pour Unity.md` — `type: bloc`, `code: CSU`, `prerequis`,
      `projet`, table `## Cours` à trois lignes, `## Objectifs`, `## Validation`, `## Liens`.
- [ ] Créer `_GSDA_Tech_Vault/Bloc/Scènes, Build et Livraison.md` — même structure, `code: SBL`,
      deux lignes de cours.
- [ ] Mettre à jour `Spécialisations/Unity.md` : compteurs, table des blocs, ordre, prérequis.
- [ ] Poser les 4 cours concernés dans `Classes/GP-926.md` § 4-2, aujourd'hui vide côté Unity
      (« Le reste du module est à poser »).
- [ ] Arbitrer les codes à trois lettres et les intitulés — `CSU` et `SBL` sont une proposition.
- [ ] Reporter dans [[01 courses/Séances GSDA 2026-2027|Séances GSDA 2026-2027]] une fois les
      codes arrêtés.

> [!question] À trancher en même temps
> `_GSDA_Tech_Vault/Classes/GP-926.md` pose les cours `04 → 07` d'*Architecture et Patterns
> Unity* sur ce même module `4-2`, et les quatre notes de `01 courses/lectures/Unity/` portent
> `classes: [GP-926]` et `projet: Module 2`. Ces cours relèvent de la 2e année : il faut les
> sortir du module ou corriger leur `classes`, sinon le kanban et le site annoncent deux
> programmes pour le même créneau. Le vault GSDA le signalait déjà — « GP-926 aborde donc ici
> les cours 04 → 07 sans les avoir. À arbitrer avant la rentrée du module. »
