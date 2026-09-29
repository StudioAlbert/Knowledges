cmake_minimum_required(VERSION 3.28)
project(ChasseAuTresor LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Sources en UTF-8 (accents dans les commentaires)
if (MSVC)
    add_compile_options(/utf-8)
endif ()

add_executable(ChasseAuTresor
        src/main.cpp
        src/Game.cpp
        src/Treasure.cpp
        src/Messages.cpp
)
