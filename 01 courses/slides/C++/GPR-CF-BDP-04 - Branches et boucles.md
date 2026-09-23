---
title: GPR-CF-BDP-04 - Branches et boucles
type: slides
status: Backlog
subject: C++
duration_h: 1
bloc_gsda: Bases de la Programmation
theme: white
css:
  - 00 templates/css/sae_styles.css
slideNumber: true
transition: slide
width: 1280
height: 720
margin: 0
publish: true
---

# Branches et boucles
<!-- .slide: class="title" -->
## GPR-CF-BDP-04

<small>Et pourtant elle tourne</small>

---

## Objectifs

À la fin de la séance, vous savez :

- ce qu'est une **condition** et les outils du c++
- ce qu'est une boucle :
	- une boucle **tant que**
	- boucle **for**
- sortie prématurées : break, continue
- cas complexes et bonnes pratiques

**Prérequis :** variables, types de base et fonctions — [[01 courses/slides/C++/GPR-CF-BDP-03 - Fonctions|GPR-CF-BDP-03]].

---
## Prise de décisions

### un programme prend des décisions

#### Le code est il exact ?
#### La voiture est elle arretée ?

#### Le joueur est il en vie ?

#### Le jeu est-il lancé ?

#### La page est elle chargée ?
---
## Branching simple

<iframe src="https://link.excalidraw.com/readonly/tdPgjRKYn9twZWDAcK0Z" width="50%" height="50%" style="border: none;"></iframe>
---
## Branching complexe

<iframe src="https://link.excalidraw.com/readonly/oxy4C81r2vMnMTadQ5pD" width="50%" height="50%" style="border: none;"></iframe>
---
## if

si **cause** alors ***conséquence***

```cpp
if (pv <= 0)
{
    std::println("Game over");
}
```

---
## else

si **cause** alors ***consequence*** sinon ***tant pis***

```cpp
if (pv <= 0)
{
    std::println("Game over");
}
else
{
    std::println("Encore debout");
}
```

---
## else if

si cause alors consequence mais que 

```cpp
if (pv > 50)
{
    std::println("En forme");
}
else if (pv > 0)
{
    std::println("Blesse");
}
else
{
    std::println("Game over");
}
```

---
## switch

examen par valeur

```cpp
// Menu selon touche
switch (touche)
{
case 'z':
    std::println("Avancer");
    break;
case 's':
    std::println("Reculer");
    break;
default:
    std::println("Touche inconnue");
    break;
}
```

---
## while / do while

si je gagne, je joue

Pre / Post conditions

```cpp
// Pre conditions
int munitions = 0;
while (munitions > 0)
{
    std::println("Tir");
    munitions--;
}
```

```cpp
// Post conditions
int munitions = 0;
do
{
    std::println("Tir");
    munitions--;
} while (munitions > 0);
```

Note:
Même valeur de départ, deux comportements : le `while` n'affiche rien, le
`do … while` tire une fois avant de tester. La question à poser aux
étudiants : « combien de fois voulez-vous que le corps s'exécute **au
minimum** ? » — 0 fois → `while`, 1 fois → `do … while`.

---
## Exemple : Game loop

```cpp
do{
	if(key(ESC).isPressed){
		window.close();
	}
// Affichage du jeu
}while(window.isOpen());
```

est ce que je peux utiliser le while() ?

---

## for

### Syntaxe

for( On Commence;  On Continue ?; On avance)

```cpp
std::println("A l'endroit");
for (int i = 0; i <= 10; i++)
{
    std::println("{}", i);
}

std::println("A l'envers");
for (int i = 10; i >= 0; i--)
{
    std::println("{}", i);
}

std::println("c'est interdit");
for (;;)
{
    std::print(".");
}
```

---
## Qu'est ce que le vrai ?

```cpp
int pv = 42;
if (pv)
{
    std::println("vrai");
}

if (pv - 42)
{
    std::println("jamais");
}

const char* nom = "";
if (nom)
{
    std::println("toujours vrai");
}
```

Note:
Tout ce qui n'est pas `0` est vrai. Un `int`, un `char`, un pointeur :
la condition les convertit en `bool`. D'où le piège de la chaîne vide —
le pointeur existe, donc il est vrai, même si la chaîne ne contient rien.
Écrire la comparaison en entier (`if (pv != 0)`) rend l'intention visible.

---
## break

```cpp
// use case dans une boucle dowhile
int i = 0;
do
{
    if (i == 3)
    {
        break;
    }
    std::println("{}", i);
    i++;
} while (i < 10);
```

```cpp
// use case dans une boucle for
for (int i = 0; i < 10; i++)
{
    if (i == 3)
    {
        break;
    }
    std::println("{}", i);
}
```

---
## continue

```cpp
// use case dans une boucle dowhile
int i = 0;
do
{
    i++;
    if (i % 2 == 0)
    {
        continue;
    }
    std::println("{}", i);
} while (i < 10);
```

```cpp
// use case dans une boucle for
for (int i = 0; i < 10; i++)
{
    if (i % 2 == 0)
    {
        continue;
    }
    std::println("{}", i);
}
```

Note:
Dans le `for`, `continue` saute au `i++`. Dans le `do … while`, il saute
directement au test : si l'incrément était écrit **après** le `continue`,
la boucle ne se terminerait jamais. C'est la première boucle infinie que
les étudiants écrivent.

---

# Cas complexes et bonnes pratiques
<!-- .slide: class="title" -->

---
## Les sept pièges

1. `=` n'est pas `==`
2. les accolades ne sont pas optionnelles
3. `switch` : l'oubli du `break`
4. la boucle qui ne s'arrête jamais
5. `for` et `while` ne servent pas à la même chose
6. `break` ne sort que d'**une** boucle
7. comparer des flottants avec `==`

---
## 1. `=` n'est pas `==`

```cpp
if (pv = 0)
{
    std::println("Game over");
}
```

`pv = 0` **écrit** 0 dans `pv`, puis vaut 0 : la condition est toujours fausse, et les points de vie ont été effacés au passage.

```cpp
if (pv == 0)
{
    std::println("Game over");
}
```

Note:
Compiler avec les warnings activés (`-Wall` / `/W4`) : le compilateur
signale une affectation dans une condition. Certaines équipes écrivent
`if (0 == pv)` — la « condition Yoda » — pour transformer l'erreur en
erreur de compilation.

---
## 2. Les accolades ne sont pas optionnelles

```cpp
if (pv <= 0)
    std::println("Game over");
    std::println("Score final");
```

Seule la **première** ligne appartient au `if`. Le score s'affiche toujours : l'indentation ment.

```cpp
if (pv <= 0)
{
    std::println("Game over");
    std::println("Score final");
}
```

Note:
C'est le bug *goto fail* d'Apple en 2014, en une ligne. Règle de la
section : toujours des accolades, même pour une seule instruction.

---
## 3. `switch` : l'oubli du `break`

```cpp
switch (touche)
{
case 'z':
    std::println("Avancer");
case 's':
    std::println("Reculer");
}
```

`'z'` affiche **les deux** lignes : sans `break`, l'exécution continue dans le cas suivant.

- un `break` à la fin de chaque `case`
- `[[fallthrough]]` quand l'enchaînement est voulu
- un `default`, toujours

---
## 4. La boucle qui ne s'arrête jamais

```cpp
int munitions = 3;
while (munitions > 0)
{
    std::println("Tir");
}
```

Rien ne modifie `munitions` : la condition reste vraie pour toujours.

**Réflexe :** en écrivant le `while`, écrire immédiatement la ligne qui fait avancer la condition.

---
## 5. `for` et `while` ne servent pas à la même chose

```cpp
int i = 0;
while (i < 10)
{
    std::println("{}", i);
    i++;
}
```

Le nombre de tours est connu → c'est un `for`, et les trois parties tiennent sur une ligne.

```cpp
for (; pv > 0;)
{
    subir_degats();
}
```

Le nombre de tours dépend du jeu → c'est un `while`.

- **`for`** : je sais combien de fois
- **`while`** : je sais quand m'arrêter

---
## 6. `break` ne sort que d'une boucle

```cpp
for (int y = 0; y < 8; y++)
{
    for (int x = 0; x < 8; x++)
    {
        if (case_occupee(x, y))
        {
            break;
        }
    }
}
```

Le `break` quitte la boucle sur `x`. La boucle sur `y` continue.

- un drapeau : `bool trouve = false;` testé dans les deux conditions
- ou — mieux — extraire les deux boucles dans une fonction et `return`

---
## 7. Comparer des flottants avec `==`

```cpp
float t = 0.0f;
while (t != 1.0f)
{
    t += 0.1f;
}
```

`0.1f` n'est pas représentable exactement : `t` passe de `0.90000010` à `1.00000012`. Il ne vaut **jamais** `1.0f`, et la boucle ne s'arrête pas.

```cpp
while (t < 1.0f)
{
    t += 0.1f;
}
```

<small>Pourquoi : [[01 courses/slides/Theory/TC-FT-RNLB-03 - Flottants IEEE 754|TC-FT-RNLB-03]]</small>

---
## Bonnes pratiques

- **toujours** des accolades
- une condition longue se range dans un `bool` nommé : `bool peut_tirer = munitions > 0 && !recharge;`
- un `else if` en cascade sur une même valeur → c'est un `switch`
- éviter d'imbriquer plus de deux niveaux : extraire une fonction
- sortir tôt (`return`, `break`) plutôt qu'imbriquer profond
- `<` et `<=` plutôt que `==` sur des compteurs et des flottants

---
# Clôture
<!-- .slide: class="title" -->

## Questions ?

---

## À retenir

- `if` / `else if` / `else` choisissent **une** branche ; `switch` compare une valeur à des cas
- `while` teste **avant**, `do … while` teste **après** : au moins un tour
- `for` quand le nombre de tours est connu, `while` sinon
- `break` sort de la boucle, `continue` passe au tour suivant
- toute condition est convertie en `bool` : `0` est faux, tout le reste est vrai

---

## Exercices

- **l'échauffement** : une situation, une structure de contrôle
- **le mini-combat** : une boucle de gameplay complète, tour par tour

Énoncés : [[01 courses/exercises/C++/GPR-CF-BDP-04 - Branches et boucles|GPR-CF-BDP-04 - Branches et boucles]]
