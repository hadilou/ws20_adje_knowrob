#!/bin/bash

ROS_DISTRO=melodic
TAG=master
IMAGE_NAME=iki-onto

DOCKER_BASE_IMAGE=fbe-dockerreg.rwu.de/prj-iki-robotics/orga/ros-docker-base
FULL_IMAGE_NAME="$IMAGE_NAME:${TAG}"
docker build --no-cache --build-arg ROS_DISTRO=$ROS_DISTRO --build-arg DOCKER_BASE_IMAGE=$DOCKER_BASE_IMAGE -t $FULL_IMAGE_NAME -f docker/Dockerfile .
