cmake_minimum_required(VERSION 3.29)

project(apep
        VERSION 0.0.1
        DESCRIPTION ""
        LANGUAGES C CXX)

# Leave C++ standard up to the root application, so set it only if this is the
# current top-level CMake project.
if(CMAKE_SOURCE_DIR STREQUAL apep_SOURCE_DIR)
  set(CMAKE_CXX_STANDARD 20)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
  set(CMAKE_C_STANDARD 11)
  set(CMAKE_C_STANDARD_REQUIRED ON)
else()
  if(CMAKE_CXX_STANDARD LESS 20)
    message(FATAL_ERROR
      "thoth requires CMAKE_CXX_STANDARD >= 20 (got: ${CMAKE_CXX_STANDARD})")
  endif()
  if(CMAKE_C_STANDARD LESS 11)
    message(FATAL_ERROR
      "thoth requires CMAKE_C_STANDARD >= 11 (got: ${CMAKE_C_STANDARD})")
  endif()
endif()

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

# set(CMAKE_MODULE_PATH 
#   "${PROJECT_SOURCE_DIR}/cmake"
#   ${CMAKE_MODULE_PATH}
#   )

if (MSVC)
  # 4100 must be ignored as PyObject *self may be unreferenced
  add_compile_options(/permissive /WX /W4) # /wd4100) # /wd4251) #/wd4100)
else()
  add_compile_options(-Wall -Wextra -pedantic -Werror -Wno-unknown-pragmas)
endif()

# set(APEP_BUILD_DOCS OFF CACHE BOOL "Whether or not to build documentation.")
# set(APEP_BUILD_TESTS OFF CACHE BOOL "Whether or not to build tests.")

set(MODULE_ROOT "${PROJECT_SOURCE_DIR}/include")

if(NOT DEFINED PYTHON_EXTENSION_SUFFIX)
  if(WIN32)
    set(PYTHON_EXTENSION_SUFFIX ".pyd")
  else()
    set(PYTHON_EXTENSION_SUFFIX ".so")
  endif()
endif() 

add_subdirectory(thoth)
add_subdirectory(apep)

#if(APEP_BUILD_TESTS)
#  enable_testing()
#  add_subdirectory(tests)
#endif()

#if(APEP_BUILD_DOCS)
#  add_subdirectory(docs)
#  #Do I need to add pulse's dependancies as well or is that transitive!?
#  # add_dependencies(Doxygen <Target_dependancies>)
#endif()


