# 01_degats — les dégâts selon la distance

Trois règles, imposées par le game designer, et rien d'autre :

| | |
|---|---|
| moins de **0,25 m** | 25 dégâts |
| à partir de **5 m** | 0 dégât |
| entre les deux | ça descend |

Deux fonctions à écrire dans `src/degats.cc`. Elles respectent les **mêmes** bornes et
n'ont pas la même allure entre elles.

## Où écrire

- `include/degats.h` — les trois constantes et les deux signatures. **Ne pas y toucher.**
- `src/degats.cc` — les deux corps à remplir. C'est tout l'exercice.
- `main.cc` — la boucle de lecture. Pour changer de mode, commenter une ligne et
  décommenter l'autre.

## Étape 1 — `DegatsProportionnels`

1. **Les bornes seules.** La fonction ne sait répondre que trois choses : 25, 12,5 ou 0.
   C'est faux au milieu, et c'est voulu — les deux règles de bord sont posées et ne
   bougeront plus. Vérifiez avec `0.1`, `2`, `7`.
2. **La proportionnalité.** Normaliser la distance entre 0 et 1, borner ce résultat, puis
   descendre. Une fois le bornage en place, les deux `if` de l'étape 1 ne servent plus.

| distance | dégâts attendus |
|---|---|
| 0 m | 25 |
| 0,25 m | 25 |
| 2,625 m | 12,5 |
| 5 m | 0 |
| 12 m | 0 |

## Étape 2 — `DegatsAmortis`

Mêmes bornes, autre forme : celle-ci garde ses dégâts plus longtemps, puis s'effondre.
La formule n'est pas donnée ; cinq points le sont.

| distance | 0,25 | 1,40 | 2,60 | 3,80 | 5,00 |
|---|---|---|---|---|---|
| dégâts | 25,0 | 21,8 | 17,8 | 12,6 | 0,0 |

Trois indices : les deux bornes restent **exactes** ; la moitié des dégâts tombe à **3,8 m**
et non au milieu ; vous travaillez sur `1 - t`, pas sur `t`.

Et une exigence : écrivez la **vérification**. Faites afficher la table par le programme
pour ces cinq distances, comparez à ± 0,5, et concluez en une phrase.
