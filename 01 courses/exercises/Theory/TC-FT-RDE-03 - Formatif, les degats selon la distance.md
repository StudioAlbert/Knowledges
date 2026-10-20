---
seances: [TC-FT-RDE-03]
---
# Formatif — les dégâts selon la distance

Le game designer pose **trois règles**, et il ne dira rien de plus :

| | |
|---|---|
| à bout portant, **moins de 0,25 m** | 25 dégâts |
| à partir de **5 m** | 0 dégât |
| entre les deux | ça descend |

Tout le reste est à vous. Vous écrivez **deux** fonctions qui respectent ces trois règles et
qui n'ont pas la même allure entre les bornes : `DegatsProportionnels`, puis `DegatsAmortis`.

---

## Le programme de départ

> [!tip] Il est fourni
> Clonez
> [TC_FT_RDE_03_DegatsSelonLaDistance](https://github.com/StudioAlbert/TC_FT_RDE_03_DegatsSelonLaDistance) —
> il compile tel quel (`cmake -S . -B build`, puis `cmake --build build`), et les deux
> fonctions vous attendent dans `01_degats/src/degats.cc`.

On entre une distance, le programme affiche les dégâts dans la console. Les deux fonctions
sont vides : on commente l'un ou l'autre appel pour passer d'un mode à l'autre.

```cpp
#include <iostream>

constexpr float kDegatsMax = 25.f;
constexpr float kDistanceMin = 0.25f;   // en deçà : dégâts maximum
constexpr float kDistanceMax = 5.f;     // au-delà : aucun dégât

float DegatsProportionnels(float distance)
{
    return 0.f;   // étape 1
}

float DegatsAmortis(float distance)
{
    return 0.f;   // étape 2
}

int main()
{
    float distance = 0.f;
    while (std::cin >> distance)
    {
        std::cout << distance << " m  ->  "
                  << DegatsProportionnels(distance)
        //        << DegatsAmortis(distance)
                  << " degats\n";
    }
}
```

---

## Étape 1 — `DegatsProportionnels`

### 1.1 — Les bornes, et rien d'autre

Ecrivez une première version de la fonction **DegatsProportionnels** qui respecte les régles suivantes :
- `distance < 0,25` → **25**
- `distance ≥ 5` → **0**
- entre les deux → **12,5**

>[!Warning] 
>Le fonctionnement est partiel et provisoire, pour mettre en place les deux règles de bornage.
>Vérifiez avec `0.1`, `2`, `7` avant de continuer.
### 1.2 — La proportionnalité

Remplacez le **12,5** par la vraie valeur, en trois gestes :

1. **normaliser** la distance entre 0 et 1 :

   <p class="formule">t = (distance − 0,25) / (5 − 0,25)</p>

2. **borner** ce `t` entre 0 et 1 avec un `clamp` ;
3. **descendre** : `dégâts = 25 × (1 − t)`.

Une fois le `clamp` en place, les deux cas de l'étape 1.1 **disparaissent** : 
- à 0,1 m, `t` vaut −0,03 et le `clamp` le ramène à 0, donc 25 dégâts. 
- À 7 m, `t` vaut 1,42, ramené à 1, donc 0. 
- Les `if` ne servent plus à rien, ils sont remplacés par des maths purs.

> [!check] Ce qu'on vérifie
>
> | distance | dégâts attendus |
> |---|---|
> | 0 m | 25 |
> | 0,25 m | 25 |
> | 2,625 m | 12,5 |
> | 5 m | 0 |
> | 12 m | 0 |

---

## Étape 2 — `DegatsAmortis`

Même règles, autre forme. Celle-ci **garde ses dégâts plus longtemps**, puis s'effondre.
Voici sa courbe, et les cinq points qu'elle doit passer. 
Vous devez trouver la formule adéquate.

![[rde03_degats_amortis.svg]]

### 2.1 — Trouver le calcul

Il y a **une seule opération de plus** que dans l'étape 1.2. Trois indices :

- les deux bornes restent **exactes** : 25 à 0,25 m, et 0 à 5 m. Toute formule qui rate l'un
  des deux est fausse ;
- la moitié des dégâts est atteinte à **3,8 m**, et non au milieu de l'intervalle. La courbe
  n'est donc pas symétrique ;
- vous travaillez sur `1 − t`, pas sur `t`.

### 2.2 — Vérifier que le code colle au graphe

Lire la courbe à l'œil ne prouve rien. Écrivez une vérification qui se relit :

1. faire afficher par le programme la table `distance → dégâts` pour les **cinq** distances
   du schéma ;
2. comparer à la colonne de droite, avec une tolérance de **± 0,5** ;
3. ajouter les deux bornes et un point hors domaine — `0 m` et `12 m` — qui doivent donner
   25 et 0 **exactement** ;
4. Vous pouvez proposer plusieurs fonctions qui proposeraient différentes approximations.

---

## Ce qu'on rend

|                | Ce qui est attendu                                                      |
| -------------- | ----------------------------------------------------------------------- |
| **le code**    | les deux fonctions, et le `main` qui lit une distance                   |
| **la table**   | les cinq points du schéma, affichés par votre programme                 |

> [!check] Grille d'auto-évaluation
>
> | Je sais… | Vérification |
> |---|---|
> | traduire une règle de gameplay en bornes | 5 m exactement donne 0, et je sais dire pourquoi |
> | normaliser | ma variable intermédiaire vaut 0 à 0,25 m et 1 à 5 m |
> | borner | je n'ai plus besoin des `if` de l'étape 1.1 |
> | composer | je change la forme sans toucher à la normalisation |
> | vérifier | ma table se compare au schéma sans que j'aie à plisser les yeux |
