FROM openease/kinetic-swi
MAINTAINER  kaadje at ttu dot ee 

# Initialize the catkin workspace
USER ros
WORKDIR /home/ros/src
RUN /usr/bin/python /opt/ros/kinetic/bin/catkin_init_workspace

RUN echo "Cloning repositories..."
RUN git clone --recursive https://github.com/knowrob/knowrob.git -b kinetic && \

    #git clone --recursive https://github.com/knowrob/knowrob_addons.git -b kinetic && \
    
    git clone https://github.com/code-iai/iai_maps.git && \
    git clone https://github.com/code-iai/iai_common_msgs.git && \
    git clone https://github.com/code-iai/iai_cad_tools.git && \
    git clone https://github.com/RobotWebTools/mjpeg_server.git && \
    git clone https://github.com/RobotWebTools/tf2_web_republisher.git
    #git clone https://github.com/andreihaidu/knowrob_robcog.git
    
RUN git clone https://github.com/knowrob/rosowl.git && \
    git clone https://github.com/mtenorth/knowrob_tutorials.git && \
    git clone https://github.com/knowrob/genowl.git && \
    #git clone https://github.com/knowrob/knowrob_srdl.git -b kinetic && \
    #git clone https://github.com/strands-project/mongodb_store.git -b kinetic-devel && \
    
    git clone https://github.com/ease-crc/ease_ontology.git && \
    git clone https://github.com/ease-crc/dul.git && \
    
    git clone --recursive https://github.com/knowrob/knowrob_addons.git -b kinetic
    
RUN git clone https://github.com/knowrob_maps -b kinetic 
    
#pkgs with problems, patially remove for now.
# RUN touch knowrob_addons/knowrob_learning/CATKIN_IGNORE
# RUN touch knowrob_addons/knowrob_sim_games/CATKIN_IGNORE
# RUN touch knowrob_addons/knowrob_chemlab/CATKIN_IGNORE
# RUN touch knowrob_addons/knowrob_cloud_logger/CATKIN_IGNORE
# RUN touch knowrob_addons/knowrob_cram/CATKIN_IGNORE
# RUN touch knowrob_addons/knowrob_memory_graph/CATKIN_IGNORE
# RUN touch knowrob_addons/knowrob_plan_summary/CATKIN_IGNORE
#RUN rm -r -f knowrob_addons
#RUN touch  knowrob_robcog/CATKIN_IGNORE

WORKDIR /home/ros
# Build the catkin workspace
RUN /opt/ros/kinetic/bin/catkin_make --debug

# ENTRYPOINT /opt/ros/kinetic/bin/roslaunch knowrob_roslog_launch knowrob_ease.launch
