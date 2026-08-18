---
theme: white
css:
  - _templates/css/sae_styles.css
slideNumber: true
transition: slide
---

# Good practices
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

### Nomenclature, structuration, revue de code

<small>Module 4FSC0PF001 · Introduction to Games Programming</small>

Note:
Séance de revue de code. La seconde moitié de la présentation d'origine
est constituée de captures d'écran de travaux d'étudiants, commentées à
l'oral ; seuls les titres — c'est-à-dire le défaut pointé — sont
transposables ici.

---

## Source
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

<div style="color:#fff;">

Présentation d'origine (les captures de code commentées ne sont pas transposables) :

- 🔗 [Google Slides — 04 Good practices](https://docs.google.com/presentation/d/1dIT049niktL7A22lJyLSuI_pzI_-vfL2M7tCTxg3t5s/edit)

Dépôt d'exemples :

- 🔗 [github.com/StudioAlbert/CPlusPlus-Class-GoodPractices](https://github.com/StudioAlbert/CPlusPlus-Class-GoodPractices)

</div>

---

## Analyse de quelques travaux
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

🔗 [github.com/StudioAlbert/CPlusPlus-Class-GoodPractices](https://github.com/StudioAlbert/CPlusPlus-Class-GoodPractices.git)

---

# Conventions
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

---

## Nomenclature
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

**1 solution** qui contient les projets.

Nom du projet :

```
03 - Classroom - Data Structures - Vector
```

| Segment | Signification |
|---|---|
| `03` | n° de chapitre |
| `Classroom` | type de projet |
| `Data Structures` | nom du chapitre de cours |
| `Vector` | sujet traité dans le projet |

Les types de projet : **Classroom** (projet servant à illustrer le cours), **Exercice**, **Formative**.

---

## Règles de nommage — variables
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

| Convention | S'applique à |
|---|---|
| `PascalCase` | classes, public methods, properties, variables |
| `camelCase` | parameters, local variables, private / local methods, functions |
| `_underscore` | private & protected fields |
| `CAPITALS` | constants |

<small>[Microsoft — C# coding conventions](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) · [Vidéo de référence](https://www.youtube.com/watch?v=NQ6P7ecpdlY&t=302s)</small>

---

## Structuration de la solution
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Note:
Diapo constituée uniquement d'une capture de l'explorateur de solution.
Se référer à la présentation Drive, ou au dépôt d'exemples.

---

# Revue de code
<!-- .slide: data-background="_images/01_slide_GP_GA_22_08_22.jpg" -->

Note:
Les diapos qui suivent étaient chacune une capture de code d'étudiant.
Le titre énonce le défaut ; le code correspondant est à retrouver dans la
présentation d'origine ou dans le dépôt d'exemples.

---

## Utilisation du `for`
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

**La condition de sortie n'utilise pas la variable déclarée.**

---

## Répétition du code
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

Déplacement dans le programme → déplacement dans une fonction.

---

## La fonction ne remplit pas « vraiment » sa fonction
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

- **En théorie** : retourne la valeur.
- **Dans les faits** : retourne la valeur **plus le mot de liaison**.

---

## Ce cas arrive-t-il vraiment ?
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

À commenter.

---

## Fonction transparente
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->

La valeur traverse la fonction…

---

## Mélange de conditions
<!-- .slide: data-background="_images/01_slide_fond_GP_22_08_22.jpg" -->
