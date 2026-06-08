
# Get informations from tilemap
## multi dimensionnal span, 
### `std::mdspan` c'est quoi ?

- **Quoi** (C++23) : une **vue** multidimensionnelle, **non-propriétaire**,
  posée sur un buffer **1D contigu**. Un `span` à N dimensions. Zéro copie.
- **Comment** :
  - construite depuis un pointeur + des *extents* : `std::mdspan(data, nx, ny)` ;
  - indexée `tilemap[x, y]` (subscript multi-args C++23) ;
  - `extent(0)`/`extent(1)` = dimensions ; *layout-right* par défaut ⇒
    dernière dimension la plus rapide → index plat `x*height + y` ;
  - `dextents<size_t,2>` = dimensions connues **à l'exécution**.

### 3. `std::mdspan` — pourquoi ici

- **Découple** l'algo du conteneur réel : `vector`, `array`, buffer GPU…
  l'algo ne voit qu'« une grille 2D indexable ».
- **Zéro copie / zéro coût** d'abstraction.
### Comment ça marche ?

Snippet de syntaxe, lien vers le companion 
### Exercice
1. déclarer une nouvelle lbraiire astar.h, une fonction void getPath qui accepte un mdspan, une position de depart, une positin d'arrivee et renvoie un std vector de vector2i
2. tester la présence des 2 posi.tons départ et arrivee dans le md span
3. renvoyer un vector avec les 2 positions, en cas d'erreur, vecteur vide

# Structure Node astar

## Structure complete

```cpp
struct Node {
 int f() = return g + h;
 int g;
 int h;
 Vec2i pos;
 Vec2i came_from;
 bool operator<(const Node& o) const { return f > o.f;} 
 }; // min-heap !
```

## fixing neighbours

```cpp
static constexpr std::array neighbor_dirs{ {-1,0},{0,1},{1,0},{0,-1} };
```

## fixing heuristics

### Why manhattan distance over euclidean distance?
- No sqroot
- Same heuristic comparison usage

### 1. Manhattan vs Euclidienne

```cpp
auto manhattan = [](Vec2i a, Vec2i b){ return |a.x-b.x| + |a.y-b.y|; };
```

- Grille **4-connexe** ⇒ Manhattan = distance **exacte** sans obstacle :
  heuristique la **mieux informée**, **entière**, **sans `sqrt`**.
- Euclidienne (`√(dx²+dy²)`) reste admissible mais **sous-estime** ⇒
  A\* explore **plus de nœuds** pour le même résultat.
- Diagonales un jour ? → passer à **octile**, pas Euclidienne.

### two "lists"
#### Open list
```cpp
std::priority_queue<Node> open_list;
```

[explain what is a priotity queue]

#### Visited
```cpp
std::vector<int8_t> visited(total, 0);
```

Note: Explain why store the index

More lists
<iframe src="https://link.excalidraw.com/readonly/Hc6zLD4Nztvhp59sgza4?darkMode=true" width="100%" height="100%" style="border: none;"></iframe>

## Heart of astar : Main loop

### La boucle principale

```cpp
while (!open_list.empty()) {
  const auto current = open_list.top(); open_list.pop();
  if (current.pos == end_pos) { /* reconstruction → return path */ }

  const auto cur_idx = to_index(current.pos);
  if (visited[cur_idx]) continue;          // déjà traité
  visited[cur_idx] = 1;

  for (const auto& dir : neighbor_dirs) {  // 4 voisins
    const auto n = current.pos + dir;
    if (/* hors grille */ || visited[n_idx] || !tilemap[n.x,n.y].IsWalkable())
      continue;
    const int tentative_g = g_cost[cur_idx] + 1;   // arête = 1
    if (tentative_g < g_cost[n_idx]) {             // détente (relaxation)
      g_cost[n_idx]  = tentative_g;
      came_from[n_idx] = cur_idx;
      open_list.push({tentative_g + manhattan(n, end_pos), n});
    }
  }
}
return std::unexpected(PathError::kNoPathFound);
```



---

### La reconstruction du chemin

```cpp
if (current.pos == end_pos) {
  std::vector<maths::Vec2i> path;
  maths::Vec2i trace = end_pos;
  while (trace != start_pos) {
    path.push_back(trace);
    const auto idx = came_from[to_index(trace)];
    trace = { idx / height, idx % height };   // index plat → (x, y)
  }
  path.push_back(start_pos);
  std::ranges::reverse(path);                 // but→départ → départ→but
  return path;
}
```

- `came_from` mémorise « d'où je viens » → on **remonte** la chaîne.
- On reconstruit à l'envers, puis on **inverse**.

### Exercice implementation astar pas a pas


