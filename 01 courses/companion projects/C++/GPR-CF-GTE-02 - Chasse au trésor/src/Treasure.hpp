#pragma once

// Tire au sort une coordonnée (colonne ou ligne) sur la plage.
int randomCoordinate();

// Nombre de cases qui séparent la case creusée du trésor
// (déplacements horizontaux + verticaux).
int distanceToTreasure(int column, int row, int treasureColumn, int treasureRow);
