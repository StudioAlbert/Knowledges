# Exercices — GPR-CF-POO-05 — Static et surcharge d'opérateur

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-05 - Static et surcharge d'opérateur|GPR-CF-POO-05 - Static et surcharge d'opérateur]]

> [!todo] Overview à valider
> Chaque exercice est décrit en deux ou trois lignes. Les énoncés complets, les squelettes
> `main.cpp` et les corrigés viendront après validation de ces pistes.

## A / Courts — valider la compréhension

--------------------------------------------------------------------------
### Static
### 1 — Combien d'ennemis vivants
Un compteur `static` incrémenté à la construction, décrémenté à la destruction, et une méthode `static` qui le renvoie. Faire naître et mourir des ennemis dans des portées imbriquées et vérifier que le compte revient à zéro.

### 2 — L'identifiant unique
Chaque entité reçoit à sa naissance un numéro jamais réutilisé, distribué par un `static`. Montrer que deux entités n'ont jamais le même, même après des destructions.

-----------------------------------------------
### Surcharge d'opérateur
### 3 — `Vector2` qui s'additionne
#### 1 - Créer une structure `Vector2` 
```c++
struct Vector2{
	int x,y;
}
```

#### 2 - Ajouter les opérateurs : 
- l'addition, la soustraction, l'increment, le decrement entre vecteurs 
- la multiplication par un scalaire des deux côtés, 
- vérifier que le calcul d'un déplacement tient sur une ligne lisible 
```c++
position += 2 * vitesse;
```

### 4 — Trier les scores
Donner les opérateurs `==` et `<` à une classe `Score` (nom, points, temps),
Trier un tableau de dix scores et chercher un score précis sans écrire de comparaison à la main.

## B / Complet — reprendre toute la séance
-----------------------------------
### 5 — Le `Vector2` du projet
La classe complète : 
- constructeurs, 
- opérateurs arithmétiques et de comparaison, 
- norme et normalisation, 
- plus des constantes `static` pour le vecteur nul et les axes.
  
La faire servir dans une petite simulation de trois projectiles sur vingt images, où aucune ligne de calcul n'appelle de fonction nommée.

