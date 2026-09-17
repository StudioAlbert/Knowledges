---
seances:
  - GPR-CF-BDP-01
  - GPR-CF-BDP-02
  - GPR-CF-BDP-03
---

# Exercices — 01 — Programming Basics

## Jeux de dé

### « Le Cochon » (version ultra-courte)

- Lance un dé à 6 faces plusieurs fois et additionne.
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
-  Theobald et Grimgor jouent chacun leur tour.
- À chaque tour, Theobald peut :
	- **Attaquer** — causer 5 points de dégâts
	- **Défendre** — ne cause pas de dégâts, permet de réduire de 70 % les dégâts subis à la prochaine attaque
	- **Se soigner** — récupérer 3 points de vie
- À son tour, Grimgor peut :
	- causer entre 2 et 8 points de dégâts à Theobald
	- il y a 10 % de chances que Grimgor invoque la waaagh et double ses dégâts
- Une fois l'un des personnages vaincu, afficher un message désignant le vainqueur.

##### A faire
1. **Analysez par écrit :**
	1. un tour de jeu des 2 personnages sous forme d'un schéma
	2. la séquence complète du programme
	3. la liste des variables et fonctions nécessaires
2. **Mise en œuvre :** un programme dans lequel Theobald est un personnage interactif via la console, et Grimgor un personnage géré par le programme.

## Monster fight
###### `Traduire le pseudocode suivant en programme C++`

- Chaque créature a une **initiative** qui détermine qui commence
- Chaque créature a une valeur de **défense** et une valeur d'**attaque**
### Pseudocode
```
If Creature A has a greater initiative than Creature B, then
    We calculate the hit probability from Creature A offense
        against Creature B Defense
    We throw the dices.
    If the result of the dice is higher than the probability, then
        Creature B avoids the attack
    Else, if the result of the dices is lower than the probability, then
        Creature B receives damages
Else, if Creature B has a greater initiative than Creature A, then
```