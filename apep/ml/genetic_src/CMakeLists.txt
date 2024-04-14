# VV May extract to root (can we specifiy python and numpy separatly
find_package(Python3 COMPONENTS Development.Module REQUIRED)# NumPy)

set(sources 
  "genetic.cpp" 
  )

set(apep_genetic_module "")

add_library(apep_genetic SHARED ${sources})

target_sources(apep_genetic PUBLIC
  FILE_SET config_headers
  TYPE HEADERS
  BASE_DIRS ${MODULE_ROOT}
  FILES "${MODULE_ROOT}/_apep_config.h ${apep_genetic_module}"

)

target_include_directories(apep_genetic PUBLIC
  ${Python3_INCLUDE_DIRS}
  # ${Python3_NumPy_INCLUDE_DIRS}
  )

target_link_libraries(apep_genetic PRIVATE Python3::Module) #Python3::NumPy)

# target_compile_definitions(apep_genetic PRIVATE
                                   # NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION)
set_target_properties(apep_genetic PROPERTIES SUFFIX ${PYTHON_EXTENSION_SUFFIX})

if(WIN32)
  target_compile_definitions(apep_genetic PRIVATE APEP_BUILD_DLL)
endif()
  
if(WIN32)
  set_target_properties(apep_genetic PROPERTIES RUNTIME_OUTPUT_NAME "genetic")
else()
  set_target_properties(apep_genetic PROPERTIES LIBRARY_OUTPUT_NAME "genetic")
endif()



