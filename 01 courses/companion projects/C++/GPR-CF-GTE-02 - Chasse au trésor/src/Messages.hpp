#pragma once

// Tout ce que le jeu affiche ou demande au joueur.

void printWelcome();

// Demande une colonne (0 = abandonner) puis une ligne.
int askColumn();
int askRow();

void printHint(int distance);
void printVictory(int attempts);
void printGiveUp(int treasureColumn, int treasureRow);
void printDefeat(int treasureColumn, int treasureRow);
