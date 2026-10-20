---
seances: [TC-FT-PCL-01, TC-FT-PCL-03, TC-FT-PCL-04]
---
# Concevoir un platformer

**Un seul atelier, repris trois fois.** Les trois séances du bloc travaillent sur **la même
conception** : vous la dessinez en PCL-01, vous y cherchez des patterns en PCL-03, et vous
tranchez héritage ou composition en PCL-04. Le rendu final est **un schéma**, pas du code.

> [!important] Ce schéma sert ensuite — selon votre classe
> **GP-926** : c'est le jeu que vous écrirez en SFML dans le bloc *SFML et Box2D*, à partir
> du 28 octobre. Le schéma rendu ici est votre point de départ, et vous le reprendrez en
> main à la première séance.
> **WEB-925** : l'exercice s'arrête au schéma. C'est la conception qui est évaluée, pas une
> implémentation.

---

## Le jeu, en six lignes

Tout le monde conçoit **le même** jeu, pour que les schémas soient comparables :

- un **héros** qui court, saute, et qu'on pilote au clavier ;
- un **niveau** fait de sol, de plateformes, d'un mur et d'une plateforme traversable ;
- de la **physique** : gravité, collisions, et un saut interdit en l'air ;
- des **sprites** animés, une caméra qui suit le héros ;
- des **sons** : un bruit de saut, une musique de fond ;
- une **fin** : atteindre la sortie, ou tomber.

Rien de plus. Un ennemi, un score, un menu : hors sujet pour cet atelier.

---

## Étape 1 — Dessiner la conception

> Séance [[01 courses/slides/Theory/TC-FT-PCL-01 - Couplage et cohésion|TC-FT-PCL-01]] — 20 min

**Ce qu'on produit** : une liste de fonctionnalités, une liste de classes, et les relations
entre elles.

1. **Les fonctionnalités**, d'abord. Une ligne par chose que le jeu sait faire, du point de
   vue du joueur.
2. **Les classes** ensuite, déduites de cette liste. Pour chacune, écrivez **une phrase** qui
   dit ce dont elle est responsable. Si la phrase a besoin d'un « et », la classe en fait
   déjà deux.
3. **Les relations**, enfin. Trois sortes de flèches, et pas une de plus :
   - `A ──▶ B` — A **utilise** B (il l'appelle, il en dépend)
   - `A ──◆ B` — A **contient** B (B est un membre de A)
   - `A ──▷ B` — A **est un** B (héritage)

> [!tip] Le piège
> Une classe `Jeu` qui connaît tout le monde n'est pas une conception, c'est la liste des
> variables globales en costume. Si votre schéma a une boîte reliée à toutes les autres,
> l'étape 1 n'est pas finie.

---

## Étape 2 — Y chercher des patterns

> Séance [[01 courses/slides/Theory/TC-FT-PCL-03 - Taxonomie des patterns|TC-FT-PCL-03]] — 20 min

**Ce qu'on produit** : votre schéma, annoté — et au moins un « non » assumé.

1. Reprenez votre schéma et posez la question une boîte à la fois : **peut-on reconnaître un
   pattern ici ?** Les six de la séance sont les seuls candidats.
2. Pour chaque pattern que vous croyez reconnaître, écrivez les **trois** entrées : le
   problème qu'il règle *dans votre jeu*, comment il le règle, et la métaphore.
3. Trouvez au moins **un endroit où la réponse est non** : du code simple suffit, et le
   pattern ne ferait qu'ajouter des fichiers. Dites lequel vous avez été tenté d'y mettre.
4. Si vous n'en reconnaissez aucun, c'est une réponse valable — mais écrivez alors **ce qui
   devrait changer dans le jeu** pour qu'un pattern devienne utile.

> [!tip] Le piège
> Un pattern placé parce qu'on vient de l'apprendre est le défaut que la séance vous a
> montré. Le `State` du héros se défend très bien ; une fabrique abstraite pour deux types
> de plateformes **seulement**, beaucoup moins.

---

## Étape 3 — Identifier les relations

> Séance [[01 courses/slides/Theory/TC-FT-PCL-04 - Composition contre héritage|TC-FT-PCL-04]] — 20 min

**Ce qu'on produit** : le schéma final, où chaque flèche d'héritage est justifiée.

1. **Y a-t-il des héritages possibles ?** Cherchez les fonctionnalités partagées entre
   plusieurs objets du jeu — sauter, tomber, être poussé, être dessiné, faire du bruit,
   blesser. Une plateforme mobile est-elle un mur qui bouge, ou un objet qui a un
   déplacement ?
2. Pour chaque relation de votre schéma, **imaginez la phrase « X est un Y »** en entier.
   Si elle sonne faux, remplacez la flèche par une composition `──◆` ; si elle sonne juste,
   l'héritage est envisageable.
3. Posez-vous alors l'autre question : **cet héritage est-il problématique**, bloquant ou
   contraignant pour le reste du programme ?
4. Ajoutez **une fonctionnalité qui n'était pas prévue** — un ennemi volant qui tire, par
   exemple — et dites combien de classes votre schéma doit gagner pour l'accueillir.

> [!tip] Le piège
> Composer ne veut pas dire « un framework de composants ». Dans un platformer de cette
> taille, la composition commence par **un membre de plus dans une classe**. Si votre réponse
> à la question 2 est « j'écris un ECS », vous avez répondu à côté.

---

## Le rendu

Un document :

| | Ce qui est attendu |
|---|---|
| **le schéma** | une boîte par classe, les trois sortes de flèches, et rien d'autre dessus |
| **les responsabilités** | une phrase par classe, sans « et » |
| **les justifications** | une ligne par flèche d'héritage, et une ligne pour le pattern que vous n'avez pas mis |
| **l'ajout** | la fonctionnalité imprévue de l'étape 3, et ce qu'elle coûte à votre schéma |

L'outil est libre : Excalidraw, draw.io, Mermaid. Ce qui est évalué est
la conception, pas la beauté du trait.

> [!check] Grille d'auto-évaluation
>
> | Je sais… | Vérification |
> |---|---|
> | séparer fonctionnalité et classe | ma liste de départ ne contient aucun nom de classe |
> | nommer une responsabilité | aucune de mes phrases n'a besoin d'un « et » |
> | lire une dépendance | je peux désigner la classe la plus coûteuse à changer, et le dire en une phrase |
> | reconnaître un pattern sans en inventer | j'ai au moins un endroit où j'ai répondu « non » |
> | justifier un héritage | chacune de mes flèches `──▷` tient dans un « est un » qui sonne juste |
> | mesurer un ajout | je sais dire ce que coûte une fonctionnalité imprévue |
