cmake_minimum_required(VERSION 4.3)
project(Inheritance)

set(CMAKE_CXX_STANDARD 23)

add_executable(Inheritance main.cpp
        src/hero.cc
        include/hero.hpp
        src/archer.cc
        include/archer.hpp
        src/wizard.cc
        include/wizard.hpp
        include/ranger.hpp
        src/ranger.cc)
