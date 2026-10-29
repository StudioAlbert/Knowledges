# C++ exercise packages

Course context: C++23, CLion, MSVC locally (vcpkg available), GoogleTest, autograding on GitHub
Actions. If the user's request or files show a different toolchain, follow theirs.

## Naming: Google C++ Style Guide (enforce strictly)

| Element | Convention | Example |
|---|---|---|
| Files | snake_case, `.h` / `.cc` | `path_finder.h`, `path_finder.cc` |
| Types (class, struct, enum, alias, concept) | PascalCase | `PathFinder`, `NodeCost` |
| Functions / methods | PascalCase | `FindPath()`, `ComputeHeuristic()` |
| Accessors / mutators (optional) | snake_case like the variable | `count()`, `set_count()` |
| Local variables, parameters | snake_case | `open_set`, `start_node` |
| Class data members | snake_case + trailing `_` | `grid_`, `max_iterations_` |
| Struct data members | snake_case, no underscore | `x`, `cost` |
| Constants (`constexpr`, static storage) | `k` + PascalCase | `kMaxAgents` |
| Enumerators | `k` + PascalCase | `kPatrol`, `kChase` |
| Namespaces | snake_case | `game_ai` |
| Macros (avoid) | UPPER_SNAKE | `GAME_AI_PATH_FINDER_H_` (header guard) |

Other rules to respect: 2-space indentation, 80-column lines, `#define` header guards of the form
`<PROJECT>_<PATH>_<FILE>_H_`, include order (related header, C system, C++ standard, other
libraries, project), no `using namespace` in headers, `explicit` single-argument constructors.
The guide targets C++20; if an exercise needs a C++23 feature, use it and mention it in instructor notes.

Starter code and solution must both follow the style: students imitate what they are given.

## Repository layout

```
<exercise-name>/
├── CMakeLists.txt
├── README.md                 # the brief (student-facing language)
├── include/<project>/...h
├── src/...cc
├── tests/..._test.cc
└── .github/workflows/autograde.yml
solution/                     # instructor-only, never in the student repo
rubric.md                     # instructor-only
```

## CMake with GoogleTest

Prefer `FetchContent` with a pinned tag so the CI runner needs no extra setup; switch to vcpkg if the
user says the course uses it.

```cmake
cmake_minimum_required(VERSION 3.24)
project(exercise LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG v1.15.2)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)  # MSVC
FetchContent_MakeAvailable(googletest)

add_library(exercise_lib src/path_finder.cc)
target_include_directories(exercise_lib PUBLIC include)

enable_testing()
add_executable(exercise_tests tests/path_finder_test.cc)
target_link_libraries(exercise_tests PRIVATE exercise_lib GTest::gtest_main)
include(GoogleTest)
gtest_discover_tests(exercise_tests)
```

## Tests

- One `TEST` per observable behaviour, named `<Unit>Test, <Behaviour>` in PascalCase
  (e.g. `TEST(PathFinderTest, ReturnsEmptyPathWhenGoalIsBlocked)`).
- Test messages should help students: use `<< "hint"` on assertions for common mistakes.
- Cover the edge cases the lesson discussed; tests are evidence for the Apply/Analyze outcomes.
- Starter code must compile and the tests must *fail* (not crash the build) until the TODOs are done.

## CI workflow

```yaml
name: Autograde
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure
        run: cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
      - name: Build
        run: cmake --build build --parallel
      - name: Test
        run: ctest --test-dir build --output-on-failure
```

If the user runs GitHub Classroom autograding with per-test points, generate the matching
autograding configuration instead and map points to the rubric.
