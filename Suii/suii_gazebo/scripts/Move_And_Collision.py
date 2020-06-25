import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
from sensor_msgs.msg import LaserScan

roll = 0
pitch = 0
cmd_msg = Twist()
rotation = 0

collision_detected = False
collision_distance = 0.07
long_distance = 0.56
short_distance = 0.42


def Sensor_Front_callback(msg):
    global collision_detected
    for i in range(len(msg.ranges)):
        if (msg.ranges[i] < collision_distance) and (msg.ranges[i] > 0):
            collision_detected = True
    for i in range(40, 50):
        if (msg.ranges[i] < short_distance) and (msg.ranges[i] > 0):
            collision_detected = True
    for i in range(15):
        if (msg.ranges[1060 + i] < long_distance) and (msg.ranges[1060 + i] > 0):
            collision_detected = True

def Sensor_Back_callback(msg):
    global collision_detected
    for i in range(len(msg.ranges)):
        if (msg.ranges[i] < collision_distance) and (msg.ranges[i] > 0):
            collision_detected = True
    for i in range(20):
        if (msg.ranges[i] < short_distance) and (msg.ranges[i] > 0):
            collision_detected = True
    for i in range(15):
        if (msg.ranges[1060 + i] < long_distance) and (msg.ranges[1060 + i] > 0):
            collision_detected = True


def get_rotation(msg):
    global roll, pitch
    orient = msg.pose.pose.orientation
    orientations = [orient.x, orient.y, orient.z, orient.w]
    (roll, pitch, yaw_robot) = euler_from_quaternion(orientations)


def move(x, y, rz):
    global cmd_msg
    cmd_msg.linear.x = x
    cmd_msg.linear.y = y
    cmd_msg.angular.z = rz
    pub.publish(cmd_msg)


rospy.init_node('Move_Collsion')
sub = rospy.Subscriber('/odom', Odometry, get_rotation)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.Subscriber("/suii/laser/scan_front", LaserScan, Sensor_Front_callback)
rospy.Subscriber("/suii/laser/scan_back", LaserScan, Sensor_Back_callback)

while collision_detected is False:
    move(0.5, 0, 0)

rospy.loginfo("Collision")
move(0, 0, 0)

move(-0.5, 0, 0)
rospy.sleep(0.5)
collision_detected = False
while collision_detected is False:
    move(-0.5, 0.5, 0)

rospy.loginfo("Collision")
move(0, 0, 0)

rospy.spin()
