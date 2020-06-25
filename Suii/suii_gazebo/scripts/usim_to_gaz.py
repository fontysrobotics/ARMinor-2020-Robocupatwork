
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
		
		rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
		joint_names=[ 'shoulder_pan_joint', 'shoulder_lift_joint','elbow_joint','wrist_1_joint','wrist_2_joint','wrist_3_joint','ur3_mount_joint']
		self.joint_names = joint_names
		subscriber=rospy.Subscriber('joint_states1',JointState,self.callback1)
		self.client = actionlib.SimpleActionClient('/arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
		self._goal = FollowJointTrajectoryGoal()
		self.joints=0.0
		self.a=0
		self.b=0
		self.c=0
		self.d=0
		self.e=0
		self.f=0
		server_up = self.client.wait_for_server(timeout=rospy.Duration(3.0))
      		
   

	def callback1(self,data):
			self.joints=list(data.position)
			self.a=self.joints[0]
			self.b=self.joints[1]
			self.c=self.joints[2]
			self.d=self.joints[3]
			self.e=self.joints[4]
			self.f=self.joints[5]
	def goal(self):
		trajectory = JointTrajectory()
		trajectory.joint_names = self.joint_names
		trajectory.points.append(JointTrajectoryPoint())
		trajectory.points[0].positions = [self.a-pi,self.b+(pi/2),self.c,self.d,self.e,self.f,0]
		trajectory.points[0].time_from_start=rospy.Duration(0.001)
		goal = FollowJointTrajectoryGoal()
		goal.trajectory = trajectory
		goal.goal_time_tolerance = rospy.Duration(0.0)
		self.client.send_goal(goal)
		sucess=client.wait_for_result()
		while not(sucess):
			print(sucess)
tutorial=JointTrajectoryActionClient()
while True:
	tutorial.goal()

"""
0.012022725517097932, 0.08300607516512759, -0.0014655592794321493, 0.023586541841699393, -0.0006026959176050894, 0.0009635374878298464]
"""
