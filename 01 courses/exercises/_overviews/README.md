# Overviews d'exercices — en attente de validation

Le build du site ignore tout dossier dont le nom commence par `_`. Ce dossier accueille
donc les fiches d'exercices encore à l'état d'**overview** — quelques lignes par exercice —
**quand la séance est déjà publiée** : leur poser la fiche directement dans
`exercises/<matière>/` la mettrait en ligne pour les étudiants.

Une fois l'exercice écrit, déplacer le fichier dans `exercises/<matière>/` et corriger le
lien de la note de séance, qui pointe en chemin complet.

Les séances dont le deck n'est pas publié (`publish: false`) n'ont pas besoin de ce détour :
leur fiche vit directement dans `exercises/<matière>/` et reste invisible tant que le deck
n'est pas publié.
