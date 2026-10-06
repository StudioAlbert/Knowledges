# Exercices — GPR-CF-POO-02 — Classes et visibilité

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-02 - Classes et visibilité|GPR-CF-POO-02 - Classes et visibilité]]

On repart de la structure `Monstre` de
[[01 courses/slides/C++/GPR-CF-POO-01 - Structures|GPR-CF-POO-01]]. Un seul fichier
`main.cpp` par exercice — le découpage `.h` / `.cpp` arrive en
[[01 courses/slides/C++/GPR-CF-POO-03 - Découpage en fichiers|GPR-CF-POO-03]]. **Pas de
constructeur** : on initialise les attributs à leur déclaration.

## Courts — valider la compréhension

### 1 — Fermer la structure

> [!abstract] Objectifs
> passer de `struct` à `class`, constater ce qui casse, et n'ouvrir que le nécessaire

Partir de ce code, qui compile :

```cpp
struct Monstre
{
    std::string nom = "Gobelin";
    int pointsDeVie = 30;
    int pointsDeVieMax = 30;
};

Monstre g;
std::println("{} : {}/{}", g.nom, g.pointsDeVie, g.pointsDeVieMax);
```

1. Remplacer `struct` par `class`, et recompiler **sans rien changer d'autre**.
2. Recopier le message d'erreur. Combien de lignes cessent de compiler, et pourquoi ?
3. Faire recompiler le programme en ajoutant le **strict minimum** de méthodes publiques.
4. Combien en avez-vous ajouté ? Auriez-vous pu n'en écrire qu'**une seule** ?

> [!tip] La bonne réponse à la question 4
> Une seule méthode `afficherFiche()` suffit, et c'est la meilleure : l'extérieur voulait
> *afficher le monstre*, pas *lire trois champs*. Trois accesseurs rouvrent ce que `class`
> venait de fermer.

### 2 — Des points de vie toujours valides

> [!abstract] Objectifs
> faire tenir une règle par l'objet, et prouver qu'elle tient

1. Ajouter `void subirDegats(int degats)` : la vie ne descend jamais sous **0**.
2. Ajouter `void soigner(int soin)` : la vie ne monte jamais au-dessus du **maximum**.
3. Ajouter `bool estVivant() const`.
4. Dans le `main`, enchaîner : 30 dégâts, puis **9999** dégâts, puis **9999** soins.
5. Le compteur ne doit être accessible qu'en **lecture**, et seulement si c'est nécessaire.

```text
Gobelin : 30/30 pv
Gobelin : 0/30 pv       (après 9999 dégâts, et non -9969)
vivant ? false
Gobelin : 30/30 pv      (après 9999 soins, et non 10029)
```

> [!tip] Les deux bornes
> `std::max(0, vie - degats)` et `std::min(vieMax, vie + soin)`, dans `<algorithm>`. Écrites
> **une fois**, dans la méthode — c'est tout l'intérêt.

### ~~3 — Le même code, deux mots-clés~~
~~Écrire la même chose en `struct` puis en `class` sans autre modification, et dire précisément quelle ligne cesse de compiler et pourquoi.~~

### 4 — De la fonction libre à la méthode

> [!abstract] Objectifs
> voir ce que la méthode gagne par rapport à la fonction libre, et ce qu'elle perd

La fonction suivante existait avant la classe :

```cpp
void afficherFiche(const Monstre& m)
{
    std::println("{} : {}/{} pv", m.nom, m.pointsDeVie, m.pointsDeVieMax);
}
```

1. La transformer en **méthode** de `Monstre`.
2. Quel paramètre disparaît de la signature ? Où est-il passé ?
3. Pourquoi la méthode peut-elle être marquée `const`, et qu'est-ce que ça promet ?
4. La fonction libre pouvait vivre dans un autre fichier, écrite par quelqu'un d'autre. La
   méthode, non. Nommez un cas où la fonction libre reste le bon choix.

> [!tip] Question 4
> Une fonction qui concerne **deux** objets de même niveau, ou qui n'appartient à personne :
> `bool memeEspece(const Monstre& a, const Monstre& b)`. En faire une méthode de `a`
> donnerait un faux air d'asymétrie.

## Complet — reprendre toute la séance

### 5 — La classe `Joueur`

> [!abstract] Objectifs
> cinq règles du jeu, cinq méthodes, zéro attribut public — dans un projet où le reste est
> déjà écrit

**Un projet companion est fourni.** Le menu de commandes fonctionne déjà : vous ne touchez
qu'à **`joueur.h`**.

> Dossier : `01 courses/companion projects/C++/GPR-CF-POO-02 - Classes et visibilité/`
> — ouvrir le `CMakeLists.txt` dans CLion, ou `cmake -S . -B build && cmake --build build`.

| Fichier | Ce que vous en faites |
|---|---|
| `Exercice_5/main.cpp` | **Rien.** Il lit une commande et appelle une méthode |
| `Exercice_5/joueur.h` | **Tout.** Six `// TODO`, un par règle |

Le projet compile et tourne tel quel : le menu s'affiche, et **toutes les actions sont
refusées**. C'est le point de départ.

| Méthode | La règle à tenir |
|---|---|
| `courir()` | coûte 10 d'endurance, refuse si elle manque, ne descend jamais sous 0 |
| `seReposer()` | remonte l'endurance au maximum, jamais au-delà |
| `ouvrirPorte()` | consomme une clé, refuse s'il n'en reste pas |
| `acheter(prix)` | consomme l'or, refuse si l'or manque |
| `subirDegats(d)` | garde la vie entre 0 et le maximum |
| `estVivant()` | vrai tant qu'il reste de la vie |

**Le test de recette** — enchaîner ces commandes et vérifier chaque ligne :

```text
c c c c c c    l'endurance tombe à 0, puis « Trop fatigue pour courir. »
r              elle remonte à 50, pas à 60
o o o          deux portes s'ouvrent, la troisième dit « Pas de cle. »
a a            une potion achetée (30 → 5 d'or), la seconde refusée
p p p p        la vie descend 70, 40, 10, 0 — jamais négative, et la partie s'arrête
```

> [!check] Ce qu'on vérifiera
> - **Aucun attribut public.** `main.cpp` ne sait pas qu'une course coûte 10, ni qu'il reste
>   deux clés : il ne connaît que des méthodes.
> - Si vous vous surprenez à vouloir écrire `joueur.endurance_ = …` depuis le menu, c'est
>   qu'une méthode manque — pas que `private` gêne.
> - `main.cpp` n'est pas modifié. Si votre code ne compile qu'en le touchant, l'interface
>   n'est pas la bonne.

## Difficile — se projeter

### 6 — L'inventaire qui ne peut pas mentir

> [!abstract] Objectifs
> tenir **quatre** garanties à la fois, et démontrer qu'aucun code extérieur ne peut les
> violer

Une classe `Inventaire` de **huit emplacements**, avec un **poids maximum**. Quoi qu'il
arrive, et quel que soit l'ordre des appels :

1. aucune quantité négative ;
2. aucun emplacement fantôme (une quantité de 0 libère l'emplacement) ;
3. le poids total ne dépasse jamais le maximum ;
4. deux objets identiques s'empilent au lieu d'occuper deux emplacements.

**L'interface** : `ajouter(objet, quantite)`, `retirer(objet, quantite)`,
`deplacer(de, vers)`, `echanger(a, b)`. Chacune dit si elle a réussi.

**Le rendu attendu n'est pas le jeu, c'est la preuve** : écrire une liste de tests qui
*tentent* de violer chacune des quatre garanties — retirer plus qu'on n'a, ajouter au-delà
du poids, déplacer vers un emplacement occupé, échanger un emplacement vide — et montrer
que chacun échoue proprement. Puis expliquer, en trois lignes, pourquoi un code extérieur
ne peut pas y arriver autrement.

> [!tip] Le mot juste
> Ces quatre garanties s'appellent des **invariants** : ce qui est vrai avant l'appel, et
> encore vrai après. Une classe bien faite, c'est un invariant et les méthodes qui le
> préservent.
