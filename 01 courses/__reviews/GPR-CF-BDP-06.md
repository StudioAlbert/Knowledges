---
status: Ready
manual_order: 4
slides:
  - "[[01 courses/slides/C++/GPR-CF-BDP-06 - Chaînes de caractères|Slides BDP-06]]"
exercices:
  - "[[01 courses/exercises/C++/GPR-CF-BDP-06 - Chaînes de caractères|Exos BDP-06]]"
---
- [x] slide Historique de la chaine de caractères :
	- [x] Faire schéma d'une chaine 
		- [x] le mot est *Sebastien*
		- [x] chaque caractére va dans une case avec le *vrai* carctère + le code ASCII
		- [x] ajouter le caractère de fin
		- [x] ajouter une fleche pour faire comprendre le point de départ en mémoire
		- [x] ajouter snippet de code de la lecture caractère pat caractère
- [x] slide ## La chaine de caractéres comme objet : **std::string**
	- [x] Donner 3 exemples des features permises par std::string
	- [x] Donner un apercu de la librairie standard encapsulant le char*
- [x] Donner snippet pour chacun des slides traitant des features de la std::string
- [x] Exercices 1,2 ajouter screenshots
- [x] Exercice 3 : préciser les critéres a implémenter
- [x] Exercices : positionner les objectifs dans un petit cadre
- [x] Exercice 4 : vrai fichier ??? hors sujet. Remplacer

## Traité le 28.09 — à vérifier (séance du 01.10)

- **Historique** : slide schéma `bdp06_chaine_c.svg` + slide *Lire une chaîne caractère par caractère* — désormais **dans le deck**. Le fichier `Claude outputs/BDP-06 - slides chaîne C (à coller).md` est obsolète, à supprimer.
- **std::string comme objet** : 4 puces (mémoire gérée, taille connue, s'utilise comme une valeur, encapsule un `char*`), puis slide schéma *Ce qu'il y a dans une std::string* (`bdp06_std_string.svg`), puis snippet *std::string en action*.
- **Snippets** ajoutés sur : concaténer, nombre ↔ texte, longueur, `[]`/`at()`, saisie, comparer, `find`, `substr` — tous compilés et exécutés.
- **Visuel + code, en complément** : *Passer d'un nombre à du texte* devient une slide schéma (`bdp06_to_string_stoi.svg`) suivie de *Nombre ↔ texte, en code* ; `[]`/`at()`, `find` et `substr` sont chacune suivies d'une slide widget `string_index_widget.html` (`#index`, `#find`, `#substr`).
- Ressource `01 courses/resources/C++/GPR-CF-BDP-06 - Widgets.md`, inventaire du README des widgets mis à jour.

> [!note] Non modifié
> La slide *Problémes* (5 sous-puces) est laissée telle que tu l'as écrite.

## Retraité le 29.09

- **Captures 1 et 2** : sorties de terminal de corrigés compilés et exécutés (GCC 14) — `00 images/bdp06_ex1_banniere.png` (deux héros, le cadre s'élargit), `bdp06_ex2_barre_de_vie.png` (100, 73, 40, 0 PV). Ex. 1 : encadré sur les accents (`size()` compte les octets, `é` = 2).
- **Exercice 3** : règles numérotées, testées dans l'ordre (vide, 3 caractères minimum, 16 maximum, aucun espace), message exact pour chacune, 5 pseudos de test — un message différent par essai (vérifié).
- **Objectifs** : un cadre `> [!abstract] Objectifs` en tête de chaque exercice, 1 à 6 (ajouté pour le 6).
- **Exercice 4** remplacé : *Le tag de joueur* — `[SAE] Morgane#0427` → clan, pseudo, numéro en `int` ; clan facultatif (`Aldric#12`) ; même code pour trois tags, positions calculées par `find`. Corrigé vérifié.
