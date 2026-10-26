---
slides: "[[01 courses/slides/C++/GPR-CF-SBD-04 - Le monde Box2D]]"
---
- [x] la conversion est fausse 180px <-> 1,8 m = 100px/m et non 32px/m
- [x] Aller sur Box2D la plus recente, adapter les decks, creer 2 exemples dans le companion (Physique simple + Contacts)

## Traité le 20.10 — Box2D 3.2

Les trois decks qui touchent à la physique sont réécrits : **SBD-04, SBD-05 et SBD-06**.
Chaque appel est vérifié sur la documentation officielle de Box2D **3.2**, pas écrit de
mémoire — le modèle a trop changé pour ça.

| Box2D 2.4 | Box2D 3.2 |
|---|---|
| `b2World monde(gravite)` | `b2WorldDef def = b2DefaultWorldDef(); b2CreateWorld(&def)` |
| `monde.Step(dt, 8, 3)` | `b2World_Step(monde, dt, 4)` — un seul compte de sous-pas |
| `b2Body*`, `b2Fixture*` | `b2BodyId`, `b2ShapeId` — des **identifiants**, pas des pointeurs |
| `b2PolygonShape` + `SetAsBox` | `b2Polygon boite = b2MakeBox(hx, hy)` |
| `b2FixtureDef` + `CreateFixture` | `b2ShapeDef` + `b2CreatePolygonShape` — **la fixture a disparu** |
| `def.friction`, `def.restitution` | `def.material.friction`, `def.material.restitution` |
| `corps->GetPosition()` | `b2Body_GetPosition(corps)` → `b2Pos` |
| `corps->GetAngle()` | `b2Rot_GetAngle(b2Body_GetRotation(corps))` |
| `b2ContactListener` + `BeginContact` | `b2World_GetContactEvents(monde)`, **lu après le pas** |
| `PreSolve` dans l'écouteur | `b2World_SetPreSolveCallback`, le seul rappel qui reste |

### Ce que le changement apporte au cours

**Les contacts ne sont plus des rappels.** Box2D 3 range les événements et on les lit après
`b2World_Step`. Ça supprime la mise en garde « ne créez rien dans le callback » qui occupait
une slide : la simulation est finie quand on lit. C'est plus simple à enseigner **et** plus
simple à écrire.

**Un piège neuf, et il est sérieux.** `enableContactEvents` et `enableSensorEvents` valent
**false par défaut**. Sans eux, la boucle d'événements tourne à vide et on cherche une heure
une erreur qui n'existe pas. Les deux slides concernées le disent en première ligne de code,
pas en note de bas de page. Et pour les capteurs, **les deux** formes doivent l'activer.

**Plus rien à libérer.** `b2DestroyWorld` emporte tout. La slide qui disait « le monde
possède ses corps, aucun `delete` » dit maintenant « des identifiants, rien à libérer ».

### Vérifié

SBD-04 13 slides, SBD-05 15, SBD-06 20 — **aucune hors cadre**. Plus aucune trace de
`b2FixtureDef`, `CreateFixture`, `b2ContactListener`, `SetAsBox` ni `->GetPosition()` dans
les decks.

> [!warning] Ce qui n'est pas vérifié
> **Rien de ce code n'a été compilé.** Il n'y a pas de cible Box2D dans le dépôt d'exemples,
> donc aucun moyen de l'essayer. Les signatures viennent de la doc 3.2, mais une ligne qui
> se lit bien n'est pas une ligne qui compile — en particulier `b2Pos` et
> `b2World_SetPreSolveCallback`, dont je n'ai lu que la déclaration.

## Traité le 26.10 — la conversion passe à 100 px/m

Tu avais raison, et le chiffre était le tien : `180 / 1,8 = 100`, pas 32. Le schéma
montrait un héros de 180 px en face d'un héros de 1,8 m, et annonçait un facteur de
32 px/m juste entre les deux.

J'ai gardé **100 px/m** plutôt que de rapetisser le héros à 57,6 px. Deux raisons :

- un mètre vaut cent pixels, donc la conversion se vérifie de tête, sans calculette ;
- les sprites fournis dans `_Resources/sprites/` sont grands — à 32 px/m, un
  personnage Cuphead mesurerait cinq mètres.

| Fichier | Ce qui change |
|---|---|
| `tools/schemas/sbd04_metres_pixels.py` | `1 m = 100 px`, et les deux formules |
| `00 images/sbd04_metres_pixels.svg` | régénéré, 23 éléments |
| Deck SBD-05, *Une seule classe sait convertir* | `kPixelsParMetre = 100.f` |
| Summative, *Les réglages* | `kPixelsParMetre = 100.f` |

La phrase « le jour où il devient `48` » devient « le jour où il devient `64` » :
48 était un multiple de 32, il ne voulait plus rien dire à côté de 100.

Le reste du deck SBD-04 est juste : `b2MakeBox(0.4f, 0.9f)` décrit bien un héros de
0,8 m sur 1,8 m, puisque ce sont des **demi**-dimensions.

> [!done] Les deux exemples du companion
> La case « creer 2 exemples dans le companion » était cochée mais les cibles
> n'existaient pas. Le dépôt `GPR-CF-SBD-XX---Box2D-Examples` existe en revanche,
> et tu l'as poussé le 26.10 — voir la fiche générale `GPR-CF-SBD-xx - SFML` pour
> son état et son portage.
