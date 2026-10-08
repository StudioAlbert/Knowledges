# Exercices — TC-FT-GVM-02 — Produits scalaire et vectoriel

> Cours associé : [[01 courses/slides/Theory/TC-FT-GVM-02 - Produits scalaire et vectoriel|TC-FT-GVM-02 - Produits scalaire et vectoriel]]

Le **préambule** (A et B) remet en place la boîte à outils de
[[01 courses/slides/Theory/TC-FT-GVM-01 - Vecteurs et repères|GVM-01]] : à faire avant le
reste, au clavier. Les exercices 1 et 2 se font sur papier, le 7 et le 8 en C++.

## Préambule — la boîte à outils

### A — Reconstruire `Vector2`

> [!abstract] Objectifs
> réécrire la structure et les fonctions de GVM-01, qui serviront dans tous les exercices

Repartir de zéro, dans un fichier `vecteur.h` que les exercices suivants incluront.

```cpp
struct Vector2 { float x, y; };

Vector2 Ajouter(Vector2 a, Vector2 b);
Vector2 Soustraire(Vector2 a, Vector2 b);
Vector2 Multiplier(Vector2 v, float k);
float   Norme(Vector2 v);
Vector2 Normaliser(Vector2 v);
```

1. Écrire les cinq fonctions. Aucune ne dépasse deux lignes.
2. `Normaliser` doit rendre `{0, 0}` sur un vecteur nul, sans diviser par zéro.
3. Vérifier dans un `main` : `Norme({3, 4})` vaut `5`, `Normaliser({0, 7})` vaut `{0, 1}`,
   et `Normaliser({0, 0})` ne produit pas de `NaN`.

> [!tip] Tester un `NaN`
> `std::isnan(v.x)` répond `true` si le calcul a dérapé. Un `NaN` n'est **jamais** égal à
> lui-même : `v.x == v.x` est faux. C'est le test du pauvre, et il marche.

### B — L'ennemi est-il à portée ?

> [!abstract] Objectifs
> `B − A`, norme, comparaison à une portée — et la version qui évite la racine carrée

Le garde est en **(0, 0)**, sa portée d'attaque vaut **5**.

1. Écrire `bool EstAPortee(Vector2 garde, Vector2 ennemi, float portee)`.
2. Tester sur **(3, 4)**, **(5, 1)**, **(−4, −2)** et **(0, 5)** : lesquels sont à portée ?
3. Réécrire la fonction **sans `std::sqrt`**, en comparant les carrés.
4. Pourquoi les deux versions donnent-elles toujours la même réponse ?

```text
(3, 4)   distance 5      → à portée (pile à la limite)
(5, 1)   distance 5,10   → hors de portée
(−4, −2) distance 4,47   → à portée
(0, 5)   distance 5      → à portée

sans racine :  dx² + dy² ≤ portee²       25 ≤ 25, 26 ≤ 25, 20 ≤ 25, 25 ≤ 25
```

> [!tip] Pourquoi comparer les carrés
> La racine carrée est monotone sur les positifs : si `a ≤ b` alors `√a ≤ √b`, et
> réciproquement. Comparer les carrés donne donc **exactement** la même réponse, sans payer
> le `sqrt`. C'est le premier réflexe d'optimisation de la géométrie de jeu.

## Courts — valider la compréhension

### 1 — Devant ou derrière

> [!abstract] Objectifs
> décider par le **seul signe** du produit scalaire, sans calculer d'angle

Le garde est en **(0, 0)** et regarde dans la direction **(1, 0)**. Pour chacune des cinq
positions, calculer `regard · versCible` et conclure — sans normaliser, sans `acos`.

| Cible | `regard · versCible` | Devant / côté / derrière |
| --- | --- | --- |
| (4, 2) | | |
| (−3, 1) | | |
| (0, 5) | | |
| (2, −6) | | |
| (−1, −1) | | |

```text
(4, 2)   → 1×4 + 0×2 = 4    > 0  devant
(−3, 1)  → 1×(−3) + 0×1 = −3 < 0  derrière
(0, 5)   → 1×0 + 0×5 = 0     = 0  exactement sur le côté
(2, −6)  → 2                 > 0  devant
(−1, −1) → −1                < 0  derrière
```

Pourquoi la composante `y` de la cible n'apparaît-elle jamais dans le résultat ?

### 2 — Le cône de vision

> [!abstract] Objectifs
> comparer des **cosinus** et non des angles, et comprendre pourquoi

Le garde regarde toujours vers **(1, 0)**. Son cône de vision fait **60° de demi-angle**.

1. Calculer `cos 60°`. C'est la **limite**, à calculer une seule fois.
2. Pour chaque cible, normaliser `versCible`, puis comparer `regard · direction` à la limite.
3. Conclure pour **(3, 0)**, **(2, 3)**, **(1, 3)** et **(−2, 1)**.
4. Expliquer en une phrase pourquoi on ne convertit pas en degrés avec `acos`.

```text
limite = cos 60° = 0,5

(3, 0)   direction (1 ; 0)         produit 1,00  ≥ 0,5  → dans le cône
(2, 3)   direction (0,55 ; 0,83)   produit 0,55  ≥ 0,5  → dans le cône, de justesse
(1, 3)   direction (0,32 ; 0,95)   produit 0,32  < 0,5  → dehors
(−2, 1)  direction (−0,89 ; 0,45)  produit −0,89 < 0,5  → derrière, donc dehors
```

> [!tip] Le sens de la comparaison
> Le cosinus **décroît** quand l'angle grandit : un angle plus petit donne un cosinus plus
> grand. D'où le `≥` alors qu'on teste « l'angle est-il plus petit que 60° ».

## Comprendre la séance

### 3 — Les trois opérations à la main

> [!abstract] Objectifs
> écrire soi-même l'addition, la multiplication par un scalaire et le produit vectoriel,
> puis vérifier chaque propriété du cours sur des valeurs

Compléter `vecteur.h` du préambule avec les prototypes de la séance :

```cpp
Vector2 Ajouter(Vector2 a, Vector2 b);       // déjà fait en A
Vector2 Multiplier(Vector2 v, float k);      // déjà fait en A
float   Dot(Vector2 a, Vector2 b);           // produit scalaire
float   Cross(Vector2 a, Vector2 b);         // produit vectoriel, en 2D : un nombre
```

1. Écrire `Dot` et `Cross`. Chacune tient sur **une ligne**.
2. Avec `u = (3, 1)` et `v = (1, 2)`, afficher `Dot(u, v)` et `Cross(u, v)`.
3. Vérifier au programme, et dire ce que chaque ligne démontre :
   - `Dot(u, v)` et `Dot(v, u)` — que peut-on en conclure ?
   - `Cross(u, v)` et `Cross(v, u)` — et là ?
   - `Dot(u, Multiplier(v, 3))` comparé à `3 × Dot(u, v)`
   - `Cross(u, Multiplier(u, 2))` — pourquoi ce résultat était-il prévisible ?
4. Trouver **à la main** un vecteur `w` tel que `Dot(u, w) == 0`, puis le vérifier au
   programme. Combien y en a-t-il ?
5. Même question avec `Cross(u, w) == 0`.

> [!tip] Le lien entre les deux questions
> `Dot(u, w) = 0` dessine **une droite** de vecteurs perpendiculaires à `u` ;
> `Cross(u, w) = 0` dessine la droite des vecteurs **colinéaires** à `u`. Les deux droites
> sont perpendiculaires entre elles — et ensemble, elles couvrent tout le plan. C'est la
> décomposition u∥ / u⊥ (projection et composante orthogonale), vue sous un autre angle.

## Bilan formatif

### 4 — Le garde voit-il le joueur ?

> [!abstract] Objectifs
> enchaîner les trois tests de la séance — distance, angle, côté — sur une liste de cibles,
> et produire un verdict lisible

Bilan de séance, à terminer à la maison. Tout se fait avec `vecteur.h` des exercices A et 7.

**Les données**

```cpp
const Vector2 garde{0.0f, 0.0f};
const Vector2 regard = Normaliser({1.0f, 0.0f});
const float portee = 6.0f;
const float demiAngle = 45.0f * 3.14159265f / 180.0f;

const Vector2 cibles[]{
    {3, 1}, {2, -2}, {-4, 1}, {8, 0}, {0.5f, 5}, {5, 0}
};
```

**Étapes — dans cet ordre, et pas un autre**

1. Calculer `cosLimite = std::cos(demiAngle)` **une seule fois**, avant la boucle.
2. Pour chaque cible : `vers = cible − garde`, puis sa `distance`.
3. **Test de portée** : `distance <= portee`. Si c'est faux, inutile d'aller plus loin —
   afficher `trop loin` et passer à la suivante.
4. Normaliser `vers` en `direction`, puis **test d'angle** : `Dot(regard, direction) >= cosLimite`.
5. **Test de côté** : le signe de `Cross(regard, direction)` donne `gauche`, `droite` ou
   `devant`.
6. Afficher un tableau : la cible, sa distance, le cosinus obtenu, le côté, et le verdict.

```text
portee 6 , demi-angle 45 deg (cos 0.707)

cible            dist    cos    cote        verdict
(  3.0,  1.0)   3.16   0.95  gauche    VU
(  2.0, -2.0)   2.83   0.71  droite    VU
( -4.0,  1.0)   4.12  -0.97  gauche    hors du cone
(  8.0,  0.0)   8.00   1.00  devant    trop loin
(  0.5,  5.0)   5.02   0.10  gauche    hors du cone
(  5.0,  0.0)   5.00   1.00  devant    VU
```

**Puis répondre**

7. La cible **(2, −2)** donne un cosinus de **0,71** pour une limite de **0,707** : elle est
   à **45,0°**, pile sur le bord du cône. Que se passerait-il si le demi-angle était écrit
   `45.0f` en degrés et comparé directement à un angle calculé par `acos` ? Pourquoi
   l'ordre des tests de l'étape 3 protège-t-il aussi de ce genre d'ennui ?
8. Pourquoi normaliser `vers` **après** le test de portée, et pas avant ?
9. Le garde pivote et regarde maintenant vers **(0, 1)**. Sans relancer le programme, dire
   lesquelles des six cibles il voit.

> [!check] Grille d'auto-évaluation
> Cocher ce qui marche avant de rendre.
>
> | Je sais… | Vérification |
> |---|---|
> | calculer un produit scalaire | `Dot` tient sur une ligne, sans `sqrt` ni `acos` |
> | tester une portée sans racine | le test de l'étape 3 compare des carrés |
> | tester un cône par les cosinus | `cosLimite` est calculé **avant** la boucle, une fois |
> | lire le signe d'un produit vectoriel | `gauche` / `droite` / `devant` sont justes sur les six cibles |
> | protéger la normalisation | une cible posée **sur** le garde ne produit pas de `NaN` |
> | ordonner des tests du moins cher au plus cher | la distance d'abord, l'angle ensuite |
