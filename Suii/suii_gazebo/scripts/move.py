import rospy
from math import atan2
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler

roll = 0
pitch = 0
cmd_msg = Twist()
rotation = 0

def get_rotation (msg):
    global roll, pitch
    orient = msg.pose.pose.orientation
    orientations = [orient.x, orient.y, orient.z, orient.w]
    (roll, pitch, yaw_robot) = euler_from_quaternion (orientations)

def move(x, y, rz):
    global cmd_msg
    cmd_msg.linear.x = x
    cmd_msg.linear.y = y
    cmd_msg.angular.z = rz
    speed = 1
    pub.publish(cmd_msg)

rospy.init_node('move')

sub = rospy.Subscriber ('/odom', Odometry, get_rotation)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

while not rospy.is_shutdown():
    move(0, 1, 1)

move(0, 0, 0)