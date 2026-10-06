---
title: GPR-CF-BDP-06 - Chaînes de caractères
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
publish: online
---

# Chaînes de caractères
<!-- .slide: class="title" -->
## GPR-CF-BDP-06

<small>Du texte, et ce qu'on peut en faire</small>

Note:
**Révisé le 28.09.** Chaque slide de fonctionnalité porte un snippet vérifié
(GCC 14, C++23) ; `[]`/`at()`, `find` et `substr` sont suivis d'une slide
widget (`string_index_widget.html`), `to_string`/`stoi` d'un schéma. Dernière séance du bloc *Bases de la Programmation*.

---

## Objectifs

Savoir construire, mesurer, comparer et découper une `std::string`, et lire proprement ce que tape le joueur.

**Prérequis :** types, tableaux et boucles — [[01 courses/slides/C++/GPR-CF-BDP-05 - Énumérations et tableaux|GPR-CF-BDP-05]].

---

## Une chaîne n'est pas un nombre

`"42"` occupe deux caractères et ne s'additionne pas ; `42` est une valeur.

---

## Historique de la chaîne de caractères
<!-- .slide: class="schema" -->

En C, une chaîne n'est qu'une suite de cases mémoire, repérée par l'adresse de la première, et terminée par `'\0'`.

![[bdp06_chaine_c.svg]]

Note:
Ce qu'il faut lire sur le schéma :
- `nom` est un `char*` : il ne contient pas le texte, seulement l'**adresse**
  de la première case (flèche rouge) ;
- chaque case contient **un** caractère, rangé sous forme de nombre : son
  code ASCII (`'S'` = 83) — lien avec RNLB-01 (bases) ;
- la case `'\0'` (code 0) marque la fin : rien d'autre n'indique la longueur.
  9 lettres occupent donc 10 cases.
C'est la représentation héritée du C (1972), encore utilisée par les
littéraux `"Sebastien"` en C++.

---

## Lire une chaîne caractère par caractère

Pour connaître la longueur, il faut marcher case par case jusqu'au `'\0'`.

```cpp
const char* nom = "Sebastien";

int i = 0;
while (nom[i] != '\0')      // on avance jusqu'au caractère de fin
{
    std::println("{} : '{}' = {}", i, nom[i], static_cast<int>(nom[i]));
    i++;
}
std::println("longueur : {}", i);   // 9 : le '\0' n'est pas compté
```

Note:
Sortie : `0 : 'S' = 83`, `1 : 'e' = 101`, … `8 : 'n' = 110`, puis
`longueur : 9`. C'est exactement ce que fait `strlen`. Si le `'\0'`
manque, la boucle continue à lire la mémoire voisine : c'est le premier
problème de la slide suivante.
Compilé et vérifié (C++23, `<print>`).

---

## Problémes

- manque de sécurité
	- aucun assurance par le langage de ne pas dépasser
	- Caractère **pourri**
	- pb d'accés mémoire
	- pb de manipulation pour raccourcir, rallonger

---
## La chaîne de caractères comme objet : **std::string**

- elle **gère sa mémoire** : elle grandit et rétrécit seule, et se libère seule
- elle **connaît sa taille** : `size()` répond sans chercher le `'\0'`
- elle s'utilise **comme une valeur** : `=` copie le texte, `==` compare le texte, `+` colle
- dedans, toujours un `char*` : la bibliothèque standard l'**encapsule**

Note:
Réponse aux trois problèmes de la slide précédente : plus de dépassement
silencieux (la taille est connue, `at()` vérifie), plus de caractère de fin
oublié (l'objet le pose lui-même), plus de manipulation à la main pour
raccourcir ou rallonger. `#include <string>`, type `std::string`.

---

## Ce qu'il y a dans une `std::string`
<!-- .slide: class="schema" -->

Un objet de trois champs qui garde le `char*` et tient sa taille à jour.

![[bdp06_std_string.svg]]

Note:
Aperçu de l'encapsulation : un pointeur vers le texte, la taille, la
capacité (la place réservée d'avance pour grandir sans tout recopier).
Le texte garde son `'\0'` final : `c_str()` rend ce `const char*` pour
les fonctions héritées du C.
Précision si la question vient : pour les chaînes courtes, les
bibliothèques rangent le texte directement dans l'objet (*small string
optimization*, jusqu'à 15 caractères avec GCC) ; le schéma montre le cas
général. Autres encapsulations de la bibliothèque standard, à citer
seulement : `std::string_view` (une vue en lecture seule, sans copie),
`std::wstring` / `std::u8string` pour d'autres jeux de caractères.

---

## `std::string` en action

Copier, agrandir, comparer : tout ce qui demandait des boucles et des `'\0'` tient en une ligne.

```cpp
std::string nom = "Sebastien";
std::string copie = nom;          // une vraie copie du texte, pas de l'adresse
copie += " le Magicien";          // la mémoire s'agrandit toute seule

std::println("{}", copie);        // Sebastien le Magicien
std::println("{}", copie.size()); // 21
std::println("{}", nom == "Sebastien");   // true : on compare le texte
```

Note:
Sortie vérifiée (GCC 14, C++23). Avec des `char*`, chacune de ces lignes
demanderait une fonction C (`strcpy`, `strcat`, `strcmp`) et un tableau
assez grand prévu à l'avance.


---

## Déclarer et concaténer

`std::string` s'écrit comme un type ordinaire, et `operator +` colle deux chaînes bout à bout.

```cpp
#include <string>

std::string prenom = "Sebastien";
std::string titre = "le Magicien";

std::string complet = prenom + " " + titre;   // "Sebastien le Magicien"
complet += " !";                               // on ajoute à la fin
std::println("{}", complet);                   // Sebastien le Magicien !
```

Note:
Piège à montrer à l'oral : `"Sir" + " Lancelot"` ne compile pas — deux
littéraux sont deux `const char*`, pas des `std::string`. Il faut au moins
une `std::string` dans l'addition.

---

## Passer d'un nombre à du texte
<!-- .slide: class="schema" -->

`std::to_string(pv)` fabrique la chaîne, `std::stoi(saisie)` tente le retour — et peut échouer.

![[bdp06_to_string_stoi.svg]]

Note:
`42` est une valeur sur laquelle on calcule ; `"42"` est deux caractères
qu'on affiche. L'aller réussit toujours, le retour dépend de ce qu'a tapé
le joueur. Le piège `stoi("42abc")` → 42 est vérifié.

---

## Nombre ↔ texte, en code

On affiche avec `to_string`, on relit une saisie avec `stoi`.

```cpp
int pv = 42;
std::string texte = "PV : " + std::to_string(pv);   // "PV : 42"

std::string saisie = "17";
int niveau = std::stoi(saisie);                      // 17

std::stoi("abc");   // lève std::invalid_argument
```

Note:
Les exceptions (`try` / `catch`) ne sont pas encore au programme : on
retient seulement que le programme s'arrête si la saisie n'est pas un
nombre. `std::stof` et `std::stod` existent pour les flottants.

---

## Longueur

`size()` compte les caractères, et une chaîne vide se teste avec `empty()`.

```cpp
std::string pseudo = "Sebastien";
std::println("{}", pseudo.size());   // 9 : le '\0' n'est pas compté

std::string vide;
if (vide.empty())
{
    std::println("pseudo manquant");
}
```

Note:
`size()` renvoie un `std::size_t`, non signé (lien RNLB-02) :
`pseudo.size() - 1` sur une chaîne vide fait le tour. `length()` est un
synonyme de `size()`.

---

## Accès : `[]` ou `at()`

`[]` ne vérifie rien et vous laisse lire à côté ; `at()` vérifie et lève une exception.

```cpp
std::string mot = "Dungeon";

char premiere = mot[0];      // 'D'
mot[0] = 'd';                // "dungeon" : on peut aussi écrire
char troisieme = mot.at(2);  // 'n'

char a = mot.at(20);         // lève std::out_of_range
char b = mot[20];            // comportement indéfini : lit la mémoire voisine
```

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/string_index_widget.html#index" data-background-interactive -->

Note:
Widget — onglet « [] ou at() ». Pousser l'indice au-delà de 14 : `[]`
affiche ce qui traîne à côté, `at()` refuse. Changer le texte dans le
champ « Chaîne » pour montrer que le dernier indice valide est toujours
`size() − 1`. Repli : ouvrir 00 widgets/_widgets/string_index_widget.html.

---

## Lire ce que tape le joueur

`std::cin >> pseudo` s'arrête au premier espace ; `std::getline` prend la ligne entière.

```cpp
std::string nom;
std::cin >> nom;                  // tape « Sir Lancelot » → nom = "Sir"

std::string ligne;
std::getline(std::cin, ligne);    // tape « Sir Lancelot » → ligne = "Sir Lancelot"
```

Note:
Piège classique : un `std::getline` juste après un `std::cin >> x` lit une
ligne vide, car le retour à la ligne est resté dans le flux. Parade :
`std::getline(std::cin >> std::ws, ligne);` — `std::ws` saute les blancs.

---

## Comparer

`==` répond oui ou non ; `compare()` répond avant, après ou identique — utile pour trier.

```cpp
std::string a = "archer";
std::string b = "barbare";

bool meme = (a == "archer");   // true
int ordre = a.compare(b);      // < 0 : "archer" vient avant "barbare"
bool avant = (a < b);          // true : même réponse, plus lisible
```

Note:
`compare` rend un entier négatif, nul ou positif — pas forcément −1 / 0 /
1. L'ordre est celui des codes ASCII : les majuscules passent avant les
minuscules (`"Zombie" < "archer"` est vrai).

---

## Chercher : `find` et `npos`

`find` renvoie la position trouvée, ou `std::string::npos` — qui n'est pas `-1`, et qui se teste explicitement.

```cpp
std::string ligne = "give potion 3";

std::size_t espace = ligne.find(' ');          // 4

if (ligne.find("sword") == std::string::npos)
{
    std::println("pas d'épée");
}
```

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/string_index_widget.html#find" data-background-interactive -->

Note:
Widget — onglet « find ». Chercher « Crawler » (8), puis décaler « à
partir de » au-delà de 8 : `npos`, affiché en entier
(18446744073709551615) pour montrer que ce n'est pas −1.

---

## Découper : `substr`

`substr(debut, longueur)` extrait une tranche ; combiné à `find`, il découpe une ligne en morceaux.

```cpp
std::string ligne = "give potion 3";

std::size_t premier = ligne.find(' ');                // 4
std::size_t second  = ligne.find(' ', premier + 1);   // 11

std::string commande = ligne.substr(0, premier);                        // "give"
std::string objet    = ligne.substr(premier + 1, second - premier - 1); // "potion"
std::string quantite = ligne.substr(second + 1);                        // "3"
```

---

<!-- .slide: class="widget" data-background-iframe="00 widgets/_widgets/string_index_widget.html#substr" data-background-interactive -->

Note:
Widget — onglet « substr ». Le 2ᵉ argument est une **longueur** : régler
début 8, longueur 7 → "Crawler". Pousser la longueur au-delà de la fin :
le résultat est coupé, pas d'erreur. Pousser le début au-delà de 15 :
exception. C'est exactement l'atelier (console de triche).

---

## Atelier — 20 min

Écrire la console de triche du jeu : lire une ligne, reconnaître la commande, en extraire l'objet et la quantité.

---

## À retenir

Une chaîne se mesure, se compare, se cherche et se découpe — et tout index vient d'un `find` vérifié, jamais d'un nombre écrit à la main.

---

## Questions ?
