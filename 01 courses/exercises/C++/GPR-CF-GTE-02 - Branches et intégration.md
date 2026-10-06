# Atelier — GPR-CF-GTE-02 — Branches et intégration

> Cours associé : [[01 courses/slides/C++/GPR-CF-GTE-02 - Branches et intégration|GPR-CF-GTE-02 - Branches et intégration]]
> Projet de départ : [StudioAlbert/GPR_CF_GTE_02_ChasseAuTresor](https://github.com/StudioAlbert/GPR_CF_GTE_02_ChasseAuTresor)
> Aide-mémoire : [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

Terrain de jeu commun à toute la fiche : **Chasse au trésor**, un petit jeu console. Un
trésor est tiré au sort sous une plage de 5 × 5 cases ; le joueur creuse, un détecteur dit
s'il chauffe.

```
src/
├── main.cpp          initialise le hasard, lance une partie
├── Game.hpp/.cpp     la boucle de jeu
├── Treasure.hpp/.cpp tirage du trésor, calcul de distance
├── Messages.hpp/.cpp tout ce qui s'affiche et se saisit
└── GameConfig.hpp    les réglages (taille, nombre d'essais)
```

---

## Atelier commun — 20 min en classe, fin à la maison

**En binôme.** Toutes les manipulations Git se font **en ligne de commande**. Fork sert
uniquement à **regarder** ce que les commandes ont produit.

| Rôle | Qui | Mission |
|---|---|---|
| **Owner** | possède le dépôt | développe une **fonctionnalité** |
| **Worker** | invité sur le dépôt | **corrige un bug** |

`<owner>` et `<worker>` désignent les pseudos GitHub de chacun.

> [!tip] Lire la fiche
> Un cadre *Tous les participants* : les deux font la même chose. Deux colonnes *Owner* /
> *Worker* : chacun suit **sa** colonne. Un cadre *Regardez dans Fork* : on observe et on
> note ce qu'on voit, avant de passer à la suite.

---

### 0 — Préliminaires (avant la séance)

> [!tous] Tous les participants
>
> | # | À faire | Vérification |
> | --- | --- | --- |
> | 0.1 | Créer un compte sur [github.com](https://github.com) et l'envoyer à son binôme | Vous êtes connecté sur github.com |
> | 0.2 | Git est installé (séance GTE-01) | `git --version` affiche **2.23 ou plus** |
> | 0.3 | Installer **Fork** : [git-fork.com](https://git-fork.com) (téléchargement gratuit) | Fork s'ouvre |
> | 0.4 | Chaîne de compilation C++ et CMake (séances EDC-01 et EDC-03) | Un projet CMake compile |
> | 0.5 | Lire l'aide-mémoire GitHub : sections *Branch & Merge* et *Share & Update* | — |

> [!tip] Le terminal
> Sous Windows, utilisez **Git Bash** (installé avec Git) : clic droit dans un dossier →
> *Open Git Bash here*. Toutes les commandes de la fiche s'y tapent telles quelles.

> [!warning] Première fois que vous poussez
> Au premier `git push`, Git ouvre le navigateur pour vous connecter à GitHub. Acceptez :
> c'est ce qui vous autorise à écrire sur le dépôt.

---

### 1 — Forker et inviter

> [!columns]
>
> > [!owner] Owner
> >
> > 1. Ouvrir [github.com/StudioAlbert/GPR_CF_GTE_02_ChasseAuTresor](https://github.com/StudioAlbert/GPR_CF_GTE_02_ChasseAuTresor).
> > 2. Bouton **Fork** en haut à droite → **Create fork**. Vous arrivez sur `github.com/<owner>/GPR_CF_GTE_02_ChasseAuTresor` : c'est **votre** copie.
> >3. Sur github, dans votre nouveau repository : **Settings** → **Collaborators** → **Add people** → saisir `<worker>` → **Add to repository**.
>
> > [!worker] Worker
> >
> > 4. Attendre l'invitation de l'Owner.
> > 5. L'accepter depuis le mail reçu, ou en ouvrant `github.com/<owner>/GPR_CF_GTE_02_ChasseAuTresor/invitations` → **Accept invitation**.

> [!fork] Regardez sur GitHub
>
> **Owner** : *Settings → Collaborators*. Que voyez-vous à côté du pseudo du Worker, avant
> puis après qu'il a accepté ?

---

### 2 — Cloner et vérifier les droits

> [!tous] Tous les participants
>
> Chacun clone **le fork de l'Owner** — pas le dépôt StudioAlbert :
>
> ```bash
> git clone https://github.com/<owner>/GPR_CF_GTE_02_ChasseAuTresor.git
> cd GPR_CF_GTE_02_ChasseAuTresor
> ```
>
> Ouvrir le dossier dans Fork : **File → Open Repository**. 
> Dans CLION, compiler et lancer le jeu une fois.

> [!columns]
>
> > [!owner] Owner
> >
> > Attendre que le Worker ait poussé sa branche de test, puis dans Fork : bouton **Fetch**.
>
> > [!worker] Worker
> >
> > Pousser une branche vide, pour tester vos droits :
> >
> > ```bash
> > git switch -c acces-<worker>
> > git push -u origin acces-<worker>
> > ```
> >
> > Si Git répond `403` ou `Permission denied` : l'invitation n'a pas été acceptée, revenir à l'étape 1.

> [!fork] Regardez dans Fork
>
> **Owner** : dans la barre de gauche, ouvrez **Remotes → origin**. Qu'est-ce qui est apparu ?
> **Worker** : dans **Branches**, laquelle est en gras ?

> [!columns]
>
> > [!owner] Owner
> >
> > Rien à faire.
>
> > [!worker] Worker
> >
> > Supprimer la branche de test, en local et sur GitHub :
> >
> > ```bash
> > git switch main
> > git branch -d acces-<worker>
> > git push origin --delete acces-<worker>
> > ```

---

### 3 — Chacun sa branche

> [!columns]
>
> > [!owner] Owner — la fonctionnalité
> >
> > *La marée monte* : le joueur ne dispose plus que de `MAX_ATTEMPTS` essais (déjà déclaré dans `GameConfig.hpp`). Au-delà, la partie est perdue et `printDefeat` (déjà écrite dans `Messages.cpp`) s'affiche.
> >
> > ```bash
> > git switch -c feature/essais-limites
> > ```
> >
> > Modifier **uniquement** `src/Game.cpp` : 
> > - inclure `GameConfig.hpp`, 
> > - arrêter la boucle quand `attempts` atteint `MAX_ATTEMPTS`, 
> > - afficher la bonne fin de partie. 
> > - Recompiler, perdre une partie exprès. 
> > - Puis :
> >
> > ```bash
> > git status
> > git add src/Game.cpp
> > git commit -m "Limite le nombre d'essais à MAX_ATTEMPTS"
> > git push -u origin feature/essais-limites
> > ```
>
> > [!worker] Worker — le bug
> >
> > Le `README.md` le décrit : *parfois, on ne trouve jamais le trésor*. Lancez plusieurs parties en abandonnant tout de suite (colonne `0`) : le jeu affiche où était le trésor. Regardez les coordonnées.
> >
> > ```bash
> > git switch -c fix/tresor-hors-plage
> > ```
> >
> > Trouver et corriger la ligne fautive dans `src/Treasure.cpp`, recompiler, rejouer. Puis :
> >
> > ```bash
> > git status
> > git add src/Treasure.cpp
> > git commit -m "Corrige le tirage : le trésor reste sur la plage"
> > git push -u origin fix/tresor-hors-plage
> > ```

> [!fork] Regardez dans Fork
>
> **Tous** : bouton **Fetch**. Combien de branches voyez-vous dans le graphe ? D'où
> partent-elles ? Dans **Branches**, laquelle est en gras, et pourquoi ?

---

### 4 — Intégrer sans conflit

**L'ordre compte : le Worker intègre en premier.**

> [!columns]
>
> > [!owner] Owner
> >
> > **4.2** — Quand le Worker a poussé `main` : récupérer le fix, puis ramener la fonctionnalité.
> >
> > ```bash
> > git switch main
> > git pull
> > git merge --no-edit feature/essais-limites
> > git push
> > ```
>
> > [!worker] Worker
> >
> > **4.1** — Ramener le fix dans `main` :
> >
> > ```bash
> > git switch main
> > git pull
> > git merge fix/tresor-hors-plage
> > git push
> > ```
> >
> > **4.3** — Quand l'Owner a poussé à son tour, se remettre à jour :
> >
> > ```bash
> > git pull
> > ```

> [!fork] Regardez dans Fork — et dans le terminal
>
> **Tous** : relisez ce que Git a répondu à **votre** `git merge`. Un mot diffère entre
> l'Owner et le Worker : lequel, et pourquoi ?
> Dans Fork, comparez vos deux graphes, puis tapez `git log --graph --oneline --all` : la
> forme est-elle la même ? Lancez le jeu compilé depuis `main` : quels changements a-t-il ?

---

### 5 — Provoquer un conflit, puis le résoudre

Owner et Worker ne sont pas d'accord sur l'équilibrage : l'Owner veut **10** essais, le
Worker en veut **6**.

> [!tous] Tous les participants
>
> En partant d'un `main` à jour :
>
> ```bash
> git switch main
> git pull
> git switch -c equilibrage-<votre-pseudo>
> ```

> [!columns]
>
> > [!owner] Owner
> >
> > Dans `src/GameConfig.hpp`, passer `MAX_ATTEMPTS` à **10**, puis :
> >
> > ```bash
> > git commit -am "Équilibrage : 10 essais"
> > ```
> >
> > **Quand le Worker a poussé `main`**, intégrer à votre tour :
> >
> > ```bash
> > git switch main
> > git pull
> > git merge equilibrage-<owner>
> > ```
>
> > [!worker] Worker
> >
> > Dans `src/GameConfig.hpp`, passer `MAX_ATTEMPTS` à **6**, puis :
> >
> > ```bash
> > git commit -am "Équilibrage : 6 essais"
> > ```
> >
> > Intégrer le premier :
> >
> > ```bash
> > git switch main
> > git merge equilibrage-<worker>
> > git push
> > ```

> [!fork] Regardez dans Fork — Owner
>
> Lisez le message de Git. Dans **Local Changes**, comment `src/GameConfig.hpp` est-il
> signalé ? Ouvrez le fichier : que contient-il maintenant, et que désigne chaque partie ?

> [!tous] Tous les participants — résoudre en binôme
>
> Se mettre d'accord sur **une** valeur. L'Owner édite le fichier pour ne garder qu'une seule ligne `MAX_ATTEMPTS`, **sans aucun marqueur**, recompile, puis :
>
> ```bash
> git add src/GameConfig.hpp
> git commit -m "Résout le conflit d'équilibrage : <valeur> essais"
> git push
> ```
>
> Le Worker se remet à jour : `git pull`.

> [!fork] Regardez dans Fork
>
> **Tous** : `git status` et le graphe. Que dit Git ? Comment le commit de résolution
> apparaît-il dans le graphe ? Le jeu respecte-t-il la valeur choisie ?

---

### Rendu

Un seul rendu par binôme :

- l'URL du fork `github.com/<owner>/GPR_CF_GTE_02_ChasseAuTresor` ;
- ~~une capture du graphe de Fork **après** l'étape 5 ;~~
- ~~vos réponses aux questions des cadres *Regardez dans Fork*, en une ou deux lignes chacune ;~~
- ~~trois lignes : ce que chaque marqueur de conflit désignait, et la valeur retenue.~~
