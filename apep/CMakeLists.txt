set(ROOT_FOLDER_NAME "Apep")

add_subdirectory("ml")


get_directory_property(subdirectories SUBDIRECTORIES) 

foreach(dir ${subdirectories})
  get_directory_property(subtargets DIRECTORY ${dir} BUILDSYSTEM_TARGETS)
  if(subtargets)
    set_target_properties(${subtargets} PROPERTIES FOLDER ${ROOT_FOLDER_NAME})
  endif()
endforeach()


