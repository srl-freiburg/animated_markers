from animated_marker_msgs.msg import AnimatedMarker
from geometry_msgs.msg import Quaternion, Point
import rospy, tf, math

def createAnimatedPersonMarker(markerId, pos, thetaDeg, animationSpeed = 1.0, color=(1, 1, 1) ):
    marker = AnimatedMarker()
    marker.header.frame_id = "map"
    marker.header.stamp = rospy.Time.now()
    marker.id = markerId

    marker.pose.position = Point(pos[0], pos[1], 0)

    # Rotation is required because mesh model uses different coordinate system convention
    q = tf.transformations.quaternion_from_euler(math.pi / 2, 0, (thetaDeg + 90) / 180.0 * math.pi)
    marker.pose.orientation = Quaternion(q[0], q[1], q[2], q[3])

    marker.color.a = 1.0
    marker.color.r = color[0]
    marker.color.g = color[1]
    marker.color.b = color[2]

    marker.mesh_use_embedded_materials = True
    marker.type = AnimatedMarker.MESH_RESOURCE

    marker.mesh_resource = "package://animated_marker_tutorial/meshes/animated_walking_man.mesh"

    personModelScaleFactor = 2.0 / 7.0 * 1.8
    marker.scale.x = marker.scale.y = marker.scale.z = personModelScaleFactor

    marker.animation_speed = 0.7 * animationSpeed;

    return marker