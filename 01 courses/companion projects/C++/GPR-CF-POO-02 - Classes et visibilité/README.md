# La classe Joueur — companion GPR-CF-POO-02

Le squelette de l'**exercice 5** de la séance *Classes et visibilité*. Le menu de commandes
est déjà écrit et fonctionne ; votre travail tient dans **un seul fichier**, `joueur.h`.

## Compiler et lancer

Ouvrir le dossier dans CLion (ou Visual Studio), qui lit le `CMakeLists.txt` — ou en
ligne de commande :

```bash
cmake -S . -B build
cmake --build build
./build/Exercice_5            # Windows : build\Debug\Exercice_5.exe
```

Le projet **compile et tourne tel quel** : le menu s'affiche, et toutes les actions sont
refusées. C'est normal — les méthodes de `Joueur` sont vides, et c'est à vous de les
remplir.

## Organisation du code

| Fichier | Rôle |
|---|---|
| `Exercice_5/main.cpp` | **Fourni, ne pas modifier.** Lit une commande, appelle une méthode |
| `Exercice_5/joueur.h` | **À compléter.** La classe `Joueur` et les cinq règles du jeu |

## Ce qu'il y a à faire

Chaque méthode de `joueur.h` porte un `// TODO` et le comportement attendu :

| Méthode | La règle à tenir |
|---|---|
| `courir()` | coûte 10 d'endurance, refuse si elle manque, ne descend jamais sous 0 |
| `seReposer()` | remonte l'endurance au maximum, jamais au-delà |
| `ouvrirPorte()` | consomme une clé, refuse s'il n'en reste pas |
| `acheter(prix)` | consomme l'or, refuse si l'or manque |
| `subirDegats(d)` | garde la vie entre 0 et le maximum |
| `estVivant()` | vrai tant qu'il reste de la vie |

## La règle qu'on vérifiera

**Aucun attribut public.** `main.cpp` ne connaît aucun compteur : il ne sait pas qu'une
course coûte 10, ni qu'il reste deux clés. Si vous vous surprenez à vouloir écrire
`joueur.endurance_ = …` depuis le menu, c'est qu'une méthode manque.

Le menu n'affiche que ce que `Joueur` veut bien lui dire, par `afficherFiche()` et
`estVivant()`.

## Vérifier que ça marche

```text
> c c c c c c      l'endurance tombe à 0, puis « Trop fatigue pour courir. »
> r                elle remonte à 50, pas à 60
> o o o            deux portes s'ouvrent, la troisième dit « Pas de cle. »
> a a              une potion achetée (30 → 5 d'or), la seconde refusée
> p p p p          la vie descend 70, 40, 10, 0 — jamais négative
```
