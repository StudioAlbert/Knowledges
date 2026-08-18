---
title: Setup GitHub for Unity
type: course
chapter: "0.0"
duration_h: 1
module: "🐣 - Beginner"
section:
  - SAE 1A
topic:
  - Basics
created: 2024-12-04T15:18
source: notion
---
# Setup GitHub for Unity

Outils à installer:

[Sourcetree | Free Git GUI for Mac and Windows](https://www.sourcetreeapp.com/)

[education.github.com](https://education.github.com/git-cheat-sheet-education.pdf)

### Créer un repo vide destiné à accueillir le projet Unity

### Option 1 : Créer le repo via ligne de commandes

### Ajouter un fichier .gitattributes :

[gitattributes/Unity.gitattributes at master · gitattributes/gitattributes](https://github.com/gitattributes/gitattributes/blob/master/Unity.gitattributes)

Objectif : gérer les fichiers binaires et/ou trop lourds

prendre le fichier ici avec lien ci-dessus

le poser à la racine du projet

le renommer en .gitattributes

### Ajouter un fichier .gitignore

[gitignore/Unity.gitignore at main · github/gitignore](https://github.com/github/gitignore/blob/main/Unity.gitignore)

Objectif : ne pas inclure les répertoires inutiles. Ex : Library (+1Go)

le projet se présente alors comme ca

![[setup_github_for_unity_01.png]]

### Passer les commandes nécessaires pour ajouter les fichiers

```powershell
echo "# UNITY PROJECT" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/StudioAlbert/xxxxx_nom_du_repo_xxxxx.git
git push -u origin main
```

### Option 2 : Cloner le repo + Copier les fichiers

![[setup_github_for_unity_02.png]]

via SourceTree

---

```powershell
git clone https://github.com/StudioAlbert/UnityEmpty UnityEmpty_ProjectFolder
```

---

### Ajouter un fichier .gitattributes :

[gitattributes/Unity.gitattributes at master · gitattributes/gitattributes](https://github.com/gitattributes/gitattributes/blob/master/Unity.gitattributes)

Objectif : gérer les fichiers binaires et/ou trop lourds

### Ajouter un fichier .gitignore

[gitignore/Unity.gitignore at main · github/gitignore](https://github.com/github/gitignore/blob/main/Unity.gitignore)

Objectif : ne pas inclure les répertoires inutiles. Ex : Library (+1Go)

---

le projet se présente alors comme ca

![[setup_github_for_unity_01.png]]

### Copier le contenu du projet Unity

![[setup_github_for_unity_03.png]]

### A partir d’ici, le projet est pret. Vous pouvez commit les changements

### Option 3 : Script

Lancer le script suivant dans votre repo, celui-ci ajoute les fichiers nécessaires.

[[init_repo_unity.sh|InitRepoUnity.sh]]
