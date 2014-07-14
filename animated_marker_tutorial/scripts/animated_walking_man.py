#!/usr/bin/python

from animated_marker_msgs.msg import AnimatedMarkerArray
from animated_marker_tutorial import createAnimatedPersonMarker

from random import random
import rospy, math

rospy.init_node('animated_marker_publisher', anonymous=False)
publisher = rospy.Publisher("animated_markers", AnimatedMarkerArray)
rospy.loginfo("Publishing animated markers on /animated_markers topic...")
count = 0


#
# Randomly initialize some trajectories and publish person markers
#

positions = []
directions = []
velocities = []
colors = []
numPersons = 100

for i in xrange(0, numPersons):
    positions.append( (random() * 50 - 25, random() * 50 - 25 ))
    directions.append( random() * 2 * math.pi )
    velocities.append( random() * 1.5 )

    if random() > 0.5:
        c = (0.15, 0.9, 0.9)
    elif random() > 0.25:
        c = (0.9, 0.9, 0.15)
    else:
        c = (0.9, 0.15, 0.15)
    colors.append(c)


while not rospy.is_shutdown():
    markerArray = AnimatedMarkerArray()
    dt = 0.05

    for i in xrange(0, numPersons):
        positions[i] = (positions[i][0] + math.cos(directions[i]) * velocities[i] * dt, positions[i][1] + math.sin(directions[i]) * velocities[i] * dt)
        markerArray.markers.append( createAnimatedPersonMarker(i, pos=positions[i], thetaDeg=directions[i]*180.0/math.pi, color=colors[i], animationSpeed=velocities[i]) )

    publisher.publish(markerArray)
    rospy.sleep(dt)
