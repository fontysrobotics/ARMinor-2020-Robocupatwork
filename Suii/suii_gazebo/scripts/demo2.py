#!/usr/bin/env python
import rospy
import sys
import actionlib
from copy import copy
from control_msgs.msg import FollowJointTrajectoryAction,FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint, JointTrajectory
import geometry_msgs.msg
from math import pi
from sensor_msgs.msg import JointState
import std_msgs
import yaml
from std_msgs.msg import String
import math
import numpy as np
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from math import atan2
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Twist


class JointTrajectoryActionClient(object):
   
    def __init__(self):
        rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
        joint_names=[ 'shoulder_pan_joint', 'shoulder_lift_joint','elbow_joint','wrist_1_joint','wrist_2_joint','wrist_3_joint','ur3_mount_joint']
        self.joint_names = joint_names
        subscriber=rospy.Subscriber('joint_states1',JointState,self.callback1)
        self.pub = rospy.Publisher('/ur_driver/URScript', String, queue_size=10, latch=True)
        subscriber_0=rospy.Subscriber('joint_states',JointState,self.callback)
        self.client = actionlib.SimpleActionClient('/arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
        self._goal = FollowJointTrajectoryGoal()
        sub = rospy.Subscriber ('/odom', Odometry, self.get_rotation)
        self.pub1= rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.joints=0.0
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.e=0
        self.f=0
        self.joints_0=0.0
        self.a_0=0
        self.b_0=0
        self.c_0=0
        self.d_0=0
        self.e_0=0
        self.f_0=0
        self.g_0=0
        self.h_0=0
        self.yaw = 0
        self.cmd_msg = Twist()
        self.x=0
        server_up = self.client.wait_for_server(timeout=rospy.Duration(1.0))
        joint_names1=[ 'leftTilted_link','rightTilted_link']
        self.joint_names1 = joint_names1
        self.client1 = actionlib.SimpleActionClient('/gripper_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
        self._goal1 = FollowJointTrajectoryGoal()
        server_up1 = self.client.wait_for_server(timeout=rospy.Duration(1.0))

    def start(self):
        trajectory = JointTrajectory()
        trajectory.joint_names = self.joint_names
        trajectory.points.append(JointTrajectoryPoint())
        trajectory.points[0].positions = [self.a-pi,self.b+(pi/2),self.c,self.d,self.e,self.f,0]
        trajectory.points[0].time_from_start=rospy.Duration(0.001)
        goal = FollowJointTrajectoryGoal()
        goal.trajectory = trajectory
        goal.goal_time_tolerance = rospy.Duration(0.0)
        self.client.send_goal(goal)
        while True:
            list1=[self.a-pi,self.b+(pi/2),self.c,self.d,self.e,self.f,0]
            list2=[self.a_0,self.b_0,self.c_0,self.d_0,self.e_0,self.f_0,0]
            equal=0
            for i in range(7): 
                if (abs(list1[i]-list2[i])<0.1):
                    equal=equal+1
				
            if equal==7:
                break			
	
    def goal(self,state):
        if state==1:			
            send=self.buildMove("l","",[0.2641944885253906, -1.149320427571432, -1.4262059370623987,-1.968114201222555, 1.5591015815734863, 0.29005083441734314])
                
        else:
            send=self.buildMove("l","",[-1.7598956266986292, -1.733375374470846, -1.520839039479391,-1.455294434224264, 1.566258192062378, -0.19470006624330694])
        self.sendMove(send)	
        rospy.sleep(0.1)			
                
        while True:
            trajectory = JointTrajectory()
            trajectory.joint_names = self.joint_names
            trajectory.points.append(JointTrajectoryPoint())
            trajectory.points[0].positions = [self.a-pi,self.b+(pi/2),self.c,self.d,self.e,self.f,0]
            trajectory.points[0].time_from_start=rospy.Duration(0.001)
            goal = FollowJointTrajectoryGoal()
            goal.trajectory = trajectory
            goal.goal_time_tolerance = rospy.Duration(0.0)
            self.client.send_goal(goal)
            list1=[self.a-pi,self.b+(pi/2),self.c,self.d,self.e,self.f,0]
            list2=[self.a_0,self.b_0,self.c_0,self.d_0,self.e_0,self.f_0,0]
            equal=0
            for i in range(7):
                
                if (abs(list1[i]-list2[i])<0.1):
                    equal=equal+1
                        
            if equal==7:
                break	

        if state==1:
            self.goal_gripper("close")
        else:
            self.goal_gripper("open")

    def move(self,x, y, rz):
	    self.cmd_msg.linear.x = x
	    self.cmd_msg.linear.y = y
	    self.cmd_msg.angular.z = rz
	    self.pub1.publish(self.cmd_msg)
			
    def goal_gripper(self,pos):
        if pos=="close":
            self.a2=-1.6
            self.b2=1.6
        else:
            self.a2=0
            self.b2=0

        trajectory = JointTrajectory()
        trajectory.joint_names = self.joint_names1
        trajectory.points.append(JointTrajectoryPoint())
        trajectory.points[0].positions = [self.a2,self.b2]
        trajectory.points[0].time_from_start=rospy.Duration(0.001)
        goal = FollowJointTrajectoryGoal()
        goal.trajectory = trajectory
        goal.goal_time_tolerance = rospy.Duration(0.0)
        self.client1.send_goal(goal)
              
        while True:
            if abs(self.g_0-self.a2)<0.01 and abs(self.h_0-self.b2)<0.01:
                break
    
    def buildMove(self, moveType, space, pose, radius=0):
        if moveType == "j":
            acceleration = 3
            speed = 0.75
        else:
            acceleration = 1.2  #Joint acceleration in rad/s^2
            speed = 0.3 #Joint speed in rad/s
        time = 0 #Time the move must take
        array = pose
        sendable = "move%s(%s%s, a=%s, v=%s, t=%s, r=%s)"%(moveType, space, array, acceleration, speed, time, radius)
        return sendable

    def sendMove(self, string):
        st = String()        
        st.data = string
        self.pub.publish(st)
        print st.data

    def callback(self,data):
        self.joints_0=list(data.position)
        self.a_0=self.joints_0[8]
        self.b_0=self.joints_0[7]
        self.c_0=self.joints_0[0]
        self.d_0=self.joints_0[10]
        self.e_0=self.joints_0[11]
        self.f_0=self.joints_0[12]
        self.g_0=self.joints_0[2]
        self.h_0=self.joints_0[5]

    def callback1(self,data):
        self.joints=list(data.position)
        self.a=self.joints[0]
        self.b=self.joints[1]
        self.c=self.joints[2]
        self.d=self.joints[3]
        self.e=self.joints[4]
        self.f=self.joints[5]
        
    def get_rotation (self,msg):
        orient = msg.pose.pose.orientation
        orientations = [orient.x, orient.y, orient.z, orient.w]
        (roll, pitch, yaw_robot) = euler_from_quaternion (orientations)
        self.yaw=yaw_robot
        pos=msg.pose.pose.position
        self.x=pos.x
        self.y=pos.y

		
tutorial=JointTrajectoryActionClient()
tutorial.move(1,0,0)
rospy.sleep(0.8)
tutorial.move(0,1,0)
rospy.sleep(0.8)
tutorial.move(0,0,1)
rospy.sleep(0.8)
tutorial.move(0,0,0)
tutorial.start()
print("started")
rospy.sleep(0.3)
tutorial.goal(1)
print("first movement completed")
rospy.sleep(0.3)
tutorial.goal(2)
print("second movement completed")		
