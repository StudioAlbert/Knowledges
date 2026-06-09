---
theme: white
css:
- _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# A\* — Pathfinding en C++ moderne
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Cours · théorie + lecture de code + optimisations</small>

<small style="color:#fff;">Codebase de référence : `core::ai::pathfinding::FindPath` (branche <code>naive</code>)</small>

Note:
On part de la théorie A*, puis on lit *ligne par ligne* l'implémentation
réelle du projet CityBuilder, et on finit par les pistes d'optimisation.
Les étudiants travaillent sur la branche 925 (pas encore d'A*) : ce cours
leur donne la cible à atteindre.

---
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->
## Sources

<div style="color:#fff;">

Code runnable du cours (sous-modules `git`) :

- 🔗 [github.com/StudioAlbert/cpp_astar_course_companion](https://github.com/StudioAlbert/cpp_astar_course_companion)

Inclus localement :

- `companions/cpp_astar_course_companion/` — exemples par slide (Partie 2)
- `companions/cpp_astar_course_companion/STEP_BY_STEP.md` — guide d'implémentation

</div>

---
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->
## Déroulé

<div style="color:#fff;">

- **Partie 1** — Qu'est-ce que A\* ? *(théorie)*
- **Partie 2** — Construire A\* à la main *(pas à pas, code)*
  - 2.1 Le contrat (signature, garde-fous, `std::expected`)
  - 2.2 `std::mdspan` : la grille sans copie
  - 2.3 Le `Node` et la file de priorité
  - 2.4 Voisins & heuristique (Manhattan)
  - 2.5 La boucle principale
  - 2.6 Reconstruire le chemin
  - 2.7 À vous — implémentation pas à pas
- **Partie 3** — Optimisations possibles *(roadmap)*

</div>

---

## Partie 1
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->
### Qu'est-ce que A\* ?

---

### Le problème

- Trouver le **plus court chemin** entre deux cellules d'une grille.
- **Nœuds** = cellules ; **arêtes** = déplacements vers un voisin *walkable*.
- Une grille = un graphe implicite sans liaisonsa, on 
  *calcule* les voisins à la volée.

→ A\* = Dijkstra **guidé** par une estimation de la distance restante.

---

### Le cœur : `f = g + h`

- **g** = coût **réel** depuis le départ jusqu'à la cellule.
- **h** = **heuristique** : estimation du coût restant jusqu'au but.
- **f = g + h** = coût total estimé d'un chemin passant par cette cellule.

A\* explore **toujours en premier** la cellule de plus petit `f`.

---

### Deux ensembles

- **Open set** (*frontière*) : cellules découvertes, pas encore traitées.
  - Implémenté par une **file de priorité** (min-`f`).
- **Closed / visited set** : cellules déjà traitées (on n'y revient pas).

Boucle : sortir le min-`f` de l'open set → si c'est le but, fini → sinon le
marquer *visited* et **edge-relax** ses voisins.

> 📖 **Edge relaxation** — pour chaque voisin, *si* passer par le nœud
> courant donne un meilleur `g`, *alors* on met à jour son `g`, on note
> « d'où je viens » (`came_from`), et on le (re)pousse dans l'open set.
> C'est l'étape standard de Dijkstra / Bellman-Ford / A\*.

---

### Heuristique : admissible & cohérente

- **Admissible** : `h` ne **surestime jamais** le coût réel restant.
  - ⇒ A\* renvoie le chemin **optimal**.
- **Cohérente (monotone)** : `h(a) ≤ coût(a,b) + h(b)`.
  - ⇒ une cellule n'est jamais ré-ouverte → un simple *visited* suffit.

`h = 0` ⇒ admissible mais inutile : A\* **dégénère en Dijkstra**.

---

### A\* entre Dijkstra et glouton

| Algo | Utilise `g` | Utilise `h` | Optimal ? |
|------|:-----------:|:-----------:|:---------:|
| **Dijkstra** | ✅ | ❌ (h=0) | ✅ mais explore large |
| **Glouton (best-first)** | ❌ | ✅ | ❌ rapide mais peut rater |
| **A\*** | ✅ | ✅ | ✅ si `h` admissible |

A\* = le bon compromis : optimal **et** dirigé vers le but.

---

### Connectivité 4 vs 8

- **4-connexe** (N/S/E/O) → heuristique **Manhattan** `|dx| + |dy|`.
- **8-connexe** (+ diagonales) → **octile** / **Chebyshev**.
- ⚠️ Manhattan sur une grille 8-connexe **surestime** ⇒ plus admissible !

L'heuristique doit **coller au modèle de déplacement**.

---

### Zoom : l'heuristique **octile**

Sur une grille 8-connexe, un pas diagonal vaut **√2 ≈ 1.414** (ou **14** si
on encode un pas droit à **10**). Octile = distance **exacte** sans
obstacle : autant de diagonales que possible, puis des pas droits.

```cpp
// Coûts entiers : pas droit = 10, pas diagonal = 14.
int octile(Vec2i a, Vec2i b) {
  const int dx = std::abs(a.x - b.x);
  const int dy = std::abs(a.y - b.y);
  return 10 * (dx + dy) - 6 * std::min(dx, dy);   // 10·max + 14·min, factorisé
}
```

| Modèle | Heuristique | Coût diag | Cas d'usage |
|---|---|---|---|
| 4-connexe | **Manhattan** | — | grille sans diagonale |
| 8-connexe, diag = 1 | **Chebyshev** | 1 | rare (« roi d'échecs ») |
| 8-connexe, diag = √2 | **Octile** | √2 | cas standard pathfinding |
| n'importe quoi | **Euclidienne** | √2 | admissible mais sous-informée |

> 📖 **Règle de poche** — quand `h(droite) == coût_droite` *et* `h(diag) ==
> coût_diag` sans obstacle, l'heuristique est **parfaitement informée**
> pour ce modèle. Manhattan le fait en 4-connexe, octile en 8-connexe.

---
<!-- .slide: data-background-iframe="widgets/_widgets/astar_widgets.html" data-background-interactive -->
### Démo interactive

Note:
Slide en plein écran sur le widget `widgets/_widgets/astar_widgets.html`.
Dessiner des murs, placer A/B, lancer en pas-à-pas. Montrer :
- l'expansion de la frontière (open) vs visited,
- les valeurs g/h/f par cellule,
- le mode Dijkstra (h=0) qui explore beaucoup plus large,
- l'effet du toggle diagonale sur le chemin.
Fallback si l'iframe ne charge pas : ouvrir widgets/_widgets/astar_widgets.html.

---

## Partie 2
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->
### Construire A\* à la main

<small style="color:#fff;">On le re-construit pas à pas : contrat → structures → voisins → boucle → chemin.</small>

<small style="color:#fff;">Companion : <code>companions/cpp_astar_course_companion/</code></small>

Note:
Partie 2 = un atelier. À chaque étape on ajoute une brique, et chaque
brique a un mini-projet runnable dans le companion. À la fin de la
partie, on a tout vu — la 2.7 demande de tout assembler soi-même.

---

## 2.1 — Le contrat
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Que reçoit `FindPath`, que rend-il ?</small>

---

### Signature visée

```cpp
enum class PathError {
  kStartOutOfBounds, kEndOutOfBounds,
  kStartNotWalkable, kEndNotWalkable,
  kNoPathFound,
};

std::expected<std::vector<Vec2i>, PathError>
FindPath(std::mdspan<const Cell, std::dextents<std::size_t, 2>> grid,
         Vec2i start, Vec2i end);
```

- **Entrée** : une *vue* sur la grille + deux positions cellules.
- **Sortie** : un chemin **ou** une erreur typée.

---

### Garde-fous → `std::expected`

```cpp
if (!InBounds(grid, start)) return std::unexpected(PathError::kStartOutOfBounds);
if (!InBounds(grid, end))   return std::unexpected(PathError::kEndOutOfBounds);
if (!grid[start.x, start.y].walkable)
  return std::unexpected(PathError::kStartNotWalkable);
if (!grid[end.x, end.y].walkable)
  return std::unexpected(PathError::kEndNotWalkable);
```

- 4 garde-fous **avant** la recherche : bornes + cases *walkable*.
- Chaque échec a un **code distinct** → l'appelant sait *pourquoi*.
- `std::expected<T, E>` = « valeur **ou** erreur », sans exception (cousin de `Result` en Rust).

---

## 2.2 — `std::mdspan` : la grille sans copie
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Une vue multidim posée sur un buffer 1D contigu.</small>

---

### `std::mdspan` — quoi & comment

- **Quoi** (C++23) : une **vue** multidimensionnelle, **non-propriétaire**,
  posée sur un buffer **1D contigu**. Un `span` à N dimensions. **Zéro copie**.
- **Comment** :
  - construite depuis pointeur + *extents* : `std::mdspan(data, nx, ny)` ;
  - indexée `grid[x, y]` (subscript multi-args C++23) ;
  - `extent(0)` / `extent(1)` = dimensions ;
  - *layout-right* par défaut ⇒ index plat = `x * extent(1) + y` ;
  - `dextents<size_t, 2>` = dimensions connues **à l'exécution**.

<small>📁 Companion : `01_mdspan/01_basics`</small>

---

### `std::mdspan` — pourquoi ici

- **Découple** l'algo du conteneur réel : `vector`, `array`, buffer GPU…
  l'algo ne voit qu'« une grille 2D indexable ».
- **Zéro copie / zéro coût** d'abstraction.

<small>📁 Companion : `01_mdspan/02_tilemap`</small>

---

## 2.3 — Le `Node` et la file de priorité
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Ce qu'on met dans l'open list, et comment on en sort le minimum.</small>

---

### Le `Node`

```cpp
struct Node {
  int   g;        // coût réel depuis le départ
  int   h;        // heuristique vers l'arrivée
  Vec2i pos;
  int f() const { return g + h; }
  bool operator<(const Node& o) const { return f() > o.f(); }  // min-heap !
};
```

- `operator<` **inversé** : `std::priority_queue` est un *max*-heap par défaut.
  On en fait un **min-`f`** en disant « plus grand `f` = moins prioritaire ».

---

### L'open list

```cpp
std::priority_queue<Node> open_list;
```

- `push` / `pop` en **O(log n)**, accès au minimum en **O(1)**.
- Une cellule peut être **redécouverte** avec un meilleur `g` → des doublons
  existent dans l'open list. On les filtre **à la sortie** avec `visited`.

---

### Les buffers plats

```cpp
const auto W = grid.extent(0), H = grid.extent(1);
auto idx = [H](Vec2i p){ return p.x * H + p.y; };

std::vector<int8_t> visited  (W*H, 0);
std::vector<int>    g_cost   (W*H, INT_MAX);
std::vector<size_t> came_from(W*H, SIZE_MAX);
```

- Indexés par cellule → lecture/écriture **O(1)**.
- Contigus et libérés **en bloc** : cache-friendly, façon arène.

<small>📁 Companion : `02_node_pq`</small>

---
<!-- .slide: data-background-iframe="https://link.excalidraw.com/readonly/Hc6zLD4Nztvhp59sgza4?darkMode=true" data-background-interactive -->
### Open list, visited, `g_cost`, `came_from`

Note:
Slide plein écran sur le schéma Excalidraw. Pointer les 4 tableaux et
montrer comment ils communiquent : l'open list (priority_queue) tient
la frontière, `visited` la coupe (un cell traité n'y revient pas),
`g_cost` mémorise le meilleur coût connu, `came_from` mémorise le
prédécesseur pour la reconstruction.
Fallback si l'iframe ne charge pas : ouvrir le lien Excalidraw directement.

---

## 2.4 — Voisins & heuristique
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Définir le déplacement, choisir `h`.</small>

---

### Les 4 voisins (4-connexe)

```cpp
static constexpr std::array<Vec2i, 4> neighbor_dirs{{
  {-1, 0}, {1, 0}, {0, -1}, {0, 1}
}};
```

- 4-connexe : N / S / E / O. Pas de diagonale dans cette implé.
- `constexpr` → table figée à la compilation, zéro coût runtime.

---

### Manhattan plutôt qu'Euclidienne

```cpp
auto manhattan = [](Vec2i a, Vec2i b){
  return std::abs(a.x - b.x) + std::abs(a.y - b.y);
};
```

- Grille **4-connexe** ⇒ Manhattan = distance **exacte** sans obstacle :
  heuristique la **mieux informée**, **entière**, **sans `sqrt`**.
- Euclidienne (`√(dx² + dy²)`) reste admissible mais **sous-estime** ⇒
  A\* explore **plus de nœuds** pour le même résultat.
- Diagonales un jour ? → passer à **octile**, pas Euclidienne.

<small>📁 Companion : `03_neighbors_heuristic`</small>

---

## 2.5 — La boucle principale
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Pop min-`f`, marquer, edge-relax, recommencer.</small>

---

### Initialisation

```cpp
g_cost[idx(start)] = 0;
open_list.push({ /*g=*/0, /*h=*/manhattan(start, end), start });
```

- Le départ entre dans l'open list avec `g = 0`.
- Tout le reste hérite des valeurs sentinelles (`INT_MAX`, `SIZE_MAX`).

---

### Le cœur

```cpp
while (!open_list.empty()) {
  const auto cur = open_list.top(); open_list.pop();
  if (cur.pos == end) { /* reconstruction → return path */ }

  const auto i = idx(cur.pos);
  if (visited[i]) continue;                       // doublon dans l'open list
  visited[i] = 1;

  for (const auto& d : neighbor_dirs) {            // 4 voisins
    const Vec2i n = { cur.pos.x + d.x, cur.pos.y + d.y };
    if (!InBounds(grid, n) || visited[idx(n)] || !grid[n.x, n.y].walkable)
      continue;
    const int tentative_g = g_cost[i] + 1;         // arête = 1
    if (tentative_g < g_cost[idx(n)]) {            // edge relaxation
      g_cost   [idx(n)] = tentative_g;
      came_from[idx(n)] = i;
      open_list.push({ tentative_g, manhattan(n, end), n });
    }
  }
}
return std::unexpected(PathError::kNoPathFound);
```

---

### Lecture pas à pas

- **Pop** : on prend la cellule de plus petit `f`.
- **But atteint ?** → on reconstruit le chemin et on rend.
- **Doublon ?** → si déjà traitée, on saute (heuristique cohérente ⇒ un `visited` suffit).
- **Edge-relax les voisins** : meilleur `g` trouvé ⇒ on note **d'où on vient** et on **push** le voisin.

<small>📁 Companion : `04_main_loop`</small>

---

## 2.6 — Reconstruire le chemin
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<small style="color:#fff;">Remonter `came_from`, puis inverser.</small>

---

### Le code

```cpp
if (cur.pos == end) {
  std::vector<Vec2i> path;
  Vec2i trace = end;
  while (trace != start) {
    path.push_back(trace);
    const auto p = came_from[idx(trace)];
    trace = { static_cast<int>(p / H), static_cast<int>(p % H) };  // index plat → (x, y)
  }
  path.push_back(start);
  std::ranges::reverse(path);                       // but→départ → départ→but
  return path;
}
```

- `came_from` mémorise « d'où je viens » → on **remonte** la chaîne.
- On construit le chemin **à l'envers**, puis on **inverse**.
- Conversion index en `(x, y)` 
	- `index / H` et `index % H`

<small>📁 Companion : `05_reconstruction`</small>

---

## 2.7 — À vous
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Reconstruisez `FindPath` pas à pas, en **6 étapes** :

1. Contrat & garde-fous
2. Structures de données
3. Voisins & heuristique
4. Initialisation
5. Boucle principale
6. Reconstruction

Chaque étape a un **objectif** et un **critère d'acceptation**.

📘 Guide complet : <code>companions/cpp_astar_course_companion/STEP_BY_STEP.md</code>

</div>

Note:
Le but n'est pas de copier les snippets de la partie 2 — c'est de
décider à chaque étape *ce que le code doit faire* avant de l'écrire.
Le critère d'acceptation de chaque étape sert de petit test mental
(ou de vrai test unitaire si on a le temps).

---

## Partie 3
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->
### Optimisations possibles

<small style="color:#fff;">Classées par effort / gain.</small>


---

### Mutualisation — la nuance `mdspan`

- ⚠️ Le **graphe est déjà partagé sans copie** grâce au `mdspan` :
  `FindPath` travaille sur une **vue**.
- Donc l'optim **n'est PAS** « éviter de recopier la grille » — c'est **acquis**.
- Ce qui n'est **pas** mutualisé : les **buffers de recherche par appel**.
- → un seul jeu de buffers **réutilisé** par N NPC qui cherchent à tour de rôle.

---

### Pistes algorithmiques

- **Tie-breaking** : départager les `f` égaux par le plus petit `h` → moins de
  cellules explorées.
- **JPS** (*Jump Point Search*) sur grille uniforme : saute les cellules
  symétriques.
- **Hiérarchique** (clusters / portails) pour les grandes cartes.
- **Cache de chemins** + **requêtes par lots** (plusieurs NPC, même zone).

