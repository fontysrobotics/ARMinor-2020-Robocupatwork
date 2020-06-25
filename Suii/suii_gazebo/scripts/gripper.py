
import rospy
import sys
import actionlib
from copy import copy
from control_msgs.msg import FollowJointTrajectoryAction,FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint, JointTrajectory
import geometry_msgs.msg
from math import pi
from sensor_msgs.msg import JointState
class JointTrajectoryActionClient(object):
   
        def __init__(self):
		
		rospy.init_node('move_group_python_interface_tutorial1', anonymous=True)
		joint_names=[ 'leftTilted_link','rightTilted_link']
		self.joint_names = joint_names
		self.client = actionlib.SimpleActionClient('/gripper_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
		self._goal = FollowJointTrajectoryGoal()
		server_up = self.client.wait_for_server(timeout=rospy.Duration(3.0))
      		
   

	
	def goal(self):
		trajectory = JointTrajectory()
		trajectory.joint_names = self.joint_names
		trajectory.points.append(JointTrajectoryPoint())
		trajectory.points[0].positions = [0,0]
		trajectory.points[0].time_from_start=rospy.Duration(0.001)
		goal = FollowJointTrajectoryGoal()
		goal.trajectory = trajectory
		goal.goal_time_tolerance = rospy.Duration(0.0)
		self.client.send_goal(goal)
tutorial=JointTrajectoryActionClient()
tutorial.goal()
"""
close=[-1.6,1.6]
open=[0,0]
"""
