---
status: Ready
manual_order: 0.5
slides:
  - "[[01 courses/slides/C++/GPR-CF-GTE-02 - Branches et intégration|Slides GTE-02]]"
exercices:
  - "[[01 courses/exercises/C++/GPR-CF-GTE-02 - Branches et intégration|Exos GTE-02]]"
---
- [x] Creer widget
- [x] pour l'atelier commun :
	- [x] Proposer thematique adapté aux connaissances des eleves. A l'heure actuelle : programmation simple, tirage au sort.
	- [x] Trouver mini-jeu style Monster fight, etc.
		- Architecture du mini jeu : au moins 3 paires de fichiers cc / hpp (main, game, messages, ou autres)
		- introduire un bug mineur a corriger sur la branche main
	- [x] Etape du workshop :
	- [x] 1 eleve Forke le repo du companion et donne les droits a son collegue,
	- [x] verification que les autorisations fonctionnent
	- [x] chaque eleve crée une branche
		- [x] Eleve 1 modifie game pour implementer une nouvelle feature
		- [x] eleve 2 fixe le bug sur la branche main
		- [x] mise en commun via les commandes aspatées
	- [x] L'exercice est en ligne de commandes, ajouter consignes de verification visuelles dans Fork
	- [x] Etre trés précis dans l'enoncé sur les commandes a passer
	- [x] decrire tous les preliminaires, lectures et telechargements
- [x] Creer companion project selon consignes de l'atelier [[01 courses/exercises/C++/GPR-CF-GTE-02 - Branches et intégration|GPR-CF-GTE-02 - Branches et intégration]]
- [x] ajouter lien vers cheat sheet https://education.github.com/git-cheat-sheet-education.pdf dans les ressources de toutes les seances ayant trait a git
- [x] Note : Comment sait-on que qqn a deja recupere une branche ? => montrer techniques
- [x] supprimer les titres des slides avec widgets
- [x] widget git branch :
	- [x] Onglet Merge ou Rebase, pas d'interactivité, ajouter ligne de commandes sur chacun des diagrammes
	- [x] Supprimer onglets OuPointeHead (deja present dans bac a sable) / merge / rebase
	- [x] Onglet bac a sable (fusion avec onglet "ou point head")
		- [x] bouton "ajouter un commit", proposer libellés réaliste de la branche
- [x] Widget resolution de conflit : proposer plus de situations les 2 existantes + 5 (sorte de quizz avec les eleves)
- [x] Developper Pull Request
- [x] Workshop :
	- [x] Designer Eleve 1 et Eleve 2, comme Owner et Worker
	- [x] Essayer de privilégier au maxium, la mise en page suivante
		- [x] Des choses sont a faire par les 2 eleves, mettre un surtitre *tous les participants*
		- [x] Des choses differentes sont a faire par chaque eleve, scinder la page en 2 colonnes pour chaque serie de consignes
		- [x] Apres chaque etape, demander aux eleves de regarder dans Fork ce qu'il se passe sans spoil ce qu'ils sont censés voir
		- [x] ajouter un separateur ligne pour chaque etape du workshop
## Traité le 28.09 — à vérifier

- **Widget** : `00 widgets/_widgets/git_graph_widget.html`, 5 onglets (`#libre` `#head` `#merge` `#rebase` `#compare`), intégré au deck en 4 slides widget. `git_conflict_widget` non fait (choix : graphe seul pour mercredi).
- **Mini-jeu** : *Chasse au trésor*, console, `rand()`, sans tableaux ni structs (vus le 07.10). `main` + `Game` + `Treasure` + `Messages` + `GameConfig.hpp`.
	- Bug : trésor tiré hors de la plage (`% (GRID_SIZE + 1)`), visible en abandonnant.
	- Feature élève 1 : nombre d'essais limité (`Game.cpp` seul).
	- Intégration en 2 temps : merge propre (fichiers différents), puis conflit voulu sur `MAX_ATTEMPTS`.
- **Companion** : `01 courses/companion projects/C++/GPR-CF-GTE-02 - Chasse au trésor` — compilé (GCC 14, Clang 18, CMake), scénario Git complet rejoué avec deux clones.
- **Énoncé** : [[01 courses/exercises/C++/GPR-CF-GTE-02 - Branches et intégration]] — préliminaires, étapes 1 à 5, vérifications Fork, rendu ; les pistes « Tank vs Towers » sont re-thématisées sur Chasse au trésor.
- **Cheat sheet** : `01 courses/resources/C++/Git - Aide-mémoire.md` (séances GTE-01, 02, 03).

> [!warning] À faire de ton côté avant mercredi
> Publier le dépôt **public** `StudioAlbert/GPR_CF_GTE_02_ChasseAuTresor` — commandes dans la note de séance, § *Notes de préparation*.

## Retraité le 28.09 (2ᵉ passe)

- **Branche récupérée ?** : 2 slides après *La règle qui évite les drames* — *Savoir si une branche a pu être récupérée* (on raisonne sur ce qui est poussé : `git branch -r`, `git branch -vv` / `ahead`, indices GitHub) et *Les vérifier, en commandes* (`git branch -vv`, `git log origin/x..x`, `git push --force-with-lease`), sorties vérifiées sur un dépôt de test.
- **Titres sur les widgets** : la slide *Où pointe HEAD* portait titre + widget sur la même slide — séparée en une slide de texte puis une slide widget sans titre, comme les autres.
- **Widget git** : `git_conflict_widget.html` créé (`#choisir` : le conflit `MAX_ATTEMPTS` de l'atelier, « garder les deux » ne compile pas ; `#garder` : deux déclarations à conserver), 2 slides widget après *Résoudre un conflit*. Inventaire du README et ressource `GPR-CF-GTE-02 - Widgets` mis à jour.

## Retraité le 28.09 (3ᵉ passe)

- **Widget git branch** (`git_graph_widget.html`) : plus que deux onglets.
	- *Bac à sable* (`#libre`) absorbe *Où pointe HEAD* : carte explicative HEAD, bouton **ajouter un commit** avec un libellé proposé selon la branche (`saut-double` → « Input du double saut », « Physique du double saut »… ; `main` → « Menu principal »…), modifiable avant de valider.
	- *Merge ou rebase* (`#compare`) : statique, sans bouton ; sous chaque graphe, les commandes qui l'ont produit ; anciens commits du rebase en pointillés.
	- Onglets *Où pointe HEAD*, *Merge*, *Rebase* supprimés ; les anciennes ancres `#head`, `#merge`, `#rebase` redirigent vers les onglets restants.
	- Deck : la slide widget HEAD pointe sur `#libre` ; les slides widget Merge et Rebase sont retirées, la démonstration passe en note sur le bac à sable.
- **Widget conflit** (`git_conflict_widget.html`) : 7 situations en quiz — voter *HEAD / la branche / les deux / réécrire*, révéler la réponse et le pourquoi, puis résoudre (commit refusé tant que la résolution ne compile pas). Ajoutées : même bug corrigé deux fois, deux `#include`, deux conditions à fusionner, renommage + nouveau paramètre, texte de game design. Les 7 cas ont été testés (bonnes et mauvaises résolutions). Une seule slide widget dans le deck, déroulé du quiz en note.
- **Pull Request** : 5 slides — *Pull request et revue* (4 puces), schéma *Le cycle d'une pull request* (`00 images/gte02_pull_request.svg`), *Ouvrir une PR, en commandes*, *Relire une PR*, *Une bonne PR* (lien avec les 3 modes de fusion GitHub).
- README des widgets et ressource `GPR-CF-GTE-02 - Widgets` mis à jour.

## Retraité le 28.09 (4ᵉ passe) — workshop

- **Owner / Worker** partout dans l'énoncé (Owner = possède le fork, fonctionnalité ; Worker = invité, bug), avec un tableau des rôles en tête.
- **Mise en page** : cadres *Tous les participants* pour les consignes communes ; cadres **Owner | Worker côte à côte** (deux colonnes) dès que les consignes diffèrent ; séparateur `---` entre chaque étape.
- **Fork sans spoil** : après chaque étape, un cadre *Regardez dans Fork* ne pose que des questions (qu'est-ce qui est apparu ? quel mot diffère ?). Les réponses — et le graphe attendu, et le diagramme mermaid — sont passés dans la note de séance, § *Réponses aux cadres « Regardez dans Fork »*. Le rendu demande les réponses des élèves.
- Ta version de l'énoncé a servi de base (préliminaires sans l'identité Git, clone du « dépôt partagé », pas de pistes maison).
- **Affichage des colonnes** :
	- site : règles ajoutées à `site-build/assets/site.css` (vérifié avec le même rendu markdown-it que `build.mjs`) ;
	- Obsidian : extrait `.obsidian/snippets/callouts-atelier.css`, activé dans `appearance.json` — sinon Réglages → Apparence → Extraits CSS.
