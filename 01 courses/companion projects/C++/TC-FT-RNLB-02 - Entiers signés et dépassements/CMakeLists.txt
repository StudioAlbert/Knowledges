cmake_minimum_required(VERSION 3.28)
project(EntiersSignes LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(EntiersSignes
        src/main.cpp
)

# Avertissements : on veut VOIR les mélanges signé / non signé (slide « Mélanger »)
if (MSVC)
    target_compile_options(EntiersSignes PRIVATE /W4 /utf-8)
else ()
    target_compile_options(EntiersSignes PRIVATE -Wall -Wextra -Wsign-compare)
endif ()

# Détecteur de comportements indéfinis (GCC / Clang, hors Windows) :
#   cmake -S . -B build -DSANITIZE=ON
option(SANITIZE "Active -fsanitize=undefined" OFF)
if (SANITIZE AND NOT MSVC)
    target_compile_options(EntiersSignes PRIVATE -fsanitize=undefined)
    target_link_options(EntiersSignes PRIVATE -fsanitize=undefined)
endif ()
