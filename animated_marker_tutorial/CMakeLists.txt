cmake_minimum_required(VERSION 2.8.3)
project(animated_marker_tutorial)

find_package(catkin REQUIRED COMPONENTS rospy roslib animated_marker_msgs)

catkin_python_setup()

catkin_package(
)
