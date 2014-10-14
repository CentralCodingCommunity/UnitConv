# Minimum CMake version allowed is 2.6
cmake_minimum_required (VERSION 2.6)

# Project is UnitConv
project(UnitConv)

# Set the output directory to ../bin (with respect to the CMakeLists file
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/../bin)

# Compile to create unitconv in the binary directory
add_executable(unitconv main.c)
