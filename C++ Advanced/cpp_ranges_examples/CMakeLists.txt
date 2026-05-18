cmake_minimum_required(VERSION 3.20)
project(cpp_ranges_examples LANGUAGES CXX)

# C++23 is required for examples 09/10 and both exercises
# (std::ranges::to, std::views::enumerate/zip/slide, std::ranges::fold_left).
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# One independent runnable target per lecture chapter.
add_subdirectory(examples/01_the_iterator_problem)
add_subdirectory(examples/02_range_concept_basics)
add_subdirectory(examples/03_range_algorithms_basics)
add_subdirectory(examples/04_composing_pipelines)
add_subdirectory(examples/05_projections_and_constraints)
add_subdirectory(examples/06_views_lazy_evaluation)
add_subdirectory(examples/07_owning_views)
add_subdirectory(examples/08_borrowing_views)
add_subdirectory(examples/09_ranges_to)
add_subdirectory(examples/10_cpp23_enumerate_zip_chunk)

add_subdirectory(exercises/01_refactor_classic_loop)
add_subdirectory(exercises/02_top3_followers)
