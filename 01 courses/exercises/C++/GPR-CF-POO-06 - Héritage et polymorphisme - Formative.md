---
seances:
  - GPR-CF-POO-06
---
# Formative — OOP — L'armurerie

> Cours associé : [[01 courses/slides/C++/GPR-CF-POO-06 - Héritage et polymorphisme|GPR-CF-POO-06 - Héritage et polymorphisme]]
> Projet de départ : [[01 courses/resources/C++/GPR-CF-POO-06 - Projet companion Le stand de tir|Projet companion — le stand de tir]]

## Le but

Un stand de tir. Cinq armes, cinq types différents. Un menu de `1` à `5`.

**Le menu ne teste jamais le type de l'arme.** Pas de `switch`, pas de `if` sur une
énumération. Il tient des armes, il appelle.

## Le départ

Le companion donne **une** arme et **une** classe, sans parent. Le menu l'appelle
directement.

Ajoutez-en une deuxième par copier-coller. Puis une troisième. Arrêtez-vous là : le
problème est posé.

## La hiérarchie à construire

![[poo06_hierarchie_armes.svg]]

`Fire()` est **virtuelle pure** sur `Weapon` : toute arme sait tirer, aucune ne tire pareil,
et `Weapon` ne sait pas comment.

Le schéma ne dit rien de la visibilité des attributs. Dans le code, ils sont
**`protected`** : les classes filles s'en servent, l'extérieur non. POO-02 reste vrai.

## Pourquoi trois niveaux

`Melee` n'a pas de chargeur. Poser `Reload()` sur `Weapon` obligerait un couteau à
recharger. `Firearm` existe pour ça : il porte ce que seules les armes à feu partagent.

## Les étapes

1. **`Weapon`.** Reprendre la classe du companion. Rendre `Fire()` virtuelle pure. Vérifier
   que `Weapon w;` est refusé, et recopier le message du compilateur.
2. **`Firearm`.** Dériver de `Weapon`. Ajouter `caliber_`, `magazineCapacity_`, `Reload()`.
   `Fire()` consomme une munition et refuse à vide.
3. **`SemiAutomatic`.** Dériver de `Firearm`. Un coup par appui. `SingleShotMode()`.
4. **`FullAuto`.** Dériver de `Firearm`. `burstLength_` coups par appui. `FireFullAuto()`.
5. **`Melee`.** Dériver de `Weapon`. `bladeLength_`, `Swing()`. `Fire()` frappe : aucune
   munition, aucun `Reload()`.
6. **Le test.** Ajouter une sixième arme. Seule la ligne qui la crée doit changer.

## Ce qu'on vérifiera

| Je sais… | Vérification |
|---|---|
| écrire une base abstraite | `Weapon` ne s'instancie pas, et le compilateur le dit |
| placer un membre au bon niveau | `Reload()` est sur `Firearm`, jamais sur `Weapon` |
| laisser l'objet décider | le menu appelle `Fire()` sans savoir sur quoi |
| fermer ce qui doit l'être | aucun attribut public ; `protected` seulement si une fille s'en sert |
| ne rien casser en ajoutant | la sixième arme ne touche ni la base, ni le menu |

> [!tip] Le destructeur
> Le vecteur tient des `Weapon*`. Quand il se vide, c'est le destructeur de la **base** qui
> part — et sans `virtual`, celui de l'arme réelle ne part jamais. Mettre un message dans
> chaque destructeur, et lire la trace.

## Pour aller plus loin

- un **fusil à double canon** qui contient deux armes et les déclenche l'une après l'autre :
  la base ne change pas ;
- un **silencieux** ou un **viseur** applicable à n'importe quelle arme — et la question
  devient composition contre héritage, qui est
  [[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage|TC-FT-PCL-04]].
