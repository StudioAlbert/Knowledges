# Exercices — GPR-UN-VRG-01 — Formative 3 : shooter spatial isométrique 2.5D

> [!info] Terrain de jeu
> **Votre propre dépôt**, un projet neuf. Unity **6000.3**, template 3D (URP). Le spawner que
> vous avez bâti en séance 6 est le point de départ : reprenez-le.
>
> Références de genre : [Steredenn](https://www.youtube.com/watch?v=Pu9xEWhsfxg),
> [Steambirds Alliance](https://youtu.be/wAa2Ay3eVUQ),
> [From Space](https://www.youtube.com/watch?v=4Eib4mX4SkM) pour la caméra isométrique à 45°.
>
> **C'est la formative de fin de module** : tout ce qui a été vu est utilisable, et la boucle
> de jeu complète est attendue. Vous n'avez pas vu les ScriptableObjects ni les patterns
> d'architecture — ils sont au programme de 2e année. Un `HudManager` et des composants bien
> découpés suffisent.

**Temps encadré** : les workshops des séances 20 à 25, plus **2 créneaux spécifiques** le
vendredi 12 février. Terminé à la maison avant les summatives du 15 février.

## Noyau — 14 points sur 20 · *[Create]*

Chaque brique ci-dessous est une technique vue en cours ; c'est leur assemblage en un
jeu jouable, depuis un projet vide, qui est évalué ici.

### 1 — Le vaisseau et la caméra · *[Apply]*

Déplacement du vaisseau sur un plan, caméra **orthographique fixe à 45°**. La profondeur est
dans le rendu, pas dans le gameplay : tout se joue sur un plan.

### 2 — Deux armes, deux familles · *[Apply]*

- **Missile** : un prefab instancié depuis un point de tir, propulsé en ligne droite, avec une
  durée de vie et un **recyclage** — pas un `Instantiate` par frame qui laisse mille objets
  morts dans la hiérarchie.
- **Laser** : un faisceau **continu au raycast**, qui inflige des dégâts tant qu'il est actif,
  avec un point d'impact visible.

Les deux sur des touches distinctes, et une cadence pour chacune.

### 3 — Les ennemis · *[Apply]*

Apparition par **vagues** : le placement vient de la séance 6 — zones de spawn, répartition
contrôlée, jamais dans un mur ni dans le dos du joueur — et la **cadence d'une coroutine**,
séance 20. Une IA simple suffit : avancer selon un motif, ou se diriger vers le joueur.

> [!note] Hors périmètre, volontairement
> La montée en difficulté et le budget d'entités simultanées sont renvoyés au module 3.
> Une cadence constante par vague est ce qui est attendu ici — ne cherchez pas à équilibrer
> une courbe.

### 4 — Santé, dégâts et mort · *[Apply]*

Pour le joueur et pour les ennemis : prendre des dégâts, mourir, disparaître. Le missile, le
laser et la collision passent par **le même chemin de dégâts**. Le retour visuel et sonore est
découplé de la prise de dégâts.

### 5 — L'interface · *[Apply]*

Un `HudManager` qui expose `SetScore` et `SetHealth` — c'est exactement le schéma du brief
d'origine. Un menu principal en UI Toolkit, un écran de game over, et le **rechargement de
scène** pour rejouer.

### 6 — Le son · *[Apply]*

Tir, impact, explosion, et un retour de fin de partie. Branchés sur les événements du jeu, pas
appelés depuis dix endroits : passez par le gestionnaire de sons de la séance 25.

## Options — 6 points sur 20

**Deux au choix**, et vous justifiez le choix en trois lignes dans le README : ce que chacune
apporte au jeu que vous avez fait, pas à un jeu en général. *[Evaluate]*

- **Power-ups et ramassage** — tir rapide, soin, bouclier temporaire ; détection et captation
  comme en séance 23.
- **Obstacles** — astéroïdes qui dérivent, mines qui s'activent à l'approche, barrières de
  laser qui pulsent.
- **Juice** — particules de tir, d'impact et d'explosion, camera shake, arrêt sur image au
  coup qui porte, défilement de fond en parallaxe.

## Barème — sur 20

| Critère | Pts | Non acquis | En cours | Acquis |
|---|---|---|---|---|
| Vaisseau et caméra | 2 | Caméra en perspective ou qui suit | Isométrique mais cadrage ou échelle faux | Orthographique à 45°, échelle lisible, déplacement net |
| Les deux armes | 4 | Une seule famille de tir | Les deux présentes, pas de recyclage ou laser factice | Missile recyclé, laser au raycast avec impact, cadences réglées |
| Vagues d'ennemis | 3 | Ennemis posés à la main | Spawn aléatoire non contrôlé | Zones respectées, cadence en coroutine, vagues lisibles |
| Dégâts et mort | 3 | Destruction directe sans santé | Santé présente, chemins de dégâts dupliqués | Un seul chemin de dégâts, mort propre, feedback découplé |
| Interface et son | 2 | Pas de HUD ni de fin de partie | HUD complet mais couplé | `HudManager` découplé, menu, game over, rechargement, sons branchés sur les événements |
| Les deux options | 6 | Aucune, ou non fonctionnelles | Une seule, ou deux à moitié | Deux options qui tiennent, et un choix justifié |

## Livrables

```bash
git switch -c formative-3-shooter
# ... votre travail
git push -u origin formative-3-shooter
```

Puis **un build publié en release**, comme en séance 3 :

```bash
gh release create v1.0-formative3 --notes "Shooter isometrique, rendu du module 2" ./Build.zip
```

Un `README.md` à la racine : les contrôles, les deux options choisies et pourquoi, ce qui est
fait et ce qui ne l'est pas, les bugs connus. **Rien sur le NAS.**

> [!check] Réussi si
> - Quelqu'un télécharge la release, lance l'exécutable et joue **sans ouvrir Unity** ;
> - les deux armes se sentent différentes, et pas seulement en dégâts ;
> - cent missiles tirés ne laissent pas cent objets dans la hiérarchie ;
> - mourir affiche l'écran de fin et rejouer repart d'une scène propre ;
> - couper le son dans le mixer éteint tout, sans toucher au code ;
> - vos deux options sont jouables et vous savez dire ce qu'elles changent.
