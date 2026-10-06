cmake_minimum_required(VERSION 4.2)
project("GPR-CF-POO-03 - Decoupage en fichiers")

set(CMAKE_CXX_STANDARD 23)

# Une seule source aujourd'hui. A chaque fichier sorti de main.cpp, ajoutez-le ici.
add_executable(Donjon
    "Exercice_5/main.cpp"
)
target_include_directories(Donjon PRIVATE "Exercice_5")
