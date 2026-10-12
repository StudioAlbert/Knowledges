---
status: To check
manual_order: 6
url_test: http://localhost:56689/cpp/gpr-cf-poo-05/
slides: "[[01 courses/slides/C++/GPR-CF-POO-05 - Static et surcharge d'opérateur]]"
---
- [x] Ajouter contenu issu de (01 courses/lectures/C++/04 - OOP Advanced)
- [x] Développer contenu du deck definitif (01 courses/slides/C++/GPR-CF-POO-05 - Static et surcharge d'opérateur)

## Traité le 12.10 — à vérifier

**Deck rédigé**, 20 slides, de 14 titres sans contenu. Repris de `04 - OOP Advanced` : les
tranches *Static* et *Surcharge d'opérateur*. L'héritage et le polymorphisme sont partis à
POO-06 dans la même passe, comme le prévoyait la note de séance.

Deux choses du support d'origine n'ont **pas** été reprises :

- les slides `struct` et *Class vs struct* — c'est le sujet de POO-01 et POO-02, les y
  laisser évite de le redire une troisième fois ;
- l'exemple `myOwnTime`, remplacé par `Vector2`, qui sert déjà en GVM-01 et dans les
  exercices. Une addition d'heures qui ne retient pas les minutes au-delà de 60 est un
  mauvais exemple d'opérateur — elle fait exactement ce que la slide *Les pièges* interdit.

| Slide | Ce qui est montré | Vérifié |
|---|---|---|
| *Ce que ça donne* | le compteur suit les portées : 3 puis 1 | sortie réelle du programme |
| *L'oubli classique* | définition manquante dans le source | `LNK2019` + `LNK1120` au MSVC |
| *Membre ou fonction libre* | `2.0f * v` refusé sans fonction libre | `error C2677` au MSVC |
| *Comparer* | `operator== = default` et `std::ranges::find` | compilé et exécuté |

**Schéma** `poo05_static_partage.svg` : trois objets avec chacun son `pointsDeVie_`, et une
seule case `vivants_` que personne ne possède. Mesuré à 978 x 313 dans le cadre.

Le deck s'appuie sur POO-03 (l'erreur de l'éditeur de liens, déjà vue) et sur POO-04 (c'est
le constructeur et le destructeur qui tiennent le compteur) : le bloc se referme sur
lui-même.

## Hors périmètre, à décider

- **La feuille d'exercices reste un overview**, six pistes de deux lignes.
- **Le widget `static_partage_widget.html`** reste proposé, pas construit : le schéma et la
  trace du compteur disent la même chose, sans le pas-à-pas.
- Le deck est en **`publish: draft`** et la séance est le **15.10** : le passage en `online`
  est à faire avant, après ta relecture.
