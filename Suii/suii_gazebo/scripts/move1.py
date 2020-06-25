#!/usr/bin/env python
import sys
import rospy
import std_msgs
import yaml
from std_msgs.msg import String
import math
import numpy as np
from tf.transformations import quaternion_from_euler, euler_from_quaternion

class SendMove(object):
    def __init__(self):
      rospy.init_node("Manipulation")
      self.pub = rospy.Publisher('/ur_driver/URScript', String, queue_size=10, latch=True)
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
		while True:
			self.pub.publish(st)
			print st.data
a=SendMove()
send=a.buildMove("l","",[1.95358407497406, -1.367486302052633, -1.8214100042926233,
  -1.5385006109820765, 1.593897819519043, 1.953194260597229])

a.sendMove(send)
"""
HOLDER_2: !!python/tuple [1.95358407497406, -1.367486302052633, -1.8214100042926233,
  -1.5385006109820765, 1.593897819519043, 1.953194260597229]
HOLDER_3: !!python/tuple [2.4572057723999023, -1.3655450979815882, -1.8129380385028284,
  -1.5279067198382776, 1.596914529800415, 1.7027243375778198]
preHOLDER_2: !!python/tuple [1.951616883277893, -1.567681614552633, -0.8820589224444788,
  -2.2774680296527308, 1.5898520946502686, 1.9575130939483643]
preHOLDER_3: !!python/tuple [2.455453872680664, -1.5089200178729456, -1.0514186064349573,
  -2.146038834248678, 1.5932154655456543, 1.7060338258743286]
safetyStop: !!python/tuple [0.2641944885253906, -1.149320427571432, -1.4262059370623987,
  -1.968114201222555, 1.5591015815734863, 0.29005083441734314]
scanPosition0: !!python/tuple [-1.5726707617389124, -0.2505281607257288, -2.4049914518939417,
  -1.4284794966327112, 1.645344614982605, 0.002140682190656662]
scanPosition1: !!python/tuple [-1.1948736349688929, -1.536114517842428, -1.7314227263080042,
  -1.4448488394366663, 1.565421462059021, 0.3703279197216034]
scanPosition10: !!python/tuple [-1.1949856917010706, -1.73171312013735, -0.7169807592975062,
  -2.263690773640768, 1.5654211044311523, 0.3702165484428406]
scanPosition11: !!python/tuple [-0.7321270147906702, -2.052906338368551, -0.23272687593568975,
  -2.4291520754443567, 1.5659847259521484, 0.8330811858177185]
scanPosition12: !!python/tuple [-1.7598956266986292, -2.03199273744692, -0.27320605913271123,
  -2.404308859501974, 1.566258430480957, -0.19469958940614873]
scanPosition13: !!python/tuple [-0.9365142027484339, -1.373042408620016, -0.781506363545553,
  -2.5592101255999964, 1.565598487854004, 0.6286923289299011]
scanPosition14: !!python/tuple [-0.38008147874941045, -1.6840718428241175, -0.49528676668276006,
  -2.5369389692889612, 1.5671061277389526, 1.1851288080215454]
scanPosition15: !!python/tuple [-1.8577559630023401, -1.6698673407184046, -0.5175078550921839,
  -2.521703068410055, 1.5665615797042847, -0.29255992570985967]
scanPosition16: !!python/tuple [-1.1703909079181116, -1.9085772673236292, -0.1653674284564417,
  -2.6385722796069544, 1.565422534942627, 0.3948124647140503]
scanPosition2: !!python/tuple [-0.732126537953512, -1.7389510313617151, -1.512082878743307,
  -1.4637520948993128, 1.5659854412078857, 0.833081066608429]
scanPosition3: !!python/tuple [-1.7598956266986292, -1.733375374470846, -1.520839039479391,
  -1.455294434224264, 1.566258192062378, -0.19470006624330694]
scanPosition4: !!python/tuple [-1.1949852148639124, -1.530872646962301, -1.5484793821917933,
  -1.633033577595846, 1.565421462059021, 0.370216965675354]
scanPosition5: !!python/tuple [-0.732126537953512, -1.7363360563861292, -1.3273080031024378,
  -1.6511419455157679, 1.5659855604171753, 0.8330813646316528]
scanPosition6: !!python/tuple [-1.7598956266986292, -1.7302306334124964, -1.336663071309225,
  -1.6426146666156214, 1.5662583112716675, -0.19470006624330694]
scanPosition7: !!python/tuple [-1.1949852148639124, -1.5683444182025355, -1.2729976812945765,
  -1.8710430304156702, 1.565421223640442, 0.3702166676521301]
scanPosition8: !!python/tuple [-0.6503284613238733, -1.9019110838519495, -0.8726065794574183,
  -1.9406526724444788, 1.5661969184875488, 0.9148799180984497]
scanPosition9: !!python/tuple [-1.884749714528219, -1.8926766554461878, -0.8881195227252405,
  -1.928169075642721, 1.566652774810791, -0.3195551077472132]
startCali: !!python/tuple [-1.6191533247577112, -1.5828002134906214, -1.501429859791891,
  -1.6275013128863733, 1.5641525983810425, -0.0528486410724085]
tempScan: !!python/tuple [-1.6106727758990687, -1.8514307180987757, -1.1873992125140589,
  -1.6735780874835413, 1.563003659248352, -0.04381925264467412]
"""
