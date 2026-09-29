# BDP-06 — slides à coller dans le deck

Remplacent la slide « Historique de la chaine de caractères » de
`01 courses/slides/C++/GPR-CF-BDP-06 - Chaînes de caractères.md`. Le deck était en cours
d'édition dans Obsidian au moment de l'écriture : rien n'y a été modifié.

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
