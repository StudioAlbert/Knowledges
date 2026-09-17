---
seances:
  - GPR-CF-BDP-03
---

# Exercices — GPR-CF-BDP-03 — Fonctions

> Cours associé : [[01 courses/slides/C++/GPR-CF-BDP-03 - Fonctions]]

Un seul fichier `main.cpp` par exercice. Pas de `if`, pas de boucle : uniquement des fonctions, des variables et des calculs.

## Exercice 1 — La calculette

### Étape 1 — Les quatre opérations

Écrire les fonctions suivantes, chacune avec son `return` :

```cpp
int additionner(int a, int b);
int soustraire(int a, int b);
int multiplier(int a, int b);
int diviser(int a, int b);      // division entière
int reste(int a, int b);        // reste de la division, avec %
```

On suppose que `b` n'est jamais 0.

### Étape 2 — Une division à virgule

Ajouter une **surcharge** `float diviser(float a, float b)`. Vérifier que `diviser(7, 2)` et `diviser(7.0f, 2.0f)` n'appellent pas la même fonction.

### Étape 3 — Des fonctions qui en appellent d'autres

Écrire ces fonctions **en réutilisant** celles des étapes précédentes, sans écrire d'opérateur `+`, `-`, `*` ou `/` :

```cpp
int carre(int x);
int perimetre_rectangle(int largeur, int hauteur);
```

Puis `float moyenne(float a, float b)`, qui peut utiliser `+` et votre `diviser`.

### Étape 4 — Tester dans `main`

Appeler chaque fonction depuis `main` et afficher le résultat. On doit obtenir :

```
12 + 5 = 17
12 - 5 = 7
12 * 5 = 60
7 / 2 = 3
7 % 2 = 1
7.0 / 2.0 = 3.5
carre(9) = 81
perimetre(4, 3) = 14
moyenne(12, 15) = 13.5
```

### Critères de réussite

- chaque fonction tient en une ou deux lignes
- `carre` et `perimetre_rectangle` ne contiennent aucun opérateur arithmétique
- les fonctions sont **pré-déclarées** au-dessus de `main` et définies en dessous

## Exercice 2 — Le combat de monstres, en fonctions

### Code de départ

Ce programme simule trois tours d'un combat entre un orc et un troll. Il fonctionne, mais tout est dans `main`.

```cpp
#include <iostream>

int main()
{
    // L'orc
    int pv_orc = 60;
    int attaque_orc = 14;
    int defense_orc = 4;

    // Le troll
    int pv_troll = 80;
    int attaque_troll = 11;
    int defense_troll = 6;

    std::cout << "=== Tour 1 ===\n";
    int degats = attaque_orc - defense_troll;
    pv_troll = pv_troll - degats;
    std::cout << "L'orc frappe le troll : " << degats << " degats\n";
    std::cout << "Troll : " << pv_troll << " PV\n";
    degats = attaque_troll - defense_orc;
    pv_orc = pv_orc - degats;
    std::cout << "Le troll frappe l'orc : " << degats << " degats\n";
    std::cout << "Orc : " << pv_orc << " PV\n";

    std::cout << "=== Tour 2 ===\n";
    degats = attaque_orc - defense_troll;
    pv_troll = pv_troll - degats;
    std::cout << "L'orc frappe le troll : " << degats << " degats\n";
    std::cout << "Troll : " << pv_troll << " PV\n";
    degats = attaque_troll - defense_orc;
    pv_orc = pv_orc - degats;
    std::cout << "Le troll frappe l'orc : " << degats << " degats\n";
    std::cout << "Orc : " << pv_orc << " PV\n";

    std::cout << "=== Tour 3 ===\n";
    degats = attaque_orc - defense_troll;
    pv_troll = pv_troll - degats;
    std::cout << "L'orc frappe le troll : " << degats << " degats\n";
    std::cout << "Troll : " << pv_troll << " PV\n";
    degats = attaque_troll - defense_orc;
    pv_orc = pv_orc - degats;
    std::cout << "Le troll frappe l'orc : " << degats << " degats\n";
    std::cout << "Orc : " << pv_orc << " PV\n";

    return 0;
}
```

### Étapes

1. Lancer le programme et **garder sa sortie** : elle servira de référence.
2. Repérer les lignes qui se répètent. Combien de fois la formule des dégâts est-elle écrite ?
3. Écrire `int calculer_degats(int attaque, int defense)`.
4. Écrire `void afficher_pv(std::string nom, int pv)`, qui affiche par exemple `Troll : 72 PV`. Ajouter `#include <string>` en haut du fichier.
5. Écrire `void afficher_tour(int numero)`, qui affiche `=== Tour 1 ===`.
6. Écrire une fonction `attaquer` qui calcule les dégâts, affiche la ligne « … frappe … », et **renvoie** les nouveaux PV de la cible. À vous de choisir ses paramètres.
7. Réécrire `main` avec ces fonctions.

### Critères de réussite

- la sortie est **identique** à celle du programme de départ
- la formule `attaque - defense` n'apparaît qu'**une seule fois** dans tout le fichier
- un tour de combat tient en quelques lignes dans `main`
- les noms des fonctions sont des verbes qui disent ce qu'elles font

### Bonus

- Ajouter un gobelin (40 PV, 9 d'attaque, 2 de défense) qui attaque le troll au tour 3. Seul `main` doit changer.
- Pré-déclarer toutes les fonctions en haut du fichier, et placer leurs définitions après `main`.
