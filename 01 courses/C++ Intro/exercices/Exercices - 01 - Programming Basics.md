# Exercices — 01 — Programming Basics

> Source : [Google Docs](https://docs.google.com/document/d/1Rs7TPHEBmtbobBekCGwzW9WOclGp0Vn3HQBm3-Q70-g/edit)
> Cours associé : [[01.01 - Programming Basics - if, loops]]

## Jeux de dé

### « Le Cochon » (version ultra-courte)

- Lance un dé plusieurs fois et additionne.
- Tu peux t'arrêter quand tu veux.
- Mais si tu fais 1, tu perds tout et ton tour se termine.
- Si on dépasse 20, le jeu s'arrête, le score est bloqué.
- Variante avec D20, D8, D39, etc.

### Le « 421 » simplifié

- Chaque joueur lance 3 dés une fois.
- Le plus haut total gagne.

### Le 421 normal

Avec combinaisons.

## Versus Game

Theobald, le valeureux chevalier, s'attaque à Grimgor, l'orque noir.

Theobald et Grimgor jouent chacun leur tour.

À chaque tour, Theobald peut :

- **Attaquer** — causer 5 points de dégâts
- **Défendre** — ne cause pas de dégâts, permet de réduire de 70 % les dégâts subis à la prochaine attaque
- **Se soigner** — récupérer 3 points de vie

À son tour, Grimgor peut :

- causer entre 2 et 8 points de dégâts à Theobald
- il y a 10 % de chances que Grimgor invoque la waaagh et double ses dégâts

Une fois l'un des personnages vaincu, afficher un message désignant le vainqueur.

**Analysez par écrit :**

- un tour de jeu des 2 personnages sous forme d'un schéma
- la séquence complète du programme
- la liste des variables et fonctions nécessaires

**Mise en œuvre :** un programme dans lequel Theobald est un personnage interactif via la console, et Grimgor un personnage géré par le programme.
