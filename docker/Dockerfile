ARG ROS_DISTRO=melodic

#available locally, change to docker registry if needed
#you need a ros docker image, this one here is local
ARG DOCKER_BASE_IMAGE=ros-docker-base

FROM $DOCKER_BASE_IMAGE:$ROS_DISTRO

ARG ROS_DISTRO

# to avoid race-conditions, when starting some containers with rancher or docker-compose:
ENV WAIT_FOR_ROSCORE 1
ENV WAIT_FOR_CONFIG_MANAGER 0
ENV ROS_DISTRO $ROS_DISTRO
ENV ROS_MASTER_URI http://localhost:11311
ENV ROS_IP 127.0.0.1



MAINTAINER kadeyoadje@gmail.com

# set shell
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN echo "192.168.0.182	tiago-66c" >> /etc/hosts

WORKDIR /root/catkin_ws

RUN apt-get clean



RUN apt-get update --fix-missing -y && \
	apt-get upgrade -y && \
    apt-get install -y ros-$ROS_DISTRO-urdf &&\
	apt-get install -y python3-pip &&\
	apt-get install -y openjdk-8-jre
    
RUN pip3 install rospkg
RUN pip3 install Owlready2
RUN pip3 install PyYAML


RUN rosdep update

WORKDIR /root/catkin_ws/src/

RUN git clone git@github.com:hadilou/ws20_adje_knowrob.git
RUN rm -rf ws20_adje_knowrob/docker

WORKDIR /root/catkin_ws

# build
RUN source /opt/ros/$ROS_DISTRO/setup.bash && \
	rosdep install -y -r -i --from-paths src --ignore-src --rosdistro $ROS_DISTRO && \
	catkin_make

WORKDIR /root/catkin_ws/src/ws20_adje_knowrob

##pip3
##java run time

#Owlready2
#yaml
#roskpg

