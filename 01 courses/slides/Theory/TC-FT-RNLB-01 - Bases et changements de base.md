---
title: Bases et changements de base
type: slides
status: Backlog
subject: Theory
duration_h: 1
bloc_gsda: Représentation des Nombres et Logique Binaire
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

# Bases et changements de base
<!-- .slide: class="title" -->

### Binaire, octal, hexadécimal : un nombre, plusieurs écritures

<small>TC-FT-RNLB-01 · Représentation des Nombres et Logique Binaire</small>

Note:
Séance d'entrée du bloc, sans prérequis. On part de ce que tout le monde
sait faire — lire 368 — pour montrer que la base 10 n'est qu'un choix de
poids. Binaire, octal et hexadécimal suivent exactement la même méthode.
On termine par l'écriture de ces nombres en C++.

---

## Objectifs

À la fin de la séance, vous savez :

- lire un nombre écrit en base 2, 8, 10 ou 16
- convertir dans les deux sens, à la main
- passer du binaire à l'hexadécimal sans calcul
- écrire et afficher ces nombres en C++
- dire **pourquoi** la machine compte en binaire, et pourquoi on le lit en hexadécimal

**Prérequis :** aucun.

---

# Le poids des chiffres
<!-- .slide: class="title" -->

---

## C'est quoi ?

« Cet instrument était utilisé par des peuples très largement séparés comme les [Étrusques](https://fr.wikipedia.org/wiki/%C3%89trusques "Étrusques"), les [Grecs](https://fr.wikipedia.org/wiki/Gr%C3%A8ce_antique "Grèce antique"), les [Égyptiens](https://fr.wikipedia.org/wiki/%C3%89gypte_antique "Égypte antique"), les [Indiens](https://fr.wikipedia.org/wiki/Indiens_\(Inde\) "Indiens (Inde)"), les [Chinois](https://fr.wikipedia.org/wiki/Chinois_\(nation\)) et les [Mexicains](https://fr.wikipedia.org/wiki/Mexicains "Mexicains") et l'on peut penser qu'il a été inventé indépendamment dans différents endroits. »

![[boulier.png]]

---
## Qu'est-ce qu'un nombre décimal ?

C'est une somme de *a* × 10ⁿ.

Exemple avec **368** :

| Chiffre | Poids | Valeur |
|:-:|:-:|:-:|
| 3 | 3 × 10² | 300 |
| 6 | 6 × 10¹ | 60 |
| 8 | 8 × 10⁰ | 8 |

---

## Changer de base

Le même principe, mais en base 9 :

```
5 + 9 * 4 + 81 * 3
```

Note:
La base n'est qu'un choix de poids. Ici 81 = 9², 9 = 9¹, 1 = 9⁰ : rien
ne change dans la méthode, seule la valeur de la base change. Ce nombre
s'écrit 345 en base 9 et vaut 284.

---

## Une base, des règles

- en base *b*, on dispose de *b* chiffres : de 0 à *b* − 1
- le chiffre de rang *n* — en comptant à partir de 0, depuis la droite — pèse *b*ⁿ
- en cas de doute, on note la base en indice : 345₉, 101010₂, 2A₁₆

| Base | Nom | Chiffres |
|:-:|---|---|
| 2 | binaire | 0 1 |
| 8 | octal | 0 … 7 |
| 10 | décimal | 0 … 9 |
| 16 | hexadécimal | 0 … 9 puis A … F |

---

## Pourquoi le binaire ?

- un circuit électronique distingue facilement **deux états** : tension haute ou basse
- un chiffre binaire est un **bit** ; 8 bits forment un **octet**
- avec *n* bits, on écrit **2ⁿ** valeurs différentes
- entiers, flottants, caractères, pixels : tout ce que manipule la machine est une suite de bits

Note:
C'est la raison matérielle. La question qui reste — comment ranger un
nombre, négatif ou à virgule, dans ces bits — occupe tout le bloc.

---

# Binaire, hexadécimal, octal
<!-- .slide: class="title" -->

---

## Binaire

Chiffres : **0 ou 1**.

Exemple avec `1100000010` :

| Bit posé | Poids | Valeur |
|:-:|:-:|:-:|
| 1 | 1 × 2⁹ | 512 |
| 1 | 1 × 2⁸ | 256 |
| 1 | 1 × 2¹ | 2 |

⇒ 512 + 256 + 2 = **770**

---

## Les puissances de 2 à connaître

| 2ⁿ | 2⁰ | 2¹ | 2² | 2³ | 2⁴ | 2⁵ | 2⁶ | 2⁷ | 2⁸ | 2⁹ | 2¹⁰ |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Valeur** | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1024 |

Et plus loin : 2¹⁶ = 65 536 · 2³² ≈ 4,3 milliards · 2⁶⁴ ≈ 1,8 × 10¹⁹

Note:
Les connaître par cœur jusqu'à 2¹⁰ fait gagner un temps énorme en
conversion. On les retrouvera dans les plages des types entiers à la
séance suivante.

---

## Hexadécimal

Préfixe `0x`. Chiffres de **0 à F** (= 15).

Exemple avec `0x182` :

| Chiffre | Poids | Valeur |
|:-:|:-:|:-:|
| 1 | 1 × 16² | 256 |
| 8 | 8 × 16¹ | 128 |
| 2 | 2 × 16⁰ | 2 |

⇒ 256 + 128 + 2 = **386**

---

## Hexadécimal — la table

| Hexa | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Décimal** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| **Binaire** | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

---

## Binaire ↔ hexadécimal : par paquets de 4

Un chiffre hexadécimal vaut **exactement 4 bits**. On découpe en partant de la droite :

```
1001 1010 1000 0010
   9    A    8    2   →  0x9A82
```

Dans l'autre sens, on remplace chaque chiffre par ses 4 bits :

```
0x2A  →  2 = 0010, A = 1010  →  0010 1010
```

Note:
C'est la raison d'être de l'hexadécimal en programmation : du binaire
compacté, lisible, converti de tête. Un octet s'écrit toujours avec deux
chiffres hexadécimaux, de 0x00 à 0xFF.

---

## Octal

Base 8, chiffres de **0 à 7**. Un chiffre octal vaut **exactement 3 bits**.

```
755₈ = 7×8² + 5×8¹ + 5×8⁰ = 448 + 40 + 5 = 493
755₈ = 111 101 101₂
```

Encore utilisé pour les droits des fichiers Unix : `chmod 755` donne `rwx r-x r-x`, avec r = 4, w = 2, x = 1.

Note:
L'octal est surtout historique : il convenait aux machines dont les mots
faisaient 12, 18 ou 36 bits, des multiples de 3. On le croise encore dans
les permissions Unix, et dans un piège de C++ quelques slides plus loin.

---

# Conversions
<!-- .slide: class="title" -->

---

## D'une base vers le décimal

On additionne chaque chiffre multiplié par son poids :

```
0xC4      = 12×16 + 4     = 196
0b101010  = 32 + 8 + 2    = 42
052       = 5×8 + 2       = 42
```

C'est la méthode des slides précédentes : elle vaut pour **toutes** les bases.

---

## Du décimal vers une base : divisions successives

On divise par la base jusqu'à obtenir 0, puis on lit les **restes de bas en haut** :

```
42 ÷ 2 = 21   reste 0
21 ÷ 2 = 10   reste 1
10 ÷ 2 =  5   reste 0
 5 ÷ 2 =  2   reste 1
 2 ÷ 2 =  1   reste 0
 1 ÷ 2 =  0   reste 1     →  42 = 101010₂
```

Même chose en base 16 : 196 ÷ 16 = 12 reste **4**, puis 12 ÷ 16 = 0 reste **12, soit C** → `0xC4`.

---

## Vers le binaire : retirer les puissances de 2

On retire la plus grande puissance de 2 possible, et on recommence :

```
39554 = 32768 + 6786
      = 32768 + 4096 + 2690
      = 32768 + 4096 + 2048 + 642
      = 32768 + 4096 + 2048 + 512 + 130
      = 32768 + 4096 + 2048 + 512 + 128 + 2
      = 2¹⁵ + 2¹² + 2¹¹ + 2⁹ + 2⁷ + 2¹   →  1001 1010 1000 0010
```

Note:
Plus rapide que les divisions dès qu'on connaît ses puissances de 2. Les
divisions restent la méthode sûre pour les bases qui ne sont pas des
puissances de 2. Le résultat se relit en hexadécimal : 0x9A82.

---

## À vous

```
0b1111'1111  = ??          0x3E8 = ??
0b1000'0000  = ??          0777  = ??   (octal)
        100  = 0b??        = 0x??
       1000  = 0b??        = 0x??
```

Note:
Corrigé : 255 ; 1000 ; 128 ; 511. 100 = 0b110'0100 = 0x64.
1000 = 0b11'1110'1000 = 0x3E8.

---

# En C++
<!-- .slide: class="title" -->

---

## Écrire un nombre entier en C++

| Écriture | Base | Valeur |
|---|---|:-:|
| `42` | décimal | 42 |
| `0x2A` | hexadécimal | 42 |
| `052` | octal | 42 |
| `0b101010` | binaire (C++14) | 42 |

- séparateur de chiffres (C++14) : `1'000'000`, `0b1010'0101`, `0xFF'FF'FF'FF`
- suffixes : `42u` (`unsigned`), `42l` (`long`), `42ll` (`long long`), `42ull`…

<small>[en.cppreference.com/w/cpp/language/integer_literal](https://en.cppreference.com/w/cpp/language/integer_literal)</small>

---

## Le piège de l'octal

```cpp
int a = 100;
int b = 010;   // aligné pour faire joli : vaut 8
int c = 09;    // ne compile pas : 9 n'est pas un chiffre octal
```

Un `0` en tête fait de tout le nombre un **octal**.

Note:
Le bug arrive typiquement dans des tableaux de valeurs alignées à la main.
Il compile sans avertissement : seul le `09` est refusé.

---

## Afficher dans une autre base

```cpp
#include <bitset>
#include <format>
#include <iostream>

int main()
{
    std::cout << std::hex << 42 << '\n';                 // 2a
    std::cout << std::oct << 42 << '\n';                 // 52
    std::cout << std::dec << 42 << '\n';                 // 42
    std::cout << std::bitset<8>(42) << '\n';             // 00101010
    std::cout << std::format("{:#x} {:08b}\n", 42, 42);  // 0x2a 00101010
}
```

Note:
`std::hex` reste actif sur le flux tant qu'on ne remet pas `std::dec`.
`std::format` demande C++20.

---

# Clôture
<!-- .slide: class="title" -->

---

## À retenir

- une base est un choix de poids : le chiffre de rang *n* pèse *b*ⁿ
- base → décimal : **additionner** les poids ; décimal → base : **diviser** et lire les restes à l'envers
- 1 chiffre hexadécimal = **4 bits** ; 1 chiffre octal = **3 bits**
- en C++ : `0x` hexadécimal, `0b` binaire, `0` en tête **octal**, `'` pour grouper les chiffres

---

## Exercices

- lire et convertir dans les quatre bases
- compléter le tableau des conversions
- prévoir l'affichage de littéraux C++

Énoncés : [[01 courses/exercises/Theory/TC-FT-RNLB-01 - Bases et changements de base]]

---

## Pour aller plus loin

- Séance suivante : [[01 courses/slides/Theory/TC-FT-RNLB-02 - Entiers signés et dépassements|TC-FT-RNLB-02 - Entiers signés et dépassements]]
- [Système hexadécimal — Wikipédia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_hexad%C3%A9cimal)
- [Integer literal — cppreference](https://en.cppreference.com/w/cpp/language/integer_literal)
