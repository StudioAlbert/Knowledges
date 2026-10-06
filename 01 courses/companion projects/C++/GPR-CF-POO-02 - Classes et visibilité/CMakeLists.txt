cmake_minimum_required(VERSION 4.2)
project("GPR-CF-POO-02 - Classes et visibilité")

set(CMAKE_CXX_STANDARD 23)

add_executable(Exercice_5 "Exercice_5/main.cpp" "Exercice_5/joueur.h")
target_include_directories(Exercice_5 PRIVATE "Exercice_5")
