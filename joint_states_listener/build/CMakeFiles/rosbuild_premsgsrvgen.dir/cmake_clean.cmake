file(REMOVE_RECURSE
  "../srv_gen"
  "../srv_gen"
  "../src/joint_states_listener/srv"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/rosbuild_premsgsrvgen.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
