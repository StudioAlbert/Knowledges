---
type: bloc
specialisation: "[[C++]]"
mineur: Games Programming
prerequis:
  - "[[Structure de Programme et Bonnes Pratiques]]"
projet:
  - "[[City Builder]]"
cours: 9
---

# Patterns et Persistance

Construire des objets complexes lisiblement, découpler l'action de son exécutant, partager ce qui peut l'être, puis écrire le tout sur disque.

## Objectifs

- Remplacer un constructeur télescopique par un builder chaînable
- Encapsuler une action en objet Command, et la rendre annulable
- Mutualiser l'état partagé avec un Flyweight quand le nombre d'instances explose
- Aplatir un état de jeu en texte ou en binaire, et le relire fidèlement

## Cours

<!-- cours:auto -->

| # | Cours | Heures | Lien |
| --- | --- | --- | --- |
| 1 | C++ Builder | 2 | [[cpp_builder_lecture]] |
| 2 | Command Pattern | 3 | [[cpp_command_pattern_lecture]] |
| 3 | Flyweight Pattern | 3 | [[cpp_flyweight_pattern_lecture]] |
| 4 | Sérialisation & systèmes de sauvegarde | 1 | [[cpp_serialization_lecture_fr]] |

**Total : 4 cours, 9 h.**

<!-- /cours:auto -->

## Validation

Système de sauvegarde du projet : état sérialisé, rechargé, et vérifié identique.

## Liens

- Spécialisation : [[C++]]
- Prérequis : [[Structure de Programme et Bonnes Pratiques]]
- Bloc suivant : [[Communication et Robustesse]]
- Index des cours : [[index_cours.base|Index]]
