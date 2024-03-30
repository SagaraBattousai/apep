cmake_minimum_required(VERSION 3.15)

project(Project_Name
        VERSION 0.0.1
        DESCRIPTION ""
        LANGUAGES C CXX)

include(cmake/inplace_build.cmake)

# Add Interpreter if needed and remove NumPy if not used but as it is so
# common it is left by default.
find_package(Python3 COMPONENTS Development NumPy REQUIRED) 

message(DEBUG ${Python3_NumPy_VERSION})

set(BUILD_PYTHON_EXTENSIONS ON CACHE BOOL 
"Whether to build Python C Extension Libraries and set the appropriate \
extension") 

set(PYTHON_EXTENSION_DOC_STRING
"Do not manually change this variable unless you are sure you need/want to. \
Using setup.py with CMake_Extensions will set this automatically and running \
CMake with variables left as default will set the correct extension for \
libraries without the python version information that setup.py includes.")

if (BUILD_PYTHON_EXTENSIONS AND (NOT PYTHON_EXTENSION))
  if (${WIN32})
    set(PYTHON_EXTENSION ".pyd" CACHE STRING ${PYTHON_EXTENSION_DOC_STRING})
  else()
    set(PYTHON_EXTENSION ".so"  CACHE STRING ${PYTHON_EXTENSION_DOC_STRING})
  endif()
endif()

# TODO: Decide whether to keep tis or if its only for developers not users
set(BUILD_EXTENSIONS_INPLACE OFF CACHE BOOL 
  "Whether to copy the built Python C Extension Libraries to the source \
directory the module expects if running as uninstalled package \
(useful for running tests on CI etc and to not require pip install \
for tasks such as running tests etc)")

# TODO: decide src structure, may be easier/more repeatable to keep outside
# python dir
add_subdirectory("project_name/core")