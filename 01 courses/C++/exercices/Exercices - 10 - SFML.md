# Exercices — 10 — SFML

> Source : [Google Docs](https://docs.google.com/document/d/1ZzOUGYoPifzRVayYXEMqtfw6FAQxh_FV_tHuNCgQkB4/edit)
> Cours associé : [[10 - SFML]]

## Niveau 1 : découverte des bases

1. **Fenêtre simple**
    - Crée une fenêtre SFML qui s'ouvre et reste ouverte jusqu'à ce que l'utilisateur appuie sur une touche ou ferme la fenêtre.
    - Ajoute un titre à la fenêtre.
2. **Afficher des formes géométriques**
    - Dessine un rectangle, un cercle et une ligne dans la fenêtre.
    - Change leurs couleurs et leurs positions.
3. **Manipulation du texte**
    - Affiche du texte (comme « Hello SFML ») au centre de la fenêtre.
    - Change la taille, la police et la couleur du texte.
4. **Détection des événements clavier**
    - Écoute les événements clavier et affiche dans la console quelle touche a été pressée.
5. **Déplacement d'une forme**
    - Dessine un rectangle à l'écran, puis fais-le se déplacer en maintenant les flèches directionnelles.

## Niveau 2 : animation et interaction

1. **Animation simple**
    - Fais bouger un cercle dans la fenêtre automatiquement (par exemple, de gauche à droite).
    - Ajoute une détection des bords pour qu'il rebondisse lorsqu'il les atteint.
2. **Contrôle avec la souris**
    - Permets à l'utilisateur de déplacer un rectangle en suivant la position de la souris.
3. **Collision entre objets**
    - Ajoute deux rectangles mobiles et détecte leur collision (par exemple, change leur couleur lorsqu'ils se touchent).
4. **Création d'un sprite animé**
    - Charge une texture depuis un fichier.
    - Anime un personnage en affichant différentes portions d'une image en fonction du temps.

## Niveau 3 : gestion avancée

1. **Détection des clics sur des objets**
    - Place plusieurs rectangles sur l'écran et détecte lequel est cliqué par la souris.
2. **Création d'une caméra**
    - Implémente une caméra qui suit un joueur (un rectangle ou un sprite) lorsqu'il se déplace.
3. **Menu interactif**
    - Crée un menu simple avec plusieurs boutons (exemple : *Jouer*, *Options*, *Quitter*).
    - Permets la navigation entre les options avec la souris ou le clavier.

## Niveau 4 : mini-jeux complets

1. **Pong**
    - Programme un jeu complet de Pong avec deux raquettes, une balle et un score.
2. **Shoot 'em up**
    - Crée un jeu simple où un joueur peut déplacer un vaisseau et tirer des projectiles pour détruire des ennemis qui descendent depuis le haut de l'écran.
3. **Labyrinthe**
    - Génère un labyrinthe simple et permets au joueur de déplacer un personnage pour trouver la sortie.
4. **Jeu de plateforme**
    - Crée un petit jeu où un personnage peut sauter entre des plateformes, avec une gravité simple et des collisions.
5. **Jeu de type Flappy Bird**
    - Implémente un jeu où le joueur doit cliquer ou appuyer sur une touche pour maintenir un personnage dans les airs et éviter des obstacles.

## Niveau 5 : concepts avancés

1. **Effets sonores et musique**
    - Ajoute des effets sonores pour les interactions (par exemple, un clic ou une collision).
    - Joue une musique de fond qui peut être mise en pause ou arrêtée.
2. **Système d'état pour un jeu**
    - Implémente un système d'états (menu principal, jeu, écran de pause, etc.).
3. **Intelligence artificielle simple**
    - Implémente un comportement simple pour des ennemis qui poursuivent ou fuient le joueur.
4. **Système de sauvegarde**
    - Permets au joueur de sauvegarder et de charger sa progression (par exemple, position, score).
5. **Création d'un éditeur de niveaux**
    - Crée une interface où l'utilisateur peut placer des éléments (comme des plateformes ou des ennemis) dans un niveau et sauvegarder la configuration.
