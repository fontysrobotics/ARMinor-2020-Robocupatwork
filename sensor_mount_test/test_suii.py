#!/usr/bin/env python

import rospy


from nav_msgs.msg import Odometry
from geometry_msgs.msg import *
from tf.transformations import euler_from_quaternion
import math
rospy.init_node('Steering', anonymous=False) 
cmd_vel = rospy.Publisher('cmd_vel', Twist,queue_size=0)
move_cmd = Twist()
i=0
while True:
	move_cmd.angular.z = 0.0
	move_cmd.linear.x = 2.0
	cmd_vel.publish(move_cmd)
	
